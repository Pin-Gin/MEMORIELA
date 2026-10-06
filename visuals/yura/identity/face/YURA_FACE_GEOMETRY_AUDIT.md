# YURA Face Geometry Audit

Status: **ACTIVE AUDIT RECORD / INITIAL REVIEW / NOT VISUAL AUTHORITY**

This file records the audit state of the currently active YURA Face Reference.

Audit target:

- `visuals/yura/identity/face/YURA_FACE_REFERENCE.png`
- governed by `visuals/yura/identity/face/FACE_REFERENCE_RULES.md`

Revision process:

- `visuals/yura/identity/face/FACE_GEOMETRY_REVISION_LIFECYCLE.md`

This document is evidence and process state. It is not itself Face Authority.

---

## Audit objective

Determine whether the current Face Reference is geometrically strong enough to become the long-term canonical YURA face, independently from full-body scale.

The audit must answer whether the current reference has balanced:

- eye spacing and eye size;
- nose / mouth / chin placement;
- lower-face proportions;
- forehead / upper-head impression;
- ear size and placement;
- face contour;
- apparent head size after separating hair volume from actual face/head geometry.

The purpose is not to force the face toward generic human or generic anime averages. Numeric measurements are diagnostic tools for reproducing author-approved YURA identity.

---

## Current project decision

Face Geometry concerns are now formally tracked, but the current reference remains the active baseline until evidence justifies revision and the author explicitly approves a replacement.

No candidate has been promoted.

No current concern is allowed to alter Body Geometry targets automatically.

---

## Current concerns queued for audit

### 1. Eye spacing

Question:

> Are YURA's eyes too far apart relative to eye width and face width?

Current state:

- **NEEDS_NUMERIC_QA**

Required measurements:

```text
left/right inner eye landmarks
left/right outer eye landmarks
left/right eye centers
face edges at eye line

inner_eye_gap / average_eye_width
eye_center_distance / face_width_at_eye_line
average_eye_width / face_width_at_eye_line
```

Do not revise from impression alone.

---

### 2. Mouth vertical placement

Question:

> Is the mouth too high relative to the chin / lower face?

Current state:

- **NEEDS_NUMERIC_QA**

Required landmarks:

```text
nose reference point
mouth center
chin
```

Recommended diagnostic ratios:

```text
mouth_to_chin / nose_to_chin
nose_to_mouth / nose_to_chin
```

The lower face must be judged together with jaw/chin contour; a short-looking lower face is not automatically caused by mouth placement alone.

---

### 3. Forehead / upper-head impression

Question:

> Is the forehead or upper head too large, making the head read oversized?

Current state:

- **NEEDS_NUMERIC_QA**

Important separation:

```text
visible forehead
actual face height
actual skull/head silhouette
hair crown volume
bangs / hairline visibility
crop and framing
```

The current hairstyle can obscure the true hairline, so visible forehead alone may not be a reliable skull metric.

---

### 4. Overall apparent head size

Question:

> Does the current Face Reference cause an oversized-head impression independent of the intended face identity?

Current state:

- **WATCH / NEEDS_INTEGRATION_QA**

This must be separated from full-body head-to-body scale.

The Face Reference is explicitly denied authority over full-body scale. A face-up crop must not dictate the size of the head in a 7.2-head full-body target.

Potential causes to distinguish:

```text
face oval too large
skull/head silhouette too tall or wide
hair volume too large
crop/framing illusion
full-body integration incorrectly inheriting reference-image head scale
```

---

### 5. Ear height / prominence

Question:

> Are the ears too long or too visually prominent for the intended YURA face?

Current state:

- **WATCH-HIGH / PRIORITY REVIEW ITEM**

This is currently the clearest repeated face-specific concern.

Recommended landmarks:

```text
ear top
ear bottom
eye line
nose line
mouth line
face crown/chin or other stable face-height anchors
```

Recommended diagnostic values:

```text
ear_height / face_height
ear_top relative to eye line
ear_bottom relative to nose/mouth region
```

Do not correct ears by globally changing face height or head scale.

If a revision is justified, the preferred experiment is a local ear-geometry revision while preserving:

- eye geometry;
- nose/mouth geometry;
- jaw/chin contour;
- face identity;
- hair identity.

---

### 6. Eye / nose / mouth overall balance

Question:

> After separating forehead, ear, and head-scale effects, do the major facial features form a balanced YURA-specific arrangement?

Current state:

- **NEEDS_NUMERIC_QA + AUTHOR VISUAL REVIEW**

This category must not be reduced to one universal "golden ratio".

The final decision should combine:

```text
measured geometry
current Face Identity
candidate comparisons if needed
author visual judgement
```

---

## Provisional status summary

```text
Face Identity stability                 PASS / retain active baseline
Eye spacing                             NEEDS_NUMERIC_QA
Eye size                                WATCH / no revision authorized yet
Nose-mouth-chin vertical balance        NEEDS_NUMERIC_QA
Forehead / upper-head impression        NEEDS_NUMERIC_QA
Overall apparent head size              WATCH / needs integration separation
Ear height / prominence                 WATCH-HIGH / priority review
Face contour                            no confirmed failure recorded yet
```

These are audit states, not final geometry verdicts.

---

## Numeric QA landmarks to define next

The next formal Face Geometry measurement pass should define a reproducible landmark schema for the active reference.

Candidate landmarks:

```text
head_crown
face_top_anchor where measurable
chin
left_face_edge_at_eye_line
right_face_edge_at_eye_line
left_inner_eye
left_outer_eye
right_inner_eye
right_outer_eye
left_eye_center
right_eye_center
nose_reference
mouth_center
left_ear_top
left_ear_bottom
right_ear_top
right_ear_bottom
```

If a landmark is hidden by hair or rendering, record it as not measurable rather than inventing its position.

---

## Candidate revision policy

No face revision candidate should be generated until the problem statement is explicit.

Examples:

```text
EAR REVISION
change only ear height/prominence
preserve all other face geometry

EYE-SPACING REVISION
change only spacing after numeric evidence
preserve eye shape/size and other facial features

LOWER-FACE REVISION
change only the specifically diagnosed vertical relationship
preserve identity and unrelated geometry
```

One major variable per paid revision experiment is preferred.

---

## Relationship to current full-body work

The current full-body project has exposed a separate approximately-6.4-head convergence issue when using Face Reference with full-body generation.

This audit does not assume that the Face Reference itself should define that head-to-body scale.

Required integration principle remains:

```text
FACE IDENTITY = FACE AUTHORITY
FACE FEATURE GEOMETRY = FACE AUTHORITY after audit/approval
HEAD-TO-BODY SCALE = BODY GEOMETRY AUTHORITY
TOTAL HEAD COUNT = BODY GEOMETRY AUTHORITY
```

A future finalized Face Master should therefore be reusable at the correct full-body scale rather than forcing the body to inherit the face-up crop scale.

---

## Next action

When Face Geometry audit execution begins:

1. load the exact active `YURA_FACE_REFERENCE.png`;
2. confirm its SHA / Git provenance;
3. define visible landmarks without guessing hidden points;
4. record pixel coordinates;
5. compute normalized ratios;
6. compare numeric results with author visual judgement;
7. classify each concern as PASS / WATCH / FAIL;
8. create a revision candidate only for confirmed issues;
9. re-audit candidate with the same definitions;
10. promote only after explicit author approval.

Until that measurement pass is completed, the current reference stays active and the concerns above remain diagnostic questions rather than final failures.
