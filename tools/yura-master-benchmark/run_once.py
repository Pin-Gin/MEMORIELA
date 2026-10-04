from __future__ import annotations

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
        "bundle_version": 1,
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
        },
    }


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    root = Path(run(["git", "rev-parse", "--show-toplevel"], TOOL_DIR).stdout.strip())

    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for the benchmark project.")

    # Resolve and validate current main locally before any paid model request.
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

    # Build the only dataset Codex is allowed to see. Text Authorities are embedded;
    # PNGs are represented by verified path/hash/role metadata and are passed as actual
    # image files only to the later Image API call.
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
        "codex_input_mode": "sealed_authority_bundle_via_stdin",
        "codex_user_config_loaded": False,
        "codex_tool_dependency": "NONE",
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
    (run_dir / "codex_input.sha256").write_text(sha256_text(codex_input) + "\n", encoding="ascii")

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

    # No positional prompt is supplied. codex exec reads the complete sealed input from
    # stdin, avoiding Windows command-line length limits and eliminating filesystem reads
    # from the model task itself.
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

    # OpenAI Image API: reference order is fixed by config and reverified above.
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
    output_path = run_dir / "result.png"
    output_path.write_bytes(image_bytes)

    # Save response metadata without duplicating the large base64 payload.
    response_for_log = json.loads(json.dumps(result_dict))
    for item in response_for_log.get("data", []):
        if "b64_json" in item:
            item["b64_json"] = "<saved to result.png>"
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
        "note": "Use query_project_cost.py with OPENAI_ADMIN_KEY and OPENAI_PROJECT_ID for authoritative project cost attribution.",
    }
    (run_dir / "cost.json").write_text(json.dumps(cost, ensure_ascii=False, indent=2), encoding="utf-8")

    qa = {
        "candidate": "QA_PENDING",
        "master_promotion": "NO",
        "auto_checks": {},
        "author_pass": None,
        "notes": "Do not promote until geometry, face identity, ears, body silhouette, composition, and author review pass.",
    }
    (run_dir / "qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "run_dir": str(run_dir),
        "git_commit": head,
        "sealed_authority_bundle_sha256": bundle_sha,
        "compiled_prompt_sha256": prompt_sha,
        "image_path": str(output_path),
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
