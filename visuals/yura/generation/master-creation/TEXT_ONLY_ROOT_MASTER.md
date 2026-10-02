# YURA TEXT-ONLY ROOT MASTER CREATION PROFILE

Status: **PROTECTED / FIXED INPUT PROFILE**

Master Creation Submode:
`TEXT_ONLY_ROOT_MASTER`

Purpose:
画像参照を一切使わず、現行YURA Text Authorityからコンパイルした実行PayloadでRoot identityの安定性を検証する。

## Generation-time reference policy
`VISUAL_REFERENCES_ALLOWED = NONE`

No image may be supplied to the image-generation execution.

## Authority resolution inputs
Gate / compiler resolves the current protected sources:
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md`
- `visuals/yura/identity/body/BODY_SPEC.md`
- `visuals/yura/identity/face/FACE_SPEC.md`
- `visuals/yura/identity/eyes/EYE_SPEC.md`
- `visuals/yura/identity/hair/HAIR_SPEC.md`
- `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md`
- `visuals/yura/identity/skin/SKIN_SPEC.md`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`
- `visuals/CHARACTER_RENDERING_STYLE.md`
- `visuals/yura/qa/VALIDATION_CLOTHING.md`

These documents are resolution sources.
They are **not** dumped directly into the image-generation call.

## Mandatory execution payload
Image generation receives:
`visuals/yura/generation/execution/TEXT_ONLY_ROOT_EXECUTION.md`

Execution orchestration follows:
`visuals/yura/generation/execution/TEXT_ONLY_ROOT_SINGLE_RUN.md`

No raw Gate / QA / batch instruction is appended to the generation payload.

## Fixed generation condition
The fixed condition is fully compiled into `TEXT_ONLY_ROOT_EXECUTION.md`.

Do not add:
- batch count
- candidate comparison language
- QA verdict language
- Git paths
- rejection tables
- Master PNG descriptions outside the compiled text payload

## Variation policy
`AI_INFERENCE_REQUIRED = NONE`
`USER_AUTHORIZED_VARIATION = NONE`

## Stability batch
Controller / QA layer:
- minimum 3 valid independent single-image runs
- preferred 5 valid independent single-image runs

The image-generation model must not receive batch-size or comparison-sheet instructions.

## Post-generation comparison
After each valid single-image run, the registered Root Master may be used for QA comparison only.

It must not be supplied to any text-only generation call or retry.

## Candidate status
Every valid output remains:
`CANDIDATE / NOT AUTHORITY`

until explicit author approval and adoption.
