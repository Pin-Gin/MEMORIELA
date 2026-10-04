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
            channel_hists[channel_index] = [a + b for a, b in zip(channel_hists[channel_index], hist)]
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
    return tuple(int(v) for v in bbox)


def load_numeric_body_geometry_gate(
    run_dir: Path,
    raw_path: Path,
    config: dict[str, Any],
    composition_cfg: dict[str, Any],
) -> dict[str, Any]:
    if composition_cfg.get("require_numeric_body_geometry_qa_pass") is not True:
        raise RuntimeError("numeric Body Geometry QA must be required before Composition")

    qa_cfg = config.get("body_geometry_qa") or {}
    report_name = str(
        composition_cfg.get(
            "body_geometry_qa_filename",
            qa_cfg.get("report_filename", "body_geometry_qa.json"),
        )
    )
    report_path = run_dir / report_name
    if not report_path.exists():
        raise RuntimeError(
            f"Numeric Body Geometry QA report not found: {report_path}. "
            "Run body_geometry_qa.py first."
        )

    report = json.loads(report_path.read_text(encoding="utf-8"))
    if report.get("pass") is not True or report.get("status") != "PASS":
        raise RuntimeError("Numeric Body Geometry QA is not PASS; Composition remains blocked")
    if report.get("landmarks_reviewed") is not True:
        raise RuntimeError("Numeric Body Geometry landmarks were not explicitly reviewed")
    if report.get("landmark_method") != "MANUAL_PIXEL_Y":
        raise RuntimeError("Unexpected Body Geometry landmark method")

    current_raw_sha = sha256_file(raw_path)
    if report.get("raw_sha256") != current_raw_sha:
        raise RuntimeError(
            "Numeric Body Geometry QA was recorded for a different RAW image; SHA-256 mismatch"
        )
    if report.get("raw_file") != raw_path.name:
        raise RuntimeError("Numeric Body Geometry QA raw filename mismatch")

    ratio = float(report["head_ratio_heads"])
    acceptable_min = float(qa_cfg["acceptable_heads_min"])
    acceptable_max = float(qa_cfg["acceptable_heads_max"])
    if not (acceptable_min <= ratio <= acceptable_max):
        raise RuntimeError(
            f"Numeric Body Geometry ratio {ratio:.6f} is outside {acceptable_min:.1f}–{acceptable_max:.1f}"
        )

    qa_path = run_dir / "qa.json"
    if not qa_path.exists():
        raise RuntimeError(f"qa.json not found: {qa_path}")
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    if qa.get("body_geometry_status") != "PASS_NUMERIC":
        raise RuntimeError("qa.json does not record body_geometry_status=PASS_NUMERIC")

    return report


def build_plan(raw_path: Path, cfg: dict[str, Any]) -> tuple[dict[str, Any], Any, tuple[int, int, int, int]]:
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
    raw_figure_width = raw_x1 - raw_x0
    raw_figure_height = raw_y1 - raw_y0
    if raw_figure_width <= 0 or raw_figure_height <= 0:
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
        "mode": "deterministic_uniform_raster_composition_v3",
        "body_geometry_gate": "NUMERIC_QA_PASS_PLUS_EXPLICIT_CONFIRMATION_REQUIRED_BEFORE_RESULT_CREATION",
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
    return plan, source, raw_bbox


def normalize(
    run_dir: Path,
    cfg: dict[str, Any],
    numeric_geometry_report: dict[str, Any],
) -> dict[str, Any]:
    from PIL import Image

    raw_path = run_dir / str(cfg["raw_filename"])
    final_path = run_dir / str(cfg["final_filename"])
    report_path = run_dir / str(cfg["report_filename"])
    plan_path = run_dir / str(cfg.get("plan_filename", "composition_postprocess_plan.json"))

    plan, source, _raw_bbox = build_plan(raw_path, cfg)
    plan["numeric_body_geometry_qa"] = {
        "status": numeric_geometry_report["status"],
        "head_ratio_heads": numeric_geometry_report["head_ratio_heads"],
        "raw_sha256": numeric_geometry_report["raw_sha256"],
    }
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    if not plan["raw_edge_clear"]:
        report = {
            **plan,
            "status": "FAIL",
            "pass": False,
            "error": "RAW subject touches or crosses edge guard; complete subject visibility cannot be guaranteed.",
        }
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        raise RuntimeError(report["error"])

    final_width = int(cfg["final_width"])
    final_height = int(cfg["final_height"])
    scaled_width, scaled_height = (int(v) for v in plan["scaled_source_canvas"])
    paste_x, paste_y = (int(v) for v in plan["paste_xy"])

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
        "numeric_body_geometry_qa_pass": True,
        "canvas_size": canvas.size == (final_width, final_height),
        "figure_occupancy": float(cfg["acceptable_figure_height_ratio_min"]) <= occupancy <= float(cfg["acceptable_figure_height_ratio_max"]),
        "top_margin": float(cfg["acceptable_margin_ratio_min"]) <= top_margin_ratio <= float(cfg["acceptable_margin_ratio_max"]),
        "bottom_margin": float(cfg["acceptable_margin_ratio_min"]) <= bottom_margin_ratio <= float(cfg["acceptable_margin_ratio_max"]),
        "horizontal_center_proxy": abs(center_error_px) <= int(cfg["horizontal_center_tolerance_px"]),
        "raw_subject_not_clipped": bool(plan["raw_edge_clear"]),
        "uniform_scale_only": True,
        "nonuniform_or_partwise_transform": False,
    }
    passed = (
        checks["numeric_body_geometry_qa_pass"]
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
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if not passed:
        raise RuntimeError(f"Deterministic Composition QA failed; inspect {report_path}")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply deterministic final Composition only after numeric RAW Body Geometry QA PASS."
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument(
        "--confirm-body-geometry-pass",
        action="store_true",
        help=(
            "Without this flag only a plan is written. With the flag, a matching numeric "
            "body_geometry_qa.json PASS is also mandatory before result.png can be created."
        ),
    )
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    cfg = config["composition_postprocess"]
    if not cfg.get("enabled") or cfg.get("mode") != "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS":
        raise RuntimeError("composition_postprocess is not configured for deferred Body Geometry QA gating")
    if cfg.get("require_explicit_body_geometry_pass") is not True:
        raise RuntimeError("explicit Body Geometry PASS must be required")
    if cfg.get("require_numeric_body_geometry_qa_pass") is not True:
        raise RuntimeError("numeric Body Geometry QA PASS must be required")

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

    plan_path = run_dir / str(cfg.get("plan_filename", "composition_postprocess_plan.json"))
    plan, _source, _bbox = build_plan(raw_path, cfg)
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")

    if not args.confirm_body_geometry_pass:
        qa_file = run_dir / str(cfg.get("body_geometry_qa_filename", "body_geometry_qa.json"))
        qa_state = "NOT_RECORDED"
        if qa_file.exists():
            try:
                recorded = json.loads(qa_file.read_text(encoding="utf-8"))
                qa_state = str(recorded.get("status", "UNKNOWN"))
            except Exception:
                qa_state = "INVALID"
        print(json.dumps({
            "status": "PLAN_ONLY",
            "result_created": False,
            "run_dir": str(run_dir),
            "raw_image": str(raw_path),
            "numeric_body_geometry_qa_status": qa_state,
            "source_subject_bbox": plan["source_subject_bbox"],
            "source_figure_occupancy": plan["source_figure_occupancy"],
            "uniform_scale": plan["uniform_scale"],
            "next": (
                "Run body_geometry_qa.py with reviewed crown/chin/soles landmarks. "
                "Only after numeric PASS and remaining visual Body Geometry review, rerun with --confirm-body-geometry-pass."
            ),
        }, ensure_ascii=False, indent=2))
        return 0

    numeric_geometry_report = load_numeric_body_geometry_gate(run_dir, raw_path, config, cfg)
    report = normalize(run_dir, cfg, numeric_geometry_report)

    qa_path = run_dir / "qa.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    qa["body_geometry_status"] = "PASS_NUMERIC_AND_EXPLICITLY_CONFIRMED"
    qa["composition_status"] = "PASS"
    qa["normalized_image"] = str(cfg["final_filename"])
    qa["master_promotion"] = "NO"
    qa["author_pass"] = None
    qa["notes"] = (
        "RAW numeric Body Geometry QA passed and Body Geometry was explicitly confirmed before deterministic Composition. "
        "Composition PASS does not approve or promote the Master; remaining identity/visual QA and explicit author confirmation are still required."
    )
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "status": "NORMALIZED",
        "result_created": True,
        "run_dir": str(run_dir),
        "raw_image": str(raw_path),
        "final_image": str(run_dir / str(cfg["final_filename"])),
        "body_geometry_head_ratio": numeric_geometry_report["head_ratio_heads"],
        "uniform_scale": report["uniform_scale"],
        "final_figure_occupancy": report["final_figure_occupancy"],
        "final_top_margin_ratio": report["final_top_margin_ratio"],
        "final_bottom_margin_ratio": report["final_bottom_margin_ratio"],
        "final_center_error_px": report["final_center_error_px"],
        "master_promotion": "NO",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
