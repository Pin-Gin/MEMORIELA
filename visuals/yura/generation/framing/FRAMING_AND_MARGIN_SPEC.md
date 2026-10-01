# YURA Framing & Margin Spec

Status: **PROTECTED GENERATION SPECIFICATION / CURRENT FRAMING DOMAIN OWNER**
Current Revision: **v1.0**
Adopted: 2026-09-13
Updated: 2026-09-17 — protected Profile A–E size system linked
Character: 久遠ゆら / YURA
Purpose: YURA画像生成におけるアスペクト比、人物占有率、余白、用途別Quiet Zoneを固定し、キャンバスや用途変更によってBODY比率・頭身・人物形状が変化することを防ぐ。

Parent authority:

`visuals/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`

BODY authority:

- `visuals/yura/identity/body/BODY_MASTER.md`
- `visuals/yura/identity/body/BODY_SPEC.md`

Protected operational size-profile sub-spec:

`visuals/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md`

This file owns **framing / margin / quiet-zone behavior**. It never owns BODY geometry.
`visuals/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md` narrows this domain into named Profile A–E use cases and must not contradict this parent specification.

---

## 1. Core principle

Default rule:

**通常生成の余白は極小。**

ただし「極小」はゼロ余白を意味しない。
髪・頭頂・手足・衣装端・重要な小物が意図せず切れないための、必要最小限の安全余白は残す。

余白そのものに用途がある場合のみ、その用途を生成条件として明示し、必要な余白を確保する。

Examples:

- smartphone wallpaper
- SNS / X asset
- Web / UI placement
- title / text placement
- composition that intentionally requires negative space

---

## 2. BODY invariance under framing changes — absolute

余白・キャンバス・アスペクト比・人物占有率を変更しても、YURAのBODYは変更しない。

Protected behavior:

- 153 cm concept remains unchanged
- exact 7.25-head design ratio remains unchanged
- head / torso / pelvis / limbs keep the same relative scale
- limb thickness does not change
- shoulder / ribcage / waist / pelvis relationships do not change
- hair core geometry does not change merely to fit the canvas

If additional negative space is required:

**scale the entire character uniformly and/or translate the entire character inside the canvas.**

Never:

- shrink only the head
- lengthen / shorten only the legs
- compress the torso
- thin the arms / legs
- alter BODY widths to create room
- distort YURA to fit a target aspect ratio

Framing adaptation is a **layout operation, not a BODY redesign**.

---

## 3. Baseline aspect-ratio profiles

Detailed named operational profiles are defined in:

`visuals/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md`

Current routing:

- **Profile A — MASTER / Full-Body Validation** → 9:16 portrait
- **Profile B — Standard Full-Body Derivative** → 9:16 portrait
- **Profile C — Smartphone Wallpaper** → target device ratio first; 9:19.5 fallback; upper ~15–25% Quiet Zone
- **Profile D — X Thumbnail / SNS Thumbnail** → 16:9 landscape default; explicit user ratio overrides the default
- **Profile E — Background / Room / Environment Only** → 16:9 landscape

The profile default ratio is a routing default, not permission to ignore an explicit user target ratio or special placement.

Unless the current request specifies another target:

### 3.1 Full-body / standing YURA asset

- baseline aspect ratio: **9:16 portrait**
- default margin behavior: **minimal safe margin**
- full-body request: preserve head top through toes without accidental clipping

### 3.2 Room / background asset

- baseline aspect ratio: **16:9 landscape**
- room geometry / camera continuity follows formally adopted Background authority when available; pre-formalization material under `creation/background/reference-materials/` is reference-only

### 3.3 Event CG / special one-image illustration

- baseline aspect ratio: **16:9** unless the scene / UI / user request clearly requires portrait or another composition
- composition may override the baseline ratio, but never protected BODY geometry

These are layout defaults, not identity rules.

---

## 4. Normal generation margin profile

For ordinary YURA generation without a special output-use instruction:

- margin = **minimal safe margin**
- make effective use of the canvas
- avoid unnecessary large empty areas
- do not crowd hair, head, hands, feet, clothing edges, or important props against the crop boundary
- if the requested composition is full-body, preserve complete full-body visibility
- if the requested composition is bust-up / half-body / close-up, crop according to the requested shot rather than pretending to preserve full-body margins

No fixed percentage is imposed for normal minimal margins; composition determines the smallest safe margin.

---

## 5. Smartphone wallpaper profile — protected

Operational name: **Profile C**.
Detailed routing/default ratio follows `visuals/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md`.

Trigger examples:

`スマホ用の画像生成をお願い`

`機種：○○`

When the user requests a smartphone wallpaper and provides a device model:

1. use the target device's screen aspect ratio / resolution as the composition target when reliably available;
2. if the exact device specification cannot be confirmed, use user-provided dimensions or the protected 9:19.5 fallback where appropriate;
3. preserve YURA CANON LOCK and BODY invariants;
4. reserve the **upper approximately 15–25% of the canvas as a comparatively quiet visual zone**.

### 5.1 Smartphone upper Quiet Zone

The upper 15–25% is not required to be blank.
It should be visually quiet enough to coexist with clock / status / notification UI.

Prefer in this zone:

- simple sky / wall / soft room background
- low-detail gradients within the protected rendering grammar
- low-information environmental shapes
- restrained contrast

Avoid placing in this zone when practical:

- YURA's face / eyes
- important hand gestures
- key props
- important text-like shapes
- highly detailed decorations
- strong high-contrast focal points

The exact percentage inside the 15–25% range may be chosen to suit the specific device ratio and composition.

### 5.2 Smartphone scaling behavior

If extra upper space is needed:

- move YURA lower in the frame and/or
- uniformly scale the whole character smaller

Do not alter BODY proportions to create wallpaper space.

---

## 6. X thumbnail profile — protected

Operational name: **Profile D**.
Detailed routing/default ratio follows `visuals/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md`.

Trigger example:

`X用サムネの画像生成をお願い`

Default behavior:

- default logical ratio for an ordinary X / SNS thumbnail = **16:9 landscape**
- apply the normal **minimal safe margin** rule
- do not add large empty margins merely because the asset is for X
- preserve YURA at a strong readable scale
- if the user explicitly requests another ratio such as **1:1**, use that explicit ratio while keeping Profile D readability / margin behavior

If the user specifically requests a different X placement type such as:

- profile icon / avatar
- header / banner
- post image with planned text overlay

then that explicit use case may require its own crop / safe-zone behavior.
Do not silently treat every `X用サムネ` request as a circular profile icon or header.

---

## 7. Use-case-specific margin rule

General rule:

**余白そのものに用途がある場合だけ、その用途を生成条件として明示する。**

Examples:

- `上部を空けて` → increase upper negative space
- `右側にUIを置く` → reserve right-side quiet zone
- `左側にタイトルを置く` → reserve left-side low-information area
- `スマホ壁紙` → Profile C / smartphone behavior
- `X用サムネ` → Profile D behavior unless another target is explicit

When a use-case margin is applied:

- preserve all protected identity domains
- adjust whole-character scale / position only
- do not compensate by changing anatomy

---

## 8. Native generation-size limitation

If the image-generation engine cannot directly output the exact requested pixel dimensions or device ratio:

1. choose the nearest supported canvas / aspect ratio that preserves the intended composition;
2. preserve the required quiet zone and important visual placement;
3. normalize later through non-distorting crop / padding / export when needed;
4. never stretch or squash YURA to match the final dimensions.

The logical asset standard and the generator's native output size are allowed to differ.

---

## 9. Relationship to generation compile order

This specification and its Profile A–E sub-spec are applied inside:

**Block D — CAMERA / LAYOUT**

from `visuals/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`.

Compile order remains:

1. CANON LOCK
2. derivative design
3. physical pose structure
4. camera / layout — **select/apply the relevant Profile A–E and this framing / margin authority here**
5. reference isolation
6. negative / anti-drift constraints

Do not move margin logic ahead of CANON LOCK.

---

## 10. QA interpretation

Framing / margin / size-profile failures are derivative-production failures, not automatic identity failures.

Examples:

- Profile A full-body validation clips feet → derivative / layout failure
- Profile C smartphone wallpaper lacks the required upper Quiet Zone → derivative / layout failure
- Profile D X thumbnail contains unnecessary large dead space → derivative / layout failure
- creating extra margin by lengthening YURA's legs → BODY failure **and** layout failure

Correction rule:

Preserve CANON LOCK and fix the framing / margin / selected profile domain only whenever possible.

---

## 11. Change control

This specification is PROTECTED.

Do not silently change:

- default margin = minimal safe margin
- BODY-safe adaptation = uniform whole-character scale / translation only
- Profile A / B full-body baseline = 9:16 portrait
- Profile C smartphone device-ratio priority + 9:19.5 fallback + upper approximately 15–25% Quiet Zone
- Profile D ordinary X / SNS thumbnail default = 16:9 while explicit user ratio may override
- Profile E background / room baseline = 16:9 landscape
- prohibition on anatomy distortion for layout

Material revisions require explicit user approval and Git logging.
