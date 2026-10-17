# YURA Master Workflow — Current Paid Full-body Reproduction Runbook

Status: **CURRENT OPERATIONAL RUNBOOK / AUTHOR-AUTHORIZED PAID ROUTE / NOT VISUAL AUTHORITY**

Purpose: current YURA full-body Master候補を、現在のGit Visual Authorityだけから再現可能に生成する。

This document replaces the legacy paid-route procedure for current execution. Historical Test 2/3/5/6 material remains audit-only under `tools/` and must not silently become current Authority.

---

## 1. Current objective

Current sequence:

```text
current Git main
-> local runner verifies current Authority files and hashes
-> sealed Authority bundle
-> Codex prompt compile
-> runner manifest / invariant verification
-> OpenAI Image API
-> result.png
-> head-ratio QA (7.0–7.2)
-> author visual QA
-> PASS candidate
-> explicit Master promotion
```

The latest free GPT full-body PASS image is used by the author/GPT as a **balance calibration indicator only**.

It is not a Git Authority and is not automatically passed to the paid Image API.

---

## 2. Current Visual Authority set

Configured in `tools/yura-master-benchmark/config.json`.

```text
1. visuals/yura/identity/master/YURA_VISUAL_TEXT.md
2. visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md
3. visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
4. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
5. visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
6. visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
7. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
```

Highest text authority:

```text
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
```

The current repository-promoted Face Reference is the active face image. Do not restore old Face Reference geometry.

The Body Geometry Guide is body-geometry support only. If a legacy visual implication conflicts with current `YURA_VISUAL_TEXT.md`, current Visual Text wins.

---

## 3. Image reference order sent to OpenAI Image API

```text
1. YURA_BODY_GEOMETRY_GUIDE.png
2. YURA_FACE_REFERENCE.png
```

Roles:

```text
Body Geometry Guide
= body geometry support only
= NOT face / hair / expression / clothing / skin Authority

Face Reference
= face identity and face-local geometry only
= NOT body scale / head count / torso length / leg length / canvas occupancy Authority
```

`YURA_EAR_GEOMETRY_MASTER.png` is sealed and hash-verified as active ear Authority, but is not directly sent as a third full-body Image API reference. Ear behavior is enforced through the current ear text rules + Face-up authority to avoid visibility-driven ear exposure or bald-head contamination.

---

## 4. Current full-body fixed condition

Hard target:

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
Face Geometry
eye shape / size / placement
C2 baseline -> 0.3% inward
pupil bilateral symmetry
ear actual geometry / no visibility compensation
body definition
current chest-to-frame relationship
```

Never solve the head-count target by:

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

## 5. Current validation presentation

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
```

Validation clothing:

```text
plain opaque matte camisole
plain undecorated shorts
white to very light gray
```

Forbidden clothing additions:

```text
drawstring
bows / ribbons
lace / frills / ruffles
patterns
decorative seams
skirt
socks / shoes
jewelry
hair accessories
lingerie styling
transparency
satin / glossy fabric
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
retain very subtle natural blood color
```

Expression:

```text
TRUE NEUTRAL
```

No mood reinterpretation.

---

## 6. Retired legacy numeric gates

The current route does **not** use these legacy paid-route hard gates:

```text
7.1–7.3 heads
89% figure occupancy
88–90% occupancy
5–6% top/bottom margins
legacy Test 5 wording
legacy Composition postprocess percentage gates
```

Current head-count hard gate is only:

```text
7.0–7.2
```

Legacy inseam/pelvis/torso percentages remain historical audit information, but are not active hard gates unless the author explicitly reauthorizes them.

This prevents the paid runner from silently rewriting the currently locked body design.

---

## 7. Safe Git sync before execution

Repository root:

```powershell
git status
git fetch origin main
git rev-parse HEAD
git rev-parse origin/main
```

The paid runner requires:

```text
HEAD == origin/main
```

Do not use `git reset --hard` or force-push as part of this workflow.

Do not expose API keys in Git or chat.

---

## 8. Local syntax check

```powershell
python -m py_compile tools/yura-master-benchmark/run_raw_once.py
python -m py_compile tools/yura-master-benchmark/run_once.py
python -m py_compile tools/yura-master-benchmark/run_batch.py
python -m py_compile tools/yura-master-benchmark/body_geometry_qa.py
```

Install dependencies when needed:

```powershell
python -m pip install -r tools/yura-master-benchmark/requirements.txt
```

---

## 9. Free preflight

Before any paid model call:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Required result:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
head_ratio_gate = 7.0–7.2
legacy_composition_percentage_gates = RETIRED
```

Preflight verifies:

```text
current Git HEAD
Authority existence
Authority clean state
SHA-256
Authority order
image-reference order
sealed bundle construction
current execution constraints
```

No paid Codex or Image API call is made in preflight mode.

---

## 10. Exactly one paid seed run first

After preflight review:

```powershell
python tools/yura-master-benchmark/run_once.py
```

Pipeline:

```text
sealed bundle
-> Codex compile
-> manifest verification
-> prompt invariant verification
-> OpenAI Image API
-> result.png
-> qa.json = QA_PENDING
```

A generated image is never automatically a Master.

---

## 11. Head-ratio QA

After visually locating the actual structural crown, chin, and soles:

```powershell
python tools/yura-master-benchmark/body_geometry_qa.py <RUN_DIR> `
  --structural-crown-min-y <Y> `
  --structural-crown-best-y <Y> `
  --structural-crown-max-y <Y> `
  --chin-y <Y> `
  --soles-y <Y> `
  --confirm-measurement-reviewed
```

Optional:

```text
--visible-hair-crown-y
```

This is diagnostic only. Outer hair crown is not used as skull height.

PASS requires the complete reviewed head-ratio interval to remain inside:

```text
7.0–7.2
```

This numeric QA does not rewrite body geometry.

---

## 12. Author visual QA

At minimum review:

```text
Face Identity / Face Geometry
eye shape / size / C2 0.3% inward placement
pupil bilateral symmetry
ear visibility-compensation absence
body definition / overall balance
current chest-to-frame relationship
hair length around waist
white-leaning skin without over-whitening
validation clothing
upright pose
heels down / full sole contact
white background / centering
7.0–7.2 head count
```

Only explicit author PASS can promote a candidate.

---

## 13. Ten-run batch

Run a batch only after:

```text
single paid seed run completed
seed technical artifacts reviewed
cost checked
current route confirmed
```

Example:

```powershell
python tools/yura-master-benchmark/run_batch.py `
  --seed-run tools/yura-master-benchmark/runs/<RUN_DIR> `
  --runs 10 `
  --confirm-seed-reviewed `
  --allow-estimate
```

If authoritative run-specific cost attribution is available, omit `--allow-estimate`.

Each batch item is an independent run with its own:

```text
Git commit
Authority hashes
sealed bundle
Codex trace
compiled prompt + SHA-256
image result
cost data
QA data
```

---

## 14. Promotion rule

```text
FAIL
-> not Authority
-> not Master
-> never feed back automatically

PASS
-> explicit author approval required
-> then promote to current full-body Master path chosen by author
```

All paid-run process artifacts stay under `tools/**`.

Only author-approved final visual assets belong under `visuals/**`.
