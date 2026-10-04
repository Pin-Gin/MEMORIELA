# YURA BODY GEOMETRY GUIDE

Status: **AUTHOR-APPROVED / ACTIVE**

Authority image:
`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

この文書は、YURAの全身比率・内部縦方向ランドマーク・上半身／下半身境界を固定するBODY Geometry Authority定義である。

**BODY GEOMETRY IMAGE AUTHORITY = ACTIVE**

## Active guide

作者承認済みAuthority画像:
- dimensions: **1200 × 1600 px**
- format: **PNG**
- SHA-256: **7e4c6dd7c525d5a1f123418cf20e417aab654200b4ed734972467a548148b407**
- Git blob SHA: **0a4c2ec2db9e15c4edaae50a91bfb3552fae9767**

実測基準:
- crown / 0.0: **y = 160 px**
- chin / 1.0: **y = 340 px**
- 1 head = **180 px**
- crotch / pelvis-line proxy: **y = 856 px**
- knee proxy: **y = 1156 px**
- soles / 7.2: **y = 1456 px**
- (1456 - 160) / 180 = **7.2 heads**

内部ランドマーク:
- crown→crotch = **3.8667 heads**
- chin→crotch = **2.8667 heads**
- crown→knee = **5.5333 heads**
- crotch→knee : knee→soles = **300 px : 300 px = 1 : 1** in this approved guide

このAuthority画像と異なるファイルを、同名だからという理由だけでAuthorityへ昇格させてはならない。
画像を差し替える場合は、再検証・作者承認・ハッシュ更新を必須とする。

## Target geometry

全身は **7.2頭身** をTARGETとする。

頭頂から顎先までの頭部高を1.0とした場合、頭頂から足裏までを7.2とする。

**TARGET = 7.2 heads**
**ACCEPTABLE RANGE = 7.1–7.3 heads**

## Explicit upper / lower body boundary

立位全身での上半身／下半身の境界は、以下の線として明示する。

**CROTCH / PELVIS LINE = UPPER / LOWER BODY BOUNDARY**

承認済みガイド上では:
- boundary y = **856 px**
- crown→boundary = **3.8667 heads**
- chin→boundary = **2.8667 heads**

Image APIおよびQAでは、この境界より上をupper body / torso側、この境界より下をlower body / inseam側として扱う。
顔参照画像のcropや画面占有率からこの境界を推測してはならない。

## Author-approved YURA inseam proxy

立位Body Geometry QAでは、画像上の股下比率proxyを以下で定義する。

```text
inseam_proxy_ratio = (soles_y - crotch_y) / (soles_y - crown_y)
```

承認済みガイド値:

```text
(1456 - 856) / (1456 - 160)
= 600 / 1296
= 46.2963%
```

YURA用運用値:
- **PASS TARGET = 46.0–46.5%**
- **46.5%超〜47.0%未満 = FAIL**
- **47.0%以上 = HARD FAIL / too model-like**

これは一般人体の普遍的基準ではなく、YURAの「座高がやや低い印象」「骨盤位置やや高め」「下半身がわずかに長い」という作者意図を再現するためのキャラクター固有Body Geometry QA値である。

**YURA INSEAM PROXY TARGET = 46.0–46.5%.**
**47.0% OR MORE IS FORBIDDEN AS TOO MODEL-LIKE.**

## Torso-specific numeric gate

総頭身とinseam proxyを同時に満たすとき、`chin→crotch` のtorso spanを追跡する。

```text
chin_to_crotch_heads
= (crotch_y - chin_y) / (chin_y - crown_y)
```

承認済みガイド値:

```text
(856 - 340) / 180
= 2.8667 heads
```

7.1–7.3頭身かつinseam proxy 46.0–46.5%から導かれる監査用envelope:
- **chin→crotch = 2.7985–2.9420 heads**

判定:
- `chin_to_crotch_heads > 2.9420` = 上半身／torsoが長すぎるためFAIL
- `chin_to_crotch_heads < 2.7985` = 上半身を不自然に圧縮している可能性があるためFAIL
- 数値範囲内でも、胸郭・腰・骨盤配置が不自然なら視覚QAでFAILできる

**TORSO-SPECIFIC GATE = COMPACT TORSO + HIGHER PELVIS + YURA INSEAM PROXY PASS.**

## Knee / lower-leg reference

承認済みガイドでは:
- knee proxy: **y = 1156 px**
- crotch→knee = **300 px**
- knee→soles = **300 px**
- lower-body split = **1 : 1**

この1:1値は、現時点では承認済みガイド内部の参照値として使用する。
太ももだけ、または膝下だけを伸ばして股下比率を成立させていないかをQAで確認する。
独立したHard Gateとして別範囲を追加する場合は、作者承認を経て明示的に固定する。

## Authority scope

`YURA_BODY_GEOMETRY_GUIDE.png` は以下のみのAuthorityとする。

- 頭部と全身の相対スケール
- 7.2頭身の分割位置
- 上半身／下半身境界
- 肩・胸郭・腰・骨盤・股・膝・足首などの縦方向配置
- 股下proxy
- torso span
- 全身シルエットの大枠
- 全身上の頭部配置
- 全身Geometry QA

## Explicitly denied authority

このガイド画像は以下のAuthorityではない。

- 顔Identity
- 顔の縦横比
- 目の形・大きさ・間隔
- 眉・鼻・口
- 中顔面・下顔面
- 頬・顎
- 髪型Identity
- 耳Identity
- 表情
- 衣装デザイン
- レンダリングスタイル

**BODY_GEOMETRY_GUIDE -> FACE_GEOMETRY = DENIED**
**BODY_GEOMETRY_GUIDE -> FACE_IDENTITY = DENIED**

## Geometry rules

7.2頭身は、胴体・脚・肩幅・腰幅・胸郭・四肢を不自然に大型化して成立させない。
脚だけを不自然に長くしない。
胴だけを不自然に長くしない。
肩幅や骨格を大きくしない。
体格そのものを大きく見せない。

YURAの7.2頭身では、**上半身を縦方向に間延びさせない**。
首・胸郭・腹部・腰・骨盤までを長く引き延ばして頭身を稼がない。

- 顎から股までの上半身スパンを不必要に長くしない
- 胸郭から腰・骨盤までのtorso spanをコンパクトに保つ
- 腰位置を不自然に低くしない
- 骨盤／股位置をやや高めに保つ
- 股から足裏までの下半身をわずかに長く見せる
- 膝位置は自然に保つ
- 下半身を長く見せるために脚だけを機械的に伸ばさない
- 上半身を短く見せるために胸郭・腹部を不自然に圧縮しない

**UPPER BODY MUST NOT BE VERTICALLY ELONGATED.**
**TORSO MUST BE COMPACT; DO NOT LENGTHEN THE RIBCAGE-TO-PELVIS OR WAIST SPAN.**
**KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.**
**LOW SITTING-HEIGHT IMPRESSION = RELATIVELY COMPACT UPPER-BODY SPAN + SLIGHTLY LONGER LOWER BODY.**
**DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.**

フェイスアップ画像のキャンバス内サイズ、トリミング、余白、頭部の画面占有率をBODY Geometryへ持ち込まない。

DO NOT INFER BODY PROPORTION FROM FACE REFERENCE CROP OR SCALE.
DO NOT USE FACE REFERENCE CANVAS OCCUPANCY AS BODY GEOMETRY.
DO NOT CREATE A TALL MODEL-LIKE BODY TO SATISFY 7.2 HEADS.

## Body Geometry QA landmarks

RAW Master候補のBody Geometry QAでは、最低限以下の縦ランドマークを記録する。

- crown
- chin
- crotch / pelvis-line proxy
- knee
- soles

必須の数値判定:
- crown→chin = 1.0 head
- crown→soles = target 7.2 heads
- acceptable total ratio = 7.1–7.3 heads
- inseam proxy ratio = target 46.0–46.5%
- chin→crotch = torso-specific audit envelope 2.7985–2.9420 heads

加えて、以下を視覚QAする。
- torsoがcompactである
- waistが不自然に低くない
- pelvis/crotchが意図どおりやや高い
- lower bodyがわずかに長い
- knee placementが自然
- thigh-only / shin-only stretchingがない

これらの確認結果と実測ランドマーク値は `body_geometry_qa.json` に残す。

## Face identity preservation

BODY Geometry調整時も、顔Identityは `YURA_FACE_REFERENCE.png` と `YURA_VISUAL_TEXT.md` に従う。
BODY Geometry Guideは、顔内部を変更して頭身を成立させてはならない。

FACE SHAPE MUST REMAIN IDENTICAL IN PROPORTION.
BODY GEOMETRY GUIDE CONTROLS PROPORTION, NOT FACE IDENTITY.

## Guide image requirement

全身Master候補を作る際は、ACTIVEな `YURA_BODY_GEOMETRY_GUIDE.png` を7.2頭身・上半身／下半身境界・股下proxy・torso geometryの参照として使用する。
フェイス画像をBODY Geometryの代替として使用してはならない。
