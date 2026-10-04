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


def run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
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


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    root = Path(run(["git", "rev-parse", "--show-toplevel"], TOOL_DIR).stdout.strip())

    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is required for the Image API and should belong to the benchmark project.")

    # Resolve current main before any paid request.
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

    started_at = int(time.time())
    meta = {
        "run_id": run_dir.name,
        "started_at_unix": started_at,
        "started_at_utc": datetime.fromtimestamp(started_at, timezone.utc).isoformat(),
        "git_commit": head,
        "config_sha256": sha256_file(CONFIG_PATH),
        "authority_sha256": local_hashes,
    }
    (run_dir / "run_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    # Codex reads the repo and produces a machine-readable manifest plus the exact prompt.
    instruction = INSTRUCTION_PATH.read_text(encoding="utf-8")
    manifest_path = run_dir / "authority_manifest.json"
    codex_cmd = [
        config["codex"]["executable"],
        "exec",
        "--json",
        "--model",
        config["codex"]["model"],
        "--output-schema",
        str(SCHEMA_PATH),
        "-o",
        str(manifest_path),
        instruction,
    ]
    codex = run(codex_cmd, root, check=False)
    (run_dir / "codex_trace.jsonl").write_text(codex.stdout, encoding="utf-8")
    (run_dir / "codex_stderr.log").write_text(codex.stderr, encoding="utf-8")
    events, codex_usage = parse_codex_trace(codex.stdout)
    (run_dir / "codex_usage_candidates.json").write_text(
        json.dumps(codex_usage, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if codex.returncode != 0:
        raise RuntimeError(f"Codex failed; inspect {run_dir / 'codex_stderr.log'}")
    if not manifest_path.exists():
        raise RuntimeError("Codex completed without authority_manifest.json")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not manifest.get("ready"):
        raise RuntimeError("Codex reported ready=false: " + "; ".join(manifest.get("errors", [])))
    if manifest.get("git_commit") != head:
        raise RuntimeError("Codex manifest git_commit does not match current HEAD")

    reported_paths = [x["path"] for x in manifest.get("authority_order", [])]
    if reported_paths != authority_paths:
        raise RuntimeError(f"Codex Authority order mismatch: {reported_paths}")
    for item in manifest["authority_order"]:
        if item["sha256"].lower() != local_hashes[item["path"]].lower():
            raise RuntimeError(f"Codex SHA-256 mismatch: {item['path']}")
    if manifest.get("image_reference_order") != config["image_reference_order"]:
        raise RuntimeError("Codex image_reference_order mismatch")

    compiled_prompt = manifest["compiled_prompt"]
    prompt_sha = hashlib.sha256(compiled_prompt.encode("utf-8")).hexdigest()
    (run_dir / "compiled_prompt.txt").write_text(compiled_prompt, encoding="utf-8")
    (run_dir / "compiled_prompt.sha256").write_text(prompt_sha + "\n", encoding="ascii")

    # OpenAI Image API: reference order is fixed by config and verified above.
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
