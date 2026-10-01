# YURA Image Size Profile Spec

Status: **PROTECTED OPERATIONAL SUB-SPECIFICATION**
Current Revision: **v1.0**
Adopted: 2026-09-17
Character: 久遠ゆら / YURA
Purpose: YURA画像生成における用途別の標準アスペクト比・構図・余白・Quiet Zone・人物占有の選択をProfile A〜Eとして固定し、用途変更によるBODY変形やレイアウト判断のブレを防ぐ。

Parent layout authority:

`visuals/yura/generation/framing/FRAMING_AND_MARGIN_SPEC.md`

BODY authorities:

- `visuals/yura/identity/body/BODY_MASTER.md`
- `visuals/yura/identity/body/BODY_SPEC.md`

This file is a protected operational sub-spec of the framing / margin domain.
It does **not** replace `visuals/yura/generation/framing/FRAMING_AND_MARGIN_SPEC.md` and never owns BODY geometry.

---

## 1. Global invariants — absolute

All profiles A–E obey the following rules.

1. YURA remains exactly **7.25 heads tall** when full-body proportion is assessable.
2. Output size / aspect ratio / margin changes do not change face size, shoulder width, torso length, pelvis width, limb length, limb thickness or any other BODY relationship.
3. Character-size adaptation uses **uniform whole-character scale** only.
4. Additional space is created by uniform scale and/or whole-character translation inside the canvas.
5. Never resize head / torso / pelvis / legs / arms independently to fit a canvas.
6. Full-body requests preserve crown through toes without accidental clipping.
7. Unless explicitly requested, avoid extreme perspective distortion or unnecessary wide-angle deformation.
8. Pixel dimensions are secondary to the logical **aspect ratio + composition + safe-zone profile**. If the generator cannot natively output the exact target dimensions, use the nearest supported canvas and normalize later without stretching YURA.

The governing principle is:

**Canvas changes layout. Canvas never redesigns YURA.**

---

## 2. Profile A — MASTER / Full-Body Validation

### Use

- `YURA_VISUAL_MASTER` candidate generation
- BODY validation
- HAIR validation
- neutral identity validation
- formal reference candidate generation

### Canvas

- **9:16 portrait**

### Composition

- exactly one YURA
- front-facing full body unless a specific validation angle is explicitly required
- head top through toes fully visible
- centered
- near-orthographic / minimal perspective distortion
- body scale large enough for visual evaluation

### Margin

- **minimal safe margin / small surrounding negative space**
- do not leave unnecessary large blank areas
- do not crowd hair, head, hands or feet against the crop boundary

### Background baseline

- plain white to warm-white / neutral light background for controlled validation unless the tested domain itself requires another background

### Priority

Identity / BODY / FACE / EYE / HAIR / RENDERING evaluation takes priority over decorative composition.

---

## 3. Profile B — Standard Full-Body Derivative

### Use

- ordinary standing illustration
- outfit variation
- light pose variation
- ordinary SNS standing asset
- full-body derivative without a special output use case

### Canvas

- **9:16 portrait**

### Composition

- normally one YURA
- full body when the request is a standing / full-body asset
- head top through toes fully visible in full-body mode
- centered or modestly offset when scene composition requires it

### Margin

- **minimal safe margin**
- default range is visually tight to modest rather than spacious
- preserve a strong readable character scale

### Background

- task dependent
- simple background preferred when character comparison / outfit evaluation is important

---

## 4. Profile C — Smartphone Wallpaper

### Use

- smartphone lock screen
- smartphone home screen
- mobile wallpaper / device-specific vertical background

### Canvas

1. If a device model or explicit dimensions are provided, use the target device aspect ratio when reliably available.
2. If a target ratio is explicitly supplied by the user, use it.
3. If neither is available, use **9:19.5 portrait** as the default logical fallback.

### Composition

- full-body / 3/4 / upper-body may be chosen according to the requested wallpaper concept
- important identity features remain readable
- face and key gestures should not collide with expected system UI when practical

### Quiet Zone

Reserve the **upper approximately 15–25%** as a comparatively quiet visual zone.

The zone need not be blank. Prefer:

- simple sky / wall / room background
- low-detail environmental shapes
- restrained contrast
- low-information texture

Avoid placing there when practical:

- face / eyes
- important hand gesture
- key prop
- strong focal decoration
- text-like high-contrast shapes

### Scaling

Create wallpaper space by moving YURA lower and/or uniformly scaling the whole character smaller.
Never distort BODY to create UI space.

---

## 5. Profile D — X Thumbnail / SNS Thumbnail

### Use

- ordinary X thumbnail / post thumbnail
- SNS promotional thumbnail where small-display readability is important

### Default canvas

- **16:9 landscape**

This is a default, not an absolute override of an explicit requested ratio.
If the user explicitly requests **1:1**, another post format, header/banner, avatar/icon, or another placement, that explicit target replaces the default ratio while all BODY / framing invariants remain active.

### Composition

- medium framing is permitted and often preferred
- chest-up, waist-up, or approximately upper-thigh framing may be used according to the asset
- full-body is not required unless requested
- YURA's face and key co-subjects / props should remain readable at thumbnail scale

### Margin

- **minimal safe margin**
- avoid unnecessary dead space
- prioritize thumbnail readability and clear subject hierarchy

### Important distinction

`X thumbnail` does not mean profile icon or header.
Dedicated X avatar / header / text-overlay assets require their explicitly requested crop / safe-zone behavior.

---

## 6. Profile E — Background / Room / Environment Only

### Use

- room / environment background material
- room time-of-day variants
- environment plates
- background-only material for later character / UI composition

### Canvas

- **16:9 landscape** baseline

### Composition

- no character unless explicitly requested, in which case this is no longer pure Profile E
- no unrequested text
- no unrequested logo
- preserve readable environment geometry

### Layout

If later compositing is anticipated, keep the intended character / UI placement area usable without introducing arbitrary empty space that damages the environment composition.

Room/environment geometry follows the applicable Background authority when one has been formally adopted. Until then, `creation/background/reference-materials/` is non-authoritative material only.

---

## 7. Default profile selection

When the user's intended use is clear but no explicit profile name is given:

- MASTER / formal neutral validation / BODY or HAIR validation → **Profile A**
- ordinary full-body derivative / standing illustration → **Profile B**
- smartphone wallpaper → **Profile C**
- ordinary X / SNS thumbnail → **Profile D**
- background / room / environment only → **Profile E**

When the user explicitly states a ratio or special placement, apply the closest profile's behavior but let the explicit target ratio / placement override the profile's default ratio.

Examples:

- `X用だけど1:1` → Profile D behavior + explicit 1:1 ratio
- `MASTER候補を9:16` → Profile A
- `スマホ用 iPhone XX` → Profile C + device ratio
- `部屋だけ16:9` → Profile E

---

## 8. Relationship to Framing & Margin Spec

`visuals/yura/generation/framing/FRAMING_AND_MARGIN_SPEC.md` remains the layout domain owner.

This sub-spec owns only:

- the names Profile A–E
- their default use-case routing
- their default aspect ratios
- their standard composition intent
- their profile-specific margin / Quiet Zone behavior

If an item is not defined here, use the parent Framing & Margin Spec.

If this file appears to conflict with the parent:

1. obey the parent layout authority;
2. identify the conflict;
3. repair this sub-spec before material generation.

---

## 9. Generation compile placement

Apply this profile system inside:

**Block D — CAMERA / LAYOUT**

Generation compile remains:

1. CANON LOCK
2. derivative design
3. physical pose structure
4. camera / layout → select/apply Profile A–E here
5. reference isolation
6. negative / anti-drift constraints

Never allow profile selection to modify CANON LOCK.

---

## 10. QA interpretation

Profile mismatch is normally a derivative / layout failure.

Examples:

- Profile A full-body validation clips the feet → layout FAIL
- Profile C lacks usable upper Quiet Zone → layout FAIL
- Profile D thumbnail subject is unnecessarily tiny because of large dead space → layout FAIL
- Profile E contains an unrequested character → derivative request / layout FAIL
- any profile creates space by lengthening legs / shrinking the head / changing BODY widths → BODY FAIL plus layout FAIL

Correction should preserve current MASTER and all passed protected domains, then modify layout only.

---

## 11. Change control

This profile system is PROTECTED.

Do not silently change:

- Profile A = MASTER / validation, default 9:16 portrait
- Profile B = ordinary full-body derivative, default 9:16 portrait
- Profile C = smartphone wallpaper, device ratio first / 9:19.5 fallback / upper ~15–25% Quiet Zone
- Profile D = ordinary X / SNS thumbnail, default 16:9 landscape, explicit ratio may override
- Profile E = background / room / environment only, default 16:9 landscape
- universal BODY-safe uniform-scaling rule
- explicit user ratio / placement taking precedence over a profile's default ratio without changing BODY

Material changes require explicit user approval and Git logging.
