# YURA POSE RULES

Status: **PROTECTED / MANDATORY FOR SIGNIFICANT MOTION**

## Core rule
**動的ポーズではYURAのBODYを再設計せず、固定されたYURA BODYを関節回転・重心移動・接触変形だけでポーズさせる。**

Apply to:
- torso twist
- 3/4 turn
- side-oriented pose
- seated
- squat / crouch
- kneeling
- forward / backward bend
- lateral lean
- reaching
- stepping / walking / running
- furniture contact
- other meaningful movement

## Identity Lock
Pose must not change:
- face
- blue-gray eyes
- silver-white hair
- 153 cm concept
- 7.25-head system
- shoulders
- ribcage
- bust volume
- waist
- pelvis
- limb lengths / baseline thickness

## Skeleton Transform Only
Use:
- position
- rotation
- joint angle
- segment orientation
- center-of-mass shift
- support / contact

Do not use:
- segment length changes
- baseline width changes
- anatomy redesign

## Perspective Lock
Resolve camera separately:
- height
- distance
- view direction
- perspective / focal character
- pitch / yaw / roll

Foreshortening is projection, not BODY change.

## Torso Twist / 3/4 / Side Lock
- shoulder and pelvis may rotate
- ribcage geometry remains stable
- waist remains stable
- pelvis remains stable
- **bust actual volume remains stable**

When frontal area decreases:
- preserve side depth / forward projection
- show far-side volume through overlap / occlusion
- do not flatten the chest
- do not delete far-side volume
- do not widen ribcage to compensate

## Seated / Squat / Kneeling Lock
Allowed:
- local plausible soft-tissue compression
- overlap
- clothing folds
- perspective compression

Not allowed:
- pelvis redesign
- hip-width redesign
- permanent thigh/calf thickening
- leg shortening
- bust/ribcage redesign

## Hair Conservation
Movement may alter placement via gravity/contact/overlap.
Do not alter:
- source total mass
- protected principal length
- tip upper limit
- source topology

## Contact / load
- support points must be coherent
- limbs carrying weight must visibly connect and align
- hidden limbs must not carry unexplained load
- hands / feet / joints must remain anatomically plausible

## Dynamic Pose QA
Check independently:
1. identity
2. BODY geometry
3. joints
4. support/contact/load
5. chest continuity
6. hair conservation
7. camera/perspective
8. hands/feet/limb count

If one item fails, retry pose/projection/contact only.
Never change canon to rescue a failed pose.
