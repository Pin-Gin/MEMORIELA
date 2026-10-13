from __future__ import annotations

import sys

MESSAGE = """
CURRENT ROUTE DISABLED FOR THIS FILE.

This runner belonged to the superseded image-reference + OpenAI Image API ambiguity route.
The current author-approved ambiguity validation route is:

  Codex-native image generation
  + visuals/yura/identity/master/YURA_VISUAL_TEXT.md as the only YURA appearance input
  + no YURA image references
  + no OpenAI Image API / OPENAI_API_KEY during the Codex phase

Read:
  tools/yura-master-benchmark/codex_instruction_visual_ambiguity_reference.md
  tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md

Do not reactivate this runner to bypass the current text-only validation gate.
The later OpenAI text-only Face-up Pilot will require a separate route after the Codex transfer gate passes.
""".strip()


def main() -> int:
    print(MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
