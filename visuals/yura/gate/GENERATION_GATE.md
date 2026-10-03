# YURA GENERATION GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## Required pre-read
1. `../../gate-core/GATE_PROTOCOL.md`
2. `../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`
3. `../../gate-core/AUTHORITY_SCOPE_RULES.md`
4. `../../gate-core/REFERENCE_ROLE_RULES.md`
5. `../../gate-core/VISIBILITY_OCCLUSION_PROTOCOL.md`
6. `../../gate-core/POST_GENERATION_ACCEPTANCE_PROTOCOL.md`
7. `AUTHORITY_MANIFEST.md`
8. `REFERENCE_GATE.md`
9. `VIEW_ROUTER.md`

Do not generate before required pre-read completes.

## Mandatory execution boundary
Authority resolution and image-generation input are separate stages.

Raw Gate / QA / controller documents must not be concatenated into the image-generation payload.

The active mode must resolve exactly one permitted Execution Payload before generation.

It must also resolve a valid Execution Carrier through `../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`.

For TEXT_ONLY modes:
- `DIRECT_MODEL_INPUT` may PASS
- `CONTEXT_DERIVED_TEXT_EXECUTION` may PASS
- `EXTERNAL_RETRIEVAL_ONLY` may not PASS

Git / connector retrieval alone is not sufficient.
The active Execution Payload semantics must be carried into the generation-facing context.

Do not require a direct raw-prompt API merely because the mode is TEXT_ONLY.

## Mode routing — resolve before dependency checks
If the user explicitly requests text-only generation with no image references for Root creation / Root stability validation:
`MODE = MASTER_CREATION`
`MASTER_CREATION_SUBMODE = TEXT_ONLY_ROOT_MASTER`

In that case:
- evaluate the TEXT_ONLY_ROOT_MASTER branch below
- do **not** evaluate PRODUCTION-only Master reference requirements as blockers
- PRODUCTION reference dependencies are out of scope for that request

## PRODUCTION
Requires:
- mandatory text Authorities resolved
- root YURA Visual Master available in the declared role
- dedicated Face Close-up Master available in the declared role
- requested BODY orientation resolved
- required BODY view anchor available
- no unauthorized reference
- no Authority conflict
- mode-specific Execution Payload validated
- Load Receipt complete

Missing Face Master or required non-front BODY view Master:
`GENERATION_ALLOWED = NO`

## MASTER_CREATION
Requires:
- `MASTER_CREATION_FLOW.md`
- explicit `MASTER_CREATION_SUBMODE`

### TEXT_ONLY_ROOT_MASTER
Allowed now.

Authority resolution sources:
`../generation/master-creation/TEXT_ONLY_ROOT_MASTER.md`

Mandatory execution payload:
`../execution/text-only-root/PAYLOAD.txt`

Mandatory run controller:
`../execution/text-only-root/RUN.md`

Mandatory source lock:
`../execution/text-only-root/SOURCE_LOCK.md`

Generation-time visual references:
`NONE`

Execution transport:
- `DIRECT_MODEL_INPUT` is allowed when available
- `CONTEXT_DERIVED_TEXT_EXECUTION` is allowed for the current ChatGPT-style context-derived image interface
- the actual semantics of `PAYLOAD.txt` must be materialized immediately before generation
- no generation-time image reference may be attached
- Git read / connector result without the payload semantics handoff = `EXTERNAL_RETRIEVAL_ONLY` and FAIL

Image-generation semantic input for this submode is **only**:
`../execution/text-only-root/PAYLOAD.txt`

Do not append or mix:
- `RUN.md`
- `SOURCE_LOCK.md`
- Gate text
- QA instructions
- batch size
- candidate-comparison language
- retry language
- current Root Master PNG or its description
- prior-generation discussion

Current Root Master may be used only after generation as:
`POST_GENERATION_COMPARISON_REFERENCE`

Any output containing multiple figures / panels / poses is:
`EXECUTION_RUN_INVALID`

It is not evidence of Text Authority instability.

### FACE_MASTER
Blocked until Root stability status = `APPROVED`.

### BODY_VIEW_MASTER
Blocked until:
- Root stability status = `APPROVED`
- approved Face Master exists and is registered

## School uniform
When requested in an applicable production derivative, also require School Uniform Gate PASS.

## Final permission
Complete `../../gate-core/LOAD_RECEIPT_SCHEMA.md`.

For `TEXT_ONLY_ROOT_MASTER`, `SOURCE_LOCK.md` must match the current protected source blobs.
If the source lock is stale:
`GENERATION_ALLOWED = NO`

Only `GENERATION_ALLOWED = YES` permits execution.

## POST-GENERATION ACCEPTANCE — mandatory
Every generated YURA image is `CANDIDATE ONLY` until:
1. `../qa/GENERATION_QA.md` is applied
2. applicable mode-specific QA is applied
3. `../../gate-core/POST_GENERATION_ACCEPTANCE_PROTOCOL.md` classifies the candidate

For Matte Natural Anime:
- photoreal / semi-photoreal / live-action / CGI / PBR / realistic portrait drift = `RENDERING HARD FAIL`
- Rendering Hard Fail = `ACCEPTANCE_ALLOWED = NO`

Generation-tool/UI visibility before QA does not invalidate the run by itself.
A failed image remains a `REJECTED CANDIDATE`; it must not be described as accepted, promoted to Authority, or reused as a protected reference.

Post-generation QA must not be reinterpreted as a requirement for hidden pre-presentation staging.

## TEXT-ONLY retry semantics
For `MASTER_CREATION / TEXT_ONLY_ROOT_MASTER`:
- `TARGETED_RETRY = FORBIDDEN`
- any protected-domain failure rejects the entire candidate
- regenerate a new independent whole candidate with the unchanged `PAYLOAD.txt`
- rerun all YURA QA Gates
- do not issue scope-only correction prompts inside the active batch

True targeted retry is reserved for execution routes with verified visual/pixel preservation carriers.
