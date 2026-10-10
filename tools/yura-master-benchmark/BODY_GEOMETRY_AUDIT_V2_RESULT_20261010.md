# YURA Body Geometry Audit v2 — Result 2026-10-10

Status: **NON-AUTHORITY / DIAGNOSTIC RESULT / AUDIT V2**

This file records the formal re-measurement performed after Audit v2 was refined to use:
- structural-crown uncertainty;
- crotch/pelvis-boundary uncertainty;
- full 3 x 3 = 9-combination propagation for metrics that depend on both landmarks.

This result does not replace the current official `body_geometry_qa.py` gate.
It does not modify Body Authority, Face Authority, Composition Authority, or any current numeric target.
It does not authorize Composition, Master promotion, or Visual Authority promotion.

## Source state

Audit implementation commit:

```text
e100a3051f9f4ee8b64cb860d0cae3a7f169388a
Refine YURA Audit v2 pelvis-boundary uncertainty
```

Current official gates referenced by Audit v2:

```text
head target                  = 7.2
head acceptable range        = 7.1–7.3
inseam target                = 46.0–46.5%
inseam model-like hard fail  = >= 47.0%
chin→crotch envelope         = 2.7985–2.9420 heads
```

## Measurement definition

### Structural crown

For generated RAWs, the rendered visible hair crown is not used as the structural head-unit crown.

Audit v2 records:

```text
structural_crown_min_y
structural_crown_best_y
structural_crown_max_y
```

### Crotch / pelvis boundary

Audit v2 uses the structural upper/lower-body boundary at the central medial-thigh bifurcation.

Garment seams, shorts hems, garment crotch fabric, decorative clothing lines, and V-shaped garment edges have no landmark authority.

Audit v2 records:

```text
crotch_pelvis_boundary_min_y
crotch_pelvis_boundary_best_y
crotch_pelvis_boundary_max_y
```

### Uncertainty propagation

For metrics depending on both crown and boundary:

```text
3 structural-crown candidates
x
3 crotch/pelvis-boundary candidates
=
9 combinations
```

`best` uses best crown + best boundary.
Intervals use the minimum and maximum across all 9 combinations.

## Input measurements

### Active Body Guide

Author-approved exact landmarks:

```text
structural crown            160 / 160 / 160
chin                        340
crotch/pelvis boundary      856 / 856 / 856
knee                        1156
soles                       1456
```

This is an exact reference test of the author-approved landmark values, not a redefinition of the Guide.

### Test 3 RAW

RAW SHA-256:

```text
3c421884becf27565ea6ea6ec6e9042a452f7150b5a8dd7dd0a2e93ade120eb1
```

Displayed / reviewed copy:

```text
1152 x 2048
```

Audit v2 measurements:

```text
visible hair crown          35

structural crown
min                         59.84
best                        63.46
max                         67.30

chin                        338

crotch/pelvis boundary
min                         992
best                        998
max                         1005

knee                        1390
soles                       1996
```

Author visual review retained from the benchmark review:

```text
overall build not too thin              = PASS direction
chest/front volume matches author intent = FAIL
```

### Test 4 RAW

RAW SHA-256:

```text
81b8b1c7298d73ded96828060ed8cb9e28be00975c7d197074947f03a5eb71bb
```

Displayed / reviewed copy:

```text
1152 x 2048
```

Audit v2 measurements:

```text
visible hair crown          36

structural crown
min                         60.34
best                        64.00
max                         67.67

chin                        333

crotch/pelvis boundary
min                         954
best                        960
max                         966

knee                        1360
soles                       1976
```

Author visual review retained from the benchmark review:

```text
overall build not too thin              = FAIL
chest/front volume matches author intent = PASS
```

## Formal Audit v2 results

| Metric | Active Body Guide | Test 3 | Test 4 |
|---|---:|---:|---:|
| Head ratio best | 7.2000 | 7.0392 | 7.1078 |
| Head ratio interval | 7.2000 | 6.9606–7.1249 | 7.0258–7.1923 |
| Head status | EXACT_PASS | REVIEW_OVERLAP | REVIEW_OVERLAP |
| Inseam best | 46.2963% | 51.6419% | 53.1381% |
| Inseam interval | 46.2963% | 51.1838–52.0558% | 52.7233–53.5547% |
| Inseam status | EXACT_PASS | FAIL_ROBUST | FAIL_ROBUST |
| chin→boundary best | 2.8667 | 2.4040 | 2.3309 |
| chin→boundary interval | 2.8667 | 2.3512–2.4640 | 2.2776–2.3857 |
| Torso/boundary status | EXACT_PASS | FAIL_ROBUST | FAIL_ROBUST |
| boundary→knee share best | 50.0000% | 39.2786% | 39.3701% |
| boundary→knee share interval | 50.0000% | 38.8496–39.6414% | 39.0099–39.7260% |
| knee→soles share best | 50.0000% | 60.7214% | 60.6299% |
| knee→soles share interval | 50.0000% | 60.3586–61.1504% | 60.2740–60.9901% |

## Boundary position within structural figure height

Measured from structural crown to soles:

```text
Active Body Guide
best / exact = 53.7037%

Test 3
best          = 48.3581%
interval      = 47.9442–48.8162%

Test 4
best          = 46.8619%
interval      = 46.4453–47.2767%
```

Relative to the Active Body Guide, the generated crotch/pelvis boundary remains too high in the figure:

```text
Test 3 best difference ≈ -5.35 percentage points
Test 4 best difference ≈ -6.84 percentage points
```

At the Guide's 53.7037% boundary position, the corresponding approximate image-space Y would be:

```text
Test 3 ≈ y 1101
Test 4 ≈ y 1091
```

Those positions fall visibly within the thighs in the generated images, so the discrepancy cannot reasonably be explained by selecting a different garment line or by a small boundary-reading error.

## Interpretation

### 1. Previous "6.5-head convergence" diagnosis is not retained

Using structural crown rather than visible hair-shell crown changes the generated head-scale diagnosis substantially:

```text
Test 3 best = 7.039
Test 4 best = 7.108
```

Both retain uncertainty overlapping the current 7.1–7.3 band.

Therefore:

```text
"the image model is consistently forcing YURA to about 6.5 heads"
```

is not supported by Audit v2.

The earlier approximately-6.5 results contained a substantial measurement artifact caused by using the visible hair crown as the head-unit crown.

### 2. Pelvis / inseam failure is robust to measurement uncertainty

Even across all 9 crown/boundary combinations:

```text
Test 3 minimum inseam = 51.1838%
Test 4 minimum inseam = 52.7233%
```

Both remain above the current 47.0% hard-fail threshold.

Likewise:

```text
Test 3 maximum chin→boundary = 2.4640
Test 4 maximum chin→boundary = 2.3857
```

Both remain below the current minimum target of 2.7985 heads.

Therefore the vertical Body Geometry failure cannot be explained by plausible crown or crotch/pelvis-boundary uncertainty.

### 3. Test 4 is a mixed result relative to Test 3

Compared with Test 3:

```text
head scale:
Test 4 moved closer to the current accepted range.

crotch/pelvis boundary:
Test 4 moved farther upward relative to the Guide.

inseam:
Test 4 became longer relative to the Guide.
```

Thus Body-first image ordering did not produce a uniform improvement in Body Geometry.

### 4. Author visual-build and chest results remain independent axes

Audit v2 preserves the author-visible distinction:

```text
Test 3:
overall build = PASS direction
chest/front volume = FAIL

Test 4:
overall build = FAIL
chest/front volume = PASS
```

The vertical audit does not explain or overwrite these visual results.

## Diagnostic conclusion

```text
HEAD SCALE
Active Guide = PASS
Test 3      = REVIEW_OVERLAP
Test 4      = REVIEW_OVERLAP

VERTICAL BODY GEOMETRY
Active Guide = PASS
Test 3      = FAIL_ROBUST
Test 4      = FAIL_ROBUST

AUTHOR VISUAL BUILD / CHEST
Test 3      = build PASS direction / chest FAIL
Test 4      = build FAIL / chest PASS
```

The current problem is no longer best described as a simple "6.5-head problem."

The stronger remaining vertical diagnosis is:

```text
generated crotch/pelvis boundary is too high relative to the Active Body Guide,
producing an excessively long lower-body / inseam proportion.
```

This result supports promoting selected Audit v2 measurement definitions for official-QA consideration, but does not itself promote them.

## Promotion / composition state

```text
official QA replacement       = NO
Body Authority change         = NO
Face Authority change         = NO
Composition execution         = BLOCKED
Master promotion              = NO
Visual Authority promotion    = NO
Test 5 authorization          = NO
```
