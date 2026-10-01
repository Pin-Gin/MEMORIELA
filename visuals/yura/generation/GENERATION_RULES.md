# YURA GENERATION RULES

Status: **CANONICAL / MANDATORY**

## Compile order
1. Visual Master identity
2. BODY
3. FACE
4. EYE
5. HAIR
6. requested pose / camera
7. outfit
8. expression
9. scene / background
10. Matte Natural Anime rendering

Later layers never redefine earlier protected layers.

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
- bright fair skin
- YURA-specific rendering

## Color lock
- iris = blue-gray
- hair = silver-white
- skin = bright fair
- lighting may affect appearance subtly but not identity color

## Hair default
For ordinary YURA:
- load `../identity/hair/HAIR_SPEC.md`
- load `../identity/hair/styles/NORMAL_SUPER_LONG.md`

Do not load optional hairstyle specs unless requested.

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
- current approved YURA Visual Master is the whole-character visual anchor
- do not use rejected / intermediate generations as identity authority
- do not silently promote a derivative into a new master
- pose references, when used, are pose-only references

## Retry rule
When one domain fails, fix that domain only.

Examples:
- wrong eye color → fix EYE only
- wrong hair length → fix HAIR only
- chest shrinks in twist → fix pose/projection continuity, not BODY canon
- validation clothing becomes decorative → fix outfit only

Do not rewrite YURA to fit a failed generation.
