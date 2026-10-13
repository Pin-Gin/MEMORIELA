# YURA Master / Production Pipeline State

Status: **FORMAL SAMPLE 9 MASTER / FULL-BODY PIXEL V1 COMPLETE / AMBIGUITY PROTOCOL VALIDATED / DIAGNOSTIC REFERENCE PREFLIGHT NEXT**

This file records operational state. It is not Visual Authority.

## Fixed baseline

```text
Formal full-body Master = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
Master SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
full-body pixel measurement V1 = COMPLETE
body proposed bands = POPULATED / NOT FULLY FROZEN

Face Reference = visuals/yura/identity/face/YURA_FACE_REFERENCE.png
Face Git blob SHA = 4c96c4ec42f996807248be1aff60ec8a090fd570
Face SHA256 = 3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
Face ZIP ↔ current main = PASS
Face PNG integrity = PASS
```

The current Face Reference has a known author-identified ear-longation defect. Its current ear dimensions are diagnostic evidence, not automatically the corrected target.

## Governing ambiguity rule

`visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md`

Validation against current Face/BODY separation, active ear rule, Hair SUPER-LONG override, and Production measurement governance:

```text
PROTOCOL VALIDATION = PASS
```

The only prior sequencing conflict was the older instruction to proceed directly to Face measurement. The newer ambiguity protocol intentionally inserts diagnostic multi-view validation first.

## Classification

Existing source classes remain:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

Additional ambiguity classes:

```text
MEASURED_VISIBLE_FACT
MEASURED_OCCLUSION_FACT
ESTIMATED_HIDDEN_GEOMETRY
AUTHOR_INTENT
VIEW_SPECIFIC_RULE
NON_COMPENSATION_RULE
```

For occluded parts, keep ACTUAL/STRUCTURAL GEOMETRY, VISIBLE GEOMETRY, OCCLUSION/LAYER ORDER, and VIEW separate. Unknown hidden structure remains unknown.

## Naturalness gate

Low visibility alone is not a defect.

Do not expose hidden structure by enlarging, elongating, widening, moving outward, rotating toward camera, clearing natural occlusion, forcing bilateral symmetry, or unnaturally fanning hair.

Acceptance requires:

```text
STRUCTURAL CONSISTENCY
IDENTITY CONSISTENCY
VISUAL NATURALNESS
```

## Diagnostic five-view route

Generation spec:

`tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md`

Dedicated one-view runner:

`tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py`

Default set:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

One invocation produces one view. A five-panel single generation is not used.

The runner uses only these image references:

```text
1. formal YURA_VISUAL_MASTER.png
2. active YURA_FACE_REFERENCE.png
```

It explicitly denies the historic Body Geometry Guide, old Masters, Test 5/6 outputs, past generated candidates, story/manuscript/characters appearance, Memory appearance, and Git-history visual fallbacks.

The runner reuses only the already-working Image API transport settings from legacy `config.json`; it does not import the Test 5 authority order, Body Guide, historic pelvis/inseam gates, Body QA, or composition gates.

## Diagnostic status rule

Before ear and rear-hair correction, every generated view must remain:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

Route/view-behavior PASS does not mean visual Authority PASS.

## Ear state

Current working rule:

```text
ear actual height target = 20–22% face vertical dimension
HARD MAX = 23%
ear visibility lower priority than natural size / placement
no visibility compensation
```

Required decomposition after diagnostic route PASS:

```text
EAR ACTUAL GEOMETRY
EAR VISIBLE GEOMETRY
HAIR OCCLUSION
```

## Hair state

Current AUTHOR_OVERRIDE:

```text
SUPER-LONG mandatory
must clearly reach waist area
ordinary-long / mid-back = FAIL
modestly longer than Sample 9
not substantially below waist
```

Rear-hair / back-view structure remains unresolved and follows the ear checkpoint.

## Current execution state

```text
Formal Sample 9 Master                    = COMPLETE
Full-body pixel measurement V1            = COMPLETE
Visual Ambiguity Protocol                 = ACTIVE / AUTHOR APPROVED
Protocol-vs-authority validation           = PASS
Five-view generation spec                 = COMPLETE
Dedicated one-view runner                 = COMPLETE / GIT-LEVEL REVIEWED
Free preflight                            = NEXT
Five-view diagnostic generation           = NOT YET
Route / view-behavior PASS                 = NOT YET
Ear correction                             = AFTER PASS
Rear-hair / back-view correction           = AFTER EAR
Corrected multi-view promotion             = NOT YET
Paid Face-only Pilot 1                     = NOT YET
Formal Face Master                         = NOT YET
Production Visual MD                       = NOT YET
```

## Exact next action

Run free preflight with **zero paid model calls**, one view at a time, starting with FRONT:

```text
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view FRONT --preflight-only
```

Verify `preflight.json`, `compiled_prompt.txt`, exact source SHA-256 values, current-main equality, denied sources, and prompt invariants.

If FRONT preflight passes, repeat preflight for FRONT_3Q / SIDE / REAR_3Q / BACK. Do not start paid diagnostic generation until the free preflight set is reviewed.
