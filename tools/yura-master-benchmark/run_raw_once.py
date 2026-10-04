from __future__ import annotations

import argparse
import base64
import hashlib
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
    "RAW GENERATION IS BODY-GEOMETRY-FIRST.",
    "FINAL COMPOSITION IS DEFERRED TO DETERMINISTIC POST-PROCESSING.",
    "DO NOT OPTIMIZE FOR FINAL CANVAS OCCUPANCY OR MARGINS DURING GENERATION.",
    "DO NOT ALTER INTERNAL BODY LANDMARK POSITIONS FOR CANVAS FITTING.",
    "ONE HEAD IS CROWN TO CHIN.",
    "CROWN TO SOLES MUST BE 7.2 HEADS.",
    "BODY-GEOMETRY REFERENCE SCALE OVERRIDES DEFAULT LARGE-HEAD ANIME BODY PROPORTIONS.",
    "DO NOT ACHIEVE 7.2 BY LENGTHENING ONLY LEGS OR ONLY TORSO.",
    "7.2 heads",
    "7.1–7.3",
)

FORBIDDEN_GENERATION_COMPOSITION_LITERALS: tuple[str, ...] = (
    "1440 × 2560",
    "89%",
    "88–90%",
    "5–6%",
    "2278",
    "2253",
    "2304",
    "CENTER AXIS X",
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


def parse_codex_trace(text: str) -> list[dict[str, Any]]:
    usage: list[dict[str, Any]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        collect_usage_objects(event, usage)
    return usage


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


def write_failure(
    run_dir: Path,
    phase: str,
    errors: list[str],
    image_api_called: bool,
) -> None:
    (run_dir / "failure.json").write_text(
        json.dumps(
            {
                "phase": phase,
                "ready": False,
                "errors": errors,
                "image_api_called": image_api_called,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def validate_runtime_config(config: dict[str, Any]) -> None:
    body_cfg = config.get("body_geometry_qa")
    if not isinstance(body_cfg, dict) or body_cfg.get("enabled") is not True:
        raise RuntimeError("body_geometry_qa must be enabled")
    if body_cfg.get("landmark_method") != "MANUAL_PIXEL_Y":
        raise RuntimeError("body_geometry_qa landmark_method must be MANUAL_PIXEL_Y")
    if float(body_cfg.get("target_heads", -1)) != 7.2:
        raise RuntimeError("body_geometry_qa target_heads must be 7.2")
    if float(body_cfg.get("acceptable_heads_min", -1)) != 7.1:
        raise RuntimeError("body_geometry_qa acceptable_heads_min must be 7.1")
    if float(body_cfg.get("acceptable_heads_max", -1)) != 7.3:
        raise RuntimeError("body_geometry_qa acceptable_heads_max must be 7.3")
    if body_cfg.get("require_landmarks_reviewed") is not True:
        raise RuntimeError("body_geometry_qa must require reviewed landmarks")
    if body_cfg.get("require_raw_sha_match_before_composition") is not True:
        raise RuntimeError("body_geometry_qa must require RAW SHA match before Composition")

    comp_cfg = config.get("composition_postprocess")
    if not isinstance(comp_cfg, dict) or comp_cfg.get("enabled") is not True:
        raise RuntimeError("composition_postprocess must be enabled")
    if comp_cfg.get("mode") != "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS":
        raise RuntimeError("composition_postprocess mode must be DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS")
    if comp_cfg.get("require_explicit_body_geometry_pass") is not True:
        raise RuntimeError("composition_postprocess must require explicit Body Geometry PASS")
    if comp_cfg.get("require_numeric_body_geometry_qa_pass") is not True:
        raise RuntimeError("composition_postprocess must require numeric Body Geometry QA PASS")
    if str(comp_cfg.get("body_geometry_qa_filename")) != str(body_cfg.get("report_filename")):
        raise RuntimeError("Body Geometry QA report filename mismatch between config sections")

    expected_composition = {
        "final_width": 1440,
        "final_height": 2560,
        "target_figure_height_ratio": 0.89,
        "acceptable_figure_height_ratio_min": 0.88,
        "acceptable_figure_height_ratio_max": 0.90,
        "acceptable_margin_ratio_min": 0.05,
        "acceptable_margin_ratio_max": 0.06,
        "horizontal_center_x": 720,
    }
    for key, value in expected_composition.items():
        if comp_cfg.get(key) != value:
            raise RuntimeError(f"composition_postprocess {key} must equal Authority value {value!r}")
    if comp_cfg.get("resample") != "LANCZOS":
        raise RuntimeError("composition_postprocess resample must be LANCZOS")
    if str(comp_cfg.get("raw_filename")) != "result_raw.png":
        raise RuntimeError("composition_postprocess raw_filename must be result_raw.png")
    if str(comp_cfg.get("final_filename")) != "result.png":
        raise RuntimeError("composition_postprocess final_filename must be result.png")
    if str(config["image_api"]["size"]) != "1440x2560":
        raise RuntimeError("Image API raw canvas must remain 1440x2560 for this benchmark condition")


def validate_compiled_prompt(run_dir: Path, compiled_prompt: str) -> None:
    missing = [value for value in REQUIRED_PROMPT_INVARIANTS if value not in compiled_prompt]
    forbidden_present = [
        value for value in FORBIDDEN_GENERATION_COMPOSITION_LITERALS if value in compiled_prompt
    ]
    passed = not missing and not forbidden_present
    report = {
        "pass": passed,
        "required": list(REQUIRED_PROMPT_INVARIANTS),
        "missing": missing,
        "forbidden_generation_composition_literals": list(FORBIDDEN_GENERATION_COMPOSITION_LITERALS),
        "forbidden_present": forbidden_present,
        "image_api_allowed": passed,
        "body_geometry_numeric_gate": "REQUIRED_AFTER_RAW_GENERATION",
        "composition_execution": "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS",
    }
    (run_dir / "prompt_invariant_check.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    if not passed:
        errors = [
            *[f"compiled prompt missing required invariant: {v}" for v in missing],
            *[f"compiled prompt leaked deferred Composition target: {v}" for v in forbidden_present],
        ]
        write_failure(run_dir, "compiled_prompt_invariant_check", errors, False)
        raise RuntimeError("Compiled prompt invariant check failed: " + "; ".join(errors))


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
        path = root / rel
        entry: dict[str, Any] = {
            "order": index,
            "path": rel,
            "role": AUTHORITY_ROLES[rel],
            "sha256": local_hashes[rel],
        }
        if path.suffix.lower() == ".png":
            entry.update(
                {
                    "kind": "binary_image_reference",
                    "content_in_bundle": False,
                    "content_note": "Binary pixels are passed only to the later Image API call.",
                }
            )
        else:
            entry.update(
                {
                    "kind": "text_authority",
                    "content_in_bundle": True,
                    "content": path.read_text(encoding="utf-8"),
                }
            )
        entries.append(entry)

    return {
        "bundle_version": 4,
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
            "raw_body_geometry_numeric_qa_required": True,
            "composition_execution": "DEFERRED_DETERMINISTIC_POSTPROCESS_AFTER_NUMERIC_BODY_GEOMETRY_QA_PASS",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Exit before any paid Codex or Image API call.",
    )
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    validate_runtime_config(config)
    root = Path(run(["git", "rev-parse", "--show-toplevel"], TOOL_DIR).stdout.strip())

    run(["git", "fetch", "origin", "main"], root)
    head = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
    origin_main = run(["git", "rev-parse", "origin/main"], root).stdout.strip()
    if head != origin_main:
        raise RuntimeError(
            f"local HEAD is not current origin/main: HEAD={head} origin/main={origin_main}"
        )

    authority_paths = [str(x) for x in config["authority_order"]]
    dirty = run(
        ["git", "status", "--porcelain", "--", *authority_paths],
        root,
    ).stdout.strip()
    if dirty:
        raise RuntimeError("Authority files have uncommitted changes; aborting:\n" + dirty)

    local_hashes: dict[str, str] = {}
    for rel in authority_paths:
        path = root / rel
        if not path.exists():
            raise RuntimeError(f"required Authority missing: {rel}")
        local_hashes[rel] = sha256_file(path)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    runs_dir = root / config["runs_dir"]
    run_dir = runs_dir / f"run_{stamp}"
    suffix = 1
    while run_dir.exists():
        run_dir = runs_dir / f"run_{stamp}_{suffix:02d}"
        suffix += 1
    run_dir.mkdir(parents=True)

    bundle = build_sealed_bundle(root, head, config, authority_paths, local_hashes)
    bundle_text = json.dumps(bundle, ensure_ascii=False, indent=2)
    bundle_sha = sha256_text(bundle_text)
    (run_dir / "sealed_authority_bundle.json").write_text(bundle_text, encoding="utf-8")
    (run_dir / "sealed_authority_bundle.sha256").write_text(bundle_sha + "\n", encoding="ascii")

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
        "body_geometry_numeric_gate": "REQUIRED_AFTER_RAW_GENERATION",
        "composition_execution": "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS",
    }
    (run_dir / "run_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    codex_input = (
        INSTRUCTION_PATH.read_text(encoding="utf-8")
        + "\n\n<SEALED_AUTHORITY_BUNDLE_JSON>\n"
        + bundle_text
        + "\n</SEALED_AUTHORITY_BUNDLE_JSON>\n"
    )
    codex_input_sha = sha256_text(codex_input)
    (run_dir / "codex_input.sha256").write_text(codex_input_sha + "\n", encoding="ascii")

    if args.preflight_only:
        print(
            json.dumps(
                {
                    "status": "PREFLIGHT_OK",
                    "paid_model_calls": 0,
                    "run_dir": str(run_dir),
                    "git_commit": head,
                    "authority_count": len(authority_paths),
                    "sealed_authority_bundle_sha256": bundle_sha,
                    "codex_input_sha256": codex_input_sha,
                    "body_geometry_numeric_gate": "REQUIRED_AFTER_RAW_GENERATION",
                    "composition_execution": "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS",
                    "next": "Run without --preflight-only only after reviewing this preflight result.",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
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
    codex_usage = parse_codex_trace(codex.stdout)
    (run_dir / "codex_usage_candidates.json").write_text(
        json.dumps(codex_usage, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if codex.returncode != 0:
        write_failure(
            run_dir,
            "codex_prompt_compile",
            [f"Codex process exited with code {codex.returncode}"],
            False,
        )
        raise RuntimeError(f"Codex failed; inspect {run_dir / 'codex_stderr.log'}")
    if not manifest_path.exists():
        write_failure(
            run_dir,
            "codex_prompt_compile",
            ["Codex completed without authority_manifest.json"],
            False,
        )
        raise RuntimeError("Codex completed without authority_manifest.json")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not manifest.get("ready"):
        errors = [str(x) for x in manifest.get("errors", [])]
        write_failure(run_dir, "codex_prompt_compile", errors, False)
        raise RuntimeError("Codex reported ready=false: " + "; ".join(errors))
    if manifest.get("git_commit") != head:
        raise RuntimeError("Codex manifest git_commit does not match current HEAD")

    reported = manifest.get("authority_order", [])
    if [item.get("path") for item in reported] != authority_paths:
        raise RuntimeError("Codex Authority order mismatch")
    for index, item in enumerate(reported, start=1):
        path = item["path"]
        if item.get("order") != index:
            raise RuntimeError(f"Codex Authority ordinal mismatch: {path}")
        if item.get("sha256", "").lower() != local_hashes[path].lower():
            raise RuntimeError(f"Codex Authority SHA-256 mismatch: {path}")
        if item.get("role") != AUTHORITY_ROLES[path]:
            raise RuntimeError(f"Codex Authority role mismatch: {path}")

    if manifest.get("denied_sources") != [str(x) for x in config["denied_sources"]]:
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
        for ref in refs:
            ref.close()

    if not result.data or not result.data[0].b64_json:
        raise RuntimeError("Image API returned no image")

    result_dict = jsonable(result)
    post_cfg = config["composition_postprocess"]
    body_cfg = config["body_geometry_qa"]
    raw_filename = str(post_cfg["raw_filename"])
    raw_path = run_dir / raw_filename
    raw_path.write_bytes(base64.b64decode(result.data[0].b64_json))

    response_for_log = json.loads(json.dumps(result_dict))
    for item in response_for_log.get("data", []):
        if "b64_json" in item:
            item["b64_json"] = f"<saved to {raw_filename}>"
    (run_dir / "image_response.json").write_text(
        json.dumps(response_for_log, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    (run_dir / "composition_deferred.json").write_text(
        json.dumps(
            {
                "status": "DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS",
                "raw_image": raw_filename,
                "raw_sha256": sha256_file(raw_path),
                "numeric_body_geometry_qa_required": True,
                "body_geometry_qa_tool": "tools/yura-master-benchmark/body_geometry_qa.py",
                "body_geometry_qa_file": str(body_cfg["report_filename"]),
                "normalized_image": None,
                "normalizer": "tools/yura-master-benchmark/normalize_composition.py",
                "requires_explicit_body_geometry_pass": True,
                "note": (
                    "Do not create result.png until numeric RAW Body Geometry QA passes and remaining Body Geometry is explicitly confirmed. "
                    "Final Composition is a separate deterministic whole-raster scale/translate step."
                ),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    usage = response_for_log.get("usage") if isinstance(response_for_log, dict) else None
    image_estimate = estimate_image_cost(usage, config["pricing_snapshot"]["image_model"])
    ended_at = int(time.time())
    (run_dir / "cost.json").write_text(
        json.dumps(
            {
                "billing_status": "ESTIMATE_ONLY_UNTIL_PROJECT_COST_QUERY",
                "codex_usage_candidates": codex_usage,
                "image_usage": usage,
                "image_estimated_cost_usd": image_estimate,
                "run_specific_authoritative_cost_usd": None,
                "authoritative_project_day_cost_usd": None,
                "pricing_snapshot_as_of": config["pricing_snapshot"]["as_of"],
                "started_at_unix": started_at,
                "ended_at_unix": ended_at,
                "note": "Use query_project_cost.py for daily project-cost reconciliation; do not claim daily buckets as run-specific authoritative cost.",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    (run_dir / "qa.json").write_text(
        json.dumps(
            {
                "candidate": "QA_PENDING",
                "master_promotion": "NO",
                "body_geometry_status": "PENDING_NUMERIC_QA",
                "body_geometry_qa_file": str(body_cfg["report_filename"]),
                "composition_status": "BLOCKED_PENDING_BODY_GEOMETRY",
                "raw_image": raw_filename,
                "normalized_image": None,
                "auto_checks": {},
                "auto_pass": False,
                "author_pass": None,
                "notes": (
                    "Measure crown/chin/soles on result_raw.png with body_geometry_qa.py. "
                    "Composition remains blocked unless the numeric 7.1–7.3 gate passes and the RAW SHA matches."
                ),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "run_dir": str(run_dir),
                "git_commit": head,
                "sealed_authority_bundle_sha256": bundle_sha,
                "compiled_prompt_sha256": prompt_sha,
                "raw_image_path": str(raw_path),
                "normalized_image_path": None,
                "body_geometry_status": "PENDING_NUMERIC_QA",
                "composition_status": "BLOCKED_PENDING_BODY_GEOMETRY",
                "image_estimated_cost_usd": image_estimate,
                "next": (
                    f"Measure crown/chin/soles and run: python {TOOL_DIR / 'body_geometry_qa.py'} {run_dir} "
                    "--crown-y <Y> --chin-y <Y> --soles-y <Y> --confirm-landmarks-reviewed"
                ),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
