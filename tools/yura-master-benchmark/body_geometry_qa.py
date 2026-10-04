from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_image_size(path: Path) -> tuple[int, int]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required. Run: python -m pip install -r tools/yura-master-benchmark/requirements.txt"
        ) from exc
    with Image.open(path) as image:
        return int(image.width), int(image.height)


def validate_landmarks(
    crown_y: float,
    chin_y: float,
    soles_y: float,
    image_height: int,
) -> None:
    if not (0 <= crown_y < chin_y < soles_y <= image_height):
        raise RuntimeError(
            "Landmarks must satisfy 0 <= crown_y < chin_y < soles_y <= image_height"
        )
    if chin_y - crown_y < 1.0:
        raise RuntimeError("Head height is too small to measure")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Record numeric RAW Body Geometry QA from manually reviewed crown/chin/soles Y landmarks. "
            "This does not alter the image."
        )
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--crown-y", type=float, required=True)
    parser.add_argument("--chin-y", type=float, required=True)
    parser.add_argument("--soles-y", type=float, required=True)
    parser.add_argument(
        "--confirm-landmarks-reviewed",
        action="store_true",
        help="Required: confirms the three Y landmarks were visually reviewed on result_raw.png.",
    )
    args = parser.parse_args()

    if not args.confirm_landmarks_reviewed:
        raise RuntimeError(
            "Refusing to record Body Geometry QA without --confirm-landmarks-reviewed"
        )

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    qa_cfg: dict[str, Any] = config.get("body_geometry_qa") or {}
    if qa_cfg.get("enabled") is not True:
        raise RuntimeError("body_geometry_qa must be enabled in config.json")
    if qa_cfg.get("landmark_method") != "MANUAL_PIXEL_Y":
        raise RuntimeError("body_geometry_qa landmark_method must be MANUAL_PIXEL_Y")

    run_dir = args.run_dir.resolve()
    raw_name = str(qa_cfg.get("raw_filename", "result_raw.png"))
    report_name = str(qa_cfg.get("report_filename", "body_geometry_qa.json"))
    raw_path = run_dir / raw_name
    report_path = run_dir / report_name
    if not raw_path.exists():
        raise RuntimeError(f"RAW image not found: {raw_path}")

    width, height = load_image_size(raw_path)
    crown_y = float(args.crown_y)
    chin_y = float(args.chin_y)
    soles_y = float(args.soles_y)
    validate_landmarks(crown_y, chin_y, soles_y, height)

    head_height_px = chin_y - crown_y
    figure_height_px = soles_y - crown_y
    head_ratio = figure_height_px / head_height_px

    target = float(qa_cfg["target_heads"])
    acceptable_min = float(qa_cfg["acceptable_heads_min"])
    acceptable_max = float(qa_cfg["acceptable_heads_max"])
    numeric_pass = acceptable_min <= head_ratio <= acceptable_max

    raw_sha = sha256_file(raw_path)
    report = {
        "pass": numeric_pass,
        "status": "PASS" if numeric_pass else "FAIL",
        "gate": "NUMERIC_BODY_GEOMETRY_HEAD_RATIO",
        "landmark_method": "MANUAL_PIXEL_Y",
        "landmarks_reviewed": True,
        "raw_file": raw_name,
        "raw_sha256": raw_sha,
        "image_size": [width, height],
        "coordinate_convention": "Y measured downward from image top; subpixel values allowed.",
        "landmarks_y": {
            "crown": crown_y,
            "chin": chin_y,
            "soles": soles_y,
        },
        "head_height_px": head_height_px,
        "figure_height_px": figure_height_px,
        "head_ratio_heads": head_ratio,
        "target_heads": target,
        "acceptable_heads_min": acceptable_min,
        "acceptable_heads_max": acceptable_max,
        "distance_to_target_heads": head_ratio - target,
        "composition_execution_allowed": numeric_pass,
        "master_promotion": "NO",
        "note": (
            "Numeric PASS is necessary but not sufficient for Master promotion. "
            "Face Identity, internal body landmarks/silhouette, composition, and explicit author review remain separate QA gates."
        ),
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    qa_path = run_dir / "qa.json"
    if qa_path.exists():
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
    else:
        qa = {}
    qa["body_geometry_status"] = "PASS_NUMERIC" if numeric_pass else "FAIL_NUMERIC"
    qa["body_geometry_head_ratio"] = head_ratio
    qa["body_geometry_qa_file"] = report_name
    qa["composition_status"] = "READY_FOR_EXPLICIT_CONFIRMATION" if numeric_pass else "BLOCKED_BY_BODY_GEOMETRY"
    qa["master_promotion"] = "NO"
    qa["author_pass"] = None
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "status": report["status"],
        "pass": numeric_pass,
        "run_dir": str(run_dir),
        "body_geometry_qa": str(report_path),
        "head_ratio_heads": head_ratio,
        "acceptable_range": [acceptable_min, acceptable_max],
        "composition_execution_allowed": numeric_pass,
        "next": (
            "If PASS, review remaining Body Geometry/silhouette visually, then run normalize_composition.py with --confirm-body-geometry-pass."
            if numeric_pass
            else "Do not normalize Composition. This RAW candidate failed the numeric 7.1–7.3 head-ratio gate."
        ),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
