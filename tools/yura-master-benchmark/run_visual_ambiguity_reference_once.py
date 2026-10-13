from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
LEGACY_CONFIG_PATH = TOOL_DIR / "config.json"
RUNS_DIR_REL = Path("tools/yura-master-benchmark/runs/visual_ambiguity_reference")

MASTER_IMAGE = "visuals/yura/identity/master/YURA_VISUAL_MASTER.png"
FACE_IMAGE = "visuals/yura/identity/face/YURA_FACE_REFERENCE.png"

EXPECTED_IMAGE_SHA256 = {
    MASTER_IMAGE: "81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d",
    FACE_IMAGE: "3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030",
}

TEXT_SOURCES = [
    "visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md",
    "visuals/yura/identity/face/FACE_REFERENCE_RULES.md",
    "visuals/yura/identity/face/YURA_FACE_MASTER_PHASE_PLAN_20261013.md",
    "visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md",
    "tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md",
]

DENIED_SOURCES = [
    "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png",
    "visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md",
    "old YURA Master images",
    "Test 5/6 output images",
    "past generated YURA candidates",
    "characters/YURA.md",
    "story/**",
    "manuscript/**",
    "Memory-derived YURA appearance",
    "Git-history fallback visual files",
]

VIEW_INSTRUCTIONS = {
    "FRONT": (
        "Straight-on front view. Head and torso face the camera. Keep shoulders level and neutral. "
        "Do not force ears out from behind the hair."
    ),
    "FRONT_3Q": (
        "Front three-quarter view, approximately 30 to 45 degrees yaw. Head and torso share the same "
        "natural rotation. Near/far ear visibility may differ naturally."
    ),
    "SIDE": (
        "True side/profile view, approximately 90 degrees yaw. Head and torso share the same rotation. "
        "The ear region may be readable, but hair must not be moved merely to expose it."
    ),
    "REAR_3Q": (
        "Rear three-quarter view, approximately 135 degrees yaw. Prioritize a natural rear hair mass, "
        "side-layer ordering, neck overlap, and shoulder overlap. Do not fan the hair outward to reveal layers."
    ),
    "BACK": (
        "True back view, approximately 180 degrees. Do not turn the face back toward camera. Show a natural "
        "rear hair mass, neck/shoulder/back overlap, and the super-long endpoint near the waist."
    ),
}

REQUIRED_PROMPT_INVARIANTS = [
    "DIAGNOSTIC / CANDIDATE ONLY",
    "FACE REFERENCE DOES NOT DEFINE BODY SCALE",
    "NO VISIBILITY COMPENSATION",
    "DO NOT INVENT HIDDEN 3D GEOMETRY AS CANONICAL",
    "EAR ACTUAL HEIGHT TARGET = 20–22% OF FACE VERTICAL DIMENSION",
    "EAR HARD MAX = 23%",
    "SUPER-LONG HAIR MUST CLEARLY REACH THE WAIST AREA",
    "STRUCTURAL CONSISTENCY + IDENTITY CONSISTENCY + VISUAL NATURALNESS",
]


def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        capture_output=True,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\n"
            f"STDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    return proc


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def jsonable(obj: Any) -> Any:
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    return obj


def build_prompt(view: str) -> str:
    view_instruction = VIEW_INSTRUCTIONS[view]
    return f"""YURA visual ambiguity diagnostic reference generation.

STATUS: DIAGNOSTIC / CANDIDATE ONLY.
This output is not Visual Authority and must not silently promote unresolved geometry.

Use image 1 ({MASTER_IMAGE}) as the formal full-body visual baseline for YURA's established overall appearance, silver-white primarily straight super-long hair, and natural body context.
Use image 2 ({FACE_IMAGE}) for Face Identity and face-local geometry only.
FACE REFERENCE DOES NOT DEFINE BODY SCALE, head-to-body ratio, full-body size, or canvas occupancy.
The current Face Reference contains a known ear-longation defect; do not treat its current ear length as the corrected target.

Requested view: {view}
{view_instruction}

Fixed diagnostic framing:
- one YURA only
- waist-up reference image
- entire head visible
- waist region visible so the hair endpoint can be judged
- neutral upright posture
- neutral calm expression when the face is visible
- eye-level camera
- minimal perspective distortion
- plain unobtrusive background
- no dramatic pose
- no added accessories
- no wind or artificial hair-flare effect

Face identity:
Preserve the approved Face Identity: compact soft oval face, short midface, compact lower face, soft small chin, delicate blue-gray anime eyes, small understated mouth, silver-white face-framing hair identity.
Do not redesign the face to satisfy any BODY proportion.

Ear rule:
EAR ACTUAL HEIGHT TARGET = 20–22% OF FACE VERTICAL DIMENSION.
EAR HARD MAX = 23%.
Ears should be relatively small, naturally placed close to the side of the head, and low in visual prominence.
Natural partial or near-complete hair occlusion is valid.
NO VISIBILITY COMPENSATION.
Do not enlarge, elongate, widen, move outward, rotate toward camera, or push an ear outside the hair merely to make it visible.
Do not move natural hair behind an ear merely to expose it.
Do not force equal left/right ear visibility.

Hair rule:
Hair is silver-white, primarily straight, with light bangs and natural narrow face-framing locks.
SUPER-LONG HAIR MUST CLEARLY REACH THE WAIST AREA.
The intended extension relative to the formal full-body Master is modest only; do not extend substantially below the waist.
For rear-oriented views, generate only a natural diagnostic hypothesis for rear mass/layering consistent with the approved visible identity.
DO NOT INVENT HIDDEN 3D GEOMETRY AS CANONICAL.
Do not fan, spread, lift, or separate rear hair merely to expose hidden structure.

Ambiguity rule:
Keep ACTUAL/STRUCTURAL GEOMETRY, VISIBLE GEOMETRY, OCCLUSION/LAYER ORDER, and VIEW conceptually separate.
Low visibility alone is not a defect.
The visual target is STRUCTURAL CONSISTENCY + IDENTITY CONSISTENCY + VISUAL NATURALNESS, not maximal visibility.

Rendering:
High-quality clean 2D anime reference rendering, consistent with the supplied YURA references. Avoid photorealism, semi-realism, 3D CGI, and exaggerated stylization drift.
"""


def validate_prompt(prompt: str) -> None:
    missing = [value for value in REQUIRED_PROMPT_INVARIANTS if value not in prompt]
    if missing:
        raise RuntimeError("prompt invariant failure: " + "; ".join(missing))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate one YURA diagnostic ambiguity reference view."
    )
    parser.add_argument("--view", required=True, choices=list(VIEW_INSTRUCTIONS))
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Perform all source/hash/prompt checks and exit before any paid Image API call.",
    )
    args = parser.parse_args()
    view = args.view

    root = Path(run(["git", "rev-parse", "--show-toplevel"], TOOL_DIR).stdout.strip())
    run(["git", "fetch", "origin", "main"], root)
    head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
    origin_main = run(["git", "rev-parse", "origin/main"], root).stdout.strip()
    if head != origin_main:
        raise RuntimeError(f"HEAD must equal current origin/main: HEAD={head} origin/main={origin_main}")

    required_paths = [MASTER_IMAGE, FACE_IMAGE, *TEXT_SOURCES]
    dirty = run(["git", "status", "--porcelain", "--", *required_paths], root).stdout.strip()
    if dirty:
        raise RuntimeError("Required source files have uncommitted changes:\n" + dirty)

    source_hashes: dict[str, str] = {}
    for rel in required_paths:
        path = root / rel
        if not path.exists():
            raise RuntimeError(f"required source missing: {rel}")
        source_hashes[rel] = sha256_file(path)

    for rel, expected in EXPECTED_IMAGE_SHA256.items():
        actual = source_hashes[rel]
        if actual.lower() != expected.lower():
            raise RuntimeError(
                f"exact image SHA256 mismatch: {rel}: expected={expected} actual={actual}"
            )

    prompt = build_prompt(view)
    validate_prompt(prompt)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = root / RUNS_DIR_REL / f"{stamp}_{view.lower()}"
    suffix = 1
    while run_dir.exists():
        run_dir = root / RUNS_DIR_REL / f"{stamp}_{view.lower()}_{suffix:02d}"
        suffix += 1
    run_dir.mkdir(parents=True)

    (run_dir / "compiled_prompt.txt").write_text(prompt, encoding="utf-8")
    (run_dir / "source_hashes.json").write_text(
        json.dumps(source_hashes, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    preflight = {
        "status": "PREFLIGHT_OK",
        "visual_status": "DIAGNOSTIC / CANDIDATE ONLY",
        "view": view,
        "git_commit": head,
        "paid_model_calls": 0 if args.preflight_only else None,
        "image_reference_order": [MASTER_IMAGE, FACE_IMAGE],
        "denied_sources": DENIED_SOURCES,
        "source_sha256": source_hashes,
        "prompt_invariants": REQUIRED_PROMPT_INVARIANTS,
        "ear_known_defect_not_promoted": True,
        "rear_hair_unverified_not_promoted": True,
    }
    (run_dir / "preflight.json").write_text(
        json.dumps(preflight, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if args.preflight_only:
        print(json.dumps({**preflight, "run_dir": str(run_dir)}, ensure_ascii=False, indent=2))
        return 0

    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for Image API execution")

    # Reuse only the already-working Image API transport settings from the legacy benchmark config.
    # No Test 5 authority order, Body Guide, body QA, pelvis/inseam gate, or composition gate is imported.
    legacy_cfg = json.loads(LEGACY_CONFIG_PATH.read_text(encoding="utf-8"))
    image_cfg = legacy_cfg["image_api"]

    from openai import OpenAI

    client = OpenAI()
    refs = [open(root / MASTER_IMAGE, "rb"), open(root / FACE_IMAGE, "rb")]
    try:
        result = client.images.edit(
            model=image_cfg["model"],
            image=refs,
            prompt=prompt,
            size=image_cfg["size"],
            quality=image_cfg["quality"],
            output_format="png",
            background=image_cfg["background"],
            n=1,
        )
    finally:
        for file_obj in refs:
            file_obj.close()

    if not result.data or not result.data[0].b64_json:
        raise RuntimeError("Image API returned no image")

    output_path = run_dir / f"yura_ambiguity_{view.lower()}_diagnostic.png"
    output_path.write_bytes(base64.b64decode(result.data[0].b64_json))
    output_sha256 = sha256_file(output_path)

    response = jsonable(result)
    for item in response.get("data", []):
        if "b64_json" in item:
            item["b64_json"] = f"<saved to {output_path.name}>"
    (run_dir / "image_response.json").write_text(
        json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    result_meta = {
        "status": "GENERATED_DIAGNOSTIC_CANDIDATE",
        "authority_promotion": "NO",
        "view": view,
        "git_commit": head,
        "output_path": str(output_path),
        "output_sha256": output_sha256,
        "ear_known_defect_not_promoted": True,
        "rear_hair_unverified_not_promoted": True,
        "next": "Review route/view behavior. Do not promote this image to Authority before ear and rear-hair correction phases.",
    }
    (run_dir / "result_meta.json").write_text(
        json.dumps(result_meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(result_meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
