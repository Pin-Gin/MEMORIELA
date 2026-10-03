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
- POST_GENERATION_COMPARISON_REFERENCE = NONE
- ACTUAL_VISUAL_REFERENCES_AVAILABLE = NOT_REQUIRED

If any image is supplied to the image-generation execution:
`GENERATION_ALLOWED = NO`

For the current author-approved TEXT_ONLY completion target, the repository Root Master PNG is also excluded from post-generation acceptance / stability comparison.

Do not:
- attach the repository Root Master PNG to generation
- inspect it as part of the current TEXT_ONLY acceptance target
- describe it into the generation payload
- use it during a generation-time retry
- use it as a post-generation comparison reference for this TEXT_ONLY target
- allow another file to instruct PNG priority inside this submode

The current TEXT_ONLY target is evaluated against the protected text Authorities and active fixed `PAYLOAD.txt` only.

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

FRONT uses the root YURA Visual Master.
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
