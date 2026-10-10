# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / WORKING MASTER SELECTED / PELVIS-BOUNDARY REFINEMENT NEXT / COMPOSITION DEFERRED**

This file is operational documentation only. It is not a YURA visual Authority.

## Current objective

Finish the YURA Master while minimizing generation drift and preserving explicit author intent.

## Current selected visual baseline

Canonical target path:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Source: fixed-condition variance-study Sample 9.

The selection is fixed. The exact RAW binary must match the SHA-256 below; no derivative may be substituted.

RAW SHA-256:

```text
b8048a7b5997783df20b0e36b59e9e3d319cd32f10acc0034fb8d376c33e1967
```

Author decision: Sample 9 has the best overall balance of the ten-run series and is the current working Master visual baseline.

Numeric Body QA is still not PASS. Do not conflate visual selection with numeric gate status.

## Completed variance study

Result:

`tools/yura-master-benchmark/VARIANCE_STUDY_RESULT_20261011.md`

Summary:

```text
10 fixed-condition paid runs
10 RAW successes
0 Official Body PASS
4 visual all-PASS
0 Full PASS

head best mean       ≈ 7.036
boundary best mean   ≈ 48.628%
Guide boundary        53.7037%
inseam best mean     ≈ 51.372%
target                 46.0–46.5%
chin→boundary mean   ≈ 2.421 heads
target                 2.7985–2.942 heads
```

The systematic failure is the crotch/pelvis boundary being generated too high.

## Active next test

`tools/yura-master-benchmark/TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`

One hypothesis only:

```text
explicit normalized structural boundary anchor
-> move crotch/pelvis boundary toward 53.7037%
-> preserve selected Master appearance
```

No other appearance redesign is part of Test 6.

## Hair

The author approved a later slight hair-length increase relative to the selected working Master.

It is recorded in:

`visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md`

It is intentionally excluded from Test 6 to avoid a second causal variable.

## Official Body QA remains unchanged

```text
head target = 7.2
acceptable = 7.1–7.3
inseam = 46.0–46.5%
>=47.0% hard fail
chin→boundary = 2.7985–2.942 heads
structural crown min/best/max
boundary min/best/max
full 3×3 uncertainty
REVIEW_OVERLAP blocks Composition
```

## Execution state

```text
Test 5 variance study     = COMPLETE
working Master selection = COMPLETE
working Master binary    = PENDING EXACT COPY
Test 6 preregistration   = COMPLETE
Test 6 implementation    = NOT YET
Test 6 free preflight    = NOT YET
Test 6 paid RAW          = NOT YET
Composition              = BLOCKED
Production switch        = NOT YET
```

## Next action

Implement Test 6 exactly from the preregistered spec, review the diff, run free preflight, then one paid RAW.

Do not reroll.
Do not combine hair refinement with Test 6.
Do not change the Body QA numbers unless explicitly ordered.
