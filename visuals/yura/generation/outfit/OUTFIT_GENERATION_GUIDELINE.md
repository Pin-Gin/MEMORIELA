# YURA Outfit Generation Guideline

Status: PROTECTED GENERATION GUIDELINE
Adopted: 2026-09-08
Updated: 2026-09-19 — current MASTER + protected validation clothing synchronized
Applies to: 久遠ゆら / YURA の衣装・日常服・季節服・部屋着・外出着・特別衣装・衣装派生画像

## 1. Purpose

This document governs outfit derivatives while preserving the current neutral YURA identity.

The current master architecture is:

**YURA neutral MASTER identity**
+ **outfit**
+ **accessories**
+ **pose / expression**
+ **scene / background**

Outfit generation must add styling layers without redesigning YURA herself.

## 2. Mandatory read order

Before generating a YURA outfit derivative:

1. `visuals/yura/identity/master/VISUAL_MASTER.md`
2. inspect `visuals/yura/identity/master/VISUAL_MASTER.png` when repository-image inspection is available
3. `visuals/yura/identity/body/BODY_MASTER.md`
4. `visuals/yura/identity/body/BODY_SPEC.md`
5. `visuals/yura/identity/face/FACE_SPEC.md`
6. `visuals/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
7. `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
8. `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
9. `visuals/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`
10. this guideline
11. `visuals/yura/qa/VALIDATION_CLOTHING_SPEC.md` when the task is MASTER / BODY / FACE-full-body / HAIR controlled validation
12. current outfit / scene request

If a ponytail / chignon / half-up / braid or another arrangement is requested, also apply `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`.

Do not reconstruct YURA from conversational memory alone or from an arbitrary older derivative.

If direct master-image inspection is unavailable, follow `visuals/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md` before concluding the MASTER cannot be viewed. Never substitute an arbitrary generated image or deleted Git revision as identity authority.


## 3. Current canonical master

Current neutral visual master:

- repository image: `visuals/yura/identity/master/VISUAL_MASTER.png`
- Git blob SHA: `2c99257f5ae8c2c878f649dd97474d6860a8d689`
- gen_id: `e942a217-75fd-4154-88cc-6c0f74e99d82`
- manifest: `visuals/yura/identity/master/VISUAL_MASTER.md`
- role: canonical neutral full-body whole-character identity reference + approved Normal Super-Long visual anchor

The current MASTER was generated after formal HAIR v1.3 + Normal Super-Long v1.0 adoption and is aligned with that baseline.

## 4. Protected visual identity

Preserve unless the user explicitly approves a change:

- Name: 久遠ゆら / YURA
- adult woman, apparent age early twenties
- height: 153 cm
- **7.25 heads tall**
- petite / slender / delicate adult build
- slender compact ribcage
- bust clearly to moderately fuller relative to the petite frame
- natural narrow shoulders / slim waist / adult pelvis balance
- legs slender with natural softness, not model-stretched
- arms slender but not stick-thin
- silver-white **super-long hair**
- formal hair endpoint: principal ends around the natural waistline to slightly below; only the longest fine ends may approach the upper-buttock boundary
- blue-gray eyes
- soft refined adult facial identity
- high-quality 2D anime illustration rendering

Canvas or outfit changes must never alter BODY proportions.

## 4A. Controlled validation clothing

For MASTER / BODY / FACE-full-body / HAIR controlled validation, ordinary outfit freedom is suspended.

Authority:
`visuals/yura/qa/VALIDATION_CLOTHING_SPEC.md`

Use the fixed neutral validation-clothing generation wording:

- plain pale opaque sleeveless top
- plain pale opaque simple shorts

Do not reinterpret the outfit as fashion.
Do not expand the generation prompt with detailed anatomy-specific clothing prohibitions.
If clothing materially changes apparent anatomy, classify that after generation as a comparison-condition failure.

## 4B. Outfit / BODY geometry separation — PROTECTED

Authority:
`visuals/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

Changing outfit never authorizes changing YURA's underlying BODY.

For outfit-only / strict-preservation / controlled-validation tasks:

- define the current BODY_LOCK from BODY MASTER + BODY SPEC;
- use a verified BODY geometry carrier;
- require `BODY_GEOMETRY_GUARANTEED`;
- garment pixels / drape / volume may change only as the requested clothing layer;
- garment overlap with torso / pelvis / limbs does not make those BODY regions editable;
- garment must fit / drape around the protected anatomy;
- do not resize shoulders / ribcage / bust / waist / pelvis / thighs / arms to fit garment;
- if hidden BODY would have to be stochastically re-inferred, return `BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED`.

For outfit-only exact preservation, also require `PROTECTED_PIXEL_PRESERVATION_GUARANTEED` for immutable visible regions.

---

## 5. Outfit design direction

Default direction:

- clean / refined
- feminine
- soft / delicate
- calm rather than flashy
- tasteful / wearable
- slightly elegant
- adult / mature enough for an early-twenties woman
- not costume-like unless requested

Useful families:

- clean casual
- feminine casual
- soft elegant
- classical
- understated romantic
- refined seasonal styling
- Japanese-gothic / special styling when explicitly requested

## 6. Exposure / coverage baseline

YURA no longer has an automatic **low-exposure** clothing bias.

Default rule:

**Use normal, context-appropriate adult clothing exposure for the named garment / outfit. Do not add extra coverage merely because the outfit shows ordinary skin, and do not alter the garment category just to reduce exposure.**

Allowed by default when natural for the requested garment / context:

- ordinary V-necks / open collars
- sleeveless or short-sleeve garments
- skirts and dresses at ordinary fashion lengths
- ordinary shoulder / back exposure
- ordinary midriff exposure when the named garment naturally includes it
- sheer / lace / cutout details within normal fashion use
- fitted silhouettes that remain normal clothing rather than lingerie-like styling

Do not automatically:

- add an undershirt, jacket, cardigan, shawl, or extra layer solely to cover ordinary skin
- lengthen a skirt / dress simply because it is above the knee
- raise a neckline beyond the requested garment structure
- merge one garment type into another to make it more covering
- redesign a specified outfit into a conservative substitute

Still avoid by default unless the user explicitly requests the relevant style / context:

- clothing that reads primarily as lingerie in an ordinary public-wear request
- implausibly extreme exposure unrelated to the named garment
- accidental wardrobe-malfunction presentation
- sex-appeal-first redesign that overrides the requested outfit identity

The named garment and its structural identity take priority over an automatic modesty correction.

## 7. Color direction

Naturally compatible colors include:

- white
- black
- gray
- navy
- muted blue
- lavender
- beige
- mauve
- dusty pink
- burgundy
- soft neutrals

These are recommendations, not hard restrictions.

Avoid defaulting to neon palettes, excessively saturated multi-color combinations, childish color blocking, or cheap-looking metallic / glitter-heavy styling.

## 8. Presentation / pose

Preferred:

- natural standing
- walking
- seated reading / café / indoor poses
- light hand gestures
- holding context-appropriate objects
- gentle smile / neutral / thoughtful expressions

Avoid by default:

- chest-forward glamour posing
- exaggerated pelvic tilt
- spread-leg or underwear-revealing presentation
- camera angles designed mainly to emphasize cleavage / thighs / buttocks

### BODY invariance

Changing outfit, shoe height, canvas ratio, or scene must not change:

- 7.25-head ratio
- head size relative to body
- shoulder / ribcage / waist / pelvis relationships
- thigh / calf thickness
- arm thickness

If a new canvas is needed, scale the whole character uniformly and adjust negative space.

## 9. Hair continuity

Follow `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`.

For ordinary down-hair back views:

- the principal hair mass remains behind the shoulders / back
- primary ends sit around the natural waistline to slightly below
- only the longest fine ends may approach the upper-buttock boundary
- do not pull most hair around to the chest merely to expose clothing
- do not spread the hair sideways merely to expose waist / back garment construction
- do not lengthen the main mass to mid-buttock or thigh merely because the garment is long

For arrangements, preserve source super-long length / total mass according to `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`.

## 10. Identity consistency over outfit consistency

If an outfit request conflicts with protected identity, identity wins unless the user explicitly approves an exception.

Do not:

- change hair color to match outfit palette
- change eye color
- age YURA up / down
- significantly change facial proportions
- change BODY scale / ratio
- change formal HAIR v1.3 source length / total mass merely to reveal an outfit
- let fashion style turn YURA into a different character
- let realistic materials push rendering into semi-photoreal CGI

## 11. Master clothing is not canonical fashion

The simple pale fitted inner + shorts used in the neutral master are **reference garments only**.

They exist to show the silhouette and do not restrict future wardrobe design.

## 12. Text inside generated images

Generated labels, signatures, profile text, biography, measurements, likes / dislikes, dialogue and other text are non-authoritative unless separately reviewed and approved.

## 13. Prompt-building rule

Every outfit generation should conceptually contain:

1. **Neutral master identity** — `visuals/yura/identity/master/VISUAL_MASTER.md` + visual cross-check of `visuals/yura/identity/master/VISUAL_MASTER.png` when available
2. **BODY** — `visuals/yura/identity/body/BODY_MASTER.md` + `visuals/yura/identity/body/BODY_SPEC.md`
3. **Face / Eye** — `visuals/yura/identity/face/FACE_SPEC.md` + `visuals/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
4. **Hair** — `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
5. **Hair arrangement**, when applicable — `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`
6. **Rendering** — `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
7. **Practical assembly** — `visuals/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`
8. **Outfit / context-appropriate exposure rules** — this document
9. **Current requested design / scene**

Standing anchor meaning remains:

`153cmの小柄・華奢 体格比で胸はやや豊かめ`

Outfit exposure / coverage is resolved separately from the BODY anchor according to the named garment and scene context.

And BODY scale cue:

`Keep YURA exactly 7.25 heads tall and preserve all approved body widths / limb thicknesses regardless of outfit or canvas.`

## 14. Change control

This guideline is protected.

Do not silently weaken or alter:

- identity invariants
- 7.25-head BODY invariance
- current FACE / EYE SIGNATURE / HAIR v1.3 / RENDERING authorities
- context-appropriate adult exposure baseline
- prohibition on automatic extra-coverage redesign of a named garment
- neutral-master + styling-layer architecture
- separation between generated visual artifacts and Persona / biography authority

Future baseline changes require explicit user approval and Git logging.
