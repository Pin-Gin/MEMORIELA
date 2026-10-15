# YURA HEAD / EAR STRUCTURE — VIEW 01 FRONT CANDIDATE

Status: **AUTHOR-APPROVED / VIEW 01 STRUCTURE CANDIDATE / NOT FINAL MASTER / NOT ACTIVE VISUAL AUTHORITY**

## 1. Scope

この記録は、YURA Head / Face / Ear構造化工程の

`VIEW 01 = FRONT`

に対する作者承認済みStructure Candidateを記録する。

これは最終Face-up Masterではない。

また、髪を外したことで新たに露出した頭頂・頭蓋外周を、測定済み普遍事実として扱わない。

## 2. Source image identity

Source image filename in validation session:

`ChatGPT Image 2026年10月14日 22_58_22.png`

Image size:

`1268 x 1240 px`

SHA256:

`b22323612af19ff6731292a4d601fbf7c5949f8dad5b11ee3082365c162deaae`

このSHA256は、作者が承認したVIEW 01候補画像の同一性確認用とする。

## 3. Source / Authority separation

### MASTER-DERIVED

顔Identityは以下から維持したものとして評価する。

`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

対象：

- face shape
- facial proportions
- eyes
- eyebrows
- nose
- mouth
- cheeks
- chin
- jaw contour
- facial center-line
- expression identity

### AUTHOR OVERRIDE

耳Actual Geometryの現行条件：

```text
EAR ACTUAL HEIGHT TARGET
= 20–22% of face vertical

HARD MAX
= 23% of face vertical
```

このAUTHOR OVERRIDEの正式分母は `face vertical` である。

今回のVIEW 01画像上では、髪を外した構造Candidateの診断値として `crown → chin` の `head vertical` も別途計測する。
この診断値を正式な `face vertical` 条件と同一視しない。

### TEST / HYPOTHESIS

髪を外したことで新たに露出した以下は、現段階では構造仮説である。

- scalp contour
- crown contour
- temple surface
- side-head contour

これらをMEASURED_MASTER_FACTとして扱わない。

## 4. Image-space measurement

計測は生成画像上の可視輪郭を使用する。
アンチエイリアスおよび耳付け根の読み取りに数px程度の不確実性を含む。

### Head vertical — construction diagnostic only

```text
CROWN Y ≈ 28 px
CHIN Y ≈ 837 px
HEAD VERTICAL ≈ 809 px
```

この `HEAD VERTICAL` はVIEW 01構造Candidate上の診断分母であり、正式な `face vertical` の代替定義ではない。

### Ear actual vertical span

可視輪郭の変曲点を耳上端・下端の構造境界として読み取った。

```text
IMAGE-LEFT EAR
≈ 168 px
≈ 20.8% of HEAD vertical

IMAGE-RIGHT EAR
≈ 167 px
≈ 20.6% of HEAD vertical
```

結果：

```text
LEFT / RIGHT HEIGHT CONSISTENCY = PASS
VERTICAL COMPACTNESS = PASS
```

左右耳高の計測差は約1 px、約0.6%であり、構造上の大きな左右差は確認されない。

重要：

```text
20.8% / 20.6% of HEAD vertical
!=
formal 20–22% of FACE vertical test
```

したがって、このhead-vertical診断値だけを根拠に正式TARGET / HARD MAXの数値PASSを主張しない。
正式条件との整合は、耳が縦長化していないこと、左右Actual Geometryが安定していること、作者承認を含む総合構造評価として保持する。

### Horizontal face balance

両眼の主要暗部中心から求めた中点：

```text
EYE PAIR MIDPOINT X ≈ 636.1 px
IMAGE CENTER X = 634.0 px
OFFSET ≈ +2.1 px
```

正面中心線の大きな横ズレは確認されない。

### Reference-preserved vertical asymmetry check

現行Face Referenceには左右眼のごく小さな高さ差が存在する。
正規化した左右眼高さ差は、

```text
FACE REFERENCE ≈ 2.57% of reference head vertical
VIEW 01 CANDIDATE ≈ 2.39% of candidate head vertical
```

であり、左右差を機械的に消す方向への大きな再設計は確認されない。

## 5. Visual evaluation

```text
FACE IDENTITY MATCH
= PASS

FACE PROPORTION
= PASS

HAIR REMOVAL
= PASS

HEAD CONTOUR
= PLAUSIBLE CANDIDATE

LEFT EAR ACTUAL GEOMETRY
= PASS

RIGHT EAR ACTUAL GEOMETRY
= PASS

EAR VERTICAL COMPACTNESS
= PASS

LEFT / RIGHT EAR CONSISTENCY
= PASS

EAR OUTWARD PROJECTION
= NONE TO MILD

EAR LOBE ELONGATION
= NONE
```

## 6. Author decision

作者判断により、この画像を

```text
YURA HEAD / EAR STRUCTURE
VIEW 01 — FRONT
```

の正式なStructure Candidateとして採用する。

ただし：

```text
VIEW 01 CANDIDATE
!= FINAL FACE-UP MASTER
!= PERMANENT HEAD 3D FACT
```

である。

非正面Geometryは、今後のProfile / 3/4 / Rear構築と作者確認を経て確定する。

## 7. Qualification

```text
YURA HEAD / EAR STRUCTURE
VIEW 01 — FRONT:
QUALIFY
```

## 8. Next intended phase

VIEW 01 Candidateを頭部基礎として、次にHair Structureを分離生成し、

```text
HEAD / FACE / EAR
+
HAIR STRUCTURE
```

の接続検証を行う。

髪生成時に、Head / Face / Ear Geometryを髪へ合わせて変形してはならない。
