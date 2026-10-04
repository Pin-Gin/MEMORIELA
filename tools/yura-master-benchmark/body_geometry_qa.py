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
    crotch_y: float,
    knee_y: float,
    soles_y: float,
    image_height: int,
) -> None:
    if not (0 <= crown_y < chin_y < crotch_y < knee_y < soles_y <= image_height):
        raise RuntimeError(
            "Landmarks must satisfy 0 <= crown_y < chin_y < crotch_y < knee_y < soles_y <= image_height"
        )
    if chin_y - crown_y < 1.0:
        raise RuntimeError("Head height is too small to measure")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Record RAW Body Geometry QA from manually reviewed vertical landmarks. "
            "Hard gates cover total head ratio, YURA inseam proxy, and torso span; "
            "visual review remains mandatory for torso/pelvis/knee naturalness."
        )
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--crown-y", type=float, required=True)
    parser.add_argument("--chin-y", type=float, required=True)
    parser.add_argument("--crotch-y", type=float, required=True)
    parser.add_argument("--knee-y", type=float, required=True)
    parser.add_argument("--soles-y", type=float, required=True)
    parser.add_argument(
        "--confirm-landmarks-reviewed",
        action="store_true",
        help="Required: confirms crown/chin/crotch/knee/soles Y landmarks were visually reviewed on result_raw.png.",
    )
    parser.add_argument(
        "--confirm-upper-body-not-elongated",
        action="store_true",
        help="Required for PASS: confirms the upper body is not vertically elongated.",
    )
    parser.add_argument(
        "--confirm-torso-compact",
        action="store_true",
        help="Required for PASS: confirms ribcage-to-waist-to-pelvis torso span is compact rather than long.",
    )
    parser.add_argument(
        "--confirm-waist-not-low",
        action="store_true",
        help="Required for PASS: confirms waist placement is not unnaturally low.",
    )
    parser.add_argument(
        "--confirm-pelvis-high-enough",
        action="store_true",
        help="Required for PASS: confirms pelvis/crotch position reads slightly high as intended.",
    )
    parser.add_argument(
        "--confirm-lower-body-slightly-longer",
        action="store_true",
        help="Required for PASS: confirms the lower body reads subtly longer without exaggerated model-like legs.",
    )
    parser.add_argument(
        "--confirm-knee-placement-natural",
        action="store_true",
        help="Required for PASS: confirms thigh/shin distribution and knee placement are natural.",
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
    if qa_cfg.get("landmark_method") != "MANUAL_PIXEL_Y_WITH_INTERNAL_LANDMARKS":
        raise RuntimeError(
            "body_geometry_qa landmark_method must be MANUAL_PIXEL_Y_WITH_INTERNAL_LANDMARKS"
        )

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
    crotch_y = float(args.crotch_y)
    knee_y = float(args.knee_y)
    soles_y = float(args.soles_y)
    validate_landmarks(crown_y, chin_y, crotch_y, knee_y, soles_y, height)

    head_height_px = chin_y - crown_y
    figure_height_px = soles_y - crown_y
    head_ratio = figure_height_px / head_height_px

    crown_to_crotch_heads = (crotch_y - crown_y) / head_height_px
    chin_to_crotch_heads = (crotch_y - chin_y) / head_height_px
    crotch_to_knee_heads = (knee_y - crotch_y) / head_height_px
    knee_to_soles_heads = (soles_y - knee_y) / head_height_px
    crotch_to_soles_heads = (soles_y - crotch_y) / head_height_px
    knee_from_crown_heads = (knee_y - crown_y) / head_height_px
    inseam_proxy_ratio = (soles_y - crotch_y) / figure_height_px

    target = float(qa_cfg["target_heads"])
    acceptable_min = float(qa_cfg["acceptable_heads_min"])
    acceptable_max = float(qa_cfg["acceptable_heads_max"])
    head_ratio_pass = acceptable_min <= head_ratio <= acceptable_max

    inseam_min = float(qa_cfg["inseam_proxy_target_min"])
    inseam_max = float(qa_cfg["inseam_proxy_target_max"])
    inseam_hard_fail_min = float(qa_cfg["inseam_proxy_model_like_hard_fail_min"])
    inseam_target_pass = inseam_min <= inseam_proxy_ratio <= inseam_max
    inseam_model_like_hard_fail = inseam_proxy_ratio >= inseam_hard_fail_min

    torso_min = float(qa_cfg["torso_chin_to_crotch_heads_min"])
    torso_max = float(qa_cfg["torso_chin_to_crotch_heads_max"])
    torso_numeric_pass = torso_min <= chin_to_crotch_heads <= torso_max

    review = {
        "upper_body_not_elongated": bool(args.confirm_upper_body_not_elongated),
        "torso_compact": bool(args.confirm_torso_compact),
        "waist_not_low": bool(args.confirm_waist_not_low),
        "pelvis_high_enough": bool(args.confirm_pelvis_high_enough),
        "lower_body_slightly_longer": bool(args.confirm_lower_body_slightly_longer),
        "knee_placement_natural": bool(args.confirm_knee_placement_natural),
    }
    internal_visual_review_pass = all(review.values())

    torso_specific_gate_pass = (
        torso_numeric_pass
        and inseam_target_pass
        and not inseam_model_like_hard_fail
        and review["torso_compact"]
        and review["waist_not_low"]
        and review["pelvis_high_enough"]
    )

    passed = (
        head_ratio_pass
        and torso_specific_gate_pass
        and internal_visual_review_pass
    )

    raw_sha = sha256_file(raw_path)
    report = {
        "pass": passed,
        "status": "PASS" if passed else "FAIL",
        "gate": "HEAD_RATIO_PLUS_INSEAM_PROXY_PLUS_TORSO_SPECIFIC_GATE",
        "landmark_method": "MANUAL_PIXEL_Y_WITH_INTERNAL_LANDMARKS",
        "landmarks_reviewed": True,
        "raw_file": raw_name,
        "raw_sha256": raw_sha,
        "image_size": [width, height],
        "coordinate_convention": "Y measured downward from image top; subpixel values allowed.",
        "landmarks_y": {
            "crown": crown_y,
            "chin": chin_y,
            "crotch": crotch_y,
            "knee": knee_y,
            "soles": soles_y,
        },
        "metrics": {
            "head_height_px": head_height_px,
            "figure_height_px": figure_height_px,
            "head_ratio_heads": head_ratio,
            "crown_to_crotch_heads": crown_to_crotch_heads,
            "chin_to_crotch_heads": chin_to_crotch_heads,
            "crotch_to_knee_heads": crotch_to_knee_heads,
            "knee_to_soles_heads": knee_to_soles_heads,
            "crotch_to_soles_heads": crotch_to_soles_heads,
            "knee_from_crown_heads": knee_from_crown_heads,
            "inseam_proxy_ratio": inseam_proxy_ratio,
            "inseam_proxy_percent": inseam_proxy_ratio * 100.0,
        },
        "head_ratio_gate": {
            "pass": head_ratio_pass,
            "target_heads": target,
            "acceptable_heads_min": acceptable_min,
            "acceptable_heads_max": acceptable_max,
            "distance_to_target_heads": head_ratio - target,
        },
        "inseam_proxy_gate": {
            "pass": inseam_target_pass and not inseam_model_like_hard_fail,
            "target_min": inseam_min,
            "target_max": inseam_max,
            "model_like_hard_fail_min": inseam_hard_fail_min,
            "value": inseam_proxy_ratio,
            "value_percent": inseam_proxy_ratio * 100.0,
            "model_like_hard_fail": inseam_model_like_hard_fail,
            "definition": "(soles_y - crotch_y) / (soles_y - crown_y)",
            "scope": "YURA-specific image-space proxy, not a universal human-body standard.",
        },
        "torso_specific_gate": {
            "pass": torso_specific_gate_pass,
            "chin_to_crotch_heads": chin_to_crotch_heads,
            "acceptable_min": torso_min,
            "acceptable_max": torso_max,
            "numeric_pass": torso_numeric_pass,
            "inseam_proxy_pass": inseam_target_pass and not inseam_model_like_hard_fail,
            "torso_compact_confirmed": review["torso_compact"],
            "waist_not_low_confirmed": review["waist_not_low"],
            "pelvis_high_enough_confirmed": review["pelvis_high_enough"],
            "derivation_note": (
                "The torso numeric envelope is derived from the approved 7.1–7.3 total-head range "
                "and 46.0–46.5% YURA inseam proxy target; it is not an independently invented body ratio."
            ),
        },
        "internal_landmark_policy": {
            "status": "NUMERIC_PLUS_AUTHOR_VISUAL_GATE",
            "preference": (
                "Compact torso, waist not low, pelvis/crotch slightly high, subtly longer lower body, "
                "natural knee placement, and no leg-only or torso-only stretching."
            ),
            "review": review,
            "review_pass": internal_visual_review_pass,
        },
        "composition_execution_allowed": passed,
        "master_promotion": "NO",
        "note": (
            "PASS is necessary but not sufficient for Master promotion. Face Identity, detailed silhouette, "
            "final Composition, and explicit author confirmation remain separate QA gates."
        ),
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    qa_path = run_dir / "qa.json"
    if qa_path.exists():
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
    else:
        qa = {}
    qa["body_geometry_status"] = "PASS" if passed else "FAIL"
    qa["body_geometry_head_ratio"] = head_ratio
    qa["body_geometry_inseam_proxy_ratio"] = inseam_proxy_ratio
    qa["body_geometry_torso_specific_gate_pass"] = torso_specific_gate_pass
    qa["body_geometry_internal_review_pass"] = internal_visual_review_pass
    qa["body_geometry_qa_file"] = report_name
    qa["composition_status"] = (
        "READY_FOR_EXPLICIT_CONFIRMATION" if passed else "BLOCKED_BY_BODY_GEOMETRY"
    )
    qa["master_promotion"] = "NO"
    qa["author_pass"] = None
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "status": report["status"],
        "pass": passed,
        "run_dir": str(run_dir),
        "body_geometry_qa": str(report_path),
        "head_ratio_heads": head_ratio,
        "acceptable_head_ratio_range": [acceptable_min, acceptable_max],
        "inseam_proxy_percent": inseam_proxy_ratio * 100.0,
        "inseam_proxy_target_percent": [inseam_min * 100.0, inseam_max * 100.0],
        "torso_chin_to_crotch_heads": chin_to_crotch_heads,
        "torso_target_heads": [torso_min, torso_max],
        "torso_specific_gate_pass": torso_specific_gate_pass,
        "internal_visual_review_pass": internal_visual_review_pass,
        "composition_execution_allowed": passed,
        "next": (
            "If PASS, Composition may be normalized only with the separate explicit confirmation flag."
            if passed
            else "Do not normalize Composition. Fix the failing Body Geometry condition first."
        ),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
