# YURA GENERATION GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## Required pre-read
1. `../../gate-core/GATE_PROTOCOL.md`
2. `../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`
3. `../../gate-core/AUTHORITY_SCOPE_RULES.md`
4. `../../gate-core/REFERENCE_ROLE_RULES.md`
5. `../../gate-core/VISIBILITY_OCCLUSION_PROTOCOL.md`
6. `AUTHORITY_MANIFEST.md`
7. `REFERENCE_GATE.md`
8. `VIEW_ROUTER.md`

Do not generate before required pre-read completes.

## Mandatory execution boundary
Authority resolution and image-generation input are separate stages.

Raw Gate / QA documents must not be concatenated into the image-generation payload.

The active mode must resolve exactly one permitted Execution Payload before generation.

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
