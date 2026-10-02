# VISUAL GENERATION GATE PROTOCOL

Status: **PROTECTED / MANDATORY / FAIL-CLOSED / PROJECT-WIDE**

Applies to all MEMORIELA Visual generation domains that adopt this protocol.

## Core rule
Gate PASS and Load Receipt completion are required before image generation.

If any required condition is missing, ambiguous, conflicting or unavailable:
`GENERATION_ALLOWED = NO`

## Source-of-truth rule
Use current Git Authority only.

The following are not valid substitutes:
- memory
- previous conversation
- previous generation
- remembered path
- similar filename
- old repository layout
- unstated convention

## No discovery / no fallback
Do not recursively discover a directory and choose files by interpretation.
Do not substitute a missing Authority with a similar file.
Do not guess alternate paths.
Only exact paths listed by the active Authority Manifest may enter the generation context.

## No unauthorized inference
`UNSPECIFIED != PERMISSION TO INVENT`

Default:
`AI_INFERENCE_REQUIRED = NONE`

AI-created variation is allowed only when the user explicitly authorizes that exact Scope.

## Modes
### PRODUCTION
Approved Masters / required visual references must exist and be available to the generation execution.

### MASTER_CREATION
Used only to create a missing or replacement Master / derived view anchor.

Each Domain must define an explicit `MASTER_CREATION_SUBMODE`.
The active submode must be recorded in the Load Receipt.

A Domain may define a text-only submode whose correct reference policy is:
`VISUAL_REFERENCES_ALLOWED = NONE`

In that case, zero visual references is a PASS condition, not a missing-reference failure.

Generated candidate is:
- CANDIDATE
- NOT AUTHORITY
- NOT REFERENCE FOR PRODUCTION
until explicit author approval and Git registration.

### VALIDATION
Controlled comparison / QA mode. Does not promote outputs.

## Dependency gates
When a request invokes another protected domain, that dependency Gate must PASS before generation.
Example: YURA + school uniform requires both YURA Gate and School Uniform Gate.

## Reference discipline
Every visual reference must have exactly one declared role from `REFERENCE_ROLE_RULES.md`.
An image must not silently control another Scope.

A text-only Master Creation submode may explicitly prohibit all generation-time visual references.

## Visibility rule
Apply `VISIBILITY_OCCLUSION_PROTOCOL.md`.
Do not alter anatomy / hair / pose merely to expose a feature.

## Post-generation
Run the active Domain QA.
Rejected or intermediate outputs are denied as future Identity Authority unless explicitly adopted through Master change control.

A reference permitted for post-generation comparison only must not be reintroduced into the generation call unless the active Gate explicitly permits it.
