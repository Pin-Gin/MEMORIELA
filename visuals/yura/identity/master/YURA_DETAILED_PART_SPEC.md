# YURA DETAILED PART SPECIFICATION

Status: **DRAFT / CANONICAL PIXEL MEASUREMENT PENDING / NOT YET GATE-ACTIVE**

This file is the working destination for the final YURA per-part Production specification.

It is not yet a Production Authority until the canonical Master has been measured, the numeric bands have been reviewed, and the author explicitly freezes the specification.

Measurement method and governance:

`visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md`

## 0. Formal Master

```text
path = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
source = Variance Study Sample 9 original local RAW
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
binary commit = c20ffc31fe5ccd16323ce36b129af93014d269ee
```

The full-body Master is formally promoted by author decision.

The known historic Body Guide discrepancy remains audit history and is not a reason to replace the Master.

## 1. Specification fact labels

Every frozen item must be one of:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
```

Experimental ideas are recorded as TEST/HYPOTHESIS elsewhere and are not allowed into this final table without explicit promotion.

## 2. Current explicit author correction

### Hair length — AUTHOR_OVERRIDE

Sample 9 is visually accepted as Master but is slightly shorter-haired than final YURA intent.

Final definition:

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

Hair color / general straight identity remains the Sample 9 / active Visual definition.

Numeric endpoint bands are **PENDING canonical pixel measurement + author review**.

## 3. Existing qualitative baseline carried from active visual definition

These items are source-supported baseline descriptions and will be converted into measurable Production terms where possible.

### Face

```text
small face
soft short oval tendency
not long-faced
shorter midface
compact lower face
small softly rounded chin
cheeks taper gradually rather than sharp V-line
```

Fine face-local geometry will later be handled by the Face Reference phase; the full-body Master supplies only coarse head/face proportions.

### Hair

```text
silver-white
primarily straight
super-long identity
thin/light bangs with some forehead visibility
natural narrow face-framing locks
no hair ornament
```

Final length uses the author override in Section 2.

### Skin

```text
very light/pale
subtle natural warmth/blush
smooth 2D anime rendering
no realistic skin texture
```

Final color bands: **PENDING pixel sampling**.

### Body / overall build

```text
slender but not excessively frail
relatively narrow shoulders and waist
hips-to-thighs retain soft natural volume
thighs / calves / ankles must not collapse into an extremely thin silhouette
```

All final width/landmark gates below are to be derived from Sample 9 pixels, not from generic anatomy.

## 4. Legacy Sample 9 audit values — NOT FINAL PART GATES

Historic QA-equivalent estimates already recorded:

```text
Head best              ≈ 7.214 heads
Boundary best          ≈ 49.17% of structural-crown→soles
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

These are retained as audit context only.

They must be remeasured from the canonical PNG before entering the final Production numeric table.

The old Body Guide targets (`53.7037% boundary`, `46.0–46.5% inseam`, `2.7985–2.942 heads`) are historic Master-generation QA, not automatically the new Production reproduction gate.

## 5. Final numeric table — schema

Each row will be filled after the canonical measurement pass.

| Part | Metric | Master min | Master best | Master max | Normalized value | Allowed min | Allowed max | Priority | Source | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| Whole body | crown→soles H | PENDING | PENDING | PENDING | 100% | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | canonical normalization |
| Head | crown→chin HH | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | structural crown |
| Head | H/HH head count | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | remeasure Sample 9 |
| Head | max head width / HH | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | detached hair excluded |
| Hair | longest endpoint Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | AUTHOR_OVERRIDE + measured baseline | final target slightly longer than Master |
| Hair | max silhouette width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | strand variation allowed |
| Shoulder | shoulder Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | hair excluded |
| Shoulder | width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | bilateral contour |
| Upper torso | ribcage width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | front silhouette |
| Upper torso | front-volume contour proxy | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | technical 2D contour only |
| Waist | narrowest Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | garment line not automatically authoritative |
| Waist | narrowest width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | body silhouette |
| Pelvis | widest Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | body silhouette |
| Pelvis | widest width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | body silhouette |
| Boundary | structural pelvis/crotch Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | DIAGNOSTIC/HARD TBD | MEASURED_MASTER_FACT | min/best/max |
| Thigh | max width L/R / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | feminine contour baseline |
| Thigh | 10/25/50/75% span widths | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD/SOFT TBD | MEASURED_MASTER_FACT | curvature profile |
| Knee | center Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | author PASS trait |
| Knee | width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | local contour |
| Calf | max width + Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD/SOFT TBD | MEASURED_MASTER_FACT | both legs |
| Ankle | min width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | both legs |
| Foot | ankle→sole span | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | front view |
| Foot | forefoot width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | front view only |
| Arm | elbow Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | L/R |
| Arm | wrist Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD/SOFT TBD | MEASURED_MASTER_FACT | L/R |
| Hand | fingertip Y% | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | L/R |
| Whole body | shoulder / hip width | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | cross-part identity |
| Whole body | waist / hip width | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | HARD | MEASURED_MASTER_FACT | cross-part identity |
| Whole body | stance width / H | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | SOFT | MEASURED_MASTER_FACT | neutral Master stance |

No `Allowed min/max` value may be filled by guesswork.

## 6. Part-specific qualitative gates to combine with the numeric table

### 6.1 Face

PASS requires preservation of the compact, soft face identity. A numerically correct full-body head that produces a long/mature/model-like face is still FAIL.

### 6.2 Hair

PASS requires both:

```text
Sample 9 silver-white straight identity preserved
AND
final SUPER-LONG author override satisfied
```

Hair-style local structure will be refined later with dedicated Hair Reference work.

### 6.3 Skin

PASS requires pale clean anime skin with subtle warmth, without gray/blue cast or realistic texture.

### 6.4 Shoulders / upper torso

PASS requires the narrow, compact Sample 9 upper-body silhouette. Do not broaden shoulders or torso to satisfy unrelated ratios.

### 6.5 Upper-torso front-volume silhouette

PASS is judged against Sample 9's neutral front silhouette. Do not flatten it, and do not exaggerate it beyond the Master.

This gate is technical character-shape reproduction only.

### 6.6 Waist / pelvis

PASS requires the Sample 9 waist-to-pelvis transition and overall balance. Historic Body Guide mismatch is not independently sufficient to reject a reproduction that matches the formal Master-derived Production gate.

### 6.7 Thighs

PASS requires Sample 9's soft curved thigh contour and adequate volume. A straight, overly thin model-like line is FAIL even if total body height is correct.

### 6.8 Knees

Sample 9 knee placement is an explicit author PASS trait and should be preserved closely.

### 6.9 Lower legs

PASS requires natural calf-to-ankle taper and the Sample 9 leg balance; do not lengthen thighs or shins independently to force a numeric target.

### 6.10 Feet

Preserve the small, neutral front-view foot/ankle impression of the Master without inventing unseen 3D geometry.

### 6.11 Overall

The final criterion is not any one percentage in isolation. The generated character must remain recognizable as the same YURA formal Master under the complete set of HARD + SOFT + qualitative gates.

## 7. Measurement status

```text
canonical binary hash known        = YES
canonical binary pixel access here = PENDING
full pixel measurement pass        = NOT YET
numeric table populated            = NOT YET
author tolerance review            = NOT YET
part spec frozen                    = NOT YET
Production Visual MD               = NOT YET
reproduction gate active           = NO
```

## 8. Next exact action

Load the exact canonical Master PNG and verify SHA256.

Then measure in this order:

```text
Face coarse geometry
Hair
Skin
Shoulders / upper torso
Upper-torso front-volume silhouette
Waist / pelvis
Thighs
Knees
Lower legs
Feet
Arms / hands
Whole-body ratios
```

Populate this document with the measured values and proposed allowed bands.

The author reviews and freezes each group before the final Production Visual MD is promoted.

## 9. Deferred Hair/Face reference work

Only after this document is substantially complete:

- create hairstyle-difference references;
- create a Hair-definition MD;
- create/inspect face-up references;
- explore 3D-style hair-part decomposition around temple/ear-cover locks;
- isolate ear inflation;
- create corrected Face Reference candidates;
- run ~10 fixed-condition Face-only stability generations;
- promote a new Face Master only after PASS;
- re-test whole-body generation with the new Face Master + formal full-body Master + Production Visual MD.
