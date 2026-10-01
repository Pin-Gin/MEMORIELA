# YURA GENERATION QA

Status: **CANONICAL / CURRENT**

Evaluate domains independently. Do not average failures into one score.

## Gate 1 — Identity
PASS if:
- same YURA face impression
- adult readability
- blue-gray eyes
- silver-white hair
- bright fair skin
- no unrelated character traits

Visible wrong iris color = FAIL.

## Gate 2 — BODY
PASS if:
- 7.25-head system remains plausible
- petite/slender adult frame remains
- shoulders / ribcage / waist / pelvis relationships remain
- chest remains moderately fuller relative to frame
- limbs preserve lengths and baseline thickness
- pose has not redesigned anatomy

For twist / 3/4 / side:
- frontal area may reduce
- actual chest volume must remain
- side depth / forward projection must remain
- far-side volume must be represented by overlap / occlusion

## Gate 3 — FACE / EYE
Check:
- soft oval face
- small rounded chin
- eye geometry
- blue-gray iris
- pupil signature when resolvable
- nose / mouth remain YURA-like

## Gate 4 — HAIR
Default Normal Super-Long:
- silver-white
- principal ends = waist to slightly below
- only sparse longest fine tips may approach just before upper-buttock
- total mass slightly above standard
- restrained lateral spread
- center-back mass conserved
- no unauthorized braid / bun / ornament

## Gate 5 — RENDERING
PASS if:
- clear high-quality 2D anime
- Matte Natural Anime
- restrained gloss
- low-to-medium contrast
- YURA colors preserved
- no semi-real / PBR / realistic CGI drift

## Gate 6 — Request fidelity
Check requested:
- outfit
- hairstyle
- expression
- pose
- scene
- crop / framing

A request mismatch can fail while identity still passes.

## Gate 7 — Pose / physical structure
For significant movement, check:
- plausible joints
- support/contact/load
- center of gravity
- perspective
- chest continuity
- hair conservation
- hands / feet / limb count

Pose failure must not trigger BODY canon changes.

## Gate 8 — Output hygiene
Check:
- extra / missing limbs
- broken hands / feet
- unintended text / logos
- duplicate props
- severe crop / occlusion accidents

## Validation clothing gate
When validation clothing is required:
- broad-shoulder sleeveless top
- plain shorts
- no drawstring / bow / lace / frill
- pale / opaque / matte
- barefoot
- white background

Clothing mismatch = comparison-condition FAIL.

## Decision
- **PASS**: identity + BODY + applicable request/pose gates pass
- **TARGETED RETRY**: one or more local domains fail; retry only those domains
- **REJECT**: material identity/BODY failure or severe structural artifact

Never change YURA canon to fit a failed generation.
