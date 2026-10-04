# YURA MASTER GENERATION — WORKLOG / HANDOFF

Status: **ACTIVE WORK IN PROGRESS**

Last updated: **2026-10-04 JST**

This file is an operational handoff document for continuing the current YURA Master-generation and benchmark work in a new chat or a new Codex/OpenAI session.

**This file is NOT a YURA visual Authority and MUST NOT be used as an image-generation appearance source.**

---

## 0. Why this document exists

The current work spans Git Authority design, Codex-based Authority resolution, OpenAI image generation, cost measurement, QA, and later Production migration.

A new chat that only reads the repository must be able to answer all of the following without relying on chat memory:

1. What is the overall objective?
2. Why was the YURA visual system rebuilt?
3. Which files are authoritative now?
4. What stage has already been completed?
5. What exact step is currently in progress?
6. What must be done next?
7. How should proposals be made so they remain consistent with the decisions already taken?
8. Which sources and operations are forbidden?

This document records that state.

---

# 1. Overall objective

The immediate objective is to create a new, high-confidence **YURA full-body Master image** from explicitly separated Git Authorities.

The process must be reproducible and measurable.

The current experiment is specifically designed to answer:

- Can Codex read the approved Git Authorities in a fixed order and compile a stable generation prompt?
- Can OpenAI image generation produce a YURA Master candidate that passes geometry/identity/composition QA?
- How much does **one complete run** cost?
- If one run costs only a small amount, what is the PASS rate across **10 independent runs**?
- If results vary, is the variance coming from the Codex prompt-compilation stage or from image generation?

The experimental flow is:

```text
current Git main
    ↓
Codex resolves ONLY approved Authorities
    ↓
Codex discloses read order + commit + SHA-256 values
    ↓
Codex compiles an exact prompt
    ↓
runner independently verifies the manifest
    ↓
OpenAI image generation receives the compiled prompt + approved reference images
    ↓
result.png + usage/cost logs
    ↓
geometry/composition QA
    ↓
author visual QA
    ↓
PASS candidate may later be promoted to YURA Master
```

The first paid experiment must be **ONE RUN ONLY**.

Only after its actual cost is checked should a 10-run batch be considered.

---

# 2. Why the YURA visual system was rebuilt

The previous YURA visual generation flow suffered from authority drift and propagation of defects from old generated/Master images.

A major concrete problem was unnatural ear geometry in the previous Master. Reusing that Master as a reference risked reproducing the same defect.

Therefore, the YURA visual domain was reset and rebuilt from separated Authorities instead of continuing to iterate on failed images.

Core principle:

```text
FAILED GENERATED IMAGE -> REFERENCE REUSE = DENIED
```

A failed image must not be fed back into generation as a correction reference.

The rebuild deliberately separated:

- Face identity
- Body geometry
- Composition
- Master-generation text specification

This avoids one reference source accidentally controlling a domain it was never intended to control.

---

# 3. Critical separation from novel material

The novel side and the visual-generation side are intentionally isolated.

`characters/YURA.md` is novel material only.

It is **not** a YURA image-generation Authority.

Do not use any of the following as YURA visual fallback sources:

- `characters/YURA.md`
- `manuscript/**`
- story/novel-side material
- Memory-derived YURA appearance information
- old Git history for YURA visual settings
- old YURA Master images
- rejected generated candidates
- prior generated images unless explicitly promoted to an active Authority

If an approved visual Authority is missing or conflicting, stop rather than silently filling gaps from those sources.

---

# 4. Current YURA Authority architecture

At the current Master-generation phase, Authority is separated as follows.

## 4.1 Face Identity Authority

Approved active files:

```text
visuals/yura/identity/face/YURA_FACE_REFERENCE.png
visuals/yura/identity/face/FACE_REFERENCE_RULES.md
```

Purpose:

- face identity
- face aspect/proportions
- eyes
- brows
- nose
- mouth
- cheeks
- chin
- face-framing hair / bangs
- ear visibility around the face where applicable

Explicitly NOT authoritative for:

- full-body head ratio
- body scale
- perceived height
- shoulder/ribcage/waist/leg scale
- full-body canvas occupancy

Key rule:

```text
FACE_REFERENCE -> BODY_PROPORTION = DENIED
FACE_REFERENCE -> FULL_BODY_SCALE = DENIED
FACE_REFERENCE -> CANVAS_OCCUPANCY = DENIED
```

---

## 4.2 Body Geometry Authority

Approved active files:

```text
visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md
```

Purpose:

- 7.2-head full-body geometry
- head-to-body relative scale
- broad whole-body placement
- vertical placement of major body landmarks
- body geometry QA

The approved geometry guide was constructed and measured as a 7.2-head schematic.

Target:

```text
TARGET = 7.2 heads
ACCEPTABLE RANGE = 7.1–7.3 heads
```

The guide image is geometry-only.

It is NOT face, hair, clothing, expression, or rendering Authority.

Key rule:

```text
BODY_GEOMETRY_GUIDE -> FACE_GEOMETRY = DENIED
BODY_GEOMETRY_GUIDE -> FACE_IDENTITY = DENIED
```

Also important:

The geometry guide image itself uses a 1200×1600 canvas, but that canvas ratio and occupancy are **not** Production composition rules.

---

## 4.3 Composition Authority

Approved active file:

```text
visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md
```

Current fixed Master-generation composition target:

```text
Canvas:             1440 × 2560 px
Aspect ratio:       9:16
Figure occupancy:   89% target
Acceptable:         88–90%
Top margin:         5–6%
Bottom margin:      5–6%
Horizontal center:  fixed to canvas center
```

For 1440×2560:

```text
Target figure height ≈ 2278 px
Center X = 720 px
Top/bottom margin center ≈ 141 px
```

Composition controls placement only.

It must NOT modify face identity or body geometry to make the figure fit.

Key rules:

```text
COMPOSITION -> FACE_IDENTITY = DENIED
COMPOSITION -> BODY_GEOMETRY = DENIED
COMPOSITION -> BODY_WIDTH = DENIED
COMPOSITION -> HEAD_TO_BODY_RATIO = DENIED
```

---

## 4.4 Master-generation text specification

Current file:

```text
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
```

Important lifecycle decision:

**This file is now considered the OpenAI API Master-generation specification.**

It is not intended to remain the normal day-to-day Production text Authority forever.

Its current job is to help generate the new Master accurately.

It includes YURA appearance constraints such as hair, face, body, ears, rendering, pose, and validation requirements.

Ear geometry currently includes a measurable constraint:

```text
Ear target = 20–22% of face vertical dimension
HARD MAX = 23%
```

Head-to-body target remains:

```text
TARGET = 7.2 heads
ACCEPTABLE RANGE = 7.1–7.3
```

Do not reintroduce the abandoned method of mechanically shrinking the head to ~80–81% based on earlier 5.8-head candidates.

That method was intentionally discarded because it risked distorting face identity.

---

# 5. Master-generation lifecycle after a PASS image is found

The lifecycle is documented in:

```text
visuals/yura/identity/master/YURA_MASTER_GENERATION_LIFECYCLE.md
```

The intended transition is:

```text
MASTER PASS
    ↓
commit approved Master image
    ↓
GPT-based visual inspection of the actual Master image
    ↓
create a NEW text description from what is visibly present in that Master
    ↓
YURA_MASTER_VISUAL_DESCRIPTION.md
    ↓
switch normal Production Authority to Master image + Master-derived description
    ↓
archive the Master-generation API package outside normal Production auto-load
```

Planned Master image path:

```text
visuals/yura/identity/master/YURA_VISUAL_MASTER.png
```

Planned Master-derived description:

```text
visuals/yura/identity/master/YURA_MASTER_VISUAL_DESCRIPTION.md
```

The future description must be generated by visually inspecting the approved Master image itself.

It must not invent features or backfill from Memory, novel material, rejected candidates, or old visual configuration.

---

# 6. Future role of the Master-generation API package

After the new YURA Master is established, `YURA_VISUAL_TEXT.md` and the Master-generation tooling should be moved out of normal Production discovery, preferably into a dedicated archive repository or equivalently isolated storage.

It should then be invoked only deliberately for special high-precision jobs such as:

- rebuilding a Master-quality reference
- generating a highly accurate school-uniform standing reference
- generating special two-character reference compositions
- reconstructing visual Authorities
- creating a new exact reference where the normal Master alone is insufficient

The archived Master-generation package must not be silently auto-loaded during ordinary YURA Production generation.

---

# 7. Why Codex is in the loop

Codex is not being asked to creatively decide what YURA looks like.

Its role is to act as a deterministic-ish Git Authority resolver and prompt compiler.

The intended Codex responsibilities are:

1. Resolve current repository HEAD.
2. Read only the approved Authority files.
3. Read them in the configured order.
4. Record file paths and SHA-256 values.
5. Explicitly record denied sources.
6. Produce a machine-readable manifest.
7. Produce the exact compiled generation prompt.

This makes it possible to determine whether variability comes from:

```text
Codex / prompt compile
```

or from:

```text
Image model sampling
```

If 10 runs produce the same `compiled_prompt.sha256`, then prompt compilation is stable and image differences are primarily downstream.

If hashes differ, the prompt compiler itself is unstable and image PASS-rate analysis should be paused until that is fixed.

---

# 8. Benchmark tooling already added

Benchmark directory:

```text
tools/yura-master-benchmark/
```

Current files include:

```text
.gitignore
README.md
authority_manifest.schema.json
codex_instruction.md
config.json
query_project_cost.py
requirements.txt
run_batch.py
run_once.py
```

Purpose:

```text
fixed Git Authority resolution
    ↓
Codex manifest + prompt compile
    ↓
OpenAI Image API generation
    ↓
usage / cost capture
    ↓
QA_PENDING artifact output
```

Generated runs are intended to live under:

```text
tools/yura-master-benchmark/runs/
```

and are excluded from Git.

---

# 9. Benchmark design decisions already made

## 9.1 One run first

Do NOT start with 10 paid generations.

The first experiment must be one run only.

Purpose:

- verify Codex authority resolution
- verify prompt stability infrastructure
- verify image API execution
- inspect one generated candidate
- measure actual cost
- detect configuration/API problems before multiplying them by 10

---

## 9.2 Dedicated OpenAI Project

Recommended setup:

Create a dedicated OpenAI API Project, for example:

```text
yura-master-benchmark
```

Use the same benchmark Project for:

- Codex API-key billing
- OpenAI image-generation billing

Reason:

A dedicated project makes one-run and batch costs easier to attribute.

API keys must never be committed to Git.

Do not paste API keys into chat.

Environment variables are intended to be used locally.

The benchmark scripts expect an `OPENAI_API_KEY`.

For project-cost querying, the tooling also expects the relevant project/admin environment variables documented in the benchmark README.

Before any paid run, verify current official OpenAI API/auth/billing behavior rather than relying on this worklog as evergreen API documentation.

---

## 9.3 Cost measurement

The goal is to measure the complete cost of one benchmark run, not merely estimate the image call.

Desired result example:

```text
run_001
Codex cost:       $X
Image cost:       $Y
Total:            $Z
```

The repository's current benchmark config contains a batch gate.

At the time this worklog was written, the intended default gate was:

```text
max total cost per run for automatic batch = $1.00
```

This is a safety threshold, not a claim that a run will actually cost $1.

The whole reason for the first run is to obtain a real measurement.

---

## 9.4 Ten-run experiment

If the first run is inexpensive enough and technically correct, run 10 independent iterations.

Use one image per request/run rather than requesting all 10 as a single opaque batch.

Each run should retain its own:

- commit
- Authority hashes
- Codex trace
- compiled prompt
- compiled prompt SHA-256
- image result
- usage/cost data
- QA data

Desired final report:

```text
Runs:                   10
Total cost:             ...
Average cost/run:       ...
Prompt hash stable:     x/10
Geometry auto-PASS:     x/10
Author PASS:            x/10
Final yield:            ...%
Cost per accepted image: ...
```

---

# 10. QA strategy already proposed

Automatable/measurable checks should be separated from author visual judgment.

## 10.1 Geometry / composition QA

At minimum:

```text
canvas = 1440×2560 / 9:16
figure occupancy = 88–90%, target 89%
top margin = 5–6%
bottom margin = 5–6%
horizontal centering
head-to-body ratio = 7.1–7.3, target 7.2
```

Composition must not be "fixed" by distorting body geometry.

## 10.2 Identity/appearance visual QA

Then inspect:

- Face Identity match
- ear size/placement constraints
- body width / unwanted body enlargement
- hair identity
- overall YURA impression
- upper-body silhouette relative to the approved specification, without turning the QA into sexualized focus

## 10.3 Final approval

The runner must initially mark generated output as:

```text
candidate = QA_PENDING
master_promotion = NO
```

Only explicit author approval can turn a candidate into a Master candidate PASS.

Do not auto-promote an image because numeric checks passed.

---

# 11. Important generation behavior learned during testing

Several early full-body candidates landed around roughly 5.7–6.5 heads instead of 7.2.

This established that simply writing "7.2 heads" in text is not enough.

The model could instead:

- preserve a large anime head
- enlarge/elongate the body unnaturally
- change perceived body mass
- drift composition

Therefore the solution was **not** to mechanically shrink the approved face.

The solution was to separate:

```text
Face Identity
Body Geometry
Composition
```

and give each domain its own Authority.

This separation should be preserved in future proposals.

---

# 12. Proposal style / decision-making pattern used so far

A new assistant/chat should continue proposing changes with the following pattern.

## 12.1 Prefer measurable constraints over vague prose

Examples already adopted:

```text
7.2 heads, acceptable 7.1–7.3
Ear target 20–22%, HARD MAX 23%
Figure occupancy target 89%, acceptable 88–90%
Top/bottom margins 5–6%
Canvas 1440×2560
```

When a visual problem can be converted into a measurable constraint, propose that before adding more descriptive adjectives.

## 12.2 Separate Authorities instead of letting one image control everything

When one reference is good for one domain but bad for another, do not discard the good domain and do not let it control the bad domain.

Create explicit Authority separation.

Example:

```text
Face reference -> face only
Body geometry guide -> body proportions only
Composition Authority -> placement only
```

## 12.3 Fail closed on conflicts

Do not "average" conflicting Authorities.

Do not use hidden fallback sources.

If Authority resolution cannot be verified, stop before generation.

## 12.4 Do not iterate by feeding failed images back

Rejected candidates are not future references.

Change text/geometry/composition Authorities and regenerate from the authoritative sources instead.

## 12.5 Preserve author-approved good components

A good face should not be redesigned merely to satisfy full-body geometry.

Fix the domain that is wrong.

## 12.6 Measure cost before scaling

Do one paid run, measure real cost, then decide whether 10-run automation is worthwhile.

## 12.7 Keep archive/Production roles explicit

Generation bootstrap specifications and final Production Authorities are different artifacts and should not be mixed after Master promotion.

---

# 13. Current local Git state immediately before this worklog was added

The user's local repository was synchronized successfully to:

```text
3323fa0 Document YURA master benchmark workflow
```

At that point:

```text
HEAD -> main
origin/main -> same commit
```

There is intentionally one unrelated local unstaged change:

```text
manuscript/episode-001/EP001_DRAFT.txt
```

This novel draft must not be modified, discarded, committed, reset, or included in YURA visual work.

The safe sync procedure previously used successfully was:

```powershell
git stash push -m "WIP EP001 before YURA benchmark sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Do not use `git reset --hard` or force push as a shortcut.

Because this worklog itself is being added to GitHub after that local sync, the user's local copy will need one more safe pull before continuing.

---

# 14. Current environment/setup progress

Completed locally:

```powershell
python -m pip install -r tools/yura-master-benchmark/requirements.txt
```

Observed result:

```text
openai 3.24.0 installed successfully
Python environment is Python 3.12 on Windows
```

The install produced PATH warnings for auxiliary executables such as `idna.exe` and `httpx2.exe`.

Those warnings were considered non-blocking for the benchmark because the runner imports the Python SDK directly.

No paid benchmark run has been intentionally started yet.

---

# 15. EXACT CURRENT STEP

**We are currently at the preflight/authentication-verification stage immediately before creating/configuring the dedicated OpenAI benchmark Project and before the first paid run.**

The next checks that were proposed were:

```powershell
python -c "import openai; print(openai.__version__)"

codex --version

codex login status
```

Purpose:

1. confirm Python OpenAI SDK version
2. confirm Codex CLI is installed and callable
3. determine current Codex authentication mode

Do not skip directly to `run_once.py` until authentication/project billing configuration is understood.

---

# 16. Next actions, in order

A new chat should resume from here.

## Step 1 — sync this worklog to local safely

Because this file was committed remotely after the previous local sync, protect the unrelated EP001 draft and pull current main.

Recommended pattern:

```powershell
git stash push -m "WIP EP001 before YURA worklog sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Then confirm:

```powershell
git log -1 --oneline
git status
```

Expected status: only the existing `EP001_DRAFT.txt` local modification should remain.

## Step 2 — verify SDK/Codex CLI

Run:

```powershell
python -c "import openai; print(openai.__version__)"
codex --version
codex login status
```

Inspect the results before changing authentication.

## Step 3 — verify current official OpenAI API model/auth/billing details

Before a paid run, check current official OpenAI documentation for:

- Codex CLI API-key authentication flow
- current supported Codex API model name
- current image model name and image-edit/reference API behavior
- whether the configured custom image size is currently accepted
- current pricing
- Project/usage/cost API behavior

The repository currently contains a frozen benchmark configuration, but external API products can change.

If current official API reality differs from `config.json`, update the config in a new explicit commit before running the benchmark.

Do not silently substitute a model or endpoint at runtime.

## Step 4 — create/use a dedicated OpenAI Project

Recommended project purpose/name:

```text
yura-master-benchmark
```

Keep Codex and image-generation API activity attributable to the same benchmark Project where supported.

Set appropriate environment variables locally.

Never commit or paste secret keys.

## Step 5 — verify Codex is using the intended billing/auth mode

The experiment only answers "what does one full run cost?" if Codex usage is measured consistently with the intended API billing setup.

If Codex remains on ChatGPT-plan authentication while the image call uses API billing, record that explicitly; do not pretend it is a unified per-run dollar cost.

## Step 6 — perform ONE run only

Only after all preflight checks pass:

```powershell
python tools/yura-master-benchmark/run_once.py
```

Do not start 10 runs yet.

## Step 7 — inspect artifacts before any batch

Verify:

- Git commit matches current main
- Authority paths/order are correct
- Authority SHA-256 values match
- denied sources are present
- compiled prompt is complete
- compiled prompt contains no novel/Memory/old-Master leakage
- result image exists
- usage logs exist
- cost data can be attributed correctly
- candidate remains QA_PENDING

## Step 8 — measure authoritative cost

Use the benchmark cost-query tooling as documented in:

```text
tools/yura-master-benchmark/README.md
```

Do not treat an estimate as authoritative if Project cost data is available.

## Step 9 — visually/quantitatively QA the one candidate

Measure head-to-body ratio and Composition.

Then inspect face/ears/body/hair/overall identity.

Record PASS/FAIL without using the failed candidate as a future reference.

## Step 10 — decide whether to run 10

Only if:

- technical pipeline is correct
- Authority resolution is correct
- cost is acceptable
- user explicitly wants the 10-run test

Then run independent iterations and compare `compiled_prompt.sha256` across runs.

---

# 17. Benchmark files to read first in a new chat

For operational continuation, inspect these first:

```text
tools/YURA_MASTER_GENERATION_WORKLOG.md
tools/yura-master-benchmark/README.md
tools/yura-master-benchmark/config.json
tools/yura-master-benchmark/codex_instruction.md
tools/yura-master-benchmark/run_once.py
tools/yura-master-benchmark/run_batch.py
```

For YURA generation Authority, inspect only the files explicitly listed by the benchmark configuration and lifecycle rules.

Do not infer Authority merely because a file exists elsewhere in the repository.

---

# 18. Important caution about current benchmark configuration

At the time this worklog was created, `tools/yura-master-benchmark/config.json` contained explicit model identifiers and a pricing snapshot.

Those values are benchmark inputs, not timeless facts.

Before the first paid run, verify them against current official OpenAI documentation.

If any value is no longer valid, change it deliberately in Git, explain why, and treat the changed commit as a different benchmark condition.

Reproducibility requires that model/config changes be versioned rather than silently substituted.

---

# 19. What NOT to do next

Do not:

- run a 10-image experiment before the one-run cost check
- use rejected generated candidates as references
- use `characters/YURA.md` for visual generation
- use manuscript files for visual generation
- use Memory-derived appearance data
- pull old YURA settings from Git history as fallback
- redesign the approved face just to hit 7.2 heads
- distort the body to satisfy Composition
- use the Body Geometry Guide's 3:4 canvas as Production composition
- auto-promote a candidate to Master
- archive `YURA_VISUAL_TEXT.md` before the new Master is actually approved and promoted
- modify or lose `manuscript/episode-001/EP001_DRAFT.txt`
- commit API keys
- expose secret keys in chat
- silently switch API models/endpoints when current configuration fails

---

# 20. Definition of success for the current experiment

The current benchmark phase is successful if we can produce a report that answers all of the following with evidence:

```text
1. Which exact Git commit was used?
2. Which exact Authority files were read, and in what order?
3. What were their SHA-256 values?
4. Was the compiled prompt stable?
5. What did one complete run cost?
6. Did the generated image meet 7.2-head geometry?
7. Did it meet Composition targets?
8. Did it preserve YURA Face Identity?
9. Did it respect ear/body/hair constraints?
10. If 10 runs were executed, how many passed?
11. What was the cost per accepted image?
```

The purpose is not merely to produce many images.

The purpose is to establish a reproducible, auditable way to produce a high-confidence YURA Master or other special high-precision reference images when needed.

---

# 21. Short resume instruction for a new chat

If a new chat reads this document, resume with this assumption:

```text
The YURA visual Authority rebuild is already well advanced.
Face, Body Geometry, Composition, Master-generation lifecycle, and benchmark tooling already exist.
Do not redesign the architecture from scratch.
The current task is preflight/auth verification for the first single paid benchmark run.
First sync current main safely, preserve EP001_DRAFT.txt, verify Codex/OpenAI API configuration against current official docs, then run exactly ONE benchmark iteration and inspect cost + QA before proposing a 10-run batch.
```
