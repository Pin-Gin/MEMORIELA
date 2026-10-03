# YURA BODY GEOMETRY GUIDE

Status: **PREPARED / GUIDE IMAGE PENDING**

予定画像:
`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

この文書は、YURAの全身比率を7.2頭身で固定するためのBODY Geometry Authority定義である。
ガイド画像が存在するまでは、BODY GEOMETRY IMAGE AUTHORITY = NONE とする。

## Target geometry

全身は **7.2頭身** をTARGETとする。

頭頂から顎先までの頭部高を1.0とした場合、頭頂から足裏までを7.2とする。

**TARGET = 7.2 heads**
**ACCEPTABLE RANGE = 7.1〜7.3 heads**

## Authority scope

YURA_BODY_GEOMETRY_GUIDE.png が存在し、作者が承認した後、この画像は以下のみのAuthorityとする。

- 頭部と全身の相対スケール
- 7.2頭身の分割位置
- 肩・胸郭・腰・膝・足首などの縦方向配置
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

フェイスアップ画像のキャンバス内サイズ、トリミング、余白、頭部の画面占有率をBODY Geometryへ持ち込まない。

DO NOT INFER BODY PROPORTION FROM FACE REFERENCE CROP OR SCALE.
DO NOT USE FACE REFERENCE CANVAS OCCUPANCY AS BODY GEOMETRY.
DO NOT CREATE A TALL MODEL-LIKE BODY TO SATISFY 7.2 HEADS.

## Face identity preservation

BODY Geometry調整時も、顔Identityは `YURA_FACE_REFERENCE.png` と `YURA_VISUAL_TEXT.md` に従う。
BODY Geometry Guideは、顔内部を変更して頭身を成立させてはならない。

FACE SHAPE MUST REMAIN IDENTICAL IN PROPORTION.
BODY GEOMETRY GUIDE CONTROLS PROPORTION, NOT FACE IDENTITY.

## Guide image requirement

全身Master候補を作る際は、BODY Geometry Guide画像が存在する場合、その画像を7.2頭身のGeometry参照として使用する。
BODY Geometry Guide画像が存在しない場合、フェイス画像を代替Geometryとして使用してはならない。
