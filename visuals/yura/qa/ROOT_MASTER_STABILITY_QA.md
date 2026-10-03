# YURA ROOT MASTER STABILITY QA

Status: **PROTECTED / MANDATORY FOR FINAL TEXT_ONLY_ROOT_MASTER**

Purpose:
同一の固定 `PAYLOAD.txt` から生成した独立Single Run間で、最終reference-free TEXT_ONLY再現安定性を評価する。

## Workflow precondition
Before a final TEXT_ONLY batch starts:
- protected text Authorities must represent the approved target
- current text-only `SOURCE_LOCK.md` must PASS

## Run preconditions
A valid run requires:
- mode = MASTER_CREATION
- submode = TEXT_ONLY_ROOT_MASTER
- exact `visuals/yura/execution/text-only-root/PAYLOAD.txt` used unchanged
- `RUN.md` controller-only
- `SOURCE_LOCK.md` current
- generation-time visual references = NONE
- post-generation visual comparison reference = NONE
- repository Root Master PNG not supplied to generation
- no Gate / QA / controller / retry / batch text mixed into generation semantics
- no appended per-run correction
- same framing/aspect class
- exactly one YURA / one canvas / one composition

Invalid:
- multi-panel / triptych / comparison sheet
- multiple figures / poses
- reference contamination
- payload mutation
- targeted prompt correction inside the batch
- stale `SOURCE_LOCK.md`

Invalid run does not count toward stability.

## Minimum batch
At least 3 valid independent single-image runs.
Preferred = 5.

## Evaluate every valid candidate
### FACE
- small face
- soft oval
- standard-to-slightly-short vertical length
- vertically compact; no oblong / elongated impression
- slightly narrow face width
- modest cheek softness
- smooth taper to compact lower face
- small narrow softly rounded chin
- stable feature placement

### EYE
- blue-gray only
- gray component clearly present
- restrained saturation
- mild horizontally elongated almond shape
- restrained vertical height
- stable identity

### EAR
- slightly small scale
- approximately 28–30% of forehead-to-chin face vertical length
- restrained approximately 5–10 degree posterior tilt
- restrained projection
- visible / hidden / partially hidden all acceptable
- bilateral equal exposure not required
- no visibility-driven enlargement / displacement / rotation
- stable geometry across valid runs

### BODY
- exact 7.25-head system
- petite / slender frame
- somewhat narrow shoulders
- narrow compact ribcage
- clearly fuller chest relative to frame without torso widening
- slim natural waist
- natural restrained pelvis / hips
- slender limbs with natural softness

### HAIR
- silver-white, cool-neutral / white-leaning
- principal dense mass through waist into upper-hip / hip-bone region
- clear taper through upper hip
- only sparse finest tips toward very upper-thigh boundary
- no dense mid-thigh-or-lower curtain
- stable total mass / lateral spread

### SKIN
- bright fair / slightly white-leaning
- subtle blood color
- no clipping

### RENDERING — PROTECTED STABILITY CONDITION
Required simultaneously:
- unmistakable high-quality 2D anime illustration
- Matte Natural Anime
- clean fine but clearly readable linework
- linework remains visible
- soft cel / grouped shadow shapes define form
- diffuse gradients remain mild support only
- low-to-medium contrast, not ultra-low contrast
- bright but not overexposed
- white-background separation remains clear
- silver-white hair reads as grouped anime masses, not translucent haze
- matte / low-gloss
- not watercolor-like / pastel-faded / ethereal-faded
- no photoreal / semi-real / CGI / PBR

Material rendering drift or Rendering Hard Fail candidate does not count.

### VALIDATION CLOTHING
- pale / off-white plain fitted tank-style sleeveless top
- medium-width integrated shoulder panels
- rounded scoop neckline
- pale simple fitted shorts
- clean waistband
- opaque
- matte to low-gloss
- no drawstring / cord / tie / bow / lace / frill / logo / decorative trim
- barefoot

## Cross-run classification
Per domain:
- STABLE
- MINOR_VARIANCE
- MATERIAL_VARIANCE
- SYSTEMATIC_DRIFT

## Text-only retry semantics
No scope-only retry inside a batch.

If one candidate fails:
- reject whole candidate
- keep `PAYLOAD.txt` unchanged
- generate another independent whole candidate
- re-run all QA

If the same domain repeatedly fails:
- stop batch
- diagnose payload against current protected Authorities and source lock
- revise outside batch only
- update source lock
- begin new batch

## Decisions
### PASS_FOR_AUTHOR_REVIEW
At least 3 valid runs; all core protected domains acceptably stable.

### FULL_CANDIDATE_RETRY
A candidate failed without established systematic drift.

### EXECUTION_FIX_REQUIRED
Execution isolation / source-lock / fixed-payload discipline failed.

### EXECUTION_PAYLOAD_REFINEMENT_REQUIRED
Repeated valid runs show same domain drift.

### REJECT_BATCH
Material uncontrolled variance, reference contamination, stale source lock, or repeated Rendering failure.

Only the author approves final Root stability.
