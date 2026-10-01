# YURA Validation Clothing Spec

Status: **PROTECTED VALIDATION-CLOTHING SUB-SPEC / CURRENT**
Current Revision: **v1.0**
Adopted: 2026-09-19
Updated: 2026-09-19 — generation wording simplified to neutral clothing terms
Character: 久遠ゆら / YURA

Purpose:
YURAのMASTER候補、BODY検証、HAIR検証などで、服装の再解釈によって体格・シルエットの見え方が変わり、比較QAが汚染されることを防ぐ。

This file defines **validation clothing only**.
It does not define YURA's ordinary fashion or public outfit canon.

Parent authorities:
- BODY → `visuals/yura/identity/body/BODY_MASTER.md` + `visuals/yura/identity/body/BODY_SPEC.md`
- OUTFIT → `visuals/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md`
- whole-character cross-check → `visuals/yura/identity/master/VISUAL_MASTER.md`

---

## 1. Scope / trigger

Apply this spec whenever the task is primarily:

- YURA visual MASTER candidate generation
- BODY validation
- HAIR validation / hairstyle MASTER candidate generation
- FACE validation where full-body clothing is present
- controlled A/B comparison in which BODY / silhouette must remain comparable

Representative phrases:
- `MASTER候補`
- `マスター画像用`
- `髪型のマスター`
- `BODY検証`
- `体格比較`
- `髪だけ変更`
- `変更は髪型のみ`

Ordinary derivative fashion generation does not automatically use this validation outfit.

---

## 2. Validation outfit — fixed category

Use exactly the following validation-clothing category.

### 2.1 Generation prompt block — use this wording

For image generation, compile only this simple positive clothing description:

**淡色・無地・不透明のシンプルなノースリーブトップス**
+
**淡色・無地・不透明のシンプルなショートパンツ**

English equivalent when needed:

**plain pale opaque sleeveless top**
+
**plain pale opaque simple shorts**

Required generation meaning:

- ordinary adult clothing
- solid pale / off-white / light-neutral color
- opaque
- simple construction
- no decorative styling
- natural fit
- no special shaping function
- not tight compression wear
- not oversized enough to hide the body silhouette

### 2.2 Prompt-compiler rule

The generation prompt must stay short and neutral.

Do **not** inject the detailed QA / rejection vocabulary from this file into the image-generation prompt.
In particular, do not expand the prompt into a long list of anatomy-specific or exposure-specific prohibitions.

The purpose is to reduce semantic over-attention and garment reinterpretation.

Use:
- positive neutral garment identity
- plain / pale / opaque / simple
- ordinary fit

Then evaluate the result after generation through QA.

### 2.3 Lower garment

Use:

**淡色・無地・不透明のシンプルなショートパンツ**

Required:
- plain
- pale / off-white / light neutral
- opaque
- ordinary short-pants construction
- natural fit
- no decorative fashion reinterpretation

---

## 3. BODY-neutral presentation principle

Validation clothing must remain visually neutral and must not intentionally reshape the protected BODY.

Generation-side instruction stays generic:

**keep the current protected YURA BODY unchanged; clothing is neutral validation clothing only.**

Do not compile detailed anatomy-specific correction language into the image prompt.

The protected BODY specification remains authoritative and post-generation QA determines whether the output stayed comparable.

---

## 3A. BODY geometry preservation during validation

Validation clothing is a measurement condition, not BODY authorization.

For strict A/B comparison / BODY-preservation runs, apply:
`visuals/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

Required behavior:

- keep current protected BODY geometry independently from clothing pixels;
- clothing may overlap projected torso / pelvis / limbs without making anatomy editable;
- garment adapts to BODY;
- do not repair garment mismatch by changing BODY;
- when the execution route would otherwise re-infer hidden BODY beneath the garment, require `BODY_GEOMETRY_GUARANTEED`;
- if that cannot be guaranteed, use `BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED`.

---

## 4. Clothing interpretation tolerance

Tiny generative variation is acceptable only when it does **not** change the comparison function.

Acceptable small variation:
- minor seam placement
- tiny edge thickness difference
- very small neckline curvature difference within the same simple modest category
- slight fabric-fold variation caused by gravity

Not acceptable:
- changing the plain sleeveless top into a clearly different garment category
- adding visible decorative styling
- changing fit enough to materially alter BODY comparability
- adding sheer / translucent material
- changing shorts into a clearly different fashion-oriented lower garment

If the outfit changes category or materially changes apparent anatomy, the candidate is **not comparable** for MASTER / BODY / HAIR validation.

---

## 5. No-compensation rule

Do not modify clothing to expose a region hidden by hair, arms, pose, or camera.

Do not:
- redesign the top
- redesign the shorts
- tighten or loosen clothing specifically to expose hidden structure
- add openings
- remove fabric
- add contrast decoration

merely to make BODY easier to inspect.

Likewise, do not move hair / limbs merely to make the validation clothing easier to inspect.

Occlusion is allowed when physically natural.
Use the correct domain QA status rather than redesigning another domain.

---

## 6. MASTER-aligned neutral presentation

For neutral MASTER / HAIR MASTER candidates:

- front-facing full body
- neutral upright posture
- arms naturally lowered
- bare feet
- white / warm-white background
- Profile A / 9:16
- this fixed validation outfit
- no unrelated accessories
- no text / labels / panels

The outfit exists only to preserve comparison consistency.

---

## 7. QA interpretation

For MASTER / BODY / HAIR validation:

### PASS
- upper garment remains a plain pale opaque simple sleeveless top
- shorts remain plain pale opaque simple shorts
- no decorative reinterpretation
- garment does not materially change apparent BODY

### FAIL — validation clothing mismatch
- garment category materially changes
- decorative styling is introduced
- transparency is introduced
- garment fit materially changes BODY comparability
- outfit becomes fashion-oriented rather than neutral validation clothing

Important:
A validation-clothing mismatch is **not itself a BODY failure**.
It is a **comparison-condition failure** and blocks BODY / hairstyle-MASTER adoption until a comparable candidate is generated.

Do not rewrite BODY canon to fit a clothing-confounded image.

---

## 8. Relationship to Strong Braided Half-Up

`visuals/yura/identity/hair/styles/strong-braided-half-up/SPEC.md` must use this file for MASTER-candidate validation clothing.

The hairstyle-only change rule becomes:

**Current protected YURA identity + protected BODY + protected FACE + fixed validation clothing + fixed neutral pose/camera/background + only the hairstyle arrangement changes.**

---

## 9. Change control

This spec is protected.

Do not silently change:
- pale / plain / opaque validation outfit category
- simple sleeveless-top + simple-shorts generation wording
- prompt-compiler rule that keeps detailed QA negatives out of the generation prompt
- prohibition on fashion reinterpretation during validation
- comparison-condition FAIL semantics

Material changes require explicit user approval and Git logging.
