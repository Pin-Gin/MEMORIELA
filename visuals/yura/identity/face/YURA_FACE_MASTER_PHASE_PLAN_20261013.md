# YURA FACE MASTER PHASE PLAN — 2026-10-13

Status: **AUTHOR-APPROVED WORK PLAN / FACE DETAILED SPEC NEXT / NOT YET FACE AUTHORITY**

This document records the author-approved sequencing decision made after the exact Sample 9 full-body Master was pixel-measured.

It is an operational decision record. It does not by itself replace the current Face Reference or promote any new Face Master.

## 1. Why the sequence changed

The previous plan deferred detailed Face/Hair/Ear work until after all full-body part gates were frozen and an initial full-body reproduction test was complete.

That sequence is now intentionally changed.

Reason:

1. The formal Sample 9 full-body Master is already fixed and its exact binary has been verified.
2. Canonical pixel measurement V1 has already established a detailed full-body baseline for shoulders, torso, pelvis transition, thighs, knees, lower legs, ankles, feet, arms/hands anchors, hair/skin color, and cross-part ratios.
3. The remaining Face problem is not merely a coarse full-body proportion problem. The project has a known ear elongation/inflation tendency.
4. Current rules already restrict ear size, yet the problem can still recur. This suggests that local Face/Hair geometry and occlusion may be part of the failure mode.
5. The current authority model already separates Face Identity from BODY proportion, so a face-up reference can be introduced without granting it authority over head-to-body scale, shoulder width, torso length, leg length, or full-body canvas occupancy.
6. Production Visual MD should not be frozen while a known Face-local failure remains structurally unresolved if that Face work can now be isolated without reopening BODY geometry.

Therefore the project will resolve Face detailed geometry and create a validated Face Master candidate before freezing Hair and Skin production details.

## 2. Current fixed baseline

Formal full-body Master:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

```text
source = Variance Study Sample 9 original local RAW
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
canvas = 1440 x 2560 px
formal author promotion = YES
```

Canonical pixel measurement V1:

`visuals/yura/identity/master/YURA_MASTER_PIXEL_MEASUREMENT_20261013.md`

Detailed full-body Production draft:

`visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md`

Body work is sufficiently advanced to protect the established full-body identity while Face-local work proceeds.

The full-body part bands are still proposed / not fully gate-active; this Face phase does not erase or restart that work.

## 3. Authority separation — mandatory

### Formal full-body Master

Controls:

```text
full-body visual baseline
overall build
shoulder / torso / pelvis / leg silhouette
full-body balance
coarse head placement within the body
SUPER-LONG total-length relation once final override is frozen
```

### Current / future Face Reference or Face Master

Controls only Face-local identity and geometry, such as:

```text
face shape
face aspect ratio
eye size / shape / spacing
brow / nose / mouth relative placement
midface / lower-face proportion
cheek / chin shape
ear actual geometry and local placement
face-local hair relationship where explicitly scoped
```

Explicitly denied:

```text
FACE -> head-to-body ratio = DENIED
FACE -> shoulder width = DENIED
FACE -> torso length = DENIED
FACE -> leg length = DENIED
FACE -> full-body scale = DENIED
FACE -> canvas occupancy = DENIED
```

A face-up crop must never be used to infer full-body scale.

### Future Hair Reference

May later control local hairstyle structure such as:

```text
bangs
face-framing locks
temple locks
ear-cover locks
side-long locks
back-main
outer-back
under-layer
```

It must not independently redefine:

```text
BODY geometry
ear actual size
full-body head ratio
total SUPER-LONG endpoint unless explicitly scoped to a full-length reference
```

## 4. Ear problem — split into three independent concepts

Do not treat “ear appearance” as a single variable.

### A. EAR ACTUAL GEOMETRY

The physical 2D ear shape implied by the Face image:

```text
ear top
ear bottom
ear height
outer projection from head side
ear lobe length / shape
orientation
```

### B. EAR VISIBLE GEOMETRY

How much of the ear is visible after hair overlap.

This is not equal to actual ear size.

### C. HAIR OCCLUSION

Hair strands crossing or covering the ear region:

```text
temple lock overlap
ear-cover lock overlap
front/behind-ear ordering
visible-ear fraction
```

A small visible ear fraction must not cause compensation by enlarging the actual ear.

The project must be able to represent:

```text
actual ear = within target
visible ear = partially hidden
hair occlusion = high
```

without interpreting the hidden ear as “too small.”

## 5. Existing ear rule carried into detailed measurement

The active visual specification currently states:

```text
ear actual height target = 20–22% of face vertical dimension
HARD MAX = 23%
ear visibility is lower priority than ear size / natural placement
ear may be partly or almost completely hidden by hair
no visibility compensation by enlarging, elongating, moving outward, or rotating the ear toward camera
```

These numbers remain the current working rule while the exact Face Reference is measured.

They are not to be silently replaced. If pixel measurement or author review suggests a revision, the old value and the new proposal must be distinguished and explicitly approved.

## 6. Face detailed specification — measurement scope

Before any new paid Face generation, measure the exact current Face Reference binary and compare it with the formal Sample 9 head/face region.

Required Face-local metrics should include where measurable:

```text
face vertical dimension
face maximum / cheek width
face width / face height
chin position
jaw taper
midface span
lower-face span

eye line Y
eye-to-eye spacing
single-eye width
eye width / face width
left-right eye symmetry

brow line Y
nose landmark Y
mouth line Y
mouth width / face width

EAR ACTUAL GEOMETRY:
ear top Y
ear bottom Y
ear actual height / face height
ear projection / face width
left-right difference

EAR VISIBLE GEOMETRY:
visible ear height
visible fraction of estimated actual ear

HAIR OCCLUSION:
temple-lock overlap
ear-cover-lock overlap
whether hair passes in front of / behind ear
```

Use `min / best / max` for ambiguous boundaries.

No hidden 3D ear depth may be invented from a 2D image.

## 7. Paid-generation discipline

### Stage 1 — design validation

After Face measurements and the corrected Face Reference / Face Master candidate design are complete:

```text
paid Face-only Pilot = 1 image
```

Purpose:

```text
validate that the specification / reference design points in the intended direction
check Face Identity
check ear actual size / shape
check ear visibility behavior
check local hair interaction
```

### Important promotion rule

One good paid Face Pilot is **NOT** sufficient to promote a formal Face Master.

A successful first image may only become:

```text
WORKING FACE MASTER CANDIDATE
```

Formal Face Master promotion requires stability testing later.

### Stage 2 — stability validation

After Hair detailed specification / Hair Reference and Skin freeze are sufficiently prepared, run approximately:

```text
~10 fixed-condition Face-only generations
```

Evaluate at minimum:

```text
Face Identity stability
face aspect ratio
eye geometry stability
midface / lower-face stability
ear actual geometry
ear size ratio
ear elongation / inflation
ear outward projection
ear visibility / occlusion behavior
temple / ear-cover hair interpretation
```

Promote a new formal Face Master only if the author-defined Face / ear gate is stable across the series.

Do not select one lucky image while ignoring the series behavior.

If the prompt, reference set, or relevant Face/Hair specification changes materially, that becomes a new fixed-condition test rather than being pooled silently with the previous series.

## 8. New active sequence

This sequence supersedes the older “freeze all body parts -> Production Visual MD -> full-body reproduction -> Face/Ear” sequencing only where the order conflicts.

New order:

```text
A. Formal Sample 9 full-body Master                 = COMPLETE
B. Canonical full-body pixel measurement V1        = COMPLETE
C. Face detailed specification                     = NEXT
D. Measure exact current Face Reference             = NEXT SUBTASK
E. Design corrected Face Reference / Face candidate
F. Free preflight / invariant review if a runner is created
G. Paid Face-only Pilot 1
H. Author review
I. If successful: Working Face Master Candidate only
J. Hair detailed specification + Hair Reference work
K. Skin detail / color gate freeze
L. ~10 fixed-condition Face-only stability runs
M. Formal Face Master promotion only if stable
N. Finish/freeze remaining full-body Production gates
O. Production Visual MD / YURA Master visual description
P. Full-body reproduction using formal full-body Master + Production Visual MD + promoted Face Authority
Q. Production-route cleanup / archive of old benchmark materials
```

## 9. Relationship to current Hair SUPER-LONG override

The current author override remains active:

```text
SUPER-LONG is mandatory
must clearly reach the waist area
ordinary-long / mid-back = FAIL
only modestly longer than Sample 9
not substantially below waist
```

Current first proposed endpoint band remains:

```text
39.0–41.0% of visible figure H
```

This Face phase does not freeze or replace the final Hair detail specification.

## 10. Working philosophy to preserve in new chats

The project must continue to use this decision discipline:

```text
measure exact approved source
-> separate measured fact from author override and test hypothesis
-> propose a gate
-> author review
-> freeze before validation
-> use fixed-condition tests
-> distinguish one good sample from reproducible stability
-> do not silently move gates after seeing results
```

The project optimizes for low drift and traceable authority, not for one-off attractive outputs.

When visual author judgment and an old experimental numeric gate disagree, do not erase either. Keep the historic measurement as audit data and record the explicit author promotion / override separately.

## 11. New-chat restart order

A new chat should read current `main` in this order before proposing next actions:

```text
1. tools/yura-master-benchmark/CURRENT_HANDOFF.md
2. tools/yura-master-benchmark/PIPELINE_STATE.md
3. visuals/yura/identity/face/YURA_FACE_MASTER_PHASE_PLAN_20261013.md
4. visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md
5. visuals/yura/identity/master/YURA_MASTER_PIXEL_MEASUREMENT_20261013.md
6. visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md
7. visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md
8. visuals/yura/identity/face/FACE_REFERENCE_RULES.md
9. visuals/yura/identity/master/YURA_VISUAL_TEXT.md only for currently active Face/ear rules that have not yet been replaced by Production Authority
```

If older documents contain the previous sequencing order, this 2026-10-13 author-approved Face-phase plan is the newer sequencing decision.

Do not revive Test 6, do not restart pelvis/boundary rerolling, and do not treat the historic Body Guide as the new Production gate.

## 12. Exact next action

No paid generation yet.

Next task:

```text
obtain / load the exact current YURA_FACE_REFERENCE.png binary
verify its repository identity / hash
measure Face-local geometry and ear/hair-overlap metrics
compare with the formal Sample 9 face region
prepare the Face detailed specification and corrected Face Master candidate design
```

Only after this measurement / design review should a one-image paid Face-only Pilot be authorized.
