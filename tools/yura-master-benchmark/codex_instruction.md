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
   - Composition Authority controls canvas/placement only
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
- include the active composition constraints contained in `YURA_COMPOSITION_AUTHORITY.md`
- respect lifecycle/rule files in the sealed bundle
- state that the output is a **QA-pending Master candidate**, not an approved Master
- contain no fallback from denied sources

## Output

Return only the JSON object required by `tools/yura-master-benchmark/authority_manifest.schema.json`.

Populate it from the sealed bundle:

- `git_commit` = sealed bundle `git_commit`
- `authority_order` = exact supplied order, paths, declared roles, and SHA-256 values
- `denied_sources` = exact supplied denied-source list
- `image_reference_order` = exact supplied API image-reference order
- `compiled_prompt` = complete Image API prompt
- `errors` = empty only when `ready=true`

Do not mention unavailable shell/filesystem access as an error. Tool access is intentionally unnecessary in this benchmark mode.
