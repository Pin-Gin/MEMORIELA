# 久遠ゆら BODY SPEC

Status: **PROTECTED / CURRENT**

## Core
- Height concept: **153 cm**
- Total body ratio: **exactly 7.25 heads tall**
- Adult woman; petite / slender / delicate, not childlike and not skeletal
- Head remains adult-balanced; do not enlarge it to express small stature
- Legs: standard to slightly long inside the 7.25-head system

## Neck / shoulders
- neck: slender to standard, natural adult length
- shoulders: somewhat narrow
- shoulder line: soft natural slope
- no broad / athletic / square shoulders

## Ribcage / bust
Ribcage:
- slender and compact
- do not widen the upper torso to support bust volume

Bust:
- **moderately fuller relative to YURA's petite/slender frame**
- soft hemispherical direction
- restrained upper fullness
- naturally fuller lower contour
- natural forward projection
- smooth transition into ribcage
- not independently oversized
- not implant-like / rigid / conical

### Front / 3/4 / side continuity — mandatory
The same physical bust volume must remain across viewing angles.

For twist / 3/4 / side:
- frontal visible area may decrease by projection
- **actual volume must not decrease**
- preserve side depth and forward projection
- far-side volume is represented by overlap / occlusion / perspective, not deletion
- do not flatten the chest toward the camera
- do not widen the ribcage to compensate

## Torso / waist / abdomen
- torso: standard to slightly short for an adult woman
- waist: slim and clearly defined, but not corset-like
- abdomen: flat-leaning with slight natural softness
- ribcage → waist → pelvis transition remains smooth

## Pelvis / hips
- natural adult-female pelvis width
- hips approximately similar to or slightly wider than shoulders
- restrained soft roundness
- no exaggerated glamour hourglass
- neutral pelvic tilt by default

## Legs
- thighs: slender with natural softness; neither thick nor stick-thin
- knees: small/modest and anatomically readable
- calves: slender with gentle natural curve
- ankles: slim but plausible
- preserve thigh/calf proportions across angle and pose

## Arms / hands
- arms: slender to slightly below average adult-female thickness
- not stick-thin
- forearms retain natural thickness near elbow and taper toward wrist
- hands: small to standard for a petite adult woman
- fingers: slender, slightly long, softly tapered

## Feet
- natural size for a 153 cm adult woman
- do not make doll-small feet
- restrained 2D-anime detail

## Scale invariance
Canvas, crop, aspect ratio, camera distance, outfit and pose do not redefine BODY.

Preserve:
- 7.25-head ratio
- shoulder width
- ribcage
- bust volume
- waist
- pelvis / hip scale
- limb lengths
- baseline limb thickness

When framing changes, adapt composition and negative space rather than anatomy.

## Dynamic-pose invariant
**動的ポーズではYURAのBODYを再設計せず、固定されたYURA BODYを関節回転・重心移動・接触変形だけでポーズさせる。**

Allowed:
- joint rotation
- center-of-mass shift
- perspective / foreshortening
- local soft-tissue compression at contact

Not allowed:
- pose-driven segment length changes
- permanent thigh/calf inflation
- pelvis redesign
- chest-volume shrinkage
- torso widening
- childlike proportion drift

## Body-view anchor lock

BODY geometry is invariant. A body-view Master is a projection / silhouette anchor for a viewing direction, not a new BODY design.

- FRONT uses `../master/YURA_VISUAL_MASTER.png` as the front body-view anchor.
- Non-front orientations are routed by `../../gate/VIEW_ROUTER.md`.
- A selected body-view reference may stabilize projected shoulder width, ribcage depth, bust projection, waist depth, pelvis / hip silhouette and baseline limb thickness.
- A body-view reference must never redefine the protected BODY dimensions.
- When a required body-view anchor is missing, PRODUCTION must stop. Do not substitute a neighboring angle and do not infer the missing view from memory.
- Hidden or foreshortened anatomy must not be enlarged, rotated or exposed merely to make it easier to read.
- Visibility is governed by camera, pose, overlap and occlusion; it is not a target to maximize.

## Fail boundaries
FAIL if materially present:
- head/body ratio drift
- 8+ head fashion-model elongation
- childlike large head
- broad athletic shoulders
- enlarged ribcage
- chest reduction in side/3/4
- independently oversized chest
- extreme waist pinch
- over-wide hips
- skeletal or inflated limbs
- pose-dependent anatomy redesign
