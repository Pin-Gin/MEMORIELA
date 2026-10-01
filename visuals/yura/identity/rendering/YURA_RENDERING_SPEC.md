# YURA RENDERING SPEC

Status: **PROTECTED YURA-SPECIFIC RENDERING LAYER**

Project-wide base:
`../../../CHARACTER_RENDERING_STYLE.md`

YURA always uses **Matte Natural Anime** unless the user explicitly requests a one-off style derivative.

## YURA-specific anchors
- clearly high-quality 2D anime illustration
- delicate low-contrast line art
- soft cel / grouped shading
- shallow natural skin volume
- simplified anime nose / lips
- blue-gray detailed non-photoreal eyes
- grouped silver-white hair locks with limited fine-strand accents
- low-to-medium contrast
- restrained gloss
- **Matte Natural Anime is the primary visual target, not a loose preference**

## Matte reproducibility lock — mandatory
To reduce rendering drift between generations, preserve the following visible conditions:

- specular highlights on **skin / hair / clothing are minimal**
- form is described primarily by **soft cel + soft diffuse shading**, not by gloss
- skin reads as **soft, dry-matte, and calm**, never wet / oily / waxy
- hair texture is expressed through **grouped locks, overlap, thickness, and value separation**
- do not use a strong anime gloss ring, glass-like streaks, or metallic sheen on hair
- clothing must remain matte; do not reinterpret plain validation clothing as satin, silk, vinyl, or glossy sports fabric
- highlights should be **broad and weak**, not narrow, sharp, high-contrast specular streaks
- overall contrast remains **low to medium**
- white-background scenes must still preserve readable contour and soft form separation without blowing out the character
- natural volume is expressed by diffuse light-and-shadow structure, not by reflective surface treatment

## Skin
- **bright fair skin**
- **ほんの少し白寄り**
- **ごく薄い自然な血色**
- **白飛びしない**
- do not force pink / orange warmth
- no plastic / waxy / wet gloss
- no pores or photographic microtexture

## Hair
- silver-white identity must remain stable
- grouped anime locks first
- fine accents second
- texture comes from lock overlap / depth / soft value separation
- no photographic strand field
- no metallic or glass-like shine
- no dominant gloss ring
- do not increase gloss when correcting hair length / volume / pose

## Rendering priority
1. YURA Identity / BODY
2. pose / camera
3. hair physical placement
4. clothing response
5. **Matte Natural Anime rendering last**

Rendering describes structure; it does not redesign anatomy or recolor identity.

A targeted retry for BODY / FACE / EYE / HAIR / outfit / pose must **not silently change the rendering grammar**. Preserve the same matte surface, line delicacy, contrast range, diffuse shading behavior, and gloss level unless the user explicitly requests a style change.

## Prohibited
- photorealism
- semi-photoreal portrait
- realistic CGI / PBR
- glossy plastic skin
- heavy HDR
- photographic hair
- realistic pore / lip texture
