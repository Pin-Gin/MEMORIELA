# YURA EAR STRUCTURE

Status: **DRAFT / FREEZE CANDIDATE / NOT ACTIVE AUTHORITY**

## 1. Purpose

この文書は、現行YURA Face Referenceに残る既知の長耳問題を、
顔Identityを変更せずに修正するための耳構造候補仕様である。

この段階ではまだ正式Authorityへ昇格しない。

耳について、以下の3要素を必ず分離して扱う。

```text
A. EAR ACTUAL GEOMETRY
B. EAR VISIBLE GEOMETRY
C. HAIR OCCLUSION
```

耳そのもののサイズと、
画面上で見えている耳の量と、
髪による遮蔽を混同してはならない。

目的は、

- 耳の可視性を理由とした縦方向の長大化
- 耳の外側への突出
- 耳を見せるための髪操作
- 耳を隠すための髪Identity変更

を防止することである。

## 2. Authority boundary

現在の検証段階では以下の役割分離を使用する。

```text
FACE IDENTITY / FACE GEOMETRY
= visuals/yura/identity/face/YURA_FACE_REFERENCE.png

EAR STRUCTURE CANDIDATE
= this file

CURRENT FACE REFERENCE EAR GEOMETRY
= KNOWN DEFECT / NOT TARGET
```

現行Face Referenceから以下を継承してはならない。

- ear height
- ear vertical elongation
- ear projection
- ear exposure
- ear prominence

現行Face Referenceの可視ピクセルから、
髪で隠れている耳の3D形状を逆算してはならない。

## 3. Source-status separation

### AUTHOR OVERRIDE — CURRENT FIXED CONDITION

```text
EAR ACTUAL HEIGHT TARGET
= 20–22% of face vertical

HARD MAX
= 23% of face vertical
```

この値は現段階のAUTHOR OVERRIDEとして扱う。

測定済み普遍値ではない。

### STRUCTURAL RULES

- 耳は縦方向にコンパクトである。
- 「小さい耳」を、細いだけで縦長の耳として解釈しない。
- 耳は頭部側面に近く沿う。
- 外側へ張り出さない。
- 可視性より耳本体の自然なサイズを優先する。
- 髪による部分遮蔽・完全遮蔽を許可する。
- 正面では耳が完全に見えなくても正常とする。

## 4. Terminology — face-framing side strand

この文書内の

`FACE-FRAMING SIDE STRAND`

は、

YURAの顔の左右に自然に落ちる既存の顔脇毛束を指す。

これは一般的な「もみあげ」という人体部位名称ではなく、
YURAの既存Hair Identityを構成する顔脇の毛束である。

この毛束の、

- 基本位置
- 太さ
- 本数
- 流れ
- 顔との距離感
- 全体Hair Identity

を、耳の可視性調整のために再設計してはならない。

# 5. A — EAR ACTUAL GEOMETRY

`EAR ACTUAL GEOMETRY` は、
髪で隠れている部分を含む、本来存在する耳全体を指す。

## Height

```text
TARGET = 20–22% of face vertical
HARD MAX = 23%
```

この比率は耳本体の推定全高に適用する。

画面上で見えている部分だけに適用しない。

## Vertical compactness

耳は、

- short vertically
- compact
- low-prominence

を基本とする。

禁止：

```text
narrow-but-tall ear
vertically stretched ear
long earlobe
elongated lower ear
elongated upper ear
```

耳の高さを減らした結果として、
横幅を大きくして補償してはならない。

## Placement landmarks

耳の付け根の上側は、
おおむね目の高さ付近を基準とする。

耳の付け根の下側は、
おおむね鼻下付近を基準とする。

耳全体の上端は、
眉付近を大きく越えないことを目安とする。

ただし、これらは位置のガイドであり、

```text
眉付近
↓
鼻下付近
```

の領域全体を耳で埋める指示ではない。

配置ランドマークを接続するために
耳を縦方向へ伸ばしてはならない。

ランドマークとコンパクトな耳高が競合する場合：

```text
COMPACT EAR HEIGHT WINS.
```

## Projection / orientation

耳は頭部側面に沿わせる。

禁止：

- outward flare
- outward displacement
- camera-facing rotation
- front-facing rotation
- hair mass outside projection

耳を認識しやすくするために、
耳を頭部シルエットから外へ出してはならない。

# 6. B — EAR VISIBLE GEOMETRY

`EAR VISIBLE GEOMETRY` は、
Hair Occlusion適用後にそのカメラ視点から実際に見える耳部分のみを指す。

```text
EAR ACTUAL GEOMETRY
!=
EAR VISIBLE GEOMETRY
```

この2つを同一視してはならない。

## Front-view primary rule

正面視では、耳は視覚的特徴として読ませない。

```text
FULL EAR OUTLINE REQUIRED = NO

PARTIAL VISIBILITY = ACCEPTABLE

VERY SMALL VISIBLE FRAGMENT = ACCEPTABLE

ZERO VISIBLE EAR = ACCEPTABLE

LEFT / RIGHT EQUAL VISIBILITY = NOT REQUIRED
```

## Front-view visibility topology

正面視では、耳は

`FACE-FRAMING SIDE STRAND`

より前方または顔中央側へ露出してはならない。

耳が見える場合でも、

顔脇毛束の後方・外側から
ごく小さな局所断片だけが見える状態を基本とする。

### Required topology

正面視では：

```text
EAR IN FRONT OF FACE-FRAMING SIDE STRAND
= FORBIDDEN

EAR MEDIAL TO FACE-FRAMING SIDE STRAND
= FORBIDDEN

COMPLETE OUTER EAR CONTOUR
= FORBIDDEN

EAR TOP AND EAR BOTTOM BOTH CLEARLY VISIBLE
= FORBIDDEN

CONTINUOUS VERTICAL EAR SILHOUETTE
= FORBIDDEN
```

耳の上端と下端を同時に見せない。

耳の外周全体を連続した線として見せない。

目付近から鼻下付近まで、
一本の連続した耳シルエットを成立させない。

## Visible fragment rule

耳が見える場合は、

```text
small local fragment
broken contour
partial visibility
```

を許容する。

耳が存在することを視聴者へ説明するために、
耳の輪郭を完成させてはならない。

見える耳部分から、
完全な耳形状が容易に読み取れる必要はない。

## Readability prohibition

正面視では、

```text
EAR READABILITY
```

を生成目的にしない。

禁止：

- 耳を認識させるために上下端を見せる
- 耳を認識させるために輪郭を連続させる
- 耳を認識させるために縦方向へ露出量を増やす
- 耳を認識させるために外側へ移動する

耳が読みにくい場合：

```text
KEEP IT UNREADABLE OR HIDE IT.
```

可視性不足は失敗ではない。

# 7. C — HAIR OCCLUSION

Hair Occlusionは、
自然な耳Geometryを維持した結果として耳が見えにくくなることを許容するための構造である。

耳を隠すために髪型そのものを作り直す規則ではない。

## Allowed

- 既存のface-framing hairが耳へ重なってよい。
- 耳上部を隠してよい。
- 耳下部を隠してよい。
- 耳全体を隠してよい。
- 左右の遮蔽量が違ってよい。
- 正面では両耳とも完全不可視でもよい。

## Face-framing side strand ordering

正面視の基本レイヤー順は、

```text
CAMERA
↓
FACE-FRAMING SIDE STRAND
↓
EAR
↓
SIDE / REAR HAIR MASS
```

とする。

つまり、耳は既存の顔脇毛束の奥側に存在してよい。

耳を顔脇毛束より前へ出して
「耳がある」と説明する必要はない。

## Hair Identity lock

耳を隠す目的でも、
既存のHair Identityを変更してはならない。

禁止：

```text
make face-framing side strand wider
move side strand toward face center
increase number of side strands
make side strand artificially thicker
press hair unnaturally against face
redesign local hair flow
```

耳を見せるためにも、
耳を隠すためにも、
Hair Identityを再設計しない。

## Forbidden visibility compensation

耳を見せるために：

- 髪を耳の後ろへ送らない。
- 耳周囲だけ人工的な隙間を開けない。
- 顔脇毛束を細くしない。
- 顔脇毛束を分離しない。
- 髪を外側へ扇状に広げない。
- 耳を髪の外へ押し出さない。
- 耳をカメラ方向へ回転させない。

# 8. CROSS-LAYER NO-COMPENSATION RULE

以下の問題を別要素で補償してはならない。

## Ear too difficult to see

禁止：

```text
increase ear height
increase ear width
move ear outward
rotate ear toward camera
clear hair
```

正解：

```text
ALLOW PARTIAL OR ZERO VISIBILITY
```

## Ear becomes hidden

これは失敗ではない。

耳を再露出させない。

## Compact ear does not reach both placement landmarks

耳を伸ばさない。

```text
COMPACT HEIGHT WINS.
```

## Hair naturally covers the ear

その状態を維持する。

## Occlusion seems asymmetric

左右対称化のために耳や髪を移動しない。

# 9. Corrected Face Master edit contract

将来の耳修正Candidateは、
現行の作者承認済みFace Referenceを基準にする。

## MUST NOT CHANGE

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
- expression identity
- hair color
- bangs identity
- face-framing hair identity
- global hair silhouette
- rendering style
- line quality
- color character

## MAY CHANGE

- ear vertical height
- ear upper extent
- ear lower extent
- ear local projection
- ear visible amount
- minimum local ear/hair overlap necessary to satisfy the fixed layer ordering

ただし、

`minimum local ear/hair overlap`

はHair Identityの再設計を許可するものではない。

# 10. Target front-view state

正面Face Masterにおける優先結果：

```text
FACE IDENTITY
= unchanged

EAR ACTUAL GEOMETRY
= short / compact

EAR PROJECTION
= close to side of head

EAR VISIBLE GEOMETRY
= minimal / fragmented / zero

EAR TOP + BOTTOM BOTH VISIBLE
= no

COMPLETE EAR OUTLINE
= no

EAR IN FRONT OF FACE-FRAMING SIDE STRAND
= no

HAIR IDENTITY
= unchanged

LONG-EAR DEFECT
= removed
```

正面では、

耳が見えないことより、
耳を長く見せることの方を明確な失敗とする。

# 11. Failure conditions

FAIL if any of the following occurs:

- 耳が明確に縦長に見える
- 実耳がTARGET / HARD MAXを超える
- 耳の上端と下端が正面から同時に明瞭に見える
- 耳外周が連続して読める
- 耳がface-framing side strandより顔中央側へ露出する
- 耳が髪より前へ押し出される
- 高さを短くした代償として耳が太くなる
- 高さを短くした代償として耳が外側へ張り出す
- 耳可視性のために髪が移動する
- 耳遮蔽のためにHair Identityが変更される
- 顔Identityが変わる
- 目・口・顎・輪郭が変わる
- global hair identityが変わる

# 12. View scope

この強いVisibility Topology Lockは、

```text
STRAIGHT FRONT VIEW
```

を対象とする。

3/4 view、side view、rear 3/4 viewについては、
正面用遮蔽規則をそのまま機械的に流用しない。

それらは正面耳構造が確定した後、
別View ruleとして検証する。

# 13. Freeze rule

この文書は現在、

```text
DRAFT / FREEZE CANDIDATE
```

である。

作者確認前にACTIVE Authorityへ昇格しない。

作者承認後にのみ、

```text
AUTHOR-APPROVED / ACTIVE EAR STRUCTURE AUTHORITY
```

へ変更する。

その後、
Face-up Master + Visual Text + Ear Structure
を使った耳修正検証へ進む。
