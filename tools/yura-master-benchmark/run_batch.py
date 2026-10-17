from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

TOOL_DIR = Path(__file__).resolve().parent
CONFIG = json.loads((TOOL_DIR / "config.json").read_text(encoding="utf-8"))
CURRENT_ROUTE_STATUS = str(CONFIG.get("route_state", "UNKNOWN_ROUTE_STATE"))


def newest_run() -> Path | None:
    runs = TOOL_DIR / "runs"
    if not runs.exists():
        return None
    dirs = [
        p
        for p in runs.iterdir()
        if p.is_dir() and (p / "cost.json").exists() and (p / "run_meta.json").exists()
    ]
    return max(dirs, key=lambda p: p.stat().st_mtime) if dirs else None


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def estimate_full_run_cost(cost: dict) -> float | None:
    stored = cost.get("run_estimated_cost_usd")
    if stored is not None:
        return float(stored)

    image_estimate = cost.get("image_estimated_cost_usd")
    candidates = cost.get("codex_usage_candidates") or []
    if image_estimate is None or not candidates:
        return None

    usage = candidates[-1]
    try:
        input_tokens = int(usage.get("input_tokens", 0))
        cached_tokens = int(usage.get("cached_input_tokens", 0))
        output_tokens = int(usage.get("output_tokens", 0))
    except (TypeError, ValueError):
        return None

    uncached_tokens = max(input_tokens - cached_tokens, 0)
    rates = CONFIG["pricing_snapshot"]["codex_model_standard"]
    codex_estimate = (
        (uncached_tokens / 1_000_000) * float(rates["input_per_1m_usd"])
        + (cached_tokens / 1_000_000) * float(rates["cached_input_per_1m_usd"])
        + (output_tokens / 1_000_000) * float(rates["output_per_1m_usd"])
    )
    return round(codex_estimate + float(image_estimate), 8)


def eligible_cost(cost: dict, allow_estimate: bool) -> tuple[float, str]:
    authoritative = cost.get("run_specific_authoritative_cost_usd")
    if authoritative is None:
        authoritative = cost.get("authoritative_total_project_cost_usd")
    if authoritative is not None:
        return float(authoritative), "authoritative-run-cost"

    if allow_estimate:
        estimate = estimate_full_run_cost(cost)
        if estimate is not None:
            return estimate, "codex-plus-image-estimate"

    raise RuntimeError(
        "No authoritative run-specific cost is available. "
        "Use an isolated project/day for authoritative attribution, "
        "or pass --allow-estimate to explicitly accept the stored pricing snapshot estimate."
    )


def validate_seed(seed: Path) -> None:
    meta = load_json(seed / "run_meta.json")
    if meta.get("route_status") != CURRENT_ROUTE_STATUS:
        raise RuntimeError(
            "Seed run does not match the current configured YURA recovery route state. "
            "Generate a new seed only after the route is explicitly reauthorized."
        )
    if meta.get("head_ratio_gate") != "7.0–7.2":
        raise RuntimeError("Seed run does not use the current 7.0–7.2 head-ratio gate")
    if not (seed / "compiled_prompt.sha256").exists():
        raise RuntimeError("Seed run has no compiled_prompt.sha256")
    if not (seed / str(CONFIG["image_api"].get("result_filename", "result.png"))).exists():
        raise RuntimeError("Seed run has no generated result image")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run independent YURA recovery-route paid generations only after explicit reauthorization."
    )
    parser.add_argument("--seed-run", type=Path, default=None)
    parser.add_argument("--runs", type=int, default=CONFIG["batch"]["runs_after_single"])
    parser.add_argument("--allow-estimate", action="store_true")
    parser.add_argument(
        "--confirm-seed-reviewed",
        action="store_true",
        help="Required: confirms the single paid seed run and its cost/technical artifacts were reviewed.",
    )
    parser.add_argument("--query-costs", action="store_true")
    parser.add_argument("--cost-wait-seconds", type=int, default=30)
    args = parser.parse_args()

    if CONFIG.get("paid_generation_allowed") is not True:
        raise RuntimeError(
            "Paid YURA generation is frozen after Full-body Master promotion. "
            "Explicit author reauthorization and config update are required before batch execution."
        )
    if (CONFIG.get("batch") or {}).get("current_batch_authorized") is not True:
        raise RuntimeError(
            "YURA batch generation is not currently authorized. "
            "Set current_batch_authorized only after explicit author authorization."
        )
    if not args.confirm_seed_reviewed:
        raise RuntimeError("Batch requires --confirm-seed-reviewed")
    if args.runs < 1:
        raise RuntimeError("--runs must be >= 1")

    seed = args.seed_run.resolve() if args.seed_run else newest_run()
    if seed is None:
        raise RuntimeError("No seed run found. Execute an explicitly reauthorized run_once.py first.")

    validate_seed(seed)

    seed_cost = load_json(seed / "cost.json")
    run_cost, cost_source = eligible_cost(seed_cost, args.allow_estimate)
    threshold = float(CONFIG["batch"]["max_total_cost_per_run_usd_for_auto_batch"])
    if run_cost >= threshold:
        raise RuntimeError(
            f"Seed run cost ${run_cost:.6f} is not below batch threshold ${threshold:.2f}"
        )

    produced: list[Path] = []
    for index in range(1, args.runs + 1):
        print(f"[{index}/{args.runs}] running reauthorized YURA paid recovery benchmark...", flush=True)
        p = subprocess.run(
            [sys.executable, str(TOOL_DIR / "run_once.py")],
            cwd=TOOL_DIR,
            text=True,
            capture_output=True,
        )
        sys.stdout.write(p.stdout)
        sys.stderr.write(p.stderr)
        if p.returncode != 0:
            raise RuntimeError(f"run_once.py failed at batch item {index}")

        try:
            payload = json.loads(p.stdout[p.stdout.rfind("{"):])
            run_dir = Path(payload["run_dir"])
        except Exception:
            run_dir = newest_run()
            if run_dir is None:
                raise RuntimeError("Could not resolve generated run directory")
        produced.append(run_dir)

        if (
            args.query_costs
            and os.environ.get("OPENAI_ADMIN_KEY")
            and os.environ.get("OPENAI_PROJECT_ID")
        ):
            q = subprocess.run(
                [
                    sys.executable,
                    str(TOOL_DIR / "query_project_cost.py"),
                    str(run_dir),
                    "--wait-seconds",
                    str(args.cost_wait_seconds),
                ],
                cwd=TOOL_DIR,
                text=True,
            )
            if q.returncode != 0:
                print(f"WARNING: cost query failed for {run_dir.name}", file=sys.stderr)

    prompt_hashes: list[str] = []
    authoritative_costs: list[float] = []
    author_pass = 0
    head_ratio_pass = 0

    for d in produced:
        sha_file = d / "compiled_prompt.sha256"
        if sha_file.exists():
            prompt_hashes.append(sha_file.read_text(encoding="ascii").strip())

        cost = load_json(d / "cost.json")
        run_authoritative = cost.get("run_specific_authoritative_cost_usd")
        if run_authoritative is not None:
            authoritative_costs.append(float(run_authoritative))

        qa_path = d / "qa.json"
        if qa_path.exists():
            qa = load_json(qa_path)
            if qa.get("author_pass") is True:
                author_pass += 1
            if qa.get("head_ratio_pass") is True:
                head_ratio_pass += 1

    summary = {
        "route": CURRENT_ROUTE_STATUS,
        "head_ratio_gate": "7.0–7.2",
        "seed_run": str(seed),
        "seed_cost_usd": run_cost,
        "seed_cost_source": cost_source,
        "threshold_usd": threshold,
        "requested_runs": args.runs,
        "completed_runs": len(produced),
        "run_dirs": [str(x) for x in produced],
        "compiled_prompt_sha256_counts": dict(Counter(prompt_hashes)),
        "compiled_prompt_stable": len(set(prompt_hashes)) <= 1 if prompt_hashes else False,
        "head_ratio_pass_count": head_ratio_pass,
        "author_pass_count": author_pass,
        "authoritative_run_costs_available": len(authoritative_costs),
        "authoritative_batch_cost_usd": (
            round(sum(authoritative_costs), 8) if authoritative_costs else None
        ),
        "note": (
            "Each batch item is an independent run. "
            "A generated image remains QA_PENDING until image-based head-ratio QA and explicit author review. "
            "The repository-promoted Full-body Master is the primary integrated visual baseline."
        ),
    }

    out = TOOL_DIR / "runs" / "latest_batch_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
