# YURA Master Benchmark — Current Handoff

Status: **ACTIVE / HANDOFF CHECKPOINT / MASTER-IMAGE-ONLY SCOPE LOCK / BODY GEOMETRY CALIBRATION IN PROGRESS**

This file is operational documentation only. It is **NOT** a YURA visual Authority.

## Mandatory recovery document

Before continuing this benchmark in a new chat, read:

- `tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md`

That runbook records the PowerShell commands, Git synchronization procedure, local benchmark execution, sealed Authority/prompt workflow, QA commands, Composition gate, face audit execution, GitHub-side assistant work, and the new-chat recovery sequence used in this project.

Use together with:

- `tools/yura-master-benchmark/PIPELINE_STATE.md`
- `visuals/MASTER_CREATION_WORKFLOW.md`

---

# HARD SCOPE LOCK — MASTER IMAGE CREATION ONLY

## Sole project objective in this workflow

The purpose of this workflow is **to create the final high-quality YURA Master image, with generation drift reduced to the smallest practical level**.

Everything done in this benchmark must be directly necessary for that objective.

Allowed work is limited to:

```text
YURA Master image generation
Face Identity / Face Geometry work required for the Master
Body Geometry work required for the Master
Master-construction visual text
controlled generation experiments required to improve the Master
numeric / visual QA required to judge the Master
prompt compiler / invariant / benchmark code required to run those tests
Authority and lifecycle documents required to make the Master reproducible
deterministic final Composition required for the Master
Git / PowerShell / cost / run-artifact work directly required to execute and audit the Master workflow
```

Anything outside this list is out of scope unless the author explicitly orders it.

## Explicitly forbidden scope diversion

Without an explicit author instruction, DO NOT switch to, propose as a replacement task, or begin work on:

```text
school-uniform Master / 制服マスタ
outfit Master
pose pack
production illustration set
story / manuscript work
scene illustration work
other character Master work
SHIORI / MIO generation
production deployment work unrelated to finishing the current YURA Master
"while we are here" side work
any alternate deliverable that substitutes for finishing the current Master
```

SHIORI, MIO, school-uniform work, pose/view anti-drift work, and other downstream work may be documented as future reuse targets, but **they must not replace or interrupt the active YURA Master task unless the author explicitly changes the objective**.

## Historical failure that must not recur

A prior failure mode was:

```text
YURA Body test was in progress
-> chest-related Master text was deliberately changed for that controlled test
-> the test was not completed
-> later discussion drifted toward proposals such as school-uniform Master work
```

That is prohibited scope drift.

If a controlled test variable has been changed — for example chest/body text, head-scale invariants, Body Geometry wording, Face-reference scale separation, or another Master parameter — that test becomes the active experiment and must be carried through its defined completion path unless the author explicitly cancels or replaces it.

Default completion path:

```text
requested change
-> smallest necessary diff
-> commit / sync
-> free preflight
-> inspect compiled_prompt.txt and prompt_invariant_check.json
-> exactly one paid RAW when authorized
-> measure / inspect the result
-> record result and decision in Git
-> only then move to another hypothesis
```

Do **not** leave a test half-applied and silently move to another topic.

## No autonomous reinterpretation

The assistant must not reinterpret the author's goal into a different goal because it appears more convenient, more general, more reusable, more aesthetically interesting, or easier to complete.

Rules:

```text
AUTHOR EXPLICIT INSTRUCTION > assistant preference
CURRENT ACTIVE TEST > unsolicited alternative task
MASTER COMPLETION > downstream asset creation
EXACT REQUESTED VARIABLE > inferred substitute variable
```

Do not convert:

```text
"test this chest/body text change"
into
"make a uniform Master instead"

"finish YURA Master"
into
"start work that may be useful later"

"keep 7.2 and test scale decoupling"
into
"accept 6.4 because the model seems to prefer it"
```

If the author's instruction is technically possible and safe, execute it as written.

If a genuinely blocking ambiguity exists, ask only about that ambiguity. Do not fill the gap with an unrelated plan.

If a test fails, diagnose the failure. Do not use failure as permission to change the project objective.

## Active-test continuity rule

Before suggesting or starting a new experiment, confirm all three:

```text
1. What is the active Master hypothesis/test?
2. Has its requested change actually been executed and measured?
3. Has the author accepted, rejected, cancelled, or replaced that test?
```

If #2 or #3 is NO, continue the existing test. Do not branch into another task.

## New-chat mandatory behavior

A new chat must not merely read these files and then improvise.

Before making changes, it must reconstruct and state internally from current Git:

```text
MASTER OBJECTIVE
CURRENT ACTIVE TEST
WHAT HAS ALREADY BEEN CHANGED
WHAT HAS NOT YET BEEN EXECUTED
NEXT REQUIRED COMMAND / DIFF
FORBIDDEN SIDE WORK
```

The next action must advance the current YURA Master test, not invent a new project direction.

---

## Primary objective

Create a **high-quality YURA visual Master while reducing generation drift and stochastic variance to the smallest practical level**.

The target is not merely one attractive image. The completed method should make the desired identity and body geometry reproducible enough that later Masters for SHIORI, MIO, and other characters can be created with much less exploratory waste.

Additional operational goals:

- preserve explicit author intent instead of generic anime/model defaults;
- make Face Identity, Body Geometry, Composition, rendering, and local refinements independently diagnosable;
- turn useful subjective judgments into measurable calibration values;
- keep failed candidates out of future visual Identity/Geometry Authority unless explicitly promoted;
- make Authority inputs, hashes, prompt compilation, QA, and promotion auditable;
- spend paid generations on hypothesis testing rather than random rerolls;
- carry the method to later characters without copying YURA-specific proportions.

These additional goals are subordinate to the sole active deliverable: **finish the YURA Master image**. They are not independent projects.

## Current strategic decision

The remaining benchmark budget may be used aggressively on YURA **if each paid generation removes a specific uncertainty and improves the reusable process**.

The intended discipline is:

```text
one paid RAW
= one explicit hypothesis
= one measurable result
= one decision
```

Do not spend paid calls repeatedly sampling the same unchanged setup just to look for a lucky image.

The value of the YURA work is partly methodological: if the process is solved here, later characters should begin from a mature pipeline instead of repeating the same discovery work. A practical aspiration is that later character Masters can be completed within a small, controlled generation budget (for example roughly USD 5–10), but this is a planning target rather than a guaranteed cost.

## Current Body Geometry conclusion

The latest promising RAW after replacing the Body Geometry guide was visually much better than previous attempts:

- torso no longer reads obviously elongated;
- pelvis/crotch reads higher;
- lower body reads longer;
- overall full-body balance is much closer to author intent.

This RAW is **not** a Master, PASS, or visual reference. It is currently a **measurement/calibration sample**.

Preliminary measurement on the uploaded 1152×2048 copy was approximately:

```text
crown   ≈ y 59
chin    ≈ y 360
crotch  ≈ y 1000
knee    ≈ y 1368
soles   ≈ y 1976

head ratio          ≈ 6.37 heads
inseam proxy        ≈ 50.9%
chin→crotch         ≈ 2.13 heads
crotch→knee share   ≈ 37.7% of crotch→soles
knee→soles share    ≈ 62.3% of crotch→soles
```

These values are **preliminary**, because final calibration must be made from the original local `result_raw.png`, not from a displayed/downscaled copy.

The important observation is that the visually preferred balance appears to be materially different from the currently active runtime gate of 46.0–46.5% inseam and 7.1–7.3 total heads.

## Head-ratio decision

The author preference is to keep **7.2 heads** as the final target if practical.

Reason:

- YURA should eventually coexist visually with SHIORI, MIO, and the rest of the cast;
- a shared, controlled head-count standard helps reduce subtle cross-character scale mismatch;
- abandoning the standard too early would make later cast-level alignment harder to reason about.

However, repeated generations across the last two days have tended to land around roughly **6.4 heads** when using the Face Identity reference. This suggests a possible model/reference bias:

```text
Face Identity image reference
  -> may influence apparent head size / head-to-body scale
  -> Body Geometry requests 7.2 heads
  -> generated body repeatedly converges nearer ~6.4 heads
```

This is a hypothesis, not yet proven.

Therefore:

**Do not abandon 7.2 heads yet.**

Treat 7.2 as the desired final/cross-character standard while testing whether the Face Identity reference can be decoupled from head-to-body scale.

## Current interpretation of the promising RAW

The promising RAW may contain two separable signals:

```text
A. internal upper/lower-body balance
   -> visually successful
   -> likely valuable calibration evidence

B. total head ratio
   -> still around ~6.4 in preliminary measurement
   -> likely not the final desired standard
```

The next target is therefore not simply “copy this RAW.”

The better target is:

```text
preserve the successful torso / pelvis / lower-body balance
+ retain Face Identity
+ move total head ratio toward 7.2
```

## Test 1 execution result — 2026-10-10

Test 1 (Face Identity vs head/body scale decoupling) was executed after:

- adding the existing Face-reference scale-denial rules to the compiled-prompt contract;
- enforcing those rules in `REQUIRED_PROMPT_INVARIANTS`;
- adding `性的な強調を目的としない` as the approved non-sexual-intent statement.

Free preflight:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
git_commit = b9ea99d29a5e8f18f8a853e4ab0a0302a6f70715
```

Paid RAW:

- Image API generation succeeded; no moderation block occurred.
- local `result_raw.png` dimensions were confirmed as 1440×2560.
- Composition was not run.

Preliminary landmark measurement from the uploaded 1152×2048 proportional display copy:

```text
head ratio      ≈ 6.51 heads
inseam proxy    ≈ 51.8%
chin→crotch     ≈ 2.13 heads
```

Current-gate result:

```text
7.1–7.3 head ratio              = FAIL
46.0–46.5% inseam proxy         = FAIL
2.7985–2.9420 chin→crotch range = FAIL
```

Decision:

Test 1 did not decouple Face-reference influence strongly enough to reach 7.2 heads.
The result remains a QA/calibration sample only and MUST NOT become visual Authority.
Composition remains blocked.

Next active test:

**Test 2 — diagnostic A/B isolation of Face-reference influence, as already defined below.**

Do not change existing Body information while setting up Test 2.

## Next paid-test strategy

Before any further paid generation, perform exact landmark measurement on the original local `result_raw.png` unless current Git contains a newer explicit active test state.

Then proceed one variable at a time.

### Test 1 — decouple Face Identity from head/body scale

Keep the same Face Identity and Body Geometry Authorities, but strengthen the prompt/invariant contract so that the Face reference explicitly has **no authority** over:

```text
head-to-body scale
head vertical size
total head count
body proportions
```

The Body Geometry Authority must exclusively determine total head count and body scale.

Conceptually the prompt contract should communicate:

```text
FACE REFERENCE DEFINES FACIAL IDENTITY ONLY.
IT DOES NOT DEFINE HEAD-TO-BODY SCALE OR TOTAL HEAD COUNT.
HEAD VERTICAL SIZE FOR FULL-BODY PROPORTION IS GOVERNED BY BODY GEOMETRY.
CROWN-TO-SOLES TARGET REMAINS 7.2 CROWN-TO-CHIN HEAD UNITS.
```

Run free preflight first, then exactly one paid RAW.

### Test 2 — A/B diagnose Face-reference influence if needed

If Test 1 still converges near ~6.4 heads, perform one **diagnostic-only** controlled RAW in which Face image influence is removed or otherwise isolated while Body Geometry remains the main variable.

Purpose:

```text
if body moves materially toward 7.2
  -> Face reference is strongly influencing head/body scale

if body still remains near ~6.4
  -> likely model/body-generation bias or insufficient Body Geometry enforcement
```

A diagnostic RAW does not become a visual reference or Master candidate automatically.

### Test 3 — solve the identified layer only

Once the cause is known, adjust only that layer and repeat one controlled RAW.

Do not change Face Identity, Body Geometry, Composition, and rendering simultaneously.

## Numeric calibration policy

Numeric gates are calibration instruments, not sacred constants.

If exact measurement confirms that the visually preferred YURA lower-body balance is nearer ~50% inseam than 46%, the inseam target may be recalibrated **after explicit author approval**.

But do not conflate inseam calibration with total-head calibration.

It is valid to target something like:

```text
successful long-leg / compact-torso internal balance
+ 7.2 total heads
```

rather than copying the promising RAW's total head count unchanged.

Any approved recalibration must update the full chain together:

```text
Body Geometry Authority image/text
benchmark config
body_geometry_qa.py
Codex instruction / prompt invariants
runner validation
Composition gate validation
free preflight
then one paid RAW
```

## Face audit status

A dedicated Face Geometry audit/revision lifecycle now exists:

```text
visuals/yura/identity/face/FACE_GEOMETRY_REVISION_LIFECYCLE.md
visuals/yura/identity/face/YURA_FACE_GEOMETRY_AUDIT.md
```

Numeric audit of the active Face Reference has been executed. Current conclusion:

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

Broad Face redesign is not justified. Ear refinement is intentionally deferred.

The later ear solution should also address generation behavior that tries to expose/show ears during oblique views or pose changes. Ear visibility should be incidental, and hair may naturally hide the ears.

## Pose/view anti-drift issue queued for later

After base full-body stability, address pose/view transformations such as squatting, leaning, and 45-degree/oblique poses where the model may stretch body regions or alter ear visibility.

Desired separation:

```text
BASE GEOMETRY = locked
POSE TRANSFORM = pose only
VIEW ANGLE TRANSFORM = view only
FORBIDDEN DRIFT = no redesign of head count, torso length, leg length, face-feature layout, or ear prominence
```

This is deferred until base geometry is stable and must not replace the active YURA Master test.

## Composition remains blocked

Do not run final Composition while Body Geometry is still under calibration.

Composition must remain deterministic and may not repair anatomy by nonuniform transforms, part scaling, warp, inpainting, or face regeneration.

## Definition of success for YURA

The intended completion state is approximately:

```text
Face Identity      stable
Body Geometry      author-approved and measurably reproducible
Total head ratio   preferably 7.2 / accepted project standard
Internal balance   author-approved torso/pelvis/leg balance
Variance           low enough that acceptable results do not depend on luck
Composition        deterministic
Face details        final local issues such as ears refined after body stability
Final QA            PASS
Author approval      explicit PASS
Master promotion     completed
```

## Reuse for SHIORI / MIO / later characters

Reuse the **process**, not YURA's numeric values.

This is a future benefit only. It is **not permission to start those characters before the YURA Master objective is completed or the author explicitly redirects the work**.

The desired long-term payoff is:

```text
YURA
  -> spend experimentation budget to discover robust method

SHIORI / MIO / later characters
  -> start with established Authority separation
  -> explicit Body Geometry guide and internal boundaries
  -> one-hypothesis-per-paid-RAW discipline
  -> measurement-driven calibration
  -> free preflight before payment
  -> fewer paid iterations
  -> high-quality, lower-variance Master creation
```

## Test 3 completion checkpoint — 2026-10-10

Test 3 completed.
Face Reference restoration preserved Face Identity direction, but explicit Body Guide landmark enforcement still produced approximately 6.47 heads rather than the required 7.1–7.3.

Test 3 = FAIL for Body Geometry.
Composition remains blocked.
Test 3 RAW is diagnostic only and is not Visual Authority.

No Test 4 hypothesis is active yet.
Do not change Face Identity, Body Authority, numeric gates, Composition, or rendering until the author explicitly approves the next controlled hypothesis.

## Immediate handoff instructions for the next chat

1. Read current Git `main` before changing anything.
2. Read `tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md` first, then this file, `PIPELINE_STATE.md`, and `visuals/MASTER_CREATION_WORKFLOW.md`.
3. Read the **HARD SCOPE LOCK** in this file and treat it as operationally mandatory.
4. Preserve the unrelated local `manuscript/episode-001/EP001_DRAFT.txt` change; do not commit, discard, or edit it.
5. Determine the exact currently active YURA Master test from current Git. Do not infer it from memory if Git has advanced.
6. Identify what change was already made for that test and what execution/measurement step remains unfinished.
7. Continue that test to completion. Do not substitute school-uniform Master, other-character work, pose packs, or another side task.
8. Sync GitHub/local using the existing stash/pull/pop pattern recorded in the runbook when needed.
9. If the active test requires code/Authority changes, make only the smallest diff necessary.
10. Run free preflight and inspect `compiled_prompt.txt` + `prompt_invariant_check.json` before any paid RAW.
11. Only after PASS and author authorization, run exactly one paid RAW for the active hypothesis.
12. Measure the original RAW, not a downscaled chat display.
13. Record result and decision in Git.
14. Do not run Composition until Body Geometry passes.
15. Do not move to a new hypothesis until the active test is explicitly completed, rejected, cancelled, or replaced by the author.
