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
- repository Root Master PNG
- previous generation
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
