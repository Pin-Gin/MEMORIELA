# YURA Face Geometry Audit

Status: **ACTIVE AUDIT RECORD / NUMERIC AUDIT EXECUTED / NOT VISUAL AUTHORITY**

This file records the audit state of the currently active YURA Face Reference.

Audit target:

- `visuals/yura/identity/face/YURA_FACE_REFERENCE.png`
- governed by `visuals/yura/identity/face/FACE_REFERENCE_RULES.md`

Revision process:

- `visuals/yura/identity/face/FACE_GEOMETRY_REVISION_LIFECYCLE.md`

This document is evidence and process state. It is not itself Face Authority.

---

## Audit objective

Determine whether the current Face Reference is geometrically strong enough to remain the canonical YURA face baseline, independently from full-body scale.

The audit specifically checks:

- eye spacing and eye size;
- facial center-line alignment;
- nose / mouth / chin placement;
- lower-face proportions;
- forehead / upper-head impression;
- ear size, placement, and prominence;
- face contour;
- apparent head size after separating hair volume from actual face/head geometry where possible.

The purpose is not to force the face toward generic human or generic anime averages. Numeric measurements are diagnostic tools for reproducing author-approved YURA identity.

---

## Source verification

The exact active image was loaded and visually inspected.

```text
file = visuals/yura/identity/face/YURA_FACE_REFERENCE.png
image dimensions = 372 × 364 px
Git blob SHA = 4c96c4ec42f996807248be1aff60ec8a090fd570
SHA-256 = 3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
```

The inspected image bytes matched the active Git blob recorded by `FACE_REFERENCE_RULES.md`.

Visual inspection capability for this audit: **AVAILABLE**.

---

## Measurement method and uncertainty

Coordinates use image-space convention:

```text
origin = upper-left
x increases rightward
y increases downward
```

Landmarks were placed by direct visual inspection on the native 372 × 364 image, with enlarged crops used for confirmation.

Because the source is a rendered anime face rather than a landmark chart, anti-aliasing, eyelashes, hair overlap, and soft facial edges introduce uncertainty.

Unless otherwise noted, landmark coordinates should be interpreted as approximately **±2–4 px**, not as sub-pixel anatomical ground truth.

Hidden landmarks are not invented. In particular, the true hairline / forehead-top boundary is obscured by bangs and is therefore not treated as measurable.

---

## Measured landmark set

Approximate native-image landmarks used for this audit:

```text
head crown / visible hair crown      = (186, 8)
chin                                  = (187, 252)

left face edge at eye-line proxy      = x 109
right face edge at eye-line proxy     = x 270

left eye outer corner                 = (119, 173)
left eye inner corner                 = (166, 176)
right eye inner corner                = (206, 173)
right eye outer corner                = (253, 169)

left eye horizontal center proxy      = x 142.5
right eye horizontal center proxy     = x 229.5

nose reference                        = (186, 201)
mouth center                          = (187, 222)

left visible ear top                  = y 164
left visible ear bottom               = y 207
right visible ear top                 = y 158
right visible ear bottom              = y 204
```

The face-edge-at-eye-line points are visual proxies because hair partially obscures the temple boundary.

---

## Derived measurements

### Eye geometry

```text
left eye projected width  = 47 px
right eye projected width = 47 px
average eye width         = 47 px
inner-eye gap             = 40 px

inner_eye_gap / average_eye_width
= 40 / 47
≈ 0.85
```

Eye center separation proxy:

```text
right eye center - left eye center
= 229.5 - 142.5
= 87 px
```

Face width proxy at eye line:

```text
270 - 109 = 161 px
```

Therefore:

```text
eye_center_distance / face_width_at_eye_line
≈ 87 / 161
≈ 0.54

average_eye_width / face_width_at_eye_line
≈ 47 / 161
≈ 0.29
```

### Facial center-line alignment

```text
midpoint between eye centers ≈ x 186
nose reference               ≈ x 186
mouth center                 ≈ x 187
chin                         ≈ x 187
```

The major facial center-line landmarks align within roughly 1 px in this audit.

### Nose-mouth-chin vertical balance

```text
nose y  = 201
mouth y = 222
chin y  = 252

nose→chin  = 51 px
nose→mouth = 21 px
mouth→chin = 30 px
```

Normalized position within the nose→chin interval:

```text
nose→mouth / nose→chin
= 21 / 51
≈ 0.41

mouth→chin / nose→chin
= 30 / 51
≈ 0.59
```

The mouth therefore sits slightly above the midpoint of the nose→chin interval, leaving more vertical space below the mouth than above it.

### Ear visibility / vertical span

Visible ear spans:

```text
left ear  ≈ 43 px
right ear ≈ 46 px
average   ≈ 44.5 px
```

Visible crown→chin head span:

```text
252 - 8 = 244 px
```

Diagnostic only:

```text
average visible ear span / visible crown→chin head span
≈ 44.5 / 244
≈ 18.2%
```

This ratio is **not** treated as a universal ear standard because crown→chin includes hair-crown volume and is not identical to true face height.

---

## Audit results

### 1. Face Identity stability

**Status: PASS**

The current reference is internally coherent and clearly usable as the current YURA identity baseline.

No evidence was found that the face should be discarded wholesale.

---

### 2. Eye spacing

**Status: PASS / LOW WATCH**

The concern was:

> Are the eyes too far apart?

Measured self-relative evidence:

```text
inner-eye gap ≈ 0.85 × average eye width
```

The gap is smaller than one eye width, and the eye-center midpoint aligns almost exactly with the nose / mouth / chin center line.

Visual inspection also does not show a clear "eyes are excessively far apart" failure.

Conclusion:

- no current evidence justifies moving the eyes inward;
- do not revise eye spacing at this stage;
- retain as a low-level WATCH only because the author explicitly raised the concern and future candidate comparison may still be informative.

---

### 3. Eye size

**Status: PASS / STYLE-DEPENDENT**

The eyes are large relative to the face-width proxy:

```text
average eye width / face width ≈ 0.29
```

However, this is consistent with the current soft-anime YURA identity and does not visually read as a geometry failure by itself.

No eye-size revision is justified from this audit alone.

---

### 4. Horizontal facial balance / symmetry

**Status: PASS**

The horizontal center of the two eyes, nose reference, mouth center, and chin are nearly coincident:

```text
central x ≈ 186–187
```

This is a strong result. There is no evidence of a meaningful horizontal drift in the central facial features.

Small left/right eyelid or rendering differences are within normal illustration asymmetry and landmark uncertainty.

---

### 5. Mouth vertical placement

**Status: PASS / WATCH**

The concern was:

> Is the mouth too high relative to the chin?

Measured result:

```text
nose→mouth = 41% of nose→chin span
mouth→chin = 59% of nose→chin span
```

So the mouth is above the midpoint of the nose→chin interval, but the lower-face silhouette does not visually show an obvious severe imbalance.

Conclusion:

- the mouth is not currently a confirmed failure;
- do not move it based only on the current concern;
- retain WATCH status until a deliberately revised candidate or author-preferred comparison face exists.

---

### 6. Lower-face / chin balance

**Status: PASS**

The chin is centered and the jaw converges cleanly toward it.

The lower face is compact, but no clear visual evidence shows that the chin is excessively short or that the mouth is collapsing the lower-face region.

No lower-face global reshape is justified at this stage.

---

### 7. Forehead / upper-head geometry

**Status: NOT_MEASURABLE_FROM_CURRENT_REFERENCE**

The concern was:

> Is the forehead too large and making the whole head too big?

The true hairline / forehead-top landmark is obscured by bangs.

Therefore the audit cannot reliably derive a true forehead-height ratio from this reference.

What can be said visually:

- the upper-head silhouette is large;
- the hairstyle has substantial crown / side hair volume;
- the apparent head-size impression is therefore strongly influenced by hair volume;
- the current image does **not** provide enough evidence to conclude that the underlying skull or forehead itself is too large.

Do not reduce skull height or forehead height based on this image alone.

---

### 8. Overall apparent head size

**Status: WATCH / INTEGRATION ISSUE MUST REMAIN SEPARATE**

The face-up image has a large apparent head silhouette, but that cannot be converted directly into full-body head-to-body scale.

The project has separately observed approximately 6.4-head convergence during full-body generation.

This audit does not establish that the face geometry itself is the cause.

Required principle remains:

```text
FACE IDENTITY = FACE AUTHORITY
FACE FEATURE GEOMETRY = FACE AUTHORITY
HEAD-TO-BODY SCALE = BODY GEOMETRY AUTHORITY
TOTAL HEAD COUNT = BODY GEOMETRY AUTHORITY
```

The correct next full-body integration test is to preserve this face while explicitly denying the Face Reference authority over physical head scale.

---

### 9. Ear height / prominence

**Status: WATCH-HIGH / REVISION CANDIDATE JUSTIFIED IF AUTHOR CONFIRMS**

This remains the strongest face-specific concern.

Measured visible vertical spans are approximately:

```text
left ear  ≈ 43 px
right ear ≈ 46 px
```

The raw numeric span alone does not prove a generic anatomical failure. However, direct visual inspection supports the author's earlier concern that the ears read somewhat long / prominent for the intended YURA face.

The issue appears to be a combination of:

- vertical span;
- degree of exposure beside the hair;
- top/bottom placement relative to the eye / nose region.

Conclusion:

- ears are the first local face-geometry item worth testing;
- if revised, change ear geometry only;
- do not globally shrink the face or alter head-to-body scale to solve the ear issue.

Recommended first candidate contract:

```text
PROBLEM TO FIX:
  ears read too long / prominent for intended YURA identity

MAY CHANGE:
  ear vertical height
  ear top/bottom placement
  local exposure / prominence

MUST NOT CHANGE:
  eye spacing
  eye size / shape
  eyebrows
  nose
  mouth
  jaw / chin contour
  central face alignment
  hair identity except the minimum local interaction required around the ears

EXPECTED RESULT:
  lower ear prominence while preserving the current face identity
```

No numeric percentage reduction is frozen yet. A revision amount should be author-approved rather than invented by this audit.

---

### 10. Eye / nose / mouth overall balance

**Status: PASS WITH WATCH ITEMS**

After measuring the visible geometry:

- horizontal center-line balance is strong;
- eye spacing does not show a clear over-spacing failure;
- mouth vertical placement is slightly high within the nose→chin span but not visually broken;
- lower-face contour is coherent;
- the main unresolved visual concern is the ears;
- true forehead height cannot be determined because the hairline is hidden.

The current face is therefore much closer to "retain and locally refine" than "redesign the face."

---

## Updated status summary

```text
Face Identity stability                 PASS
Eye spacing                             PASS / LOW WATCH
Eye size                                PASS / style-dependent
Horizontal facial center-line           PASS
Nose-mouth-chin vertical balance        PASS / WATCH
Lower-face / chin contour               PASS
Forehead true geometry                  NOT_MEASURABLE_FROM_CURRENT_REFERENCE
Upper-head apparent size                WATCH / hair-volume confound
Overall full-body head scale            NOT A FACE-AUDIT AUTHORITY
Ear height / prominence                 WATCH-HIGH / first revision target
Overall face-feature geometry           PASS WITH LOCAL WATCH ITEMS
```

---

## Audit conclusion

The active Face Reference is **not geometrically broken** and should remain the baseline.

This audit does **not** support broad changes to eye spacing, eye size, mouth position, jaw shape, or the whole head.

The strongest justified next face experiment is a **local ear-geometry revision only**, provided the author wants to proceed.

The forehead concern cannot be resolved from this reference because the true hairline is hidden. Apparent upper-head size must not be confused with skull size or full-body head-to-body scale.

The current face should therefore be treated as:

```text
IDENTITY BASELINE = RETAIN
BROAD FACE REDESIGN = NO
EAR LOCAL REVISION = CANDIDATE-LEVEL TEST JUSTIFIED
FULL-BODY HEAD SCALE = CONTINUE TO SOLVE IN BODY / INTEGRATION PIPELINE
```

No candidate is promoted by this audit.

Explicit author approval is still required for any Face Authority replacement.
