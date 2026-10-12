# YURA Master / Production Specification — Current Handoff

Status: **SAMPLE 9 FORMAL FULL-BODY MASTER / TEST 6 CLOSED / CANONICAL PIXEL PART-SPEC PHASE ACTIVE**

This document is the operational restart point for a new chat. It is not itself a YURA visual Authority.

## 1. Scope lock

Current work is YURA visual Production-authority completion only.

Immediate task:

> Derive detailed per-part YURA specifications from the exact Sample 9 formal Master, using pixel measurements and normalized ratios, then freeze author-approved numeric/visual gates before GPT reproduction testing.

Do not begin unrelated outfits, pose packs, other characters, story work, or ear-correction experiments before the current part-spec phase reaches the planned checkpoint.

Do not use `git reset --hard` or force-push.

## 2. Formal full-body Master — fixed

Canonical file:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

```text
source = Variance Study Sample 9 original local RAW
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
binary commit = c20ffc31fe5ccd16323ce36b129af93014d269ee
```

Sample 9 is formally promoted by explicit author decision.

Do not substitute another sample, Test 6 output, screenshot, recompressed image, old Master, or historical Git image.

Master status:

`visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md`

## 3. Why Sample 9 remains formal Master

The original 10-run study found Sample 9 to have the best author-judged whole-body balance.

Test 6 then attempted to move the pelvis/boundary toward the historic Body Guide through a normalized textual anchor. Three fixed-condition paid samples all returned NO SUPPORT around the same failure region.

Result:

`tools/yura-master-benchmark/TEST6_RESULT_20261012.md`

```text
Sample 1 = NO SUPPORT
Sample 2 = NO SUPPORT
Sample 3 = NO SUPPORT
Sample 4–5 = NOT RUN
H6 = NO SUPPORT
further pelvis/boundary rerolling = STOP
```

Therefore Sample 9 is the formal full-body visual truth for the next Production specification phase.

## 4. Historic numeric discrepancy — audit only

Historic Sample 9 estimates:

```text
Head best              ≈ 7.214 heads
Boundary best          ≈ 49.17%
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

Historic Master-generation Body Guide targets:

```text
Head                    7.1–7.3
Boundary                53.7037%
Inseam                  46.0–46.5%
Chin→boundary           2.7985–2.942 heads
```

Do not relabel the historic mismatch as PASS.

However, do not automatically reuse the old boundary/inseam/torso targets as the new Production reproduction gate. The new Production gate is to be derived from the formally promoted Sample 9 pixel geometry plus explicit author corrections.

This phase-specific distinction is critical.

## 5. New active working documents

Read these before continuing:

```text
visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md
visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md
```

`YURA_PRODUCTION_PART_SPEC_PROTOCOL.md` fixes the measurement method, source discipline, gate-building rules, and new-chat workflow.

`YURA_DETAILED_PART_SPEC.md` is the working destination for actual per-part measurements and allowed ranges.

The detailed part spec is currently DRAFT and is not yet gate-active.

## 6. Core working philosophy

Every final visual claim must be separated into:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

Never merge them silently.

### MEASURED_MASTER_FACT

Directly read/measured from the formal Sample 9 Master.

### AUTHOR_OVERRIDE

Explicit author correction that intentionally differs from what Sample 9 visibly contains.

### TEST / HYPOTHESIS

Experimental idea not yet promoted to Authority.

No chat memory, generic anatomy, old image, or inferred preference may silently fill missing values.

## 7. Current explicit AUTHOR_OVERRIDE — SUPER-LONG hair

Sample 9 is accepted as Master but its hair is slightly shorter than final intent.

Frozen author intent:

```text
hair category = SUPER-LONG
SUPER-LONG is mandatory, not loose wording
must read unmistakably as super-long
must reach the waist area clearly
merely long / mid-back = FAIL
length increase vs Sample 9 = modest only
must not become dramatically longer
must not extend substantially below the waist
```

Do not edit the formal Master merely to conceal this known difference.

Encode the final hair requirement in the detailed spec / Production Visual MD and verify it in reproduction tests.

## 8. Neutral technical body-analysis rule

The body-analysis phase is for character geometry and reproducibility.

It is not intended to amplify sexual appeal, sexualize anatomy, fetishize a body region, or create provocative presentation.

Use technical terms such as:

```text
silhouette width
landmark position
normalized ratio
contour curvature
taper
front-volume silhouette proxy
```

For the upper torso/chest region, measure only front-view 2D silhouette geometry supported by the image. Do not invent unseen 3D depth and do not exaggerate the region beyond the formal Master.

## 9. Canonical pixel-measurement rule

Before calculating final numeric values, the runtime must have access to the exact canonical Master binary.

Required verification:

```text
SHA256 == 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

If the exact binary is unavailable in a new chat/runtime, request the canonical PNG as a file or a ZIP preserving the PNG bytes.

Do not derive final numbers from remembered screenshots.

The GitHub text connector can confirm the repository asset identity but does not expose usable binary pixels for image-space measurement; a measurable runtime copy is required.

Use Python for numeric calculations after landmarks are selected. Do not OCR.

## 10. Fixed measurement order

Proceed exactly in this order:

```text
01 Face — coarse full-body geometry only
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
12 Whole-body ratios / cross-part relationships
```

For ambiguous landmarks use `min / best / max` uncertainty.

Widths and vertical locations must be normalized to the character figure, not the output canvas.

Full definitions are in `YURA_PRODUCTION_PART_SPEC_PROTOCOL.md`.

## 11. Gate-building rule

Do not invent `Allowed min/max` before measurement.

For each metric, record:

```text
metric definition
Master min/best/max or exact best
normalized value
proposed allowed minimum
proposed allowed maximum
priority = HARD / SOFT / DIAGNOSTIC
source = MEASURED_MASTER_FACT / AUTHOR_OVERRIDE
```

Proposed tolerance bands become active only after author review.

During later reproduction validation:

- visually accepted outputs outside a proposed gate trigger gate review, not automatic character distortion;
- visually wrong outputs inside a proposed gate indicate the gate is insufficient;
- never modify a gate silently after seeing a result;
- gate changes require documentation + author approval.

## 12. Source restrictions

Do not use these as appearance sources:

```text
characters/YURA.md
story/**
manuscript/**
Memory-derived appearance
old branches / Git history as fallback
old rejected YURA images
Test 6 outputs as new Master
```

Current appearance work uses the formal Master plus current approved visual/face rules only as explicitly scoped.

## 13. Face / Hair / ear work — deferred but planned

After the full-body part specification and first GPT reproduction checkpoint:

1. create hairstyle-difference references;
2. create a dedicated Hair-definition MD;
3. create face-up reference candidates;
4. explore 3D-style hair-part decomposition such as bangs, face-framing locks, temple locks, ear-cover locks, side-long locks, back-main and under-layer;
5. test whether separating ear-cover hair geometry from ear geometry reduces ear elongation/inflation;
6. isolate the Face ear-size problem;
7. generate a corrected Face Reference/Master;
8. run approximately 10 fixed-condition Face-only generations;
9. promote the new Face Master only after the author-defined Face/ear gate passes;
10. re-test full-body generation with new Face Master + formal full-body Master + Production Visual MD.

Do not start this phase before the current detailed full-body part spec is substantially frozen.

## 14. Lifecycle after part specification

Planned sequence:

```text
FORMAL SAMPLE 9 MASTER
-> CANONICAL PIXEL MEASUREMENT
-> AUTHOR-APPROVED DETAILED PART GATES
-> YURA_MASTER_VISUAL_DESCRIPTION / Production Visual MD
-> GPT FULL-BODY REPRODUCTION TEST
-> HAIR / FACE-UP / EAR REFERENCE PHASE
-> ~10 FACE-ONLY STABILITY RUNS
-> NEW FACE MASTER IF PASS
-> FULL-BODY REPRODUCTION RECHECK
-> ARCHIVE OLD MASTER-GENERATION / BENCHMARK MATERIALS OUTSIDE NORMAL GENERATION ROUTE
```

Archive means isolate/retire from normal generation, not delete; rollback/audit material remains preserved.

## 15. Current exact next action

Obtain the exact canonical `YURA_VISUAL_MASTER.png` in the active runtime and verify its SHA.

Then begin the measurement sequence at:

```text
01 Face coarse geometry
02 Hair
03 Skin
...
```

Populate `YURA_DETAILED_PART_SPEC.md` progressively.

Do not start a paid generation call for this measurement phase.
