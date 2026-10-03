# YURA GENERATION QA

Status: **CANONICAL / CURRENT**

Evaluate domains independently. Do not average failures into one score.

## Gate 0 — Execution integrity
### PRODUCTION
PASS only if:
- YURA Generation Gate passed
- Authority Manifest exact paths were resolved
- actual required visual references were available
- required Face Root / BODY View references passed
- no unauthorized reference
- active Execution Payload was validated

### MASTER_CREATION / TEXT_ONLY_FACE_ROOT_MASTER
Use mandatory mode QA:
`FACE_ROOT_QA.md`

### MASTER_CREATION / FACE_ANCHORED_ROOT_MASTER
Use mandatory mode QA:
`FACE_ANCHORED_ROOT_QA.md`

### MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
PASS only if:
- workflow dependency for final reference-free verification passed
- submode = `TEXT_ONLY_ROOT_MASTER`
- exact `visuals/yura/execution/text-only-root/PAYLOAD.txt` was used
- `visuals/yura/execution/text-only-root/RUN.md` was controller-only
- `visuals/yura/execution/text-only-root/SOURCE_LOCK.md` matched current protected source blobs
- generation-time visual references = NONE
- post-generation comparison visual reference = NONE
- Face Root / Face-Anchored Root / repository Root Master PNG did not enter generation
- no Gate / QA / controller / retry / batch text entered generation semantics
- no per-run prompt mutation
- one person / one image / one canvas
- AI_INFERENCE_REQUIRED = NONE

## Gate 1 — Identity
PASS:
- intended YURA face impression
- blue-gray eyes
- silver-white hair
- bright fair skin

Visible wrong iris color = FAIL.

## Gate 2 — BODY
PASS:
- exact 7.25-head system
- petite/slender protected frame
- somewhat narrow shoulders
- compact ribcage
- clearly fuller chest volume relative to the petite/slender frame without widening the torso
- slim natural waist
- natural restrained pelvis / hips
- thighs / calves remain slender with visible natural softness and plausible thickness
- stable waist / pelvis / limb proportions

FAIL if the full-body silhouette becomes broad, glamour-dominant, heavy in the lower body, stick-thin, or 8+ heads tall.

## Gate 3 — FACE / EYE
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
- very small short closed mouth
- extremely subtle soft smile / calm expression
- stable eye / nose / mouth placement

## EAR QA — HARD GEOMETRY / VISIBILITY
PASS only if:
- ear scale reads slightly small
- vertical ear length is approximately 28–30% of forehead-to-chin face vertical length
- protected ear length has priority over exact endpoint alignment
- upper / lower placement values remain guides, not stretch targets
- ear long axis has restrained approximately 5–10 degree posterior tilt
- projection from the head remains restrained
- visible, partially hidden, or fully hidden ear is acceptable
- bilateral equal ear exposure is not required
- `HIDDEN != MISSING`

Immediate EAR FAIL:
- ear enlarged / lengthened for readability
- ear moved outward or rotated toward camera
- source hair length / total mass / identity changed to expose the ear
- head rotated merely to expose the ear
- both ears forced visible for symmetry
- any visibility-driven EAR or head-geometry compensation

## Gate 4 — HAIR
PASS:
- silver-white, cool-neutral / white-leaning
- principal dense mass continues through the waist into the upper-hip / hip-bone region
- main dense silhouette tapers through the upper hip
- only a small number of finest longest tips may continue toward the very upper-thigh boundary
- no dense main curtain at mid-thigh or lower
- no generic full thigh-length hair curtain
- slightly-above-standard total mass
- restrained lateral spread
- fine / soft strands
- vertical I-line tendency
- principal mass remains behind / around the back rather than mostly forward

## Gate 5 — Visibility / occlusion
`HIDDEN != MISSING`
No show-feature compensation.

## Gate 6 — RENDERING — PROTECTED DOMAIN
Required simultaneously:
- unmistakably high-quality 2D anime illustration
- Matte Natural Anime
- clean fine but **clearly readable** anime linework
- linework remains visibly present; not painterly / watercolor-faded
- soft cel / grouped illustration shading is the base
- readable grouped shadow shapes define form
- diffuse gradients are mild support only, not uniform airbrush rendering
- low-to-medium contrast, **not ultra-low contrast**
- bright presentation without overexposure
- on white background, face / skin / silver-white hair / pale clothing / linework / shading remain clearly separated
- hair reads as grouped anime masses with overlap / thickness / tonal depth
- no translucent pale fiber haze
- matte / low-gloss surface quality
- soft and calm but not washed-out / watercolor-like / pastel-faded / ethereal-faded

Material `RENDERING FAIL`:
- visibly absent or excessively faded linework
- grouped shading replaced by uniform airbrush softness
- washed-out ultra-low contrast
- white-background separation materially lost
- silver-white hair collapses into translucent haze
- watercolor / pastel-faded / ethereal-faded touch replaces Matte Natural Anime

Immediate `RENDERING HARD FAIL`:
- photoreal
- semi-photoreal
- live-action
- realistic CGI / 3D
- PBR / game-engine render
- photographic skin / hair

Any Rendering FAIL or Hard Fail:
- `ACCEPTANCE_ALLOWED = NO`
- candidate remains rejected
- never promote or reuse as protected Authority / reference

## Gate 7 — Request fidelity
Apply exact active mode-specific payload and reference policy.

## Gate 8 — Physical structure
Check limbs / joints / support / hands / feet / proportions.

## Gate 9 — Output hygiene
Check extra limbs, malformed anatomy, unintended text/logos, crop accidents.

## Validation clothing gate
PASS:
- pale / off-white plain fitted tank-style sleeveless validation top
- medium-width integrated shoulder panels, clearly wider than spaghetti straps / thin cords
- rounded scoop neckline with moderate depth
- opaque
- matte to low-gloss
- plain simple fitted shorts
- upper-thigh length
- clean waistband
- no drawstring / cord / tie / bow / lace / frill / logo / decorative trim
- no lingerie / sleepwear reading
- barefoot
- white / warm-white background

## TEXT_ONLY_ROOT_MASTER failure handling
If any protected domain FAILS:
- reject the entire candidate
- `TARGETED_RETRY = FORBIDDEN`
- do not preserve the candidate as an execution carrier
- do not promote it to Authority or future protected reference
- run a new independent full candidate with unchanged active payload inside a valid batch
- run all Gates again

Repeated systematic drift requires deliberate source / payload diagnosis outside the batch.

## Decisions
- **PASS**: all mandatory Gates pass
- **FULL_CANDIDATE_RETRY**: text-only candidate failed a protected domain; regenerate whole candidate with unchanged payload
- **TARGETED_RETRY**: only where an active route has verified preservation carriers
- **REJECT**: Rendering Fail / Hard Fail, reference-policy fail, execution-integrity fail, severe identity/BODY fail, or severe structural artifact

Never change canon to fit a failed generation.
