# YURA Body Geometry Audit v2

Status: **NON-AUTHORITY / DIAGNOSTIC ONLY / PARALLEL TO CURRENT QA**

This document does not replace `BODY_GEOMETRY_GUIDE.md`.
This document does not modify any current Body Authority value.
This document does not authorize Composition or Master promotion.

## Purpose

Audit v2 exists to test whether current Body Geometry QA is conflating rendered hair-shell size with structural head scale, and to retain author-visible body-build differences that the current vertical-only QA cannot represent.

It is designed to:

- separate visible hair silhouette from structural head scale;
- propagate crown uncertainty instead of forcing a false exact landmark;
- separate global body build from local chest/front-volume evaluation;
- keep horizontal measurements diagnostic until author-approved thresholds exist;
- compare current QA and Audit v2 before any gate replacement.

The current official QA remains `body_geometry_qa.py` until explicit author approval promotes a replacement.

---

## 1. Coordinate convention

Image coordinates use:

```text
origin = upper-left
x increases rightward
y increases downward
```

All landmark values are image-space measurements in pixels.

Hidden landmarks must not be represented as exact ground truth.

---

## 2. Head landmark separation

### `visible_hair_crown_y`

The highest persistent visible point of the main hair shell.

Use it for:

- rendered apparent-head-silhouette analysis;
- Face Reference indirect-pull diagnostics;
- measuring visible hair-shell inflation.

Do not use it for:

- structural head-unit calculation;
- 7.2-head pass/fail calculation;
- torso or inseam normalization.

Single stray hairs or isolated anti-aliased pixels are not the main hair shell.

### `structural_crown_proxy_y`

A diagnostic proxy for the top of the underlying structural head, excluding visible hair-shell inflation.

Because this point can be hidden by hair, Audit v2 records an uncertainty interval:

```text
structural_crown_min_y
structural_crown_best_y
structural_crown_max_y
```

With Y increasing downward:

```text
min_y  = upper bound of plausible structural crown position
best_y = central reviewed estimate
max_y  = lower bound of plausible structural crown position
```

Required ordering:

```text
structural_crown_min_y <= structural_crown_best_y <= structural_crown_max_y
```

The interval is diagnostic uncertainty, not permission to move or redesign the Face Reference.

---

## 3. Structural head calculations

For each structural-crown candidate independently:

```text
head_height_px
= chin_y - structural_crown_y

figure_height_px
= soles_y - structural_crown_y

total_head_ratio
= figure_height_px / head_height_px
```

Do not estimate a structural result by multiplying an old visible-crown head ratio by a correction factor.

Changing crown position changes both the head-height denominator and the full-figure numerator, so all metrics must be recomputed from landmarks.

### Head-ratio interval status

The current official acceptable range remains **7.1–7.3 heads**.

Audit v2 diagnostic states:

```text
EXACT_PASS
  min_y = best_y = max_y and the resulting value is inside 7.1–7.3

PASS_ROBUST
  the full uncertainty interval is inside 7.1–7.3

REVIEW_OVERLAP
  the uncertainty interval intersects 7.1–7.3 but is not fully contained

FAIL_ROBUST
  the uncertainty interval does not intersect 7.1–7.3
```

These labels do not replace the current official QA gate.

---

## 4. Face Reference indirect head-shell diagnostic

Face Reference remains **FACE IDENTITY AUTHORITY ONLY**.

Audit v2 may nevertheless compare visible and structural head-shell spans:

```text
visible_head_height
= chin_y - visible_hair_crown_y

structural_head_height
= chin_y - structural_crown_proxy_y

hair_shell_inflation_ratio
= visible_head_height / structural_head_height
```

This ratio is diagnostic evidence of apparent-head-shell inflation.

It must not be interpreted as:

- Body Authority;
- proof that Face Reference directly controls full-body proportion;
- permission to resize, replace, or redesign the Face Reference;
- a universal anatomical head ratio.

`head-shell` mode never executes a 7.2 full-body pass/fail calculation.

---

## 5. Pelvis / leg-root landmark

Primary Audit v2 body landmark:

```text
pelvis_leg_root_proxy_y
```

Definition:

> the approximate vertical level at which the left and right upper legs structurally separate from the pelvis.

Do not derive this point solely from:

- underwear seam;
- shorts hem;
- garment crotch fabric;
- decorative clothing line.

If the structural leg-root cannot be visually resolved, record it as not measurable during manual review rather than inventing a landmark.

The current author-approved Body Guide value `crotch / pelvis-line proxy = y 856` is not changed by this diagnostic terminology. For the Active Body Guide exact reference test, `pelvis_leg_root_proxy_y = 856`.

---

## 6. Body vertical calculations

For each structural-crown candidate:

```text
inseam_proxy_ratio
= (soles_y - pelvis_leg_root_proxy_y)
  / (soles_y - structural_crown_y)

chin_to_pelvis_heads
= (pelvis_leg_root_proxy_y - chin_y)
  / (chin_y - structural_crown_y)

pelvis_to_knee_heads
= (knee_y - pelvis_leg_root_proxy_y)
  / (chin_y - structural_crown_y)

knee_to_soles_heads
= (soles_y - knee_y)
  / (chin_y - structural_crown_y)
```

Audit v2 reports the full metric interval induced by structural-crown uncertainty.

Current official Body Guide gates are read from existing `config.json`; Audit v2 does not invent replacements.

Current values at creation time are:

```text
head target                  7.2
head acceptable range        7.1–7.3
inseam target                46.0–46.5%
inseam model-like hard fail  >= 47.0%
chin→pelvis current envelope 2.7985–2.9420 heads
```

---

## 7. Diagnostic horizontal geometry

Optional manually reviewed measurements:

```text
shoulder_width_px
ribcage_width_px
chest_outer_width_px
waist_width_px
pelvis_hip_width_px
upper_thigh_left_width_px
upper_thigh_right_width_px
calf_left_width_px
calf_right_width_px
ankle_left_width_px
ankle_right_width_px
```

Measurements must exclude hair and obvious garment flare where possible.

If a body contour is hidden or contaminated enough that it cannot be distinguished reliably, leave the measurement absent. Missing values are `NOT_MEASURED`; they are never converted to zero.

Widths are normalized to best-estimate structural figure height:

```text
normalized_width = width_px / structural_figure_height_best_px
```

When the required inputs exist, Audit v2 also reports:

```text
shoulder / hip
ribcage / hip
waist / hip
average upper thigh / hip
average calf / hip
chest / ribcage
chest / waist
```

These ratios are **DIAGNOSTIC ONLY**.

No numeric PASS threshold is frozen by Audit v2.

Clothing contamination, hair overlap, perspective, and stylized rendering must remain part of human review.

Do not promote a diagnostic width ratio into a Hard Gate without explicit author approval.

---

## 8. Author visual gates

Audit v2 records two independent author-review dimensions required to distinguish Test 3 and Test 4 failure modes.

### `overall_build_not_too_thin`

Checks the whole-body mass / silhouette.

This is not equivalent to:

- shoulder width only;
- hip width only;
- BMI-like interpretation;
- generic human anatomy.

### `chest_front_volume_matches_author_intent`

Checks chest/front-volume appearance relative to the whole YURA build.

This is not equivalent to:

- chest width alone;
- a single absolute size value;
- generic anatomical targets.

This validation is for character Master Body Geometry and silhouette review, not sexual emphasis.

Allowed review states:

```text
PASS
FAIL
NOT_REVIEWED
NOT_MEASURABLE
```

Audit v2 keeps these two states separate. A body-build failure must not overwrite a chest result, and a chest failure must not overwrite a body-build result.

---

## 9. Modes

### `head-shell`

Required:

- image path;
- visible hair crown;
- structural crown min / best / max;
- chin.

Produces head-shell diagnostic metrics only.

Does not calculate a 7.2 full-body gate.

### `body`

Required:

- image path;
- structural crown min / best / max;
- chin;
- pelvis / leg-root proxy;
- knee;
- soles.

`visible_hair_crown_y` is optional and adds apparent-head-shell diagnostics when supplied.

Optional horizontal geometry and author visual review may also be recorded.

---

## 10. Fail-closed validation

Audit v2 rejects invalid landmark order.

Required structural ordering:

```text
0 <= structural_crown_min_y
structural_crown_min_y <= structural_crown_best_y <= structural_crown_max_y
structural_crown_max_y < chin_y
```

For body mode:

```text
chin_y < pelvis_leg_root_proxy_y < knee_y < soles_y <= image_height
```

If `visible_hair_crown_y` is supplied:

```text
0 <= visible_hair_crown_y < chin_y
```

Width measurements must be positive if supplied.

---

## 11. Active Body Guide reference test

The current Active Body Guide exact landmarks remain:

```text
structural crown = 160
chin             = 340
pelvis proxy     = 856
knee             = 1156
soles            = 1456
```

Expected Audit v2 outputs:

```text
total head ratio = 7.2
inseam proxy     = 46.2963%
chin→pelvis      = 2.8667 heads
```

Failure to reproduce these values means the Audit v2 calculation implementation is invalid.

This exact test does not modify the Body Guide.

---

## 12. Parallel-operation rule

Until explicitly promoted by author approval:

```text
body_geometry_qa.py
= CURRENT OFFICIAL QA

body_geometry_qa_v2.py
= PARALLEL DIAGNOSTIC QA
```

An Audit v2 result cannot by itself authorize:

- Composition execution;
- Master promotion;
- Visual Authority promotion;
- Body Authority changes;
- Face Authority changes.

All Audit v2 reports must therefore retain:

```text
composition_execution_allowed = false
master_promotion = NO
authority_status = DIAGNOSTIC_ONLY
```

---

## 13. Validation sequence before any promotion

Run without paid generation:

```text
1. Python syntax check
2. Active Body Guide exact reference test
3. Face Reference head-shell test
4. Test 3 body audit
5. Test 4 body audit
6. Record author visual gates
7. Compare current QA and Audit v2
8. Review results with the author
```

Only after that comparison may a separate author-approved change promote any Audit v2 definition into official QA.

Test 5 is outside this specification and must not be started merely because Audit v2 runs successfully.
