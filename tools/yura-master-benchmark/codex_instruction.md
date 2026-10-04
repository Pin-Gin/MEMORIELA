# Codex instruction — YURA master benchmark

You are preparing one deterministic YURA master-generation request.

## Hard requirements

1. Resolve and report the current `git rev-parse HEAD`.
2. Read only the Authority files listed in `tools/yura-master-benchmark/config.json`, and read them in exactly that order.
3. Do not read Git history, old branches, deleted files, `characters/YURA.md`, `story/**`, `manuscript/**`, Memory, or unrelated YURA generations.
4. For PNG Authority files, record SHA-256 and their declared Authority role. Do not infer full-body geometry from the face reference crop. Do not infer face identity from the body geometry guide.
5. If any required Authority file is missing, contradictory, or not ACTIVE where activation is required, set `ready=false`, list the error, and do not create a usable generation prompt.
6. Do not modify the repository.

## Prompt compilation

Compile one prompt for the OpenAI Image API reference-image edit workflow.

The image request will pass exactly two reference images in this order:

1. `visuals/yura/identity/face/YURA_FACE_REFERENCE.png` — FACE IDENTITY ONLY
2. `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png` — BODY GEOMETRY ONLY

The compiled prompt must explicitly preserve this separation and must include the active text constraints from:

- `YURA_VISUAL_TEXT.md` — current Master-generation API visual specification
- `YURA_COMPOSITION_AUTHORITY.md` — production canvas/composition constraints for this Master candidate

The prompt must state that the result is a QA-pending Master candidate, not an approved Master.

Do not silently resolve conflicts. Fail closed.

## Output

Return only the JSON object required by `tools/yura-master-benchmark/authority_manifest.schema.json`.

`authority_order` must reveal the exact read order and SHA-256 of every required Authority file.
`image_reference_order` must contain the two reference-image paths in exact API order.
`compiled_prompt` must be the complete text that can be passed directly to the Image API.
