# YURA Face Geometry Revision Lifecycle

Status: **ACTIVE PROCESS DOCUMENT / NOT VISUAL AUTHORITY**

This document defines how YURA Face Geometry is audited, revised, verified, and promoted without contaminating the active Face Identity Authority.

The active Face Authority remains:

- `visuals/yura/identity/face/YURA_FACE_REFERENCE.png`
- `visuals/yura/identity/face/FACE_REFERENCE_RULES.md`

This lifecycle does not itself define YURA appearance. It defines the controlled revision process.

---

## Primary objective

Create and preserve a high-quality canonical YURA face while minimizing visual drift and stochastic variance.

The face must satisfy both:

- **identity quality**: it must clearly remain YURA;
- **geometry quality**: eyes, nose, mouth, chin, forehead/head impression, ears, and related facial proportions must be well balanced and author-approved.

A visually recognizable face is not automatically geometrically final. Likewise, a mathematically regular face is not acceptable if it weakens YURA's identity.

---

## Separation of responsibilities

The project separates these concepts explicitly:

```text
FACE IDENTITY
  = who the face belongs to

FACE FEATURE GEOMETRY
  = relative position / size / spacing of facial features

HEAD-TO-BODY SCALE
  = controlled by Body Geometry during full-body generation
```

Face Geometry revision must never silently acquire authority over full-body proportions.

The active Face Reference must not define:

- total head count;
- head-to-body scale;
- body height;
- torso length;
- leg length;
- canvas occupancy;
- final full-body composition.

---

## Stage 0 — Freeze active baseline

Before auditing or revising, the current active reference is treated as a frozen baseline.

The baseline may be:

- inspected;
- measured;
- compared;
- used to define revision requirements.

It must not be silently modified in place during exploration.

Rejected candidates never become active reference material automatically.

---

## Stage 1 — Face Geometry Audit

Audit the active Face Reference for the following categories.

### Required visual categories

- eye size;
- eye spacing;
- eye vertical placement;
- left/right balance;
- eyebrow-to-eye relationship;
- nose placement;
- nose-to-mouth spacing;
- mouth placement;
- mouth-to-chin spacing;
- lower-face balance;
- cheek / jaw / chin contour;
- face width-to-height impression;
- forehead / upper-head impression;
- ear height, position, and prominence;
- hair-volume contribution to apparent head size.

### Recommended numeric metrics

Where landmarks are sufficiently visible, measure ratios rather than relying only on impression.

Examples:

```text
inner_eye_gap / average_eye_width
eye_center_distance / face_width_at_eye_line
average_eye_width / face_width_at_eye_line
mouth_to_chin / nose_to_chin
nose_to_mouth / nose_to_chin
face_width / face_height
ear_height / face_height
```

Forehead/head analysis must distinguish:

```text
actual face geometry
actual skull/head silhouette
visible forehead
hair volume / crown volume
crop or framing effects
```

Do not call a large hair silhouette a large skull without evidence.

---

## Stage 2 — Audit decision

Each concern receives one of these states:

```text
PASS
WATCH
FAIL
NEEDS_NUMERIC_QA
NOT_MEASURABLE_FROM_CURRENT_REFERENCE
```

Interpretation:

- **PASS**: no revision is currently justified;
- **WATCH**: plausible concern, but insufficient evidence for revision;
- **FAIL**: revision candidate should be created;
- **NEEDS_NUMERIC_QA**: visual judgement alone is insufficient;
- **NOT_MEASURABLE_FROM_CURRENT_REFERENCE**: the reference does not expose the required landmark reliably.

Author visual judgement remains the final decision layer.

---

## Stage 3 — Candidate revision

If revision is justified, create a non-authoritative candidate.

Recommended naming:

```text
YURA_FACE_REFERENCE_CANDIDATE_001.png
YURA_FACE_REFERENCE_CANDIDATE_002.png
...
```

Every candidate must have a written change contract:

```text
PROBLEM TO FIX
WHAT MAY CHANGE
WHAT MUST NOT CHANGE
EXPECTED IMPROVEMENT
```

Example:

```text
PROBLEM TO FIX: ears read too long vertically
MAY CHANGE: ear vertical size / placement
MUST NOT CHANGE: eyes, nose, mouth, face contour, hair identity
EXPECTED IMPROVEMENT: lower ear prominence while preserving YURA identity
```

A candidate is never Authority merely because it was generated.

---

## Stage 4 — Candidate re-audit

Apply the same audit categories and measurement definitions to the candidate.

Compare candidate against:

- active baseline;
- author intent;
- numeric measurements where valid;
- unintended collateral changes.

A local improvement that damages identity elsewhere is a failed revision.

---

## Stage 5 — Author approval

Promotion requires explicit author approval.

Before approval, record:

- candidate file;
- audit result;
- measured ratios used for the decision;
- remaining WATCH items;
- known limitations.

No automatic promotion is allowed.

---

## Stage 6 — Promotion

After explicit author approval:

1. replace the canonical active Face Reference;
2. update `FACE_REFERENCE_RULES.md` if scope or hashes changed;
3. record new file hashes / Git provenance;
4. preserve prior versions through Git history;
5. re-run the full-body benchmark preflight before another paid integration test.

Promotion affects Face Authority only. It does not authorize a new Body Geometry target.

---

## Stage 7 — Full-body integration verification

After Face promotion, verify that the updated Face Authority integrates with Body Geometry without reintroducing head-scale drift.

Required principle:

```text
FACE IDENTITY = FIXED
FACE FEATURE GEOMETRY = FIXED
HEAD-TO-BODY SCALE = BODY GEOMETRY RESPONSIBILITY
TOTAL HEAD COUNT = BODY GEOMETRY RESPONSIBILITY
```

The face must not be enlarged merely because the Face Reference image contains a large face crop.

If full-body integration changes facial geometry, treat that as an integration failure rather than silently redefining the Face Master.

---

## Failed-candidate policy

A rejected face candidate:

- may remain in experiment artifacts for diagnosis;
- may be measured;
- may be compared against later candidates;
- must not become a future generation reference unless explicitly promoted by the author.

This prevents self-referential identity drift.

---

## Current YURA audit questions

The following concerns are explicitly queued for audit and are not yet assumed to be failures:

- Are the eyes too far apart?
- Is the mouth vertically too high relative to the chin?
- Is the visible forehead / upper-head region too large?
- Does hair volume make the whole head read too large?
- Are the ears too long or too prominent?
- Are eye / nose / mouth positions internally balanced after those effects are separated?

These questions must be answered by audit evidence, not by prompt accumulation.

---

## Reuse for SHIORI, MIO, and later characters

Reuse this lifecycle architecture, not YURA-specific measurements.

Each character requires their own:

- active Face Identity baseline;
- audit measurements;
- author-approved geometry decisions;
- revision candidates;
- promotion history.

The project-level objective is a repeatable method that produces high-quality Masters with minimal drift across the cast.
