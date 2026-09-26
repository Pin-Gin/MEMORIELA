# YURA RENDERING STYLE SPEC

Status: **PROTECTED RENDERING SPECIFICATION / CURRENT RENDERING DOMAIN AUTHORITY**
Current Revision: **v0.1**
Started: 2026-09-11
Validated: 2026-09-11
Authority aligned: 2026-09-13 — status / authority metadata synchronized with `docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
Purpose: 久遠ゆらを「誰として描くか」と「どう描くか」を分離し、参照画像なしでもYURAらしい2Dアニメイラスト描画を再現するための描画仕様。

> このファイルは **rendering style only** を定義する現行のprotected domain authorityである。
> 顔形状・目鼻口・額・肌色などのidentity geometryは `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md` を正とする。
> 瞳孔のprotected signatureは `docs/assistant-context/creation/yura/identity/eyes/EYE_SIGNATURE_SPEC.md` を正とする。
> 髪型構造は `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md` を正とする。通常生成では旧HAIR revisionをGit履歴から取得しない。
> 身体比率・人体寸法は `docs/assistant-context/creation/yura/identity/body/BODY_MASTER.md` / `docs/assistant-context/creation/yura/identity/body/BODY_SPEC.md` を正とし、このファイルから再定義しない。
> 実用生成の統合入口は `docs/assistant-context/creation/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md` とする。

Text-only validation success:

- gen_id: `b0621ffd-7096-4530-b04f-181039dd9d63`
- calibration image input: **none**
- user assessment: **良い / intended direction preserved**

## 1. Core style identity

YURAの基準描画は、**高品質な2Dアニメイラスト**を主体とする。

狙いは「半リアルCGIをアニメ化した絵」ではなく、最初から2Dイラストとして設計された、柔らかく上品で透明感のある成人女性キャラクター表現。

主要原則:

- illustration-first / 2D-first
- clean anime illustration
- delicate visible line art
- soft cel-like grouped shading
- low micro-texture
- low photographic realism
- low CGI / 3D-render feel
- adult-balanced anatomy
- refined, soft, approachable
- subdued, elegant color handling
- no chibi / mascot simplification

Conceptual balance only:

- anime / illustration character: **strong majority**
- semi-real detail: **supporting minority only**

数値比率そのものを生成命令の中心にしない。重要なのは以下の具体的な描画文法。

## 2. Line art

- 輪郭線は**細く、柔らかく、明確に読める**。
- 線は真っ黒な漫画インクではなく、淡い灰〜青灰〜髪や肌に馴染む低コントラスト色を許容する。
- 顔輪郭、目、鼻・口の最小限の形、主要な髪束、衣服境界が線として認識できること。
- 線の強弱は穏やか。外周だけ極端に太くしない。
- 線画が陰影に埋もれて消え、CGIペイントに見える状態を避ける。
- 過剰なクロスハッチ、写実スケッチ、荒い鉛筆質感は使用しない。

Target impression:
**delicate clean anime line art with soft low-contrast edges**.

## 3. Face rendering

### 3.1 Skin

- 肌は**フラット〜浅いセル塗りを基礎**にする。
- 立体感は大きく整理された1〜2段階の陰影と、ごく柔らかな補助グラデーションで出す。
- 頬、顎下、首、鼻周辺に必要最小限の陰影を置く。
- 写真的なsubsurface scattering、湿った肌艶、毛穴、微細な凹凸、3Dレンダー的なスペキュラは避ける。
- ハイライトは狭いテカりではなく、柔らかな面として扱う。
- 色白・健康的な血色は `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md` の仕様に従う。

### 3.2 Nose

- 鼻は**イラストとして簡潔に描く**。
- 鼻筋全体をリアルな立体面で彫刻しない。
- 正面では小さな影、短い線、鼻先付近の最小限の明暗で存在を示す。
- 鼻孔を黒く強調しない。
- 横顔では形は読めるが、CGI的な骨格モデリングにはしない。

### 3.3 Mouth / lips

- 口は**細い線と淡い自然な色**で構成する。
- 唇に写実的な厚み・濡れ・グロス・強いハイライトを付けない。
- 上下唇の立体面をリアルに描き分けすぎない。
- 下唇のみごく薄い色面または柔らかな影で存在感を補う程度。
- neutral faceでは口元を静かで柔らかく保つ。

### 3.4 Cheeks / blush

- 頬の血色は低彩度の淡いピンク。
- 境界は柔らかいが、エアブラシで顔全体を赤く染めない。
- 強い化粧感・ドールメイク感を避ける。

## 4. Eye rendering

目はYURAの識別性のため、顔の中で最も情報量を許容する部位。

ただし眼球自体を写実化しない。

- `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md` の青灰色、虹彩構造、ハイライト、瞳孔意匠を維持する。
- protected pupil signatureは `docs/assistant-context/creation/yura/identity/eyes/EYE_SIGNATURE_SPEC.md` に従う。
- 虹彩グラデーションは丁寧にしてよい。
- 外周は少し濃い青灰色だが、黒いコンタクトレンズ状リングにしない。
- 白目は真っ白ではなく、周囲の光に馴染むわずかな暖色 / 灰色を許容。
- 眼球のwetness、角膜の写真的反射、血管、涙膜のリアル表現を避ける。
- 上まぶた・まつ毛は明確だが簡潔。
- 下まぶたは軽く、囲い込みすぎない。
- 目を大きく見せるために既定geometryを変更しない。

Target:
**detailed anime iris inside clearly illustrated, non-photographic eyes**.

## 5. Hair rendering

YURAの銀白髪は、写真の髪ではなく**イラスト化された毛束構造**として描く。

- 大きな毛束 / 中くらいの毛束を主構造にする。
- 細い補助線は必要最小限。
- 一本一本を数百本描くような near-photographic strand rendering を避ける。
- 毛束の重なりで流れと立体感を作る。
- ハイライトは多数の細い白線ではなく、**面・帯・まとまり**として置く。
- 髪の影も大きく整理された形にする。
- 毛先は自然に分かれるが、ノイズ状の細毛を増やしすぎない。
- 柔らかく軽い質感を保つ。
- hairstyle geometry自体は `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md` を正とする。

### Back-view continuity rule

背面・後ろ向きでは、**後ろ髪の大部分を背中側へ自然に残す**。

- 後ろ髪を左右から不自然に胸側へ回し込まない。
- 背中や服を見せるためだけに髪を前方へ退避させない。
- 少量の前髪・サイドバングのみ自然に前側へ存在してよい。
- front / side / back で髪量・長さ・重力方向の連続性を保つ。

Target:
**clean grouped silver-white hair masses with elegant strand accents**.

## 6. Shading / lighting

- 基本は**soft cel shading / grouped illustration shading**。
- 明暗境界は完全な硬セル塗りではなく、必要に応じて少し柔らかくする。
- ただし全身を滑らかな3Dグラデーションで丸めない。
- 主要な影は「形として読める」こと。
- Ambient occlusionを強く入れすぎない。
- 肌、髪、服の材質差は色・線・影形で示し、リアルなPBR反射に依存しない。
- neutral referenceではsoft diffuse lightを基本とする。
- dramatic rim light、cinematic bloom、lens effectsはスタイル判定を邪魔するため基準画像では使わない。

## 7. Color handling

- 全体は低〜中彩度。
- YURAの基準色: silver-white / soft gray / blue-gray / pale natural pink / neutral fair skin.
- 白飛びで情報を消さない。
- 強いネオン色・HDR調・極端なコントラストを避ける。
- 透明感は「高輝度CGI光沢」ではなく、明るい配色・整理された陰影・淡い反射で出す。

## 8. Material rendering

衣服やアクセサリーも2Dイラスト文法に統一する。

- cloth: 大きなfold + restrained secondary folds
- lace: pattern readable but not microscopic photoreal textile scan
- metal: small clean highlights; no ray-traced mirror realism
- skin: matte-soft
- hair: silky illustrated, not physically simulated individual fiber realism
- eyes: luminous illustration, not wet optical simulation

材質表現が顔だけ／身体だけリアル化することを避ける。

## 9. Body rendering extension

Current `docs/assistant-context/creation/yura/identity/body/BODY_MASTER.md` / `docs/assistant-context/creation/yura/identity/body/BODY_SPEC.md` のBODY geometryへ、この描画文法をそのまま全身適用する。

- anatomical proportions may be carefully controlled, but rendering remains illustrated.
- 肩、鎖骨、胸郭、腰、膝、足首などを写実的な筋骨格レンダーで彫り込みすぎない。
- 体表の立体感は大きな影面と輪郭線で整理する。
- 肌の局所的なハイライトや細かな筋肉陰影を増やさない。
- 手足は形を正確にしつつ、線と簡潔な影で描く。

## 10. Expression behavior

このスタイルでは、表情はリアル筋肉変形より**イラストとして読みやすい協調変化**を優先する。

Neutral identity authority:
- calm neutral face
- relaxed eyelids
- soft mouth corners

Smile future rule:
- mouth corners + cheek lift + slight lower-lid response + softer eye expression を同時に変化させる。
- 口角だけを上げる「貼り付けた笑顔」は禁止。
- smile spec は別途作成するため、現時点では neutral face をidentity authorityとする。

## 11. Positive generation directives

Text-only generation時は、以下の概念を優先する:

- high-quality 2D anime illustration
- clean delicate line art
- soft cel shading with restrained gradients
- flat-to-gently-modeled skin
- simplified illustrated nose and lips
- grouped illustrated hair locks
- low micro-texture
- matte soft materials
- detailed but non-photographic anime irises
- elegant adult anime character design
- soft low-contrast color palette
- natural approachable refinement

## 12. Negative generation directives

Avoid:

- photorealistic
- semi-photorealistic portrait rendering
- 3D CGI character render
- polished game cinematic face
- PBR skin
- waxy / glossy skin
- visible pores
- realistic subsurface scattering
- hyper-detailed nostrils
- glossy volumetric lips
- wet photoreal eyes
- photographic eye reflections
- individually rendered realistic hair fibers
- ray-traced specular highlights
- dramatic cinematic HDR
- heavy bloom
- strong depth-of-field glamour portrait look
- generic high-fashion / commercial-model facial rendering
- chibi proportions
- giant symbolic anime eyes
- thick manga ink outlines
- sketchy rough line art
- back-view hair pulled unnaturally to the front

## 13. Priority order when constraints conflict

1. YURA identity / geometry from FACE or BODY SPEC
2. adult readability
3. hairstyle specification
4. this 2D illustration rendering style
5. scene / outfit request
6. decorative effects

Do not sacrifice identity geometry merely to make the image look “more anime”.
Do not sacrifice 2D illustration style merely to make lighting/materials look more realistic.

## 14. Text-only reproduction validation

Validation conditions intentionally used **no image reference**.

Current application authorities:

1. `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md`
2. `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md`
3. this `docs/assistant-context/creation/yura/identity/rendering/RENDERING_STYLE_SPEC.md`

The original text-only validation is retained only as evidence for the selected rendering grammar; current HAIR geometry always comes from the current HAIR domain owner.

Successful result:

- gen_id: `b0621ffd-7096-4530-b04f-181039dd9d63`
- user review: **良いね 変わりなし**
- result preserved the intended 2D illustration direction without feeding the calibration image back into generation.

Pass criteria satisfied at protected-baseline level:

- clearly 2D anime illustration rather than the prior semi-real CGI direction
- accepted YURA face geometry remained recognizable
- nose / lips stayed illustrational and restrained
- skin used shallow grouped rendering rather than glossy realistic modeling
- hair read as illustrated grouped locks
- blue-gray eye identity remained detailed but non-photographic
- adult / early-twenties impression remained intact

Therefore:

**TEXT-ONLY STYLE REPRODUCTION = PASSED**

## 15. Provenance / calibration note

This spec was distilled from internal YURA style-calibration results on 2026-09-11 after semi-real candidates remained too realistic even when verbally requested as anime-heavy.

A successful image-reference-assisted calibration first demonstrated the intended 2D illustration direction. The rendering grammar was then written into this specification, and a subsequent text-only generation reproduced the direction without image-reference input.

The calibration image therefore remains **evidence / troubleshooting reference only**, not a required ordinary-generation source.

## 16. Operational generation entry point

For ordinary generation, first read:

`docs/assistant-context/creation/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`

That file assembles the FACE, EYE, HAIR and RENDERING layers into a reusable generation baseline and contains the explicit back-view hair rule.

## 17. Change-control

This file is the current **protected RENDERING domain authority** after successful text-only validation.

It does not replace the protected VISUAL MASTER or any geometry-domain owner. Material rendering-style changes require explicit user approval and must be committed to Git.
