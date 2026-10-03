# YURA ROOT MASTER STABILITY QA

Status: **PROTECTED / MANDATORY FOR TEXT_ONLY_ROOT_MASTER**

Purpose:
同一の固定 `PAYLOAD.txt` から生成した独立Single Run間で、作者承認済み完成ターゲットのTEXT_ONLY再現安定性を評価する。

## Preconditions
A valid run requires:
- mode = MASTER_CREATION
- submode = TEXT_ONLY_ROOT_MASTER
- exact `visuals/yura/execution/text-only-root/PAYLOAD.txt` used unchanged
- `visuals/yura/execution/text-only-root/RUN.md` followed as controller-only material
- `visuals/yura/execution/text-only-root/SOURCE_LOCK.md` matches current protected source blobs
- generation-time visual references = NONE
- post-generation visual comparison reference = NONE
- repository `YURA_VISUAL_MASTER.png` is not used for this target
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

Invalid run = execution-control failure and does not count toward stability.

## Minimum batch
At least 3 valid independent single-image runs.
Preferred = 5.

## Evaluate every valid candidate
### FACE
- small face
- soft oval
- face vertical length = standard to slightly short
- vertically compact; no oblong / elongated impression
- slightly narrow face width
- modest cheek softness
- smooth taper to a compact lower face
- small narrow softly rounded chin
- horizontally elongated eyes with restrained vertical height
- very small delicate nose
- very small short closed mouth
- extremely subtle soft smile / calm expression
- stable eye / nose / mouth placement

### EYE
- blue-gray only
- gray component clearly present
- restrained saturation
- mild almond shape
- horizontally elongated
- restrained vertical height
- visible sclera on both sides of iris
- neutral to very slightly downturned outer corners
- stable geometry

### EAR
- slightly small ear scale
- vertical ear length approximately 28–30% of forehead-to-chin face vertical length
- ear length has priority over exact eyebrow / nose endpoint alignment
- upper rim around eyebrow height and lower rim around nose-tip to subnasal height are guides only
- restrained approximately 5–10 degree posterior tilt
- restrained projection from the head
- visible / hidden / partially hidden ears are all acceptable
- local hair placement around the ear may vary naturally
- bilateral equal exposure is not required
- no source hair length / total-mass / identity change for ear visibility
- no head rotation, ear rotation, outward displacement or enlargement for visibility
- no forced bilateral ear visibility
- stable ear geometry without visibility-driven EAR/head compensation

### BODY
- exact 7.25-head system
- petite / slender frame
- somewhat narrow shoulders
- narrow compact ribcage
- clearly fuller chest volume relative to the frame without torso widening
- slim natural waist
- natural restrained pelvis / hips
- thighs / calves slender with visible natural softness and plausible thickness
- stable waist / pelvis / limbs

### HAIR
- silver-white, cool-neutral / white-leaning
- principal dense mass continues through the waist into the upper-hip / hip-bone region
- clear taper through the upper hip
- only a small number of sparse finest tips may continue toward the very upper-thigh boundary
- no dense main curtain at mid-thigh or lower
- no generic full thigh-length hair curtain
- stable total mass / lateral spread
- fine / soft strands
- vertical I-line tendency

### SKIN
- bright fair / slightly white-leaning
- subtle blood color
- no clipping

### RENDERING — HARD STABILITY CONDITION
- unmistakable 2D anime illustration
- Matte Natural Anime
- fine anime line
- soft cel / grouped shading
- restrained gloss
- low-to-medium contrast
- bright high-key presentation
- no photoreal / semi-real / CGI / PBR

Rendering Hard Fail candidate does not count.

### VALIDATION CLOTHING
- pale / off-white plain fitted tank-style sleeveless top
- medium-width integrated shoulder panels, clearly wider than spaghetti straps
- rounded scoop neckline with moderate depth
- pale simple fitted shorts
- clean waistband
- opaque
- matte to low-gloss
- no drawstring / cord / tie / bow / lace / frill / logo / decorative trim
- no lingerie / sleepwear reading
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
- reject that whole candidate
- keep `PAYLOAD.txt` unchanged
- generate another independent whole candidate
- re-run all QA

If the same domain repeatedly fails across otherwise valid isolated runs:
- stop the batch
- diagnose `PAYLOAD.txt` against current protected Authorities and `SOURCE_LOCK.md`
- revise outside the batch
- update `SOURCE_LOCK.md`
- begin a new batch

## Decisions
### PASS_FOR_AUTHOR_REVIEW
At least 3 valid runs; all core protected domains acceptably stable.

### FULL_CANDIDATE_RETRY
A candidate failed, but no repeated systematic drift is yet established.

### EXECUTION_FIX_REQUIRED
Execution isolation / source-lock / fixed-payload discipline failed.

### EXECUTION_PAYLOAD_REFINEMENT_REQUIRED
Repeated valid runs show the same domain drift and `PAYLOAD.txt` needs deliberate revision.

### REJECT_BATCH
Material uncontrolled variance, reference contamination, stale source lock, or repeated Rendering Hard Fail.

Only the author approves Root stability.
