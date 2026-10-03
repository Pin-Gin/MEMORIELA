# YURA FACE ROOT GEOMETRY REFINEMENT PROFILE

Status: PROTECTED / FIXED INPUT PROFILE / IMAGE-EDIT REFINEMENT

Master Creation Submode:
`FACE_ROOT_GEOMETRY_REFINEMENT`

Purpose:
TEXT_ONLY Face Root candidateのうち、EAR geometryのみがprotected targetから外れ、他のFace Root protected domainsがPASSしている候補について、顔全体との相対空間を保持したままEAR geometryを補正する。

Required input:
- candidate classified `REFINEMENT_ELIGIBLE` by `visuals/yura/qa/FACE_ROOT_QA.md`
- FACE / EYE / HAIR FRAMING / SKIN / RENDERING / composition = PASS
- at least one ear observable
- EAR geometry alone = FAIL
- no other protected-domain FAIL

Generation-time visual Reference roles:
`NONE`

Required non-reference image input:
exactly one eligible candidate as `EDIT_SOURCE_CARRIER`.

The edit source carrier is not Authority, not an Identity or Production Reference, and not Canon evidence. It supplies only the existing pixel/layout coordinate system for correction of that same candidate.

No other image may be supplied.

Authority resolution inputs:
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md`
- `visuals/yura/identity/face/FACE_SPEC.md`
- `visuals/yura/identity/ears/EAR_SPEC.md`
- `visuals/yura/identity/eyes/EYE_SPEC.md`
- `visuals/yura/identity/hair/HAIR_SPEC.md` — face-framing / color / material only
- `visuals/yura/identity/skin/SKIN_SPEC.md`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`
- `visuals/CHARACTER_RENDERING_STYLE.md`

Execution package:
- payload: `visuals/yura/execution/face-root-refinement/PAYLOAD.txt`
- controller: `visuals/yura/execution/face-root-refinement/RUN.md`
- source lock: `visuals/yura/execution/face-root-refinement/SOURCE_LOCK.md`
- QA: `visuals/yura/qa/FACE_ROOT_REFINEMENT_QA.md`

Refinement target:
- ear vertical length approximately 28–30% of forehead-to-chin face vertical length
- slightly-small visual read
- restrained projection
- approximately 5–10 degree posterior tilt when observable
- no visibility-driven enlargement, lengthening, outward movement, or camera-facing rotation
- do not alter FACE or HAIR geometry merely to expose an ear

The edit request may preserve already-passing non-EAR content, but preservation is not assumed or guaranteed. Every output is a new candidate and all protected Face Root domains must be re-evaluated.

A failed refinement output must not become the next edit-source carrier. If another refinement run is authorized, use the same originally eligible edit-source candidate and the same fixed refinement payload.

Only after refinement QA PASS and explicit author approval may the result be registered as:
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

Declared later-use role after adoption only:
`FACE_DETAIL_REFERENCE`
