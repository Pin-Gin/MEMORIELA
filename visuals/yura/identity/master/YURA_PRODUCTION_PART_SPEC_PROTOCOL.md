# YURA PRODUCTION PART SPECIFICATION PROTOCOL

Status: **AUTHOR-DIRECTED / ACTIVE WORK PROTOCOL / NOT YET A PRODUCTION VISUAL AUTHORITY**

## 1. Purpose

This document fixes the working method for deriving the final YURA Production visual specification from the formally promoted full-body Master.

The goal is reproducibility, not free-form redesign.

The body-analysis phase is a neutral character-geometry / silhouette analysis. It is not intended to amplify sexual appeal, fetishize anatomy, or add provocative emphasis. Where body regions are measured, they are treated as technical image-space geometry only.

## 2. Formal source of truth

Canonical full-body Master:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

```text
source = Variance Study Sample 9 original local RAW
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
binary commit = c20ffc31fe5ccd16323ce36b129af93014d269ee
```

The exact binary above is the full-body visual source for Production part measurement.

Do not substitute:

```text
chat screenshots
recompressed copies
other variance-study samples
Test 6 outputs
old Master images
Git-history images
Memory-derived appearance
characters/YURA.md
story/**
manuscript/**
```

## 3. Phase-specific authority rule

The Master-generation Body Guide and historic numeric QA remain preserved for audit, but they did not match the author-selected final Master and Test 6 failed to move the generated body toward those values.

Therefore, for the new **Production reproduction gate**, do not silently reuse the old pelvis/inseam/torso numeric targets as acceptance criteria.

Production part specification must be derived from:

1. the formal Sample 9 full-body Master pixel geometry;
2. explicit author corrections confirmed after Master promotion;
3. later author-approved Face/Hair local references, once created.

Historic Body Guide values stay audit history unless the author explicitly reactivates them for a future experiment.

This is not a retroactive claim that the old Body QA passed.

## 4. Mandatory separation of three fact types

Every final specification item must be labeled conceptually as one of:

```text
MEASURED_MASTER_FACT
= directly measured or visually read from the formal Master

AUTHOR_OVERRIDE
= explicit author correction that intentionally differs from the visible Master

TEST / HYPOTHESIS
= experimental idea not yet promoted to Authority
```

Never merge these categories silently.

Current known AUTHOR_OVERRIDE:

```text
Hair length:
Sample 9 is slightly shorter than final intent.
Final identity must read unmistakably as SUPER-LONG.
Hair must reach the waist area clearly.
Merely long / mid-back = FAIL.
Only a modest extension relative to Sample 9 is intended.
Do not extend dramatically or substantially below the waist.
```

The formal Master image itself remains unchanged.

## 5. Required canonical-image verification before pixel measurement

Before any pixel measurement session:

1. load the exact canonical `YURA_VISUAL_MASTER.png` binary;
2. compute SHA-256;
3. require exact match with:
   `81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d`;
4. record image width / height / mode;
5. stop if the SHA does not match, unless the author explicitly authorizes measurement of a derivative copy.

A new chat must not estimate final gate values from remembered screenshots.

If the canonical binary cannot be accessed in the runtime, request the exact PNG as a file or a ZIP that preserves the PNG bytes.

## 6. Measurement coordinate system

All full-body Production ratios are normalized to the character figure, not to the output canvas.

Define:

```text
crown_y = structural crown of the skull, not the top of elevated hair strands
chin_y  = anatomical chin point
soles_y = lowest visible foot/sole pixel line
H        = soles_y - crown_y
HH       = chin_y - crown_y
```

Normalized vertical coordinate:

```text
Y% = (landmark_y - crown_y) / H * 100
```

Normalized horizontal width:

```text
W%H = (right_x - left_x) / H * 100
```

Head-relative local size:

```text
local_heads = local_pixel_span / HH
```

For bilateral widths, use the external anatomical/body silhouette rather than hair strands, garment bows, ribbons, or detached antialias pixels.

If clothing obscures an anatomical boundary, record min / best / max rather than pretending the landmark is exact.

## 7. Measurement uncertainty

Every ambiguous structural landmark is recorded as:

```text
min / best / max
```

Clear silhouette widths are measured at least twice independently. If the two readings differ, perform a third reading and use the median as `best`, while retaining the observed measurement spread.

No final numeric gate is frozen from a single guessed click.

## 8. Pixel edge policy

The image uses soft antialiasing and near-white materials. Therefore:

- do not use exact-white/non-white thresholding alone;
- use crops plus visual inspection of the intended contour;
- reject isolated antialias pixels and hair crossings when measuring body width;
- record the crop and y/x landmark definitions used;
- use Python for arithmetic and normalized percentages after landmarks are selected;
- do not OCR the image.

## 9. Parts to specify, in fixed order

The specification phase proceeds in this order and does not skip ahead:

```text
01 Face
02 Hair
03 Skin
04 Shoulders / upper torso
05 Upper-torso front-volume silhouette
06 Waist / pelvis
07 Thighs
08 Knees
09 Lower legs
10 Feet
11 Arms / hands
12 Whole-body ratios and cross-part relationships
```

The Face ear-correction project and Hair-style reference generation are deferred until this full-body part specification is complete.

## 10. Required measurements by part

### 10.1 Face — full-body coarse geometry

Measure only what the full-body Master can support reliably:

```text
structural head height HH
maximum visible head width excluding detached hair
face/chin vertical location
head-width / HH
HH / H
head-count = H / HH
```

Do not derive fine eye/ear geometry from the full-body Master. Fine face geometry remains Face-Reference work.

### 10.2 Hair

Measure:

```text
visible crown / structural crown distinction
maximum side-to-side hair silhouette width
left longest strand endpoint Y%
right longest strand endpoint Y%
central/back visible endpoint Y% where identifiable
hair endpoint relative to shoulder / chest / waist / pelvis landmarks
```

The measured Sample 9 length is descriptive only. Final SUPER-LONG target includes the explicit author override and therefore may intentionally exceed Sample 9 slightly.

Future Hair Reference work may subdivide the hairstyle in a 3D-style part model, e.g. bangs, face-framing locks, temple locks, ear-cover locks, side-long locks, back-main, outer-back, under-layer. That is a later TEST/HYPOTHESIS until author-approved.

### 10.3 Skin

Sample multiple clean skin regions that are not hair-shadowed and not garment-overlayed.

Candidate regions:

```text
cheek
upper arm
forearm
thigh
lower leg
```

Record median sRGB and optionally Lab/HSV summaries per region. Use a range, not a single exact color, because anime shading changes local luminance.

Final skin gate should protect the pale, lightly warm/blushed identity without forcing one flat fill color.

### 10.4 Shoulders / upper torso

Measure:

```text
shoulder-line Y%
maximum shoulder width W%H
upper-ribcage width W%H
underarm/upper-torso width W%H where visible
shoulder-width / head-width
shoulder-width / hip-width
```

Hair crossings are excluded from shoulder width.

### 10.5 Upper-torso front-volume silhouette

This is a neutral silhouette/volume gate, not a sexual-content gate.

Measure only reproducible front-view geometry supported by the image:

```text
upper-torso side-contour width at fixed y levels
left/right contour symmetry tolerance
vertical placement of maximum front-torso garment contour where visible
upper-torso width relative to ribcage / waist / shoulder width
```

Do not infer 3D depth that cannot be measured from a frontal 2D image.

Do not turn prose descriptors into exaggerated volume. The formal Master silhouette is the baseline.

### 10.6 Waist / pelvis

Measure:

```text
narrowest waist Y% and W%H
pelvis/hip widest Y% and W%H
structural crotch/pelvis boundary min/best/max Y%
waist width / hip width
hip width / shoulder width
waist-to-pelvis vertical span as %H and in heads
```

Garment waistband and shorts hem have no anatomical-landmark authority unless the author explicitly defines them as visual proxies for a separate garment measurement.

### 10.7 Thighs

For each leg, between structural boundary and knee, measure outer silhouette widths at normalized local positions:

```text
10% thigh span
25% thigh span
50% thigh span
75% thigh span
```

Also record:

```text
maximum thigh width and its Y%
left/right width difference
hip-to-thigh taper
thigh-to-knee taper
```

The goal is to reproduce Sample 9's soft feminine leg contour without adding or removing mass arbitrarily.

### 10.8 Knees

Measure:

```text
knee center Y%
knee width W%H
boundary→knee / knee→soles relationship
left/right knee-level difference
```

Knee position is a known author PASS trait in Sample 9 and therefore is a high-priority reproduction feature.

### 10.9 Lower legs

Measure each leg at:

```text
25% knee-to-sole span
50% knee-to-sole span
75% knee-to-sole span
ankle minimum width
calf maximum width and Y%
```

Record calf-to-ankle taper and left/right symmetry.

### 10.10 Feet

Front-view data can support:

```text
ankle-to-sole vertical span
maximum visible forefoot/toe-group width
left/right foot width difference
foot separation / stance width
```

Do not invent unseen 3D foot length from a front view.

### 10.11 Arms / hands

Measure:

```text
shoulder-to-elbow Y span where estimable
elbow Y%
wrist Y%
fingertip Y%
upper-arm / forearm width samples
hand length proxy relative to HH
left/right arm endpoint difference
```

### 10.12 Whole-body ratios

Record at minimum:

```text
H / HH head count
head width / HH
shoulder width / H
waist width / H
hip width / H
shoulder / hip
waist / hip
boundary Y%
knee Y%
inseam-like boundary-to-sole fraction as description of the Master
arm endpoint Y%
stance width / H
```

Historic values already recorded for Sample 9 are provisional audit measurements only:

```text
Head best              ≈ 7.214
Boundary best          ≈ 49.17%
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

These must be remeasured from the exact canonical PNG before entering the final Production gate table.

## 11. Gate-building rule

Do not invent tolerance ranges before the canonical measurement table exists.

For every metric, the final table must contain:

```text
metric name
landmark definition
Master min / best / max or exact best
normalized Master value
author-approved allowed minimum
author-approved allowed maximum
priority: HARD / SOFT / DIAGNOSTIC
source type: MEASURED_MASTER_FACT / AUTHOR_OVERRIDE
notes / exclusions
```

Initial proposed tolerances may be calculated after measurement, but they are not active until author review.

Reproduction testing is then used to calibrate the gate:

- if a visually accepted output repeatedly falls outside a proposed numeric band, review the band rather than forcing the character away from the accepted visual identity;
- if a visually wrong output falls inside the band, add/tighten a metric that actually captures the failure;
- never widen or tighten a gate silently after seeing a result;
- every gate revision must be documented and author-approved.

## 12. Priority classes

### HARD

Identity-defining geometry whose failure materially changes YURA.

Expected examples after measurement:

```text
head-count / head-to-body relation
overall build envelope
shoulder/hip relationship
waist/hip relationship
knee location
major thigh/calf contour
SUPER-LONG hair requirement
later: Face Identity and ear-size gate
```

### SOFT

Natural generation variation allowed within a wider band, e.g. minor left/right asymmetry or local strand placement.

### DIAGNOSTIC

Tracked to understand drift but not independently sufficient to fail an otherwise author-approved reproduction.

## 13. Body-spec wording rule

Body metrics must remain technical and image-space based.

Prefer:

```text
silhouette width
landmark position
contour curvature
taper
relative proportion
front-volume silhouette proxy
```

Avoid adding sexualized framing, provocative pose instructions, or anatomy emphasis that is not required to reproduce the formal Master.

## 14. Hair and ear future phase

After all full-body parts are frozen and GPT reproduction from Master + Production Visual MD is demonstrated:

1. create Hair-style reference candidates and a Hair definition MD;
2. explore 3D-style hair-part decomposition as a method to keep temple/ear-cover locks separate from ear geometry;
3. isolate the existing Face ear-enlargement issue;
4. create a corrected Face Reference/Master;
5. run approximately 10 fixed-condition Face-only generations;
6. promote only after author-defined Face/ear stability passes;
7. re-test full-body reproduction with the new Face Master + formal full-body Master + Production Visual MD.

Do not mix this ear/hair-reference experiment into the current full-body pixel-measurement phase.

## 15. New-chat continuity rule

A new chat continuing this work must first read, from current `main`:

```text
visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md
visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md
visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md
tools/yura-master-benchmark/CURRENT_HANDOFF.md
tools/yura-master-benchmark/PIPELINE_STATE.md
tools/yura-master-benchmark/TEST6_RESULT_20261012.md
```

Then load/verify the exact canonical Master PNG before calculating new pixel values.

Do not reconstruct missing values from chat memory, old screenshots, or historic Body Guide assumptions.
