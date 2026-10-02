# YURA TEXT-ONLY ROOT SINGLE-RUN PROTOCOL

Status: **PROTECTED / MANDATORY**

Purpose:
Text-only Root stability testを常に「1回 = 1人 = 1枚」の独立生成として実行する。

## Controller-only batch rule
3枚 / 5枚などの枚数指定はController / QAだけが知る。

Image generation must not receive:
- batch size
- candidate count
- comparison sheet wording
- triptych wording
- side-by-side wording
- multi-variant wording

## Per-call invariant
Every call:
- uses exactly `TEXT_ONLY_ROOT_EXECUTION.md`
- uses no visual reference
- uses no appended ad-hoc prompt
- uses the same framing/aspect class
- requests exactly one YURA
- requests exactly one composition
- requests exactly one canvas
- returns exactly one image

## Text-only retry rule
`TARGETED_RETRY = FORBIDDEN`

Reason:
Text-only regeneration is a new stochastic full-image sample; unaffected pixels/domains cannot be guaranteed to remain fixed.

When any protected domain fails:
1. reject the entire candidate
2. do not mutate the fixed Execution Block inside the active batch
3. run full QA
4. if the batch still has enough valid runs, continue
5. otherwise start a new independent single run using the same unchanged block

Only after repeated valid isolated runs show the same failure may the Execution Block or source Authority be revised.
Any revision starts a **new batch**.

## Invalid run
Exclude from stability evidence if:
- more than one YURA
- more than one panel
- multiple poses
- triptych / contact sheet
- character sheet
- labels / swatches / measurements
- altered Execution Block
- any generation-time image reference
- targeted prompt mutation after a failed candidate

Invalid run = execution-control failure, not Text Authority evidence.
