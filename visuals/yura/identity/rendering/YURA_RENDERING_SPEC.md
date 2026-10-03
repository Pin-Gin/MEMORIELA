# YURA RENDERING SPEC

Status: **PROTECTED YURA-SPECIFIC RENDERING ADAPTER**

Project-wide rendering authority:
`../../../CHARACTER_RENDERING_STYLE.md`

Skin authority:
`../skin/SKIN_SPEC.md`

## Purpose
This file defines only YURA-specific protection when the project-wide Matte Natural Anime rendering is applied.

It does not define a separate YURA art style.
It does not duplicate BODY / FACE / EAR / EYE / HAIR / SKIN identity.

## YURA rendering rule
YURA uses the project-wide **Matte Natural Anime** rendering style unless the user explicitly requests an allowed one-off rendering derivative.

Rendering may describe visible form, but must not:
- redesign YURA BODY
- alter FACE geometry
- alter EAR size / placement / tilt / projection / visibility behavior
- recolor EYE / HAIR / SKIN identity
- change source hair length or mass
- change outfit structure
- reinterpret YURA as another character

## Mandatory YURA execution compilation lock
Every YURA Execution Payload that uses Matte Natural Anime must carry the following rendering meaning without weakening it:

- **HIGH-QUALITY 2D ANIME ILLUSTRATION ONLY**
- clean, fine, but clearly readable 2D-anime linework
- linework remains visibly present; do not fade into painterly / watercolor rendering
- soft cel / grouped illustration shading is the base
- readable grouped shadow shapes define form; diffuse gradients are mild support only
- do not replace grouped anime shading with uniform airbrush softness
- low-to-medium contrast, **not ultra-low contrast**
- bright presentation is allowed, but highlights must not be overexposed
- on white / warm-white backgrounds, face, skin, silver-white hair, pale clothing, linework, and shading must remain clearly separated and readable
- hair is rendered as readable large anime hair masses with overlap, thickness, tonal depth, and restrained strand accents
- do not reduce silver-white hair to a pale translucent fiber haze
- matte / low-gloss surface quality
- soft and calm, but **not washed-out, watercolor-like, ethereal-faded, or pastel-faded**
- NOT photoreal
- NOT semi-photoreal
- NOT live-action
- NOT realistic portrait
- NOT CGI / 3D render
- NOT PBR / game-engine rendering
- NOT photographic skin
- NOT photographic hair

`BRIGHT != WASHED_OUT`
`SOFT != AIRBRUSH_ONLY`
`FINE_LINE != INVISIBLE_LINE`

If a YURA payload reduces this to only `high-key`, `soft`, `low contrast`, or `matte`, the rendering compilation is incomplete.

## Mode-specific authority

### MASTER_CREATION / TEXT_ONLY_ROOT_MASTER
Generation-time visual references are **NONE**.

Rendering authority for the execution payload:
1. protected YURA Text Identity Specs
2. this YURA rendering adapter
3. project-wide `CHARACTER_RENDERING_STYLE.md`

The current YURA Visual Master PNG must **not** be loaded, attached, inspected as a generation reference, or described into the image-generation call for this submode.

### PRODUCTION
After required Masters are approved and the Production Gate passes:
1. Gate-approved visual references in their declared roles
2. protected YURA Identity Specs
3. requested authorized derivative variables
4. this YURA rendering adapter
5. project-wide `CHARACTER_RENDERING_STYLE.md`

The image references do not override precise protected Identity Specs or the project-wide rendering authority.

## Rendering drift classification
YURA rendering is a protected domain.

Material drift includes:
- fine linework becoming visually absent
- grouped anime shading becoming uniform airbrush softness
- low-to-medium contrast collapsing into washed-out ultra-low contrast
- white-background high-key treatment erasing separation between skin / hair / clothing / background
- anime hair masses becoming translucent fiber haze
- watercolor / pastel-faded / ethereal rendering replacing Matte Natural Anime

Material rendering drift = `RENDERING FAIL` even when the result remains nominally 2D anime.
Photoreal / semi-photoreal / CGI / PBR drift remains `RENDERING HARD FAIL`.

## Targeted retry stability
When a mode with a verified visual carrier permits targeted correction:
- preserve line treatment
- preserve shading behavior
- preserve gloss level
- preserve overall contrast
- preserve realism level

Text-only stochastic modes do not claim targeted preservation.
