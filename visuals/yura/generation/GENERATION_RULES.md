# YURA GENERATION RULES

Status: **CANONICAL / MANDATORY OPERATIONAL RULES**

Authority paths / Reference roles are resolved by the active Gate and Manifest.

## Execution separation
Do not send the entire Authority set to the image-generation model.

Follow:
`../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`

The active mode must resolve one mode-specific Execution Payload.

## One-person / one-image invariant
Unless the user explicitly requests a multi-character composition:
- exactly one YURA
- one canvas
- one composition
- one image
- no character sheet
- no multi-pose sheet
- no automatic front+side+back layout
- no comparison sheet / triptych

Multiple requested outputs = multiple independent single-image calls.

## Identity lock
Always preserve:
- 153 cm concept
- exact 7.25-head BODY
- YURA face
- protected EAR geometry / placement / visibility behavior
- blue-gray eyes
- silver-white hair
- default Normal Super-Long unless explicitly changed
- protected SKIN
- project-wide rendering through the YURA rendering adapter

## No AI reinterpretation
Do not:
- replace protected identity with generic anime defaults
- redesign for beauty / readability
- average protected traits
- invent unspecified identity changes

`UNSPECIFIED != PERMISSION TO INVENT`

## Ear visibility lock
Ear visibility must follow the protected EAR Authority and natural occlusion.

Do not:
- enlarge / lengthen the ear for readability
- move or rotate the ear to expose it
- rotate the head merely to show the ear
- force both ears visible

Local hair placement around the ear may vary naturally and may make the ear more or less visible.
Do not change source hair length / total mass / identity for ear visibility.
A naturally visible, partially hidden, or fully hidden ear is valid.
`HIDDEN != MISSING`

## Rendering compilation lock
Every YURA execution payload must implement the mandatory rendering block in:
`../identity/rendering/YURA_RENDERING_SPEC.md`

Do not collapse the rendering meaning into only:
- high-key
- soft
- low contrast
- matte

Required protected touch includes:
- visible fine 2D anime linework
- grouped soft-cel shadow shapes
- mild diffuse gradients as support only
- low-to-medium, not ultra-low, contrast
- white-background separation
- grouped anime hair masses
- no washed-out / watercolor / pastel-faded / ethereal-faded drift

## TEXT_ONLY_FACE_ROOT_MASTER
Resolution:
`master-creation/TEXT_ONLY_FACE_ROOT_MASTER.md`

Execution:
`../execution/face-root/PAYLOAD.txt`

Generation-time image references = NONE.
Edit source carrier = NONE.

Purpose:
Create the Face Root identity candidate before full-body Root generation.

The candidate must be classified by `../qa/FACE_ROOT_QA.md`.

Possible outcomes:
- `PASS_FOR_AUTHOR_REVIEW`
- `REFINEMENT_ELIGIBLE`
- `REJECTED_CANDIDATE`

Only `PASS_FOR_AUTHOR_REVIEW` may proceed directly to author approval.
`REFINEMENT_ELIGIBLE` remains rejected for adoption and may only enter the protected refinement route below.

## FACE_ROOT_GEOMETRY_REFINEMENT
Resolution:
`master-creation/FACE_ROOT_GEOMETRY_REFINEMENT.md`

Execution:
`../execution/face-root-refinement/PAYLOAD.txt`

Run controller:
`../execution/face-root-refinement/RUN.md`

Source lock:
`../execution/face-root-refinement/SOURCE_LOCK.md`

Required non-reference image input:
exactly one `REFINEMENT_ELIGIBLE` Face Root candidate as `EDIT_SOURCE_CARRIER`.

All Reference roles remain `NONE`.

The edit-source image:
- is not Authority
- is not an Identity / Production Reference
- is not Canon evidence
- supplies only the existing pixel / layout starting state for correction of that same candidate

Use this route only when EAR geometry is the sole protected-domain failure and at least one ear is observable.
Do not use it to rescue rendering, FACE, EYE, HAIR, SKIN, or composition failures.
Do not use it merely to expose a naturally hidden ear.

The edit request may ask to preserve non-EAR content, but do not claim preservation is guaranteed.
Every refinement output is a new candidate and must pass `../qa/FACE_ROOT_REFINEMENT_QA.md` across all protected Face Root domains.

A failed refinement output must not become the next edit source.
If another refinement attempt is authorized, restart from the same originally eligible `EDIT_SOURCE_CARRIER` with the unchanged active refinement payload.

Only a refinement output that passes QA and receives explicit author approval may be registered as Face Root Authority.

## FACE_ANCHORED_ROOT_MASTER
Resolution:
`master-creation/FACE_ANCHORED_ROOT_MASTER.md`

Execution:
`../execution/face-anchored-root/PAYLOAD.txt`

Required visual reference:
exact approved `../identity/master/face-root/YURA_FACE_ROOT.png` as `FACE_DETAIL_REFERENCE`.

No other visual reference is allowed.

FACE_DETAIL_REFERENCE may control FACE / EYE / EAR / face-framing hair only.
It must not control BODY, full hair length, outfit, pose, scene, or rendering style.

The actual image must reach generation execution; Git existence alone is not enough.

Failed full-body candidates never become the next reference.
The approved Face Root remains the sole face identity carrier in this submode.

## TEXT_ONLY_ROOT_MASTER — final reference-free verification
Resolution:
`master-creation/TEXT_ONLY_ROOT_MASTER.md`

Actual image-generation semantic input:
`../execution/text-only-root/PAYLOAD.txt`

Run controller:
`../execution/text-only-root/RUN.md`

Source lock:
`../execution/text-only-root/SOURCE_LOCK.md`

Generation-time image references = NONE.
Edit source carrier = NONE.

Do not inject:
- Face Root
- face-anchored Root
- repository Root Master PNG
- previous generation
- refinement edit-source carrier
- controller / QA / Gate text

Only `PAYLOAD.txt` enters the generation-facing semantic handoff.

### Text-only source lock
Before generation, `SOURCE_LOCK.md` must match the current protected source blobs.

A stale source lock blocks generation until `PAYLOAD.txt` is deliberately recompiled and the lock is updated.

### Text-only failure handling
`TARGETED_RETRY = FORBIDDEN`

A failed text-only candidate is rejected as a whole.
Keep the fixed payload unchanged inside the active batch.
Repeated systematic drift requires batch stop, deliberate payload/source diagnosis, source-lock update, then a new batch.

## PRODUCTION targeted retry
Only a mode with verified visual carriers / references may claim preservation of unaffected domains.

## Pose route
For significant motion:
- load `POSE_RULES.md`
- route BODY view through `../gate/VIEW_ROUTER.md`
- keep references locked by declared role
- apply Visibility / Occlusion Protocol

## Outfit route
School Uniform requires its dependency Gate.

`GARMENT FOLLOWS BODY.`
`BODY NEVER FOLLOWS GARMENT MASTER.`

Rejected / intermediate generation is never auto-promoted to Identity Authority or Production Reference.
A Gate-authorized `EDIT_SOURCE_CARRIER` remains a non-reference edit input and does not alter that rule.
