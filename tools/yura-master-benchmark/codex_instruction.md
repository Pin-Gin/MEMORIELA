# Codex instruction — YURA master benchmark

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
   - `YURA_FACE_REFERENCE.png` = FACE IDENTITY ONLY
   - `YURA_BODY_GEOMETRY_GUIDE.png` = BODY GEOMETRY ONLY
   - Composition Authority controls final canvas/placement only
   - Master-generation text specification supplies the active Master-generation appearance constraints
6. Do not infer full-body geometry from the face reference.
7. Do not infer face identity from the body geometry guide.
8. Do not use anything listed in `denied_sources`.
9. If the sealed text Authorities are internally contradictory, required activation status is absent where required, or bundle data is structurally incomplete, set `ready=false`, list the exact error, and do not produce a usable generation prompt.
10. Do not silently resolve conflicts. Fail closed.

## Benchmark execution split

This benchmark deliberately separates **RAW visual generation** from **final Composition normalization**.

The Image API generation step is responsible for:

- Face Identity
- Body Geometry
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

Compile one complete **RAW Body-Geometry-first** prompt for the OpenAI Image API reference-image edit workflow.

This run is Test 4 — diagnose whether reference-image order changes Body Geometry adherence by using the Body Geometry Guide as Image 1 / edit base while keeping the Face Reference as Image 2 / Face Identity only.

The Image API will receive exactly two reference images in this order:

1. `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png` — BODY GEOMETRY EDIT BASE
2. `visuals/yura/identity/face/YURA_FACE_REFERENCE.png` — FACE IDENTITY ONLY

Image 1 must be treated as the structural full-body edit base, not merely as a loose visual suggestion. Preserve its relative Body Geometry and vertical landmark layout while rendering the active YURA Master appearance.

Image 2 supplies Face Identity only. Do not transfer Image 2 crop, canvas occupancy, apparent head size, or reference-image scale into full-body geometry. Do not reinterpret or rescale Image 1 Body Geometry to match Image 2.

This Test 4 changes reference-image order/role only. No mask is used in this test.

The compiled prompt must:

- explicitly preserve the separation between Face Identity and Body Geometry
- include the active character/appearance constraints contained in `YURA_VISUAL_TEXT.md`
- use `YURA_COMPOSITION_AUTHORITY.md` only to preserve Authority separation and Body-Geometry precedence during RAW generation
- respect lifecycle/rule files in the sealed bundle
- state that the output is a **QA-pending RAW Master candidate**, not an approved Master
- contain no fallback from denied sources
- request exactly one complete front-view full-body subject with crown and soles visible and comfortable white clearance
- avoid any final occupancy/margin optimization during generation
- treat the approved Body Geometry Guide as a measurable geometry reference rather than a vague style suggestion
- preserve a compact torso, slightly high pelvis/crotch, and subtly longer lower body within the approved 7.2-head geometry
- target the YURA-specific image-space inseam proxy range 46.0–46.5%, never 47.0% or more
- treat the approved Body Geometry Guide landmark values as fixed relative geometry anchors, not output-canvas absolute coordinates
- treat Image 1 as the Body-Geometry edit base and Image 2 as Face Identity only

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
FACE REFERENCE DEFINES FACIAL IDENTITY AND FACE-LOCAL GEOMETRY ONLY.
FACE REFERENCE DOES NOT DEFINE HEAD-TO-BODY SCALE.
FACE REFERENCE DOES NOT DEFINE HEAD VERTICAL SIZE FOR FULL-BODY PROPORTION.
FACE REFERENCE DOES NOT DEFINE TOTAL HEAD COUNT.
FACE REFERENCE DOES NOT DEFINE BODY PROPORTIONS.
DO NOT INFER BODY PROPORTION FROM FACE REFERENCE CROP OR SCALE.
DO NOT USE FACE REFERENCE CANVAS OCCUPANCY AS BODY GEOMETRY.
FACE_REFERENCE -> BODY_PROPORTION = DENIED
FACE_REFERENCE -> FULL_BODY_SCALE = DENIED
FACE_REFERENCE -> CANVAS_OCCUPANCY = DENIED
BODY GEOMETRY EXCLUSIVELY CONTROLS FULL-BODY HEAD SCALE AND TOTAL HEAD COUNT.
CROWN TO SOLES MUST BE 7.2 HEADS.
TEST 4 USES IMAGE 1 AS THE BODY-GEOMETRY EDIT BASE.
IMAGE 1 = YURA_BODY_GEOMETRY_GUIDE.png — BODY GEOMETRY EDIT BASE.
IMAGE 2 = YURA_FACE_REFERENCE.png — FACE IDENTITY ONLY.
PRESERVE IMAGE 1 RELATIVE BODY-LANDMARK LAYOUT.
USE IMAGE 2 FOR FACE IDENTITY ONLY.
DO NOT RESCALE IMAGE 1 BODY GEOMETRY TO MATCH IMAGE 2.
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
FACE REFERENCE PRESERVES FACE IDENTITY ONLY; BODY GEOMETRY GUIDE CONTROLS FULL-BODY HEAD SCALE AND INTERNAL BODY LANDMARK PLACEMENT.
BODY-GEOMETRY REFERENCE SCALE OVERRIDES DEFAULT LARGE-HEAD ANIME BODY PROPORTIONS.
DO NOT ACHIEVE 7.2 BY LENGTHENING ONLY LEGS OR ONLY TORSO.
UPPER BODY MUST NOT BE VERTICALLY ELONGATED.
TORSO MUST BE COMPACT; DO NOT LENGTHEN THE RIBCAGE-TO-PELVIS OR WAIST SPAN.
KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.
LOW SITTING-HEIGHT IMPRESSION = RELATIVELY COMPACT UPPER-BODY SPAN + SLIGHTLY LONGER LOWER BODY.
DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.
INSEAM PROXY RATIO = CROTCH-TO-SOLES / CROWN-TO-SOLES.
YURA INSEAM PROXY TARGET = 46.0–46.5%.
47.0% OR MORE IS FORBIDDEN AS TOO MODEL-LIKE.
性的な強調を目的としない
これは性的表現を目的としない、キャラクターMaster作成のためのBody Geometry検証です。
上半身前面のシルエットと体積バランスのみです。
```

The compiled prompt must also retain:

```text
7.2 heads
7.1–7.3
```

These are Body Geometry invariants.

The approved guide landmark values above are not output-canvas coordinates. They encode the guide's internal relative geometry and must be preserved proportionally when generating the RAW candidate.

The phrases above are not permission to redesign the body independently from the active Body Geometry Guide. They clarify the approved internal-balance intent:

- do not let neck/chest/abdomen/pelvis stack into an elongated upper body
- keep the ribcage-to-waist-to-pelvis torso span compact
- do not let the waist read unnaturally low
- keep pelvis/crotch slightly high in the standing full-body silhouette
- let the lower body read subtly longer, not exaggeratedly model-like
- keep knee placement natural
- do not solve the preference by stretching only thighs, shins, or total leg length
- do not compress the ribcage/abdomen unnaturally merely to shorten the upper body
- interpret the inseam proxy only as the YURA-specific image-space QA proxy defined by the active Body Geometry Authority

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
- `compiled_prompt` = complete RAW Body-Geometry-first Image API prompt
- `errors` = empty only when `ready=true`

Do not mention unavailable shell/filesystem access as an error. Tool access is intentionally unnecessary in this benchmark mode.
