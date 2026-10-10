# YURA Test 6 — Pelvis/Boundary normalized-position lock

Status: **PREREGISTERED / IMPLEMENTATION COMPLETE / FREE PREFLIGHT NEXT / BOUNDED 1–5 SAMPLE SERIES**

## Purpose

Test exactly one remaining Body Geometry hypothesis after the completed 10-run variance study.

The 10-run study showed:

```text
visual quality can reach all-PASS
7.2-head best values can occur
but crotch/pelvis boundary placement remains systematically too high
```

The repeated boundary miss is the active problem.

## Single hypothesis

**H6**

> If the author-selected Sample 9 working Master is treated as the visual/edit baseline and the crotch/pelvis boundary is expressed as one explicit normalized structural anchor at the Body Guide position, the model can move that boundary downward toward the approved Guide geometry without redesigning the already-approved visual traits.

This test is about **boundary placement only**.

It is not a test of hair length, chest design, thigh design, Face Identity, knee design, Composition, or a new head-count target.

## Test 5 breakpoint inheritance rule

Test 6 is derived from the frozen Test 5 state.

The exact Test 5 compiler specification is preserved separately as a rollback/breakpoint artifact at:

`tools/yura-master-benchmark/archive/test5_breakpoint_20261011/codex_instruction_test5.md`

Frozen blob SHA:

```text
ced76faf3b382052c2928dd2ae0795c739ce2222
```

The former active Test 5 `tools/yura-master-benchmark/codex_instruction.md` has been retired from the active generation route after the archive copy was verified.

Test 6 must not modify that archived Test 5 instruction.

Test 6 uses newly created Test-6-specific files and changes only the causal elements required for the boundary experiment. All unchanged QA, Composition, safety, Authority-separation, and 7.2-head rules inherit the Test 5 behavior.

## Baseline

Working Master:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

SHA-256 of the committed original local Sample 9 RAW:

```text
81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

Binary commit:

```text
c20ffc31fe5ccd16323ce36b129af93014d269ee
```

Sample 9 recorded study values:

```text
Head best              ≈ 7.214
Boundary best          ≈ 49.17%
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

Guide target:

```text
structural crown = 0%
soles            = 100%

crotch/pelvis boundary
= (856 - 160) / (1456 - 160)
= 696 / 1296
= 53.7037037% downward from structural crown

equivalent crotch→soles fraction
= 46.2962963%

Guide chin→boundary
= 2.8667 heads
```

The implementation must use these values as **relative body geometry**, never as output-canvas absolute pixel coordinates.

## Exact boundary definition

The boundary means:

```text
CENTRAL MEDIAL-THIGH BIFURCATION
=
UPPER / LOWER BODY STRUCTURAL BOUNDARY
```

It does **not** mean:

```text
waistline
shorts waistband
garment hem
visible clothing seam
navel
hip widest point
```

Garment lines have no landmark authority.

## Test 6 intervention

Only the pelvis/boundary enforcement method may change.

The implementation makes the following normalized relationship explicit and primary:

```text
CROTCH/PELVIS BOUNDARY MUST BE AT 53.7037% OF CROWN-TO-SOLES BODY HEIGHT,
MEASURED DOWNWARD FROM THE STRUCTURAL CROWN.

EQUIVALENT:
CROTCH-TO-SOLES MUST BE 46.2963% OF CROWN-TO-SOLES BODY HEIGHT.
```

The boundary is not an aesthetic suggestion and not a qualitative “high pelvis” direction. It is a measurable structural anchor inherited from the approved Body Guide.

## Test 6 active implementation files

```text
tools/yura-master-benchmark/config_test6.json
tools/yura-master-benchmark/codex_instruction_test6.md
tools/yura-master-benchmark/run_test6_once.py
```

The original Test 5 runner logic remains the inherited implementation base. Test 6 overrides only the Test-6-specific config/instruction/reference roles/invariants and exact Working Master hash check.

## Test 6 image-reference change

Test 5 used the Body Guide as the edit base and the Face Reference as the second Image API input.

Test 6 changes only the reference arrangement required to edit the author-selected Working Master directly:

```text
IMAGE 1
visuals/yura/identity/master/YURA_VISUAL_MASTER.png
= AUTHOR-SELECTED WORKING MASTER / VISUAL EDIT BASE

IMAGE 2
visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
= BODY GEOMETRY CORRECTION AUTHORITY
```

`YURA_FACE_REFERENCE.png` is intentionally excluded from the Test 6 Authority order and from Image API pixel inputs. `FACE_REFERENCE_RULES.md` remains active as Face-preservation text rules. The existing Working Master face is preserved rather than regenerated from the Face Reference image.

## Frozen non-target variables

Test 6 must preserve, rather than redesign:

```text
Sample 9 Face Identity
Sample 9 overall build
Sample 9 chest appearance
Sample 9 thigh feminine volume/curve
Sample 9 knee position as judged by the author
Sample 9 overall leg visual balance
Sample 9 skin appearance
Sample 9 general hair identity
Sample 9 current hair length
front-view full-body presentation
white background
7.2-head target and current 7.1–7.3 gate
current Body Guide
current official Body QA definitions
current Composition deferral
```

Do not alter these to make the boundary easier to satisfy.

## Hair-length isolation rule

The author has approved a later micro-refinement:

```text
hair slightly longer than Sample 9
```

That change is **not part of Test 6**.

For Test 6:

```text
preserve Sample 9 hair length as closely as practical
do not intentionally lengthen or shorten hair
```

Reason: combining hair editing with the boundary intervention would break the one-hypothesis discipline.

Hair-length refinement occurs only after the Body Geometry decision.

## Geometry behavior required

Move the structural boundary toward the Guide position by redistributing the torso/pelvis transition, not by arbitrary leg stretching.

Do not solve the target by:

```text
changing head size
lengthening only thighs
lengthening only shins
moving the soles
moving the knee merely to manipulate the ratio
raising the waistline as a fake boundary
using shorts/garment edges as the landmark
nonuniform body scaling
Composition warp
```

Crown, chin, knee, and soles are measurement controls. They may show ordinary generation variance, but the prompt must not intentionally direct them as the solution.

## Measurement for every paid Test 6 sample

For every generated RAW, record the full structural-uncertainty set before deciding whether another Test 6 replication is justified:

```text
structural_crown_min
structural_crown_best
structural_crown_max
chin
crotch_pelvis_boundary_min
crotch_pelvis_boundary_best
crotch_pelvis_boundary_max
knee
soles
```

Then run the current official 3×3 crown×boundary uncertainty evaluation.

Report at minimum:

```text
head interval / best
normalized boundary interval / best
inseam interval / best
chin→boundary interval / best
overall_build_not_too_thin
chest_front_volume_matches_author_intent
author knee-position judgment
author leg-balance judgment
author thigh-curve judgment
author hair judgment
author overall-balance judgment
```

Each paid RAW remains one measurable result. Test 6 as a whole is a bounded replication series of the same frozen hypothesis.

## Decision rules

### EXACT SUPPORT

H6 is exactly supported only if:

```text
full uncertainty inseam interval is inside 46.0–46.5%
AND
full uncertainty chin→boundary interval is inside 2.7985–2.942 heads
AND
the boundary corresponds to the approved Guide-relative location
AND
non-target author visual judgments do not materially regress
```

Head is evaluated by the unchanged official gate. Final Body PASS still requires the full existing official QA contract.

### DIRECTIONAL SUPPORT

Use this label if:

```text
boundary moves materially toward 53.7037%
and both inseam and chin→boundary move toward their gates
but one or more required intervals remain outside PASS
```

A directional improvement is evidence, not a PASS. The same frozen Test 6 condition may be replicated, up to the five-sample maximum, to determine whether the movement is reproducible.

### NO SUPPORT / NO MATERIAL CHANGE

Use this label if the boundary remains in approximately the prior failure region and the derived metrics do not materially improve.

One such sample is evidence but may be insufficient because the previous study demonstrated end-to-end generation variance. Additional identical-condition replications are allowed up to the five-sample maximum when needed to decide whether the intervention has any reproducible effect.

### OVERSHOOT

Use this label if the boundary is pushed beyond the approved Guide region and the inseam becomes too short relative to the current gate.

### REGRESSION

Use this label if the boundary improves but the intervention materially damages the author-selected Master visual baseline or causes a non-target structural failure.

## Bounded paid-run discipline — 1 to 5 samples

Test 6 is not an open-ended reroll search.

```text
minimum paid Test 6 samples = 1
maximum paid Test 6 samples = 5

same Git
same Test 6 config
same Test 6 compiler instruction
same Working Master binary
same Body Guide
same hypothesis
```

Rules:

1. Generate Sample 1 only after free preflight and compiled-prompt/invariant review.
2. Measure and author-review Sample 1 before deciding whether Sample 2 is needed.
3. If EXACT SUPPORT and the full official Body QA passes without material visual regression, the series may stop early.
4. If DIRECTIONAL SUPPORT is observed, identical-condition replication may continue up to Sample 5 to test reproducibility.
5. If NO SUPPORT / NO MATERIAL CHANGE is observed, identical-condition replication may continue only as needed to rule out ordinary variance; never exceed five total samples.
6. If the implementation causes major visual collapse, stop and use the frozen Test 5 breakpoint / Sample 9 Working Master as the recovery point.
7. Do not change the prompt/config/Authority between Test 6 samples. Any such change starts a new test and cannot be pooled into this series.
8. Do not select a lucky image while ignoring the series result.

## Author fallback decision if Test 6 does not materially improve geometry

If the bounded 1–5 Test 6 series shows no reproducible material improvement over Sample 9, the author has decided that Sample 9 will be promoted as the formal YURA full-body Master despite the already-recorded numeric Body-Guide discrepancy.

In that case:

```text
Sample 9 visual decision = authoritative final Master choice
known boundary/inseam/torso numeric discrepancy = retained in audit history
numeric discrepancy must not be falsely rewritten as a measured PASS
further Body-geometry rerolling = stop
```

The next phase then becomes detailed Master-derived part specification and reproduction verification, not further pelvis/boundary optimization.

## Composition

Composition remains blocked during Test 6.

Test 6 outputs are QA-pending geometry-refinement candidates only.

No deterministic Composition step may run unless the current official Body Geometry gate permits it, or the author later explicitly promotes Sample 9 through the documented fallback decision after Test 6 concludes.

## What happens after Test 6

### If Test 6 produces a materially better accepted corrected Master

Use the accepted corrected candidate as the new full-body Master baseline, then perform the separately approved slight hair-length micro-refinement only if still required.

### If Test 6 does not materially change/improve the boundary within the bounded series

Promote Sample 9 as the formal full-body Master by explicit author decision while preserving the numeric discrepancy in audit history.

Then proceed in this fixed order:

```text
1. derive detailed per-part visual specifications from the formal full-body Master
2. create/refine the Production Visual MD from the Master image without inventing absent traits
3. verify GPT-based reproduction from formal full-body Master + Production Visual MD
4. after whole-body reproduction is demonstrated, isolate the Face ear-enlargement issue
5. generate a corrected Face Reference designed to prevent ear inflation while preserving Face Identity
6. perform approximately 10 fixed-condition Face-only generations and evaluate ear/Face stability
7. if Face-only stability passes, promote the corrected Face Master/Reference
8. re-verify full-body generation using the new Face Master + formal full-body Master + Production Visual MD
9. archive/retire the Master-generation benchmark materials from the normal YURA generation route without deleting them
```

The final archive step must prevent old benchmark/Test/Authority materials from being accidentally auto-loaded by normal Production generation while preserving them for rollback and audit.
