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
4. The actual PNG references will be supplied later by the runner directly to the OpenAI Image API.
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

## Prompt compilation

Compile one complete prompt for the OpenAI Image API reference-image edit workflow.

The Image API will receive exactly two reference images in this order:

1. `visuals/yura/identity/face/YURA_FACE_REFERENCE.png` — FACE IDENTITY ONLY
2. `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png` — BODY GEOMETRY ONLY

The compiled prompt must:

- explicitly preserve the separation between Face Identity and Body Geometry
- include the active constraints contained in `YURA_VISUAL_TEXT.md`
- preserve the active final-composition constraints contained in `YURA_COMPOSITION_AUTHORITY.md`
- treat exact final occupancy/margins/centering as a **runner postprocess contract**, not as a reason for the Image model to change anatomy
- respect lifecycle/rule files in the sealed bundle
- state that the Image API output is a **RAW QA-pending Master candidate**, not an approved Master and not yet the final composition-normalized artifact
- contain no fallback from denied sources
- preserve the exact BODY-Geometry-before-Composition precedence defined below

## RAW generation stage

The Image API must concentrate on Face Identity, Body Geometry, silhouette, pose, rendering, and complete visibility of the subject.

The compiled prompt must tell the Image model to:

- generate the complete full body without cropping crown or soles
- keep visible white background above and below the subject so later uniform scaling is safe
- keep the subject generally centered, but do not chase exact final occupancy or exact final margin numbers
- never lengthen/shorten/warp head, neck, torso, waist position, legs, knees, ankles, or any internal body landmarks to satisfy final composition
- leave exact final 1440×2560 / 89% / 5–6% / horizontal-centering enforcement to the deterministic runner postprocess

The exact final composition numbers may appear in the compiled prompt only as a clearly identified **FINAL COMPOSITION POSTPROCESS CONTRACT — NOT A RAW BODY-GEOMETRY TARGET**.

## Required verbatim precedence and stage block

The following lines MUST appear verbatim in `compiled_prompt`, in this order, with the same capitalization and punctuation:

```text
BODY GEOMETRY IS RESOLVED FIRST.
BODY GEOMETRY HAS PRIORITY OVER COMPOSITION.
WHOLE-FIGURE UNIFORM SCALING ONLY.
DO NOT ALTER INTERNAL BODY LANDMARK POSITIONS TO SATISFY OCCUPANCY OR MARGINS.
BODY GEOMETRY WINS; COMPOSITION MAY FAIL.
RAW GENERATION MUST NOT ALTER BODY GEOMETRY TO SATISFY FINAL COMPOSITION.
FINAL COMPOSITION IS APPLIED BY DETERMINISTIC RUNNER POSTPROCESS.
POSTPROCESS MAY SCALE AND TRANSLATE THE COMPLETE RASTER ONLY.
```

The compiled prompt must also explicitly explain that:

- Body Geometry is fixed before final Composition is applied.
- The Image API is responsible for RAW subject generation, not exact final numeric placement.
- Final Composition may move and uniformly scale the already-proportioned complete raster only.
- Final Composition must never independently lengthen or shorten the head, neck, torso, waist placement, legs, knee placement, ankles, or other internal body landmark distances.
- If final numeric placement cannot be achieved without changing Body Geometry, preserve Body Geometry and allow Composition QA to fail.
- A Composition miss is preferable to deforming the approved Body Geometry.

Do not soften, paraphrase away, omit, or reverse this precedence/stage separation.

## Required numeric constraints in compiled prompt

The compiled prompt must retain all of the following literal values inside the final postprocess contract:

```text
7.2 heads
7.1–7.3
1440 × 2560
89%
88–90%
5–6%
```

These are compilation invariants. If the source Authorities do not support them, set `ready=false` instead of inventing them.

## Output

Return only the JSON object required by `tools/yura-master-benchmark/authority_manifest.schema.json`.

Populate it from the sealed bundle:

- `git_commit` = sealed bundle `git_commit`
- `authority_order` = exact supplied order, paths, declared roles, and SHA-256 values
- `denied_sources` = exact supplied denied-source list
- `image_reference_order` = exact supplied API image-reference order
- `compiled_prompt` = complete RAW Image API prompt including the postprocess-only composition contract
- `errors` = empty only when `ready=true`

Do not mention unavailable shell/filesystem access as an error. Tool access is intentionally unnecessary in this benchmark mode.
