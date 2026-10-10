# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / TEST 6 IMPLEMENTED / FREE PREFLIGHT NEXT / COMPOSITION DEFERRED**

This file is operational documentation only. It is not a YURA visual Authority.

## Current objective

Finish the YURA Master while minimizing generation drift and preserving explicit author intent.

## Current selected visual baseline

Canonical target path:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Source: fixed-condition variance-study Sample 9.

Canonical original local RAW SHA-256:

```text
81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

Binary commit:

```text
c20ffc31fe5ccd16323ce36b129af93014d269ee
```

Author decision: Sample 9 has the best overall balance of the ten-run series and is the current Working Master / Test 6 recovery baseline.

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

Systematic failure:

```text
crotch/pelvis boundary too high
-> torso/chin→boundary too short
-> inseam too long
```

## Test 5 breakpoint state

The exact Test 5 compiler instruction is archived at:

`tools/yura-master-benchmark/archive/test5_breakpoint_20261011/codex_instruction_test5.md`

Blob SHA:

```text
ced76faf3b382052c2928dd2ae0795c739ce2222
```

The active-root `codex_instruction.md` from Test 5 has been retired so Test 6 cannot silently execute the old compiler path. The archive is rollback/audit only and is not an active Test 6 Authority.

## Active Test 6 implementation

Specification:

`tools/yura-master-benchmark/TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`

Active Test 6 files:

```text
tools/yura-master-benchmark/config_test6.json
tools/yura-master-benchmark/codex_instruction_test6.md
tools/yura-master-benchmark/run_test6_once.py
```

Test 6 is derived from Test 5. Unchanged QA/Composition/safety behavior is inherited through the existing runner; Test 6 overrides only the new config, compiler instruction, Working Master role/reference order, exact Master SHA check, and boundary-specific invariants.

Image reference order:

```text
1. YURA_VISUAL_MASTER.png         = Working Master / edit base
2. YURA_BODY_GEOMETRY_GUIDE.png   = Body Geometry correction Authority
```

The Face Reference is not an Image API pixel input in Test 6. The Working Master's existing Face Identity is preserved.

Single causal intervention:

```text
boundary from structural crown = 53.7037% of crown→soles
crotch→soles                   = 46.2963%
boundary                       = central medial-thigh bifurcation / upper-lower body structural boundary
garment-line authority         = DENIED
```

Hair length is frozen during Test 6.

## Test 6 bounded replication

```text
minimum paid samples = 1
maximum paid samples = 5
```

Every sample must use identical Git/config/compiler/Working-Master/Body-Guide conditions. Measure and author-review each RAW before another is justified.

Stop early on exact accepted support. Continue only to establish whether directional/no-change behavior is reproducible. No lucky reroll selection.

If the bounded series shows no reproducible material improvement, Sample 9 becomes the formal YURA full-body Master by explicit author decision, while the known numeric Body discrepancy remains preserved in audit history and is not relabeled as measured PASS.

## Hair

The author approved a later slight hair-length increase relative to Sample 9:

```text
same hair identity
slightly longer only
reach the waist area more clearly
not dramatically longer
not substantially below the waist
```

It remains excluded from Test 6.

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

## Fixed downstream order

After Test 6:

```text
formal full-body Master selection/promotion
-> detailed per-part Master-derived specifications
-> Production Visual MD
-> GPT reproduction test from full-body Master + Production Visual MD
-> isolate Face ear-enlargement issue
-> corrected Face Reference/Master generation
-> approximately 10 fixed-condition Face-only stability generations
-> Face promotion if PASS
-> full-body reproduction test using new Face Master + full-body Master + Production Visual MD
-> archive benchmark/Test/Master-generation materials away from normal Production generation without deleting them
```

## Execution state

```text
Test 5 variance study          = COMPLETE
Test 5 compiler breakpoint     = ARCHIVED / VERIFIED
Working Master selection      = COMPLETE
Working Master binary         = PRESENT / SHA VERIFIED
Test 6 preregistration        = COMPLETE
Test 6 implementation files   = COMPLETE
Test 6 free preflight         = NEXT
Test 6 paid series            = NOT YET / 1–5 MAX
Composition                   = BLOCKED DURING TEST 6
Production switch             = NOT YET
```

## Next action

Synchronize current `main`, then run:

```text
python tools/yura-master-benchmark/run_test6_once.py --preflight-only
```

Inspect `compiled_prompt.txt` and `prompt_invariant_check.json` before authorizing any paid Test 6 RAW.

Do not combine hair refinement with Test 6.
Do not change Body QA numbers unless explicitly ordered.
