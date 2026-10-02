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

Raw Gate / QA documents must not be concatenated into the image-generation payload.

The active mode must resolve exactly one permitted Execution Payload before generation.

It must also resolve a valid Execution Carrier through `../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`.

`AUTHORITY_RESOLVED = YES` does not imply `PAYLOAD_DELIVERED_TO_IMAGE_GENERATION = YES`.

Git / connector retrieval alone is not a valid carrier.
If the protected payload semantics are not present in the actual generation-facing carrier:
`GENERATION_ALLOWED = NO`

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
`../generation/execution/TEXT_ONLY_ROOT_EXECUTION.md`

Mandatory single-run controller:
`../generation/execution/TEXT_ONLY_ROOT_SINGLE_RUN.md`

Generation-time visual references:
`NONE`

Execution transport:
- if a direct model-facing prompt carrier exists, use the fixed Execution Block through it
- if the image tool derives instructions from conversation context, use `CONVERSATION_CONTEXT_CARRIER`
- in conversation-context mode, the fixed `TEXT_ONLY_ROOT_EXECUTION.md` generation block must be materialized immediately before generation
- a Git read / connector result without semantic handoff is `EXTERNAL_RETRIEVAL_ONLY` and FAIL

The image-generation call must receive only the single-run execution semantics, not:
- batch size
- QA instructions
- Gate instructions
- candidate-comparison language
- current Root Master PNG

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

Only `GENERATION_ALLOWED = YES` permits execution.


## POST-GENERATION ACCEPTANCE — mandatory
Every generated YURA image is `CANDIDATE ONLY` until:
1. `../qa/GENERATION_QA.md` is applied
2. applicable mode-specific QA is applied
3. `../../gate-core/POST_GENERATION_ACCEPTANCE_PROTOCOL.md` passes

For Matte Natural Anime:
- photoreal / semi-photoreal / live-action / CGI / PBR / realistic portrait drift = `RENDERING HARD FAIL`
- Rendering Hard Fail = `PRESENTATION_ALLOWED = NO`

Do not present a failed rendering as the completed generation result.


## TEXT-ONLY retry semantics
For `MASTER_CREATION / TEXT_ONLY_ROOT_MASTER`:
- `TARGETED_RETRY = FORBIDDEN`
- any protected-domain failure rejects the entire candidate
- regenerate a new independent whole candidate with the unchanged fixed Execution Block
- rerun all YURA QA Gates
- do not issue scope-only correction prompts inside the active batch

True targeted retry is reserved for execution routes with verified visual/pixel preservation carriers.
