# YURA GENERATION QA

Status: **CANONICAL / CURRENT**

Evaluate domains independently. Do not average failures into one score.

## Gate 0 — Execution integrity
PASS only if:
- YURA Generation Gate passed
- Authority Manifest exact paths were loaded
- actual required visual references were available to execution
- Face Detail Reference passed for PRODUCTION
- routed BODY View Reference passed when required
- no unauthorized / derivative Identity reference was mixed
- AI_INFERENCE_REQUIRED = NONE unless the user explicitly authorized that variation scope

## Gate 1 — Identity
PASS if:
- same YURA face impression
- adult readability
- blue-gray eyes
- silver-white hair
- bright fair skin
- no unrelated character traits

Visible wrong iris color = FAIL.

## Gate 2 — BODY / view continuity
PASS if:
- 7.25-head system remains plausible
- petite/slender adult frame remains
- shoulders / ribcage / waist / pelvis relationships remain
- chest remains moderately fuller relative to frame
- limbs preserve lengths and baseline thickness
- pose has not redesigned anatomy
- projection agrees with the routed BODY view anchor

For twist / 3/4 / side:
- frontal visible area may reduce
- actual volume remains
- side depth / forward projection remains
- far-side volume may be occluded rather than exposed

FAIL if anatomy is widened, rotated or exposed merely to make it easier to see.

## Gate 3 — FACE / EYE / EAR
Check:
- soft oval face
- small rounded chin
- eye geometry
- blue-gray iris
- pupil signature when resolvable
- nose / mouth remain YURA-like
- ear attachment / scale / projection remain stable
- ear visibility follows real head angle + camera + hair occlusion

FAIL if:
- ears are enlarged or pulled outward for readability
- hair is moved aside merely to show ears
- both ears are artificially exposed for symmetry
- facial geometry changes due to pose / outfit / lighting

## Gate 4 — HAIR
Default Normal Super-Long:
- silver-white
- principal ends = waist to slightly below
- only sparse longest fine tips may approach just before upper-buttock
- total mass slightly above standard
- restrained lateral spread
- center-back mass conserved
- no unauthorized braid / bun / ornament

## Gate 5 — Visibility / occlusion integrity
PASS if hidden features remain naturally hidden when dictated by:
- camera
- pose
- hair
- clothing
- body overlap
- perspective

`HIDDEN != MISSING`

FAIL on show-feature compensation.

## Gate 6 — RENDERING
PASS if:
- clear high-quality 2D anime
- Matte Natural Anime
- restrained gloss
- low-to-medium contrast
- YURA colors preserved
- no semi-real / PBR / realistic CGI drift

## Gate 7 — Request fidelity
Check requested outfit / hairstyle / expression / pose / scene / crop / framing.

## Gate 8 — Pose / physical structure
For significant movement:
- plausible joints
- support/contact/load
- center of gravity
- perspective
- chest continuity
- hair conservation
- hands / feet / limb count
- routed body view remains consistent

## Gate 9 — Output hygiene
Check:
- extra / missing limbs
- broken hands / feet
- unintended text / logos
- duplicate props
- severe crop / occlusion accidents

## Validation clothing gate
When required:
- broad-shoulder sleeveless top
- plain shorts
- no drawstring / bow / lace / frill
- pale / opaque / matte
- barefoot
- white background

## Decision
- **PASS**: execution integrity + identity + BODY + applicable request/domain gates pass
- **TARGETED RETRY**: local domain failure; retry only that scope while references and manifests remain locked
- **REJECT**: material identity/BODY/reference failure or severe structural artifact

Never change YURA canon to fit a failed generation.
