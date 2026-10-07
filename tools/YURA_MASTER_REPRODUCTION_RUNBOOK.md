# YURA Master Workflow — Reproduction / Session Recovery Runbook

Status: **ACTIVE OPERATIONAL RUNBOOK / NOT VISUAL AUTHORITY**

Purpose: restore the exact working method used during the YURA Master benchmark when a new chat starts, including the PowerShell commands run by the author and the AI-side/GitHub-side work that must happen before, during, and after paid generation.

This file exists because the workflow is intentionally strict and differs from ordinary ad-hoc image prompting. A new chat should read this file before changing the pipeline.

---

## 0. Primary objective

Create a **high-quality character Master while reducing generation drift and stochastic variance to the smallest practical level**.

The YURA work is also the proving ground for a reusable method for SHIORI, MIO, and later characters.

Operational goals:

- high visual quality, not merely technical PASS;
- low variance / reproducibility;
- Face Identity, Face Geometry, Body Geometry, Composition, rendering, and later local refinements remain separable;
- author intent overrides generic anime/model defaults;
- failed candidates never silently become future visual references;
- paid generations are controlled experiments, not random rerolls;
- all Authority inputs, hashes, prompt compilation, QA, and promotion are auditable;
- Composition never repairs anatomy by deforming body parts.

Core discipline:

```text
one paid RAW
= one explicit hypothesis
= one measurable result
= one decision
```

---

## 1. Current repository checkpoint

At the time this runbook was created, GitHub `main` was:

```text
da561c4847d8d12754fc9c092ee2ca819c4886a5
Record numeric audit of active YURA Face Reference
```

A future session must **not assume this SHA is still current**. Always read current `main` first.

Important unrelated local change that has repeatedly existed:

```text
manuscript/episode-001/EP001_DRAFT.txt
```

Never edit, stage, commit, discard, or overwrite that file while doing visual benchmark work.

Never use `git reset --hard` and never force-push as part of this workflow.

---

## 2. Files a new chat must read first

Before changing anything, read current Git `main` and then read at minimum:

```text
tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md
tools/yura-master-benchmark/CURRENT_HANDOFF.md
tools/yura-master-benchmark/PIPELINE_STATE.md
visuals/MASTER_CREATION_WORKFLOW.md
visuals/yura/identity/face/FACE_REFERENCE_RULES.md
visuals/yura/identity/face/FACE_GEOMETRY_REVISION_LIFECYCLE.md
visuals/yura/identity/face/YURA_FACE_GEOMETRY_AUDIT.md
visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md
visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
visuals/yura/identity/master/YURA_MASTER_GENERATION_LIFECYCLE.md
```

The operational docs are not visual Authorities. The configured Authority files are defined by the benchmark config and must be verified from current Git.

---

## 3. YURA Authority separation used by the benchmark

The benchmark has used this role separation:

```text
Face Identity Authority
  visuals/yura/identity/face/YURA_FACE_REFERENCE.png
  visuals/yura/identity/face/FACE_REFERENCE_RULES.md

Body Geometry Authority
  visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
  visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md

Master-construction visual text
  visuals/yura/identity/master/YURA_VISUAL_TEXT.md

Composition Authority
  visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md

Lifecycle / process
  visuals/yura/identity/master/YURA_MASTER_GENERATION_LIFECYCLE.md
```

Denied YURA appearance sources during Master construction include:

```text
characters/YURA.md
story/**
manuscript/**
old Git history / old branches as appearance authority
old/rejected YURA visuals
Memory-derived YURA appearance
past generated YURA images unless explicitly active Authority
```

Novel/story material is isolated from visual Master generation.

---

## 4. Safe local Git synchronization pattern

When `manuscript/episode-001/EP001_DRAFT.txt` is locally modified, use this exact pattern before pulling documentation or pipeline changes:

```powershell
git stash push -m "WIP EP001 before visual benchmark sync" -- manuscript/episode-001/EP001_DRAFT.txt

git pull --rebase origin main

git stash pop

git log -1 --oneline
git status --short
```

Expected state after a clean visual sync is usually:

```text
HEAD == origin/main
 M manuscript/episode-001/EP001_DRAFT.txt
```

The leading-space ` M` means the novel draft remains unstaged, which is desired.

For a read-only state check before any write:

```powershell
git fetch origin main

git rev-parse HEAD
git rev-parse origin/main
git status --short
```

Do not pull blindly if local visual files are intentionally being replaced; inspect status first.

---

## 5. PowerShell commands used to validate a replaced visual Authority image

For a canonical image such as the Body Geometry guide:

```powershell
$img = "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png"

(Get-FileHash $img -Algorithm SHA256).Hash.ToLower()
git hash-object $img

python -c "from PIL import Image; im=Image.open(r'visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png'); print(im.size)"
```

For the active long-leg Body Geometry guide, the replacement that was approved had:

```text
size = 1200 × 1600
SHA-256 = 7e4c6dd7c525d5a1f123418cf20e417aab654200b4ed734972467a548148b407
Git blob SHA = 0a4c2ec2db9e15c4edaae50a91bfb3552fae9767
```

Canonical geometry recorded for that guide:

```text
crown   = y 160
chin    = y 340
crotch  = y 856
knee    = y 1156
soles   = y 1456
one head = 180 px
total = 7.2 heads

CROTCH / PELVIS LINE
= UPPER / LOWER BODY BOUNDARY

crown→crotch = 3.8667 heads
chin→crotch  = 2.8667 heads
inseam proxy = 46.2963%
```

If the image is replaced again, recompute these values; do not reuse old hashes.

---

## 6. Staging / committing visual Authority changes without touching the novel

Example for the Body Geometry image + MD pair:

```powershell
git add -- `
  visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md `
  visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png

git status --short
git diff --cached --name-status
```

Desired pattern:

```text
 M manuscript/episode-001/EP001_DRAFT.txt
M  visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md
M  visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
```

Then:

```powershell
git commit -m "Replace YURA Body Geometry guide with approved long-leg geometry"
git push origin main

git log -1 --oneline
git status --short
```

Never use `git commit -a` for this benchmark, because it risks including the novel draft.

---

## 7. Python syntax checks used before preflight

When benchmark Python changes have been pulled or edited:

```powershell
python -m py_compile tools/yura-master-benchmark/body_geometry_qa.py
python -m py_compile tools/yura-master-benchmark/normalize_composition.py
python -m py_compile tools/yura-master-benchmark/run_raw_once.py
python -m py_compile tools/yura-master-benchmark/run_once.py
```

A syntax failure is fixed before any paid model call.

---

## 8. Free preflight command

The standard preflight command is:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Preflight must return:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
```

Recent expected gate labels after the torso/inseam work were:

```text
body_geometry_gate = HEAD_RATIO_PLUS_INSEAM_PROXY_PLUS_TORSO_SPECIFIC_GATE_REQUIRED_AFTER_RAW
body_geometry_inseam_proxy_target = 46.0–46.5%
body_geometry_torso_gate = COMPACT_TORSO_AND_SLIGHTLY_HIGH_PELVIS
composition_execution = DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS
```

Do not proceed to a paid RAW if preflight fails or if `paid_model_calls` is not zero.

No API key should be required merely to return before paid calls in preflight mode.

---

## 9. Paid RAW generation command

Only after reviewing a successful preflight:

```powershell
python tools/yura-master-benchmark/run_once.py
```

This stage must produce `result_raw.png` only for the body-first generation stage.

Do **not** immediately run Composition.

A successful RAW run normally produces artifacts such as:

```text
result_raw.png
composition_deferred.json
qa.json
cost.json
compiled_prompt.txt
compiled_prompt.sha256
prompt_invariant_check.json
```

`result.png` is intentionally absent until Body Geometry has passed.

---

## 10. What the local runner / AI pipeline is doing behind the command

The benchmark is not simply sending a handwritten prompt to the image model.

The intended execution architecture is:

```text
current Git main
  -> local runner verifies HEAD == origin/main
  -> configured Authority paths are verified
  -> Authority files are read only from the configured set
  -> SHA-256 values are computed locally
  -> a sealed Authority bundle is built
  -> full text Authority contents + PNG path/hash/role metadata are sealed
  -> Codex receives instruction + sealed bundle through stdin
  -> Codex compiles the RAW image prompt
  -> runner validates required prompt invariants
  -> runner rejects forbidden/deferred Composition literals
  -> only then Image API is called
  -> original RAW is retained
  -> QA/cost artifacts are written
```

The sealed architecture was introduced because early Codex attempts failed when the model was expected to discover/read local files itself. The reliable design does **not** depend on Codex using shell/Git/MCP to find Authority files.

Codex is run with a read-only / isolated posture; the Python host is responsible for supplying verified Authority content.

The runner also verifies that the returned Authority manifest matches expected:

```text
path
ordinal/order
role
SHA
commit
denied sources
image reference order
```

The active image-reference order used by the benchmark has been:

```text
1. YURA_FACE_REFERENCE.png
2. YURA_BODY_GEOMETRY_GUIDE.png
```

---

## 11. Frozen model / API configuration used during the benchmark

The benchmark was developed around:

```text
Codex model:
  gpt-5.3-codex

Image model:
  gpt-image-2.5-sunburst-2026-09-08

Image request:
  size = 1440x2560
  quality = high
  format = png
  background = opaque
  n = 1
```

Environment variables used locally:

```text
OPENAI_API_KEY
OPENAI_PROJECT_ID
```

Admin cost querying, when needed, uses:

```text
OPENAI_ADMIN_KEY
```

Never paste actual key values into chat, documentation, or Git.

---

## 12. Body Geometry QA command

After the original `result_raw.png` is visually reviewed and the five vertical landmarks are manually located:

```powershell
python tools/yura-master-benchmark/body_geometry_qa.py <RUN_DIR> `
  --crown-y <Y> `
  --chin-y <Y> `
  --crotch-y <Y> `
  --knee-y <Y> `
  --soles-y <Y> `
  --confirm-landmarks-reviewed `
  --confirm-upper-body-not-elongated `
  --confirm-torso-compact `
  --confirm-waist-not-low `
  --confirm-pelvis-high-enough `
  --confirm-lower-body-slightly-longer `
  --confirm-knee-placement-natural
```

**Do not supply a confirmation flag if the image does not satisfy that condition.**

The script calculates values including:

```text
head_ratio_heads
crown_to_crotch_heads
chin_to_crotch_heads
crotch_to_knee_heads
knee_to_soles_heads
crotch_to_soles_heads
knee_from_crown_heads
inseam_proxy_ratio
inseam_proxy_percent
```

and binds the report to the exact RAW SHA-256.

At the time of this runbook, active runtime gates still included:

```text
head ratio acceptable = 7.1–7.3
inseam proxy target = 46.0–46.5%
>=47.0% = explicit model-like hard-fail reason
chin→crotch audit envelope = 2.7985–2.9420 heads
```

These are calibration values, not universal anatomical truths. They may be deliberately recalibrated after author review, but the entire Authority/config/QA/prompt chain must be updated together.

---

## 13. Composition gate and commands

Composition is deferred until Body Geometry passes.

Plan/check stage:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR>
```

Final normalization only after explicit body PASS:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR> --confirm-body-geometry-pass
```

Allowed final transforms only:

```text
uniform whole-raster scaling
x/y translation
white-background crop/pad as implied by final canvas placement
```

Never use:

```text
nonuniform scaling
body-part scaling
warp
content-aware deformation
inpainting/body reshaping
face regeneration
```

Final Composition Authority target has been 1440×2560, with figure occupancy/margins handled after anatomy rather than leaking those numeric targets into RAW generation.

---

## 14. Prompt invariants that were deliberately strengthened

The RAW prompt gate was designed to require concepts equivalent to:

```text
BODY GEOMETRY IS RESOLVED FIRST.
BODY GEOMETRY HAS PRIORITY OVER COMPOSITION.
RAW GENERATION IS BODY-GEOMETRY-FIRST.
FINAL COMPOSITION IS DEFERRED TO DETERMINISTIC POST-PROCESSING.
DO NOT OPTIMIZE FOR FINAL CANVAS OCCUPANCY OR MARGINS DURING GENERATION.
DO NOT ALTER INTERNAL BODY LANDMARK POSITIONS FOR CANVAS FITTING.
ONE HEAD IS CROWN TO CHIN.
CROWN TO SOLES MUST BE 7.2 HEADS.
BODY-GEOMETRY REFERENCE SCALE OVERRIDES DEFAULT LARGE-HEAD ANIME BODY PROPORTIONS.
DO NOT ACHIEVE 7.2 BY LENGTHENING ONLY LEGS OR ONLY TORSO.
UPPER BODY MUST NOT BE VERTICALLY ELONGATED.
TORSO MUST BE COMPACT; DO NOT LENGTHEN THE RIBCAGE-TO-PELVIS OR WAIST SPAN.
KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.
DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.
```

Later testing also identified a likely integration issue: Face Reference may be influencing apparent physical head size even though it is denied Body authority.

A planned head-scale decoupling test should strengthen the contract conceptually to:

```text
FACE REFERENCE DEFINES FACIAL IDENTITY ONLY.
IT DOES NOT DEFINE HEAD-TO-BODY SCALE.
IT DOES NOT DEFINE HEAD VERTICAL SIZE FOR FULL-BODY PROPORTION.
IT DOES NOT DEFINE TOTAL HEAD COUNT.
BODY GEOMETRY EXCLUSIVELY CONTROLS FULL-BODY HEAD SCALE / TOTAL HEAD COUNT.
```

Do not implement this blindly; read current `CURRENT_HANDOFF.md` and current main first because later chats may already have changed it.

---

## 15. Important Body Geometry experiment history / diagnosis

Earlier Body Geometry runs repeatedly produced approximately 6.4-head characters even when 7.2 was requested.

A revised explicit Body Geometry guide was then created with a visible:

```text
CROTCH / PELVIS LINE = UPPER / LOWER BODY BOUNDARY
```

The first RAW after that guide was visually much better in torso/pelvis/lower-body balance, but preliminary measurement of the uploaded/downscaled copy was roughly:

```text
head ratio ≈ 6.37
inseam proxy ≈ 50.9%
chin→crotch ≈ 2.13 heads
```

Important interpretation:

```text
internal upper/lower-body balance looked good
but total head ratio still looked ~6.4
```

Do not simply copy that RAW. It is a calibration sample, not Authority.

Preferred strategic direction at that checkpoint:

```text
preserve successful compact-torso / long-leg balance
+ keep Face Identity
+ still attempt final 7.2 head standard
```

The original local RAW should be measured, not the chat display copy, before freezing any new numeric gate.

---

## 16. Face Geometry audit executed in this workflow

The active Face Reference was audited separately from Body Geometry.

Files:

```text
visuals/yura/identity/face/FACE_GEOMETRY_REVISION_LIFECYCLE.md
visuals/yura/identity/face/YURA_FACE_GEOMETRY_AUDIT.md
```

The exact active Face Reference inspected was:

```text
image dimensions = 372 × 364 px
Git blob SHA = 4c96c4ec42f996807248be1aff60ec8a090fd570
SHA-256 = 3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
```

Approximate manually reviewed landmark measurements recorded in the audit:

```text
head crown / visible hair crown = (186, 8)
chin = (187, 252)

face edge proxy at eye line:
left x ≈ 109
right x ≈ 270

left eye outer = (119, 173)
left eye inner = (166, 176)
right eye inner = (206, 173)
right eye outer = (253, 169)

left eye center x ≈ 142.5
right eye center x ≈ 229.5

nose reference = (186, 201)
mouth center = (187, 222)

left visible ear y ≈ 164–207
right visible ear y ≈ 158–204
```

Derived audit values:

```text
average eye width ≈ 47 px
inner-eye gap ≈ 40 px
inner-eye gap / average eye width ≈ 0.85

eye-center distance ≈ 87 px
face-width proxy ≈ 161 px
eye-center distance / face width ≈ 0.54
average eye width / face width ≈ 0.29

nose→chin = 51 px
nose→mouth = 21 px
mouth→chin = 30 px
nose→mouth / nose→chin ≈ 0.41
mouth→chin / nose→chin ≈ 0.59
```

Audit conclusion:

```text
Face Identity stability           PASS
Eye spacing                       PASS / LOW WATCH
Eye size                          PASS / style-dependent
Horizontal facial center-line     PASS
Mouth vertical placement          PASS / WATCH
Lower face / chin                 PASS
True forehead geometry            NOT MEASURABLE (hairline hidden)
Upper-head apparent size          WATCH / hair-volume confound
Ear height / prominence           WATCH-HIGH
Overall face geometry             PASS WITH LOCAL WATCH ITEMS
```

Broad Face redesign is **not** justified.

Ear revision is intentionally deferred. The project later identified that ear problems may be partly caused by generation behavior that tries to expose/show ears, especially at pose/view changes. Ear correction should therefore be considered together with future anti-drift rules for pose/view transformations rather than solved by globally changing the face.

---

## 17. Future pose/view anti-drift issue to solve later

After base Face and Body are stable, a later pipeline stage should address pose/view changes such as:

```text
squatting
forward lean
45-degree stretch / oblique standing
other perspective-heavy poses
```

Known risk:

```text
pose/view change
-> model stretches torso or limbs
-> head/body ratios drift
-> ears may be exposed/enlarged to make them visible
```

Desired rule architecture:

```text
BASE GEOMETRY
= locked Face + Body geometry

POSE TRANSFORM
= pose only

VIEW ANGLE TRANSFORM
= camera/view only

FORBIDDEN DRIFT
= do not redesign head count, torso length, leg length, facial feature layout, or ear prominence merely to make the pose/readability easier
```

Ear visibility should be incidental. Hair may naturally obscure ears. The model should not open hair gaps or enlarge ears merely to display them.

This work is deferred until base full-body stability is solved.

---

## 18. AI/GitHub-side work performed during this project

The assistant has used GitHub directly to create/update operational documentation and Authority-adjacent process files. Important commits include, in chronological order from this phase:

```text
09628e3  Replace YURA Body Geometry guide with approved long-leg geometry
6a8284c  Activate replaced YURA Body Geometry guide
588dce3  Record YURA Master benchmark checkpoint and next calibration steps
6573ca8  Record YURA benchmark handoff and paid-iteration strategy
cfd397e  Add YURA Face Geometry revision lifecycle
b5347e9  Add YURA Face Geometry audit record
da561c4  Record numeric audit of active YURA Face Reference
```

Do not assume these are the newest commits forever. Their purpose here is reconstruction/history.

When the assistant changes GitHub directly, the local Windows checkout must later be synchronized using the stash/pull/pop pattern before running local benchmark code.

---

## 19. Cost accounting behavior

`cost.json` records benchmark estimates from model usage.

OpenAI project cost API has daily granularity for the project-day bucket; do not falsely label an entire project-day cost as run-specific when multiple runs occurred that day.

Run estimates are acceptable for experiment budgeting; authoritative project-day costs become available after the relevant UTC day closes.

Do not block the main visual workflow on exact authoritative cost attribution unless the author specifically asks for it.

---

## 20. What NOT to do in a new chat

Do not:

```text
start from memory alone
use rejected RAWs as visual reference
use old YURA Masters as regeneration Authority
read novel/story for visual appearance
change Face and Body at the same time without a controlled reason
run paid generation before free preflight
run Composition before Body Geometry PASS
repair anatomy via part scaling/warp/inpainting
commit manuscript/episode-001/EP001_DRAFT.txt
paste API keys into chat or Git
randomly reroll unchanged conditions
```

If a paid RAW fails, diagnose before launching the next one.

---

## 21. New-chat recovery sequence

A new chat should follow this exact recovery order:

```text
1. Read current GitHub main SHA.
2. Read this runbook.
3. Read CURRENT_HANDOFF.md and PIPELINE_STATE.md.
4. Read current Face/Body/Composition Authority text files.
5. Check whether GitHub has advanced beyond local checkout.
6. Preserve EP001 draft with stash if necessary.
7. Pull/rebase main.
8. Restore stash.
9. Run git status and confirm only expected local changes remain.
10. If Python pipeline changed, run py_compile checks.
11. Identify the exact next hypothesis from CURRENT_HANDOFF.md.
12. Make the smallest code/Authority diff necessary.
13. Commit/push that diff without touching the novel.
14. Sync local if the assistant committed through GitHub.
15. Run free preflight and inspect compiled_prompt.txt + prompt_invariant_check.json.
16. Only after PASS, run exactly one paid RAW for that hypothesis.
17. Measure original RAW, not a downscaled chat display.
18. Record result and decision in Git.
19. Do not normalize Composition until Body Geometry passes.
```

---

## 22. Current likely next technical direction

At the time of this runbook, the main unresolved full-body problem was:

```text
Face Identity reference retained
+ desired total head ratio = 7.2
+ generation repeatedly converges near ~6.4
```

The leading hypothesis is that Face Reference may be implicitly influencing physical head scale despite explicit Authority denial.

The next controlled test should therefore isolate/strengthen **Face Identity vs head-to-body scale separation**, while preserving the successful internal torso/pelvis/lower-body balance.

However, before implementing a new test, always read current `CURRENT_HANDOFF.md` because a newer chat may already have advanced this plan.

---

## 23. Minimal prompt for a new chat

A new chat can be started with:

```text
現行 GitHub Pin-Gin/MEMORIELA の current main を実際に読んでください。
最初に tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md、
tools/yura-master-benchmark/CURRENT_HANDOFF.md、
tools/yura-master-benchmark/PIPELINE_STATE.md を読み、
そこに記録された PowerShell 実行手順、Authority 分離、sealed benchmark、QA gate、Git 同期方法をそのまま復元してください。
manuscript/episode-001/EP001_DRAFT.txt は絶対に触らないでください。
記憶や過去チャットだけで手順を推測せず、current main を基準に続きから実作業してください。
```

This runbook is intentionally redundant. Reproducibility is more important than compactness here.
