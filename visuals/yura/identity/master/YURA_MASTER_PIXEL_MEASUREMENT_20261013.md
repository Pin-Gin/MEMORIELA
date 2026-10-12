# YURA FORMAL MASTER — CANONICAL PIXEL MEASUREMENT 2026-10-13

Status: **MEASUREMENT PASS V1 COMPLETE / PROPOSED PRODUCTION BANDS / AUTHOR REVIEW REQUIRED BEFORE GATE ACTIVATION**

This document records image-space measurements from the exact formally promoted YURA full-body Master. It is a technical character-geometry / silhouette measurement artifact. It is not intended to amplify sexual appeal, fetishize anatomy, or invent unsupported anatomy.

## 1. Exact source verification

Canonical repository asset:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Runtime input was supplied as `YURA_VISUAL_MASTER.zip` and extracted without recompression.

Verified extracted PNG:

```text
filename = YURA_VISUAL_MASTER.png
canvas = 1440 x 2560 px
format = PNG / RGBA
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

This exactly matches the canonical formal-Master SHA recorded in Git.

No screenshot, chat-resized copy, Test 6 output, old Master, or reconstructed image was used for the measurements below.

## 2. Measurement coordinate system

For directly visible Production measurements, use the visible-figure normalization:

```text
visible hair crown best = y 59 px
visible sole/figure-bottom best = y 2471 px
VISIBLE_FIGURE_HEIGHT H = 2471 - 59 = 2412 px
```

Vertical normalized position:

```text
Y% = (landmark_y - 59) / 2412 * 100
```

Horizontal normalized width:

```text
W% = measured_width_px / 2412 * 100
```

This visible normalization is intentionally distinct from the old Master-generation structural-crown Body Guide system.

The hidden structural skull crown is not directly observable in the formal Master because it is covered by hair. Therefore no new Production hard gate may pretend that a single exact structural-crown pixel was directly measured here.

Historic head-count measurements remain audit history. Production coarse head/face gates in this phase use directly visible features instead.

## 3. Direct visible landmark measurements

Values with ranges represent selection/occlusion uncertainty, not generation tolerance.

| Feature | Pixel min | Pixel best | Pixel max | Best normalized |
|---|---:|---:|---:|---:|
| visible hair crown Y | 58 | 59 | 60 | 0.00% H origin |
| chin Y | 434 | 435 | 436 | 15.589% |
| shoulder line Y | 525 | 530 | 535 | 19.527% |
| current layered hair endpoint Y | 950 | 965 | 980 | 37.562% |
| visible waist-region reference Y | 1005 | 1020 | 1035 | 39.842% |
| central medial-thigh bifurcation / Production lower-body boundary Y | 1245 | 1252 | 1260 | 49.461% |
| fingertip Y, neutral standing pose | 1380 | 1390 | 1400 | 55.182% |
| knee center / narrow-joint zone Y | 1685 | 1700 | 1720 | 68.035% |
| calf maximum-width region Y | 1845 | 1855 | 1865 | 74.461% |
| ankle reference Y | 2235 | 2250 | 2265 | 90.837% |
| forefoot reference Y | — | 2420 | — | 97.886% |
| sole / visible figure bottom Y | 2469 approx | 2471 | 2473 faint AA | 100.000% |

### Boundary definition

The Production boundary measurement above means:

```text
central medial-thigh bifurcation / upper-lower visible structural transition
```

It does not use shorts waistband, garment hem, navel, or clothing seam as the landmark.

Formal-Master best value using the direct visible normalization is approximately **49.46% H**.

This is intentionally recorded separately from the historic Body Guide target 53.7037%. The historic mismatch is not rewritten as PASS; the formal Master is simply the new source for the later Production reproduction gate.

## 4. Coarse face measurement

The full-body Master supports only coarse face geometry. Fine face-local geometry remains delegated to the later Face Reference phase.

Measured visible cheek/face envelope near y≈340:

```text
face visible width uncertainty = 264–270 px
best = 267 px
best = 11.070% H
```

Direct chin location:

```text
best y = 435 px
best Y% = 15.589% H
```

Do not infer hidden skull depth or hidden crown from this full-body image for a new hard gate.

## 5. Hair — measured baseline

Measured whole-hair visible facts:

```text
visible crown best y = 59 px
maximum outer hair silhouette width ≈ 632 px
outer-width measurement uncertainty ≈ 620–645 px
best outer width = 26.202% H
current layered lower endpoint best ≈ y 965 px
current endpoint uncertainty ≈ y 950–980 px
current endpoint best = 37.562% H
```

The formal Master is known to be slightly shorter-haired than final author intent.

### AUTHOR_OVERRIDE — final SUPER-LONG endpoint

The final Production requirement is not the measured y≈965 endpoint.

Proposed normalized target derived from the visible Master waist region + explicit author correction:

```text
required hair category = SUPER-LONG
must clearly reach the waist area
proposed endpoint band = 39.0–41.0% H
approx canonical-pixel equivalent = y 1000–1048 px on this exact Master scale
merely mid-back / ordinary-long appearance = FAIL
substantially below the waist = FAIL
```

This remains **PROPOSED** until author review freezes the numeric band.

Hair-style local structure / temple locks / ear-cover locks / face-up references are deferred until the full-body part specification checkpoint, per the fixed project order.

## 6. Hair color sampling

Technical pixel sampling from multiple hair regions, excluding near-white background and obvious skin:

```text
sample median sRGB ≈ (239, 236, 239)
sample mean sRGB   ≈ (236.3, 232.8, 235.9)
median CIELAB      ≈ L* 93.70, a* +1.53, b* -1.09
```

This supports the established silver-white / very light neutral-cool appearance.

Color should be a SOFT gate because line shading and illumination alter exact pixels.

## 7. Skin color sampling

Multiple face/neck/arm/thigh/calf interior regions were sampled while excluding line art and background.

Aggregate sample:

```text
median sRGB ≈ (253, 244, 242)
mean sRGB   ≈ (252.1, 242.8, 240.3)
median CIELAB ≈ L* 96.82, a* +2.66, b* +2.04
```

Robust sampled CIELAB 10–90 percentile envelope:

```text
L* ≈ 94.84–97.61
a* ≈ +1.81–+3.70
b* ≈ +1.56–+3.15
```

This is a pale, slightly warm anime-skin baseline. It is not a photographic skin-calibration standard.

Proposed SOFT reproduction band:

```text
L* = 94.5–98.5
a* = +1.0–+5.0
b* = +0.5–+4.5
```

Author review is required before activating this band.

## 8. Shoulder / torso frontal silhouette measurements

Because the image is front-view only, these are 2D frontal-envelope measurements. No unseen 3D depth is inferred.

### Shoulder

```text
shoulder outer-span uncertainty ≈ 390–410 px
best ≈ 400 px
best = 16.584% H
shoulder-line best Y = 530 px = 19.527% H
```

### Upper-torso frontal envelope

Reference row around y≈740:

```text
width uncertainty ≈ 310–325 px
best ≈ 317 px
best = 13.143% H
```

This metric is the neutral front silhouette of the upper torso. It is not a 3D depth/volume estimate.

### Mid-torso narrow envelope

Reference row around y≈800:

```text
width uncertainty ≈ 295–305 px
best ≈ 299 px
best = 12.396% H
```

### Lower-torso envelope

Reference row around y≈950:

```text
width uncertainty ≈ 330–345 px
best ≈ 338 px
best = 14.013% H
```

The Sample 9 torso is therefore not a uniform vertical column: it narrows through the mid-torso and opens again toward the lower torso / pelvis transition.

## 9. Pelvis / upper-thigh transition

At y≈1300, just below the garment-obscured upper transition, the visible bilateral outer span is approximately:

```text
outer pair width uncertainty ≈ 400–416 px
best ≈ 408 px
best = 16.915% H
```

Cross-part relation:

```text
lower outer pair / shoulder span ≈ 408 / 400 = 1.020
```

This ratio is useful as a stable whole-body shape descriptor and avoids using generic anatomy.

## 10. Thigh contour profile

Per-side left/right widths are almost symmetric at the selected rows.

| Y px | Y% H | Per-side width best | Width % H | Width / root |
|---:|---:|---:|---:|---:|
| 1300 | 51.451% | ≈196.5 px | 8.147% | 1.000 |
| 1400 | 55.597% | ≈167.5 px | 6.944% | 0.852 |
| 1500 | 59.743% | ≈139 px | 5.763% | 0.707 |
| 1600 | 63.889% | ≈119.5 px | 4.954% | 0.608 |
| 1700 | 68.035% | ≈115 px | 4.768% | 0.585 |

This progressive curve is a stronger descriptor than a single thigh width. The contour should taper continuously toward the knee rather than becoming a straight, uniformly thin column.

## 11. Knee

```text
center/narrow-joint best Y ≈ 1700 px = 68.035% H
selection uncertainty ≈ y 1685–1720
per-side width ≈ 115 px
width uncertainty ≈ 112–118 px
best width = 4.768% H
```

Sample 9 knee placement is an explicit author-PASS trait.

## 12. Lower-leg profile

| Y px | Y% H | Per-side width best | Width % H | Relative to knee |
|---:|---:|---:|---:|---:|
| 1700 | 68.035% | 115 px | 4.768% | 1.000 |
| 1800 | 72.181% | 121.5 px | 5.037% | 1.057 |
| 1855 | 74.461% | 131 px | 5.431% | 1.139 |
| 1900 | 76.327% | 128 px | 5.307% | 1.113 |
| 2000 | 80.473% | 99.5 px | 4.125% | 0.865 |
| 2100 | 84.619% | 71.5 px | 2.964% | 0.622 |
| 2250 | 90.837% | 71.5 px | 2.964% | 0.622 |

The calf expands after the knee, peaks near 74–75% H, then tapers strongly into the ankle.

## 13. Ankle / foot

### Ankle

```text
best reference Y ≈ 2250 px = 90.837% H
per-side width ≈ 72 px
measurement uncertainty ≈ 69–75 px
best width = 2.985% H
```

### Forefoot

At y≈2420:

```text
left width ≈ 101 px
right width ≈ 97 px
bilateral best average ≈ 99 px
best = 4.104% H
```

Relationship:

```text
forefoot / ankle width ≈ 99 / 72 = 1.375
```

Only the visible front-view footprint is measured; no unseen foot depth is inferred.

## 14. Arms / hands — first-pass anchors

Front-neutral pose coarse anchors:

```text
elbow region best ≈ y 920 px = 35.697% H
wrist region best ≈ y 1210 px = 47.720% H
fingertip best ≈ y 1390 px = 55.182% H
```

Uncertainty is wider than for legs because hair / garment overlap complicates elbow selection:

```text
elbow ≈ y 900–940
wrist ≈ y 1195–1225
fingertip ≈ y 1380–1400
```

These should remain SOFT until a later author review confirms the arm landmarks.

## 15. Whole-body cross-part ratios

Best-value relationships from the formal Master:

```text
lower outer pair / shoulder      = 1.020
mid-torso / shoulder             = 0.748
upper-torso envelope / shoulder  = 0.793
upper-thigh / knee width         = 1.713
calf-max / knee width            = 1.139
ankle / knee width               = 0.626
forefoot / ankle width           = 1.375
```

These ratios are scale-independent and useful for future Production gates.

## 16. Proposed Production reproduction bands — NOT YET ACTIVE

The ranges below are deliberately wider than pixel-selection uncertainty but still centered on the formal Master. They are the first author-review proposal, not frozen gates.

| Metric | Master best | Proposed allowed band | Proposed priority |
|---|---:|---:|---|
| chin Y% | 15.589% | 15.2–16.0% | HARD candidate |
| shoulder Y% | 19.527% | 19.0–20.1% | HARD candidate |
| shoulder width / H | 16.584% | 15.9–17.3% | HARD candidate |
| face cheek width / H | 11.070% | 10.6–11.5% | SOFT/HARD TBD |
| hair max outer width / H | 26.202% | 25.0–27.4% | SOFT |
| final hair endpoint Y% | AUTHOR_OVERRIDE | 39.0–41.0% | HARD candidate |
| upper-torso frontal width / H | 13.143% | 12.5–13.8% | HARD candidate |
| mid-torso narrow width / H | 12.396% | 11.9–12.9% | HARD candidate |
| lower-torso width / H | 14.013% | 13.4–14.7% | HARD candidate |
| Production boundary Y% | 49.461% | 48.5–50.5% | HARD candidate |
| upper-thigh per-side width / H | 8.147% | 7.8–8.6% | HARD candidate |
| mid-thigh width / H | 5.763% | 5.4–6.1% | HARD candidate |
| knee center Y% | 68.035% | 67.2–68.9% | HARD candidate |
| knee width / H | 4.768% | 4.5–5.1% | SOFT/HARD TBD |
| calf maximum Y% | 74.461% | 73.5–75.5% | SOFT/HARD TBD |
| calf max width / H | 5.431% | 5.1–5.8% | HARD candidate |
| ankle Y% | 90.837% | 90.0–91.8% | SOFT |
| ankle width / H | 2.985% | 2.8–3.2% | SOFT |
| forefoot width / H | 4.104% | 3.8–4.4% | SOFT |
| lower outer pair / shoulder | 1.020 | 0.97–1.07 | HARD candidate |
| mid-torso / shoulder | 0.748 | 0.72–0.78 | HARD candidate |
| upper-thigh / knee | 1.713 | 1.60–1.83 | HARD candidate |
| calf-max / knee | 1.139 | 1.05–1.24 | HARD candidate |
| ankle / knee | 0.626 | 0.57–0.69 | SOFT |
| forefoot / ankle | 1.375 | 1.25–1.50 | SOFT |

### Bilateral symmetry proposal

The selected leg cross-sections differ only by a few pixels left/right.

First proposal:

```text
matched L/R width difference <= 3% relative = preferred PASS
> 6% relative without pose/foreshortening reason = review/fail candidate
```

Do not use this in non-frontal or intentionally asymmetric poses without pose normalization.

## 17. Upper-torso / chest-region safety and measurement rule

For Production specification, the frontal upper-torso/chest region is represented numerically only by visible 2D frontal envelope and contour continuity.

```text
NO unseen depth estimate
NO generic cup/size taxonomy
NO added anatomical projection beyond the Master
NO amplification beyond Sample 9
```

The measured front-envelope width at y≈740 is approximately 317 px / 13.143% H and the final qualitative gate should compare the neutral Master silhouette, not invent 3D volume from the front view.

## 18. What is not yet frozen

The following remain pending author review:

```text
all proposed allowed bands
HARD vs SOFT final classification
coarse face width priority
arm/elbow/wrist gates
exact hair endpoint production band
skin/hair color soft bands
```

Fine Face Identity, ear geometry, hairstyle-part decomposition, and face-up reference work remain deferred to the separately planned Face/Hair phase.

## 19. Next decision checkpoint

Author reviews the measured values and proposed allowed bands.

After approval / edits:

1. promote accepted ranges into `YURA_DETAILED_PART_SPEC.md`;
2. freeze the Production gate semantics;
3. create `YURA_MASTER_VISUAL_DESCRIPTION.md` from formal Master + explicit AUTHOR_OVERRIDE items;
4. run the first GPT full-body reproduction test;
5. only after that checkpoint, begin Hair-style / face-up / ear-inflation work.
