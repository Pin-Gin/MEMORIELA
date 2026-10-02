# YURA GENERATION GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## Required pre-read
1. `../../gate-core/GATE_PROTOCOL.md`
2. `../../gate-core/AUTHORITY_SCOPE_RULES.md`
3. `../../gate-core/REFERENCE_ROLE_RULES.md`
4. `../../gate-core/VISIBILITY_OCCLUSION_PROTOCOL.md`
5. `AUTHORITY_MANIFEST.md`
6. `REFERENCE_GATE.md`
7. `VIEW_ROUTER.md`

Do not generate before all required pre-read completes.

## Base production checks
PRODUCTION requires:
- all mandatory text Authorities in `AUTHORITY_MANIFEST.md`
- root YURA Visual Master available as actual visual reference
- dedicated Face Close-up Master available as actual visual reference
- requested body orientation resolved by `VIEW_ROUTER.md`
- required BODY view anchor available
- no unauthorized reference
- no Authority conflict
- Load Receipt complete

If the dedicated Face Close-up Master has not yet been created:
`GENERATION_ALLOWED = NO` for PRODUCTION.

If a routed non-front BODY view Master has not yet been created:
`GENERATION_ALLOWED = NO` for that PRODUCTION view.

## Request routing
### Ordinary front-facing generation
- root Master = IDENTITY_ROOT_REFERENCE
- root Master also = FRONT BODY_VIEW_REFERENCE
- dedicated Face Close-up Master = FACE_DETAIL_REFERENCE

### Significant motion / torso rotation / side-oriented generation
- load `../generation/POSE_RULES.md`
- route BODY orientation through `VIEW_ROUTER.md`
- keep dedicated Face Close-up Master
- apply Visibility / Occlusion Protocol

### School uniform
Also require:
- `../../school-uniform/gate/GENERATION_GATE.md` PASS
- `../generation/profiles/SCHOOL_UNIFORM_YURA.md`

### Validation
Load:
- `../qa/VALIDATION_CLOTHING.md`
- `../qa/GENERATION_QA.md`

## Master creation mode
MASTER_CREATION requires:
- `MASTER_CREATION_FLOW.md`
- explicit `MASTER_CREATION_SUBMODE`

### TEXT_ONLY_ROOT_MASTER
Allowed now.

Required:
- `../generation/master-creation/TEXT_ONLY_ROOT_MASTER.md`
- `../qa/ROOT_MASTER_STABILITY_QA.md`

Generation-time visual references must be:
`NONE`

The current Root Master image may be used only after generation as:
`POST_GENERATION_COMPARISON_REFERENCE`

### FACE_MASTER
Blocked until:
`../identity/master/ROOT_MASTER_STABILITY_STATUS.md`
records `APPROVED`.

### BODY_VIEW_MASTER
Blocked until:
- Root Master stability status = `APPROVED`
- approved Face Master exists and is registered

Candidate output is not Authority until author approval, Git placement, manifest registration and QA.

## Final permission
Complete `../../gate-core/LOAD_RECEIPT_SCHEMA.md`.

Only:
`GENERATION_ALLOWED = YES`
permits image generation.
