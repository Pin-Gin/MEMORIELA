# YURA FACE REFERENCE RULES

Status: **PREPARED / IMAGE PENDING**

予定画像:
`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

この画像は、作者がローカル同期後に手動追加する。
画像が存在するまでは、FACE IMAGE AUTHORITY = NONE とする。

## Authority scope

YURA_FACE_REFERENCE.png が存在し、作者が承認した後、この画像は以下のみのAuthorityとする。

- 顔Identity
- 顔の縦横比
- 目の大きさ・形・間隔
- 眉・鼻・口の相対位置
- 中顔面・下顔面の比率
- 頬・顎の形状
- 顔まわりの髪・前髪のIdentity
- 顔付近で確認可能な耳の見え方

## Explicitly denied authority

この画像は以下のAuthorityではない。

- 全身頭身
- BODYサイズ
- 身長感
- 肩幅
- 胸郭幅
- 胴長
- 腰幅
- 脚長
- 四肢比率
- 全身キャンバス占有率
- 全身構図
- 全身ポーズ
- 服装

**FACE_REFERENCE -> BODY_PROPORTION = DENIED**
**FACE_REFERENCE -> FULL_BODY_SCALE = DENIED**
**FACE_REFERENCE -> CANVAS_OCCUPANCY = DENIED**

フェイスアップ画像のピクセル寸法、トリミング、余白、画面内の頭部サイズを、全身生成時の頭部サイズへ直接変換してはならない。

## Face lock

FACE GEOMETRY IS LOCKED.

全身生成時も、顔Identityを7.2頭身へ合わせるために再設計しない。
顔を面長化しない。
顔を横長化しない。
目・眉・鼻・口を個別に再配置しない。

BODY Geometryとの整合は、顔Identityを変更するのではなく、BODY Geometry Guide側の全身配置で解決する。

## Missing guide fail-safe

BODY Geometry Guideが存在しない場合、このフェイス画像をBODY Geometryの代替として使用してはならない。

FACE REFERENCE CONTROLS IDENTITY, NOT FULL-BODY SCALE.
