# YURA Normal Super-Long Validation Template

Status: **ACTIVE VALIDATION TEMPLATE / NOT A CANON OWNER**
Created: 2026-09-15
Character: 久遠ゆら / YURA
Primary Normal-style authority: `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`
Parent HAIR authority: `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
QA authority: `visuals/yura/qa/GENERATION_QA.md`
Purpose: Normal Super-Longを他の変数から分離して生成・比較・採否判定するための固定テスト条件。

---

## 1. Validation objective

このテンプレートでは、YURAの通常時の下ろし髪 **Normal Super-Long** について以下を検証する。

- 正式な長さ境界
- 縦長Iライン寄りのシルエット
- 標準よりやや多めの総毛量
- 細く柔らかな髪質
- 上部の落ち着き
- 中間〜背面の十分な密度
- restrained lateral spread
- 毛先の自然なテーパー
- 正面 / 側面 / 背面のmass continuity
- HAIR v1.3とRendering grammarの両立

この検証はBODY / FACE / EYE / RENDERINGを再設計するものではない。

---

## 2. Fixed CANON LOCK

生成ごとに次を固定する。

### Identity / BODY

- 久遠ゆら / YURA
- 成人女性、見た目20代前半
- 153 cm
- exactly 7.25 heads tall
- petite / slender / delicate, not skeletal
- protected BODY v1.0 unchanged

### FACE / EYE

- current `visuals/yura/identity/face/FACE_SPEC.md`
- blue-gray eye identity
- current `visuals/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
- full-bodyでpupil notchが解像できない場合は拡大しない

### HAIR

- `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
- `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`
- no ponytail / bun / chignon / half-up / braid
- no hair ornament

### RENDERING

- `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
- high-quality 2D anime illustration
- low PBR / low CGI
- grouped illustrated hair locks

---

## 3. Fixed neutral presentation conditions

Normal Super-Longだけを比較しやすくするため、原則として以下を固定する。

- exactly one YURA
- full-body standing reference
- simple pale fitted inner top
- simple pale shorts
- bare feet
- no accessories
- no jewelry
- no hair ornaments
- neutral / relaxed-to-soft expression
- no strong emotional expression
- no decorative pose
- plain white / warm-white background
- no text
- no logo
- no labels
- no panel / character-sheet / turnaround-board layout
- 9:16 portrait
- minimal safe margin
- near-orthographic / minimal perspective distortion

MASTERのreference clothingはfashion canonではなく、この検証では比較条件としてのみ使用する。

---

## 4. Phase A — FRONT main candidate

### Camera / pose

- front-facing
- full body head-to-toe visible
- face forward
- balanced standing posture
- feet naturally parallel / slightly relaxed
- arms naturally down and slightly separated from torso
- no deliberate wind

### Hair requirements

- silver-white Normal Super-Long
- principal ends = natural waistline to slightly below
- only longest fine ends may approach just before upper-buttock region
- principal mass must not reach mid-buttock or thighs
- total mass slightly above standard
- strands fine / soft
- upper area settles under weight
- middle / back retains sufficient density
- overall silhouette = vertical I-line leaning
- lateral spread restrained
- tips taper lightly / delicately
- main back mass remains behind shoulders / back
- front-visible hair limited mainly to face-framing / some chest-area strands

### FRONT pass emphasis

特に見る項目:

1. 顔の横で膨らみすぎていないか
2. 肩から外へ扇状に広がっていないか
3. 正面だからという理由で後ろ髪の大半が胸側へ来ていないか
4. ウエスト基準の長さが読み取れるか
5. 毛先が厚い板状 / スカスカのどちらにもなっていないか

---

## 5. Phase B — SIDE structural validation

FRONT候補が十分強い場合に追加する。

### Camera / pose

- clean side view or mild 3/4 side structural view
- full body visible
- same neutral clothing / BODY / expression / lighting family
- no wind

### SIDE pass emphasis

- root-to-tip continuity
- shoulder / back / waist contact
- upper hair does not float away from body without cause
- hair depth is sufficient but not an oversized slab
- principal endpoint remains around waist to slightly below
- longest fine ends stay within upper-buttock boundary
- front face-framing and rear main mass remain physically connected

SIDE image is an **auxiliary structural reference**, not an independent alternate hairstyle.

---

## 6. Phase C — BACK structural validation

FRONT候補が十分強い場合に追加する。

### Camera / pose

- straight or near-straight back view
- full body visible
- same neutral conditions
- no wind

### BACK pass emphasis

- main mass centered from back of head through central back
- sufficient middle / back density
- waist region may be substantially covered
- main mass not split widely simply to reveal BODY / clothing
- principal ends around waist to slightly below
- only the finest longest tips may approach just before upper-buttock region
- principal mass does not reach mid-buttock / thighs
- tips taper naturally

BACK image is an **auxiliary structural reference**, not a replacement for the current whole-character VISUAL MASTER.

---

## 7. Generation prompt baseline

Use the current YURA protected identity and the following Normal Super-Long meaning.

`YURAの通常時の基本髪型はNormal Super-Long。銀白色。主な毛先は自然なウエストライン付近〜わずかに下まで届き、最長の細い毛先のみ上臀部手前まで許容する。主要毛量を臀部中央より下や太ももまで延長しない。一本一本は細く柔らかいが、総毛量は標準よりやや多め。長さの自重で頭頂〜上部は落ち着き、中間〜背中には十分な密度を残す。全体は縦長のIライン寄りで横へ大きく広がらない。下方へ進むほど自然にテーパーし、毛先は軽く繊細に収束する。前髪は薄めのロングバング、顔まわりは頬に沿う長めのサイドバング。正面でも主毛量は背面側に保持し、前へ回り込む髪は顔まわり〜胸付近の一部だけにする。風のない通常状態では重力に従って自然に下へ落ちる。`

Anti-drift guard:

`Do not extend the principal hair mass to mid-buttock or thigh length. Do not make fine hair sparse. Do not fan the hair widely sideways. Do not move most back hair to the front merely to expose the outfit or body. Keep the main mass gravity-dominant and behind the shoulders/back.`

---

## 8. Strict output guard

Validation generationでは次を禁止する。

- character sheet
- multiple YURAs
- front / side / back panels in one image
- inset portraits
- hair diagrams
- labels / measurements / arrows
- text / logo
- swatches
- decorative poster design
- strong wind
- dramatic action pose
- outfit redesign
- hair arrangement

目的は **Normal Super-Longそのものを一枚ずつ評価すること**。

---

## 9. Hair-specific validation checklist

Use `PASS / FAIL / NOT OBSERVABLE / N/A` semantics from `visuals/yura/qa/GENERATION_QA.md`.

### Length

- [ ] principal ends around natural waistline to slightly below
- [ ] longest fine ends no lower than just before upper-buttock region
- [ ] dominant length is not only below-chest
- [ ] principal mass does not reach mid-buttock
- [ ] hair does not reach thigh length

### Mass / silhouette

- [ ] total mass reads slightly above standard
- [ ] strands read fine / soft
- [ ] fine does not read sparse
- [ ] upper hair settles naturally
- [ ] middle / back retains sufficient density
- [ ] silhouette remains I-line leaning
- [ ] lateral fan / triangle spread absent

### Tips

- [ ] tips gradually taper
- [ ] tips are not a heavy blunt slab
- [ ] tips are not excessively sparse

### Front distribution

- [ ] main mass remains principally behind shoulders / back
- [ ] only reasonable face-framing / chest-area strands come forward
- [ ] no artificial front-loading of back hair

### Back continuity

- [ ] main mass remains centered down the back
- [ ] no artificial wide split to expose BODY / outfit
- [ ] root-to-tip continuity is physically plausible

### Rendering

- [ ] high-quality 2D anime grammar
- [ ] grouped illustrated locks
- [ ] no photoreal hair-fiber dominance
- [ ] no waxy / PBR / CGI hair material

---

## 10. Candidate decision

### ACCEPT AS NORMAL SUPER-LONG VISUAL REFERENCE CANDIDATE

Use when:

- protected YURA identity remains intact
- BODY / FACE / EYE / RENDERING remain canon-consistent
- Normal Super-Long hair-specific checklist materially passes
- no major output artifact blocks comparison

### TARGETED HAIR RETRY

Use when:

- YURA identity / BODY / FACE / RENDERING pass
- only Normal Super-Long hair length / mass / distribution / tip behavior fails

Action:

- keep CANON LOCK fixed
- modify only HAIR instructions belonging to the failed criterion

### REJECT

Use when:

- a protected non-hair domain materially drifts
- output becomes character sheet / multi-panel / wrong composition
- hair is materially outside the protected range and cannot serve as a useful candidate

---

## 11. Promotion rule

A successful output may be promoted only by explicit user decision.

Possible role:

- `Normal Super-Long visual reference`
- future dedicated Normal Super-Long hair master / reference artifact

It does **not** automatically replace:

- `visuals/yura/identity/master/VISUAL_MASTER.png`
- `visuals/yura/identity/master/VISUAL_MASTER.md`

If the user later explicitly chooses to replace the whole-character neutral MASTER, handle that as a separate MASTER change-control event.

---

## 12. Current production scope

As of 2026-09-15:

- near-term hairstyle production focus = **Normal Super-Long only**
- Low Chignon / Braided Half-Up / Mid Ponytail / Low Ponytail visual-master production = **deferred until October 2026 or later unless the user explicitly reopens them earlier**

This scheduling note controls current work priority only. It does not delete the already-defined arrangement rules.
