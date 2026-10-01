# YURA TEXT-ONLY GENERATION REFERENCE

Status: PROTECTED PRACTICAL GENERATION BASELINE
Current Revision: **v1.0**
Adopted: 2026-09-12
Updated: 2026-09-19 — Strong Braided Half-Up protected route synchronized
Purpose: 画像参照を必須にせず、承認済みのYURAの顔・髪・描画スタイル・BODYを文章仕様から安定再構築するための実用生成入口。

## 0. Current visual anchor

Canonical neutral visual master:

- repository image: `visuals/yura/identity/master/VISUAL_MASTER.png`
- Git blob SHA: `2c99257f5ae8c2c878f649dd97474d6860a8d689`
- gen_id: `e942a217-75fd-4154-88cc-6c0f74e99d82`
- manifest: `visuals/yura/identity/master/VISUAL_MASTER.md`
- exported PNG SHA-256: `bddf347cd38c1a38e8154b06d9e3d01a8dd3d585991903fa464aa7924966ccf2`

This is the preferred whole-character visual cross-check and the approved visual anchor for the Normal Super-Long baseline. When repository-image inspection is available, inspect the committed PNG before formal derivative generation. Text specs remain authoritative for exact geometry / continuity rules.

Current HAIR relationship:

The current MASTER was generated after adoption of formal HAIR v1.3 + Normal Super-Long v1.0 and is aligned with that baseline. `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md` still owns HAIR core; `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md` owns the ordinary unarranged down-style implementation; the MASTER is their preferred whole-character visual cross-check.

## 1. Authority / read order

Before ordinary YURA full-body generation:

1. `visuals/yura/identity/master/VISUAL_MASTER.md`
2. `visuals/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md` — recover / verify current visual MASTER
3. inspect the verified current MASTER representation
4. `visuals/yura/identity/body/BODY_MASTER.md`
5. `visuals/yura/identity/body/BODY_SPEC.md`
6. `visuals/yura/identity/face/FACE_SPEC.md`
7. `visuals/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
8. `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
9. `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md` when no alternate arrangement is requested / ordinary YURA hair is intended
9. `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
10. this file
11. `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md` when ponytail / chignon / half-up / braid or another arrangement is involved
12. `visuals/yura/identity/hair/styles/strong-braided-half-up/SPEC.md` when `ハーフアップ + 編み込み強め` / `Strong Braided Half-Up` is explicitly requested
13. `visuals/yura/qa/VALIDATION_CLOTHING_SPEC.md` for MASTER / BODY / HAIR controlled validation
14. `visuals/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md` when outfit generation is involved
15. current scene / outfit request

Normal generation uses current branch authorities only. If direct image inspection is unavailable, follow `visuals/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md`; do not substitute an arbitrary derivative or deleted Git revision.

## 2. Priority order

1. YURA visual identity / face
2. protected YURA eye signature when visible at the asset scale
3. approved BODY geometry
4. adult readability
5. protected HAIR v1.3 geometry / mass / gravity
6. protected Normal Super-Long implementation when ordinary down hair is intended
7. YURA-specific 2D rendering grammar
8. project-wide Matte Natural Anime rendering layer
9. outfit / scene
10. decorative presentation effects

## 3. Core identity

久遠ゆら / YURA。成人女性、見た目年齢20代前半。身長153cm。

- soft oval adult face
- small softly rounded chin
- forehead standard to slightly compact
- healthy bright fair skin
- small refined nose
- small-to-modest natural pale-pink lips
- blue-gray eyes with restrained saturation
- adult-balanced eyes slightly larger than average, mildly almond-shaped and horizontally elongated
- pupil is very dark blue-gray / deep gray, close to black, almost circular with extremely subtle vertical elongation
- YURA-specific protected eye signature: **an extremely small teardrop-like notch on the lower-right edge of the pupil**
- the notch is a discreet identity / provenance-supporting cue, not a conspicuous symbol and not a technical watermark
- close-up assets should preserve it intentionally; full-body assets must not enlarge it merely to force visibility
- silver-white super-long hair following `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
- ordinary unarranged hairstyle = `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`
- refined / soft / approachable adult impression

Exact facial geometry follows `visuals/yura/identity/face/FACE_SPEC.md`.
Protected pupil-signature behavior follows `visuals/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`.

## 3A. Protected color lock — mandatory

These colors are Identity, not styling:

- iris: **blue-gray with restrained saturation**
- pupil: very dark blue-gray / deep gray, close to black
- hair: **silver-white**
- skin: healthy bright fair skin

Do not let Matte Natural Anime, warm/cool scene lighting, outfit palette, background palette, or cinematic color grading recolor these identity anchors.

Eye-color anti-drift cue:

`YURA's irises must remain clearly blue-gray with restrained saturation. Do not shift them to amber, brown, hazel, purple, vivid blue, or cyan. Lighting may affect highlights only; it must not change the perceived base iris color.`

Hair-color anti-drift cue:

`Keep YURA's hair silver-white. Do not reinterpret it as blonde, beige, lavender, gray-purple, or metallic white.`

A derivative with visibly non-blue-gray irises is an Identity FAIL.

---

## 4. Approved BODY block

- 153 cm petite adult scale
- **exactly 7.25 heads tall — protected invariant**
- slender / delicate but not skeletal
- somewhat narrow natural shoulders
- slender compact ribcage
- bust clearly to moderately fuller relative to petite frame, not independently oversized
- soft hemispherical bust direction; gently sloped upper contour / naturally fuller lower contour
- standard-to-slightly-short torso
- slim natural waist
- flat-leaning abdomen with slight natural softness
- natural adult pelvis / hips; outer hips about shoulder width to slightly wider
- standard-to-slightly-long legs
- thighs slender with natural softness, neither thick nor stick-thin
- small restrained knees
- slender gently curved calves
- slim plausible ankles
- arms slender to slightly below average adult-female thickness, **not stick-thin**
- hands small to standard; fingers slightly long / slender / elegant
- feet standard / natural for a 153 cm adult woman

Magic phrase:

`153cmの小柄・華奢 体格比で胸はやや豊かめ`

Outfit exposure / coverage is not part of this BODY anchor. Resolve clothing structure and normal context-appropriate exposure through `visuals/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md` and the current outfit request.

## 5. Canvas / scale invariance — mandatory

Canvas size and aspect ratio are layout variables only.

- crown-to-sole figure height = **7.25 × head height**
- use one uniform scale factor for the entire character
- never independently resize head / torso / pelvis / thighs / calves / arms / feet
- never thicken legs because the canvas is portrait-oriented
- never lengthen legs to fill a tall canvas
- never enlarge the head because the character is shown smaller
- absorb aspect-ratio changes through framing / negative space
- if necessary, reduce overall character occupancy rather than changing anatomy

Prompt cue:

`Keep YURA exactly 7.25 heads tall. Treat her as one uniformly scaled proportion system. Canvas size changes only framing and empty space, never anatomy.`

Portrait invariance validation:

- gen_id: `24b1e4e2-9930-4fc0-bec7-d0a555da09c7`
- user assessment: **「OK 変わりなし」**
- result: PASS

## 6. Hair block — formal v1.3 + Normal Super-Long v1.0

Current HAIR authority:
`visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`

Current default normal-down implementation:
`visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`

Protected core baseline:

- silver-white super-long hair
- primary ends reach the **natural waistline to slightly below**
- only the longest fine ends may extend toward the **upper waist / just before the upper-buttock region**
- dominant hair ending only around below-chest is too short
- main hair mass reaching mid-buttock / lower buttock / thighs is too long
- total hair mass is **slightly above standard**
- individual strands are **fine and soft**
- fine strands must not be interpreted as sparse total hair
- upper hair settles naturally under the weight of the total length
- middle / back retains sufficient density
- lateral spread remains restrained rather than fan-shaped
- tips gradually lose mass and taper lightly / delicately
- very gentle natural wave
- thin long bangs flowing naturally from center-ish area to left / right
- long cheek-framing side-bangs
- soft face layers

### Normal Super-Long default

Unless another arrangement is explicitly requested:

- wear the hair fully down as **Normal Super-Long**
- overall silhouette = **vertical I-line leaning**
- do not fan the hair widely sideways
- main mass remains behind the shoulders / back
- only reasonable face-framing / chest-area strands come forward
- front view must not pull most back hair to the chest simply to show the length
- back view keeps the main mass centered down the back
- main mass must not extend to mid-buttock or thighs
- tips remain light and delicately tapered, not blunt-heavy and not sparse

Prompt cue:

`銀白色のNormal Super-Long。主な毛先は自然なウエストライン付近〜わずかに下まで。最長の細い毛先のみ上臀部手前まで許容。主要毛量を臀部中央より下や太ももまで延長しない。総毛量は標準よりやや多めだが一本一本は細く柔らかい。上部は自重で落ち着き、中間〜背中には十分な密度を残す。全体は縦長のIライン寄りで横へ大きく広がらず、毛先は徐々に量が抜けて軽く繊細に収束する。正面でも主毛量は背面側に保持する。`

Anti-drift guard:

`Do not extend the principal hair mass to mid-buttock or thigh length. Do not make fine hair sparse. Do not fan the hair widely sideways. Keep the main mass gravity-dominant and behind the shoulders/back.`

### Back-view continuity

- majority of long back hair stays behind the shoulders and down the back
- dominant mass remains centered behind the body
- do not pull most hair forward merely to expose BODY / clothing
- do not split the mass widely merely to reveal the waist / back silhouette
- the waist area may be substantially covered by the main mass
- only the longest fine ends may approach the upper-buttock area
- do not extend the principal mass to mid-buttock or thighs

### Low Chignon specialized route

If the request explicitly specifies `ローシニヨン` / `low chignon` / `full low chignon`, apply `visuals/yura/identity/hair/styles/LOW_CHIGNON_SPEC.md`.

Key lock:
- rear-center lower-head placement
- bun stays on the back of the head; not on the neck
- all non-face-framing Super-Long hair is fully stored inside the chignon
- compact-to-small-medium bun
- true front view may hide the bun completely
- do not move / enlarge / expose it merely for camera readability

### Strong Braided Half-Up specialized route

If the request explicitly specifies `ハーフアップ + 編み込み強め` / `ハーフアップ＋編み込み強め` / `強めの編み込みハーフアップ` / `Strong Braided Half-Up`, apply `visuals/yura/identity/hair/styles/strong-braided-half-up/SPEC.md`, read `visuals/yura/identity/hair/styles/strong-braided-half-up/VISUAL_MASTER.md`, and inspect paired `visuals/yura/identity/hair/styles/strong-braided-half-up/VISUAL_MASTER.png` when repository-image inspection is available. Use gen_id `0336bd46-16bf-4d17-823b-73d6204cba31` as the protected hairstyle topology visual anchor.

Key lock:
- principal ends remain natural waistline to slightly below
- only longest fine tips may approach upper-buttock boundary
- no principal mass at mid-buttock / thighs
- total mass remains only slightly above standard
- do not increase the loose lower section
- luxury comes from braid structure and restrained ornament, never extra length / width / mass
- do not relocate or expose hidden rear structure merely for camera readability

### Arranged-hair conservation

When a ponytail, low chignon, half-up, bun or braid is explicitly requested:

- apply `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`
- source total hair mass remains slightly above standard
- source super-long length is not silently deleted
- a ponytail reflects the source length / mass
- a full chignon stores the source length through credible wrapping / folding / internal overlap
- camera visibility never relocates an anatomical tie point merely to show the hairstyle

Near-term hairstyle production remains focused on Normal Super-Long. Other arrangement visual-master work is deferred until October 2026 or later unless explicitly reopened.

## 7. Rendering block

Render YURA as a **high-quality 2D anime illustration**.

- delicate visible low-contrast line art
- soft cel / grouped illustration shading
- flat-to-shallow skin modeling
- simplified illustrated nose and lips
- low micro-texture
- low PBR / low CGI cues
- grouped illustrated hair locks, not photoreal fibers
- detailed but non-photographic anime irises
- soft low-to-medium contrast palette
- adult-balanced anatomy

Avoid photoreal / semi-photoreal portraits, 3D CGI, waxy PBR skin, pores, wet photographic eyes, glossy volumetric lips, photoreal individual hair fibers, heavy HDR / bloom, chibi proportions, giant symbolic eyes.

2D/anime rendering does not remove the protected pupil signature. Preserve it when the eye is large enough to render it naturally; never enlarge it into an obvious symbol.

### Controlled validation clothing

For MASTER / BODY / HAIR validation, apply `visuals/yura/qa/VALIDATION_CLOTHING_SPEC.md`.

Use only the neutral positive clothing block from `visuals/yura/qa/VALIDATION_CLOTHING_SPEC.md`:

- **plain pale opaque sleeveless top**
- **plain pale opaque simple shorts**

Japanese:
- **淡色・無地・不透明のシンプルなノースリーブトップス**
- **淡色・無地・不透明のシンプルなショートパンツ**

Keep the generation prompt short and neutral.
Do not inject detailed QA / rejection vocabulary into the image-generation prompt.
Validation clothing is a comparison instrument, not fashion.

## 8. Neutral MASTER composition mode

When reproducing the neutral current MASTER concept:

- exactly one YURA
- front-facing full body
- head top through toes fully visible
- near-orthographic / minimal perspective distortion
- centered
- small but sufficient margins
- feet naturally parallel / not crossed
- balanced left-right weight
- arms naturally down and slightly separated from torso
- face forward / no deliberate head tilt
- neutral to very soft expression
- plain pale opaque sleeveless top
- plain pale opaque simple shorts
- bare feet
- no accessories / hair ornaments
- plain white / warm-white background
- no text / logos / panels / labels / decorative board layout
- apply formal HAIR v1.3 + Normal Super-Long v1.0 exactly
- use current MASTER `e942...` as the preferred visual comparison

The simple master clothing is not canonical fashion; it exists only to expose the silhouette.

## 9. Strict single-standing-illustration mode

For one standing image / 立ち絵 / 一枚もの:

- one YURA only
- one composition only
- requested angle only
- full body fully visible when requested
- retain exact 7.25-head ratio independent of canvas size
- no character sheet / turnaround / expression sheet / insets / panels / callouts / swatches / measurements / labels / text / logos
- preserve the eye-signature design in the high-resolution source when practical, but do not distort the eye to make it visible at small display scale

## 9A. Dynamic pose route — mandatory when movement is significant

When the requested pose is more complex than neutral standing, walking, or another low-risk posture, read and apply:

`visuals/yura/generation/pose/POSE_GENERATION_GUIDELINE.md`

For twist, seated, squat / crouch, kneeling, large forward / backward lean, strong lateral lean, reaching, running / dynamic stepping, or other significant movement, the guideline's **Dynamic Pose Preservation Rule** is mandatory.

Core rule:

`動的ポーズではYURAのBODYを再設計せず、固定されたYURA BODYを関節回転・重心移動・接触変形だけでポーズさせる。`

Generation order:

1. protected YURA Identity / BODY
2. skeleton transform
3. camera / perspective
4. support / contact / load
5. hair physical placement while conserving source mass / length
6. outfit physical response
7. YURA rendering + Matte Natural Anime last

Do not let pose, foreshortening, seating compression, or camera perspective redefine BODY.

---

## 10. Outfit / accessory separation

The master fixes YURA herself, not styling.

Variable derivative layers:

- clothing
- jewelry
- hair ornaments
- footwear
- pose
- expression beyond neutral baseline
- background / scene

Body geometry must remain stable when these layers change.

## 11. Generation assembly

**CURRENT VISUAL MASTER IDENTITY (`e942...`)**
+ **FACE / EYE DETAILS**
+ **PROTECTED EYE SIGNATURE**
+ **APPROVED BODY v1.0 / 7.25-HEAD INVARIANT**
+ **FORMAL HAIR v1.3 GEOMETRY / MASS / GRAVITY**
+ **NORMAL SUPER-LONG v1.0 when ordinary down hair is intended**
+ **HAIR ARRANGEMENT TOPOLOGY only when explicitly requested**
+ **2D RENDERING STYLE**
+ **OUTFIT / ACCESSORIES**
+ **POSE / SCENE**
+ **LAYOUT CONTROL**
+ **NEGATIVE CONSTRAINTS**

Do not allow styling, camera or canvas language to redefine protected identity.

## 12. Change control

This v1.0 practical generation reference is protected.

If later generation drifts, diagnose in this order:

1. layout / prompt-control failure
2. rendering-style drift
3. Normal Super-Long / HAIR drift against current protected specs
4. BODY drift
5. face / eye-signature / identity drift

Do not alter protected identity merely because a single derivative generation fails.
