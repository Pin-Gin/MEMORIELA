# YURA RENDERING SPEC

Status: **PROTECTED YURA-SPECIFIC RENDERING LAYER**

Project-wide rendering authority:
`../../../CHARACTER_RENDERING_STYLE.md`

Skin authority:
`../skin/SKIN_SPEC.md`

## Purpose

This file defines only YURA-specific rendering behavior that is not already defined by the Visual Master, protected Identity Specs, or the project-wide Matte Natural Anime style.

Do not duplicate BODY / FACE / EYE / HAIR / SKIN identity definitions here.

## YURA rendering rule

YURA uses the project-wide **Matte Natural Anime** rendering style unless the user explicitly requests a one-off style derivative.

Rendering may describe visible form, but must not:
- redesign YURA's BODY
- alter FACE geometry
- recolor EYE / HAIR / SKIN identity
- change source hair length or mass
- change outfit structure
- reinterpret YURA as another character

## Targeted retry stability

When retrying a failed BODY / FACE / EYE / HAIR / SKIN / outfit / pose domain:
- preserve the current rendering grammar
- do not silently change line treatment
- do not silently change shading behavior
- do not silently change gloss level
- do not silently change overall contrast

Only the failed domain should be corrected unless the user explicitly requests a rendering change.

## Authority

For generation:
1. current YURA Visual Master PNG
2. protected Identity Specs
3. requested pose / camera / outfit / expression / scene
4. this YURA-specific rendering layer
5. project-wide Matte Natural Anime rendering style

This file does not override higher-priority identity authority.
