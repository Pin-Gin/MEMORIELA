# YURA ROOT MASTER STABILITY QA

Status: **PROTECTED / MANDATORY FOR TEXT_ONLY_ROOT_MASTER**

Purpose:
Text Authorityからコンパイルした固定Execution Payloadを使う複数の独立Single Runについて、再現安定性を評価する。

## Preconditions
A run is valid only if:
- mode = `MASTER_CREATION`
- submode = `TEXT_ONLY_ROOT_MASTER`
- `TEXT_ONLY_ROOT_EXECUTION.md` was the execution payload
- `TEXT_ONLY_ROOT_SINGLE_RUN.md` was followed
- generation-time visual references = NONE
- same execution payload / framing class was used
- output contains exactly one YURA / one canvas / one composition

Invalid-run conditions:
- multi-panel
- triptych
- comparison sheet
- multiple YURA figures
- multiple poses in one image
- generation-time visual reference contamination
- payload modified between runs

An invalid run diagnoses **execution-control failure**.
It must not be counted as evidence of Text Authority instability.

## Minimum batch
Evaluate at least 3 **valid independent single-image runs**.
Preferred = 5.

## Domain comparison
Evaluate every valid candidate independently for:

### FACE
- soft oval adult face
- small softly rounded chin
- stable eye / nose / mouth placement
- no childlike / sharp-face drift

### EYE
- blue-gray
- restrained saturation
- stable geometry
- pupil signature when naturally resolvable

### BODY
- exact 7.25-head system
- petite / slender adult frame
- somewhat narrow shoulders
- compact ribcage
- bust moderately fuller relative to frame
- soft hemispherical / お椀型 direction
- natural forward projection and lower fullness
- waist / pelvis / limb proportions stable

### HAIR
- silver-white
- principal ends natural waist to slightly below
- only sparse longest fine tips near upper-buttock boundary
- slightly-above-standard total mass
- restrained lateral spread
- back mass conserved

### SKIN
- bright fair
- slightly white-leaning
- subtle natural blood color
- no clipping

### RENDERING — HARD STABILITY CONDITION
- unmistakably high-quality 2D anime illustration
- anime facial / line / shading grammar dominant
- Matte Natural Anime
- fine low-contrast anime line
- soft cel + grouped illustration shading
- low-to-medium contrast
- restrained gloss
- no photoreal / semi-photoreal / live-action / CGI / PBR reading

Any realism-mode violation = RENDERING HARD FAIL.
A Rendering Hard Fail candidate does not count as a valid stable candidate.

### VALIDATION CLOTHING
- broad-shouldered pale opaque sleeveless top
- pale opaque simple shorts
- clean waistband
- barefoot

## Cross-run classification
Per protected domain:
- STABLE
- MINOR_VARIANCE
- MATERIAL_VARIANCE
- SYSTEMATIC_DRIFT

## Systematic drift rule
Repeated same-direction failure across **valid runs** may indicate:
- execution payload defect
- source Text Authority ambiguity
- model interpretation issue

Diagnose in that order:
1. execution payload / orchestration
2. rendering / composition leakage
3. domain text ambiguity

Do not change canon to fit failed generations.

## Post-generation Root Master comparison
After generation only, the registered Root Master may be used as:
`POST_GENERATION_COMPARISON_REFERENCE`

It must not have entered generation.

## Decision
### PASS_FOR_AUTHOR_REVIEW
All core domains acceptably stable across valid runs.

### EXECUTION_FIX_REQUIRED
Runs were contaminated by multi-panel / multi-figure / payload / reference-control failure.

### TEXT_REFINEMENT_REQUIRED
Valid isolated runs still show repeated systematic drift traceable to text semantics.

### BATCH_RETRY_REQUIRED
One-off structural artifacts prevent enough valid comparisons.

### REJECT_BATCH
Material uncontrolled variance, reference contamination, or repeated Rendering Hard Fail invalidates the batch.

### RENDERING_HARD_FAIL
Reject the individual candidate immediately. Do not present it as a completed result and do not count it toward the minimum valid batch.

Only the author can approve Root stability.
