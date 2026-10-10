from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from statistics import mean
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"
SCHEMA = "YURA_BODY_GEOMETRY_AUDIT_V2"
AUTHOR_REVIEW_VALUES = {
    "pass": "PASS",
    "fail": "FAIL",
    "not-reviewed": "NOT_REVIEWED",
    "not-measurable": "NOT_MEASURABLE",
}

WIDTH_ARG_TO_KEY = {
    "shoulder_width_px": "shoulder_width_px",
    "ribcage_width_px": "ribcage_width_px",
    "chest_outer_width_px": "chest_outer_width_px",
    "waist_width_px": "waist_width_px",
    "hip_width_px": "pelvis_hip_width_px",
    "upper_thigh_left_width_px": "upper_thigh_left_width_px",
    "upper_thigh_right_width_px": "upper_thigh_right_width_px",
    "calf_left_width_px": "calf_left_width_px",
    "calf_right_width_px": "calf_right_width_px",
    "ankle_left_width_px": "ankle_left_width_px",
    "ankle_right_width_px": "ankle_right_width_px",
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


def load_current_gate_config() -> dict[str, float]:
    if not CONFIG_PATH.exists():
        raise RuntimeError(f"Current config not found: {CONFIG_PATH}")
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    qa_cfg: dict[str, Any] = config.get("body_geometry_qa") or {}
    required = [
        "target_heads",
        "acceptable_heads_min",
        "acceptable_heads_max",
        "inseam_proxy_target_min",
        "inseam_proxy_target_max",
        "inseam_proxy_model_like_hard_fail_min",
        "torso_chin_to_crotch_heads_min",
        "torso_chin_to_crotch_heads_max",
    ]
    missing = [key for key in required if key not in qa_cfg]
    if missing:
        raise RuntimeError(
            "Current body_geometry_qa config missing required keys: " + ", ".join(missing)
        )
    return {key: float(qa_cfg[key]) for key in required}


def validate_common_landmarks(
    *,
    visible_hair_crown_y: float | None,
    structural_min_y: float,
    structural_best_y: float,
    structural_max_y: float,
    chin_y: float,
    image_height: int,
) -> None:
    if not (
        0 <= structural_min_y <= structural_best_y <= structural_max_y < chin_y <= image_height
    ):
        raise RuntimeError(
            "Structural landmarks must satisfy "
            "0 <= structural_min_y <= structural_best_y <= structural_max_y < chin_y <= image_height"
        )
    if visible_hair_crown_y is not None and not (0 <= visible_hair_crown_y < chin_y):
        raise RuntimeError(
            "visible_hair_crown_y must satisfy 0 <= visible_hair_crown_y < chin_y"
        )
    if chin_y - structural_max_y < 1.0:
        raise RuntimeError("Structural head height is too small to measure")


def validate_body_landmarks(
    *,
    chin_y: float,
    boundary_min_y: float,
    boundary_best_y: float,
    boundary_max_y: float,
    knee_y: float,
    soles_y: float,
    image_height: int,
) -> None:
    if not (
        chin_y
        < boundary_min_y
        <= boundary_best_y
        <= boundary_max_y
        < knee_y
        < soles_y
        <= image_height
    ):
        raise RuntimeError(
            "Body landmarks must satisfy chin_y < crotch_pelvis_boundary_min_y "
            "<= crotch_pelvis_boundary_best_y <= crotch_pelvis_boundary_max_y "
            "< knee_y < soles_y <= image_height"
        )


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
            "inseam_proxy_ratio": lower_body_px / figure_height,
            "chin_to_crotch_pelvis_boundary_heads": (boundary_y - chin_y) / head_height,
            "crotch_pelvis_boundary_to_knee_heads": boundary_to_knee_px / head_height,
            "knee_to_soles_heads": knee_to_soles_px / head_height,
            "crotch_pelvis_boundary_to_soles_heads": lower_body_px / head_height,
            "crotch_pelvis_boundary_to_knee_share": boundary_to_knee_px / lower_body_px,
            "knee_to_soles_share": knee_to_soles_px / lower_body_px,
        }
    )
    return values


def parse_widths(args: argparse.Namespace, structural_figure_height_best: float) -> dict[str, Any]:
    raw: dict[str, float] = {}
    for arg_name, report_name in WIDTH_ARG_TO_KEY.items():
        value = getattr(args, arg_name)
        if value is None:
            continue
        if value <= 0:
            raise RuntimeError(f"{arg_name} must be positive when supplied")
        raw[report_name] = float(value)

    if not raw:
        return {"status": "NOT_MEASURED"}

    normalized = {
        key: value / structural_figure_height_best for key, value in raw.items()
    }

    ratios: dict[str, float] = {}
    hip = raw.get("pelvis_hip_width_px")
    if hip:
        for source_key, ratio_key in [
            ("shoulder_width_px", "shoulder_over_hip"),
            ("ribcage_width_px", "ribcage_over_hip"),
            ("waist_width_px", "waist_over_hip"),
        ]:
            if source_key in raw:
                ratios[ratio_key] = raw[source_key] / hip

        thighs = [
            raw[key]
            for key in ("upper_thigh_left_width_px", "upper_thigh_right_width_px")
            if key in raw
        ]
        if thighs:
            ratios["average_upper_thigh_over_hip"] = mean(thighs) / hip

        calves = [
            raw[key]
            for key in ("calf_left_width_px", "calf_right_width_px")
            if key in raw
        ]
        if calves:
            ratios["average_calf_over_hip"] = mean(calves) / hip

    chest = raw.get("chest_outer_width_px")
    if chest is not None:
        ribcage = raw.get("ribcage_width_px")
        waist = raw.get("waist_width_px")
        if ribcage:
            ratios["chest_over_ribcage"] = chest / ribcage
        if waist:
            ratios["chest_over_waist"] = chest / waist

    return {
        "status": "DIAGNOSTIC_ONLY",
        "raw_widths_px": raw,
        "normalized_to_structural_figure_height_best": normalized,
        "ratios": ratios,
        "threshold_policy": "NO_NUMERIC_PASS_THRESHOLD_FROZEN",
    }


def build_head_shell_report(
    *,
    image_path: Path,
    width: int,
    height: int,
    visible_hair_crown_y: float,
    structural_min_y: float,
    structural_best_y: float,
    structural_max_y: float,
    chin_y: float,
) -> dict[str, Any]:
    visible_head_height = chin_y - visible_hair_crown_y
    structural = {
        "min_y": structural_min_y,
        "best_y": structural_best_y,
        "max_y": structural_max_y,
    }
    structural_head_heights = {
        "at_min_y": chin_y - structural_min_y,
        "at_best_y": chin_y - structural_best_y,
        "at_max_y": chin_y - structural_max_y,
    }
    height_values = list(structural_head_heights.values())
    inflation_values = [visible_head_height / value for value in height_values]

    return {
        "schema": SCHEMA,
        "authority_status": "DIAGNOSTIC_ONLY",
        "mode": "head-shell",
        "input": {
            "image": str(image_path),
            "sha256": sha256_file(image_path),
            "image_size": [width, height],
        },
        "landmarks": {
            "visible_hair_crown_y": visible_hair_crown_y,
            "structural_crown": structural,
            "chin_y": chin_y,
        },
        "visible_head_height_px": visible_head_height,
        "structural_head_height_px": {
            "min": min(height_values),
            "best": structural_head_heights["at_best_y"],
            "max": max(height_values),
        },
        "hair_shell_inflation": {
            "best": visible_head_height / structural_head_heights["at_best_y"],
            "range": [min(inflation_values), max(inflation_values)],
            "definition": "visible_head_height / structural_head_height",
            "scope": "diagnostic apparent-head-shell inflation only; not Body Authority",
        },
        "full_body_head_ratio_gate": "NOT_APPLICABLE_IN_HEAD_SHELL_MODE",
        "composition_execution_allowed": False,
        "master_promotion": "NO",
        "note": "Audit v2 is diagnostic until explicitly promoted by author approval.",
    }


def build_body_report(
    *,
    args: argparse.Namespace,
    image_path: Path,
    width: int,
    height: int,
    gates: dict[str, float],
) -> dict[str, Any]:
    structural_values = [
        args.structural_crown_min_y,
        args.structural_crown_best_y,
        args.structural_crown_max_y,
    ]
    boundary_values = [
        args.crotch_pelvis_boundary_min_y,
        args.crotch_pelvis_boundary_best_y,
        args.crotch_pelvis_boundary_max_y,
    ]

    head_samples = [
        head_metrics(crown_y, args.chin_y, args.soles_y)
        for crown_y in structural_values
    ]
    combined_metrics = [
        body_metrics(
            crown_y,
            args.chin_y,
            boundary_y,
            args.knee_y,
            args.soles_y,
        )
        for crown_y in structural_values
        for boundary_y in boundary_values
    ]
    best = body_metrics(
        args.structural_crown_best_y,
        args.chin_y,
        args.crotch_pelvis_boundary_best_y,
        args.knee_y,
        args.soles_y,
    )

    exact_crown = (
        args.structural_crown_min_y
        == args.structural_crown_best_y
        == args.structural_crown_max_y
    )
    exact_boundary = (
        args.crotch_pelvis_boundary_min_y
        == args.crotch_pelvis_boundary_best_y
        == args.crotch_pelvis_boundary_max_y
    )
    exact_combined = exact_crown and exact_boundary

    head_min, head_max = metric_interval([m["head_ratio_heads"] for m in head_samples])
    head_status = classify_interval(
        head_min,
        head_max,
        gates["acceptable_heads_min"],
        gates["acceptable_heads_max"],
        exact=exact_crown,
    )

    inseam_min, inseam_max = metric_interval(
        [m["inseam_proxy_ratio"] for m in combined_metrics]
    )
    inseam_status = classify_interval(
        inseam_min,
        inseam_max,
        gates["inseam_proxy_target_min"],
        gates["inseam_proxy_target_max"],
        exact=exact_combined,
    )

    torso_min, torso_max = metric_interval(
        [m["chin_to_crotch_pelvis_boundary_heads"] for m in combined_metrics]
    )
    torso_status = classify_interval(
        torso_min,
        torso_max,
        gates["torso_chin_to_crotch_heads_min"],
        gates["torso_chin_to_crotch_heads_max"],
        exact=exact_combined,
    )

    boundary_to_knee_heads_min, boundary_to_knee_heads_max = metric_interval(
        [m["crotch_pelvis_boundary_to_knee_heads"] for m in combined_metrics]
    )
    knee_to_soles_heads_min, knee_to_soles_heads_max = metric_interval(
        [m["knee_to_soles_heads"] for m in combined_metrics]
    )
    boundary_to_knee_share_min, boundary_to_knee_share_max = metric_interval(
        [m["crotch_pelvis_boundary_to_knee_share"] for m in combined_metrics]
    )
    knee_to_soles_share_min, knee_to_soles_share_max = metric_interval(
        [m["knee_to_soles_share"] for m in combined_metrics]
    )

    horizontal_geometry = parse_widths(args, best["figure_height_px"])

    report: dict[str, Any] = {
        "schema": SCHEMA,
        "authority_status": "DIAGNOSTIC_ONLY",
        "mode": "body",
        "input": {
            "image": str(image_path),
            "sha256": sha256_file(image_path),
            "image_size": [width, height],
        },
        "landmarks": {
            "visible_hair_crown_y": args.visible_hair_crown_y,
            "structural_crown": {
                "min_y": args.structural_crown_min_y,
                "best_y": args.structural_crown_best_y,
                "max_y": args.structural_crown_max_y,
            },
            "chin_y": args.chin_y,
            "crotch_pelvis_boundary_proxy": {
                "min_y": args.crotch_pelvis_boundary_min_y,
                "best_y": args.crotch_pelvis_boundary_best_y,
                "max_y": args.crotch_pelvis_boundary_max_y,
                "measurement_definition": (
                    "central medial-thigh bifurcation / upper-lower body boundary"
                ),
                "garment_line_authority": "DENIED",
            },
            "knee_y": args.knee_y,
            "soles_y": args.soles_y,
        },
        "head_ratio": {
            "best": best["head_ratio_heads"],
            "min": head_min,
            "max": head_max,
            "current_target": gates["target_heads"],
            "current_gate_min": gates["acceptable_heads_min"],
            "current_gate_max": gates["acceptable_heads_max"],
            "status": head_status,
        },
        "inseam_proxy": {
            "best": best["inseam_proxy_ratio"],
            "best_percent": best["inseam_proxy_ratio"] * 100.0,
            "range": [inseam_min, inseam_max],
            "range_percent": [inseam_min * 100.0, inseam_max * 100.0],
            "current_gate": [
                gates["inseam_proxy_target_min"],
                gates["inseam_proxy_target_max"],
            ],
            "current_gate_percent": [
                gates["inseam_proxy_target_min"] * 100.0,
                gates["inseam_proxy_target_max"] * 100.0,
            ],
            "model_like_hard_fail_min": gates["inseam_proxy_model_like_hard_fail_min"],
            "model_like_hard_fail_min_percent": gates[
                "inseam_proxy_model_like_hard_fail_min"
            ]
            * 100.0,
            "model_like_hard_fail_best": best["inseam_proxy_ratio"]
            >= gates["inseam_proxy_model_like_hard_fail_min"],
            "model_like_hard_fail_robust": inseam_min
            >= gates["inseam_proxy_model_like_hard_fail_min"],
            "status": inseam_status,
        },
        "chin_to_crotch_pelvis_boundary_heads": {
            "best": best["chin_to_crotch_pelvis_boundary_heads"],
            "range": [torso_min, torso_max],
            "current_gate": [
                gates["torso_chin_to_crotch_heads_min"],
                gates["torso_chin_to_crotch_heads_max"],
            ],
            "status": torso_status,
        },
        "lower_body_split": {
            "crotch_pelvis_boundary_to_knee_heads": {
                "best": best["crotch_pelvis_boundary_to_knee_heads"],
                "range": [boundary_to_knee_heads_min, boundary_to_knee_heads_max],
            },
            "knee_to_soles_heads": {
                "best": best["knee_to_soles_heads"],
                "range": [knee_to_soles_heads_min, knee_to_soles_heads_max],
            },
            "crotch_pelvis_boundary_to_knee_share_percent": {
                "best": best["crotch_pelvis_boundary_to_knee_share"] * 100.0,
                "range": [
                    boundary_to_knee_share_min * 100.0,
                    boundary_to_knee_share_max * 100.0,
                ],
            },
            "knee_to_soles_share_percent": {
                "best": best["knee_to_soles_share"] * 100.0,
                "range": [
                    knee_to_soles_share_min * 100.0,
                    knee_to_soles_share_max * 100.0,
                ],
            },
        },
        "horizontal_geometry": horizontal_geometry,
        "author_visual_review": {
            "overall_build_not_too_thin": AUTHOR_REVIEW_VALUES[args.overall_build],
            "chest_front_volume_matches_author_intent": AUTHOR_REVIEW_VALUES[
                args.chest_front_volume
            ],
        },
        "uncertainty_policy": {
            "structural_crown_samples": len(structural_values),
            "crotch_pelvis_boundary_samples": len(boundary_values),
            "combined_body_metric_samples": len(combined_metrics),
            "method": "FULL_3X3_CROWN_BY_BOUNDARY_COMBINATION",
        },
        "official_qa_replacement": False,
        "composition_execution_allowed": False,
        "master_promotion": "NO",
        "note": "Audit v2 is diagnostic until explicitly promoted by author approval.",
    }

    if args.visible_hair_crown_y is not None:
        visible_head_height = args.chin_y - args.visible_hair_crown_y
        structural_head_heights = [args.chin_y - y for y in structural_values]
        inflation_values = [visible_head_height / value for value in structural_head_heights]
        report["apparent_head_shell"] = {
            "visible_head_height_px": visible_head_height,
            "structural_head_height_best_px": args.chin_y
            - args.structural_crown_best_y,
            "hair_shell_inflation_best": visible_head_height
            / (args.chin_y - args.structural_crown_best_y),
            "hair_shell_inflation_range": [
                min(inflation_values),
                max(inflation_values),
            ],
        }

    return report


def add_width_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--shoulder-width-px", type=float)
    parser.add_argument("--ribcage-width-px", type=float)
    parser.add_argument("--chest-outer-width-px", type=float)
    parser.add_argument("--waist-width-px", type=float)
    parser.add_argument("--hip-width-px", type=float)
    parser.add_argument("--upper-thigh-left-width-px", type=float)
    parser.add_argument("--upper-thigh-right-width-px", type=float)
    parser.add_argument("--calf-left-width-px", type=float)
    parser.add_argument("--calf-right-width-px", type=float)
    parser.add_argument("--ankle-left-width-px", type=float)
    parser.add_argument("--ankle-right-width-px", type=float)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Parallel diagnostic YURA Body Geometry Audit v2. "
            "Does not replace the current official body_geometry_qa.py gate."
        )
    )
    parser.add_argument("image_path", type=Path)
    parser.add_argument("--mode", choices=["head-shell", "body"], required=True)
    parser.add_argument("--visible-hair-crown-y", type=float)
    parser.add_argument("--structural-crown-min-y", type=float, required=True)
    parser.add_argument("--structural-crown-best-y", type=float, required=True)
    parser.add_argument("--structural-crown-max-y", type=float, required=True)
    parser.add_argument("--chin-y", type=float, required=True)

    parser.add_argument("--crotch-pelvis-boundary-min-y", type=float)
    parser.add_argument("--crotch-pelvis-boundary-best-y", type=float)
    parser.add_argument("--crotch-pelvis-boundary-max-y", type=float)
    parser.add_argument("--knee-y", type=float)
    parser.add_argument("--soles-y", type=float)

    parser.add_argument(
        "--overall-build",
        choices=list(AUTHOR_REVIEW_VALUES),
        default="not-reviewed",
    )
    parser.add_argument(
        "--chest-front-volume",
        choices=list(AUTHOR_REVIEW_VALUES),
        default="not-reviewed",
    )
    parser.add_argument("--report-path", type=Path)
    add_width_arguments(parser)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    image_path = args.image_path.resolve()
    if not image_path.exists():
        raise RuntimeError(f"Image not found: {image_path}")
    width, height = load_image_size(image_path)

    validate_common_landmarks(
        visible_hair_crown_y=args.visible_hair_crown_y,
        structural_min_y=args.structural_crown_min_y,
        structural_best_y=args.structural_crown_best_y,
        structural_max_y=args.structural_crown_max_y,
        chin_y=args.chin_y,
        image_height=height,
    )

    boundary_args = (
        args.crotch_pelvis_boundary_min_y,
        args.crotch_pelvis_boundary_best_y,
        args.crotch_pelvis_boundary_max_y,
    )

    if args.mode == "head-shell":
        if args.visible_hair_crown_y is None:
            raise RuntimeError("head-shell mode requires --visible-hair-crown-y")
        if any(value is not None for value in (*boundary_args, args.knee_y, args.soles_y)):
            raise RuntimeError(
                "head-shell mode does not accept crotch-pelvis-boundary/knee/soles body landmarks"
            )
        report = build_head_shell_report(
            image_path=image_path,
            width=width,
            height=height,
            visible_hair_crown_y=args.visible_hair_crown_y,
            structural_min_y=args.structural_crown_min_y,
            structural_best_y=args.structural_crown_best_y,
            structural_max_y=args.structural_crown_max_y,
            chin_y=args.chin_y,
        )
    else:
        if any(value is None for value in (*boundary_args, args.knee_y, args.soles_y)):
            raise RuntimeError(
                "body mode requires --crotch-pelvis-boundary-min-y, "
                "--crotch-pelvis-boundary-best-y, --crotch-pelvis-boundary-max-y, "
                "--knee-y, and --soles-y"
            )
        validate_body_landmarks(
            chin_y=args.chin_y,
            boundary_min_y=args.crotch_pelvis_boundary_min_y,
            boundary_best_y=args.crotch_pelvis_boundary_best_y,
            boundary_max_y=args.crotch_pelvis_boundary_max_y,
            knee_y=args.knee_y,
            soles_y=args.soles_y,
            image_height=height,
        )
        gates = load_current_gate_config()
        report = build_body_report(
            args=args,
            image_path=image_path,
            width=width,
            height=height,
            gates=gates,
        )

    rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    print(rendered)
    if args.report_path is not None:
        report_path = args.report_path.resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
