# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / BODY-GEOMETRY-FIRST / HEAD-RATIO+INSEAM+TORSO-GATED / COMPOSITION-DEFERRED**

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
       target = 7.2; acceptable = 7.1–7.3
       inseam proxy = (soles - crotch) / (soles - crown)
       YURA target = 46.0–46.5%
       >=47.0% = model-like hard FAIL
       chin-to-crotch torso span must fit the derived 2.7985–2.9420-head envelope
       author review must confirm:
         upper body not vertically elongated
         torso compact
         waist not unnaturally low
         pelvis/crotch slightly high
         lower body subtly longer
         knee placement natural / not leg-only stretching
       RAW SHA-256 is bound into body_geometry_qa.json
     -> FAIL: stop; Composition blocked
     -> PASS: explicit Body Geometry confirmation still required
  -> normalize_composition.py verifies all Body Geometry gates + RAW SHA match
  -> uniform whole-raster scale + x/y translation only
  -> result.png at final Composition target
  -> final QA / author confirmation
  -> Master promotion remains NO until explicit final PASS
```

## Current Body Geometry intent

The active Body Geometry Authority fixes total height at:

```text
TARGET = 7.2 heads
ACCEPTABLE = 7.1–7.3 heads
ONE HEAD = crown to chin
```

The author-approved internal balance is now also numerically frozen for the image-space inseam proxy:

```text
inseam_proxy_ratio = (soles_y - crotch_y) / (soles_y - crown_y)
PASS TARGET = 46.0–46.5%
47.0% OR MORE = HARD FAIL / TOO MODEL-LIKE
```

This is a **YURA-specific image-space QA proxy**, not a claim about a universal human-body standard.

The active Authority also requires:

```text
UPPER BODY MUST NOT BE VERTICALLY ELONGATED.
TORSO MUST BE COMPACT; DO NOT LENGTHEN THE RIBCAGE-TO-PELVIS OR WAIST SPAN.
KEEP THE PELVIS/CROTCH POSITION SLIGHTLY HIGH, WITH A SUBTLY LONGER LOWER BODY.
LOW SITTING-HEIGHT IMPRESSION = RELATIVELY COMPACT UPPER-BODY SPAN + SLIGHTLY LONGER LOWER BODY.
DO NOT CREATE THE LOWER-BODY EMPHASIS BY LEG-ONLY STRETCHING.
```

“Low sitting height” is shorthand only. In standing full-body generation it operationally means compact torso, waist not low, pelvis/crotch slightly high, and lower body subtly longer while preserving natural knee placement.

## Torso-specific numeric gate

Given the approved total-head range and inseam proxy target, the corresponding audited `chin→crotch` torso span is:

```text
2.7985–2.9420 heads
```

This envelope is mathematically derived from the already approved ranges; it is not an independently invented body ratio.

Therefore a candidate fails Body Geometry if:

```text
chin_to_crotch_heads < 2.7985
or
chin_to_crotch_heads > 2.9420
```

Even when the numeric torso span is inside the envelope, the author visual gate can still fail a candidate if the ribcage/waist/pelvis stack looks elongated or unnatural.

## Why the QA uses multiple gates

Total head ratio alone can miss a bad internal distribution. A candidate can approach 7.2 heads while still having an overlong torso, low waist/pelvis, or an unnatural thigh/shin distribution.

The prior RAW diagnosis exposed exactly this failure mode: the body could improve toward the total target yet the torso still looked visibly too long.

Therefore RAW QA records:

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
inseam_proxy_ratio
inseam_proxy_percent
```

Hard numeric gates now cover:

```text
head ratio = 7.1–7.3
inseam proxy = 46.0–46.5%
model-like guard = >=47.0% FAIL
chin-to-crotch torso span = 2.7985–2.9420 heads
```

Knee placement still has no independently author-approved absolute numeric threshold, so the benchmark does not invent one; it remains an explicit visual review gate.

## RAW Image API responsibility

The RAW Image API prompt contains Face Identity, Body Geometry, appearance, pose and complete full-body visibility requirements.

It does **not** contain final Composition numeric targets such as 1440×2560, 89% occupancy, 88–90%, or 5–6% margins. Those values remain in the active Composition Authority and operational postprocess config, but are intentionally withheld from the RAW generation prompt so the image model does not optimize anatomy for canvas fitting.

The RAW Body Geometry prompt explicitly includes total head ratio, compact torso, slightly high pelvis, YURA inseam proxy 46.0–46.5%, and the >=47% model-like guard.

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
  --confirm-torso-compact `
  --confirm-waist-not-low `
  --confirm-pelvis-high-enough `
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
inseam proxy is inside 46.0–46.5%
inseam proxy is below the 47.0% hard guard
chin-to-crotch torso span is inside 2.7985–2.9420 heads
crown/chin/crotch/knee/soles were reviewed
upper_body_not_elongated == true
torso_compact == true
waist_not_low == true
pelvis_high_enough == true
lower_body_slightly_longer == true
knee_placement_natural == true
body_geometry_qa.raw_sha256 == current result_raw.png SHA-256
qa.json body_geometry_status == PASS
qa.json body_geometry_torso_specific_gate_pass == true
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

Then run the free preflight only. The expected preflight must show:

```text
paid_model_calls = 0
body_geometry_gate = HEAD_RATIO_PLUS_INSEAM_PROXY_PLUS_TORSO_SPECIFIC_GATE_REQUIRED_AFTER_RAW
body_geometry_inseam_proxy_target = 46.0–46.5%
body_geometry_torso_gate = COMPACT_TORSO_AND_SLIGHTLY_HIGH_PELVIS
composition_execution = DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS
```
