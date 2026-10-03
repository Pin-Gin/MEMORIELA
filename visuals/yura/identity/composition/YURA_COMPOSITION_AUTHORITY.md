# YURA COMPOSITION AUTHORITY

Status: **AUTHOR-APPROVED / ACTIVE**

Purpose: YURA全身生成時のキャンバス寸法・人物占有率・上下余白・中央配置を固定するComposition Authority。

この文書は、顔Identity・BODY Geometry・体格・衣装・レンダリングを変更するAuthorityではない。

## Canvas

生成キャンバスは以下を基準とする。

- width: **1440 px**
- height: **2560 px**
- aspect ratio: **9:16**

**TARGET CANVAS = 1440 × 2560 px**

他の解像度で内部生成・変換される場合でも、最終Compositionは9:16の同等比率として扱う。
キャンバス比率の変更を理由に、YURAの顔Identity・BODY Geometry・頭身を変更してはならない。

## Figure occupancy

頭頂から足裏までの人物全高は、キャンバス高の **89%** をTARGETとする。

**TARGET FIGURE HEIGHT = 89% of canvas height**
**ACCEPTABLE RANGE = 88–90%**

1440×2560の場合:

- target figure height = **2278.4 px**
- practical target ≈ **2278 px**
- acceptable range = **2253–2304 px**

人物全高は、髪先ではなく **頭頂から足裏まで** で測定する。
髪が頭頂より上へ装飾的に突出した場合でも、その突出を頭身計算の基準にしない。

## Vertical margins

頭頂上の余白と足裏下の余白は、各 **5–6%** を基準とする。

**TOP MARGIN TARGET = 5–6%**
**BOTTOM MARGIN TARGET = 5–6%**

1440×2560の場合:

- 5% = **128 px**
- 5.5% = **140.8 px**
- 6% = **153.6 px**

標準配置では、上余白・下余白とも約 **141 px** を中心値とする。
人物を上端または下端へ寄せない。
頭頂・足裏をキャンバス端へ接触させない。

## Horizontal centering

人物の身体中心軸をキャンバス水平中央へ一致させる。

1440 px幅の場合:

**CENTER AXIS X = 720 px**

左右余白は概ね均等とする。
人物を横方向へ移動させて余白を片側へ偏らせない。
画面を埋めるために人物幅を拡大しない。

## Authority separation

Composition Authorityは以下のみを規定する。

- canvas width / height
- aspect ratio
- figure occupancy
- top margin
- bottom margin
- horizontal center placement

Composition Authorityは以下を変更するAuthorityではない。

- 顔Identity
- 顔内部Geometry
- 7.2頭身
- 頭部とBODYの内部相対比率
- 肩幅
- 胸郭幅
- 腰幅
- 四肢長
- 四肢太さ
- 胸部形状
- 髪型Identity
- 耳Identity
- 衣装
- レンダリング

**COMPOSITION -> FACE_IDENTITY = DENIED**
**COMPOSITION -> BODY_GEOMETRY = DENIED**
**COMPOSITION -> BODY_WIDTH = DENIED**
**COMPOSITION -> HEAD_TO_BODY_RATIO = DENIED**

全身を89%へ収める際は、人物全体を一体として均等に配置・スケールする。
頭部だけ、BODYだけ、胴だけ、脚だけを個別に拡大・縮小して占有率へ合わせてはならない。

**CANVAS SCALE DOES NOT CHANGE BODY GEOMETRY.**
**COMPOSITION DOES NOT CHANGE HEAD-TO-BODY RATIO.**

## Relationship with BODY Geometry Authority

BODY Geometry Authority:
- `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`
- `visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md`

BODY Geometry Authorityは **7.2頭身と人物内部Geometry** を規定する。
Composition Authorityは **その7.2頭身の人物をキャンバス内のどこに、どの大きさで配置するか** のみを規定する。

`YURA_BODY_GEOMETRY_GUIDE.png` 自体のキャンバスは **1200×1600** だが、この1200×1600というキャンバス寸法・3:4比率・余白・人物画面占有率は、本番YURA生成のComposition Authorityではない。

**BODY_GEOMETRY_GUIDE_CANVAS -> PRODUCTION_COMPOSITION = DENIED**
**BODY_GEOMETRY_GUIDE_CANVAS_OCCUPANCY -> PRODUCTION_COMPOSITION = DENIED**

ガイド画像から使用してよいのは、承認済みの7.2頭身・人物内部Geometryのみ。
本番のキャンバスと余白は、この `YURA_COMPOSITION_AUTHORITY.md` に従う。

## Relationship with Face Identity Authority

Face Identity Authority:
- `visuals/yura/identity/face/YURA_FACE_REFERENCE.png`
- `visuals/yura/identity/face/FACE_REFERENCE_RULES.md`

フェイスアップ画像のキャンバス寸法・トリミング・頭部画面占有率・余白を、本番Compositionへ持ち込まない。

**FACE_REFERENCE_CANVAS -> PRODUCTION_COMPOSITION = DENIED**
**FACE_REFERENCE_CROP -> PRODUCTION_COMPOSITION = DENIED**

## QA

全身Master候補では最低限、以下を確認する。

- canvas aspect ratio = **9:16**
- target canvas = **1440×2560 px**
- figure height = **88–90%**, target **89%**
- top margin = **5–6%**
- bottom margin = **5–6%**
- body center axis = **horizontal center**
- head-to-body ratio remains **7.1–7.3**, target **7.2**

Composition条件を満たすためにBODY Geometryが変化した場合はFAILとする。

**COMPOSITION QA FAIL -> MASTER_PROMOTION = NO**
