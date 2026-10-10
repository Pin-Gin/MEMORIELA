from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"

PASS_INTERVAL_STATUSES = {"EXACT_PASS", "PASS_ROBUST"}
AUTHOR_REVIEW_VALUES = {
    "pass": "PASS",
    "fail": "FAIL",
    "not-reviewed": "NOT_REVIEWED",
    "not-measurable": "NOT_MEASURABLE",
}


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


def classify_interval(
    value_min: float,
    value_max: float,
    gate_min: float,
    gate_max: float,
    *,
    exact: bool,
) -> str:
    if value_min > value_max:
        value_min, value_max = value_max, value_min
    if exact and gate_min <= value_min <= gate_max:
        return "EXACT_PASS"
    if gate_min <= value_min and value_max <= gate_max:
        return "PASS_ROBUST"
    if value_max >= gate_min and value_min <= gate_max:
        return "REVIEW_OVERLAP"
    return "FAIL_ROBUST"


def metric_interval(values: list[float]) -> tuple[float, float]:
    return min(values), max(values)


def head_metrics(crown_y: float, chin_y: float, soles_y: float) -> dict[str, float]:
    head_height = chin_y - crown_y
    figure_height = soles_y - crown_y
    return {
        "head_height_px": head_height,
        "figure_height_px": figure_height,
        "head_ratio_heads": figure_height / head_height,
    }


def body_metrics(
    crown_y: float,
    chin_y: float,
    boundary_y: float,
    knee_y: float,
    soles_y: float,
) -> dict[str, float]:
    values = head_metrics(crown_y, chin_y, soles_y)
    head_height = values["head_height_px"]
    figure_height = values["figure_height_px"]
    lower_body_px = soles_y - boundary_y
    boundary_to_knee_px = knee_y - boundary_y
    knee_to_soles_px = soles_y - knee_y
    values.update(
        {
            "crown_to_crotch_pelvis_boundary_heads": (boundary_y - crown_y) / head_height,
            "chin_to_crotch_pelvis_boundary_heads": (boundary_y - chin_y) / head_height,
            "crotch_pelvis_boundary_to_knee_heads": boundary_to_knee_px / head_height,
            "knee_to_soles_heads": knee_to_soles_px / head_height,
            "crotch_pelvis_boundary_to_soles_heads": lower_body_px / head_height,
            "knee_from_crown_heads": (knee_y - crown_y) / head_height,
            "inseam_proxy_ratio": lower_body_px / figure_height,
            "crotch_pelvis_boundary_to_knee_share": boundary_to_knee_px / lower_body_px,
            "knee_to_soles_share": knee_to_soles_px / lower_body_px,
        }
    )
    return values


def validate_landmarks(
    *,
    visible_hair_crown_y: float | None,
    structural_min_y: float,
    structural_best_y: float,
    structural_max_y: float,
    chin_y: float,
    boundary_min_y: float,
    boundary_best_y: float,
    boundary_max_y: float,
    knee_y: float,
    soles_y: float,
    image_height: int,
) -> None:
    if not (
        0
        <= structural_min_y
        <= structural_best_y
        <= structural_max_y
        < chin_y
        < boundary_min_y
        <= boundary_best_y
        <= boundary_max_y
        < knee_y
        < soles_y
        <= image_height
    ):
        raise RuntimeError(
            "Landmarks must satisfy 0 <= structural_crown_min_y <= structural_crown_best_y "
            "<= structural_crown_max_y < chin_y < crotch_pelvis_boundary_min_y "
            "<= crotch_pelvis_boundary_best_y <= crotch_pelvis_boundary_max_y "
            "< knee_y < soles_y <= image_height"
        )
    if visible_hair_crown_y is not None and not (0 <= visible_hair_crown_y < chin_y):
        raise RuntimeError(
            "visible_hair_crown_y must satisfy 0 <= visible_hair_crown_y < chin_y"
        )
    if chin_y - structural_max_y < 1.0:
        raise RuntimeError("Structural head height is too small to measure")


def require_official_config(qa_cfg: dict[str, Any]) -> None:
    expected = {
        "landmark_method": "MANUAL_PIXEL_Y_WITH_STRUCTURAL_UNCERTAINTY",
        "crotch_pelvis_boundary_definition": (
            "CENTRAL_MEDIAL_THIGH_BIFURCATION_UPPER_LOWER_BODY_BOUNDARY"
        ),
        "garment_line_landmark_authority": "DENIED",
        "uncertainty_combination_policy": (
            "STRUCTURAL_CROWN_3_X_CROTCH_PELVIS_BOUNDARY_3"
        ),
        "interval_pass_policy": "FULL_INTERVAL_MUST_BE_INSIDE_CURRENT_GATE",
        "review_overlap_policy": "BLOCK_COMPOSITION_PENDING_REVIEW",
    }
    for key, value in expected.items():
        if qa_cfg.get(key) != value:
            raise RuntimeError(f"body_geometry_qa {key} must be {value}")
    if qa_cfg.get("require_overall_build_not_too_thin_review") is not True:
        raise RuntimeError("overall-build author review must be required")
    if qa_cfg.get("require_chest_front_volume_match_review") is not True:
        raise RuntimeError("chest/front-volume author review must be required")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Record official RAW Body Geometry QA using structural-crown and "
            "crotch/pelvis-boundary uncertainty. Numeric gates use full intervals; "
            "Composition remains blocked on REVIEW_OVERLAP or FAIL_ROBUST."
        )
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--visible-hair-crown-y", type=float)
    parser.add_argument("--structural-crown-min-y", type=float, required=True)
    parser.add_argument("--structural-crown-best-y", type=float, required=True)
    parser.add_argument("--structural-crown-max-y", type=float, required=True)
    parser.add_argument("--chin-y", type=float, required=True)
    parser.add_argument("--crotch-pelvis-boundary-min-y", type=float, required=True)
    parser.add_argument("--crotch-pelvis-boundary-best-y", type=float, required=True)
    parser.add_argument("--crotch-pelvis-boundary-max-y", type=float, required=True)
    parser.add_argument("--knee-y", type=float, required=True)
    parser.add_argument("--soles-y", type=float, required=True)
    parser.add_argument(
        "--confirm-landmarks-reviewed",
        action="store_true",
        help=(
            "Required: confirms structural crown, chin, crotch/pelvis boundary, "
            "knee and soles were visually reviewed on result_raw.png."
        ),
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
    parser.add_argument(
        "--overall-build",
        choices=tuple(AUTHOR_REVIEW_VALUES),
        required=True,
        help="Author visual gate: whole-body mass/silhouette is not too thin.",
    )
    parser.add_argument(
        "--chest-front-volume",
        choices=tuple(AUTHOR_REVIEW_VALUES),
        required=True,
        help="Author visual gate: chest/front-volume silhouette matches YURA intent.",
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
    require_official_config(qa_cfg)

    run_dir = args.run_dir.resolve()
    raw_name = str(qa_cfg.get("raw_filename", "result_raw.png"))
    report_name = str(qa_cfg.get("report_filename", "body_geometry_qa.json"))
    raw_path = run_dir / raw_name
    report_path = run_dir / report_name
    if not raw_path.exists():
        raise RuntimeError(f"RAW image not found: {raw_path}")

    width, height = load_image_size(raw_path)
    visible_hair_crown_y = (
        float(args.visible_hair_crown_y)
        if args.visible_hair_crown_y is not None
        else None
    )
    structural_min_y = float(args.structural_crown_min_y)
    structural_best_y = float(args.structural_crown_best_y)
    structural_max_y = float(args.structural_crown_max_y)
    chin_y = float(args.chin_y)
    boundary_min_y = float(args.crotch_pelvis_boundary_min_y)
    boundary_best_y = float(args.crotch_pelvis_boundary_best_y)
    boundary_max_y = float(args.crotch_pelvis_boundary_max_y)
    knee_y = float(args.knee_y)
    soles_y = float(args.soles_y)

    validate_landmarks(
        visible_hair_crown_y=visible_hair_crown_y,
        structural_min_y=structural_min_y,
        structural_best_y=structural_best_y,
        structural_max_y=structural_max_y,
        chin_y=chin_y,
        boundary_min_y=boundary_min_y,
        boundary_best_y=boundary_best_y,
        boundary_max_y=boundary_max_y,
        knee_y=knee_y,
        soles_y=soles_y,
        image_height=height,
    )

    structural_values = [structural_min_y, structural_best_y, structural_max_y]
    boundary_values = [boundary_min_y, boundary_best_y, boundary_max_y]

    head_samples = [
        head_metrics(crown_y, chin_y, soles_y) for crown_y in structural_values
    ]
    combined_samples = [
        body_metrics(crown_y, chin_y, boundary_y, knee_y, soles_y)
        for crown_y in structural_values
        for boundary_y in boundary_values
    ]
    best = body_metrics(
        structural_best_y,
        chin_y,
        boundary_best_y,
        knee_y,
        soles_y,
    )

    exact_crown = structural_min_y == structural_best_y == structural_max_y
    exact_boundary = boundary_min_y == boundary_best_y == boundary_max_y
    exact_combined = exact_crown and exact_boundary

    target = float(qa_cfg["target_heads"])
    acceptable_min = float(qa_cfg["acceptable_heads_min"])
    acceptable_max = float(qa_cfg["acceptable_heads_max"])
    head_min, head_max = metric_interval(
        [sample["head_ratio_heads"] for sample in head_samples]
    )
    head_status = classify_interval(
        head_min,
        head_max,
        acceptable_min,
        acceptable_max,
        exact=exact_crown,
    )
    head_pass = head_status in PASS_INTERVAL_STATUSES

    inseam_target_min = float(qa_cfg["inseam_proxy_target_min"])
    inseam_target_max = float(qa_cfg["inseam_proxy_target_max"])
    inseam_hard_fail_min = float(qa_cfg["inseam_proxy_model_like_hard_fail_min"])
    inseam_min, inseam_max = metric_interval(
        [sample["inseam_proxy_ratio"] for sample in combined_samples]
    )
    inseam_status = classify_interval(
        inseam_min,
        inseam_max,
        inseam_target_min,
        inseam_target_max,
        exact=exact_combined,
    )
    inseam_hard_fail_best = best["inseam_proxy_ratio"] >= inseam_hard_fail_min
    inseam_hard_fail_robust = inseam_min >= inseam_hard_fail_min
    inseam_pass = (
        inseam_status in PASS_INTERVAL_STATUSES
        and not inseam_hard_fail_best
        and not inseam_hard_fail_robust
    )

    torso_target_min = float(qa_cfg["torso_chin_to_crotch_heads_min"])
    torso_target_max = float(qa_cfg["torso_chin_to_crotch_heads_max"])
    torso_min, torso_max = metric_interval(
        [
            sample["chin_to_crotch_pelvis_boundary_heads"]
            for sample in combined_samples
        ]
    )
    torso_status = classify_interval(
        torso_min,
        torso_max,
        torso_target_min,
        torso_target_max,
        exact=exact_combined,
    )
    torso_numeric_pass = torso_status in PASS_INTERVAL_STATUSES

    boundary_to_knee_heads_min, boundary_to_knee_heads_max = metric_interval(
        [
            sample["crotch_pelvis_boundary_to_knee_heads"]
            for sample in combined_samples
        ]
    )
    knee_to_soles_heads_min, knee_to_soles_heads_max = metric_interval(
        [sample["knee_to_soles_heads"] for sample in combined_samples]
    )
    boundary_to_knee_share_min, boundary_to_knee_share_max = metric_interval(
        [
            sample["crotch_pelvis_boundary_to_knee_share"]
            for sample in combined_samples
        ]
    )
    knee_to_soles_share_min, knee_to_soles_share_max = metric_interval(
        [sample["knee_to_soles_share"] for sample in combined_samples]
    )

    review = {
        "upper_body_not_elongated": bool(args.confirm_upper_body_not_elongated),
        "torso_compact": bool(args.confirm_torso_compact),
        "waist_not_low": bool(args.confirm_waist_not_low),
        "pelvis_high_enough": bool(args.confirm_pelvis_high_enough),
        "lower_body_slightly_longer": bool(
            args.confirm_lower_body_slightly_longer
        ),
        "knee_placement_natural": bool(args.confirm_knee_placement_natural),
    }
    internal_visual_review_pass = all(review.values())

    author_review = {
        "overall_build_not_too_thin": AUTHOR_REVIEW_VALUES[args.overall_build],
        "chest_front_volume_matches_author_intent": AUTHOR_REVIEW_VALUES[
            args.chest_front_volume
        ],
    }
    author_visual_gate_pass = all(
        value == "PASS" for value in author_review.values()
    )
    author_visual_explicit_fail = any(
        value == "FAIL" for value in author_review.values()
    )

    numeric_gate_pass = head_pass and inseam_pass and torso_numeric_pass
    torso_specific_gate_pass = (
        torso_numeric_pass
        and inseam_pass
        and review["torso_compact"]
        and review["waist_not_low"]
        and review["pelvis_high_enough"]
    )
    passed = (
        numeric_gate_pass
        and internal_visual_review_pass
        and author_visual_gate_pass
    )

    robust_numeric_fail = any(
        status == "FAIL_ROBUST"
        for status in (head_status, inseam_status, torso_status)
    )
    if passed:
        overall_status = "PASS"
    elif robust_numeric_fail or author_visual_explicit_fail:
        overall_status = "FAIL"
    else:
        overall_status = "REVIEW"

    raw_sha = sha256_file(raw_path)
    report = {
        "pass": passed,
        "status": overall_status,
        "gate": (
            "STRUCTURAL_UNCERTAINTY_HEAD_INSEAM_TORSO_PLUS_AUTHOR_VISUAL_GATE"
        ),
        "landmark_method": "MANUAL_PIXEL_Y_WITH_STRUCTURAL_UNCERTAINTY",
        "landmarks_reviewed": True,
        "raw_file": raw_name,
        "raw_sha256": raw_sha,
        "image_size": [width, height],
        "coordinate_convention": (
            "Y measured downward from image top; subpixel values allowed. "
            "Hidden structural landmarks are represented by reviewed min/best/max intervals."
        ),
        "landmarks_y": {
            "visible_hair_crown": visible_hair_crown_y,
            "structural_crown": {
                "min": structural_min_y,
                "best": structural_best_y,
                "max": structural_max_y,
            },
            "chin": chin_y,
            "crotch_pelvis_boundary": {
                "min": boundary_min_y,
                "best": boundary_best_y,
                "max": boundary_max_y,
                "definition": qa_cfg["crotch_pelvis_boundary_definition"],
                "garment_line_authority": qa_cfg[
                    "garment_line_landmark_authority"
                ],
            },
            "knee": knee_y,
            "soles": soles_y,
        },
        "metrics": {
            "head_height_px": best["head_height_px"],
            "figure_height_px": best["figure_height_px"],
            "head_ratio_heads": best["head_ratio_heads"],
            "crown_to_crotch_heads": best[
                "crown_to_crotch_pelvis_boundary_heads"
            ],
            "chin_to_crotch_heads": best[
                "chin_to_crotch_pelvis_boundary_heads"
            ],
            "crotch_to_knee_heads": best[
                "crotch_pelvis_boundary_to_knee_heads"
            ],
            "knee_to_soles_heads": best["knee_to_soles_heads"],
            "crotch_to_soles_heads": best[
                "crotch_pelvis_boundary_to_soles_heads"
            ],
            "knee_from_crown_heads": best["knee_from_crown_heads"],
            "inseam_proxy_ratio": best["inseam_proxy_ratio"],
            "inseam_proxy_percent": best["inseam_proxy_ratio"] * 100.0,
            "chin_to_crotch_pelvis_boundary_heads": best[
                "chin_to_crotch_pelvis_boundary_heads"
            ],
        },
        "head_ratio_gate": {
            "pass": head_pass,
            "status": head_status,
            "best": best["head_ratio_heads"],
            "interval": [head_min, head_max],
            "target_heads": target,
            "acceptable_heads_min": acceptable_min,
            "acceptable_heads_max": acceptable_max,
            "distance_to_target_heads": best["head_ratio_heads"] - target,
        },
        "inseam_proxy_gate": {
            "pass": inseam_pass,
            "status": inseam_status,
            "best": best["inseam_proxy_ratio"],
            "best_percent": best["inseam_proxy_ratio"] * 100.0,
            "interval": [inseam_min, inseam_max],
            "interval_percent": [inseam_min * 100.0, inseam_max * 100.0],
            "target_min": inseam_target_min,
            "target_max": inseam_target_max,
            "model_like_hard_fail_min": inseam_hard_fail_min,
            "model_like_hard_fail_best": inseam_hard_fail_best,
            "model_like_hard_fail_robust": inseam_hard_fail_robust,
            "definition": (
                "(soles_y - crotch_pelvis_boundary_y) / "
                "(soles_y - structural_crown_y)"
            ),
            "scope": (
                "YURA-specific image-space proxy, not a universal human-body standard."
            ),
        },
        "torso_specific_gate": {
            "pass": torso_specific_gate_pass,
            "status": torso_status,
            "numeric_pass": torso_numeric_pass,
            "best": best["chin_to_crotch_pelvis_boundary_heads"],
            "interval": [torso_min, torso_max],
            "acceptable_min": torso_target_min,
            "acceptable_max": torso_target_max,
            "inseam_proxy_pass": inseam_pass,
            "torso_compact_confirmed": review["torso_compact"],
            "waist_not_low_confirmed": review["waist_not_low"],
            "pelvis_high_enough_confirmed": review["pelvis_high_enough"],
            "derivation_note": (
                "The torso numeric envelope is derived from the approved 7.1–7.3 total-head range "
                "and 46.0–46.5% YURA inseam proxy target; it is not an independently invented body ratio."
            ),
        },
        "lower_body_split": {
            "boundary_to_knee_heads": {
                "best": best["crotch_pelvis_boundary_to_knee_heads"],
                "interval": [
                    boundary_to_knee_heads_min,
                    boundary_to_knee_heads_max,
                ],
            },
            "knee_to_soles_heads": {
                "best": best["knee_to_soles_heads"],
                "interval": [
                    knee_to_soles_heads_min,
                    knee_to_soles_heads_max,
                ],
            },
            "boundary_to_knee_share_percent": {
                "best": best["crotch_pelvis_boundary_to_knee_share"] * 100.0,
                "interval": [
                    boundary_to_knee_share_min * 100.0,
                    boundary_to_knee_share_max * 100.0,
                ],
            },
            "knee_to_soles_share_percent": {
                "best": best["knee_to_soles_share"] * 100.0,
                "interval": [
                    knee_to_soles_share_min * 100.0,
                    knee_to_soles_share_max * 100.0,
                ],
            },
            "threshold_policy": "DIAGNOSTIC_ONLY_NO_NEW_HARD_GATE",
        },
        "uncertainty_policy": {
            "structural_crown_samples": structural_values,
            "crotch_pelvis_boundary_samples": boundary_values,
            "combined_sample_count": len(combined_samples),
            "combination_policy": qa_cfg["uncertainty_combination_policy"],
            "interval_pass_policy": qa_cfg["interval_pass_policy"],
            "review_overlap_policy": qa_cfg["review_overlap_policy"],
        },
        "numeric_gate": {
            "pass": numeric_gate_pass,
            "head_status": head_status,
            "inseam_status": inseam_status,
            "torso_status": torso_status,
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
        "author_visual_gate": {
            **author_review,
            "pass": author_visual_gate_pass,
        },
        "composition_execution_allowed": passed,
        "master_promotion": "NO",
        "note": (
            "PASS is necessary but not sufficient for Master promotion. Face Identity, detailed silhouette, "
            "final Composition, and explicit author confirmation remain separate QA gates."
        ),
    }
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    qa_path = run_dir / "qa.json"
    if qa_path.exists():
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
    else:
        qa = {}
    qa["body_geometry_status"] = overall_status
    qa["body_geometry_head_ratio"] = best["head_ratio_heads"]
    qa["body_geometry_head_ratio_status"] = head_status
    qa["body_geometry_head_ratio_interval"] = [head_min, head_max]
    qa["body_geometry_inseam_proxy_ratio"] = best["inseam_proxy_ratio"]
    qa["body_geometry_inseam_proxy_status"] = inseam_status
    qa["body_geometry_inseam_proxy_interval"] = [inseam_min, inseam_max]
    qa["body_geometry_torso_specific_gate_pass"] = torso_specific_gate_pass
    qa["body_geometry_torso_status"] = torso_status
    qa["body_geometry_torso_interval"] = [torso_min, torso_max]
    qa["body_geometry_internal_review_pass"] = internal_visual_review_pass
    qa["body_geometry_author_visual_gate_pass"] = author_visual_gate_pass
    qa["body_geometry_qa_file"] = report_name
    qa["composition_status"] = (
        "READY_FOR_EXPLICIT_CONFIRMATION"
        if passed
        else (
            "BLOCKED_BY_BODY_GEOMETRY"
            if overall_status == "FAIL"
            else "BLOCKED_PENDING_BODY_GEOMETRY_REVIEW"
        )
    )
    qa["master_promotion"] = "NO"
    qa["author_pass"] = None
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "status": overall_status,
                "pass": passed,
                "run_dir": str(run_dir),
                "body_geometry_qa": str(report_path),
                "head_ratio_best": best["head_ratio_heads"],
                "head_ratio_interval": [head_min, head_max],
                "head_ratio_status": head_status,
                "inseam_proxy_best_percent": best["inseam_proxy_ratio"] * 100.0,
                "inseam_proxy_interval_percent": [
                    inseam_min * 100.0,
                    inseam_max * 100.0,
                ],
                "inseam_proxy_status": inseam_status,
                "torso_chin_to_boundary_best_heads": best[
                    "chin_to_crotch_pelvis_boundary_heads"
                ],
                "torso_chin_to_boundary_interval_heads": [
                    torso_min,
                    torso_max,
                ],
                "torso_status": torso_status,
                "torso_specific_gate_pass": torso_specific_gate_pass,
                "internal_visual_review_pass": internal_visual_review_pass,
                "author_visual_gate": report["author_visual_gate"],
                "composition_execution_allowed": passed,
                "next": (
                    "If PASS, Composition may be normalized only with the separate explicit confirmation flag."
                    if passed
                    else "Do not normalize Composition. Resolve FAIL/REVIEW Body Geometry conditions first."
                ),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
