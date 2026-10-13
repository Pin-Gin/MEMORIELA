# YURA FACE REFERENCE RULES

Status: **AUTHOR-APPROVED / ACTIVE**

Active image:
`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

Git blob SHA:
`4c96c4ec42f996807248be1aff60ec8a090fd570`

この画像は作者承認済みのYURA Face Identity Referenceである。
**FACE IMAGE AUTHORITY = ACTIVE**

## Authority scope

`YURA_FACE_REFERENCE.png` は以下のみのAuthorityとする。

- 顔Identity
- 顔の縦横比
- 目の大きさ・形・間隔
- 眉・鼻・口の相対位置
- 中顔面・下顔面の比率
- 頬・顎の形状
- 顔まわりの髪・前髪のIdentity

## Ear exception / current known defect

現行Face Referenceの耳は、縦方向の長さ・露出・存在感について既知の欠陥を持つ。
そのため、現行Face Referenceは耳のGeometry・可視性・存在感のAuthorityとして使用しない。

現在の耳Authorityは以下とする。

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

**FACE_REFERENCE -> EAR_GEOMETRY = DENIED**
**FACE_REFERENCE -> EAR_HEIGHT = DENIED**
**FACE_REFERENCE -> EAR_VISIBILITY = DENIED**
**FACE_REFERENCE -> EAR_PROMINENCE = DENIED**

顔IdentityをReferenceへ合わせる場合でも、Reference内の耳の縦寸法・突出・露出をコピーしてはならない。
耳はVisual Textのサイズ・配置・遮蔽・非補償規則を優先する。

## Explicitly denied authority

この画像は以下のAuthorityではない。

- 耳の縦寸法・実形状
- 耳の突出量
- 耳の可視量・露出
- 耳の存在感
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

Face Referenceが入力として与えられた場合、顔Geometry・内部比率・顔IdentityはReferenceを優先する。
ただし、このFace lockは耳Geometry・耳可視性・耳存在感には適用しない。

BODY Geometryとの整合は、顔Identityを変更するのではなく、BODY Geometry Guide側の全身配置で解決する。

## Missing guide fail-safe

BODY Geometry Guideが存在しない場合、このフェイス画像をBODY Geometryの代替として使用してはならない。

FACE REFERENCE CONTROLS IDENTITY, NOT FULL-BODY SCALE.
FACE REFERENCE DOES NOT CONTROL CURRENT EAR GEOMETRY.
