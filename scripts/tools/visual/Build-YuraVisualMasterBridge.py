#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
from pathlib import Path
from textwrap import wrap

from PIL import Image


SOURCE_DEFAULT = Path("docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png")
OUTPUT_DEFAULT = Path("docs/assistant-context/creation/yura/identity/master/bridge")
BASE64_LINE_WIDTH = 76
# Generated bridge artifacts are UTF-8 text by design so connector-only chats can recover them.


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def encode_jpeg_under_limit(image: Image.Image, *, max_edge: int, target_bytes: int) -> tuple[bytes, tuple[int, int], int]:
    image = image.convert("RGB")
    image.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)

    for quality in (88, 84, 80, 76, 72, 68, 64, 60):
        buf = io.BytesIO()
        image.save(buf, format="JPEG", quality=quality, optimize=True, progressive=True, subsampling="4:2:0")
        payload = buf.getvalue()
        if len(payload) <= target_bytes:
            return payload, image.size, quality

    while max(image.size) > 320:
        image.thumbnail((int(image.width * 0.9), int(image.height * 0.9)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        image.save(buf, format="JPEG", quality=60, optimize=True, progressive=True, subsampling="4:2:0")
        payload = buf.getvalue()
        if len(payload) <= target_bytes:
            return payload, image.size, 60

    raise RuntimeError(f"Could not encode preview under {target_bytes} bytes")


def write_base64_text(path: Path, payload: bytes) -> None:
    encoded = base64.b64encode(payload).decode("ascii")
    path.write_text("\n".join(wrap(encoded, BASE64_LINE_WIDTH)) + "\n", encoding="utf-8", newline="\n")


def build(source: Path, output_dir: Path) -> None:
    source_bytes = source.read_bytes()
    source_sha256 = sha256_bytes(source_bytes)
    source_blob_sha1 = git_blob_sha1(source_bytes)

    with Image.open(io.BytesIO(source_bytes)) as im:
        im.load()
        source_size = im.size

        full_payload, full_size, full_quality = encode_jpeg_under_limit(
            im.copy(), max_edge=960, target_bytes=90000
        )

        w, h = im.size
        portrait_crop = im.crop(
            (
                int(w * 0.18),
                0,
                int(w * 0.82),
                int(h * 0.40),
            )
        )
        portrait_payload, portrait_size, portrait_quality = encode_jpeg_under_limit(
            portrait_crop, max_edge=720, target_bytes=70000
        )

    output_dir.mkdir(parents=True, exist_ok=True)

    full_b64 = output_dir / "FULL.jpg.b64.txt"
    portrait_b64 = output_dir / "PORTRAIT.jpg.b64.txt"
    write_base64_text(full_b64, full_payload)
    write_base64_text(portrait_b64, portrait_payload)

    manifest = {
        "format_version": 1,
        "role": "non-authoritative text transport bridge for ChatGPT visual recovery",
        "authority": "VISUAL_MASTER.png remains the canonical visual artifact; bridge files are cache only",
        "source": {
            "path": str(source).replace("\\", "/"),
            "bytes": len(source_bytes),
            "width": source_size[0],
            "height": source_size[1],
            "sha256": source_sha256,
            "git_blob_sha1": source_blob_sha1,
        },
        "base64_line_width": BASE64_LINE_WIDTH,
        "previews": [
            {
                "name": "full",
                "base64_path": str(full_b64).replace("\\", "/"),
                "mime_type": "image/jpeg",
                "decoded_bytes": len(full_payload),
                "decoded_sha256": sha256_bytes(full_payload),
                "width": full_size[0],
                "height": full_size[1],
                "jpeg_quality": full_quality,
                "purpose": "whole-character identity / body / hair / overall-balance visual recovery",
            },
            {
                "name": "portrait",
                "base64_path": str(portrait_b64).replace("\\", "/"),
                "mime_type": "image/jpeg",
                "decoded_bytes": len(portrait_payload),
                "decoded_sha256": sha256_bytes(portrait_payload),
                "width": portrait_size[0],
                "height": portrait_size[1],
                "jpeg_quality": portrait_quality,
                "purpose": "face / eye / upper-hair visual recovery; protected text specs still own exact micro-details",
            },
        ],
    }

    manifest_path = output_dir / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    readme = f"""# YURA Visual Master Bridge

Status: GENERATED / NON-AUTHORITATIVE TRANSPORT CACHE

Canonical source:

`{manifest['source']['path']}`

Source Git blob SHA-1 at generation:

`{source_blob_sha1}`

Source SHA-256 at generation:

`{source_sha256}`

## Purpose

The GitHub connector can identify the canonical PNG but may not expose binary repository content as a visual input. These UTF-8 Base64 files provide a transport bridge that can be fetched as text, decoded locally, and visually inspected without asking the user to re-upload the MASTER in every chat.

The bridge never becomes authority. `VISUAL_MASTER.png` plus protected domain specifications remain authoritative.

## Required recovery procedure

1. Confirm the current Git blob SHA of `VISUAL_MASTER.png`.
2. Read `MANIFEST.json`.
3. Use the bridge only when `source.git_blob_sha1` matches the current MASTER blob SHA.
4. Fetch and concatenate all lines of the required `.b64.txt` file.
5. Base64-decode it to JPEG.
6. Verify the decoded SHA-256 against the manifest before visual inspection.
7. Use the full preview for whole-character cross-check and the portrait preview for face / eye / upper-hair cross-check.
8. Exact BODY / FACE / EYE / HAIR / RENDERING decisions remain owned by their protected text specifications.

If the source SHA does not match, treat the bridge as stale and do not use it.

## Generation

Generated by:

`scripts/tools/visual/Build-YuraVisualMasterBridge.py`

Do not hand-edit generated bridge files.
"""
    (output_dir / "README.md").write_text(readme, encoding="utf-8", newline="\n")


def verify(source: Path, output_dir: Path) -> None:
    manifest_path = output_dir / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source_bytes = source.read_bytes()

    expected_source_sha256 = manifest["source"]["sha256"]
    expected_blob_sha1 = manifest["source"]["git_blob_sha1"]
    actual_source_sha256 = sha256_bytes(source_bytes)
    actual_blob_sha1 = git_blob_sha1(source_bytes)

    if actual_source_sha256 != expected_source_sha256:
        raise SystemExit(f"source SHA-256 mismatch: expected {expected_source_sha256}, got {actual_source_sha256}")
    if actual_blob_sha1 != expected_blob_sha1:
        raise SystemExit(f"source Git blob SHA-1 mismatch: expected {expected_blob_sha1}, got {actual_blob_sha1}")

    for preview in manifest["previews"]:
        b64_path = Path(preview["base64_path"])
        encoded = "".join(b64_path.read_text(encoding="utf-8").splitlines())
        decoded = base64.b64decode(encoded, validate=True)
        actual = sha256_bytes(decoded)
        if actual != preview["decoded_sha256"]:
            raise SystemExit(f"preview SHA-256 mismatch for {preview['name']}: expected {preview['decoded_sha256']}, got {actual}")

    print("YURA visual master bridge verification: PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build or verify the YURA visual-master text transport bridge.")
    parser.add_argument("--source", type=Path, default=SOURCE_DEFAULT)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()

    if args.verify_only:
        verify(args.source, args.output_dir)
    else:
        build(args.source, args.output_dir)
        verify(args.source, args.output_dir)


if __name__ == "__main__":
    main()
