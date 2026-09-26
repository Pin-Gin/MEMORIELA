# YURA Hair Arrangement Guideline

Status: **ACTIVE DERIVATIVE HAIR-ARRANGEMENT GUIDELINE / NOT A HAIR CORE OWNER**
Created: 2026-09-13
Updated: 2026-09-19 — Strong Braided Half-Up specialized routing added
Character: 久遠ゆら / YURA
Purpose: ポニーテール、ローシニヨン、ハーフアップ、団子、編み込み等の派生髪型を、既存画像のトレースに依存せず、結び位置・毛流れ・総毛量・重力・カメラ投影から安定生成する。

## 0. Authority / role

This file does **not** redefine YURA's protected HAIR core.

Current protected HAIR core authority:

- `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md`

Normal generation must not recover superseded HAIR rules from Git history.


This guideline owns only arrangement topology and physical behavior:

- anatomical gather / tie / knot / braid position
- gathered vs loose sections
- root-flow convergence
- tail / bun / braid structure
- wrapping / folding / tucking
- gravity and collision behavior
- camera projection / visibility

It never changes the v1.3 core:

- silver-white color
- super-long source length
- slightly-above-standard total hair mass
- fine / soft strands
- restrained lateral spread
- bangs / face-framing layers
- gravity-dominant behavior
- FACE / BODY / RENDERING

## 1. Provenance / no-tracing

Hairstyle references may be used only to extract generic construction principles such as tie height, sectioning, convergence, wrapping, gravity, and camera projection.

Do not trace or reproduce a source image's exact silhouette, line routing, artist-specific stylization, or decorative details.
Generate the arrangement from written geometry + YURA's protected specifications.

## 2. Core physical rule — anatomy first, camera second

**The tie / gather point is defined in head-body coordinates, not by what the camera wants to show.**

- default ponytail = centered rear midline
- default low chignon = centered rear midline at lower occipital / nape
- side ponytail / side chignon = only when explicitly requested
- front camera may hide the tie / bun completely
- invisibility is valid and must not trigger lateral relocation
- perspective changes visibility, never anatomical attachment

General anti-drift rule:

**Do not move a rear hairstyle to the left / right merely to make it readable from the front.**

## 3. Root convergence

Gathered hair must physically converge toward the specified gather point.

- upper / side / back hair gradually flows toward one tie or knot
- do not attach a separate tail or bun to otherwise unchanged loose hair
- do not create disconnected hair masses
- preserve soft natural tension; YURA's hair is not rigid or shellacked
- protected bangs and designated face-framing strands remain outside unless explicitly changed

## 4. Total-hair-mass conservation — mandatory

Changing arrangement never reduces YURA's source hair length or total hair mass.

Formal v1.3 source properties remain active in every arrangement:

1. total mass = slightly above standard
2. strands = fine and soft
3. upper hair settles under the weight of the length
4. middle / back retains sufficient density
5. lateral spread remains restrained
6. tips taper lightly and delicately
7. fine strands do not mean sparse total hair
8. ponytail / chignon / half-up must not silently delete hair mass

When hair is gathered, the source super-long length is represented by the resulting tail length or by credible internal wrapping / folding / overlap.

## 5. Ponytail definitions

### 5.1 High ponytail

Tie point:
- upper rear head / upper occipital area
- clearly above ear horizontal
- rear centerline

Physics:
- roots rise toward tie
- small initial upward / backward lift allowed
- long heavy tail then settles downward under gravity

### 5.2 Mid ponytail — standard / normal position

`通常位置` / `標準位置` means **Mid Ponytail** unless the user specifies otherwise.

Tie point:
- middle occipital / rear center
- approximately ear height to slightly above
- centered on rear midline

Physics:
- modest outward arc immediately after tie is acceptable
- most of the super-long tail then falls downward behind the back
- do not convert it into high ponytail merely for visibility

### 5.3 Low ponytail

Tie point:
- lower occipital / nape
- base of skull / upper neck
- rear centerline

Physics:
- minimal upward lift
- tail falls close to neck / back
- strongly gravity-dominant
- may contact body, clothing, chair, sofa, etc.

## 6. Ponytail camera projection

### Front
- tie may be fully hidden
- tail originates behind the head / neck, never cheek or side skull
- only naturally projected portions need be visible
- **unseen portions do not need to be artificially exposed**
- never side-shift the ponytail merely to show it

### 3/4
- anatomical tie remains centered
- apparent side offset may occur only from perspective

### Side
- tie height should clearly distinguish high / mid / low

### Back
- root convergence and continuous tail origin must be readable

## 7. Low chignon / ローシニヨン

Protected specialized implementation:
`docs/assistant-context/creation/yura/identity/hair/styles/LOW_CHIGNON_SPEC.md`

When the user requests ordinary `ローシニヨン` / `low chignon` / `full low chignon`, apply that protected sub-spec in addition to this general arrangement guideline.

### 7.1 Default position

YURA `ローシニヨン` means:

- centered rear midline
- lower occipital / nape
- close to base of skull / upper neck
- not lateral unless explicitly requested as `side low chignon`

### 7.2 Full-gather topology — mandatory

For a normal full low chignon:

- all long side / back hair converges into the low rear center
- protected bangs and intended face-framing strands remain outside
- only minimal incidental wisps outside the face-framing area are allowed
- all other super-long back hair is wrapped / twisted / folded / tucked into the chignon
- extra source length is stored through internal wrapping / folding, not deletion

**Do not leave long back hair hanging from the chignon.**

Unless an explicit hybrid / partially untucked style is requested, visible unrequested full-length back strands below the chignon are an arrangement failure.

### 7.3 Bun size / mass

- soft, compact-to-moderate bun
- enough volume to credibly contain the slightly-above-standard super-long source mass
- not an implausibly tiny bun
- not an oversized fantasy sphere
- fine hair may compress, but source length / mass does not vanish

### 7.4 Front-view visibility — protected arrangement behavior

For a centered low chignon viewed from the front:

- the chignon may be almost completely or completely hidden behind the head / neck
- this is **correct**, not a visibility failure
- a small natural edge may appear beside the neck depending perspective and bun volume
- do not shift the bun beside an ear to show the hairstyle
- do not leave long loose hair merely to signal that YURA originally has long hair

Rule:

**Build the low chignon physically at the rear-center nape first, then project it into the camera. Never place it according to front-camera readability.**

### 7.5 QA cue

For a normal front-facing low chignon:

- mostly hidden / tiny natural edge = PASS
- clearly lateralized bun for visibility = FAIL
- unrequested long back hair hanging below bun = FAIL
- face-framing strands preserved = PASS

## 8. Half-up family

A half-up gathers **only the upper section** while the lower section remains loose.

Default:
- gather roughly from above ear line / upper sides
- lower back-hair mass remains substantial
- never reduce lower hair to a thin sheet

### Simple half-up
- upper section to centered rear tie
- lower super-long section remains loose

### Braided / twisted half-up
- upper side sections braid / twist continuously toward centered rear gathering
- `編み込み強め` means clearly readable braid structure in the gathered upper section
- lower hair remains the full loose source mass appropriate to a half-up
- braid complexity must not erase YURA's bangs / face framing

### Strong Braided Half-Up — protected specialized routing

When the request includes `ハーフアップ + 編み込み強め`, `ハーフアップ＋編み込み強め`, `強めの編み込みハーフアップ`, `髪型：ハーフアップ ＋ 編み込み強め`, or `Strong Braided Half-Up`, apply:

`docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/SPEC.md`

Current visual MASTER for this arrangement:
`docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/VISUAL_MASTER.md` / gen_id `0336bd46-16bf-4d17-823b-73d6204cba31`

That sub-spec fixes:
- source Super-Long length limits
- no lower-section mass inflation
- no luxury-through-length / width / mass
- braid complexity + restrained ornament as the luxury mechanism
- rear-center physical construction
- no camera / pose / outfit visibility compensation

A simple `ハーフアップ` request alone does not automatically trigger that specialized sub-spec.

### Half-up bun
- only gathered upper section forms bun
- bun volume corresponds to that section only
- lower super-long hair remains loose

## 9. Collision / contact

Hair is flexible physical mass.

- shoulder → drape over / behind / beside according to actual ordering
- back → rest / slide along back
- collar → locally bunch / redirect
- chair / sofa → locally compress / spread
- raised arm → pass in front / behind according to pose
- low chignon + collar/headrest → local compression only; do not relocate whole bun

Avoid clipping, detached tails/buns, unexplained sharp bends, teleporting from center to side, or random left/right swaps.

## 10. Neutral arrangement defaults

Unless explicitly overridden:

- down style = protected v1.3 super-long
- ponytail = centered rear **Mid Ponytail / standard position** when user says only `ポニーテール` or `通常位置`
- low ponytail = centered nape
- high ponytail = upper rear center
- low chignon = centered rear nape
- half-up = upper section only, centered rear
- hair ornament = none unless requested
- loose wisps = minimal / natural beyond protected face-framing strands

## 11. Generation compile order

For an arrangement request:

1. `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md` core
2. arrangement family
3. exact anatomical gather position
4. gathered vs loose sections
5. root convergence
6. resulting tail / bun / braid mass
7. wrapping / folding / tucking if needed
8. gravity
9. body / clothing / furniture collision
10. camera projection
11. anti-drift constraints

**Do not start from how much of the hairstyle should be visible to the camera. Start from its physical construction.**

## 12. Reusable generation cues

### Mid ponytail / standard position

`銀白色の正式スーパーロングを、後頭部中央の中程度の高さ、耳の高さ前後〜わずかに上で一つに結ぶ。側頭部・後頭部の髪は結び目へ自然に収束し、結び目直後のごく自然な外向きの弧の後、十分な毛量を保った長い毛束が重力に従って背中側へ落ちる。結び位置は左右へずらさない。正面から見えない結び目や毛束部分は無理に見せなくてよい。`

### Low ponytail

`銀白色の正式スーパーロングを、後頭部正中のうなじ付近で低く一つに結ぶ。結び目は側面ではなく後頭部中央に固定し、長い毛束は首の後ろから背中側へ重力に沿って落ちる。正面で結び目が隠れてよく、見せるために左右へ移動させない。`

### Full low chignon / front camera

`銀白色の正式スーパーロングを、後頭部正中・うなじ中央の低い位置へ集めたフルローシニヨン。前髪と指定された顔まわりの毛だけを残し、それ以外の長い後ろ髪はすべてシニヨン内部へ巻き込み、折り込み、収納する。シニヨンから長い後ろ髪を垂らさず、顔まわり以外の後れ毛は最小限。正面ではシニヨンがほぼまたは完全に隠れてよい。髪型を見せるために左右へ移動させない。`

## 13. Change control

This guideline is active and protected as an arrangement guideline.

Do not silently change:

- anatomical tie-position principle
- `standard ponytail = Mid Ponytail`
- front-view invisibility acceptance
- prohibition on lateral relocation for readability
- total-hair-mass conservation
- low-chignon full containment
- protected face-framing preservation

Core HAIR values remain owned only by `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md`.
