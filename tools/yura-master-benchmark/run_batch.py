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


def newest_run() -> Path | None:
    runs = TOOL_DIR / "runs"
    if not runs.exists():
        return None
    dirs = [p for p in runs.iterdir() if p.is_dir() and (p / "cost.json").exists()]
    return max(dirs, key=lambda p: p.stat().st_mtime) if dirs else None


def load_cost(run_dir: Path) -> dict:
    return json.loads((run_dir / "cost.json").read_text(encoding="utf-8"))


def eligible_cost(cost: dict, allow_estimate: bool) -> tuple[float, str]:
    authoritative = cost.get("authoritative_total_project_cost_usd")
    if authoritative is not None:
        return float(authoritative), "authoritative"
    if allow_estimate and cost.get("image_estimated_cost_usd") is not None:
        return float(cost["image_estimated_cost_usd"]), "image-estimate-only"
    raise RuntimeError(
        "No authoritative run cost is available. Run query_project_cost.py first, "
        "or pass --allow-estimate to explicitly accept an image-only estimate."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-run", type=Path, default=None)
    parser.add_argument("--runs", type=int, default=CONFIG["batch"]["runs_after_single"])
    parser.add_argument("--allow-estimate", action="store_true")
    parser.add_argument("--query-costs", action="store_true", help="Query project cost after each run when admin credentials are set")
    parser.add_argument("--cost-wait-seconds", type=int, default=30)
    args = parser.parse_args()

    seed = args.seed_run.resolve() if args.seed_run else newest_run()
    if seed is None:
        raise RuntimeError("No seed run found. Execute run_once.py first.")
    seed_cost = load_cost(seed)
    run_cost, cost_source = eligible_cost(seed_cost, args.allow_estimate)
    threshold = float(CONFIG["batch"]["max_total_cost_per_run_usd_for_auto_batch"])
    if run_cost >= threshold:
        raise RuntimeError(f"Seed run cost ${run_cost:.6f} is not below batch threshold ${threshold:.2f}")

    produced: list[Path] = []
    for index in range(1, args.runs + 1):
        print(f"[{index}/{args.runs}] running YURA benchmark...", flush=True)
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

        if args.query_costs and os.environ.get("OPENAI_ADMIN_KEY") and os.environ.get("OPENAI_PROJECT_ID"):
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

    prompt_hashes = []
    authoritative_costs = []
    author_pass = 0
    auto_pass = 0
    for d in produced:
        sha_file = d / "compiled_prompt.sha256"
        if sha_file.exists():
            prompt_hashes.append(sha_file.read_text(encoding="ascii").strip())
        cost = load_cost(d)
        if cost.get("authoritative_total_project_cost_usd") is not None:
            authoritative_costs.append(float(cost["authoritative_total_project_cost_usd"]))
        qa_path = d / "qa.json"
        if qa_path.exists():
            qa = json.loads(qa_path.read_text(encoding="utf-8"))
            if qa.get("author_pass") is True:
                author_pass += 1
            if qa.get("auto_pass") is True:
                auto_pass += 1

    summary = {
        "seed_run": str(seed),
        "seed_cost_usd": run_cost,
        "seed_cost_source": cost_source,
        "threshold_usd": threshold,
        "requested_runs": args.runs,
        "completed_runs": len(produced),
        "run_dirs": [str(x) for x in produced],
        "compiled_prompt_sha256_counts": dict(Counter(prompt_hashes)),
        "manifest_stable": len(set(prompt_hashes)) <= 1 if prompt_hashes else False,
        "authoritative_costs_available": len(authoritative_costs),
        "authoritative_batch_cost_usd": round(sum(authoritative_costs), 8) if authoritative_costs else None,
        "auto_pass_count": auto_pass,
        "author_pass_count": author_pass,
        "note": "author_pass_count stays zero until qa.json is reviewed and explicitly marked by the author.",
    }
    out = TOOL_DIR / "runs" / "latest_batch_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
