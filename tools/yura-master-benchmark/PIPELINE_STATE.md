# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / BODY-GEOMETRY-FIRST / HEAD-RATIO+INTERNAL-LANDMARK-GATED / COMPOSITION-DEFERRED**

This file is operational documentation only. It is **NOT** a YURA visual Authority.

## Current execution order

```text
current Git main
  -> local runner verifies HEAD == origin/main
  -> configured Authority files only
  -> sealed Authority bundle + SHA-256
  -> Codex compiles RAW Body-Geometry-first Image API prompt
  -> runner rejects prompt if required Body Geometry contract is missing
  -> runner rejects prompt if final Composition numeric targets leaked into it
  -> Image API generates result_raw.png only
  -> body_geometry_qa.py
       manually reviewed crown/chin/crotch/knee/soles Y landmarks
       total head ratio = (soles - crown) / (chin - crown)
       target = 7.2
       acceptable = 7.1–7.3
       internal landmark metrics are recorded
       author review must confirm:
         upper body not vertically elongated
         pelvis/crotch slightly high and lower body subtly longer
         knee placement natural / not leg-only stretching
       RAW SHA-256 is bound into body_geometry_qa.json
     -> FAIL: stop; Composition blocked
     -> PASS: explicit Body Geometry confirmation still required
  -> normalize_composition.py verifies Body Geometry PASS + RAW SHA match
  -> uniform whole-raster scale + x/y translation only
  -> result.png at final Composition target
  -> final QA / author confirmation
  -> Master promotion remains NO until explicit final PASS
```

## Current Body Geometry intent

The active Body Geometry Authority still fixes total height at:

```text
TARGET = 7.2 heads
ACCEPTABLE = 7.1–7.3 heads
ONE HEAD = crown to chin
```

The author has additionally clarified the internal vertical balance:

```text
UPPER BODY MUST NOT BE VERTICALLY ELONGATED.
KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.
LOW SITTING-HEIGHT IMPRESSION = RELATIVELY COMPACT UPPER-BODY SPAN + SLIGHTLY LONGER LOWER BODY.
DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.
```

“Low sitting height” is only shorthand. In standing full-body generation it operationally means a relatively compact chin-to-crotch / torso span, a slightly high pelvis/crotch position, and a subtly longer crotch-to-soles lower body, while preserving natural knee placement.

This is **not** permission to create an extreme fashion-model body or to lengthen only the legs.

## Why the QA now includes internal vertical landmarks

Total head ratio alone can miss a bad internal distribution. A candidate can approach 7.2 heads while still having an overlong neck/torso/pelvis stack, an overly low crotch, or an unnatural thigh/shin distribution.

Therefore RAW QA now records:

```text
crown
chin
crotch / pelvis-line proxy
knee
soles
```

and derives:

```text
head_ratio_heads
crown_to_crotch_heads
chin_to_crotch_heads
crotch_to_knee_heads
knee_to_soles_heads
crotch_to_soles_heads
knee_from_crown_heads
lower_body_share_of_figure
```

The total 7.1–7.3 head-ratio range remains a hard numeric gate.

The active Authority does not yet define author-approved absolute numeric thresholds for crotch/knee placement. The benchmark therefore **does not invent those thresholds**. Until an approved good reference is numerically frozen, internal landmark values are measured and recorded, and explicit author review is required for the upper/lower-body balance.

## RAW Image API responsibility

The RAW Image API prompt contains Face Identity, Body Geometry, appearance, pose and complete full-body visibility requirements.

It does **not** contain final Composition numeric targets such as 1440×2560, 89% occupancy, 88–90%, or 5–6% margins. Those values remain in the active Composition Authority and operational postprocess config, but are intentionally withheld from the RAW generation prompt so the image model does not optimize anatomy for canvas fitting.

The RAW Body Geometry prompt explicitly includes the total head-ratio contract and the compact-upper-body / subtly-longer-lower-body intent.

## Hard prompt gate

Before Image API is called, the runner requires all RAW-stage invariants and rejects any compiled prompt that contains deferred final-Composition literals.

Failure at this gate means:

```text
Image API called = false
```

## Files produced by a successful RAW run

```text
result_raw.png
composition_deferred.json
qa.json
cost.json
compiled_prompt.txt
compiled_prompt.sha256
prompt_invariant_check.json
```

`result.png` is intentionally absent at this stage.

## Body Geometry QA command

After visually locating the five vertical landmarks on `result_raw.png`, record them with:

```powershell
python tools/yura-master-benchmark/body_geometry_qa.py <RUN_DIR> `
  --crown-y <Y> `
  --chin-y <Y> `
  --crotch-y <Y> `
  --knee-y <Y> `
  --soles-y <Y> `
  --confirm-landmarks-reviewed `
  --confirm-upper-body-not-elongated `
  --confirm-lower-body-slightly-longer `
  --confirm-knee-placement-natural
```

Do not supply a confirmation flag if the RAW does not actually satisfy that condition. A missing confirmation makes the Body Geometry report FAIL and keeps Composition blocked.

The tool writes `body_geometry_qa.json` and binds it to the exact `result_raw.png` SHA-256.

## Body Geometry -> Composition gate

Plan only, no final image:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR>
```

Final normalization is allowed only when all of the following hold:

```text
body_geometry_qa.json exists
status == PASS
pass == true
head ratio is inside 7.1–7.3
crown/chin/crotch/knee/soles were reviewed
upper_body_not_elongated == true
lower_body_slightly_longer == true
knee_placement_natural == true
body_geometry_qa.raw_sha256 == current result_raw.png SHA-256
qa.json body_geometry_status == PASS
qa.json body_geometry_internal_review_pass == true
--confirm-body-geometry-pass was explicitly supplied
```

Then:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR> --confirm-body-geometry-pass
```

creates `result.png` only if deterministic Composition QA also passes.

## Allowed final Composition transforms

Only:

- uniform whole-raster scaling
- x/y translation
- white-background crop/pad implied by final canvas placement

Never:

- nonuniform scaling
- body-part scaling
- warp
- content-aware deformation
- inpainting/body reshaping
- face regeneration

## Current next step

Sync latest main while preserving the unrelated local novel draft. Run syntax checks for:

```text
body_geometry_qa.py
normalize_composition.py
run_raw_once.py
run_once.py
```

Then run the free preflight only. The expected preflight must show both the internal-landmark Body Geometry gate and deferred Composition, with `paid_model_calls = 0`.
