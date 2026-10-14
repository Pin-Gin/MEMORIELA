# YURA HEAD / EAR STRUCTURE PLAN

Status: **DRAFT / CONSTRUCTION PLAN / NOT VISUAL AUTHORITY**

## 1. 目的

この文書は、YURAの最終Face-up Masterを完成させるための一時的なHead / Face / Ear構造化工程を定義する。

目的は以下。

- 髪に隠されている頭部構造を作業上分離する
- Face Identityを維持したまま耳の実形状を確定する
- 正面だけではなく複数角度で頭部と耳の整合を確認する
- 後工程でHair Structureを同じ頭部へ被せられる基礎を作る
- 最終Face-up Master完成後は、通常生成入力から構造資料を外す

基本思想：

```text
MASTER
= final visible truth

STRUCTURE
= temporary construction / validation support

VISUAL TEXT
= identity-preserving supplemental specification
```

構造資料そのものを、永久的な通常生成Authorityにすることを目的としない。

## 2. 最終ワークフロー

```text
CURRENT FACE-UP MASTER / FACE REFERENCE
        ↓
HEAD + FACE + EAR STRUCTURE CANDIDATES
        ↓
MULTI-VIEW AUTHOR VALIDATION
        ↓
APPROVED HEAD / EAR CONSTRUCTION
        ↓
HAIR STRUCTURE CONSTRUCTION
        ↓
HEAD + EAR + HAIR INTEGRATION
        ↓
NEW FACE-UP MASTER CANDIDATE
        ↓
AUTHOR APPROVAL
        ↓
FINAL FACE-UP MASTER
```

最終Face-up Master完成後の通常生成は、必要最小限の入力へ戻す。

```text
NORMAL GENERATION
=
FACE-UP MASTER
+ VISUAL MASTER when needed
+ YURA_VISUAL_TEXT.md
+ relevant PART VISUAL TEXT only when necessary
```

Head / Ear構造画像は通常生成では原則使用しない。

## 3. 構造化工程中のAuthority境界

### FACE IDENTITY / FRONT FACE GEOMETRY

Authority:

`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

Controls:

- face shape
- facial proportions
- eye size
- eye shape
- eye spacing
- eye placement
- eyebrows
- nose
- mouth
- cheeks
- chin
- jaw contour
- facial center-line
- overall YURA face identity

### EAR ACTUAL GEOMETRY TEST CONDITION

Source:

`visuals/yura/identity/ears/YURA_EAR_STRUCTURE.md`

Current status:

```text
DRAFT / FREEZE CANDIDATE
```

このファイルは構造検証条件として使用できるが、現段階では永久的なActive Authorityではない。

### GENERAL APPEARANCE SUPPORT

Source:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

### HAIR

Head / Ear構造化の初期段階では、最終Hair Geometryを対象外とする。

現行Face Reference内の髪は、既存Face Identityや遮蔽位置を確認する補助としてのみ扱う。

現行Referenceに見える耳の長さ・露出・突出を、髪と一体の正解として保存してはならない。

## 4. 重要な認識境界

現行Face Referenceは2Dの正面画像である。

したがって：

```text
VISIBLE FRONT FACE GEOMETRY
= authoritative within existing Face scope

HIDDEN CRANIAL GEOMETRY
= NOT DIRECTLY MEASURED

SIDE / REAR HEAD GEOMETRY
= CONSTRUCTION HYPOTHESIS until author-approved
```

現行Face Referenceから直接見えない以下を、測定済み事実として扱わない。

- 後頭部深度
- 側頭部深度
- 頭蓋の背面形状
- 隠れた耳付け根の3D形状
- 頭頂から後頭部への立体曲面

生成された非正面ビューは、作者承認前はすべて：

```text
STRUCTURE CANDIDATE
```

とする。

見えない3D形状を生成AIが作っただけで、事実へ昇格させない。

## 5. 構造化対象

構造化対象は：

```text
HEAD CORE
+ FACE
+ BOTH EARS
+ NECK CONNECTION
```

最終髪型は含めない。

### Hairless の意味

この工程での「髪なし」は、以下を外した一時的な構造表現を指す。

- bangs
- face-framing strands
- side hair
- rear hair mass
- ponytail / braid / hair accessory
- hairstyle silhouette

これはYURAを坊主キャラクターとして再設計するものではない。

目的は構造を見える状態にすることだけである。

## 6. 髪を外したことで露出する頭部表面

髪を外すと、現行Face Referenceでは直接確認できない領域が露出する。

以下は初期段階では：

```text
TEST / HYPOTHESIS
```

として扱う。

- scalp contour
- crown contour
- temple surface
- side-head contour
- rear-head contour

生成された頭部輪郭は、作者承認前に固定しない。

## 7. Face Identity維持ルール

髪を外すことを、顔再設計の許可にしない。

変更禁止：

- 顔の縦横比
- 目の大きさ
- 目の形
- 目の間隔
- 目の縦位置
- 眉
- 鼻
- 口
- 頬
- jaw
- chin
- midface length
- lower-face length
- expression identity

髪なし化によってYURAの承認済みFace Identityが変わった場合：

```text
CANDIDATE = FAIL
```

頭部や耳がもっともらしくてもFAILとする。

## 8. EAR ACTUAL GEOMETRY

髪なしHead / Ear構造化では、Hair Occlusionの影響を外して：

```text
EAR ACTUAL GEOMETRY
```

を確認する。

現行の構造候補条件：

```text
EAR ACTUAL HEIGHT TARGET
= 20–22% of face vertical

HARD MAX
= 23%
```

耳は以下を満たす。

- vertically compact
- short upper-to-lower span
- close to side of head
- non-protruding
- non-pointed
- no long earlobe

「小さい耳」を：

```text
narrow but vertically tall
```

として解釈しない。

## 9. 左右実耳の構造条件

Head / Ear構造化段階では、左耳と右耳の基礎Actual Geometryは同一を初期条件とする。

```text
LEFT EAR ACTUAL GEOMETRY
≈
RIGHT EAR ACTUAL GEOMETRY
```

目的：

- 生成側の左右差による逃げ道を減らす
- 耳本体の左右差とHair Occlusionによる可視差を分離する
- 左右の構造比較を可能にする

これは人間の生体が完全左右対称であるという主張ではない。

最終的な可視差は：

```text
HAIR OCCLUSION
CAMERA VIEW
POSE
```

によって生じてもよい。

## 10. Ear placement

現行配置候補：

- upper attachment region ≈ eye-line region
- lower attachment / lower-limit region ≈ lower-nose region
- outer upper limit should not materially exceed eyebrow region

これらは配置ランドマークであり、耳がその縦区間全体を埋める指示ではない。

ランドマークとCompact Heightが競合する場合：

```text
COMPACT EAR HEIGHT WINS
```

ランドマークを接続するために耳を縦へ伸ばさない。

## 11. 髪なし構造Viewと最終Face-up Viewの分離

以下を同一視しない。

```text
HAIRLESS STRUCTURE VIEW
```

と：

```text
FINAL HAIRED FACE-UP VIEW
```

髪なし構造段階では：

- Actual Ear全体が見えてよい
- 耳全体が見えるのはGeometry確認のため意図的
- Hair Occlusion Ruleは適用しない

最終Hair適用後のFace-upでは：

- visible ear may be fragmentary or zero
- Hair Occlusionを適用する
- VISIBLE / OCCLUSIONを別に評価する

したがって：

```text
HAIRLESS FULL EAR VISIBILITY
!=
FINAL FACE-UP FULL EAR VISIBILITY
```

髪なし構造画像の耳全露出を、最終Face-up Masterへ持ち込まない。

## 12. 必要Multi-view

全角度を最初から一度に確定しない。

1ビューずつ生成・検証・作者承認して進める。

### Stage A — Front structural baseline

```text
VIEW 01 = FRONT
```

目的：

- 承認済みFace Identity維持
- hairstyle dependency除去
- 左右耳Actual Geometry確立
- 暫定Head Contour確立

最重要Anchor Viewとする。

### Stage B — Profile views

```text
VIEW 02 = LEFT PROFILE
VIEW 03 = RIGHT PROFILE
```

目的：

- head depth候補確認
- ear projection確認
- ear attachment確認
- forehead / nose / chin projection consistency確認
- 左右構造drift検出

作者承認前はHypothesisである。

### Stage C — Front three-quarter views

```text
VIEW 04 = FRONT 3/4 LEFT
VIEW 05 = FRONT 3/4 RIGHT
```

目的：

- front identityとprofile geometryの接続
- cheek / jaw transition確認
- ear placement in depth確認
- 回転してもYURA Face Identityが維持されるか確認

### Stage D — Rear construction

Front / Profile / Front 3/4安定後にのみ進む。

```text
VIEW 06 = REAR 3/4 LEFT
VIEW 07 = REAR 3/4 RIGHT
VIEW 08 = BACK
```

目的：

- rear-head construction candidate確立
- earとrear headの関係確認
- 後のrear-hair constructionの基礎作成

Back Geometryを先に生成して、その形にFront Faceを後から合わせない。

## 13. ONE VIEW / ONE IMAGE / ONE REVIEW

初期構造生成では：

```text
ONE VIEW
ONE IMAGE
ONE REVIEW
```

を原則とする。

最初から1枚のMulti-view turnaround sheetを生成しない。

理由：

- 1つの誤Viewが他Viewを汚染する
- PanelごとにFace Identityが変わる可能性がある
- どのView起因のエラーか追跡しにくい
- 未承認のHidden Geometryが他Viewへ伝播しやすい

各View承認後にのみ、統合Structure Sheet作成を検討する。

## 14. View inheritance rule

新しいViewは、承認済みUpstream Structureのみを継承する。

推奨順：

```text
APPROVED FRONT
    ↓
PROFILE CANDIDATES
    ↓
APPROVED PROFILES
    ↓
FRONT 3/4 CANDIDATES
    ↓
APPROVED FRONT 3/4
    ↓
REAR 3/4
    ↓
BACK
```

未承認CandidateをDownstreamの正解に使用しない。

## 15. Rendering during construction

構造化工程はRendering再設計テストではない。

YURA Identityを正しく判断できる、clean / neutral / high-quality 2D anime presentationを使用する。

禁止：

- photorealism
- semi-realistic human portrait
- 3D CGI look
- dramatic lighting
- heavy texture
- geometry認識を変えるstyle shift

Default Rendering Baselineは別文書として独立管理できる。

Head / Ear構造作業を使って、Renderingを勝手に再定義しない。

## 16. 構造CandidateのComposition

推奨Default：

```text
single head / upper neck
plain white background
eye-level camera
neutral expression
upright head
no tilt
no perspective exaggeration
consistent approximate scale between views
```

衣装詳細は不要。

首・肩の終端を自然に処理するための最小限のみ許可する。

これはFashion / Full-body Testではない。

## 17. Candidate評価区分

各Viewを独立評価する。

### FACE IDENTITY

```text
PASS
SOFT FAIL
FAIL
```

### HEAD CONSTRUCTION

```text
PLAUSIBLE CANDIDATE
REVISION REQUIRED
REJECT
```

### EAR ACTUAL GEOMETRY

```text
PASS
BORDERLINE
FAIL
```

### LEFT / RIGHT STRUCTURAL CONSISTENCY

```text
PASS
MINOR DIFFERENCE
FAIL
```

### SOURCE STATUS

承認する各要素に、以下のどれかを明示する。

```text
MASTER-DERIVED
AUTHOR OVERRIDE
AUTHOR-APPROVED CONSTRUCTION
TEST / HYPOTHESIS
```

これらを混同しない。

## 18. Failure conditions

以下はFAIL：

- Face Identity materially changes
- eye geometry changes
- facial proportions change
- jaw / chin identity changes
- ear remains long / vertically stretched
- left/right actual ears diverge without deliberate author decision
- ear height reduction is compensated by excessive width
- ear is pushed outward
- profile becomes a different character
- rear geometry forces front-face redesign
- generated hidden geometry is treated as fact without review
- later view contradicts already-approved upstream geometry

## 19. Promotion model

Individual Structure Imageは：

```text
CANDIDATE ONLY
```

から始める。

作者承認後のみ：

```text
AUTHOR-APPROVED CONSTRUCTION REFERENCE
```

へ昇格する。

承認されたStructure Viewは、即座にFace-up Masterを置換しない。

十分なMulti-view Consistency確認後にのみ、統合Head / Ear Construction SetをMaster再構築用資料としてFreezeできる。

## 20. Hair Structureへの引き渡し

Head / Face / Ear Constructionが十分安定した後：

```text
HEAD / EAR STRUCTURE
        ↓
HAIR STRUCTURE CONSTRUCTION
```

へ進む。

Hairは承認済みHead Substrateに合わせる。

```text
HAIR FITS THE HEAD
```

を原則とし、髪型に合わせるためHead Geometryを歪めない。

Hair Structureで扱う候補：

- hairline / part interface
- crown origin
- bangs
- face-framing strands
- side mass
- rear mass
- ear occlusion
- neck / shoulder overlap
- rear silhouette
- tip region

Hair Structureは別Phaseとして扱う。

## 21. Final Face-up Master再構築

構造化完了後：

```text
FINAL FACE-UP MASTER CANDIDATE
=
APPROVED FACE IDENTITY
+ APPROVED HEAD / EAR CONSTRUCTION
+ APPROVED STANDARD HAIR CONSTRUCTION
+ APPROVED RENDERING BASELINE
```

を作る。

その後、作者Reviewを行う。

## 22. 通常Runtimeからの退役

Final Face-up Masterが作者承認された後、Head / Ear Construction資料はGitに残す。

用途：

```text
AUDIT
REVISION
REBUILD
MULTI-VIEW DEVELOPMENT
```

ただし通常生成入力からは原則外す。

通常生成は必要最小限を優先する。

例：

```text
FACE-UP MASTER
+ YURA_VISUAL_TEXT.md
```

必要時のみRelevant Part Visual Textを追加する。

通常生成でConstruction Document一式を毎回読ませない。

## 23. Core principle

```text
STRUCTURE EXISTS TO BUILD THE MASTER.

THE MASTER DOES NOT EXIST TO FORCE
EVERY FUTURE GENERATION TO RE-READ THE STRUCTURE.
```

最終状態は：

```text
STRONGER MASTER
+ SIMPLER RUNTIME
```

とする。
