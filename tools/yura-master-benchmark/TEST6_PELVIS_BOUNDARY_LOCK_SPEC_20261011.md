# YURA Test 6 — Pelvis/Boundary normalized-position lock

Status: **PREREGISTERED / NOT YET EXECUTED**

## Purpose

Test exactly one remaining Body Geometry hypothesis after the completed 10-run variance study.

The 10-run study showed:

```text
visual quality can reach all-PASS
7.2-head best values can occur
but crotch/pelvis boundary placement remains systematically too high
```

The repeated boundary miss is the active problem.

## Single hypothesis

**H6**

> If the author-selected Sample 9 working Master is treated as the visual/edit baseline and the crotch/pelvis boundary is expressed as one explicit normalized structural anchor at the Body Guide position, the model can move that boundary downward toward the approved Guide geometry without redesigning the already-approved visual traits.

This test is about **boundary placement only**.

It is not a test of hair length, chest design, thigh design, Face Identity, knee design, Composition, or a new head-count target.

## Baseline

Working Master:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

SHA-256 of the committed original local Sample 9 RAW:

```text
81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

Binary commit:

```text
c20ffc31fe5ccd16323ce36b129af93014d269ee
```

Sample 9 recorded study values:

```text
Head best              ≈ 7.214
Boundary best          ≈ 49.17%
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

Guide target:

```text
structural crown = 0%
soles            = 100%

crotch/pelvis boundary
= (856 - 160) / (1456 - 160)
= 696 / 1296
= 53.7037037% downward from structural crown

equivalent crotch→soles fraction
= 46.2962963%

Guide chin→boundary
= 2.8667 heads
```

The next implementation must use these values as **relative body geometry**, never as output-canvas absolute pixel coordinates.

## Exact boundary definition

The boundary means:

```text
CENTRAL MEDIAL-THIGH BIFURCATION
=
UPPER / LOWER BODY STRUCTURAL BOUNDARY
```

It does **not** mean:

```text
waistline
shorts waistband
garment hem
visible clothing seam
navel
hip widest point
```

Garment lines have no landmark authority.

## Test 6 intervention

Only the pelvis/boundary enforcement method may change.

The implementation must make the following normalized relationship explicit and primary:

```text
CROTCH/PELVIS BOUNDARY MUST BE AT 53.7037% OF CROWN-TO-SOLES BODY HEIGHT,
MEASURED DOWNWARD FROM THE STRUCTURAL CROWN.

EQUIVALENT:
CROTCH-TO-SOLES MUST BE 46.2963% OF CROWN-TO-SOLES BODY HEIGHT.
```

The intervention must also state that the boundary is not an aesthetic suggestion and not a qualitative “high pelvis” direction. It is a measurable structural anchor inherited from the approved Body Guide.

## Frozen non-target variables

Test 6 must preserve, rather than redesign:

```text
Sample 9 Face Identity
Sample 9 overall build
Sample 9 chest appearance
Sample 9 thigh feminine volume/curve
Sample 9 knee position as judged by the author
Sample 9 overall leg visual balance
Sample 9 skin appearance
Sample 9 general hair identity
front-view full-body presentation
white background
7.2-head target and current 7.1–7.3 gate
current Body Guide
current official Body QA definitions
current Composition deferral
```

Do not alter these to make the boundary easier to satisfy.

## Hair-length isolation rule

The author has approved a later micro-refinement:

```text
hair slightly longer than Sample 9
```

That change is **not part of Test 6**.

For Test 6:

```text
preserve Sample 9 hair length as closely as practical
do not intentionally lengthen or shorten hair
```

Reason: combining hair editing with the boundary intervention would break the one-hypothesis discipline.

Hair-length refinement occurs only after the Body Geometry decision.

## Geometry behavior required

Move the structural boundary toward the Guide position by redistributing the torso/pelvis transition, not by arbitrary leg stretching.

Do not solve the target by:

```text
changing head size
lengthening only thighs
lengthening only shins
moving the soles
moving the knee merely to manipulate the ratio
raising the waistline as a fake boundary
using shorts/garment edges as the landmark
nonuniform body scaling
Composition warp
```

Crown, chin, knee, and soles are measurement controls. They may show ordinary generation variance, but the prompt must not intentionally direct them as the solution.

## Measurement after one paid RAW

Record the full structural-uncertainty set:

```text
structural_crown_min
structural_crown_best
structural_crown_max
chin
crotch_pelvis_boundary_min
crotch_pelvis_boundary_best
crotch_pelvis_boundary_max
knee
soles
```

Then run the current official 3×3 crown×boundary uncertainty evaluation.

Report at minimum:

```text
head interval / best
normalized boundary interval / best
inseam interval / best
chin→boundary interval / best
overall_build_not_too_thin
chest_front_volume_matches_author_intent
author knee-position judgment
author leg-balance judgment
author thigh-curve judgment
```

## Decision rules

### EXACT SUPPORT

H6 is exactly supported only if:

```text
full uncertainty inseam interval is inside 46.0–46.5%
AND
full uncertainty chin→boundary interval is inside 2.7985–2.942 heads
AND
the boundary corresponds to the approved Guide-relative location
AND
non-target author visual judgments do not materially regress
```

Head is evaluated by the unchanged official gate. Final Body PASS still requires the full existing official QA contract.

### DIRECTIONAL SUPPORT

Use this label if:

```text
boundary moves materially toward 53.7037%
and both inseam and chin→boundary move toward their gates
but one or more required intervals remain outside PASS
```

A directional improvement is evidence, not a PASS.

### NO SUPPORT

Use this label if the boundary remains near the prior failure region and the derived metrics do not materially improve.

### OVERSHOOT

Use this label if the boundary is pushed beyond the approved Guide region and the inseam becomes too short relative to the current gate.

### REGRESSION

Use this label if the boundary improves but the intervention materially damages the author-selected Master visual baseline or causes a non-target structural failure.

## Paid-run discipline

```text
one paid RAW
= H6 only
= one complete measurement
= one decision
```

Do not reroll until a favorable image appears.

Do not run multiple paid samples before judging the first Test 6 RAW.

Do not change the prompt after seeing the image and then count the changed rerun as the same test.

## Composition

Composition remains blocked.

Test 6 output is a QA-pending geometry-refinement candidate only.

No deterministic Composition step may run unless the current official Body Geometry gate permits it.

## What happens after Test 6

If H6 is EXACT SUPPORT and the official Body QA passes, the next separate task is the approved **slight hair-length micro-refinement** while preserving the corrected body.

If H6 is only DIRECTIONAL SUPPORT, the next hypothesis may strengthen the same normalized-boundary mechanism, but must be preregistered as a new test.

If H6 has NO SUPPORT, do not change unrelated appearance layers. Diagnose why the image edit is not honoring the structural boundary anchor.
