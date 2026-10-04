# YURA BODY GEOMETRY GUIDE

Status: **AUTHOR-APPROVED / ACTIVE**

Authority image:
`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

この文書は、YURAの全身比率を7.2頭身で固定するためのBODY Geometry Authority定義である。
GitHub `main` 上のガイド画像は、作者承認済み候補画像と同一であることを確認済み。

**BODY GEOMETRY IMAGE AUTHORITY = ACTIVE**

## Active guide

作者承認済みAuthority画像:
- dimensions: **1200 × 1600 px**
- format: **PNG / RGBA**
- SHA-256: **da18dbd7a8cdc9c3659f83ca8970349c18923bd4b4e29bcedf1f1b8cb1e7e379**
- Git blob SHA: **63f5a6496afac5a142e63a7b329cc7d0ffc3c6b7**

実測基準:
- crown / 0.0: y = 160 px
- chin / 1.0: y = 340 px
- 1 head = 180 px
- soles / 7.2: y = 1456 px
- (1456 - 160) / 180 = **7.2 heads**

このAuthority画像と異なるファイルを、同名だからという理由だけでAuthorityへ昇格させてはならない。
画像を差し替える場合は、再検証・作者承認・ハッシュ更新を必須とする。

## Target geometry

全身は **7.2頭身** をTARGETとする。

頭頂から顎先までの頭部高を1.0とした場合、頭頂から足裏までを7.2とする。

**TARGET = 7.2 heads**
**ACCEPTABLE RANGE = 7.1〜7.3 heads**

## Authority scope

`YURA_BODY_GEOMETRY_GUIDE.png` は以下のみのAuthorityとする。

- 頭部と全身の相対スケール
- 7.2頭身の分割位置
- 肩・胸郭・腰・骨盤・股・膝・足首などの縦方向配置
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

作者意図として、全身バランスは **骨盤／股位置がやや高めで、下半身がわずかに長く見える方向** を採用する。
日本語で「座高がやや低い印象」と表現してよいが、立位全身生成での実運用定義は以下とする。

- 顎から股までの上半身スパンを不必要に長くしない
- 胸郭から腰・骨盤までのtorso spanをコンパクトに保つ
- 腰位置を不自然に低くしない
- 骨盤／股位置をわずかに高めに保つ
- 股から足裏までの下半身をわずかに長く見せる
- 膝位置は自然に保つ
- 下半身を長く見せるために脚だけを機械的に伸ばさない
- 上半身を短く見せるために胸郭・腹部を不自然に圧縮しない

**UPPER BODY MUST NOT BE VERTICALLY ELONGATED.**
**TORSO MUST BE COMPACT; DO NOT LENGTHEN THE RIBCAGE-TO-PELVIS OR WAIST SPAN.**
**KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.**
**LOW SITTING-HEIGHT IMPRESSION = RELATIVELY COMPACT UPPER-BODY SPAN + SLIGHTLY LONGER LOWER BODY.**
**DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.**

この「下半身がわずかに長い」は、7.2頭身という全体比率の中での内部配分であり、モデル体型のような極端な長脚化を意味しない。
BODY Geometry Guideの人物内部ランドマーク配置を優先し、自然なシルエットを保持する。

フェイスアップ画像のキャンバス内サイズ、トリミング、余白、頭部の画面占有率をBODY Geometryへ持ち込まない。

DO NOT INFER BODY PROPORTION FROM FACE REFERENCE CROP OR SCALE.
DO NOT USE FACE REFERENCE CANVAS OCCUPANCY AS BODY GEOMETRY.
DO NOT CREATE A TALL MODEL-LIKE BODY TO SATISFY 7.2 HEADS.

## Author-approved inseam proxy target

YURAの立位Body Geometry QAでは、画像上の股下比率proxyを以下で定義する。

```text
inseam_proxy_ratio = (soles_y - crotch_y) / (soles_y - crown_y)
```

これは実身長・実寸股下の測定ではなく、正面立位RAW画像上での **crotch-to-soles / crown-to-soles の画像空間proxy** である。

作者承認済みのYURA用運用値:

- **PASS TARGET = 46.0%〜46.5%**
- **MODEL-LIKE HARD GUARD = 47.0%以上はFAIL**
- 46.5%超〜47.0%未満もYURAのPASS TARGET外なのでFAILとする

この値は一般人体の普遍的基準としてではなく、YURAの「座高がやや低い印象」「骨盤位置やや高め」「下半身がわずかに長い」という作者意図を再現するためのキャラクター固有Body Geometry QA値として扱う。

**YURA INSEAM PROXY TARGET = 46.0–46.5%.**
**47.0% OR MORE IS FORBIDDEN AS TOO MODEL-LIKE.**

## Torso-specific numeric gate

総頭身とinseam proxyを同時に満たすとき、`chin→crotch` のtorso spanは次式で追跡する。

```text
chin_to_crotch_heads
= ((crotch_y - chin_y) / (chin_y - crown_y))
```

7.1〜7.3頭身かつinseam proxy 46.0〜46.5%という承認済み範囲から導かれるtorso envelopeは概ね:

- **chin→crotch = 2.7985〜2.9420 heads**

これは新しい独立した体型値を発明したものではなく、承認済みの総頭身範囲とinseam proxy範囲から数学的に導かれる監査用envelopeである。

- `chin_to_crotch_heads > 2.9420` は胴／上半身が長すぎるためFAIL
- `chin_to_crotch_heads < 2.7985` は上半身を不自然に圧縮している可能性があるためFAIL
- 数値範囲内でも、胸郭・腰・骨盤配置が不自然なら視覚QAでFAILできる

**TORSO-SPECIFIC GATE = COMPACT TORSO + HIGHER PELVIS + YURA INSEAM PROXY PASS.**

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
- inseam proxy ratio >= 47.0% = hard FAIL
- chin→crotch torso envelope = 2.7985–2.9420 heads

追加の内部ランドマーク値は、上半身の間延び・骨盤位置・下半身配分・膝位置を追跡するために記録する。

以下はBody Geometry PASSの追加条件とする。

- torsoがコンパクトで、胸郭→腰→骨盤が縦に間延びしていないことを作者が確認
- 腰位置が不自然に低くないことを作者が確認
- 骨盤／股位置がやや高めで、下半身がわずかに長い意図を満たすことを作者が確認
- 膝位置が自然で、脚だけを伸ばした形になっていないことを作者が確認

これらの確認結果と実測ランドマーク値は `body_geometry_qa.json` に残す。
膝位置など、まだ作者承認済みの絶対数値閾値が固定されていない項目については、AIが勝手に閾値を発明してはならない。

## Face identity preservation

BODY Geometry調整時も、顔Identityは `YURA_FACE_REFERENCE.png` と `YURA_VISUAL_TEXT.md` に従う。
BODY Geometry Guideは、顔内部を変更して頭身を成立させてはならない。

FACE SHAPE MUST REMAIN IDENTICAL IN PROPORTION.
BODY GEOMETRY GUIDE CONTROLS PROPORTION, NOT FACE IDENTITY.

## Guide image requirement

全身Master候補を作る際は、ACTIVEな `YURA_BODY_GEOMETRY_GUIDE.png` を7.2頭身のGeometry参照として使用する。
フェイス画像をBODY Geometryの代替として使用してはならない。
