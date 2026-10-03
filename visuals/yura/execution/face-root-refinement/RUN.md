# YURA FACE ROOT GEOMETRY REFINEMENT RUN CONTROLLER

Status: **PROTECTED / CONTROLLER-ONLY / MANDATORY**

This file is **NOT image-generation input**.

The image-edit execution receives only:
- `visuals/yura/execution/face-root-refinement/PAYLOAD.txt`
- exactly one eligible runtime image as `EDIT_SOURCE_CARRIER`

## Mode
- MODE = MASTER_CREATION
- MASTER_CREATION_SUBMODE = FACE_ROOT_GEOMETRY_REFINEMENT
- REFERENCE_POLICY = NONE
- all visual Reference roles = NONE
- EDIT_SOURCE_POLICY = EXACTLY_ONE_ELIGIBLE_CANDIDATE
- AI_INFERENCE_REQUIRED = NONE beyond the fixed payload and edit operation

## Eligibility gate
Before execution, the supplied candidate must have active `FACE_ROOT_QA.md` classification:
`REFINEMENT_ELIGIBLE`

Required prior QA state:
- FACE = PASS
- EYE = PASS
- HAIR FRAMING = PASS
- SKIN = PASS
- RENDERING = PASS
- composition / single-image constraints = PASS
- at least one ear observable
- EAR geometry = FAIL
- no other protected-domain FAIL

If any required eligibility condition is missing:
`GENERATION_ALLOWED = NO`

## Edit-source boundary
The supplied image is `EDIT_SOURCE_CARRIER` only.

It is:
- NOT Authority
- NOT Identity Reference
- NOT Production Reference
- NOT Canon evidence

Record its exact runtime SHA-256 in the Load Receipt before execution.
The actual image must be available to the image-edit operation.
Git existence is not relevant to this runtime carrier.

No other image may be supplied.
No prior Face Root, Root Master, prior failed refinement, or unrelated image may be added.

## Execution carrier
Use an image-edit capable execution route.

Generation-facing inputs must be limited to:
1. exact active refinement `PAYLOAD.txt`
2. exact eligible `EDIT_SOURCE_CARRIER` image

Do not mix Gate / QA / controller / source-lock / retry prose into image-generation semantics.

## One-run invariant
- exactly one YURA
- one face close-up
- one canvas
- one composition
- front-facing
- head vertical
- white / warm-white background
- one edited output image

Invalid:
- comparison sheet
- before / after side-by-side
- multiple figures
- labels / measurements / swatches

## Preservation boundary
The payload requests local preservation of already-passing non-EAR content.
The controller does not claim such preservation is guaranteed.

The edit output is always a new candidate.
All protected Face Root domains must be re-QA'd by `FACE_ROOT_REFINEMENT_QA.md`.

## Payload integrity
- use current refinement `PAYLOAD.txt` unchanged within the active refinement batch
- no per-run paraphrase
- no ad-hoc additional ear correction wording
- no hidden prompt mutation based on the previous edit result

## Retry boundary
If a refinement output FAILS:
- reject that output
- do not promote it
- do not use it as the next edit source

If another run is explicitly allowed:
- return to the same originally eligible `EDIT_SOURCE_CARRIER`
- use unchanged active `PAYLOAD.txt`
- run full QA again

## Adoption boundary
A passing refinement output is still candidate-only.

Adoption requires:
1. `FACE_ROOT_REFINEMENT_QA.md` PASS
2. explicit author approval
3. actual PNG placed at `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
4. `YURA_FACE_ROOT.md` created with hash and role declaration
5. Manifest / Gate revalidation
