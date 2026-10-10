# Codex instruction — YURA master benchmark — Test 6

You are compiling one deterministic YURA Master-generation request from a **sealed Authority bundle** supplied directly in this prompt.

## Execution boundary

The local Python runner has already performed all filesystem/Git verification before invoking you.

You MUST NOT:

- call shell tools
- read the filesystem
- run Git
- use MCP or other external tools
- search Git history, branches, deleted files, or unrelated files
- request missing local access
- fail merely because filesystem or shell tools are unavailable

All facts you are allowed to use are contained in the sealed bundle appended to this instruction.
Treat the bundle's `git_commit`, Authority paths, order, SHA-256 values, declared roles, denied sources, and embedded text contents as the complete input dataset for this compile step.

The bundle was produced by the runner from current local files only after verifying:

- local `HEAD == origin/main`
- required Authority paths exist
- those Authority paths have no uncommitted changes
- SHA-256 was computed locally by the runner

Do not attempt to independently re-read or re-resolve those facts.

## Authority handling

1. Process `authority_order` in exactly the order supplied by the sealed bundle.
2. Text Authority entries include their complete UTF-8 contents. Use only those contents.
3. PNG Authority entries intentionally contain metadata/role/hash only. Do not pretend to visually inspect them in this Codex step.
4. Only the PNG paths listed in the sealed bundle's `image_reference_order` will be supplied later by the runner directly to the OpenAI Image API.
5. Preserve Authority separation strictly:
   - `YURA_VISUAL_MASTER.png` = AUTHOR-SELECTED WORKING MASTER / VISUAL EDIT BASE
   - `YURA_BODY_GEOMETRY_GUIDE.png` = BODY GEOMETRY CORRECTION AUTHORITY ONLY
   - `FACE_REFERENCE_RULES.md` remains available as Face-preservation rules
   - `YURA_FACE_REFERENCE.png` is intentionally excluded from the Test 6 Authority bundle and Image API reference inputs
   - Composition Authority controls final canvas/placement only
   - Master-generation text specification supplies the active Master-generation appearance constraints
6. Do not reconstruct or infer a new Face Identity from an absent Face Reference image; preserve the Working Master's face.
7. Do not infer Face Identity from the Body Geometry Guide.
8. Do not use anything listed in `denied_sources`.
9. If the sealed text Authorities are internally contradictory, required activation status is absent where required, or bundle data is structurally incomplete, set `ready=false`, list the exact error, and do not produce a usable generation prompt.
10. Do not silently resolve conflicts. Fail closed.

## Benchmark execution split

This benchmark deliberately separates **RAW visual generation** from **final Composition normalization**.

The Image API generation step is responsible for:

- preserving the author-selected Working Master visual identity
- Body Geometry correction for the Test 6 boundary hypothesis
- active appearance constraints
- pose / full-body completeness
- white background
- one QA-pending RAW candidate

The Image API generation step is NOT responsible for satisfying the final numeric Composition targets for:

- final canvas dimensions as a prompt constraint
- final figure occupancy
- final top/bottom margin percentages
- final horizontal placement coordinates

Those final Composition targets remain authoritative in `YURA_COMPOSITION_AUTHORITY.md`, but the runner applies them later with deterministic Python post-processing **only after Body Geometry QA has explicitly passed**.

Do not copy the numeric Composition targets into `compiled_prompt`.
Do not ask the image model to stretch, shrink, lengthen, shorten, or otherwise change internal body geometry to fit final Composition.

## Prompt compilation

Compile one complete **RAW Body-Geometry-first Test 6 edit prompt** for the OpenAI Image API reference-image edit workflow.

Test 6 is derived from the frozen Test 5 benchmark state. Change only the intervention needed to test the preregistered pelvis/boundary hypothesis.

The Image API will receive exactly two reference images in this order:

1. `visuals/yura/identity/master/YURA_VISUAL_MASTER.png` — AUTHOR-SELECTED WORKING MASTER / VISUAL EDIT BASE
2. `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png` — BODY GEOMETRY CORRECTION AUTHORITY

Image 1 is the Sample 9 Working Master selected by the author. Preserve its accepted Face Identity, overall build, chest appearance, thigh feminine volume/curve, knee appearance/position, overall leg visual balance, skin appearance, general hair identity, front-view presentation, and current hair length as closely as practical.

Image 2 supplies the approved Body Geometry relationship needed for the Test 6 correction. Use it to correct the crotch/pelvis structural boundary only. Do not copy its rendering style, face, clothing, or unrelated appearance into Image 1.

`YURA_FACE_REFERENCE.png` is intentionally not included in the Test 6 sealed Authority order and is not passed to the Image API. Do not request a redesign of the Working Master's face and do not compensate for the absent Face Reference by inventing new Face Identity.

No mask is used in this test.

### Test 6 single causal intervention

The only intentional intervention is the normalized crotch/pelvis boundary lock already preregistered in `TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`.

The structural boundary is defined as:

```text
CENTRAL MEDIAL-THIGH BIFURCATION
=
UPPER / LOWER BODY STRUCTURAL BOUNDARY
```

It is NOT the waistline, shorts waistband, garment hem, visible clothing seam, navel, or hip widest point. Garment lines have no landmark authority.

The approved normalized structural anchor is:

```text
structural crown = 0%
soles            = 100%

crotch/pelvis boundary
= 53.7037% downward from structural crown within crown-to-soles body height

EQUIVALENT:
crotch-to-soles
= 46.2963% of crown-to-soles body height
```

These are relative body-geometry values, never output-canvas absolute coordinates.

Move the structural boundary toward the approved Guide position by redistributing the torso/pelvis transition. Do not solve the ratio through arbitrary leg stretching, head-size change, knee displacement, sole displacement, clothing-line manipulation, nonuniform scaling, or Composition warp.

### Frozen non-target variables

Test 6 must preserve rather than redesign:

- Working Master Face Identity
- Working Master overall build
- Working Master chest appearance
- Working Master thigh feminine volume/curve
- Working Master knee position/appearance
- Working Master overall leg visual balance
- Working Master skin appearance
- Working Master general hair identity
- Working Master current hair length
- front-view full-body presentation
- white background
- 7.2-head target and 7.1–7.3 acceptable gate
- current Body Guide
- current official Body QA definitions
- current Composition deferral

The approved later hair-length micro-refinement is NOT part of Test 6. Do not intentionally lengthen or shorten hair in this test.

The compiled prompt must:

- explicitly preserve the separation between Working Master visual identity and Body Geometry correction
- include the active character/appearance constraints contained in `YURA_VISUAL_TEXT.md` only insofar as they preserve the selected Working Master rather than redesign it
- use `YURA_COMPOSITION_AUTHORITY.md` only to preserve Authority separation and Body-Geometry precedence during RAW generation
- respect lifecycle/rule files in the sealed bundle
- state that the output is a **QA-pending Test 6 Master-refinement candidate**, not an approved final Master
- contain no fallback from denied sources
- request exactly one complete front-view full-body subject with crown and soles visible and comfortable white clearance
- avoid any final occupancy/margin optimization during generation
- treat the approved Body Geometry Guide as a measurable geometry correction Authority rather than a vague style suggestion
- preserve the Working Master everywhere except the single Test 6 boundary intervention
- retain the current 7.2-head / 7.1–7.3 Body Geometry contract
- retain the YURA-specific image-space inseam proxy range 46.0–46.5%, never 47.0% or more
- treat the approved Body Geometry Guide landmark values as relative geometry anchors, not output-canvas absolute coordinates

## Required verbatim RAW-generation block

The following lines MUST appear verbatim in `compiled_prompt`, in this order, with the same capitalization and punctuation:

```text
BODY GEOMETRY IS RESOLVED FIRST.
BODY GEOMETRY HAS PRIORITY OVER COMPOSITION.
RAW GENERATION IS BODY-GEOMETRY-FIRST.
FINAL COMPOSITION IS DEFERRED TO DETERMINISTIC POST-PROCESSING.
DO NOT OPTIMIZE FOR FINAL CANVAS OCCUPANCY OR MARGINS DURING GENERATION.
DO NOT ALTER INTERNAL BODY LANDMARK POSITIONS FOR CANVAS FITTING.
ONE HEAD IS CROWN TO CHIN.
BODY GEOMETRY EXCLUSIVELY CONTROLS FULL-BODY HEAD SCALE AND TOTAL HEAD COUNT.
CROWN TO SOLES MUST BE 7.2 HEADS.
TEST 6 USES IMAGE 1 AS THE AUTHOR-SELECTED WORKING MASTER EDIT BASE.
IMAGE 1 = YURA_VISUAL_MASTER.png — AUTHOR-SELECTED WORKING MASTER EDIT BASE.
IMAGE 2 = YURA_BODY_GEOMETRY_GUIDE.png — BODY GEOMETRY CORRECTION AUTHORITY.
PRESERVE IMAGE 1 FACE IDENTITY.
PRESERVE IMAGE 1 OVERALL BUILD.
PRESERVE IMAGE 1 CHEST APPEARANCE.
PRESERVE IMAGE 1 THIGH FEMININE VOLUME AND CURVE.
PRESERVE IMAGE 1 KNEE POSITION AND OVERALL LEG VISUAL BALANCE.
PRESERVE IMAGE 1 SKIN APPEARANCE.
PRESERVE IMAGE 1 GENERAL HAIR IDENTITY AND CURRENT HAIR LENGTH.
DO NOT INTENTIONALLY LENGTHEN OR SHORTEN HAIR IN TEST 6.
APPROVED BODY-GEOMETRY GUIDE LANDMARKS ARE FIXED RELATIVE GEOMETRY ANCHORS.
BODY GUIDE CROWN Y = 160.
BODY GUIDE CHIN Y = 340.
BODY GUIDE CROTCH Y = 856.
BODY GUIDE KNEE Y = 1156.
BODY GUIDE SOLES Y = 1456.
BODY GUIDE ONE HEAD = 180 PX.
BODY GUIDE CROWN-TO-SOLES = 7.2 HEADS.
BODY GUIDE CROWN-TO-CROTCH = 3.8667 HEADS.
BODY GUIDE CHIN-TO-CROTCH = 2.8667 HEADS.
BODY GUIDE CROTCH-TO-KNEE : KNEE-TO-SOLES = 1 : 1.
THESE BODY-GUIDE PIXEL VALUES DEFINE RELATIVE GEOMETRY ONLY; DO NOT TREAT THEM AS OUTPUT-CANVAS ABSOLUTE COORDINATES.
BODY-GEOMETRY REFERENCE SCALE OVERRIDES DEFAULT LARGE-HEAD ANIME BODY PROPORTIONS.
DO NOT ACHIEVE 7.2 BY LENGTHENING ONLY LEGS OR ONLY TORSO.
UPPER BODY MUST NOT BE VERTICALLY ELONGATED.
TORSO MUST BE COMPACT; DO NOT LENGTHEN THE RIBCAGE-TO-PELVIS OR WAIST SPAN.
CROTCH/PELVIS BOUNDARY = CENTRAL MEDIAL-THIGH BIFURCATION / UPPER-LOWER BODY STRUCTURAL BOUNDARY.
CROTCH/PELVIS BOUNDARY MUST BE AT 53.7037% OF CROWN-TO-SOLES BODY HEIGHT, MEASURED DOWNWARD FROM THE STRUCTURAL CROWN.
CROTCH-TO-SOLES MUST BE 46.2963% OF CROWN-TO-SOLES BODY HEIGHT.
THIS IS A MEASURABLE STRUCTURAL ANCHOR, NOT A QUALITATIVE AESTHETIC SUGGESTION.
GARMENT LINES HAVE NO LANDMARK AUTHORITY.
DO NOT USE THE WAISTLINE, SHORTS WAISTBAND, GARMENT HEM, NAVEL, OR HIP WIDEST POINT AS THE CROTCH/PELVIS BOUNDARY.
MOVE THE STRUCTURAL BOUNDARY BY REDISTRIBUTING THE TORSO/PELVIS TRANSITION.
DO NOT SOLVE THE TARGET BY CHANGING HEAD SIZE.
DO NOT SOLVE THE TARGET BY LENGTHENING ONLY THIGHS OR SHINS.
DO NOT MOVE THE KNEES OR SOLES MERELY TO MANIPULATE THE RATIO.
DO NOT USE NONUNIFORM BODY SCALING OR COMPOSITION WARP.
QUALITATIVE PELVIS/LOWER-BODY WORDING MUST NOT APPLY ANY ADDITIONAL OFFSET BEYOND THE APPROVED BODY-GUIDE LANDMARKS.
BODY GUIDE CROTCH/PELVIS BOUNDARY POSITION OVERRIDES QUALITATIVE DIRECTIONAL WORDING.
DO NOT RAISE THE CROTCH/PELVIS BOUNDARY ABOVE THE APPROVED BODY-GUIDE RELATIVE POSITION.
INTERPRET "SLIGHTLY HIGH PELVIS/CROTCH" AND "SUBTLY LONGER LOWER BODY" ONLY AS DESCRIPTIVE LABELS FOR THE APPROVED GUIDE GEOMETRY.
DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.
INSEAM PROXY RATIO = CROTCH-TO-SOLES / CROWN-TO-SOLES.
YURA INSEAM PROXY TARGET = 46.0–46.5%.
47.0% OR MORE IS FORBIDDEN AS TOO MODEL-LIKE.
性的な強調を目的としない
性的な魅力の増幅、性的特徴の強調、フェティッシュ化、挑発的な演出、性的な視線誘導を目的としない。本検証の目的は、キャラクターMasterの技術的な整合性・一貫性・再現性の確認のみである。
これは性的表現を目的としない、キャラクターMaster作成のためのBody Geometry検証です。
上半身前面のシルエットと体積バランスのみです。
```

The compiled prompt must also retain:

```text
7.2 heads
7.1–7.3
```

These remain Body Geometry invariants.

The approved guide landmark values above are not output-canvas coordinates. They encode the guide's internal relative geometry and must be preserved proportionally when editing the Working Master.

The qualitative pelvis/lower-body phrases remain descriptive labels only. They do not authorize an offset beyond the 53.7037% structural anchor.

Do not let neck/chest/abdomen/pelvis stack into an elongated upper body, but do not compress the upper body unnaturally merely to force a number. The intended correction is the torso/pelvis transition and structural bifurcation, while preserving the author's accepted Working Master visual balance wherever possible.

## Forbidden final-Composition literals in compiled prompt

The following final-Composition literals MUST NOT appear in `compiled_prompt`:

```text
1440 × 2560
89%
88–90%
5–6%
2278
2253
2304
CENTER AXIS X
```

They remain in the sealed Composition Authority and are applied by deterministic post-processing after Body Geometry PASS. If you include them in the Image API prompt, the benchmark separation is broken.

## Output

Return only the JSON object required by `tools/yura-master-benchmark/authority_manifest.schema.json`.

Populate it from the sealed bundle:

- `git_commit` = sealed bundle `git_commit`
- `authority_order` = exact supplied order, paths, declared roles, and SHA-256 values
- `denied_sources` = exact supplied denied-source list
- `image_reference_order` = exact supplied API image-reference order
- `compiled_prompt` = complete RAW Body-Geometry-first Test 6 edit prompt
- `errors` = empty only when `ready=true`

Do not mention unavailable shell/filesystem access as an error. Tool access is intentionally unnecessary in this benchmark mode.
