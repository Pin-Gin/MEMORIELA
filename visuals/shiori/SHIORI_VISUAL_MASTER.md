# 一ノ瀬 栞 Visual Master

Status: **PROTECTED VISUAL MASTER / CURRENT**

Adopted: **2026-09-29**

Purpose: MEMORIELA における一ノ瀬栞の whole-character Visual Identity を固定する現行マスタ。  
人物設定そのものは `characters/SHIORI.md`、生成時の具体的な数値・形状・FAIL条件は `visuals/shiori/SHIORI_VISUAL_TEXT.md` を正とする。

---

## 1. Current approved master artifact

Current canonical Shiori Visual Master:

- repository image: `visuals/shiori/SHIORI_VISUAL_MASTER.png`
- Git blob SHA-1: `40a3e1cee043e0e2895b8b8f7efce50ca1330466`
- generation id: `3e81a4a2-2d9e-4424-af02-a72bec952e0d`
- dimensions: **1024 × 1536**
- PNG bytes: **1,237,713**
- SHA-256: `5561bd5945cead011752ad2e449c12ea1fe09c19953e3d88ad4bf4a55d1b200c`
- role: **front-facing full-body whole-character Visual Identity anchor**

This PNG is the current visual authority for Shiori's approved whole-character appearance.

---

## 2. Authority relationship

Use this master together with:

- character canon: `characters/SHIORI.md`
- generation / geometry authority: `visuals/shiori/SHIORI_VISUAL_TEXT.md`

Authority split:

- **VISUAL MASTER PNG**
  - whole-character appearance
  - face impression
  - glasses impression
  - body balance
  - hair color / overall silhouette
  - rendering impression
- **SHIORI_VISUAL_TEXT.md**
  - exact BODY values
  - FACE / EYES / GLASSES definitions
  - HAIR length / color / mass limits
  - SIDE / BACK continuity
  - validation clothing
  - generation layout
  - FAIL boundaries

If an incidental detail in the PNG conflicts with an explicit fixed rule in the Visual Text, **the explicit Visual Text rule wins inside that domain**.

---

## 3. Approved master composition

The master establishes the following neutral comparison condition:

- exactly **one Shiori**
- front-facing
- full-body standing view
- entire figure visible from head to feet
- centered composition
- minimal perspective distortion
- white / warm-white background
- barefoot
- relaxed neutral standing posture
- calm expression / very slight smile
- no text
- no logo
- no decorative accessory other than Shiori's fixed glasses

This is the default whole-character validation presentation.

---

## 4. Whole-character visual identity — protected

### 4.1 Height / body balance

- height concept: **168 cm**
- total body ratio: **7.5 heads tall**
- high-school girl with adult-proportioned, tall-leaning silhouette
- relatively long legs
- slender overall frame without appearing frail

Canvas size or framing must not redefine the 7.5-head BODY relationship.

### 4.2 BODY

Approved combined impression:

- shoulders: standard to slightly narrow
- ribcage: natural / not wide
- waist: clearly slim
- pelvis / hips: natural adult female width
- thighs: naturally full rather than extremely thin
- legs: relatively long
- arms: slender but not stick-thin
- bust: **clearly / substantially fuller relative to the frame**
- bust shape: **hemispherical direction**
- upper torso must not be widened merely to support bust volume

The master fixes the overall BODY impression, while exact front / side / back continuity is controlled by the Visual Text.

---

## 5. FACE — protected visual anchor

The approved face impression is:

- soft oval face
- not excessively long
- refined, slightly narrow chin
- calm / gentle adult-balanced expression
- eyes slightly larger than average but horizontally balanced
- small mouth
- small but slightly high nose
- fair skin
- soft, intelligent, composed impression

Do not reinterpret the face into:

- extreme V-line
- childlike round face
- strongly mature / realistic face
- fashion-model / semi-photoreal face

---

## 6. EYES — protected visual anchor

Approved eye impression:

- pale blue-gray base
- very weak lavender component
- low-to-medium saturation
- medium-to-slightly-high brightness
- mildly almond-shaped
- horizontal balance retained
- outer corners neutral to very slightly downturned

Do not shift to vivid violet, bright blue, fox-eye, or excessively droopy-eye styling.

---

## 7. GLASSES — protected identity element

Glasses are part of Shiori's default Visual Identity.

Approved master direction:

- thin frame
- dark navy to black
- horizontally oriented soft-square to oval
- restrained visual presence
- eyes remain clearly readable through lenses
- no strong lens reflection in ordinary neutral presentation

Strong reflection is allowed only as a deliberate scene / expression effect.

---

## 8. HAIR — protected visual anchor

### 8.1 Default hairstyle

- long hair worn down
- this down-hair state is the default source hairstyle
- ponytail and other arrangements are derivatives

### 8.2 Color

- **blue-black**
- dark areas read nearly black
- deep navy appears only in lit regions
- avoid vivid blue or purple reinterpretation

### 8.3 Length / volume / texture

- principal ends: **below chest to above waist**
- some longer strands may approach the waist
- principal mass must not extend clearly below the waist
- total hair amount: standard to slightly above standard
- individual strands: fine / soft
- mild natural wave is allowed
- avoid strong curls or large-volume lateral expansion

The master provides the whole-hair appearance anchor; precise length / mass limits remain governed by the Visual Text.

---

## 9. Validation clothing — not canonical fashion

The clothing shown in this master is **validation clothing**, not Shiori's everyday canonical outfit.

Approved validation category:

Upper:
- pale / off-white / light-neutral
- sleeveless tank-top shape
- broad shoulder sections rather than thin straps
- hem around the hip-bone line
- plain
- opaque
- matte

Lower:
- pale / off-white / light-neutral
- plain simple shorts
- no ornament
- no drawstring
- hem from upper thigh to slightly below
- opaque
- matte

The validation outfit exists to expose BODY / HAIR / whole-character balance and must not redefine anatomy.

---

## 10. Rendering baseline

The master establishes the following rendering direction:

- high-quality 2D anime illustration
- delicate clean line art
- low-to-medium contrast
- soft cel / grouped shading
- fair skin with shallow illustrated shading
- grouped blue-black hair masses with fine strand accents
- detailed but non-photoreal eyes
- low PBR / low CGI
- no realistic skin microtexture
- no 3D-render-like anatomy

---

## 11. Default generation relationship

When generating ordinary Shiori images:

1. read `characters/SHIORI.md`
2. read `visuals/shiori/SHIORI_VISUAL_TEXT.md`
3. use `visuals/shiori/SHIORI_VISUAL_MASTER.png` as the whole-character visual cross-check
4. preserve BODY / FACE / EYES / GLASSES / HAIR / RENDERING unless the user explicitly requests a derivative change
5. default to **one Shiori per image**
6. do not automatically convert ordinary generation into a character sheet / three-view layout

The master is the visual anchor; the Visual Text is the reusable generation specification.

---

## 12. Master acceptance / QA baseline

A normal derivative should be considered drifted if it materially departs from the approved master + Visual Text in any of the following:

- 7.5-head body balance
- tall-leaning overall silhouette
- bust-to-frame relationship
- shoulder / ribcage / waist balance
- face shape
- eye color / eye shape
- glasses shape / thickness
- blue-black hair color
- default long-hair length
- default rendering style

A derivative does **not** become a new Visual Master merely because it looks good.

---

## 13. Change control

This master is **PROTECTED**.

Do not:

- replace the PNG without explicit author approval
- promote an intermediate generation to master automatically
- change protected BODY / FACE / EYES / GLASSES / HAIR / RENDERING based on one derivative
- treat validation clothing as permanent fashion canon

A future replacement requires:

1. explicit author approval
2. replacement image committed to Git
3. updated Git blob SHA / dimensions / byte size / SHA-256
4. updated generation id when available
5. consistency check against the current Visual Text
6. this manifest updated in the same change set

---

## 14. Current master identity summary

**一ノ瀬栞 / Shiori Ichinose**

168 cm / 7.5 heads.  
Tall-leaning, slender adult-proportioned high-school girl with relatively long legs, natural hips and thighs, and a clearly fuller hemispherical bust relative to her frame.  
Soft oval face, small but slightly high nose, pale blue-gray eyes with a faint lavender component, thin dark glasses, and blue-black long hair worn down with principal ends between below-chest and above-waist.  
Quiet, soft, intelligent, composed visual impression.  
High-quality 2D anime rendering with delicate linework and restrained soft shading.
