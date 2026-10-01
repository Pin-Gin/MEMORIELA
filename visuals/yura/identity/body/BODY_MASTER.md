# YURA BODY MASTER

Status: PROTECTED FRONT BODY MASTER
Approved: 2026-09-12
Character: 久遠ゆら / YURA

## Approved generation

- gen_id: `23d14b91-3551-4685-a162-fdd734b814f2`
- approval: **「これで決定しましょう！」**
- role: authoritative front-view BODY proportion reference

## Relationship to current VISUAL MASTER

Current canonical neutral visual master:

- `visuals/yura/identity/master/VISUAL_MASTER.md`
- gen_id: `e942a217-75fd-4154-88cc-6c0f74e99d82`

The VISUAL MASTER is the preferred whole-character appearance reference, while this BODY MASTER remains authoritative for body geometry.

If a small visual discrepancy exists between the neutral VISUAL MASTER and the BODY text / BODY MASTER, **BODY geometry rules win for anatomy**.

Important example:

- the current `e942...` visual master is the current whole-character identity / Normal Super-Long visual anchor
- a later candidate `40ef612e-dfcb-4b0d-a041-4b881af5ff9c` slightly increased arm fullness but introduced subtle face / eye drift and was rejected as master
- therefore future generations should keep the current `e942...` whole-character identity while still following this BODY rule that arms are slender **but not overly thin / skeletal**

Do not use the slightly slimmer-looking arms in a single visual artifact to weaken the protected BODY rule.

## Authority scope

This master fixes YURA's approved body geometry and front-view proportion balance:

- 153 cm petite adult scale
- **exact design target: 7.25 heads tall**
- slender / delicate build without skeletal thinness
- somewhat narrow natural adult-female shoulders
- slender compact ribcage
- bust clearly/moderately fuller relative to the petite frame
- soft hemispherical bust direction with gentle upper slope and fuller lower contour
- standard-to-slightly-short torso
- slim natural waist
- flat-leaning abdomen with slight natural softness
- natural adult-female pelvis / hips, approximately shoulder width to slightly wider
- standard-to-slightly-long legs
- slender thighs with natural softness
- small / restrained knees
- slender gently curved calves and slim plausible ankles
- arms slender to slightly below standard thickness, explicitly not stick-thin
- small-to-standard hands with slightly long elegant fingers
- standard natural feet for a 153 cm adult woman

## Scale invariance — PROTECTED

**7.25 heads is invariant under canvas / image-size changes.**

Changing canvas dimensions, aspect ratio, export size, display size, or character occupancy must not change BODY geometry.

- crown-to-sole total figure height = **7.25 × head height**
- scale the **entire figure uniformly**
- head, neck, torso, pelvis, thighs, calves, arms, hands and feet all use the same scale factor
- do not enlarge the head when the figure is made smaller
- do not thicken thighs / calves when moving to a taller canvas
- do not lengthen / shorten legs because aspect ratio changed
- do not compress / stretch torso to fill canvas
- absorb format changes through background / negative space
- if necessary, make the entire character smaller rather than violate 7.25 heads

Different image size = layout change, **not BODY redesign**.

## Non-authoritative details in BODY baseline image

The following are not BODY identity:

- exact ivory camisole design
- exact shorts design / trim
- black ribbon decorations
- small blue floral hair ornament
- hand touching hair
- crossed-ankle stance
- exact white studio background

## Generation rule

For ordinary full-body generation:

1. `visuals/yura/identity/master/VISUAL_MASTER.md`
2. this BODY MASTER
3. `visuals/yura/identity/body/BODY_SPEC.md`
4. current FACE / HAIRSTYLE / RENDERING specs
5. outfit / pose / scene request

Do not let styling or an arbitrary derivative override protected anatomy.

## Side / back continuity

Exact SIDE and BACK views must preserve:

- shoulder width
- ribcage width
- bust volume
- waist / pelvis relationship
- thigh / calf / arm proportions

In BACK view, YURA's very long hair remains naturally behind the shoulders and down the back. BODY visibility is subordinate to hairstyle continuity in an ordinary back master.

## Validation history

Three-view candidate:
- gen_id: `a8057649-8f02-4ad2-bb48-ec50bafd0727`
- not approved due back-hair distribution, not BODY failure

Back-hair follow-up:
- gen_id: `8c15fda2-194d-40fc-a8f1-176fe14b15cf`
- still insufficient rear hair mass; back-view iteration paused

Portrait-format validation:
- gen_id: `24b1e4e2-9930-4fc0-bec7-d0a555da09c7`
- target: approximately 33.6 cm × 59.7 cm / 9:16
- rule: exact 7.25 heads + fixed limb thickness + uniform whole-character scaling
- user assessment: **「OK 変わりなし」**
- result: PASS

## Change control

Do not replace or materially alter this BODY MASTER without explicit user approval.


---

## BODY geometry preservation routing — 2026-09-20

For single-domain-only changes such as outfit-only / hair-only / background-only / expression-only, and for exact-preservation / controlled validation tasks, apply:

`visuals/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

The derivative layer never authorizes BODY change.

A garment-change mask may overlap BODY pixels in the raster image, but protected anatomy remains locked independently.

Strict BODY-preservation production requires `BODY_GEOMETRY_GUARANTEED`. If the execution route must re-infer hidden BODY geometry stochastically and no verified BODY geometry carrier exists, return:

`BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED`
