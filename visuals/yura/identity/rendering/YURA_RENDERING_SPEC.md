# YURA RENDERING SPEC

Status: **PROTECTED YURA-SPECIFIC RENDERING ADAPTER**

Project-wide rendering authority:
`../../../CHARACTER_RENDERING_STYLE.md`

Skin authority:
`../skin/SKIN_SPEC.md`

## Purpose
This file defines only YURA-specific protection when the project-wide Matte Natural Anime rendering is applied.

It does not define a separate YURA art style.
It does not duplicate BODY / FACE / EYE / HAIR / SKIN identity.

## YURA rendering rule
YURA uses the project-wide **Matte Natural Anime** rendering style unless the user explicitly requests an allowed one-off rendering derivative.

Rendering may describe visible form, but must not:
- redesign YURA BODY
- alter FACE geometry
- recolor EYE / HAIR / SKIN identity
- change source hair length or mass
- change outfit structure
- reinterpret YURA as another character

## Mode-specific authority

### MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
Generation-time visual references are **NONE**.

Rendering authority for the execution payload:
1. protected YURA Text Identity Specs
2. this YURA rendering adapter
3. project-wide `CHARACTER_RENDERING_STYLE.md`

The current YURA Visual Master PNG must **not** be loaded, attached, inspected as a generation reference, or described into the image-generation call for this submode.

Post-generation comparison with the registered Root Master is allowed only through the QA route defined by the Gate.

### PRODUCTION
After Root / Face / required BODY-view Masters are approved and the Production Gate passes:
1. Gate-approved visual references in their declared roles
2. protected YURA Identity Specs
3. requested authorized derivative variables
4. this YURA rendering adapter
5. project-wide `CHARACTER_RENDERING_STYLE.md`

The image references do not override precise protected Identity Specs.

## Targeted retry stability
When retrying a failed BODY / FACE / EYE / HAIR / SKIN / outfit / pose domain:
- preserve line treatment
- preserve shading behavior
- preserve gloss level
- preserve overall contrast
- preserve realism level

Only the failed domain should be corrected unless the user explicitly requests a rendering change.
