# YURA TEXT-ONLY ROOT MASTER CREATION PROFILE

Status: **PROTECTED / FIXED INPUT PROFILE**

Master Creation Submode:
`TEXT_ONLY_ROOT_MASTER`

Purpose:
YURAを画像参照なしで生成し、Text Authority単独でRoot identityが安定するか確認する。

## Generation-time reference policy
`VISUAL_REFERENCES_ALLOWED = NONE`

Forbidden during generation:
- current `YURA_VISUAL_MASTER.png`
- future Face Master
- BODY View Masters
- previous YURA generations
- previous chat images
- pose references
- outfit references
- scene references
- cropped / edited derivatives
- any image used as an implicit identity hint

Do not pass any visual reference to the image-generation execution.

## Required semantic text inputs
Load exactly:
1. `visuals/yura/identity/master/YURA_VISUAL_TEXT.md`
2. `visuals/yura/identity/body/BODY_SPEC.md`
3. `visuals/yura/identity/face/FACE_SPEC.md`
4. `visuals/yura/identity/eyes/EYE_SPEC.md`
5. `visuals/yura/identity/hair/HAIR_SPEC.md`
6. `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md`
7. `visuals/yura/identity/skin/SKIN_SPEC.md`
8. `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`
9. `visuals/CHARACTER_RENDERING_STYLE.md`
10. `visuals/yura/generation/GENERATION_RULES.md`
11. `visuals/yura/qa/VALIDATION_CLOTHING.md`

Governance files may be read for Gate execution, but they must not introduce visual-image information into the generation call.

## Fixed generation condition
- exactly one YURA
- front-facing
- full body
- head top through toes visible
- centered
- straight neutral standing pose
- arms naturally lowered
- legs nearly together
- minimal perspective distortion
- neutral / very soft expression
- default Normal Super-Long
- validation clothing only
- barefoot
- white / warm-white background
- no props
- no text / labels / panels
- no school uniform
- no hairstyle variation
- no outfit variation
- no pose variation
- no scene variation

Use the same framing/aspect/resolution conditions across one stability batch.

## Variation policy
`AI_INFERENCE_REQUIRED = NONE`
`USER_AUTHORIZED_VARIATION = NONE`

Do not improve, beautify, modernize, stylize or reinterpret YURA.

## Batch rule
For stability evaluation:
- minimum: 3 independent candidates
- preferred: 5 independent candidates
- generate each candidate as one YURA / one image
- keep all text inputs and generation conditions unchanged within the batch

Do not choose the best image first and treat the others as irrelevant.
Evaluate cross-run variance.

## Post-generation comparison
After each candidate is generated, the current approved Root Master may be viewed for QA comparison only.

It must not be supplied to the generation call.

If the comparison reveals a mismatch:
- identify the failing text/domain rule
- do not copy incidental pixels/features from the old Master into a prompt
- do not change canon to fit a failed candidate
- text may be corrected only when the author confirms that the existing text fails to encode the intended identity

## Candidate status
Every output is:
`CANDIDATE / NOT AUTHORITY`

until explicit author approval and Root Master adoption.
