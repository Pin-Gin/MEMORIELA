# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / BODY-GEOMETRY-FIRST / CALIBRATION-IN-PROGRESS / COMPOSITION-DEFERRED**

This file is operational documentation only. It is **NOT** a YURA visual Authority.

The reusable cross-character method is documented in:

`visuals/MASTER_CREATION_WORKFLOW.md`

---

## Project objective

The primary objective is:

> **Create a high-quality YURA visual Master while reducing generation drift and stochastic variance to the smallest practical level.**

The Master must be both visually strong and operationally stable. A beautiful one-off image is not sufficient if the same identity/geometry cannot be reproduced or audited; a stable but mediocre image is also not sufficient.

Additional objectives:

- convert author intent into measurable constraints where measurement improves repeatability;
- isolate Face Identity, Body Geometry, appearance, Composition, and rendering responsibilities;
- prevent rejected generations from contaminating future Identity/Geometry references;
- keep author-specific intent above generic anime/model defaults;
- make Authority inputs, hashes, prompt compilation, QA, and promotion auditable;
- minimize paid trial-and-error by using local checks and free preflight before paid calls;
- change one major variable at a time so improvement/regression has an identifiable cause;
- use deterministic post-processing for Composition instead of deforming anatomy;
- establish a reusable process for SHIORI, MIO, and later characters without copying YURA-specific values.

---

## Current checkpoint — 2026-10-04

### Completed

The benchmark architecture is functioning end-to-end through RAW generation:

```text
current Git main
  -> local runner verifies HEAD == origin/main
  -> configured Authority files only
  -> sealed Authority bundle + SHA-256
  -> Codex compiles RAW Body-Geometry-first Image API prompt
  -> runner enforces required prompt invariants
  -> runner rejects final-Composition numeric leakage
  -> Image API generates result_raw.png only
  -> Body Geometry QA is required before Composition
```

The following safeguards are already implemented:

- novel/story sources are denied for YURA appearance generation;
- failed generated YURA images are not valid visual references;
- Face Identity and Body Geometry are separate Authorities;
- Body Geometry is resolved before final Composition;
- final Composition is deterministic whole-raster scale/translation only;
- Body Geometry QA binds to the exact RAW SHA-256;
- Master promotion remains blocked until measurable QA and explicit author PASS;
- local preflight performs no paid model call.

### Active Body Geometry Authority replacement completed

The old Body Geometry guide was replaced with an author-approved long-leg 7.2-head guide and activated.

Active guide geometry currently records:

```text
canvas = 1200 × 1600
crown = y 160
chin = y 340
one head = 180 px
crotch / pelvis boundary = y 856
knee proxy = y 1156
soles = y 1456
total = 7.2 heads
```

The guide now explicitly labels:

```text
CROTCH / PELVIS LINE
= UPPER / LOWER BODY BOUNDARY
```

This was added because the previous geometry image did not communicate the upper/lower-body boundary strongly enough to the image model.

Current active YURA-specific image-space values encoded by the guide/text are:

```text
crown→crotch = 3.8667 heads
chin→crotch = 2.8667 heads
inseam proxy = 46.2963%
knee split proxy = approximately 1:1 within crotch→soles
```

The replacement Authority was activated in Git at commit:

```text
6a8284cadaa53d21c10b02b55415ac9e92fe3d77
Activate replaced YURA Body Geometry guide
```

### Free preflight after Authority replacement completed

The replacement Authority passed free preflight with:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
git_commit = 6a8284cadaa53d21c10b02b55415ac9e92fe3d77
authority_count = 7
sealed_authority_bundle_sha256 = b4e2c6ed9281a622e5938d8acb906dcb2a41f610cd4e6b5649e3f4977e646e59
codex_input_sha256 = a812b4d62f58cc104d9f40118fb57f06d76de41baf9dcfb3cc02dec308f09f74
body_geometry_gate = HEAD_RATIO_PLUS_INSEAM_PROXY_PLUS_TORSO_SPECIFIC_GATE_REQUIRED_AFTER_RAW
body_geometry_inseam_proxy_target = 46.0–46.5%
body_geometry_torso_gate = COMPACT_TORSO_AND_SLIGHTLY_HIGH_PELVIS
composition_execution = DEFERRED_UNTIL_BODY_GEOMETRY_QA_PASS
```

### First RAW after the new guide

One paid RAW was generated after activating the new guide.

Author visual review found this RAW **substantially closer to the desired full-body balance on the first attempt** than earlier iterations:

- torso no longer has the same obvious elongated look;
- pelvis/crotch placement reads higher;
- legs read longer and the overall body balance is much closer to the intended direction;
- the new explicit geometry guide appears to have materially improved generation behavior.

However, this RAW is **not yet a PASS, Master, or future visual reference**.

Its exact Body Geometry landmarks have not yet been formally measured. Preliminary visual inspection suggests that the successful-looking balance may not match the currently frozen 46.0–46.5% inseam target and 7.1–7.3-head gate. That is important evidence that the current numeric target may require recalibration around the author's actual preferred visual result.

The correct response is **not** to force the visually promising RAW to satisfy an old number. The next step is to measure it and compare measurement against author judgment.

### Face issue observed but intentionally deferred

The current Face Identity reference appears to produce ears that read somewhat too long vertically. The same tendency is visible in the full-body RAW.

This is recorded as a later Face Identity refinement item, but it is intentionally **deferred until full-body geometry is stable**.

Reason:

```text
change Body Geometry and Face Identity simultaneously
  -> causality becomes ambiguous

stabilize Body Geometry first
  -> then refine ear geometry locally
  -> then verify Face Identity again
```

This preserves controlled iteration.

---

## Current active numeric gates

Until explicitly changed by author-approved recalibration, the runtime gate remains:

```text
head ratio target = 7.2
acceptable head ratio = 7.1–7.3

inseam_proxy_ratio = (soles_y - crotch_y) / (soles_y - crown_y)
PASS target = 46.0–46.5%
>=47.0% = model-like hard FAIL

chin_to_crotch_heads = 2.7985–2.9420
```

The torso envelope is mathematically implied by the approved head/inseam ranges and is retained as an explicit audit value. It is not an independent anatomical truth.

These values are **current calibration values, not sacred constants**. If precise measurement of author-preferred RAWs shows that a different range better reproduces the intended YURA body, the range should be deliberately recalibrated and then frozen again through Authority + QA + prompt invariants.

---

## Immediate next step

Do **not** run Composition yet.

Do **not** generate another paid RAW yet.

Measure the current promising `result_raw.png` first.

Required vertical landmarks:

```text
crown
chin
crotch / pelvis boundary
knee
soles
```

Then compute:

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
knee split within crotch→soles
```

The purpose of this measurement is not merely pass/fail. It is to answer:

> **What numeric geometry did the first visually promising RAW actually have?**

That measured geometry can then be compared directly with author visual judgment.

---

## Decision after measuring the current RAW

### Case A — visual judgment and current numeric gates agree

If the promising RAW is close to the existing targets and only contains ordinary sampling error:

```text
keep current numeric ranges
-> diagnose remaining mismatch
-> make only the necessary small Authority/prompt adjustment
-> free preflight
-> one new paid RAW
```

### Case B — visual judgment is good but current numeric gates disagree

If the author strongly prefers the current RAW while the measured values significantly miss the existing targets:

```text
treat current RAW as a calibration sample only
-> derive a proposed YURA-specific target range from measured evidence
-> author explicitly approves the new target
-> update Body Geometry Authority image/text if needed
-> update benchmark config
-> update body_geometry_qa.py
-> update Codex instruction / prompt invariants
-> update runner validation
-> update Composition gate validation
-> free preflight
-> one new paid RAW
-> test whether the preferred geometry reproduces
```

This is the expected path if the current RAW confirms that the earlier 46.0–46.5% range was too conservative for the desired YURA appearance.

A promising RAW used this way remains a **measurement/calibration sample**. It does not automatically become a Face Identity or Body Geometry visual reference.

---

## Stabilization target before Face refinement

Full-body geometry should be considered stable only when controlled generations repeatedly land near the author-approved balance without relying on luck.

The goal is not merely one successful image. The goal is:

```text
same Authority
same benchmark architecture
same measurable target
-> low-variance, consistently acceptable YURA full-body geometry
```

Once full-body geometry is stable:

```text
1. refine Face Identity local issues such as ear vertical size/placement;
2. regenerate/verify face-level Identity as needed;
3. confirm the Face change does not destabilize full-body identity;
4. perform final deterministic Composition;
5. run final QA;
6. explicit author PASS;
7. promote the final Master;
8. create Master-derived production description per lifecycle.
```

---

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
       current target = 7.2; acceptable = 7.1–7.3
       inseam proxy = (soles - crotch) / (soles - crown)
       current YURA target = 46.0–46.5%
       >=47.0% = current model-like hard FAIL
       chin-to-crotch torso span current envelope = 2.7985–2.9420 heads
       author review confirms internal torso/pelvis/knee quality
       RAW SHA-256 is bound into body_geometry_qa.json
     -> FAIL: stop; Composition blocked
     -> PASS: explicit Body Geometry confirmation still required
  -> normalize_composition.py verifies all Body Geometry gates + RAW SHA match
  -> uniform whole-raster scale + x/y translation only
  -> result.png at final Composition target
  -> final QA / author confirmation
  -> Master promotion remains NO until explicit final PASS
```

---

## Why the process is working better now

Earlier iterations exposed several distinct failure modes that were being conflated:

- total head ratio alone did not control torso distribution;
- text-only geometry statements were not enough for the image model;
- the old guide did not make the upper/lower-body boundary explicit enough;
- asking generation to satisfy final Composition risked anatomy being changed for canvas fit;
- changing many concerns at once made diagnosis weak.

The current process addresses those separately:

```text
explicit geometry guide
+ explicit internal boundary
+ measurable landmarks
+ character-specific numeric gates
+ author visual judgment
+ sealed prompt compilation
+ preflight before payment
+ one controlled paid experiment
+ deterministic Composition after anatomy PASS
```

The first RAW after the revised guide being visually much closer is evidence that this decomposition is useful. Reproducibility must still be demonstrated before the geometry is considered solved.

---

## Reuse for SHIORI, MIO, and later characters

The same **method** should be reused for later character Masters.

Do not copy YURA's geometry numbers into other characters.

For each character:

```text
character-specific Face Identity Authority
+ character-specific Body Geometry guide
+ explicit internal landmarks/boundaries
+ initial author-approved numeric ranges where useful
+ sealed preflight
+ one controlled RAW
+ exact measurement
+ author judgment
+ recalibration if evidence supports it
+ repeated stability test
+ Face/detail refinement after body stability
+ deterministic Composition
+ explicit author PASS
+ Master promotion
```

This allows SHIORI, MIO, and later characters to benefit from the process learned during YURA development without inheriting YURA-specific proportions or accidental visual traits.

---

## Composition remains deferred

The RAW Image API prompt must not contain final Composition numeric targets such as final occupancy/margins. Those remain post-generation concerns.

Allowed final Composition transforms only:

- uniform whole-raster scaling;
- x/y translation;
- white-background crop/pad implied by final canvas placement.

Never:

- nonuniform scaling;
- body-part scaling;
- warp;
- content-aware body deformation;
- inpainting/body reshaping;
- face regeneration during Composition.

Master promotion remains **NO** until Body Geometry, Face Identity, Composition, final QA, and explicit author approval all pass.
