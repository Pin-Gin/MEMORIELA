from __future__ import annotations

import sys

MESSAGE = """
YURA legacy RAW paid runner is DISABLED / REBUILD REQUIRED.

PAID_GENERATION_ALLOWED = NO

Read:
  project-management/yura-visual/START_HERE.md
  tools/yura-master-benchmark/PAID_ROUTE_STATUS.md

The original pre-rebuild implementation is archived at:
  tools/yura-master-benchmark/archive/legacy-runner/run_raw_once.py

Do not execute the legacy paid condition as the current YURA route.
""".strip()


def main() -> int:
    print(MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
