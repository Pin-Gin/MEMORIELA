# YURA AUTHORITY MANIFEST

Status: **PROTECTED / EXACT-PATH MANIFEST**

Only paths listed here may participate in YURA Visual Authority resolution.

## Gate / governance
GATE:
`visuals/yura/gate/GENERATION_GATE.md`

MASTER_CREATION_FLOW:
`visuals/yura/gate/MASTER_CREATION_FLOW.md`

ROOT_STABILITY_STATUS:
`visuals/yura/identity/master/ROOT_MASTER_STABILITY_STATUS.md`

## Protected semantic authorities
ROOT_MASTER_MANIFEST:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.md`

VISUAL_TEXT:
`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

BODY:
`visuals/yura/identity/body/BODY_SPEC.md`

FACE:
`visuals/yura/identity/face/FACE_SPEC.md`

EAR:
`visuals/yura/identity/ears/EAR_SPEC.md`

EYE:
`visuals/yura/identity/eyes/EYE_SPEC.md`

HAIR:
`visuals/yura/identity/hair/HAIR_SPEC.md`

DEFAULT_HAIR:
`visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md`

SKIN:
`visuals/yura/identity/skin/SKIN_SPEC.md`

YURA_RENDERING_ADAPTER:
`visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`

PROJECT_RENDERING:
`visuals/CHARACTER_RENDERING_STYLE.md`

GENERATION_RULES:
`visuals/yura/generation/GENERATION_RULES.md`

QA:
`visuals/yura/qa/GENERATION_QA.md`

## TEXT_ONLY_FACE_ROOT_MASTER
PROFILE:
`visuals/yura/generation/master-creation/TEXT_ONLY_FACE_ROOT_MASTER.md`

EXECUTION_PAYLOAD:
`visuals/yura/execution/face-root/PAYLOAD.txt`

RUN_CONTROLLER:
`visuals/yura/execution/face-root/RUN.md`

SOURCE_LOCK:
`visuals/yura/execution/face-root/SOURCE_LOCK.md`

QA:
`visuals/yura/qa/FACE_ROOT_QA.md`

Reference policy:
`NONE`

Edit source policy:
`NONE`

Adoption slot:
`visuals/yura/identity/master/face-root/`

Expected approved artifact:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

Expected approved manifest:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

Declared role after adoption:
`FACE_DETAIL_REFERENCE`

## FACE_ROOT_GEOMETRY_REFINEMENT
PROFILE:
`visuals/yura/generation/master-creation/FACE_ROOT_GEOMETRY_REFINEMENT.md`

EXECUTION_PAYLOAD:
`visuals/yura/execution/face-root-refinement/PAYLOAD.txt`

RUN_CONTROLLER:
`visuals/yura/execution/face-root-refinement/RUN.md`

SOURCE_LOCK:
`visuals/yura/execution/face-root-refinement/SOURCE_LOCK.md`

QA:
`visuals/yura/qa/FACE_ROOT_REFINEMENT_QA.md`

Reference policy:
`NONE`

All declared visual reference roles:
`NONE`

Edit source policy:
`EXACTLY_ONE_ELIGIBLE_FACE_ROOT_CANDIDATE`

Edit source carrier:
Runtime-supplied candidate image only. It is not stored in this Manifest as Authority and has no Reference role.

Eligibility is controlled by `FACE_ROOT_QA.md` and `FACE_ROOT_GEOMETRY_REFINEMENT.md`.
The edit result is a new candidate and must pass the full refinement QA before author review.

Adoption target after QA PASS + explicit author approval remains:
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

## FACE_ANCHORED_ROOT_MASTER
PROFILE:
`visuals/yura/generation/master-creation/FACE_ANCHORED_ROOT_MASTER.md`

EXECUTION_PAYLOAD:
`visuals/yura/execution/face-anchored-root/PAYLOAD.txt`

RUN_CONTROLLER:
`visuals/yura/execution/face-anchored-root/RUN.md`

SOURCE_LOCK:
`visuals/yura/execution/face-anchored-root/SOURCE_LOCK.md`

QA:
`visuals/yura/qa/FACE_ANCHORED_ROOT_QA.md`

Required visual reference:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

Required role:
`FACE_DETAIL_REFERENCE`

No other visual reference is allowed for this Master-Creation submode.

## TEXT_ONLY_ROOT_MASTER — FINAL REFERENCE-FREE VERIFICATION
PROFILE:
`visuals/yura/generation/master-creation/TEXT_ONLY_ROOT_MASTER.md`

EXECUTION_PAYLOAD:
`visuals/yura/execution/text-only-root/PAYLOAD.txt`

RUN_CONTROLLER:
`visuals/yura/execution/text-only-root/RUN.md`

SOURCE_LOCK:
`visuals/yura/execution/text-only-root/SOURCE_LOCK.md`

STABILITY_QA:
`visuals/yura/qa/ROOT_MASTER_STABILITY_QA.md`

Reference policy:
`NONE`

The Face Root, face-anchored Root, repository Root Master PNG, and previous generations must not enter this final TEXT_ONLY generation handoff.

## Execution boundary
Raw semantic Authorities are resolved to validate the active Execution Payload.
They are not directly dumped into the image-generation call.

Only the active mode-specific `PAYLOAD.txt` may enter the text semantic handoff.
Controller / source-lock / Gate / QA / status documents are not image-generation input.

For `FACE_ROOT_GEOMETRY_REFINEMENT`, the generation execution may additionally receive exactly one Gate-authorized `EDIT_SOURCE_CARRIER` image. That image is not Authority and is not a Reference role.

## PRODUCTION visual references
IDENTITY_ROOT_REFERENCE:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

FACE_DETAIL_REFERENCE:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

## BODY view anchors
FRONT:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

FRONT_LEFT:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_FRONT_LEFT.png`

LEFT:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_LEFT.png`

BACK_LEFT:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_BACK_LEFT.png`

BACK:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_BACK.png`

BACK_RIGHT:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_BACK_RIGHT.png`

RIGHT:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_RIGHT.png`

FRONT_RIGHT:
`visuals/yura/identity/master/body-views/YURA_BODY_VIEW_FRONT_RIGHT.png`

Missing required non-front anchors block that PRODUCTION route.

## Conditional authorities
POSE:
`visuals/yura/generation/POSE_RULES.md`

OUTFIT:
`visuals/yura/generation/OUTFIT_RULES.md`

VALIDATION_CLOTHING:
`visuals/yura/qa/VALIDATION_CLOTHING.md`

SCHOOL_UNIFORM_PROFILE:
`visuals/yura/generation/profiles/SCHOOL_UNIFORM_YURA.md`

No alternate path or similar file is allowed.
