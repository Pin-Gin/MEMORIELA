# SCHOOL UNIFORM GENERATION GATE

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

## Pre-read
1. `../../gate-core/GATE_PROTOCOL.md`
2. `../../gate-core/AUTHORITY_SCOPE_RULES.md`
3. `../../gate-core/REFERENCE_ROLE_RULES.md`
4. `AUTHORITY_MANIFEST.md`
5. `REFERENCE_GATE.md`

## Modes
### MASTER_CREATION
Allowed before a Uniform Master exists.

Required:
- `../SCHOOL_UNIFORM_SPEC.md`
- applicable component specs
- applicable grade variant
- neutral mannequin / no character identity transfer

Candidate output is NOT Authority until author approval.

### PRODUCTION
Requires:
- approved Uniform Master image
- Master manifest
- `SCHOOL_UNIFORM_VISUAL_TEXT.md` created from the approved Master
- all required component specs
- OUTFIT_REFERENCE actually available to generation
- Load Receipt PASS

If any required Master artifact is absent:
`GENERATION_ALLOWED = NO`

## Scope
Uniform Gate controls:
- blazer / shirt / ribbon / tie
- skirt / slacks
- piping / buttons
- emblem
- colors / pattern
- canonical garment construction

Uniform Gate must not change:
- character BODY
- FACE / EYE / HAIR / SKIN
- character identity
- pose unless clothing physics requires local drape only

`GARMENT FOLLOWS CHARACTER BODY.`

## Final permission
Complete `../../gate-core/LOAD_RECEIPT_SCHEMA.md` before generation.
