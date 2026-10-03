# YURA TEXT-ONLY ROOT MASTER CREATION PROFILE

Status: **PROTECTED / FIXED INPUT PROFILE**

Master Creation Submode:
`TEXT_ONLY_ROOT_MASTER`

Purpose:
画像参照を一切使わず、現行YURA Text Authorityからコンパイルした実行PayloadでRoot identityの安定性を検証する。

## Generation-time reference policy
`VISUAL_REFERENCES_ALLOWED = NONE`

No image may be supplied to the image-generation execution.

`TEXT_ONLY` is a Source / Reference Mode.
It means the generation is driven only by the resolved text Authorities and compiled text Execution Payload.
It does not require a direct raw-prompt API and must not be blocked merely because the image interface derives instructions from conversation context.

## Authority resolution inputs
Gate / compiler resolves the current protected sources:
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md`
- `visuals/yura/identity/body/BODY_SPEC.md`
- `visuals/yura/identity/face/FACE_SPEC.md`
- `visuals/yura/identity/ears/EAR_SPEC.md`
- `visuals/yura/identity/eyes/EYE_SPEC.md`
- `visuals/yura/identity/hair/HAIR_SPEC.md`
- `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md`
- `visuals/yura/identity/skin/SKIN_SPEC.md`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`
- `visuals/CHARACTER_RENDERING_STYLE.md`
- `visuals/yura/qa/VALIDATION_CLOTHING.md`

These documents are resolution sources.
They are **not** dumped directly into the image-generation call.

## Isolated execution package
Image-generation semantic input only:
`visuals/yura/execution/text-only-root/PAYLOAD.txt`

Controller only:
`visuals/yura/execution/text-only-root/RUN.md`

Source-integrity lock only:
`visuals/yura/execution/text-only-root/SOURCE_LOCK.md`

Only `PAYLOAD.txt` may enter the generation-facing semantic context.
`RUN.md` and `SOURCE_LOCK.md` must never be appended to it.

## Fixed generation condition
The fixed generation condition is fully compiled into `PAYLOAD.txt`.

Do not add to the generation handoff:
- batch count
- candidate comparison language
- QA verdict language
- Git paths
- rejection tables
- retry procedure
- Master PNG descriptions
- prior-generation discussion

## Variation policy
`AI_INFERENCE_REQUIRED = NONE`
`USER_AUTHORIZED_VARIATION = NONE`

## Source integrity
Before generation, `SOURCE_LOCK.md` must match the current protected source blobs.

If any locked Authority changed without deliberate payload recompilation:
`PAYLOAD_SOURCE_LOCK = STALE`
`GENERATION_ALLOWED = NO`

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
