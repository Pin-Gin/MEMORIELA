# YURA REFERENCE GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## Identity root
Only:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`
may serve as the root whole-character Identity reference.

## Face detail
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

## BODY view
Resolve through `VIEW_ROUTER.md`.

FRONT uses root YURA Master.
Non-front uses exactly one routed BODY View Master.

Do not:
- load all BODY view Masters at once
- average two neighboring angles
- substitute a missing angle
- let a BODY view reference redesign FACE / HAIR / outfit / rendering

## Actual-reference requirement
A PNG existing in Git is not sufficient by itself.
PASS requires that the actual approved image is available to the image-generation execution as the declared role.

## Additional references
Pose / outfit / scene references are allowed only with declared roles from `../../gate-core/REFERENCE_ROLE_RULES.md`.

Rejected / intermediate images are denied.
