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
10. `MASTER_CREATION_FLOW.md`

Do not generate before required pre-read completes.

## Mandatory execution boundary
Authority resolution and image-generation input are separate stages.

Raw Gate / QA / controller documents must not be concatenated into the image-generation payload.
The active mode must resolve exactly one permitted Execution Payload before generation.
It must also resolve a valid Execution Carrier through `../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`.

For text-only Master-Creation modes:
- `DIRECT_MODEL_INPUT` may PASS
- `CONTEXT_DERIVED_TEXT_EXECUTION` may PASS
- `EXTERNAL_RETRIEVAL_ONLY` may not PASS

Git / connector retrieval alone is not sufficient.
The active Execution Payload semantics must be carried into the generation-facing context.

## Mode routing — resolve before dependency checks
### Face-first identity creation
If the user requests creation of the YURA face anchor / face close-up before full-body Root creation:
`MODE = MASTER_CREATION`
`MASTER_CREATION_SUBMODE = TEXT_ONLY_FACE_ROOT_MASTER`

### Face-anchored full-body Root
If the user requests full-body Root generation using the approved Face Root:
`MODE = MASTER_CREATION`
`MASTER_CREATION_SUBMODE = FACE_ANCHORED_ROOT_MASTER`

### Final reference-free verification
If the user explicitly requests pure text-only full-body Root generation with no image references:
`MODE = MASTER_CREATION`
`MASTER_CREATION_SUBMODE = TEXT_ONLY_ROOT_MASTER`

Do not evaluate PRODUCTION-only requirements as blockers for these Master-Creation submodes unless that submode explicitly requires a visual reference.

## PRODUCTION
Requires:
- mandatory text Authorities resolved
- root YURA Visual Master available in declared role
- approved Face Root available as FACE_DETAIL_REFERENCE
- requested BODY orientation resolved
- required BODY view anchor available
- no unauthorized reference
- no Authority conflict
- mode-specific Execution Payload validated
- Load Receipt complete

Missing approved Face Root or required BODY view Master:
`GENERATION_ALLOWED = NO`

## MASTER_CREATION
Requires:
- explicit `MASTER_CREATION_SUBMODE`
- exact profile / execution package from `AUTHORITY_MANIFEST.md`

### TEXT_ONLY_FACE_ROOT_MASTER
Allowed now.

Authority profile:
`../generation/master-creation/TEXT_ONLY_FACE_ROOT_MASTER.md`

Execution payload:
`../execution/face-root/PAYLOAD.txt`

Run controller:
`../execution/face-root/RUN.md`

Source lock:
`../execution/face-root/SOURCE_LOCK.md`

QA:
`../qa/FACE_ROOT_QA.md`

Generation-time visual references:
`NONE`

Execution transport:
- `DIRECT_MODEL_INPUT` or `CONTEXT_DERIVED_TEXT_EXECUTION`
- exact payload semantics materialized immediately before generation
- no image reference attached
- no Gate / QA / controller / prior-generation text mixed into payload

Generated candidate is not Face Root Authority until QA PASS + explicit author approval + Git PNG / manifest registration.

### FACE_ANCHORED_ROOT_MASTER
Blocked until approved Face Root is registered and hash-locked.

Authority profile:
`../generation/master-creation/FACE_ANCHORED_ROOT_MASTER.md`

Execution payload:
`../execution/face-anchored-root/PAYLOAD.txt`

Run controller:
`../execution/face-anchored-root/RUN.md`

Source / reference lock:
`../execution/face-anchored-root/SOURCE_LOCK.md`

QA:
`../qa/FACE_ANCHORED_ROOT_QA.md`

Required generation-time visual reference:
exactly one approved `../identity/master/face-root/YURA_FACE_ROOT.png` as `FACE_DETAIL_REFERENCE`.

No other visual reference is allowed in this submode.
The actual Face Root image must be available to execution; Git existence alone is insufficient.

Face Root scope is limited to FACE / EYE / EAR / face-framing hair boundary.
It must not redesign BODY, full hair length, outfit, pose, scene, or rendering.

Until `face-anchored-root/SOURCE_LOCK.md` records the approved Face Root hash and explicitly permits generation:
`GENERATION_ALLOWED = NO`

### TEXT_ONLY_ROOT_MASTER — FINAL VERIFICATION
This route is intentionally deferred until face-first stabilization is complete.

Required before a new final TEXT_ONLY batch:
- author-approved Face Root exists and is registered
- author-approved Face-Anchored Root exists as the stabilized full-body target
- protected text Authorities represent that approved target
- current text-only `SOURCE_LOCK.md` passes after any required recompile

If any dependency is incomplete:
`TEXT_ONLY_ROOT_FINAL_VERIFICATION = DEFERRED`
`GENERATION_ALLOWED = NO`

Authority profile:
`../generation/master-creation/TEXT_ONLY_ROOT_MASTER.md`

Execution payload:
`../execution/text-only-root/PAYLOAD.txt`

Run controller:
`../execution/text-only-root/RUN.md`

Source lock:
`../execution/text-only-root/SOURCE_LOCK.md`

QA:
`../qa/ROOT_MASTER_STABILITY_QA.md`

Generation-time visual references:
`NONE`

Post-generation visual comparison reference:
`NONE`

Do not attach, inspect into generation, or describe into the payload:
- Face Root PNG
- Face-Anchored Root
- repository Root Master PNG
- prior generations

Image-generation semantic input for this submode is only the active `PAYLOAD.txt`.

### BODY_VIEW_MASTER
Blocked until:
- final Root stability status = `APPROVED`
- approved Face Root exists and is registered

## Rendering execution requirement
Every YURA Execution Payload must satisfy the mandatory compilation lock in:
`../identity/rendering/YURA_RENDERING_SPEC.md`

If the payload collapses Matte Natural Anime into washed-out high-key / uniform airbrush / invisible linework:
`EXECUTION_PAYLOAD_VALIDATION = FAIL`
`GENERATION_ALLOWED = NO`

## School uniform
When requested in an applicable production derivative, also require School Uniform Gate PASS.

## Final permission
Complete `../../gate-core/LOAD_RECEIPT_SCHEMA.md`.

For every source-locked Master-Creation route, its active SOURCE_LOCK must PASS.
A stale or unresolved lock:
`GENERATION_ALLOWED = NO`

Only `GENERATION_ALLOWED = YES` permits execution.

## POST-GENERATION ACCEPTANCE — mandatory
Every generated YURA image is `CANDIDATE ONLY` until:
1. common `../qa/GENERATION_QA.md` where applicable
2. active mode-specific QA
3. `../../gate-core/POST_GENERATION_ACCEPTANCE_PROTOCOL.md`

For Matte Natural Anime:
- photoreal / semi-photoreal / live-action / CGI / PBR / realistic portrait drift = `RENDERING HARD FAIL`
- washed-out / watercolor-like / pastel-faded / airbrush-only / linework-loss drift = `RENDERING FAIL`
- any Rendering FAIL keeps `ACCEPTANCE_ALLOWED = NO`

Generation-tool/UI visibility before QA does not invalidate the run by itself.
A failed image remains a `REJECTED CANDIDATE`; it must not be promoted or reused as protected reference.

## Retry semantics
### Text-only modes
For `TEXT_ONLY_FACE_ROOT_MASTER` and `TEXT_ONLY_ROOT_MASTER`:
- `TARGETED_RETRY = FORBIDDEN`
- failed candidate is rejected as a whole
- next run is a new independent candidate using unchanged active payload inside the batch

### Face-anchored mode
The approved Face Root remains the only identity reference.
A failed full-body candidate must never replace it.
Do not promote or feed a failed full-body candidate back as a reference.
