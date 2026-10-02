# YURA GENERATION QA

Status: **CANONICAL / CURRENT**

Evaluate domains independently. Do not average failures into one score.

## Gate 0 — Execution integrity
### PRODUCTION
PASS only if:
- YURA Generation Gate passed
- Authority Manifest exact paths were loaded
- actual required visual references were available to execution
- Face Detail Reference passed
- routed BODY View Reference passed when required
- no unauthorized / derivative Identity reference was mixed
- AI_INFERENCE_REQUIRED = NONE unless the user explicitly authorized that variation scope

### MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
PASS only if:
- YURA Generation Gate passed
- `MASTER_CREATION_SUBMODE = TEXT_ONLY_ROOT_MASTER`
- `TEXT_ONLY_ROOT_MASTER.md` exact profile was loaded
- generation-time visual references = NONE
- ACTUAL_VISUAL_REFERENCES_AVAILABLE = NOT_REQUIRED
- no previous/current Master image entered the generation call
- AI_INFERENCE_REQUIRED = NONE
- USER_AUTHORIZED_VARIATION = NONE

The current Root Master may be used only after generation as a comparison reference.

## Gate 1 — Identity
PASS if:
- same intended YURA face impression
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

For PRODUCTION non-front views:
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

## Gate 6 — RENDERING — HARD GATE

Required PASS:
- unmistakably high-quality **2D anime illustration**
- anime facial / line / shading grammar remains dominant
- Matte Natural Anime
- soft cel / grouped illustration shading
- delicate visible line art
- restrained gloss
- low-to-medium contrast
- YURA colors preserved
- no semi-real / photoreal / live-action / CGI / PBR drift

Immediate **RENDERING HARD FAIL**:
- output reads primarily as a real human portrait
- semi-photoreal portrait rendering
- live-action appearance
- realistic CGI / 3D render
- game-engine / PBR rendering
- photographic skin
- photographic hair fibers
- realistic portrait facial modeling overriding anime facial grammar

`matte / low gloss` alone is NOT sufficient.

If any Rendering Hard Fail is present:
- `REJECT`
- `PRESENTATION_ALLOWED = NO`
- do not expose the candidate as a completed/accepted generation

## Gate 7 — Request fidelity
Check requested outfit / hairstyle / expression / pose / scene / crop / framing.

For TEXT_ONLY_ROOT_MASTER, request fidelity means exact compliance with the fixed Master Creation profile.

## Gate 8 — Pose / physical structure
For significant movement:
- plausible joints
- support/contact/load
- center of gravity
- perspective
- chest continuity
- hair conservation
- hands / feet / limb count
- routed body view remains consistent where applicable

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

## Text-only stability route
For `TEXT_ONLY_ROOT_MASTER`, also run:
`ROOT_MASTER_STABILITY_QA.md`

A single good-looking candidate is not stability evidence.

## Decision
- **PASS**: execution integrity + identity + BODY + applicable request/domain gates pass
- **TARGETED RETRY**: local domain failure; retry only that scope while text inputs remain locked
- **REJECT**: material identity/BODY/reference-policy failure, **RENDERING HARD FAIL**, execution-integrity failure, or severe structural artifact

Never change YURA canon to fit a failed generation.
