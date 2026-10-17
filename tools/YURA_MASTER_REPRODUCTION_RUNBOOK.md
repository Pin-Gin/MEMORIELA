# YURA Master Workflow — Frozen Recovery / Regeneration Runbook

Status: **FULL-BODY MASTER PROMOTED / PAID ROUTE FROZEN / NOT VISUAL AUTHORITY**

Purpose: preserve a reproducible recovery path for YURA Full-body Master regeneration using only the current Git Visual Authorities. The current Master-generation phase is complete; no billable call is authorized unless the author explicitly reopens the phase.

Historical Test 2/3/5/6 material remains audit-only under `tools/` and must not silently become current Authority.

---

## 1. Current state

```text
Ear Geometry Master = PROMOTED
Face-up Master = PROMOTED
Full-body Master = PROMOTED
7.0-head Body Geometry Guide = PROMOTED AS SUPPORT
paid generation = COMPLETED / STOPPED BY AUTHOR
paid batch = NOT EXECUTED
PAID_GENERATION_ALLOWED = NO
```

Official Full-body Master:

```text
visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
promotion commit = 3ce89e33193effa627ea794e803d9a3b50cb085b
SHA-256 = CCBE315659DAC02169C833F8140096322725E85250FAB73214D30FBBC835EDF1
```

Body-directory synchronized copy:

```text
visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png
```

Current Body Geometry Guide:

```text
visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
SHA-256 = C23D1D2C348102B4ED9D75C422E1C2323800565B94E27A7FF13AF7C624EBDF95
```

---

## 2. Current Visual Authority set

Configured in `tools/yura-master-benchmark/config.json`.

```text
1. visuals/yura/identity/master/YURA_VISUAL_TEXT.md
2. visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
3. visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md
4. visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
5. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
6. visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
7. visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
8. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
```

Role separation:

```text
YURA_VISUAL_TEXT.md
= highest YURA visual text authority

YURA_FULL_BODY_MASTER.png
= primary integrated full-body visual authority

YURA_FACE_REFERENCE.png / YURA_FACE_UP_MASTER.md
= face-local identity / geometry authority

YURA_EAR_GEOMETRY_MASTER.png / YURA_EAR_BASIC_RULES.md
= ear-local authority

YURA_BODY_GEOMETRY_GUIDE.png
= 7.0-head body-geometry recovery support only
```

The Body Geometry Guide must not override or be averaged with the official Full-body Master.
The validation camisole / shorts visible in the Full-body Master are validation presentation, not permanent wardrobe Authority.

---

## 3. Recovery image-reference order

If the author explicitly reopens Full-body Master regeneration, the Image API reference order is:

```text
1. YURA_FULL_BODY_MASTER.png
2. YURA_BODY_GEOMETRY_GUIDE.png
3. YURA_FACE_REFERENCE.png
```

Roles:

```text
Full-body Master
= primary integrated full-body body / silhouette / balance reference
= validation clothing is not permanent wardrobe Authority

Body Geometry Guide
= 7.0-head proportion / body-geometry recovery support only
= NOT face / hair / expression / clothing / skin Authority

Face Reference
= face identity and face-local geometry only
= NOT body scale / torso length / leg length / canvas occupancy Authority
```

Ear Authority remains sealed and hash-verified; ear behavior is controlled by the current ear text / geometry Authorities.

---

## 4. Current full-body standard

```text
TARGET HEAD COUNT RANGE = 7.0–7.2 heads
TARGET HEIGHT IMPRESSION = 152–153 cm
```

One head:

```text
actual structural crown / skull top -> chin
```

Do not use outer hair volume as skull height.

Locked:

```text
official integrated Full-body Master proportions
Face Geometry
eye shape / size / placement
C2 baseline -> 0.3% inward
pupil bilateral symmetry
ear actual geometry / no visibility compensation
body definition
current chest-to-frame relationship
```

Never solve the head-count standard by:

```text
face elongation
midface/lower-face/chin elongation
torso-only elongation
leg-only elongation
shoulder widening
ribcage enlargement
tall model-like conversion
```

---

## 5. Validation presentation

The promoted Master uses this validation presentation:

```text
exactly one YURA
front-facing
full body
completely upright
head not tilted
arms naturally down
legs near together
both feet flat on ground
heels down
full sole contact
no tiptoe
no heel lift
no crossed legs
no contrapposto
barefoot
pure white background
centered
plain opaque matte camisole
plain undecorated shorts
```

Hair:

```text
silver-white
straight-dominant
SUPER-LONG
ends around waist
not substantially below waist
```

Skin:

```text
clearly white-leaning pale
do not over-whiten
not pure white
not sickly pale
```

Expression:

```text
TRUE NEUTRAL
```

The validation camisole / shorts are not a permanent wardrobe definition. For derivative clothing generation, preserve the official Master body / identity and apply only the requested clothing change.

---

## 6. Retired legacy numeric gates

The recovery route does **not** use these historical hard gates:

```text
7.1–7.3 heads
89% figure occupancy
88–90% occupancy
5–6% top/bottom margins
legacy Test 5 wording
legacy composition postprocess percentage gates
```

Current head-count standard:

```text
7.0–7.2
```

Legacy inseam / pelvis / torso percentages remain historical audit information only unless the author explicitly reauthorizes them.

---

## 7. Normal derivative use

For ordinary future full-body generation such as temporary clothing changes, do **not** reopen the paid Master-generation route by default.

Primary reference:

```text
visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
```

Use current Face / Ear / Visual Text Authorities as needed for local consistency.
Use the Body Geometry Guide only when 7.0-head body recovery / proportion support is materially useful.

---

## 8. Recovery preflight

A free recovery preflight is permitted and makes no paid model call:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Expected core output:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
paid_generation_allowed = false
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
head_ratio_gate = 7.0–7.2
```

Preflight verifies:

```text
HEAD == origin/main
Authority files exist and are clean
Full-body Master SHA-256
body-directory Master copy matches primary Master
Body Geometry Guide SHA-256
Authority order
image-reference order
sealed bundle construction
current execution constraints
```

A successful preflight does not authorize a billable call.

---

## 9. Paid reactivation rule

Current paid execution must fail closed.

To reopen Master regeneration, all of the following are required:

```text
1. explicit author instruction to reopen paid generation
2. review current Git Authorities
3. update route_state / paid_generation_allowed deliberately
4. syntax check runner
5. free preflight
6. author review of preflight
7. exactly one paid seed first
```

Do not silently flip `paid_generation_allowed` to true.
Do not start a batch because a preflight passes.

---

## 10. Syntax check after any future reactivation edit

```powershell
python -m py_compile tools/yura-master-benchmark/run_raw_once.py
python -m py_compile tools/yura-master-benchmark/run_once.py
python -m py_compile tools/yura-master-benchmark/run_batch.py
python -m py_compile tools/yura-master-benchmark/body_geometry_qa.py
```

---

## 11. Future candidate QA

If a future regeneration phase is explicitly reopened, review at minimum:

```text
official Full-body Master balance preservation
Face Identity / Face Geometry
eye shape / size / C2 0.3% inward placement
pupil bilateral symmetry
ear visibility-compensation absence
body definition / overall balance
current chest-to-frame relationship
hair length around waist
white-leaning skin without over-whitening
requested / validation clothing correctness
upright pose
heels down / full sole contact
white background / centering
7.0–7.2 head count measured from the image
```

Only explicit author PASS may replace the current official Full-body Master.

---

## 12. Historical artifacts

Paid-run prompts, manifests, cost records, traces, candidates, rejected outputs and QA remain under `tools/**`.
They are implementation / audit history and are not current Visual Authority.
