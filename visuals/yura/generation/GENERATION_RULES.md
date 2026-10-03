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

## TEXT_ONLY_ROOT_MASTER
Resolution:
`master-creation/TEXT_ONLY_ROOT_MASTER.md`

Actual image-generation semantic input:
`../execution/text-only-root/PAYLOAD.txt`

Run controller:
`../execution/text-only-root/RUN.md`

Source lock:
`../execution/text-only-root/SOURCE_LOCK.md`

Generation-time image references = NONE.

Only `PAYLOAD.txt` enters the image-generation semantic handoff.

Do not append:
- `RUN.md`
- `SOURCE_LOCK.md`
- Gate text
- QA text
- batch count
- comparison language
- current Master PNG or its description
- retry procedure
- per-run corrective wording
- prior-generation discussion

### Text-only source lock
Before generation, `SOURCE_LOCK.md` must match the current protected source blobs.

A stale source lock blocks generation until `PAYLOAD.txt` is deliberately recompiled and the lock is updated.

### Text-only failure handling
`TARGETED_RETRY = FORBIDDEN`

A failed text-only candidate is rejected as a whole.

Do not say:
- keep BODY fixed and change EYE only
- keep FACE fixed and change HAIR only
- preserve this candidate and repair one semantic scope by stochastic regeneration

Those guarantees require a fixed visual carrier and are not available in text-only full regeneration.

Instead:
- keep `PAYLOAD.txt` unchanged inside the active batch
- generate a new independent full candidate
- re-run all protected-domain QA

If repeated isolated runs show the same failure, revise `PAYLOAD.txt` / source Authority outside the active batch, update `SOURCE_LOCK.md`, and start a new batch.

## PRODUCTION targeted retry
Only a mode with verified visual carriers / references may use true targeted retry where the execution route can preserve unaffected protected domains.

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

Rejected / intermediate generation is never auto-promoted to Identity Authority.
