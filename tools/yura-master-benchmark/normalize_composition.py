from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"

PASS_INTERVAL_STATUSES = {"EXACT_PASS", "PASS_ROBUST"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _median_from_histogram(hist: list[int]) -> int:
    total = sum(hist)
    if total <= 0:
        raise RuntimeError("empty background sample")
    target = (total + 1) // 2
    acc = 0
    for value, count in enumerate(hist):
        acc += count
        if acc >= target:
            return value
    return 255


def estimate_background_rgb(image: Any, corner_sample_px: int) -> tuple[int, int, int]:
    width, height = image.size
    sample = max(1, min(int(corner_sample_px), width // 4, height // 4))
    boxes = (
        (0, 0, sample, sample),
        (width - sample, 0, width, sample),
        (0, height - sample, sample, height),
        (width - sample, height - sample, width, height),
    )
    channel_hists = [[0] * 256 for _ in range(3)]
    for box in boxes:
        crop = image.crop(box).convert("RGB")
        for channel_index, channel in enumerate(crop.split()):
            hist = channel.histogram()
            channel_hists[channel_index] = [
                a + b for a, b in zip(channel_hists[channel_index], hist)
            ]
    return tuple(_median_from_histogram(hist) for hist in channel_hists)  # type: ignore[return-value]


def detect_subject_bbox(
    image: Any,
    background_rgb: tuple[int, int, int],
    difference_threshold: int,
    median_filter_size: int,
) -> tuple[int, int, int, int]:
    from PIL import Image, ImageChops, ImageFilter

    rgb = image.convert("RGB")
    background = Image.new("RGB", rgb.size, background_rgb)
    diff = ImageChops.difference(rgb, background)
    red, green, blue = diff.split()
    max_diff = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    threshold = max(1, min(255, int(difference_threshold)))
    mask = max_diff.point(lambda value: 255 if value >= threshold else 0)
    if median_filter_size > 1:
        mask = mask.filter(ImageFilter.MedianFilter(size=median_filter_size))
    bbox = mask.getbbox()
    if bbox is None:
        raise RuntimeError("could not detect generated subject against white background")
    return tuple(int(value) for value in bbox)


def _require_interval_inside(
    name: str,
    gate: dict[str, Any],
    minimum: float,
    maximum: float,
) -> tuple[float, float]:
    if gate.get("status") not in PASS_INTERVAL_STATUSES:
        raise RuntimeError(
            f"{name} status {gate.get('status')} is not a Composition-eligible interval PASS"
        )
    if gate.get("pass") is not True:
        raise RuntimeError(f"{name} pass flag is not true")
    interval = gate.get("interval")
    if not isinstance(interval, list) or len(interval) != 2:
        raise RuntimeError(f"{name} interval is missing or invalid")
    value_min = float(interval[0])
    value_max = float(interval[1])
    if value_min > value_max:
        raise RuntimeError(f"{name} interval is reversed")
    if value_min < minimum or value_max > maximum:
        raise RuntimeError(
            f"{name} interval [{value_min:.6f}, {value_max:.6f}] is not fully inside "
            f"[{minimum:.6f}, {maximum:.6f}]"
        )
    return value_min, value_max


def load_body_geometry_gate(
    run_dir: Path,
    raw_path: Path,
    config: dict[str, Any],
    composition_cfg: dict[str, Any],
) -> dict[str, Any]:
    if composition_cfg.get("require_numeric_body_geometry_qa_pass") is not True:
        raise RuntimeError("numeric Body Geometry QA must be required before Composition")
    if composition_cfg.get("require_internal_body_geometry_review_pass") is not True:
        raise RuntimeError("internal Body Geometry review must be required before Composition")
    if composition_cfg.get("require_torso_specific_gate_pass") is not True:
        raise RuntimeError("torso-specific Body Geometry gate must be required before Composition")

    qa_cfg = config.get("body_geometry_qa") or {}
    if qa_cfg.get("landmark_method") != "MANUAL_PIXEL_Y_WITH_STRUCTURAL_UNCERTAINTY":
        raise RuntimeError("official Body Geometry QA must use structural uncertainty")
    if qa_cfg.get("interval_pass_policy") != "FULL_INTERVAL_MUST_BE_INSIDE_CURRENT_GATE":
        raise RuntimeError("official Body Geometry interval pass policy is unexpected")
    if qa_cfg.get("review_overlap_policy") != "BLOCK_COMPOSITION_PENDING_REVIEW":
        raise RuntimeError("official Body Geometry REVIEW_OVERLAP policy is unexpected")
    if qa_cfg.get("garment_line_landmark_authority") != "DENIED":
        raise RuntimeError("garment-line landmark authority must be denied")

    report_name = str(
        composition_cfg.get(
            "body_geometry_qa_filename",
            qa_cfg.get("report_filename", "body_geometry_qa.json"),
        )
    )
    report_path = run_dir / report_name
    if not report_path.exists():
        raise RuntimeError(
            f"Body Geometry QA report not found: {report_path}. Run body_geometry_qa.py first."
        )

    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("pass") is not True or report.get("status") != "PASS":
        raise RuntimeError("Body Geometry QA is not PASS; Composition remains blocked")
    if report.get("composition_execution_allowed") is not True:
        raise RuntimeError("Body Geometry QA did not authorize Composition execution")
    if report.get("landmarks_reviewed") is not True:
        raise RuntimeError("Body Geometry landmarks were not explicitly reviewed")
    if report.get("landmark_method") != "MANUAL_PIXEL_Y_WITH_STRUCTURAL_UNCERTAINTY":
        raise RuntimeError("Unexpected Body Geometry landmark method")

    landmarks = report.get("landmarks_y") or {}
    expected_landmark_keys = [
        "visible_hair_crown",
        "structural_crown",
        "chin",
        "crotch_pelvis_boundary",
        "knee",
        "soles",
    ]
    if list(landmarks.keys()) != expected_landmark_keys:
        raise RuntimeError(
            "Body Geometry QA must record visible_hair_crown/structural_crown/chin/"
            "crotch_pelvis_boundary/knee/soles in the official schema"
        )
    crown = landmarks.get("structural_crown") or {}
    if list(crown.keys()) != ["min", "best", "max"]:
        raise RuntimeError("structural_crown must record min/best/max")
    boundary = landmarks.get("crotch_pelvis_boundary") or {}
    if list(boundary.keys()) != [
        "min",
        "best",
        "max",
        "definition",
        "garment_line_authority",
    ]:
        raise RuntimeError("crotch_pelvis_boundary official schema is invalid")
    if boundary.get("definition") != qa_cfg.get("crotch_pelvis_boundary_definition"):
        raise RuntimeError("crotch/pelvis boundary definition mismatch")
    if boundary.get("garment_line_authority") != "DENIED":
        raise RuntimeError("crotch/pelvis boundary garment-line authority is not DENIED")

    current_raw_sha = sha256_file(raw_path)
    if report.get("raw_sha256") != current_raw_sha:
        raise RuntimeError(
            "Body Geometry QA was recorded for a different RAW image; SHA-256 mismatch"
        )
    if report.get("raw_file") != raw_path.name:
        raise RuntimeError("Body Geometry QA raw filename mismatch")

    acceptable_min = float(qa_cfg["acceptable_heads_min"])
    acceptable_max = float(qa_cfg["acceptable_heads_max"])
    head_gate = report.get("head_ratio_gate") or {}
    _require_interval_inside(
        "head ratio",
        head_gate,
        acceptable_min,
        acceptable_max,
    )

    inseam_min = float(qa_cfg["inseam_proxy_target_min"])
    inseam_max = float(qa_cfg["inseam_proxy_target_max"])
    hard_fail_min = float(qa_cfg["inseam_proxy_model_like_hard_fail_min"])
    inseam_gate = report.get("inseam_proxy_gate") or {}
    _, inseam_interval_max = _require_interval_inside(
        "inseam proxy",
        inseam_gate,
        inseam_min,
        inseam_max,
    )
    if inseam_interval_max >= hard_fail_min:
        raise RuntimeError(
            f"inseam proxy interval reaches model-like hard guard {hard_fail_min:.3f}"
        )
    if inseam_gate.get("model_like_hard_fail_best") is True:
        raise RuntimeError("inseam proxy best value triggered model-like hard guard")
    if inseam_gate.get("model_like_hard_fail_robust") is True:
        raise RuntimeError("inseam proxy interval robustly triggered model-like hard guard")

    torso_min = float(qa_cfg["torso_chin_to_crotch_heads_min"])
    torso_max = float(qa_cfg["torso_chin_to_crotch_heads_max"])
    torso_gate = report.get("torso_specific_gate") or {}
    _require_interval_inside(
        "chin-to-crotch/pelvis-boundary torso span",
        torso_gate,
        torso_min,
        torso_max,
    )
    if torso_gate.get("numeric_pass") is not True or torso_gate.get("pass") is not True:
        raise RuntimeError("torso-specific numeric/review gate is not PASS")

    numeric_gate = report.get("numeric_gate") or {}
    if numeric_gate.get("pass") is not True:
        raise RuntimeError("numeric Body Geometry gate is not PASS")

    internal_policy = report.get("internal_landmark_policy") or {}
    if internal_policy.get("review_pass") is not True:
        raise RuntimeError("Internal Body Geometry visual review is not PASS")
    review = internal_policy.get("review") or {}
    for key in (
        "upper_body_not_elongated",
        "torso_compact",
        "waist_not_low",
        "pelvis_high_enough",
        "lower_body_slightly_longer",
        "knee_placement_natural",
    ):
        if review.get(key) is not True:
            raise RuntimeError(f"Internal Body Geometry review missing PASS: {key}")

    author_visual = report.get("author_visual_gate") or {}
    if author_visual.get("pass") is not True:
        raise RuntimeError("Author visual Body Geometry gate is not PASS")
    if author_visual.get("overall_build_not_too_thin") != "PASS":
        raise RuntimeError("overall-build author visual gate is not PASS")
    if author_visual.get("chest_front_volume_matches_author_intent") != "PASS":
        raise RuntimeError("chest/front-volume author visual gate is not PASS")

    qa_path = run_dir / "qa.json"
    if not qa_path.exists():
        raise RuntimeError(f"qa.json not found: {qa_path}")
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    if qa.get("body_geometry_status") != "PASS":
        raise RuntimeError("qa.json does not record body_geometry_status=PASS")
    if qa.get("body_geometry_torso_specific_gate_pass") is not True:
        raise RuntimeError("qa.json does not record torso-specific Body Geometry PASS")
    if qa.get("body_geometry_internal_review_pass") is not True:
        raise RuntimeError("qa.json does not record internal Body Geometry review PASS")
    if qa.get("body_geometry_author_visual_gate_pass") is not True:
        raise RuntimeError("qa.json does not record author visual Body Geometry PASS")

    return report


def build_plan(raw_path: Path, cfg: dict[str, Any]) -> tuple[dict[str, Any], Any]:
    from PIL import Image

    with Image.open(raw_path) as source_image:
        source = source_image.convert("RGB")

    source_width, source_height = source.size
    background_rgb = estimate_background_rgb(source, int(cfg["corner_sample_px"]))
    raw_bbox = detect_subject_bbox(
        source,
        background_rgb,
        int(cfg["foreground_difference_threshold"]),
        int(cfg["median_filter_size"]),
    )
    raw_x0, raw_y0, raw_x1, raw_y1 = raw_bbox
    raw_figure_height = raw_y1 - raw_y0
    if raw_figure_height <= 0:
        raise RuntimeError("invalid RAW subject bounding box")

    edge_guard = int(cfg["raw_edge_guard_px"])
    raw_edge_clear = (
        raw_x0 > edge_guard
        and raw_y0 > edge_guard
        and raw_x1 < source_width - edge_guard
        and raw_y1 < source_height - edge_guard
    )

    final_width = int(cfg["final_width"])
    final_height = int(cfg["final_height"])
    target_figure_height = round(final_height * float(cfg["target_figure_height_ratio"]))
    scale = target_figure_height / raw_figure_height
    scaled_width = max(1, round(source_width * scale))
    scaled_height = max(1, round(source_height * scale))
    target_top_margin = round((final_height - target_figure_height) / 2)
    raw_center_x = (raw_x0 + raw_x1) / 2.0
    paste_x = round(float(cfg["horizontal_center_x"]) - raw_center_x * scale)
    paste_y = target_top_margin - round(raw_y0 * scale)

    plan = {
        "status": "PLAN_ONLY",
        "mode": "deterministic_uniform_raster_composition_v5",
        "body_geometry_gate": (
            "STRUCTURAL_UNCERTAINTY_HEAD_INSEAM_TORSO_PLUS_AUTHOR_VISUAL_GATE_REQUIRED"
        ),
        "source_file": raw_path.name,
        "source_sha256": sha256_file(raw_path),
        "source_canvas": [source_width, source_height],
        "source_background_rgb": list(background_rgb),
        "source_subject_bbox": list(raw_bbox),
        "source_figure_height_px": raw_figure_height,
        "source_figure_occupancy": raw_figure_height / source_height,
        "raw_edge_guard_px": edge_guard,
        "raw_edge_clear": raw_edge_clear,
        "target_canvas": [final_width, final_height],
        "target_figure_height_px": target_figure_height,
        "target_figure_height_ratio": float(cfg["target_figure_height_ratio"]),
        "uniform_scale": scale,
        "scaled_source_canvas": [scaled_width, scaled_height],
        "paste_xy": [paste_x, paste_y],
        "allowed_transforms": [
            "uniform whole-raster scaling",
            "x/y translation",
            "white-background crop/pad by final canvas placement",
        ],
        "forbidden_transforms": [
            "nonuniform scaling",
            "partwise scaling",
            "warp",
            "content-aware deformation",
            "inpainting/body reshaping",
            "face regeneration",
        ],
        "body_geometry_changed_by_composition": False,
    }
    return plan, source


def normalize(
    run_dir: Path,
    cfg: dict[str, Any],
    body_geometry_report: dict[str, Any],
) -> dict[str, Any]:
    from PIL import Image

    raw_path = run_dir / str(cfg["raw_filename"])
    final_path = run_dir / str(cfg["final_filename"])
    report_path = run_dir / str(cfg["report_filename"])
    plan_path = run_dir / str(
        cfg.get("plan_filename", "composition_postprocess_plan.json")
    )

    plan, source = build_plan(raw_path, cfg)
    metrics = body_geometry_report.get("metrics") or {}
    head_gate = body_geometry_report.get("head_ratio_gate") or {}
    inseam_gate = body_geometry_report.get("inseam_proxy_gate") or {}
    torso_gate = body_geometry_report.get("torso_specific_gate") or {}
    plan["body_geometry_qa"] = {
        "status": body_geometry_report["status"],
        "head_ratio_best": head_gate.get("best"),
        "head_ratio_interval": head_gate.get("interval"),
        "head_ratio_status": head_gate.get("status"),
        "chin_to_crotch_pelvis_boundary_best": torso_gate.get("best"),
        "chin_to_crotch_pelvis_boundary_interval": torso_gate.get("interval"),
        "torso_status": torso_gate.get("status"),
        "inseam_proxy_best": inseam_gate.get("best"),
        "inseam_proxy_interval": inseam_gate.get("interval"),
        "inseam_status": inseam_gate.get("status"),
        "torso_specific_gate_pass": torso_gate.get("pass"),
        "internal_review_pass": (
            body_geometry_report.get("internal_landmark_policy") or {}
        ).get("review_pass"),
        "author_visual_gate_pass": (
            body_geometry_report.get("author_visual_gate") or {}
        ).get("pass"),
        "raw_sha256": body_geometry_report["raw_sha256"],
        "best_metrics_compatibility": {
            "head_ratio_heads": metrics.get("head_ratio_heads"),
            "chin_to_crotch_heads": metrics.get("chin_to_crotch_heads"),
            "inseam_proxy_ratio": metrics.get("inseam_proxy_ratio"),
        },
    }
    plan_path.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if not plan["raw_edge_clear"]:
        raise RuntimeError(
            "RAW subject touches or crosses edge guard; complete subject visibility cannot be guaranteed"
        )

    final_width = int(cfg["final_width"])
    final_height = int(cfg["final_height"])
    scaled_width, scaled_height = (
        int(value) for value in plan["scaled_source_canvas"]
    )
    paste_x, paste_y = (int(value) for value in plan["paste_xy"])

    scaled = source.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (final_width, final_height), (255, 255, 255))
    canvas.paste(scaled, (paste_x, paste_y))
    canvas.save(final_path, format="PNG")

    final_bbox = detect_subject_bbox(
        canvas,
        (255, 255, 255),
        int(cfg["foreground_difference_threshold"]),
        int(cfg["median_filter_size"]),
    )
    final_x0, final_y0, final_x1, final_y1 = final_bbox
    final_figure_height = final_y1 - final_y0
    occupancy = final_figure_height / final_height
    top_margin_ratio = final_y0 / final_height
    bottom_margin_px = final_height - final_y1
    bottom_margin_ratio = bottom_margin_px / final_height
    detected_center_x = (final_x0 + final_x1) / 2.0
    target_center_x = float(cfg["horizontal_center_x"])
    center_error_px = detected_center_x - target_center_x

    checks = {
        "body_geometry_qa_pass": True,
        "torso_specific_gate_pass": True,
        "author_visual_gate_pass": True,
        "canvas_size": canvas.size == (final_width, final_height),
        "figure_occupancy": (
            float(cfg["acceptable_figure_height_ratio_min"])
            <= occupancy
            <= float(cfg["acceptable_figure_height_ratio_max"])
        ),
        "top_margin": (
            float(cfg["acceptable_margin_ratio_min"])
            <= top_margin_ratio
            <= float(cfg["acceptable_margin_ratio_max"])
        ),
        "bottom_margin": (
            float(cfg["acceptable_margin_ratio_min"])
            <= bottom_margin_ratio
            <= float(cfg["acceptable_margin_ratio_max"])
        ),
        "horizontal_center_proxy": abs(center_error_px)
        <= int(cfg["horizontal_center_tolerance_px"]),
        "raw_subject_not_clipped": bool(plan["raw_edge_clear"]),
        "uniform_scale_only": True,
        "nonuniform_or_partwise_transform": False,
    }
    passed = (
        checks["body_geometry_qa_pass"]
        and checks["torso_specific_gate_pass"]
        and checks["author_visual_gate_pass"]
        and checks["canvas_size"]
        and checks["figure_occupancy"]
        and checks["top_margin"]
        and checks["bottom_margin"]
        and checks["horizontal_center_proxy"]
        and checks["raw_subject_not_clipped"]
        and checks["uniform_scale_only"]
        and not checks["nonuniform_or_partwise_transform"]
    )

    report = {
        **plan,
        "status": "NORMALIZED" if passed else "FAIL",
        "pass": passed,
        "final_file": final_path.name,
        "final_sha256": sha256_file(final_path),
        "final_subject_bbox": list(final_bbox),
        "final_figure_height_px": final_figure_height,
        "final_figure_occupancy": occupancy,
        "final_top_margin_px": final_y0,
        "final_top_margin_ratio": top_margin_ratio,
        "final_bottom_margin_px": bottom_margin_px,
        "final_bottom_margin_ratio": bottom_margin_ratio,
        "final_detected_center_x": detected_center_x,
        "final_center_error_px": center_error_px,
        "checks": checks,
    }
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    if not passed:
        raise RuntimeError(
            f"Deterministic Composition QA failed; inspect {report_path}"
        )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Apply deterministic final Composition only after structural-uncertainty "
            "head-ratio, inseam-proxy, torso-specific, internal visual, and author visual "
            "Body Geometry gates are all PASS."
        )
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument(
        "--confirm-body-geometry-pass",
        action="store_true",
        help=(
            "Without this flag only a plan is written. With the flag, a matching "
            "body_geometry_qa.json PASS with robust interval and visual gates is mandatory."
        ),
    )
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    cfg = config["composition_postprocess"]
    if (
        not cfg.get("enabled")
        or cfg.get("mode") != "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS"
    ):
        raise RuntimeError(
            "composition_postprocess is not configured for deferred Body Geometry QA gating"
        )
    for key in (
        "require_explicit_body_geometry_pass",
        "require_numeric_body_geometry_qa_pass",
        "require_internal_body_geometry_review_pass",
        "require_torso_specific_gate_pass",
    ):
        if cfg.get(key) is not True:
            raise RuntimeError(f"composition_postprocess {key} must be true")

    try:
        import PIL  # noqa: F401
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required. Run: python -m pip install -r tools/yura-master-benchmark/requirements.txt"
        ) from exc

    run_dir = args.run_dir.resolve()
    raw_path = run_dir / str(cfg["raw_filename"])
    if not raw_path.exists():
        raise RuntimeError(f"RAW image not found: {raw_path}")

    plan_path = run_dir / str(
        cfg.get("plan_filename", "composition_postprocess_plan.json")
    )
    plan, _source = build_plan(raw_path, cfg)
    plan_path.write_text(
        json.dumps(plan, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if not args.confirm_body_geometry_pass:
        qa_file = run_dir / str(
            cfg.get("body_geometry_qa_filename", "body_geometry_qa.json")
        )
        qa_state = "NOT_RECORDED"
        if qa_file.exists():
            try:
                recorded = json.loads(qa_file.read_text(encoding="utf-8"))
                qa_state = str(recorded.get("status", "UNKNOWN"))
            except Exception:
                qa_state = "INVALID"
        print(
            json.dumps(
                {
                    "status": "PLAN_ONLY",
                    "result_created": False,
                    "run_dir": str(run_dir),
                    "raw_image": str(raw_path),
                    "body_geometry_qa_status": qa_state,
                    "source_subject_bbox": plan["source_subject_bbox"],
                    "source_figure_occupancy": plan["source_figure_occupancy"],
                    "uniform_scale": plan["uniform_scale"],
                    "next": (
                        "Run body_geometry_qa.py with structural-crown min/best/max, "
                        "crotch/pelvis-boundary min/best/max, internal confirmations, "
                        "and author build/chest visual states. Only a full interval PASS "
                        "may proceed to --confirm-body-geometry-pass."
                    ),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    body_geometry_report = load_body_geometry_gate(
        run_dir,
        raw_path,
        config,
        cfg,
    )
    report = normalize(run_dir, cfg, body_geometry_report)

    qa_path = run_dir / "qa.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    qa["body_geometry_status"] = "PASS"
    qa["body_geometry_torso_specific_gate_pass"] = True
    qa["body_geometry_internal_review_pass"] = True
    qa["body_geometry_author_visual_gate_pass"] = True
    qa["composition_status"] = "PASS"
    qa["normalized_image"] = str(cfg["final_filename"])
    qa["master_promotion"] = "NO"
    qa["author_pass"] = None
    qa["notes"] = (
        "Structural-uncertainty head-ratio, YURA inseam proxy, torso-specific, "
        "internal visual, and author build/chest Body Geometry QA all passed before "
        "deterministic Composition. Composition PASS still does not approve or promote "
        "the Master; remaining Face Identity, silhouette, visual QA and explicit final "
        "author confirmation are required."
    )
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "status": "NORMALIZED",
                "result_created": True,
                "run_dir": str(run_dir),
                "raw_image": str(raw_path),
                "final_image": str(run_dir / str(cfg["final_filename"])),
                "uniform_scale": report["uniform_scale"],
                "final_figure_occupancy": report["final_figure_occupancy"],
                "final_top_margin_ratio": report["final_top_margin_ratio"],
                "final_bottom_margin_ratio": report["final_bottom_margin_ratio"],
                "final_center_error_px": report["final_center_error_px"],
                "master_promotion": "NO",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
