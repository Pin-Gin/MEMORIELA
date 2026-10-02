# YURA REFERENCE GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## Mode-specific reference policy

### MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
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

If any image is supplied to the generation execution:
`GENERATION_ALLOWED = NO`

The current approved Root Master may be viewed only after candidate generation as:
`POST_GENERATION_COMPARISON_REFERENCE`

It must not be fed into generation or a generation-time retry.

### PRODUCTION
Only:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`
may serve as the root whole-character Identity reference.

PRODUCTION always requires:
`visuals/yura/identity/master/face/YURA_FACE_MASTER.png`

Role:
FACE_DETAIL_REFERENCE

If absent or unavailable to the actual generation execution:
`GENERATION_ALLOWED = NO`

Do not substitute:
- cropped derivative from an unapproved generation
- previous chat image
- prior successful derivative
- similar face image

## BODY view — PRODUCTION / BODY_VIEW_MASTER
Resolve through `VIEW_ROUTER.md`.

FRONT uses root YURA Master.
Non-front uses exactly one routed BODY View Master in PRODUCTION.

Do not:
- load all BODY view Masters at once
- average two neighboring angles
- substitute a missing angle
- let a BODY view reference redesign FACE / HAIR / outfit / rendering

## Actual-reference requirement
For modes that require visual references, a PNG existing in Git is not sufficient by itself.
PASS requires that the actual approved image is available to the image-generation execution as the declared role.

## Additional references
Pose / outfit / scene references are allowed only with declared roles from `../../gate-core/REFERENCE_ROLE_RULES.md`.

Rejected / intermediate images are denied.
