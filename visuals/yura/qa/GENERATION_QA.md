# YURA GENERATION QA

Status: **CANONICAL / CURRENT**

Evaluate domains independently. Do not average failures into one score.

## Gate 0 — Execution integrity
### PRODUCTION
PASS only if:
- YURA Generation Gate passed
- Authority Manifest exact paths were resolved
- actual required visual references were available
- required Face / BODY View references passed
- no unauthorized reference
- active Execution Payload was validated

### MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
PASS only if:
- submode = `TEXT_ONLY_ROOT_MASTER`
- exact `TEXT_ONLY_ROOT_EXECUTION.md` was used
- `TEXT_ONLY_ROOT_SINGLE_RUN.md` was followed
- generation-time visual references = NONE
- no current/previous Master image entered generation
- no per-run prompt mutation
- no batch/comparison language entered generation
- one person / one image / one canvas
- AI_INFERENCE_REQUIRED = NONE

## Gate 1 — Identity
PASS:
- intended YURA face impression
- visual age reads 15–18
- youthful but not childlike
- blue-gray eyes
- silver-white hair
- bright fair skin

Visible wrong iris color = FAIL.

## Gate 2 — BODY
PASS:
- 7.25-head system
- petite/slender protected 15–18-year-old frame
- somewhat narrow shoulders
- compact ribcage
- bust moderately fuller relative to frame
- soft hemispherical / お椀型 direction
- natural forward projection / lower fullness
- stable waist / pelvis / limb proportions

## Gate 3 — FACE / EYE / EAR
Check:
- small face
- soft oval
- face vertical length = standard to slightly short
- vertically compact; no oblong / elongated impression
- slightly narrow face width
- modest cheek softness; cheekbones not emphasized
- smooth taper toward a compact lower face
- small narrow softly rounded chin
- horizontally elongated mild-almond eyes with restrained vertical height
- visible sclera on both sides of the iris
- neutral to very slightly downturned outer corners
- blue-gray iris
- very small delicate readable nose
- very small short closed mouth; no broad default smile
- stable eye / nose / mouth placement
- small-to-standard restrained ear scale / projection
- ear visibility follows angle + hair occlusion

## Gate 4 — HAIR
PASS:
- silver-white, cool-neutral / white-leaning
- principal mass ends at waist to slightly below
- below waist mass clearly decreases
- only sparse longest fine tips may approach upper-buttock boundary
- no dense main mass at mid-buttock / thighs
- slightly-above-standard total mass
- restrained lateral spread

## Gate 5 — Visibility / occlusion
`HIDDEN != MISSING`
No show-feature compensation.

## Gate 6 — RENDERING — HARD GATE
Required:
- unmistakably high-quality 2D anime illustration
- anime facial / line / shading grammar dominant
- Matte Natural Anime
- soft cel / grouped illustration shading
- delicate visible anime line art
- restrained gloss
- low-to-medium contrast

Immediate HARD FAIL:
- photoreal
- semi-photoreal
- live-action
- realistic CGI / 3D
- PBR / game-engine render
- photographic skin / hair

Rendering Hard Fail:
- REJECT
- PRESENTATION_ALLOWED = NO

## Gate 7 — Request fidelity
For TEXT_ONLY_ROOT_MASTER:
exact fixed Execution Block compliance.

## Gate 8 — Physical structure
Check limbs / joints / support / hands / feet / proportions.

## Gate 9 — Output hygiene
Check extra limbs, malformed anatomy, unintended text/logos, crop accidents.

## Validation clothing gate
PASS:
- broad-shouldered sleeveless top
- plain simple shorts
- clean waistband
- no drawstring / bow / cord / lace / frill
- pale / opaque / matte
- barefoot
- white background

## TEXT_ONLY_ROOT_MASTER failure handling
If any protected domain FAILS:
- reject the **entire candidate**
- `TARGETED_RETRY = FORBIDDEN`
- do not issue a scope-only stochastic repair instruction
- do not preserve the candidate as an execution carrier
- run a new independent full candidate with the **same unchanged fixed Execution Block**
- run **all Gates again**

If the same failure repeats across valid isolated runs:
- classify the recurring failed domain
- revise Execution Payload / source Authority outside the active batch
- start a new batch

## Decisions
- **PASS**: all mandatory Gates pass
- **FULL_CANDIDATE_RETRY**: text-only candidate failed a protected domain; regenerate whole candidate with unchanged fixed block
- **TARGETED_RETRY**: allowed only in a mode/route with verified preservation carriers
- **REJECT**: Rendering Hard Fail, reference-policy fail, execution-integrity fail, severe identity/BODY fail, or severe structural artifact

Never change canon to fit a failed generation.
