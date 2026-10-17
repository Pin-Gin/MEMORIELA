from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"

PASS_STATUSES = {"EXACT_PASS", "PASS_ROBUST"}


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


def head_ratio(crown_y: float, chin_y: float, soles_y: float) -> float:
    head_height = chin_y - crown_y
    full_height = soles_y - crown_y
    if head_height <= 0:
        raise RuntimeError("chin_y must be below structural crown")
    if full_height <= head_height:
        raise RuntimeError("soles_y must be below chin_y")
    return full_height / head_height


def classify(
    value_min: float,
    value_max: float,
    gate_min: float,
    gate_max: float,
    *,
    exact: bool,
) -> str:
    if exact and gate_min <= value_min <= gate_max:
        return "EXACT_PASS"
    if gate_min <= value_min and value_max <= gate_max:
        return "PASS_ROBUST"
    if value_max >= gate_min and value_min <= gate_max:
        return "REVIEW_OVERLAP"
    return "FAIL_ROBUST"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Current YURA paid-route head-ratio QA. "
            "Measures actual structural skull top to chin and crown to soles. "
            "Visible outer hair volume is not skull height."
        )
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--visible-hair-crown-y", type=float)
    parser.add_argument("--structural-crown-min-y", type=float, required=True)
    parser.add_argument("--structural-crown-best-y", type=float, required=True)
    parser.add_argument("--structural-crown-max-y", type=float, required=True)
    parser.add_argument("--chin-y", type=float, required=True)
    parser.add_argument("--soles-y", type=float, required=True)
    parser.add_argument(
        "--confirm-measurement-reviewed",
        action="store_true",
        help=(
            "Required. Confirms the structural skull top, chin and soles were manually reviewed "
            "on the generated image and that outer hair volume was not used as the crown."
        ),
    )
    args = parser.parse_args()

    if not args.confirm_measurement_reviewed:
        raise RuntimeError(
            "Refusing to record head-ratio QA without --confirm-measurement-reviewed"
        )

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    qa_cfg: dict[str, Any] = config.get("body_geometry_qa") or {}
    if qa_cfg.get("enabled") is not True:
        raise RuntimeError("body_geometry_qa must be enabled in config.json")

    target_min = float(qa_cfg["target_heads_min"])
    target_max = float(qa_cfg["target_heads_max"])
    if (target_min, target_max) != (7.0, 7.2):
        raise RuntimeError("Current paid route requires exactly 7.0–7.2 heads")

    run_dir = args.run_dir.resolve()
    result_name = str(qa_cfg.get("result_filename", "result.png"))
    report_name = str(qa_cfg.get("report_filename", "body_geometry_qa.json"))
    result_path = run_dir / result_name
    if not result_path.exists():
        raise RuntimeError(f"generated image not found: {result_path}")

    width, height = load_image_size(result_path)

    cmin = float(args.structural_crown_min_y)
    cbest = float(args.structural_crown_best_y)
    cmax = float(args.structural_crown_max_y)
    chin = float(args.chin_y)
    soles = float(args.soles_y)

    if not (0 <= cmin <= cbest <= cmax < chin < soles <= height):
        raise RuntimeError(
            "Require 0 <= crown_min <= crown_best <= crown_max < chin < soles <= image height"
        )

    if args.visible_hair_crown_y is not None:
        vh = float(args.visible_hair_crown_y)
        if not (0 <= vh < chin):
            raise RuntimeError("visible_hair_crown_y must be above chin")
    else:
        vh = None

    samples = [head_ratio(c, chin, soles) for c in (cmin, cbest, cmax)]
    best = head_ratio(cbest, chin, soles)
    interval_min = min(samples)
    interval_max = max(samples)
    exact = cmin == cbest == cmax
    status = classify(
        interval_min,
        interval_max,
        target_min,
        target_max,
        exact=exact,
    )
    passed = status in PASS_STATUSES

    report = {
        "pass": passed,
        "status": status,
        "gate": "CURRENT_YURA_HEAD_RATIO_7_0_TO_7_2",
        "result_file": result_name,
        "result_sha256": sha256_file(result_path),
        "image_size": [width, height],
        "coordinate_convention": "Y increases downward from image top.",
        "measurement_rule": (
            "ONE HEAD = actual structural crown / skull top to chin. "
            "Visible outer hair volume is not skull height."
        ),
        "landmarks_y": {
            "visible_hair_crown": vh,
            "structural_crown": {
                "min": cmin,
                "best": cbest,
                "max": cmax,
            },
            "chin": chin,
            "soles": soles,
        },
        "head_ratio": {
            "best": best,
            "interval": [interval_min, interval_max],
            "acceptable_min": target_min,
            "acceptable_max": target_max,
            "distance_to_nearest_boundary": min(
                abs(best - target_min),
                abs(best - target_max),
            ),
        },
        "legacy_numeric_gate_policy": (
            "Legacy 7.1–7.3 and retired composition occupancy/margin gates are inactive. "
            "Legacy internal body percentages are not active hard gates unless explicitly reauthorized."
        ),
        "body_authority_policy": (
            "This numeric check does not rewrite body geometry. "
            "Body design remains controlled by current YURA_VISUAL_TEXT.md and active Body Geometry Guide."
        ),
        "master_promotion": "NO",
        "author_pass_required": True,
    }
    (run_dir / report_name).write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    qa_path = run_dir / "qa.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8")) if qa_path.exists() else {}
    qa["head_ratio_status"] = status
    qa["head_ratio_pass"] = passed
    qa["head_ratio_best"] = best
    qa["head_ratio_interval"] = [interval_min, interval_max]
    qa["head_ratio_target_range"] = [target_min, target_max]
    qa["body_geometry_report"] = report_name
    qa["auto_pass"] = False
    qa["master_promotion"] = "NO"
    qa["author_pass"] = qa.get("author_pass")
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
