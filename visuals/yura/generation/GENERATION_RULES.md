# YURA GENERATION RULES

Status: **CANONICAL / MANDATORY**

## Strict generation priority
1. **Current YURA Visual Master PNG**
2. **Visual Master manifest / transcription**
3. **BODY**
4. **FACE**
5. **EYE**
6. **HAIR + NORMAL_SUPER_LONG**
7. **SKIN**
8. requested pose / camera
9. outfit
10. expression
11. scene / background
12. YURA-specific rendering
13. project-wide Matte Natural Anime rendering
14. output hygiene / QA

### Priority meaning
- The current approved Master PNG is the whole-character visual anchor.
- BODY / FACE / EYE / HAIR / SKIN are protected constraints used to prevent drift from the Master.
- These protected specs do not independently rebuild YURA from zero when a current Master is available.
- Later layers never redefine earlier protected layers.
- Pose, camera, outfit, expression, scene and rendering may change presentation only.
- Rejected / intermediate generations must not be used as Identity references.

## One-person rule
Unless explicitly requested otherwise:
- exactly one YURA
- one image / one figure
- no character sheet
- no multi-pose sheet
- no automatic front+side+back layout

Multiple requested images are generated separately.

## Identity lock
Always preserve:
- 153 cm concept
- exact 7.25-head BODY
- YURA face
- blue-gray eyes
- silver-white hair
- default Normal Super-Long unless another hairstyle is explicitly requested
- SKIN per `../identity/skin/SKIN_SPEC.md`
- YURA-specific rendering

## Color lock
- iris = blue-gray
- hair = silver-white
- skin = `../identity/skin/SKIN_SPEC.md`
- lighting may affect appearance subtly but not identity color

## Hair default
For ordinary YURA:
- load `../identity/hair/HAIR_SPEC.md`
- load `../identity/hair/styles/NORMAL_SUPER_LONG.md`

Do not load optional hairstyle specs unless requested.

## Skin default
Always load:
- `../identity/skin/SKIN_SPEC.md`

Skin identity must not be inferred from rendering style alone.

## Pose route
For meaningful motion, also load `POSE_RULES.md`.

Pose controls:
- joint positions
- segment orientation
- center of gravity
- support / contact
- camera projection

Pose does not control:
- identity
- BODY dimensions
- hair source length / mass
- skin identity
- rendering

## Outfit route
For clothing changes, also load `OUTFIT_RULES.md`.

Clothing follows BODY.
BODY does not reshape to fit clothing.

## Validation route
For controlled validation:
- white background
- barefoot
- load `../qa/VALIDATION_CLOTHING.md`
- run `../qa/GENERATION_QA.md`

## Framing
Framing is a layout variable, not BODY authority.

Allowed examples:
- full body
- knee-up
- waist-up
- bust-up
- face close-up
- manga-panel composition

Perspective / crop may alter what is visible but not underlying anatomy.

## Reference discipline
- current approved YURA Visual Master PNG is the sole whole-character visual anchor
- do not use rejected / intermediate generations as identity authority
- do not silently promote a derivative into a new master
- pose references, when used, are pose-only references

## Retry rule
When one domain fails, fix that domain only.

Examples:
- wrong eye color → fix EYE only
- wrong hair length → fix HAIR only
- wrong skin tone → fix SKIN only
- chest shrinks in twist → fix pose/projection continuity, not BODY canon
- validation clothing becomes decorative → fix outfit only

Do not rewrite YURA to fit a failed generation.
