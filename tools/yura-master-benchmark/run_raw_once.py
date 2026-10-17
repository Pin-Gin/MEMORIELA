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
    "visuals/yura/identity/master/YURA_VISUAL_TEXT.md":
        "HIGHEST YURA VISUAL TEXT AUTHORITY",
    "visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png":
        "OFFICIAL REPOSITORY-PROMOTED INTEGRATED FULL-BODY VISUAL MASTER",
    "visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md":
        "CURRENT FACE DETAIL SPECIFICATION",
    "visuals/yura/identity/face/YURA_FACE_UP_MASTER.md":
        "CURRENT AUTHOR-APPROVED FACE-UP TEXT AUTHORITY",
    "visuals/yura/identity/face/YURA_FACE_REFERENCE.png":
        "CURRENT REPOSITORY-PROMOTED FACE IDENTITY / FACE-LOCAL GEOMETRY ONLY",
    "visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md":
        "EAR GEOMETRY / OCCLUSION SUPPORTING RULE",
    "visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png":
        "AUTHOR-APPROVED EAR GEOMETRY REFERENCE; METADATA-ONLY FOR FULL-BODY API ROUTE",
    "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png":
        "CURRENT 7.0-HEAD BODY-GEOMETRY SUPPORT / RECOVERY GUIDE ONLY; FULL-BODY MASTER WINS ON CONFLICT",
}

REQUIRED_PROMPT_INVARIANTS: tuple[str, ...] = (
    "TARGET HEAD COUNT RANGE = 7.0–7.2 heads.",
    "TARGET HEIGHT IMPRESSION = 152–153 cm.",
    "ONE HEAD = actual structural crown / skull top to chin.",
    "VISIBLE HAIR VOLUME != SKULL HEIGHT.",
    "FACE GEOMETRY IS LOCKED.",
    "FACE IDENTITY BASELINE = CHARM + CUTENESS + APPROPRIATE YOUTHFULNESS.",
    "EYE PLACEMENT = C2 baseline -> 0.3% inward.",
    "PUPILS MUST BE BILATERALLY SYMMETRIC IN SIZE, SHAPE, DARKNESS, AND EDGE SOFTNESS.",
    "EAR VISIBILITY IS NOT REQUIRED.",
    "DO NOT EXPOSE EARS FOR READABILITY.",
    "BODY DEFINITION IS LOCKED.",
    "VALIDATION CLOTHING = plain opaque matte camisole + plain undecorated shorts.",
    "BOTH FEET FLAT ON THE GROUND.",
    "HEELS DOWN.",
    "FULL SOLE CONTACT WITH THE GROUND.",
    "PURE WHITE BACKGROUND.",
    "HAIR END = around waist; do not extend substantially below waist.",
    "SKIN TONE = CLEARLY WHITE-LEANING PALE SKIN.",
    "DO NOT OVER-WHITEN.",
)

FORBIDDEN_LEGACY_LITERALS: tuple[str, ...] = (
    "7.1–7.3",
    "7.1-7.3",
    "89% target",
    "88–90%",
    "88-90%",
    "5–6%",
    "5-6%",
    "TEST 5 USES",
    "Face-up Pilot 1",
)


def run(
    cmd: list[str],
    cwd: Path,
    *,
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
            f"command failed ({p.returncode}): {' '.join(cmd)}\n"
            f"STDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}"
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
        for child in value.values():
            collect_usage_objects(child, out)
    elif isinstance(value, list):
        for child in value:
            collect_usage_objects(child, out)


def parse_codex_trace(text: str) -> list[dict[str, Any]]:
    usage: list[dict[str, Any]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        collect_usage_objects(event, usage)
    return usage


def estimate_image_cost(
    usage: dict[str, Any] | None,
    rates: dict[str, float],
) -> float | None:
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
        (float(text_in or 0) / 1_000_000) * float(rates["text_input_per_1m_usd"])
        + (float(image_in or 0) / 1_000_000) * float(rates["image_input_per_1m_usd"])
        + (float(image_out or 0) / 1_000_000) * float(rates["image_output_per_1m_usd"]),
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
    expected_authorities = list(AUTHORITY_ROLES)
    if config.get("authority_order") != expected_authorities:
        raise RuntimeError(
            "config authority_order must exactly match the current YURA recovery authority set"
        )

    expected_images = [
        "visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png",
        "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png",
        "visuals/yura/identity/face/YURA_FACE_REFERENCE.png",
    ]
    if config.get("image_reference_order") != expected_images:
        raise RuntimeError(
            "recovery image_reference_order must be Full-body Master, Body Geometry Guide, then Face Reference"
        )

    if config.get("route_state") != "FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION":
        raise RuntimeError("unexpected YURA recovery route_state")
    if not isinstance(config.get("paid_generation_allowed"), bool):
        raise RuntimeError("paid_generation_allowed must be a boolean")

    constraints = config.get("execution_constraints") or {}
    if constraints.get("head_ratio_target_range") != [7.0, 7.2]:
        raise RuntimeError("current head ratio range must be exactly 7.0–7.2")
    if constraints.get("height_impression_cm_range") != [152, 153]:
        raise RuntimeError("current height impression range must be exactly 152–153 cm")

    qa = config.get("body_geometry_qa") or {}
    if qa.get("enabled") is not True:
        raise RuntimeError("body_geometry_qa must be enabled")
    if float(qa.get("target_heads_min", -1)) != 7.0:
        raise RuntimeError("body_geometry_qa target_heads_min must be 7.0")
    if float(qa.get("target_heads_max", -1)) != 7.2:
        raise RuntimeError("body_geometry_qa target_heads_max must be 7.2")

    if "composition_postprocess" in config:
        raise RuntimeError(
            "legacy composition_postprocess numeric gates are retired from the current route"
        )


def validate_promoted_assets(
    root: Path,
    config: dict[str, Any],
    local_hashes: dict[str, str],
) -> None:
    master_cfg = config.get("full_body_master") or {}
    master_rel = str(master_cfg.get("primary_path", ""))
    body_copy_rel = str(master_cfg.get("body_copy_path", ""))
    master_expected = str(master_cfg.get("sha256", "")).lower()

    if master_rel not in local_hashes:
        raise RuntimeError("official Full-body Master is missing from authority_order")
    if local_hashes[master_rel].lower() != master_expected:
        raise RuntimeError("official Full-body Master SHA-256 does not match config")

    body_copy = root / body_copy_rel
    if not body_copy.exists():
        raise RuntimeError("body-directory Full-body Master synchronized copy is missing")
    if sha256_file(body_copy).lower() != local_hashes[master_rel].lower():
        raise RuntimeError("body-directory Full-body Master copy does not match primary Master")

    guide_cfg = config.get("body_geometry_guide") or {}
    guide_rel = str(guide_cfg.get("path", ""))
    guide_expected = str(guide_cfg.get("sha256", "")).lower()
    if guide_rel not in local_hashes:
        raise RuntimeError("current Body Geometry Guide is missing from authority_order")
    if local_hashes[guide_rel].lower() != guide_expected:
        raise RuntimeError("current Body Geometry Guide SHA-256 does not match config")


def validate_compiled_prompt(run_dir: Path, compiled_prompt: str) -> None:
    missing = [x for x in REQUIRED_PROMPT_INVARIANTS if x not in compiled_prompt]
    forbidden = [x for x in FORBIDDEN_LEGACY_LITERALS if x in compiled_prompt]
    passed = not missing and not forbidden
    report = {
        "pass": passed,
        "required_current_invariants": list(REQUIRED_PROMPT_INVARIANTS),
        "missing": missing,
        "forbidden_legacy_literals": list(FORBIDDEN_LEGACY_LITERALS),
        "forbidden_present": forbidden,
        "image_api_prompt_gate_pass": passed,
        "head_ratio_gate": "7.0–7.2",
        "legacy_composition_percentage_gate": "RETIRED",
    }
    (run_dir / "prompt_invariant_check.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    if not passed:
        errors = [
            *[f"missing current invariant: {x}" for x in missing],
            *[f"legacy literal present: {x}" for x in forbidden],
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
    image_refs = set(config["image_reference_order"])

    for index, rel in enumerate(authority_paths, start=1):
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
                    "passed_to_image_api": rel in image_refs,
                    "content_note": (
                        "Pixels are not exposed to Codex. "
                        "Only configured image_reference_order files are passed to Image API."
                    ),
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
        "bundle_version": 8,
        "bundle_mode": "SEALED_CURRENT_YURA_FULL_BODY_RECOVERY",
        "git_commit": head,
        "route_state": config["route_state"],
        "paid_generation_allowed": config["paid_generation_allowed"],
        "authority_order": entries,
        "authority_precedence": list(config["authority_precedence"]),
        "denied_sources": list(config["denied_sources"]),
        "image_reference_order": list(config["image_reference_order"]),
        "execution_constraints": config["execution_constraints"],
        "compiler_boundary": {
            "runner_resolves_git": True,
            "runner_reads_authorities": True,
            "runner_computes_sha256": True,
            "codex_filesystem_access_required": False,
            "codex_shell_access_required": False,
            "codex_external_tools_required": False,
            "png_pixels_inspected_by_codex": False,
            "legacy_archived_runner_is_authority": False,
            "legacy_composition_percentage_gates_active": False,
            "current_head_ratio_hard_gate": "7.0–7.2",
            "official_full_body_master_is_primary_integrated_reference": True,
            "body_geometry_guide_is_support_only": True,
            "paid_generation_allowed": config["paid_generation_allowed"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Frozen YURA full-body recovery route using sealed current Git Authorities."
    )
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help="Build and verify the sealed bundle without any paid Codex or Image API call.",
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
    dirty_paths = [*authority_paths, str(config["full_body_master"]["body_copy_path"])]
    dirty = run(
        ["git", "status", "--porcelain", "--", *dirty_paths],
        root,
    ).stdout.strip()
    if dirty:
        raise RuntimeError("Authority files have uncommitted changes; aborting:\n" + dirty)

    local_hashes: dict[str, str] = {}
    for rel in authority_paths:
        path = root / rel
        if not path.exists():
            raise RuntimeError(f"required current Authority missing: {rel}")
        local_hashes[rel] = sha256_file(path)

    validate_promoted_assets(root, config, local_hashes)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    runs_dir = root / str(config["runs_dir"])
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
    (run_dir / "sealed_authority_bundle.sha256").write_text(
        bundle_sha + "\n",
        encoding="ascii",
    )

    started_at = int(time.time())
    meta = {
        "run_id": run_dir.name,
        "started_at_unix": started_at,
        "started_at_utc": datetime.fromtimestamp(started_at, timezone.utc).isoformat(),
        "git_commit": head,
        "config_sha256": sha256_file(CONFIG_PATH),
        "codex_instruction_sha256": sha256_file(INSTRUCTION_PATH),
        "authority_sha256": local_hashes,
        "sealed_authority_bundle_sha256": bundle_sha,
        "preflight_only": args.preflight_only,
        "route_status": config["route_state"],
        "paid_generation_allowed": config["paid_generation_allowed"],
        "head_ratio_gate": "7.0–7.2",
        "legacy_composition_percentage_gates": "RETIRED",
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
    (run_dir / "codex_input.sha256").write_text(
        codex_input_sha + "\n",
        encoding="ascii",
    )

    if args.preflight_only:
        print(
            json.dumps(
                {
                    "status": "PREFLIGHT_OK",
                    "paid_model_calls": 0,
                    "paid_generation_allowed": config["paid_generation_allowed"],
                    "route_state": config["route_state"],
                    "run_dir": str(run_dir),
                    "git_commit": head,
                    "authority_count": len(authority_paths),
                    "sealed_authority_bundle_sha256": bundle_sha,
                    "codex_input_sha256": codex_input_sha,
                    "head_ratio_gate": "7.0–7.2",
                    "height_impression_cm": "152–153",
                    "image_reference_order": config["image_reference_order"],
                    "legacy_composition_percentage_gates": "RETIRED",
                    "next": (
                        "Recovery preflight verified. Paid generation remains frozen. "
                        "Do not run a billable call until explicit author reauthorization and config update."
                    ),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    if config.get("paid_generation_allowed") is not True:
        raise RuntimeError(
            "Paid YURA generation is frozen after Full-body Master promotion. "
            "Explicit author reauthorization and config update are required before any Codex/Image API call."
        )

    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for paid Codex/Image API execution.")

    manifest_path = run_dir / "authority_manifest.json"
    codex_cmd = [
        str(config["codex"]["executable"]),
        "exec",
        "--ignore-user-config",
        "--sandbox",
        "read-only",
        "--json",
        "--model",
        str(config["codex"]["model"]),
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
        rel = item["path"]
        if item.get("order") != index:
            raise RuntimeError(f"Codex Authority ordinal mismatch: {rel}")
        if item.get("sha256", "").lower() != local_hashes[rel].lower():
            raise RuntimeError(f"Codex Authority SHA mismatch: {rel}")
        if item.get("role") != AUTHORITY_ROLES[rel]:
            raise RuntimeError(f"Codex Authority role mismatch: {rel}")

    if manifest.get("denied_sources") != config["denied_sources"]:
        raise RuntimeError("Codex denied_sources mismatch")
    if manifest.get("image_reference_order") != config["image_reference_order"]:
        raise RuntimeError("Codex image_reference_order mismatch")

    compiled_prompt = str(manifest["compiled_prompt"])
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
        for file_obj in refs:
            file_obj.close()

    if not result.data or not result.data[0].b64_json:
        write_failure(run_dir, "image_api", ["Image API returned no image"], True)
        raise RuntimeError("Image API returned no image")

    result_dict = jsonable(result)
    result_name = str(config["image_api"].get("result_filename", "result.png"))
    result_path = run_dir / result_name
    result_path.write_bytes(base64.b64decode(result.data[0].b64_json))

    response_for_log = json.loads(json.dumps(result_dict))
    for item in response_for_log.get("data", []):
        if "b64_json" in item:
            item["b64_json"] = f"<saved to {result_name}>"
    (run_dir / "image_response.json").write_text(
        json.dumps(response_for_log, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    usage = response_for_log.get("usage") if isinstance(response_for_log, dict) else None
    image_estimate = estimate_image_cost(
        usage,
        config["pricing_snapshot"]["image_model"],
    )
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
                "pricing_snapshot_note": config["pricing_snapshot"]["note"],
                "started_at_unix": started_at,
                "ended_at_unix": ended_at,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    qa = {
        "candidate": "QA_PENDING",
        "master_promotion": "NO",
        "result_image": result_name,
        "head_ratio_target_range": [7.0, 7.2],
        "height_impression_cm_range": [152, 153],
        "head_ratio_status": "PENDING_IMAGE_MEASUREMENT",
        "auto_pass": False,
        "author_pass": None,
        "required_author_review": {
            "full_body_master_integrated_balance": "PENDING",
            "face_identity_and_geometry": "PENDING",
            "eye_shape_size_placement": "PENDING",
            "pupil_bilateral_symmetry": "PENDING",
            "ear_no_visibility_compensation": "PENDING",
            "body_definition_and_balance": "PENDING",
            "chest_to_frame_relationship": "PENDING",
            "hair_length_around_waist": "PENDING",
            "white_leaning_skin_not_overwhitened": "PENDING",
            "validation_clothing": "PENDING",
            "upright_pose_feet_fully_planted": "PENDING",
            "white_background_centering": "PENDING",
        },
        "note": (
            "Measure head ratio from the generated image using structural skull top, chin, and soles. "
            "Author PASS remains mandatory. Legacy composition occupancy/margin percentages are not active gates."
        ),
    }
    (run_dir / "qa.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "status": "PAID_RUN_COMPLETE_QA_PENDING",
                "run_dir": str(run_dir),
                "git_commit": head,
                "route_state": config["route_state"],
                "sealed_authority_bundle_sha256": bundle_sha,
                "compiled_prompt_sha256": prompt_sha,
                "result_image_path": str(result_path),
                "head_ratio_target": "7.0–7.2",
                "image_estimated_cost_usd": image_estimate,
                "next": (
                    "Measure head ratio from result.png and perform author visual review. "
                    "Do not promote or replace the current Master until explicit author PASS."
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
