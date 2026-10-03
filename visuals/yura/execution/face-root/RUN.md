# YURA TEXT-ONLY FACE ROOT RUN CONTROLLER

Status: **PROTECTED / CONTROLLER-ONLY / MANDATORY**

This file is **NOT image-generation input**.

The image-generation model receives only:
`visuals/yura/execution/face-root/PAYLOAD.txt`

## Mode
- MODE = MASTER_CREATION
- MASTER_CREATION_SUBMODE = TEXT_ONLY_FACE_ROOT_MASTER
- REFERENCE_POLICY = NONE
- generation-time visual references = NONE
- AI_INFERENCE_REQUIRED = NONE
- USER_AUTHORIZED_VARIATION = NONE

## Execution carrier
Use `DIRECT_MODEL_INPUT` when available; otherwise `CONTEXT_DERIVED_TEXT_EXECUTION`.

For context-derived execution:
- materialize the exact semantics of `PAYLOAD.txt` immediately before the call
- no path-only shorthand
- do not mix Gate / QA / controller / retry / prior-generation text into the generation handoff

## One-run invariant
- exactly one YURA
- one face close-up
- one canvas
- one composition
- front-facing
- head vertical
- white / warm-white background
- no image reference

Invalid:
- full-body output
- multi-pose / multi-panel / comparison sheet
- multiple figures
- labels / measurements / swatches

## Payload integrity
- use current `PAYLOAD.txt` unchanged inside an active Face Root batch
- no per-run paraphrase
- no targeted mutation
- no ad-hoc ear correction wording
- no prior failed candidate as reference

## Adoption boundary
A generated Face Root is candidate only.

Adoption requires:
1. `FACE_ROOT_QA.md` PASS
2. explicit author approval
3. actual PNG placed at `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
4. `YURA_FACE_ROOT.md` created with hash and role declaration
5. Manifest / Gate revalidation

## Ear suitability
Do not modify generation semantics to force ear visibility.
If no ear is sufficiently observable for geometry verification, classify the image as valid-or-invalid by normal identity QA, but do not adopt it as the Face Root identity carrier.
