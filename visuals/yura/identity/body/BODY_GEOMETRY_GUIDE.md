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
- 骨盤／股位置をわずかに高めに保つ
- 股から足裏までの下半身をわずかに長く見せる
- 膝位置は自然に保つ
- 下半身を長く見せるために脚だけを機械的に伸ばさない
- 上半身を短く見せるために胸郭・腹部を不自然に圧縮しない

**UPPER BODY MUST NOT BE VERTICALLY ELONGATED.**
**KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.**
**LOW SITTING-HEIGHT IMPRESSION = RELATIVELY COMPACT UPPER-BODY SPAN + SLIGHTLY LONGER LOWER BODY.**
**DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.**

この「下半身がわずかに長い」は、7.2頭身という全体比率の中での内部配分であり、モデル体型のような極端な長脚化を意味しない。
BODY Geometry Guideの人物内部ランドマーク配置を優先し、自然なシルエットを保持する。

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

追加の内部ランドマーク値は、上半身の間延び・骨盤位置・下半身配分・膝位置を追跡するために記録する。
現時点では、Authority画像に対して作者承認済みの数値閾値がまだ固定されていない内部ランドマークについて、AIが勝手に絶対閾値を発明してはならない。

内部ランドマークの数値閾値を固定するまでは、以下をBody Geometry PASSの追加条件とする。

- 上半身が縦に長く見えないことを作者が確認
- 骨盤／股位置がやや高めで、下半身がわずかに長い意図を満たすことを作者が確認
- 膝位置が自然で、脚だけを伸ばした形になっていないことを作者が確認

これらの確認結果と実測ランドマーク値は `body_geometry_qa.json` に残す。
将来、作者承認済みの良好な基準値が確定した時点で、その値を数値QA閾値として別途固定してよい。

## Face identity preservation

BODY Geometry調整時も、顔Identityは `YURA_FACE_REFERENCE.png` と `YURA_VISUAL_TEXT.md` に従う。
BODY Geometry Guideは、顔内部を変更して頭身を成立させてはならない。

FACE SHAPE MUST REMAIN IDENTICAL IN PROPORTION.
BODY GEOMETRY GUIDE CONTROLS PROPORTION, NOT FACE IDENTITY.

## Guide image requirement

全身Master候補を作る際は、ACTIVEな `YURA_BODY_GEOMETRY_GUIDE.png` を7.2頭身のGeometry参照として使用する。
フェイス画像をBODY Geometryの代替として使用してはならない。
