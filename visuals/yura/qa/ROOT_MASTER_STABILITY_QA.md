# YURA ROOT MASTER STABILITY QA

Status: **PROTECTED / MANDATORY FOR TEXT_ONLY_ROOT_MASTER**

Purpose:
同一の短い固定Execution Blockから生成した独立Single Run間で、YURAの再現安定性を評価する。

## Preconditions
A valid run requires:
- mode = MASTER_CREATION
- submode = TEXT_ONLY_ROOT_MASTER
- exact `TEXT_ONLY_ROOT_EXECUTION.md` used unchanged
- `TEXT_ONLY_ROOT_SINGLE_RUN.md` followed
- generation-time visual references = NONE
- no appended per-run correction
- same framing/aspect class
- exactly one YURA / one canvas / one composition

Invalid:
- multi-panel / triptych / comparison sheet
- multiple figures / poses
- reference contamination
- Execution Block mutation
- targeted prompt correction inside the batch

Invalid run = execution-control failure and does not count toward stability.

## Minimum batch
At least 3 valid independent single-image runs.
Preferred = 5.

## Evaluate every valid candidate
### FACE
- visual age reads 15–18; youthful but not childlike
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
- very small short closed mouth with neutral to extremely subtle soft expression
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
- no source hair length / total-mass / identity change for ear visibility
- no head rotation, ear rotation, outward displacement or enlargement for visibility
- no forced bilateral ear visibility
- stable ear geometry without visibility-driven EAR/head compensation

### BODY
- exact 7.25-head system
- petite / slender frame
- narrow compact ribcage
- bust moderately fuller relative to frame
- soft hemispherical / お椀型
- stable waist / pelvis / limbs

### HAIR
- silver-white, cool-neutral / white-leaning
- principal ends waist to slightly below
- clear mass reduction below waist
- only sparse finest tips near upper-buttock limit
- no dense main mass at mid-buttock / thighs
- stable total mass / lateral spread

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
- no photoreal / semi-real / CGI / PBR

Rendering Hard Fail candidate does not count.

### VALIDATION CLOTHING
- broad-shouldered pale sleeveless top
- pale simple shorts
- clean waistband
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
- keep fixed block unchanged
- generate another independent whole candidate
- re-run all QA

If the same domain repeatedly fails across otherwise valid isolated runs:
- stop the batch
- diagnose Execution Block first
- revise outside the batch
- begin a new batch

## Decisions
### PASS_FOR_AUTHOR_REVIEW
At least 3 valid runs; all core protected domains acceptably stable.

### FULL_CANDIDATE_RETRY
A candidate failed, but no repeated systematic drift is yet established.

### EXECUTION_FIX_REQUIRED
Execution isolation / fixed-block discipline failed.

### EXECUTION_PAYLOAD_REFINEMENT_REQUIRED
Repeated valid runs show the same domain drift and the fixed block needs revision.

### REJECT_BATCH
Material uncontrolled variance, reference contamination, or repeated Rendering Hard Fail.

Only the author approves Root stability.
