# YURA ROOT MASTER STABILITY QA

Status: **PROTECTED / MANDATORY FOR TEXT_ONLY_ROOT_MASTER**

Purpose:
Text Authorityのみで生成した複数候補の再現安定性を評価する。

This QA measures:
- agreement with protected text authority
- cross-run variance
- systematic drift

It does not select a candidate by aesthetic preference alone.

## Preconditions
PASS only if:
- mode = `MASTER_CREATION`
- submode = `TEXT_ONLY_ROOT_MASTER`
- `TEXT_ONLY_ROOT_MASTER.md` fixed profile was loaded
- generation-time visual references = `NONE`
- same generation conditions were maintained across the batch
- minimum 3 independent candidates exist

If an image reference was supplied during generation:
`STABILITY_BATCH = INVALID`

## Domain comparison
Evaluate every candidate independently for:

### FACE
- soft oval adult face
- small softly rounded chin
- adult-balanced eye geometry
- nose / mouth placement and scale
- no childlike / sharp-face drift

### EYE
- blue-gray
- restrained saturation
- protected geometry
- pupil signature when resolvable

### BODY
- exact 7.25-head design target remains plausible
- petite / slender adult frame
- shoulder width
- compact ribcage
- bust volume / forward projection
- waist
- pelvis / hips
- limb length / baseline thickness

### HAIR
- silver-white
- Normal Super-Long
- principal ends at natural waist to slightly below
- sparse longest tips only near upper-buttock limit
- slightly-above-standard mass
- restrained lateral spread
- center/back mass not deleted

### SKIN
- bright fair
- slightly white-leaning
- subtle natural blood color
- no strong pink/orange drift
- no white clipping

### RENDERING
- Matte Natural Anime
- fine clean line
- soft cel + diffuse shading
- low-to-medium contrast
- restrained gloss
- no semi-real / PBR drift

### COMPOSITION
- one YURA
- front-facing full body
- centered
- validation clothing
- barefoot
- white background
- minimal perspective

## Cross-run variance
Compare candidates against each other.

Record whether each protected domain is:
- STABLE
- MINOR_VARIANCE
- MATERIAL_VARIANCE
- SYSTEMATIC_DRIFT

Material variance includes meaningful changes in:
- face identity
- eye shape/color
- head/body ratio
- shoulder/ribcage/body proportions
- bust volume
- pelvis/limb scale
- principal hair length/mass
- skin identity
- rendering grammar

## Systematic drift rule
If the same error appears repeatedly across candidates, treat it as a likely text-authority or model-interpretation problem.

Do not:
- average candidates into a new canon
- pick one accidental success and ignore repeated failures
- rewrite canon to fit the batch

Identify the exact controlling text domain first.

## Current Root Master comparison
After generation only, the registered Root Master may be used as a secondary comparison reference.

Role:
`POST_GENERATION_COMPARISON_REFERENCE`

It must not have been supplied during generation.

Use it to detect loss of intended identity, not to override precise protected text rules.

## Stability decision
### PASS_FOR_AUTHOR_REVIEW
- no material systematic drift
- protected domains remain acceptably stable across the batch
- each candidate satisfies core identity/body/rendering requirements

### TEXT_REFINEMENT_REQUIRED
- repeated systematic drift points to insufficient / ambiguous text authority

### BATCH_RETRY_REQUIRED
- one-off structural generation failures prevent a valid comparison but text itself is not implicated

### REJECT_BATCH
- reference contamination
- changed conditions inside the batch
- material uncontrolled identity variance

Only the author can approve the Root Master and change stability status to APPROVED.
