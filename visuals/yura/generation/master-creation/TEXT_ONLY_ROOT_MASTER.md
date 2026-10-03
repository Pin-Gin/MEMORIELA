# YURA TEXT-ONLY ROOT MASTER CREATION PROFILE

Status: **PROTECTED / FIXED INPUT PROFILE / FINAL REFERENCE-FREE VERIFICATION**

Master Creation Submode:
`TEXT_ONLY_ROOT_MASTER`

Purpose:
現行YURA Text Authorityからコンパイルした固定Payloadだけで最終TEXT_ONLY再現安定性を検証する。

## Workflow dependency
Before starting a new final TEXT_ONLY stability batch:
- current text Authorities must represent the approved target
- `SOURCE_LOCK.md` must match all current protected source blobs

If those workflow dependencies are incomplete:
`TEXT_ONLY_ROOT_FINAL_VERIFICATION = DEFERRED`

## Generation-time reference policy
`VISUAL_REFERENCES_ALLOWED = NONE`

No image may be supplied to the image-generation execution.

Specifically forbidden from the generation call:
- repository `YURA_VISUAL_MASTER.png`
- previous generated candidates

`TEXT_ONLY` means the generation is driven only by resolved text Authorities and compiled text Execution Payload.
It does not require a direct raw-prompt API and may use a valid context-derived execution carrier.

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

## Rendering compilation requirement
The active payload must preserve the mandatory YURA rendering compilation lock from:
`visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`

Washed-out high-key / watercolor-like / pastel-faded / airbrush-only / invisible-line drift is not acceptable Matte Natural Anime.

## Variation policy
`AI_INFERENCE_REQUIRED = NONE`
`USER_AUTHORIZED_VARIATION = NONE`

## Stability batch
Controller / QA layer:
- minimum 3 valid independent single-image runs
- preferred 5 valid independent single-image runs

The generation model must not receive batch-size or comparison-sheet instructions.

## Post-generation comparison
`POST_GENERATION_COMPARISON_REFERENCE = NONE`

Post-generation QA compares the candidate against protected text Authorities and mode QA only.

## Candidate status
Every valid output remains:
`CANDIDATE / NOT AUTHORITY`

until explicit author approval and adoption.
