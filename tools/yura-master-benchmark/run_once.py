from __future__ import annotations

import sys

MESSAGE = """
YURA paid generation route is currently DISABLED / REBUILD REQUIRED.

No paid generation is authorized from this legacy entrypoint.

Current restart point:
  project-management/yura-visual/START_HERE.md

Paid-route status:
  tools/yura-master-benchmark/PAID_ROUTE_STATUS.md

The original pre-rebuild runner is archived under:
  tools/yura-master-benchmark/archive/legacy-runner/run_once.py

Do not reactivate the legacy Face Reference / Body Guide / old full-body Master route without explicit author instruction.
""".strip()


def main() -> int:
    print(MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
