# YURA Master Benchmark — Current Handoff

Status: **ACTIVE / HANDOFF CHECKPOINT / BODY GEOMETRY CALIBRATION IN PROGRESS**

This file is operational documentation only. It is **NOT** a YURA visual Authority.

## Mandatory recovery document

Before continuing this benchmark in a new chat, read:

- `tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md`

That runbook records the PowerShell commands, Git synchronization procedure, local benchmark execution, sealed Authority/prompt workflow, QA commands, Composition gate, face audit execution, GitHub-side assistant work, and the new-chat recovery sequence used in this project.

Use together with:

- `tools/yura-master-benchmark/PIPELINE_STATE.md`
- `visuals/MASTER_CREATION_WORKFLOW.md`

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

## Next paid-test strategy

Before any further paid generation, perform exact landmark measurement on the original local `result_raw.png`.

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

This is deferred until base geometry is stable.

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

## Immediate handoff instructions for the next chat

1. Read current Git `main` before changing anything.
2. Read `tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md` first, then this file, `PIPELINE_STATE.md`, and `visuals/MASTER_CREATION_WORKFLOW.md`.
3. Preserve the unrelated local `manuscript/episode-001/EP001_DRAFT.txt` change; do not commit, discard, or edit it.
4. Sync the latest documentation commits to local using the existing stash/pull/pop pattern recorded in the runbook.
5. Locate the original local promising `result_raw.png` run.
6. Measure exact `crown / chin / crotch / knee / soles` Y coordinates on the original file.
7. Compute exact head ratio, inseam proxy, torso span, and knee split.
8. Do not run Composition and do not launch another paid RAW until that measurement has been reviewed.
9. After measurement, decide the first paid hypothesis test: preserve the successful internal balance while testing whether Face Identity can be decoupled from total head/body scale so 7.2 heads becomes attainable.
