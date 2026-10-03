# YURA TEXT-ONLY ROOT RUN CONTROLLER

Status: **PROTECTED / CONTROLLER-ONLY / MANDATORY**

Purpose:
`PAYLOAD.txt` を画像生成モデルへ渡す処理と、Gate / QA / retry / batch管理を分離する。

## Hard boundary
This file is **NOT image-generation input**.

The image-generation model receives only:
`visuals/yura/execution/text-only-root/PAYLOAD.txt`

Do not append this file, Gate text, QA text, retry text, batch text, Git paths, or prior-generation discussion to the generation-facing context.

## Mode
- MODE = MASTER_CREATION
- MASTER_CREATION_SUBMODE = TEXT_ONLY_ROOT_MASTER
- REFERENCE_POLICY = NONE
- generation-time visual references = NONE
- AI_INFERENCE_REQUIRED = NONE
- USER_AUTHORIZED_VARIATION = NONE

## Execution carrier
Use:
- `DIRECT_MODEL_INPUT` when a controllable model-facing instruction field exists
- otherwise `CONTEXT_DERIVED_TEXT_EXECUTION`

For context-derived execution:
- materialize the actual semantics of `PAYLOAD.txt` immediately before the image-generation call
- do not replace it with path-only shorthand such as `follow Git` or `same as before`
- do not mix unrelated conversation content into the generation handoff

## One-run invariant
Every image-generation call must be:
- exactly one YURA
- one figure
- one canvas
- one composition
- one image
- front-facing full body
- neutral upright standing
- white / warm-white background
- validation clothing
- no generation-time image reference

Invalid:
- character sheet
- multi-pose sheet
- multi-panel
- triptych
- contact sheet
- side-by-side variants
- multiple figures
- labels / measurements / swatches

## Payload integrity
Per call:
- load current `PAYLOAD.txt`
- use it unchanged within the active stability batch
- no per-run paraphrase
- no ad-hoc correction wording
- no targeted mutation
- no batch-size wording
- no QA verdict wording
- no candidate-comparison wording

## Failure handling
`TARGETED_RETRY = FORBIDDEN`

If any protected domain fails:
1. reject the whole candidate
2. do not promote it to Authority or protected reference
3. do not use it as the next generation carrier
4. keep `PAYLOAD.txt` unchanged inside the active batch
5. generate a new independent whole candidate
6. run all mandatory QA again

If the same protected domain repeatedly fails across valid isolated runs:
- stop the active batch
- diagnose `PAYLOAD.txt` against `SOURCE_LOCK.md` and the protected Authorities
- revise outside the batch only
- start a new batch after revision

## UI visibility
Generation-tool/UI visibility before QA is not acceptance.

`USER_VISIBLE != ACCEPTED`
`USER_VISIBLE != AUTHORITY`

Fail-Closed applies to acceptance, Authority promotion, and future protected-reference use.
