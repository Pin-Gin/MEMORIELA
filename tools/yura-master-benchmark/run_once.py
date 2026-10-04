from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"
SCHEMA_PATH = TOOL_DIR / "authority_manifest.schema.json"
INSTRUCTION_PATH = TOOL_DIR / "codex_instruction.md"

AUTHORITY_ROLES: dict[str, str] = {
    "visuals/yura/identity/master/YURA_MASTER_GENERATION_LIFECYCLE.md": "MASTER-GENERATION LIFECYCLE / AUTHORITY TRANSITION RULES",
    "visuals/yura/identity/face/FACE_REFERENCE_RULES.md": "FACE IDENTITY RULES",
    "visuals/yura/identity/face/YURA_FACE_REFERENCE.png": "FACE IDENTITY ONLY",
    "visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md": "BODY GEOMETRY RULES",
    "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png": "BODY GEOMETRY ONLY",
    "visuals/yura/identity/master/YURA_VISUAL_TEXT.md": "MASTER-GENERATION API VISUAL SPECIFICATION",
    "visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md": "COMPOSITION ONLY",
}

REQUIRED_PROMPT_INVARIANTS: tuple[str, ...] = (
    "BODY GEOMETRY IS RESOLVED FIRST.",
    "BODY GEOMETRY HAS PRIORITY OVER COMPOSITION.",
    "WHOLE-FIGURE UNIFORM SCALING ONLY.",
    "DO NOT ALTER INTERNAL BODY LANDMARK POSITIONS TO SATISFY OCCUPANCY OR MARGINS.",
    "BODY GEOMETRY WINS; COMPOSITION MAY FAIL.",
    "RAW GENERATION MUST NOT ALTER BODY GEOMETRY TO SATISFY FINAL COMPOSITION.",
    "FINAL COMPOSITION IS APPLIED BY DETERMINISTIC RUNNER POSTPROCESS.",
    "POSTPROCESS MAY SCALE AND TRANSLATE THE COMPLETE RASTER ONLY.",
    "7.2 heads",
    "7.1–7.3",
    "1440 × 2560",
    "89%",
    "88–90%",
    "5–6%",
)


def run(
    cmd: list[str],
    cwd: Path,
    check: bool = True,
    input_text: str | None = None,
) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        input=input_text,
        capture_output=True,
    )
    if check and p.returncode != 0:
        raise RuntimeError(
            f"command failed ({p.returncode}): {' '.join(cmd)}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}"
        )
    return p


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def jsonable(obj: Any) -> Any:
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    return obj


def collect_usage_objects(value: Any, out: list[dict[str, Any]]) -> None:
    if isinstance(value, dict):
        usage = value.get("usage")
        if isinstance(usage, dict):
            out.append(usage)
        for v in value.values():
            collect_usage_objects(v, out)
    elif isinstance(value, list):
        for v in value:
            collect_usage_objects(v, out)


def parse_codex_trace(text: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    events: list[dict[str, Any]] = []
    usage: list[dict[str, Any]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict):
            events.append(event)
            collect_usage_objects(event, usage)
    return events, usage


def estimate_image_cost(usage: dict[str, Any] | None, rates: dict[str, float]) -> float | None:
    if not usage:
        return None
    inp = usage.get("input_tokens_details") or {}
    out = usage.get("output_tokens_details") or {}
    text_in = inp.get("text_tokens")
    image_in = inp.get("image_tokens")
    image_out = out.get("image_tokens")
    if text_in is None and image_in is None:
        return None
    if image_out is None:
        image_out = usage.get("output_tokens", 0)
    return round(
        (float(text_in or 0) / 1_000_000) * rates["text_input_per_1m_usd"]
        + (float(image_in or 0) / 1_000_000) * rates["image_input_per_1m_usd"]
        + (float(image_out or 0) / 1_000_000) * rates["image_output_per_1m_usd"],
        8,
    )


def write_failure(run_dir: Path, phase: str, errors: list[str], image_api_called: bool) -> None:
    failure = {
        "phase": phase,
        "ready": False,
        "errors": errors,
        "image_api_called": image_api_called,
    }
    (run_dir / "failure.json").write_text(
        json.dumps(failure, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def validate_compiled_prompt(run_dir: Path, compiled_prompt: str) -> None:
    missing = [value for value in REQUIRED_PROMPT_INVARIANTS if value not in compiled_prompt]
    report = {
        "pass": not missing,
        "required": list(REQUIRED_PROMPT_INVARIANTS),
        "missing": missing,
        "image_api_allowed": not missing,
    }
    (run_dir / "prompt_invariant_check.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if missing:
        errors = [f"compiled prompt missing required invariant: {value}" for value in missing]
        write_failure(run_dir, "compiled_prompt_invariant_check", errors, False)
        raise RuntimeError("Compiled prompt invariant check failed: " + "; ".join(missing))


def validate_postprocess_config(config: dict[str, Any]) -> None:
    cfg = config.get("composition_postprocess")
    if not isinstance(cfg, dict) or not cfg.get("enabled"):
        raise RuntimeError("composition_postprocess must be enabled for benchmark_version >= 2")

    expected = {
        "final_width": 1440,
        "final_height": 2560,
        "target_figure_height_ratio": 0.89,
        "acceptable_figure_height_ratio_min": 0.88,
        "acceptable_figure_height_ratio_max": 0.90,
        "acceptable_margin_ratio_min": 0.05,
        "acceptable_margin_ratio_max": 0.06,
        "horizontal_center_x": 720,
    }
    for key, value in expected.items():
        if cfg.get(key) != value:
            raise RuntimeError(f"composition_postprocess {key} must equal Authority value {value!r}")

    if cfg.get("resample") != "LANCZOS":
        raise RuntimeError("composition_postprocess resample must be LANCZOS")
    median_size = int(cfg.get("median_filter_size", 0))
    if median_size < 1 or median_size % 2 == 0:
        raise RuntimeError("composition_postprocess median_filter_size must be a positive odd integer")

    image_size = str(config["image_api"]["size"])
    if image_size != "1440x2560":
        raise RuntimeError("Image API raw canvas must remain 1440x2560 for this benchmark condition")

    if importlib.util.find_spec("PIL") is None:
        raise RuntimeError(
            "Pillow is required for deterministic composition postprocess. "
            "Run: python -m pip install -r tools/yura-master-benchmark/requirements.txt"
        )


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
    return tuple(int(v) for v in bbox)


def normalize_composition(
    raw_path: Path,
    final_path: Path,
    report_path: Path,
    cfg: dict[str, Any],
) -> dict[str, Any]:
    from PIL import Image

    with Image.open(raw_path) as source_image:
        source = source_image.convert("RGB")

    source_width, source_height = source.size
    corner_sample = int(cfg["corner_sample_px"])
    difference_threshold = int(cfg["foreground_difference_threshold"])
    median_filter_size = int(cfg["median_filter_size"])
    edge_guard = int(cfg["raw_edge_guard_px"])

    background_rgb = estimate_background_rgb(source, corner_sample)
    raw_bbox = detect_subject_bbox(
        source,
        background_rgb,
        difference_threshold,
        median_filter_size,
    )
    raw_x0, raw_y0, raw_x1, raw_y1 = raw_bbox
    raw_figure_width = raw_x1 - raw_x0
    raw_figure_height = raw_y1 - raw_y0
    if raw_figure_width <= 0 or raw_figure_height <= 0:
        raise RuntimeError("invalid RAW subject bounding box")

    raw_edge_clear = (
        raw_x0 > edge_guard
        and raw_y0 > edge_guard
        and raw_x1 < source_width - edge_guard
        and raw_y1 < source_height - edge_guard
    )
    if not raw_edge_clear:
        report = {
            "pass": False,
            "mode": "deterministic_uniform_raster_composition_v1",
            "error": "RAW subject touches or crosses edge guard; complete subject visibility cannot be guaranteed",
            "source_canvas": [source_width, source_height],
            "source_background_rgb": list(background_rgb),
            "source_subject_bbox": list(raw_bbox),
            "raw_edge_guard_px": edge_guard,
            "raw_edge_clear": False,
        }
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        raise RuntimeError(report["error"])

    final_width = int(cfg["final_width"])
    final_height = int(cfg["final_height"])
    target_ratio = float(cfg["target_figure_height_ratio"])
    target_figure_height = round(final_height * target_ratio)
    scale = target_figure_height / raw_figure_height

    scaled_width = max(1, round(source_width * scale))
    scaled_height = max(1, round(source_height * scale))
    scaled = source.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)

    target_top_margin = round((final_height - target_figure_height) / 2)
    raw_center_x = (raw_x0 + raw_x1) / 2.0
    target_center_x = float(cfg["horizontal_center_x"])
    paste_x = round(target_center_x - raw_center_x * scale)
    paste_y = target_top_margin - round(raw_y0 * scale)

    canvas = Image.new("RGB", (final_width, final_height), (255, 255, 255))
    canvas.paste(scaled, (paste_x, paste_y))
    canvas.save(final_path, format="PNG")

    final_background = (255, 255, 255)
    final_bbox = detect_subject_bbox(
        canvas,
        final_background,
        difference_threshold,
        median_filter_size,
    )
    final_x0, final_y0, final_x1, final_y1 = final_bbox
    final_figure_height = final_y1 - final_y0
    final_figure_width = final_x1 - final_x0
    occupancy = final_figure_height / final_height
    top_margin_ratio = final_y0 / final_height
    bottom_margin_px = final_height - final_y1
    bottom_margin_ratio = bottom_margin_px / final_height
    detected_center_x = (final_x0 + final_x1) / 2.0
    center_error_px = detected_center_x - target_center_x

    checks = {
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
        "horizontal_center_proxy": abs(center_error_px) <= int(cfg["horizontal_center_tolerance_px"]),
        "raw_subject_not_clipped": raw_edge_clear,
        "uniform_scale_only": True,
        "nonuniform_or_partwise_transform": False,
    }
    passed = all(bool(value) for key, value in checks.items() if key != "nonuniform_or_partwise_transform")

    report = {
        "pass": passed,
        "mode": "deterministic_uniform_raster_composition_v1",
        "source_file": raw_path.name,
        "final_file": final_path.name,
        "source_sha256": sha256_file(raw_path),
        "final_sha256": sha256_file(final_path),
        "source_canvas": [source_width, source_height],
        "source_background_rgb": list(background_rgb),
        "source_subject_bbox": list(raw_bbox),
        "source_figure_height_px": raw_figure_height,
        "source_figure_occupancy": raw_figure_height / source_height,
        "raw_edge_guard_px": edge_guard,
        "raw_edge_clear": raw_edge_clear,
        "operation": {
            "uniform_scale_factor": scale,
            "scaled_full_raw_canvas": [scaled_width, scaled_height],
            "translation_px": [paste_x, paste_y],
            "resample": cfg["resample"],
            "partwise_scaling": False,
            "warping": False,
            "inpainting": False,
        },
        "target": {
            "canvas": [final_width, final_height],
            "figure_height_ratio": target_ratio,
            "figure_height_px": target_figure_height,
            "top_bottom_margin_center_px": target_top_margin,
            "horizontal_center_x": target_center_x,
        },
        "final_subject_bbox": list(final_bbox),
        "final_figure_width_px": final_figure_width,
        "final_figure_height_px": final_figure_height,
        "final_figure_occupancy": occupancy,
        "final_top_margin_px": final_y0,
        "final_top_margin_ratio": top_margin_ratio,
        "final_bottom_margin_px": bottom_margin_px,
        "final_bottom_margin_ratio": bottom_margin_ratio,
        "final_detected_subject_center_x": detected_center_x,
        "final_center_error_px": center_error_px,
        "checks": checks,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if not passed:
        failed_checks = [key for key, value in checks.items() if key != "nonuniform_or_partwise_transform" and not value]
        raise RuntimeError("deterministic composition QA failed: " + ", ".join(failed_checks))

    return report


def build_sealed_bundle(
    root: Path,
    head: str,
    config: dict[str, Any],
    authority_paths: list[str],
    local_hashes: dict[str, str],
) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for index, rel in enumerate(authority_paths, start=1):
        if rel not in AUTHORITY_ROLES:
            raise RuntimeError(f"no deterministic Authority role mapping for: {rel}")

        p = root / rel
        entry: dict[str, Any] = {
            "order": index,
            "path": rel,
            "role": AUTHORITY_ROLES[rel],
            "sha256": local_hashes[rel],
        }
        if p.suffix.lower() == ".png":
            entry["kind"] = "binary_image_reference"
            entry["content_in_bundle"] = False
            entry["content_note"] = (
                "Binary pixels are intentionally not embedded in the Codex bundle. "
                "The runner passes this exact file to the Image API according to image_reference_order."
            )
        else:
            entry["kind"] = "text_authority"
            entry["content_in_bundle"] = True
            entry["content"] = p.read_text(encoding="utf-8")
        entries.append(entry)

    return {
        "bundle_version": 2,
        "bundle_mode": "SEALED_AUTHORITY_BUNDLE",
        "git_commit": head,
        "authority_order": entries,
        "denied_sources": [str(x) for x in config["denied_sources"]],
        "image_reference_order": [str(x) for x in config["image_reference_order"]],
        "compiler_boundary": {
            "runner_resolves_git": True,
            "runner_reads_authorities": True,
            "runner_computes_sha256": True,
            "codex_filesystem_access_required": False,
            "codex_shell_access_required": False,
            "codex_external_tools_required": False,
            "png_pixels_inspected_by_codex": False,
            "final_composition_enforced_by_runner": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Build and hash the sealed Authority bundle, validate deterministic composition runtime, then exit before any paid Codex or Image API call.",
    )
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    validate_postprocess_config(config)
    root = Path(run(["git", "rev-parse", "--show-toplevel"], TOOL_DIR).stdout.strip())

    run(["git", "fetch", "origin", "main"], root)
    head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
    origin_main = run(["git", "rev-parse", "origin/main"], root).stdout.strip()
    if head != origin_main:
        raise RuntimeError(f"local HEAD is not current origin/main: HEAD={head} origin/main={origin_main}")

    authority_paths = [str(x) for x in config["authority_order"]]
    dirty = run(["git", "status", "--porcelain", "--", *authority_paths], root).stdout.strip()
    if dirty:
        raise RuntimeError("Authority files have uncommitted changes; aborting:\n" + dirty)

    local_hashes: dict[str, str] = {}
    for rel in authority_paths:
        p = root / rel
        if not p.exists():
            raise RuntimeError(f"required Authority missing: {rel}")
        local_hashes[rel] = sha256_file(p)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"run_{stamp}"
    runs_dir = root / config["runs_dir"]
    run_dir = runs_dir / run_id
    suffix = 1
    while run_dir.exists():
        run_dir = runs_dir / f"{run_id}_{suffix:02d}"
        suffix += 1
    run_dir.mkdir(parents=True)

    bundle = build_sealed_bundle(root, head, config, authority_paths, local_hashes)
    bundle_text = json.dumps(bundle, ensure_ascii=False, indent=2)
    bundle_sha = sha256_text(bundle_text)
    (run_dir / "sealed_authority_bundle.json").write_text(bundle_text, encoding="utf-8")
    (run_dir / "sealed_authority_bundle.sha256").write_text(bundle_sha + "\n", encoding="ascii")

    post_cfg = config["composition_postprocess"]
    started_at = int(time.time())
    meta = {
        "run_id": run_dir.name,
        "started_at_unix": started_at,
        "started_at_utc": datetime.fromtimestamp(started_at, timezone.utc).isoformat(),
        "git_commit": head,
        "config_sha256": sha256_file(CONFIG_PATH),
        "authority_sha256": local_hashes,
        "sealed_authority_bundle_sha256": bundle_sha,
        "preflight_only": args.preflight_only,
        "codex_input_mode": "sealed_authority_bundle_via_stdin",
        "codex_user_config_loaded": False,
        "codex_tool_dependency": "NONE",
        "compiled_prompt_invariant_gate": True,
        "composition_pipeline": "RAW_IMAGE_API_THEN_DETERMINISTIC_UNIFORM_RASTER_COMPOSITION_V1",
        "composition_postprocess_config": post_cfg,
        "codex_sandbox": {
            "mode": "read-only",
            "purpose": "defense in depth only; compilation requires no shell/filesystem tools",
        },
    }
    (run_dir / "run_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    instruction = INSTRUCTION_PATH.read_text(encoding="utf-8")
    codex_input = (
        instruction
        + "\n\n<SEALED_AUTHORITY_BUNDLE_JSON>\n"
        + bundle_text
        + "\n</SEALED_AUTHORITY_BUNDLE_JSON>\n"
    )
    codex_input_sha = sha256_text(codex_input)
    (run_dir / "codex_input.sha256").write_text(codex_input_sha + "\n", encoding="ascii")

    if args.preflight_only:
        print(json.dumps({
            "status": "PREFLIGHT_OK",
            "paid_model_calls": 0,
            "run_dir": str(run_dir),
            "git_commit": head,
            "authority_count": len(authority_paths),
            "sealed_authority_bundle_sha256": bundle_sha,
            "codex_input_sha256": codex_input_sha,
            "composition_postprocess": "READY",
            "next": "Run without --preflight-only only after reviewing this preflight result.",
        }, ensure_ascii=False, indent=2))
        return 0

    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for paid Codex/Image API execution.")

    manifest_path = run_dir / "authority_manifest.json"
    codex_cmd = [
        config["codex"]["executable"],
        "exec",
        "--ignore-user-config",
        "--sandbox",
        "read-only",
        "--json",
        "--model",
        config["codex"]["model"],
        "--output-schema",
        str(SCHEMA_PATH),
        "-o",
        str(manifest_path),
    ]

    codex = run(codex_cmd, root, check=False, input_text=codex_input)
    (run_dir / "codex_trace.jsonl").write_text(codex.stdout, encoding="utf-8")
    (run_dir / "codex_stderr.log").write_text(codex.stderr, encoding="utf-8")
    _events, codex_usage = parse_codex_trace(codex.stdout)
    (run_dir / "codex_usage_candidates.json").write_text(
        json.dumps(codex_usage, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if codex.returncode != 0:
        write_failure(
            run_dir,
            "codex_prompt_compile",
            [f"Codex process exited with code {codex.returncode}; inspect codex_stderr.log"],
            False,
        )
        raise RuntimeError(f"Codex failed; inspect {run_dir / 'codex_stderr.log'}")
    if not manifest_path.exists():
        write_failure(run_dir, "codex_prompt_compile", ["Codex completed without authority_manifest.json"], False)
        raise RuntimeError("Codex completed without authority_manifest.json")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not manifest.get("ready"):
        errors = [str(x) for x in manifest.get("errors", [])]
        write_failure(run_dir, "codex_prompt_compile", errors, False)
        raise RuntimeError("Codex reported ready=false: " + "; ".join(errors))
    if manifest.get("git_commit") != head:
        write_failure(run_dir, "manifest_verification", ["Codex manifest git_commit does not match runner HEAD"], False)
        raise RuntimeError("Codex manifest git_commit does not match current HEAD")

    reported = manifest.get("authority_order", [])
    reported_paths = [x.get("path") for x in reported]
    if reported_paths != authority_paths:
        write_failure(run_dir, "manifest_verification", [f"Codex Authority order mismatch: {reported_paths}"], False)
        raise RuntimeError(f"Codex Authority order mismatch: {reported_paths}")

    for index, item in enumerate(reported, start=1):
        path = item["path"]
        if item.get("order") != index:
            raise RuntimeError(f"Codex Authority ordinal mismatch for {path}: {item.get('order')} != {index}")
        if item.get("sha256", "").lower() != local_hashes[path].lower():
            raise RuntimeError(f"Codex SHA-256 mismatch: {path}")
        if item.get("role") != AUTHORITY_ROLES[path]:
            raise RuntimeError(f"Codex Authority role mismatch: {path}")

    expected_denied = [str(x) for x in config["denied_sources"]]
    if manifest.get("denied_sources") != expected_denied:
        raise RuntimeError("Codex denied_sources mismatch")
    if manifest.get("image_reference_order") != config["image_reference_order"]:
        raise RuntimeError("Codex image_reference_order mismatch")

    compiled_prompt = manifest["compiled_prompt"]
    prompt_sha = sha256_text(compiled_prompt)
    (run_dir / "compiled_prompt.txt").write_text(compiled_prompt, encoding="utf-8")
    (run_dir / "compiled_prompt.sha256").write_text(prompt_sha + "\n", encoding="ascii")

    validate_compiled_prompt(run_dir, compiled_prompt)

    from openai import OpenAI

    client = OpenAI()
    refs = [open(root / rel, "rb") for rel in config["image_reference_order"]]
    try:
        image_cfg = config["image_api"]
        result = client.images.edit(
            model=image_cfg["model"],
            image=refs,
            prompt=compiled_prompt,
            size=image_cfg["size"],
            quality=image_cfg["quality"],
            output_format=image_cfg["output_format"],
            background=image_cfg["background"],
            n=image_cfg["n"],
        )
    finally:
        for f in refs:
            f.close()

    result_dict = jsonable(result)
    if not result.data or not result.data[0].b64_json:
        raise RuntimeError("Image API returned no image")
    image_bytes = base64.b64decode(result.data[0].b64_json)

    raw_path = run_dir / str(post_cfg["raw_filename"])
    final_path = run_dir / str(post_cfg["final_filename"])
    report_path = run_dir / str(post_cfg["report_filename"])
    raw_path.write_bytes(image_bytes)

    try:
        composition_report = normalize_composition(raw_path, final_path, report_path, post_cfg)
    except Exception as exc:
        write_failure(run_dir, "deterministic_composition_postprocess", [str(exc)], True)
        raise

    response_for_log = json.loads(json.dumps(result_dict))
    for item in response_for_log.get("data", []):
        if "b64_json" in item:
            item["b64_json"] = "<saved to result_raw.png; result.png is deterministic local composition postprocess>"
    (run_dir / "image_response.json").write_text(
        json.dumps(response_for_log, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    usage = response_for_log.get("usage") if isinstance(response_for_log, dict) else None
    image_estimate = estimate_image_cost(usage, config["pricing_snapshot"]["image_model"])
    ended_at = int(time.time())
    cost = {
        "billing_status": "ESTIMATE_ONLY_UNTIL_PROJECT_COST_QUERY",
        "codex_usage_candidates": codex_usage,
        "image_usage": usage,
        "image_estimated_cost_usd": image_estimate,
        "authoritative_total_project_cost_usd": None,
        "pricing_snapshot_as_of": config["pricing_snapshot"]["as_of"],
        "started_at_unix": started_at,
        "ended_at_unix": ended_at,
        "note": "Use query_project_cost.py with OPENAI_ADMIN_KEY and OPENAI_PROJECT_ID for daily project cost accounting; run-specific billing remains usage-based estimate unless the project/day is isolated.",
    }
    (run_dir / "cost.json").write_text(json.dumps(cost, ensure_ascii=False, indent=2), encoding="utf-8")

    qa = {
        "candidate": "QA_PENDING",
        "master_promotion": "NO",
        "auto_checks": {
            "deterministic_composition_postprocess": bool(composition_report.get("pass")),
            "final_canvas_1440x2560": bool(composition_report.get("checks", {}).get("canvas_size")),
            "final_occupancy_88_90": bool(composition_report.get("checks", {}).get("figure_occupancy")),
            "final_top_margin_5_6": bool(composition_report.get("checks", {}).get("top_margin")),
            "final_bottom_margin_5_6": bool(composition_report.get("checks", {}).get("bottom_margin")),
            "final_horizontal_center_proxy": bool(composition_report.get("checks", {}).get("horizontal_center_proxy")),
            "raw_subject_not_clipped": bool(composition_report.get("checks", {}).get("raw_subject_not_clipped")),
        },
        "author_pass": None,
        "notes": "Composition auto-checks apply only to final raster placement. Body geometry, face identity, ears, silhouette, and author review remain required before promotion.",
    }
    (run_dir / "qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "run_dir": str(run_dir),
        "git_commit": head,
        "sealed_authority_bundle_sha256": bundle_sha,
        "compiled_prompt_sha256": prompt_sha,
        "raw_image_path": str(raw_path),
        "image_path": str(final_path),
        "composition_postprocess_pass": bool(composition_report.get("pass")),
        "final_figure_occupancy": composition_report.get("final_figure_occupancy"),
        "final_top_margin_ratio": composition_report.get("final_top_margin_ratio"),
        "final_bottom_margin_ratio": composition_report.get("final_bottom_margin_ratio"),
        "image_estimated_cost_usd": image_estimate,
        "next": f"python {TOOL_DIR / 'query_project_cost.py'} {run_dir}",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
