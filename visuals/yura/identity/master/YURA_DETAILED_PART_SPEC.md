# YURA DETAILED PART SPECIFICATION

Status: **DRAFT / CANONICAL PIXEL MEASUREMENT V1 COMPLETE / AUTHOR REVIEW REQUIRED / NOT YET GATE-ACTIVE**

This file is the working destination for the final YURA per-part Production specification.

It is not yet a Production Authority until the author reviews and freezes the proposed bands below.

Measurement governance:

`visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md`

Canonical measurement report:

`visuals/yura/identity/master/YURA_MASTER_PIXEL_MEASUREMENT_20261013.md`

## 0. Formal Master

```text
path = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
source = Variance Study Sample 9 original local RAW
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
binary commit = c20ffc31fe5ccd16323ce36b129af93014d269ee
canvas = 1440 x 2560 px
runtime exact-binary verification = PASS
```

The full-body Master is formally promoted by author decision.

The historic Body Guide discrepancy remains audit history and is not a reason to replace the Master.

## 1. Fact labels

Every final item must remain distinguishable as:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

Experimental ideas are not allowed into the Production Authority without explicit promotion.

## 2. Production measurement normalization

Directly visible normalization from the exact formal Master:

```text
visible hair crown best = y 59 px
visible sole best = y 2471 px
H = 2412 px

Y% = (y - 59) / 2412 * 100
W% = width_px / 2412 * 100
```

The hidden structural skull crown is not directly observable under the hair. Do not create a new Production hard gate by pretending a single exact structural-crown pixel was directly measured.

Historic head-count values remain audit data.

## 3. Explicit author correction — hair length

### AUTHOR_OVERRIDE

Sample 9 is accepted as formal Master but its hair is slightly shorter than final YURA intent.

Final semantic requirement:

```text
hair category = SUPER-LONG
SUPER-LONG is mandatory, not decorative wording
must read unmistakably as super-long
must reach the waist area clearly
merely long / mid-back impression = FAIL
increase relative to Sample 9 = modest only
must not become dramatically longer
must not extend substantially below the waist
```

Measured Sample 9 current layered endpoint:

```text
baseline endpoint ≈ y 950–980
best ≈ y 965
best = 37.562% H
```

Visible waist-region reference:

```text
≈ y 1005–1035
best ≈ y 1020
best = 39.842% H
```

First proposed Production endpoint band:

```text
39.0–41.0% H
approx y 1000–1048 on the canonical 1440x2560 Master scale
```

This numeric band is still **PROPOSED / AUTHOR REVIEW REQUIRED**.

## 4. Face — coarse full-body geometry only

Fine Face Identity is deferred to the later Face Reference phase.

### MEASURED_MASTER_FACT

```text
chin best y = 435 px = 15.589% H
visible cheek/face envelope = 264–270 px
best face width = 267 px = 11.070% H
```

Proposed reproduction bands:

```text
chin Y% = 15.2–16.0% H
face cheek width = 10.6–11.5% H
```

Face width priority remains SOFT/HARD TBD pending author review.

## 5. Hair

### MEASURED_MASTER_FACT

```text
silver-white / light neutral-cool
primarily straight
thin/light bangs with forehead visibility
narrow natural face-framing locks
no hair ornament
visible crown best y = 59
max outer silhouette width best ≈ 632 px = 26.202% H
measured outer width uncertainty ≈ 620–645 px
```

Measured hair color sample:

```text
median sRGB ≈ (239,236,239)
median CIELAB ≈ L*93.70, a*+1.53, b*-1.09
```

Proposed width band:

```text
25.0–27.4% H / SOFT
```

Final length uses the AUTHOR_OVERRIDE in Section 3.

Hair-style local structure, temple locks, ear-cover locks and hair-part decomposition are deferred to the dedicated Hair/Face phase.

## 6. Skin

### MEASURED_MASTER_FACT

Aggregate interior sampling from face/neck/arms/thighs/calves:

```text
median sRGB ≈ (253,244,242)
mean sRGB ≈ (252.1,242.8,240.3)
median CIELAB ≈ L*96.82, a*+2.66, b*+2.04
```

Robust sampled 10–90 percentile envelope:

```text
L* ≈ 94.84–97.61
a* ≈ +1.81–+3.70
b* ≈ +1.56–+3.15
```

Proposed SOFT reproduction band:

```text
L* = 94.5–98.5
a* = +1.0–+5.0
b* = +0.5–+4.5
```

Qualitative gate:

```text
pale clean anime skin
subtle warm/blush component
no gray/blue cast
no realistic photographic skin texture
```

## 7. Shoulders / upper torso

### Shoulder — MEASURED_MASTER_FACT

```text
shoulder line selection = y 525–535
best y = 530 = 19.527% H
outer span ≈ 390–410 px
best ≈ 400 px = 16.584% H
```

Proposed bands:

```text
shoulder Y% = 19.0–20.1%
shoulder width = 15.9–17.3% H
```

### Upper-torso frontal envelope — MEASURED_MASTER_FACT

At reference y≈740:

```text
width ≈ 310–325 px
best ≈ 317 px = 13.143% H
```

Proposed band:

```text
12.5–13.8% H
```

### Mid-torso narrow envelope — MEASURED_MASTER_FACT

At reference y≈800:

```text
width ≈ 295–305 px
best ≈ 299 px = 12.396% H
```

Proposed band:

```text
11.9–12.9% H
```

### Lower-torso envelope — MEASURED_MASTER_FACT

At reference y≈950:

```text
width ≈ 330–345 px
best ≈ 338 px = 14.013% H
```

Proposed band:

```text
13.4–14.7% H
```

The torso must preserve the Sample 9 progression: upper torso -> narrower mid-torso -> gently opening lower torso. A straight vertical column or broad rectangular torso is FAIL.

## 8. Upper-torso front-volume / chest-region rule

This region is measured as a neutral **front-view 2D silhouette only**.

### MEASURED_MASTER_FACT

The directly supported numeric proxy is the upper-torso frontal envelope:

```text
best ≈ 317 px = 13.143% H at y≈740
```

Production rule:

```text
NO unseen 3D depth inference
NO generic size taxonomy
NO added projection beyond the formal Master
NO flattening beyond the Master silhouette
NO amplification beyond the Master silhouette
```

The final qualitative PASS is visual comparison to the neutral Sample 9 front contour.

## 9. Waist / pelvis / Production lower-body boundary

### Visible waist-region reference — MEASURED_MASTER_FACT

```text
selection ≈ y 1005–1035
best ≈ y 1020 = 39.842% H
```

This visible garment/torso transition is useful as a hair-length reference but is not automatically the anatomical boundary.

### Production boundary — MEASURED_MASTER_FACT

Definition:

```text
central medial-thigh bifurcation / visible upper-lower structural transition
```

Measurement:

```text
selection = y 1245–1260
best = y 1252
best = 49.461% H
```

Proposed Production reproduction band:

```text
48.5–50.5% H
```

This proposed Production gate is derived from the formal Master. It does not rewrite the old Body Guide discrepancy as PASS.

### Lower outer span — MEASURED_MASTER_FACT

At y≈1300, just below the garment-obscured transition:

```text
outer bilateral span ≈ 400–416 px
best ≈ 408 px = 16.915% H
```

Cross-part ratio:

```text
lower outer span / shoulder span = 1.020
proposed band = 0.97–1.07
```

## 10. Thighs

### MEASURED_MASTER_FACT — contour profile

Per-side average widths:

| Y px | Y% H | Width px | Width % H | Relative to root |
|---:|---:|---:|---:|---:|
| 1300 | 51.451% | 196.5 | 8.147% | 1.000 |
| 1400 | 55.597% | 167.5 | 6.944% | 0.852 |
| 1500 | 59.743% | 139.0 | 5.763% | 0.707 |
| 1600 | 63.889% | 119.5 | 4.954% | 0.608 |
| 1700 | 68.035% | 115.0 | 4.768% | 0.585 |

Proposed bands:

```text
upper-thigh width ≈ 7.8–8.6% H
mid-thigh width ≈ 5.4–6.1% H
upper-thigh / knee width ratio ≈ 1.60–1.83
```

Qualitative gate:

```text
continuous curved taper
not a straight thin column
no abrupt local width collapse
left/right contour remains near-symmetric in neutral front pose
```

## 11. Knees

### MEASURED_MASTER_FACT

```text
knee center/narrow-joint selection = y 1685–1720
best y = 1700 = 68.035% H
per-side width ≈ 112–118 px
best ≈ 115 px = 4.768% H
```

Proposed bands:

```text
knee Y% = 67.2–68.9%
knee width = 4.5–5.1% H
```

Sample 9 knee placement is an explicit author-PASS trait.

## 12. Lower legs

### MEASURED_MASTER_FACT

| Y px | Y% H | Per-side width | Width % H | Relative to knee |
|---:|---:|---:|---:|---:|
| 1700 | 68.035% | 115.0 px | 4.768% | 1.000 |
| 1800 | 72.181% | 121.5 px | 5.037% | 1.057 |
| 1855 | 74.461% | 131.0 px | 5.431% | 1.139 |
| 1900 | 76.327% | 128.0 px | 5.307% | 1.113 |
| 2000 | 80.473% | 99.5 px | 4.125% | 0.865 |
| 2100 | 84.619% | 71.5 px | 2.964% | 0.622 |
| 2250 | 90.837% | 71.5 px | 2.964% | 0.622 |

Proposed calf gates:

```text
calf max Y% = 73.5–75.5%
calf max width = 5.1–5.8% H
calf-max / knee width = 1.05–1.24
```

The lower leg must expand after the knee, peak around the upper-mid calf, then taper strongly into the ankle.

## 13. Ankles / feet

### Ankle — MEASURED_MASTER_FACT

```text
reference y = 2235–2265
best y = 2250 = 90.837% H
width = 69–75 px
best = 72 px = 2.985% H
```

Proposed SOFT bands:

```text
ankle Y% = 90.0–91.8%
ankle width = 2.8–3.2% H
ankle / knee = 0.57–0.69
```

### Forefoot — MEASURED_MASTER_FACT

At y≈2420:

```text
left ≈ 101 px
right ≈ 97 px
best bilateral average ≈ 99 px = 4.104% H
```

Proposed bands:

```text
forefoot width = 3.8–4.4% H
forefoot / ankle = 1.25–1.50
```

Only front-view visible geometry is authoritative here.

## 14. Arms / hands — coarse first pass

### MEASURED_MASTER_FACT with wider uncertainty

```text
elbow region ≈ y 900–940; best 920 = 35.697% H
wrist region ≈ y 1195–1225; best 1210 = 47.720% H
fingertip ≈ y 1380–1400; best 1390 = 55.182% H
```

These remain SOFT / review-only until author confirms the selected arm landmarks.

## 15. Whole-body cross-part identity

### MEASURED_MASTER_FACT

```text
lower outer pair / shoulder      = 1.020
mid-torso / shoulder             = 0.748
upper-torso envelope / shoulder  = 0.793
upper-thigh / knee width         = 1.713
calf-max / knee width            = 1.139
ankle / knee width               = 0.626
forefoot / ankle width           = 1.375
```

First proposed scale-independent bands:

```text
lower outer pair / shoulder = 0.97–1.07
mid-torso / shoulder        = 0.72–0.78
upper-thigh / knee          = 1.60–1.83
calf-max / knee             = 1.05–1.24
ankle / knee                = 0.57–0.69
forefoot / ankle            = 1.25–1.50
```

### Bilateral symmetry proposal

For the canonical neutral front pose only:

```text
matched L/R width difference <= 3% relative = preferred PASS
> 6% without pose/foreshortening explanation = review/fail candidate
```

Do not apply this unchanged to dynamic/asymmetric poses.

## 16. Proposed gate table — NOT YET ACTIVE

| Part | Metric | Master best | Proposed min | Proposed max | Priority proposal | Source |
|---|---|---:|---:|---:|---|---|
| Face | chin Y% | 15.589% | 15.2% | 16.0% | HARD candidate | MEASURED_MASTER_FACT |
| Face | cheek width / H | 11.070% | 10.6% | 11.5% | SOFT/HARD TBD | MEASURED_MASTER_FACT |
| Hair | outer width / H | 26.202% | 25.0% | 27.4% | SOFT | MEASURED_MASTER_FACT |
| Hair | final endpoint Y% | AUTHOR_OVERRIDE | 39.0% | 41.0% | HARD candidate | AUTHOR_OVERRIDE |
| Shoulder | Y% | 19.527% | 19.0% | 20.1% | HARD candidate | MEASURED_MASTER_FACT |
| Shoulder | width / H | 16.584% | 15.9% | 17.3% | HARD candidate | MEASURED_MASTER_FACT |
| Upper torso | width / H | 13.143% | 12.5% | 13.8% | HARD candidate | MEASURED_MASTER_FACT |
| Mid torso | width / H | 12.396% | 11.9% | 12.9% | HARD candidate | MEASURED_MASTER_FACT |
| Lower torso | width / H | 14.013% | 13.4% | 14.7% | HARD candidate | MEASURED_MASTER_FACT |
| Boundary | Y% | 49.461% | 48.5% | 50.5% | HARD candidate | MEASURED_MASTER_FACT |
| Upper thigh | width / H | 8.147% | 7.8% | 8.6% | HARD candidate | MEASURED_MASTER_FACT |
| Mid thigh | width / H | 5.763% | 5.4% | 6.1% | HARD candidate | MEASURED_MASTER_FACT |
| Knee | Y% | 68.035% | 67.2% | 68.9% | HARD candidate | MEASURED_MASTER_FACT |
| Knee | width / H | 4.768% | 4.5% | 5.1% | SOFT/HARD TBD | MEASURED_MASTER_FACT |
| Calf | max Y% | 74.461% | 73.5% | 75.5% | SOFT/HARD TBD | MEASURED_MASTER_FACT |
| Calf | max width / H | 5.431% | 5.1% | 5.8% | HARD candidate | MEASURED_MASTER_FACT |
| Ankle | Y% | 90.837% | 90.0% | 91.8% | SOFT | MEASURED_MASTER_FACT |
| Ankle | width / H | 2.985% | 2.8% | 3.2% | SOFT | MEASURED_MASTER_FACT |
| Foot | forefoot width / H | 4.104% | 3.8% | 4.4% | SOFT | MEASURED_MASTER_FACT |
| Whole body | lower outer pair / shoulder | 1.020 | 0.97 | 1.07 | HARD candidate | MEASURED_MASTER_FACT |
| Whole body | mid-torso / shoulder | 0.748 | 0.72 | 0.78 | HARD candidate | MEASURED_MASTER_FACT |
| Whole body | upper-thigh / knee | 1.713 | 1.60 | 1.83 | HARD candidate | MEASURED_MASTER_FACT |
| Whole body | calf-max / knee | 1.139 | 1.05 | 1.24 | HARD candidate | MEASURED_MASTER_FACT |

No proposed range above is active until author approval.

## 17. Historic Sample 9 audit values — audit only

Previous structural-crown QA-equivalent estimates remain:

```text
Head best              ≈ 7.214 heads
Boundary best          ≈ 49.17% of structural-crown→soles
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

The old Body Guide targets (`53.7037% boundary`, `46.0–46.5% inseam`, `2.7985–2.942 heads`) remain Master-generation audit history and are not automatically the new Production gate.

## 18. Current qualitative gates

### Face
Compact, soft face identity; not long/mature/model-like.

### Hair
Silver-white straight identity + final SUPER-LONG AUTHOR_OVERRIDE.

### Skin
Pale, clean 2D-anime skin with subtle warmth.

### Shoulders / torso
Narrow compact Sample 9 silhouette. No broadening into a large/model-like upper body.

### Upper-torso front contour
Match the neutral formal-Master front silhouette; neither flattened nor amplified.

### Waist / pelvis
Preserve Sample 9 torso-to-lower-body balance and visible transition.

### Thighs
Preserve the continuous curved taper profile; straight overly thin columns fail.

### Knees
Preserve Sample 9 knee placement closely.

### Lower legs
Preserve knee->calf expansion->ankle taper.

### Feet
Preserve small neutral front-view impression; no unseen 3D inference.

### Overall
A numeric pass cannot override an obvious identity mismatch. A visually correct output outside a proposed band triggers gate review rather than forced distortion.

## 19. Measurement state

```text
canonical binary hash verification = PASS
canonical canvas                    = 1440x2560
pixel measurement pass V1          = COMPLETE
measurement report                  = CREATED
proposed numeric bands              = CREATED
proposed bands gate-active          = NO
author tolerance review             = NEXT
Production Visual MD                = NOT YET
GPT full-body reproduction          = NOT YET
Hair/Face/Ear research              = DEFERRED
```

## 20. Next checkpoint

Author reviews:

1. the measured Master values;
2. the proposed allowed bands;
3. HARD vs SOFT classifications;
4. the hair endpoint override band;
5. arm/wrist/elbow landmarks.

After review, freeze accepted values here, then create `YURA_MASTER_VISUAL_DESCRIPTION.md` and begin GPT full-body reproduction testing.

Only after that checkpoint begin the planned Hair-style / face-up / ear-inflation reference phase.
