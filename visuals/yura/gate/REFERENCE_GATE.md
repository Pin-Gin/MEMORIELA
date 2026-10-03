# YURA REFERENCE GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## MASTER_CREATION / TEXT_ONLY_FACE_ROOT_MASTER
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

If any image is supplied to this Face Root generation execution:
`GENERATION_ALLOWED = NO`

## MASTER_CREATION / FACE_ANCHORED_ROOT_MASTER
Generation-time visual references:
exactly one approved Face Root.

Required:
- IDENTITY_ROOT_REFERENCE = NONE
- FACE_DETAIL_REFERENCE = `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
- BODY_VIEW_REFERENCE = NONE
- OUTFIT_REFERENCE = NONE
- POSE_ONLY_REFERENCE = NONE
- SCENE_REFERENCE = NONE
- ACTUAL_VISUAL_REFERENCES_AVAILABLE = PASS

The Face Root manifest and image hash must match `face-anchored-root/SOURCE_LOCK.md`.
The actual approved image must be available to the generation execution.
Git existence alone is insufficient.

Any other image supplied to this submode:
`GENERATION_ALLOWED = NO`

FACE_DETAIL_REFERENCE may control only:
- face outline
- cheek / chin balance
- eye identity / placement
- nose / mouth placement
- ear geometry
- face-framing hair boundary

It must not control BODY / full hair length / outfit / pose / scene / rendering style.

Rejected, unapproved, or previous full-body generations are denied.

## MASTER_CREATION / TEXT_ONLY_ROOT_MASTER — FINAL VERIFICATION
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

Do not attach or describe into this final TEXT_ONLY call:
- Face Root PNG
- face-anchored Root candidate / Master
- repository Root Master PNG
- previous generation

The final TEXT_ONLY target is evaluated against protected text Authorities and active fixed `PAYLOAD.txt` only.

## PRODUCTION
Only Gate-approved references may be attached in declared roles.

Root whole-character Identity:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Face detail:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

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
For every mode that requires visual references, Git existence alone is not enough.
The actual approved image must be available to execution in the declared role.

Rejected / intermediate images are denied.
