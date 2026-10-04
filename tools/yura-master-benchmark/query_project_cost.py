from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
CONFIG_PATH = TOOL_DIR / "config.json"
UTC_DAY_SECONDS = 24 * 60 * 60


def jsonable(obj: Any) -> Any:
    if hasattr(obj, "model_dump"):
        return obj.model_dump(mode="json")
    return obj


def collect_amounts(value: Any, out: list[dict[str, Any]]) -> None:
    if isinstance(value, dict):
        amount = value.get("amount")
        if isinstance(amount, dict) and "value" in amount:
            out.append(amount)
        for v in value.values():
            collect_amounts(v, out)
    elif isinstance(value, list):
        for v in value:
            collect_amounts(v, out)


def utc_iso(unix_seconds: int) -> str:
    return datetime.fromtimestamp(unix_seconds, timezone.utc).isoformat()


def estimate_codex_cost(cost: dict[str, Any], config: dict[str, Any]) -> float | None:
    candidates = cost.get("codex_usage_candidates") or []
    if not candidates:
        return None

    # The final candidate is expected to be the completed-turn cumulative usage object.
    # Do not sum candidates because traces may contain repeated/cumulative usage records.
    usage = candidates[-1]
    try:
        input_tokens = int(usage.get("input_tokens", 0))
        cached_tokens = int(usage.get("cached_input_tokens", 0))
        output_tokens = int(usage.get("output_tokens", 0))
    except (TypeError, ValueError):
        return None

    uncached_tokens = max(input_tokens - cached_tokens, 0)
    rates = config["pricing_snapshot"]["codex_model_standard"]
    return round(
        (uncached_tokens / 1_000_000) * float(rates["input_per_1m_usd"])
        + (cached_tokens / 1_000_000) * float(rates["cached_input_per_1m_usd"])
        + (output_tokens / 1_000_000) * float(rates["output_per_1m_usd"]),
        8,
    )


def update_run_estimate(cost: dict[str, Any], config: dict[str, Any]) -> None:
    codex_estimate = estimate_codex_cost(cost, config)
    image_estimate = cost.get("image_estimated_cost_usd")

    cost["codex_estimated_cost_usd"] = codex_estimate
    if codex_estimate is not None and image_estimate is not None:
        cost["run_estimated_cost_usd"] = round(
            float(codex_estimate) + float(image_estimate), 8
        )
    else:
        cost["run_estimated_cost_usd"] = None
    cost["run_estimate_pricing_snapshot_as_of"] = config["pricing_snapshot"]["as_of"]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Query OpenAI organization Costs API without misattributing its daily buckets "
            "to a single benchmark run."
        )
    )
    parser.add_argument("run_dir", type=Path)
    parser.add_argument(
        "--wait-seconds",
        type=int,
        default=90,
        help=(
            "After the relevant UTC day has closed, poll this long for delayed cost accounting. "
            "No polling is performed while the UTC day is still open."
        ),
    )
    parser.add_argument("--poll-seconds", type=int, default=10)
    parser.add_argument(
        "--isolated-project-day",
        action="store_true",
        help=(
            "Assert that this run was the only billable activity in OPENAI_PROJECT_ID across "
            "every queried UTC daily bucket. Only use this with a deliberately isolated project/day."
        ),
    )
    args = parser.parse_args()

    admin_key = os.environ.get("OPENAI_ADMIN_KEY")
    project_id = os.environ.get("OPENAI_PROJECT_ID")
    if not admin_key:
        raise RuntimeError("OPENAI_ADMIN_KEY is required for organization cost queries")
    if not project_id:
        raise RuntimeError("OPENAI_PROJECT_ID is required so cost is isolated to the benchmark project")

    run_dir = args.run_dir.resolve()
    meta_path = run_dir / "run_meta.json"
    cost_path = run_dir / "cost.json"
    if not meta_path.exists():
        raise RuntimeError(f"run_meta.json not found: {meta_path}")
    if not cost_path.exists():
        raise RuntimeError(f"cost.json not found: {cost_path}")

    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    cost = json.loads(cost_path.read_text(encoding="utf-8"))
    update_run_estimate(cost, config)

    run_start = int(meta["started_at_unix"])
    run_end = int(cost["ended_at_unix"])
    if run_end < run_start:
        raise RuntimeError("cost ended_at_unix precedes run started_at_unix")

    first_day_start = (run_start // UTC_DAY_SECONDS) * UTC_DAY_SECONDS
    last_activity_second = max(run_end - 1, run_start)
    last_day_start = (last_activity_second // UTC_DAY_SECONDS) * UTC_DAY_SECONDS
    query_start = first_day_start
    query_end = last_day_start + UTC_DAY_SECONDS

    cost["project_id"] = project_id
    cost["cost_api_granularity"] = "1d"
    cost["cost_query_scope"] = "PROJECT_UTC_DAY_BUCKETS"
    cost["cost_query_window"] = {
        "start_time": query_start,
        "end_time": query_end,
        "start_time_utc": utc_iso(query_start),
        "end_time_utc": utc_iso(query_end),
    }
    cost["run_specific_authoritative_cost_usd"] = None
    cost["authoritative_total_project_cost_usd"] = None
    cost["authoritative_project_day_cost_usd"] = None
    cost["isolated_project_day_asserted"] = bool(args.isolated_project_day)

    now = int(time.time())
    raw_path = run_dir / "authoritative_cost_raw.json"

    # Costs API currently exposes daily buckets only. An open UTC day cannot provide a
    # completed authoritative bucket, so do not waste time polling until it closes.
    if now < query_end:
        status = "PROJECT_DAY_COST_PENDING_UTC_CLOSE"
        raw = {
            "queried": False,
            "reason": "Costs API uses 1d buckets and the relevant UTC day is still open.",
            "bucket_width": "1d",
            "project_id": project_id,
            "query_start": query_start,
            "query_end": query_end,
            "available_after_utc": utc_iso(query_end),
        }
        raw_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
        cost["billing_status"] = status
        cost["cost_accounting_note"] = (
            "Run-specific token/image usage estimates are available now. Authoritative Costs API "
            "data is daily; this project/day total cannot be attributed to this run unless the "
            "project/day was deliberately isolated."
        )
        cost_path.write_text(json.dumps(cost, ensure_ascii=False, indent=2), encoding="utf-8")

        print(json.dumps({
            "run_dir": str(run_dir),
            "billing_status": status,
            "run_estimated_cost_usd": cost.get("run_estimated_cost_usd"),
            "run_specific_authoritative_cost_usd": None,
            "authoritative_project_day_cost_usd": None,
            "cost_api_granularity": "1d",
            "available_after_utc": utc_iso(query_end),
            "reason": "Relevant UTC daily cost bucket has not closed yet.",
        }, ensure_ascii=False, indent=2))
        return 0

    from openai import OpenAI

    client = OpenAI(admin_api_key=admin_key)
    deadline = time.time() + max(args.wait_seconds, 0)
    raw: dict[str, Any] | None = None
    amounts: list[dict[str, Any]] = []

    while True:
        response = client.admin.organization.usage.costs(
            start_time=query_start,
            end_time=query_end,
            bucket_width="1d",
            project_ids=[project_id],
            group_by=["project_id", "line_item", "api_key_id"],
        )
        raw = jsonable(response)
        amounts = []
        collect_amounts(raw, amounts)
        if amounts or time.time() >= deadline:
            break
        time.sleep(max(args.poll_seconds, 1))

    raw_path.write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")

    currencies = {str(x.get("currency", "usd")).lower() for x in amounts}
    if amounts and currencies - {"usd"}:
        raise RuntimeError(f"unexpected currencies in cost response: {sorted(currencies)}")

    project_day_total = round(sum(float(x["value"]) for x in amounts), 8) if amounts else None
    cost["authoritative_project_day_cost_usd"] = project_day_total

    if project_day_total is None:
        status = "PROJECT_DAY_COST_NOT_AVAILABLE_YET"
        cost["cost_accounting_note"] = (
            "The UTC day is closed but the Costs API has not returned amount entries yet. "
            "Retry later; do not treat this as a zero-cost run."
        )
    elif args.isolated_project_day:
        status = "AUTHORITATIVE_RUN_COST_FROM_ISOLATED_PROJECT_DAY"
        cost["run_specific_authoritative_cost_usd"] = project_day_total
        # Backward-compatible field: only populated when project-day isolation was explicitly asserted.
        cost["authoritative_total_project_cost_usd"] = project_day_total
        cost["cost_accounting_note"] = (
            "Costs API is daily. This project-day total is treated as run-specific only because "
            "--isolated-project-day explicitly asserted that no other billable activity used this "
            "project in the queried UTC bucket(s)."
        )
    else:
        status = "AUTHORITATIVE_PROJECT_DAY_COST_ONLY"
        cost["cost_accounting_note"] = (
            "Costs API is daily. This is an authoritative project/day total, NOT an authoritative "
            "single-run cost. Use run_estimated_cost_usd for this run, or use a deliberately isolated "
            "project/day and rerun with --isolated-project-day."
        )

    cost["billing_status"] = status
    cost_path.write_text(json.dumps(cost, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "run_dir": str(run_dir),
        "billing_status": status,
        "run_estimated_cost_usd": cost.get("run_estimated_cost_usd"),
        "run_specific_authoritative_cost_usd": cost.get("run_specific_authoritative_cost_usd"),
        "authoritative_project_day_cost_usd": project_day_total,
        "authoritative_total_project_cost_usd": cost.get("authoritative_total_project_cost_usd"),
        "cost_api_granularity": "1d",
        "isolated_project_day_asserted": bool(args.isolated_project_day),
        "amount_entries": len(amounts),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
