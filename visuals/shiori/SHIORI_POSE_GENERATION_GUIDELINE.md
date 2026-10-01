# 一ノ瀬 栞 Pose Generation Guideline

Status: **PROTECTED / MANDATORY**

Purpose: 一ノ瀬栞の動的ポーズ生成時に、Visual Master / Visual Text のBODY・FACE・EYES・GLASSES・HAIRを維持したまま、ひねり・座り・しゃがみ・前後屈・大きな動きによる再解釈を防ぐ。

Authority:
- `visuals/shiori/SHIORI_VISUAL_MASTER.png`
- `visuals/shiori/SHIORI_VISUAL_MASTER.md`
- `visuals/shiori/SHIORI_VISUAL_TEXT.md`
- `visuals/CHARACTER_RENDERING_STYLE.md`

---

## 1. Trigger

Neutral standing baselineを超える意味のある動きを含む場合、本書を必ず適用する。

Examples:
- torso twist
- 3/4 turn
- side-oriented pose
- seated pose
- squat / crouch
- kneeling
- forward bend / backward lean
- strong lateral lean
- reaching
- dynamic stepping / walking / running
- furniture contact / support pose
- other poses with material joint / weight / perspective change

---

## 2. Identity Lock

ポーズによって以下を変更しない。

- FACE identity
- pale blue-gray eyes with faint lavender component
- thin dark navy-to-black glasses
- blue-black hair
- 168 cm scale concept
- exact 7.5-head BODY system
- shoulder width
- ribcage scale
- bust volume / relationship to frame
- waist width
- pelvis / hip scale
- baseline arm thickness
- baseline thigh / calf proportions
- overall leg length

Pose is a derivative layer and does not authorize character redesign.

---

## 3. Skeleton Transform Only

ポーズ変更は主に以下で表現する。

- position
- rotation
- joint angle
- relative segment orientation
- center-of-mass shift
- support / contact

Applicable segments:
- head
- neck
- shoulders
- upper arms
- forearms
- torso
- pelvis
- thighs
- lower legs
- feet

各部位のcanonicalな長さ・幅・基礎体積を、ポーズ成立のために変更しない。

---

## 4. Pose Reference = pose only

Unity / 3D mannequin / PoseMy.Art / Daz / OpenPose / depth / normal 等を使用する場合、参照してよいのは:

- joint placement
- skeletal orientation
- center of gravity
- support / contact points
- load direction
- camera position / angle / perspective

参照してはいけないもの:

- reference model face
- BODY proportions
- bust / waist / pelvis
- limb thickness
- hair / hair color
- glasses
- clothing
- material / lighting
- rendering style

栞のidentityは必ず Shiori Visual Master / Visual Text が支配する。

---

## 5. Perspective Lock

BODYとは別にcameraを解決する。

Before generation, resolve:
- camera height
- camera distance
- viewing direction
- focal-length / perspective character
- pitch / yaw / roll when relevant

Do not shorten / thicken limbs merely to fill the frame.
Do not use BODY deformation as a substitute for perspective.

---

## 6. Foreshortening ≠ BODY change

投影による見え方の変化をBODY redesignとして扱わない。

- limb toward camera may appear shorter, but segment length is unchanged
- near hand / foot may project larger, but base anatomy is unchanged
- squat / crouch must not inflate thighs / calves
- perspective compression must not rewrite shoulders / ribcage / pelvis

---

## 7. Torso Twist / 3/4 / Side Lock

ひねり・3/4・側面では:

- shoulder and pelvis orientation may rotate
- ribcage width / depth relationship remains stable
- waist width remains stable
- pelvis scale remains stable
- bust volume remains stable

栞の胸部は体格比でかなり豊かで、半球型を基準とする。

**正面から見える面積が減少しても実体積を縮小しない。**
**胸部をcamera方向へ平坦化せず、側面方向の奥行き・前方投影として保持する。**
**片側が奥へ回る場合は消失させず、重なり・遠近・遮蔽として表現する。**

Do not:
- shrink bust volume because less frontal area is visible
- widen ribcage to support bust
- flatten bust for side view
- make one side disappear unnaturally

---

## 8. Seated / Squat / Kneeling Lock

Allowed:
- plausible soft-tissue compression at contact points
- plausible thigh / hip contact deformation
- clothing fold / compression changes
- perspective-driven overlap

Not allowed:
- pelvis redesign
- hip-width redesign
- permanent thigh / calf thickening
- shortening legs to simplify pose
- changing the 7.5-head BODY relationship
- altering bust / ribcage geometry to fit a seated posture

Separate **contact deformation** from **BODY redesign**.

---

## 9. Hair Conservation

Pose may move Shiori's hair through:

- gravity
- body contact
- furniture contact
- local flow
- overlap / occlusion

But preserve:

- blue-black identity
- default source length
- principal ends below chest to above waist
- longest strands approaching waist only
- source total hair mass
- standard-to-slightly-above-standard volume
- fine / soft strand character
- mild natural wave

Do not:
- shorten hair because seated
- extend main mass below waist
- remove hair mass to expose BODY
- route most hair unnaturally to the front during a bend

---

## 10. Glasses Conservation

Glasses remain part of Shiori's default identity during dynamic poses.

Preserve:
- thin dark navy-to-black frame
- horizontal soft-square to oval shape
- moderate scale
- readable eyes through lenses

Head tilt / perspective may change projected shape, but must not:
- make frames thick / oversized
- remove glasses without instruction
- turn them into round fashion frames
- use heavy reflection unless explicitly requested

---

## 11. Rendering Last

Resolve in this order:

1. Shiori Identity / BODY
2. skeleton pose
3. camera / perspective
4. support / contact / load
5. hair physical placement
6. glasses projection
7. outfit physical response
8. **Matte Natural Anime rendering**

Rendering describes the resolved structure. It does not reinterpret anatomy.

---

## 12. Dynamic Pose QA

Evaluate independently:

### DP-1 Identity
- face
- eye color
- glasses
- hair color / identity

### DP-2 BODY geometry
- 7.5-head system
- shoulder / ribcage / waist / pelvis
- leg length
- limb thickness
- bust-to-frame relationship

### DP-3 Joint / skeleton
- plausible joint directions
- no impossible elbow / knee / wrist / ankle / neck configuration
- apparent shortening explained by projection

### DP-4 Support / contact / load
- coherent support points
- local contact compression only
- no unexplained hidden-limb load

### DP-5 Bust continuity
PASS only if:
- twist / 3/4 / side keeps actual bust volume
- front-area reduction is represented through projection
- side depth / forward projection remains
- far-side breast is represented by overlap / occlusion rather than deletion

### DP-6 Hair conservation
- protected source length / mass maintained
- no pose-driven shortening / overextension

### DP-7 Camera / perspective
- projected size changes explained by perspective
- no anatomy distortion to fit frame

### DP-8 Limb / hand / foot artifacts
FAIL on:
- extra / missing limb
- impossible duplication
- broken hand / foot attachment
- severe structural artifact

---

## 13. Core rule

**動的ポーズでは栞のBODYを再設計せず、固定された栞BODYを関節回転・重心移動・接触変形だけでポーズさせる。**

This rule is mandatory for all significant-motion Shiori generations.

---

## 14. Change control

This guideline is PROTECTED.

Do not alter BODY / FACE / EYES / GLASSES / HAIR / Rendering canon to fit a failed pose.
Retry the pose / camera / contact layer instead.
