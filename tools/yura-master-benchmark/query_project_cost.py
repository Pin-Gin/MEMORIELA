from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--wait-seconds", type=int, default=90)
    parser.add_argument("--poll-seconds", type=int, default=10)
    args = parser.parse_args()

    admin_key = os.environ.get("OPENAI_ADMIN_KEY")
    project_id = os.environ.get("OPENAI_PROJECT_ID")
    if not admin_key:
        raise RuntimeError("OPENAI_ADMIN_KEY is required for organization cost queries")
    if not project_id:
        raise RuntimeError("OPENAI_PROJECT_ID is required so cost is isolated to the benchmark project")

    run_dir = args.run_dir.resolve()
    meta = json.loads((run_dir / "run_meta.json").read_text(encoding="utf-8"))
    cost_path = run_dir / "cost.json"
    cost = json.loads(cost_path.read_text(encoding="utf-8"))
    start_time = int(meta["started_at_unix"]) - 2
    end_time = int(cost["ended_at_unix"]) + 2

    from openai import OpenAI

    client = OpenAI(admin_api_key=admin_key)
    deadline = time.time() + max(args.wait_seconds, 0)
    raw: dict[str, Any] | None = None
    amounts: list[dict[str, Any]] = []

    while True:
        response = client.admin.organization.usage.costs(
            start_time=start_time,
            end_time=end_time,
            project_ids=[project_id],
        )
        raw = jsonable(response)
        amounts = []
        collect_amounts(raw, amounts)
        if amounts or time.time() >= deadline:
            break
        time.sleep(max(args.poll_seconds, 1))

    (run_dir / "authoritative_cost_raw.json").write_text(
        json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    currencies = {str(x.get("currency", "usd")).lower() for x in amounts}
    if amounts and currencies - {"usd"}:
        raise RuntimeError(f"unexpected currencies in cost response: {sorted(currencies)}")

    total = round(sum(float(x["value"]) for x in amounts), 8) if amounts else None
    status = "AUTHORITATIVE_PROJECT_COST" if total is not None else "COST_ACCOUNTING_NOT_AVAILABLE_YET"

    cost["billing_status"] = status
    cost["authoritative_total_project_cost_usd"] = total
    cost["project_id"] = project_id
    cost["cost_query_window"] = {"start_time": start_time, "end_time": end_time}
    cost_path.write_text(json.dumps(cost, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "run_dir": str(run_dir),
        "billing_status": status,
        "authoritative_total_project_cost_usd": total,
        "amount_entries": len(amounts),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
