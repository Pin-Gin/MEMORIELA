# YURA REFERENCE GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
Generation-time visual references:
`NONE`

Required:
- IDENTITY_ROOT_REFERENCE = NONE
- FACE_DETAIL_REFERENCE = NONE
- BODY_VIEW_REFERENCE = NONE
- OUTFIT_REFERENCE = NONE
- POSE_ONLY_REFERENCE = NONE
- SCENE_REFERENCE = NONE
- ACTUAL_VISUAL_REFERENCES_AVAILABLE = NOT_REQUIRED

If any image is supplied to the image-generation execution:
`GENERATION_ALLOWED = NO`

The current registered Root Master may be viewed only **after** a candidate exists and only as:
`POST_GENERATION_COMPARISON_REFERENCE`

Do not:
- attach it to generation
- describe it into the generation payload
- use it during a generation-time retry
- allow another file to instruct PNG priority inside this submode

## PRODUCTION
Only Gate-approved references may be attached in declared roles.

Root whole-character Identity:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Face detail:
`visuals/yura/identity/master/face/YURA_FACE_MASTER.png`

Missing required production reference:
`GENERATION_ALLOWED = NO`

## BODY view — PRODUCTION
Resolve through `VIEW_ROUTER.md`.

FRONT uses the root YURA Master.
Non-front uses exactly one routed BODY View Master.

Do not:
- load all BODY view Masters at once
- average neighboring view anchors
- substitute a missing view
- let BODY view reference redesign FACE / HAIR / outfit / rendering

## Actual-reference requirement
For modes that require visual references, Git existence alone is not enough.
The actual approved image must be available to execution in the declared role.

Rejected / intermediate images are denied.
