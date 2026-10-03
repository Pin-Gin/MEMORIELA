# YURA FACE-ANCHORED ROOT RUN CONTROLLER

Status: **PROTECTED / CONTROLLER-ONLY / MANDATORY / BLOCKED UNTIL FACE ROOT ADOPTED**

This file is **NOT image-generation input**.

The image-generation model receives:
1. `visuals/yura/execution/face-anchored-root/PAYLOAD.txt`
2. exactly one approved `FACE_DETAIL_REFERENCE`: `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

No other image reference is allowed in this submode.

## Mode
- MODE = MASTER_CREATION
- MASTER_CREATION_SUBMODE = FACE_ANCHORED_ROOT_MASTER
- IDENTITY_ROOT_REFERENCE = NONE
- FACE_DETAIL_REFERENCE = approved Face Root only
- BODY_VIEW_REFERENCE = NONE
- OUTFIT_REFERENCE = NONE
- POSE_ONLY_REFERENCE = NONE
- SCENE_REFERENCE = NONE

## Hard dependency
Generation is forbidden until all are true:
- `YURA_FACE_ROOT.png` exists
- `YURA_FACE_ROOT.md` exists
- author approval is recorded
- exact image hash is recorded in `SOURCE_LOCK.md`
- the actual image is available to the generation execution

Git existence alone is not sufficient.

## Reference scope enforcement
FACE_DETAIL_REFERENCE controls only:
- face outline
- cheek / chin
- eyes
- nose / mouth
- ears
- face-framing hair boundary

It must not redesign:
- BODY
- chest / shoulders / pelvis / legs
- full hair length
- validation clothing
- full-body pose
- rendering style

## One-run invariant
- exactly one YURA
- one figure
- one canvas
- one composition
- one image
- front-facing full body
- neutral upright standing
- white / warm-white background
- validation clothing

## Payload integrity
- use current `PAYLOAD.txt` unchanged inside an active batch
- no extra face-correction prose appended per run
- no failed candidate used as reference
- only approved Face Root is the identity carrier

## Acceptance
Every output remains candidate only until `FACE_ANCHORED_ROOT_QA.md` and common YURA QA pass.
