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

## Per-call execution carrier
Before every image-generation call:
1. resolve the active Execution Carrier
2. verify that the actual generation-facing context contains the fixed `TEXT_ONLY_ROOT_EXECUTION.md` `FIXED EXECUTION BLOCK` semantics
3. when using `CONVERSATION_CONTEXT_CARRIER`, materialize that fixed block immediately before the image-generation call without ad-hoc paraphrase
4. do not assume connector/Git retrieval output is automatically visible to the image-generation instruction synthesizer

Invalid:
- path-only handoff
- "follow Git" without payload semantics
- "same as previous"
- EXTERNAL_RETRIEVAL_ONLY

If semantic handoff cannot be verified:
`GENERATION_ALLOWED = NO`

## Per-call invariant
Every call:
- uses exactly `TEXT_ONLY_ROOT_EXECUTION.md`
- has a valid Execution Carrier
- has the fixed generation semantics present in the actual generation-facing context
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
