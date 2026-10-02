# YURA GENERATION RULES

Status: **CANONICAL / MANDATORY OPERATIONAL RULES**

Authority paths / Reference roles are resolved by the active Gate and Manifest.

## Execution separation
Do not send the entire Authority set to the image-generation model.

Follow:
`../../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md`

The active mode must resolve a concise mode-specific Execution Payload.

## One-person / one-image invariant
Unless the user explicitly asks for a multi-character composition:
- exactly one YURA
- one canvas
- one composition
- one image
- no character sheet
- no multi-pose sheet
- no automatic front+side+back layout
- no comparison sheet / triptych

When multiple outputs are requested, execute multiple independent single-image calls.

## Identity lock
Always preserve:
- 153 cm concept
- exact 7.25-head BODY
- YURA face
- blue-gray eyes
- silver-white hair
- default Normal Super-Long unless explicitly changed
- protected SKIN
- project-wide rendering through the YURA rendering adapter

## No AI reinterpretation
Do not:
- replace protected identity with generic anime defaults
- redesign for beauty / readability
- average conflicting traits
- invent unspecified identity changes

`UNSPECIFIED != PERMISSION TO INVENT`

## TEXT_ONLY_ROOT_MASTER
Use exactly:
- `master-creation/TEXT_ONLY_ROOT_MASTER.md` for resolution
- `execution/TEXT_ONLY_ROOT_EXECUTION.md` for image-generation semantics
- `execution/TEXT_ONLY_ROOT_SINGLE_RUN.md` for call isolation

Generation-time image references = NONE.

Do not append:
- Gate text
- QA text
- batch count
- comparison language
- current Master PNG priority

## Pose route
For significant motion:
- load `POSE_RULES.md`
- route BODY view through `../gate/VIEW_ROUTER.md`
- keep references locked by their declared roles
- apply Visibility / Occlusion Protocol

## Outfit route
When outfit changes, load `OUTFIT_RULES.md`.

School Uniform requires its dependency Gate.

`GARMENT FOLLOWS BODY.`
`BODY NEVER FOLLOWS GARMENT MASTER.`

## Retry lock
Correct only the failed execution Scope.
Do not silently change unaffected identity / rendering / reference roles.

Rejected / intermediate generation is never auto-promoted to Identity Authority.
