# YURA Master Benchmark — Current Handoff

Status: **ACTIVE / TEST 6 IMPLEMENTED / FREE PREFLIGHT NEXT / COMPOSITION BLOCKED**

This file is operational documentation only. It is not a YURA visual Authority.

## Scope lock

Current scope is YURA Master image completion only.

Do not begin uniforms, outfit Masters, pose packs, other characters, SHIORI/MIO work, story work, or downstream Production work unless the author explicitly redirects the project.

Do not alter or touch:

`manuscript/episode-001/EP001_DRAFT.txt`

Do not use `git reset --hard` and do not force-push.

## Test 5 completed and frozen as breakpoint

The completed fixed-condition variance study used:

```text
generation baseline commit
cc38457dc39e509adcd44da10c75f354c49c8844

sealed_authority_bundle_sha256
11f3626d7eb140cec8f344fa5e78ac8258861d6a45ef648922bd42dc037f4b28
```

Full result:

`tools/yura-master-benchmark/VARIANCE_STUDY_RESULT_20261011.md`

The exact Test 5 compiler MD is frozen outside the active Test 6 route at:

`tools/yura-master-benchmark/archive/test5_breakpoint_20261011/codex_instruction_test5.md`

Frozen blob SHA:

```text
ced76faf3b382052c2928dd2ae0795c739ce2222
```

The former active `tools/yura-master-benchmark/codex_instruction.md` was removed after the exact archive copy was verified. This prevents accidental Test 5 compiler use while preserving a rollback breakpoint.

## Working Master selected

The author selected variance-study **Sample 9** as the current visual Master baseline.

Canonical path:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Working Master binary commit:

```text
c20ffc31fe5ccd16323ce36b129af93014d269ee
```

Canonical original local RAW SHA-256:

```text
81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

Sample 9 is the author's best-balanced image of the ten-run series and is the recovery baseline if Test 6 causes major visual collapse.

Do not falsely relabel its known numeric Body Geometry mismatch as a measured PASS.

## Current unresolved geometry

```text
Head best mean              ≈ 7.036
Boundary best mean          ≈ 48.628%
Guide boundary               53.7037%
Inseam best mean            ≈ 51.372%
Target                        46.0–46.5%
Chin→boundary mean          ≈ 2.421 heads
Target                        2.7985–2.942 heads
```

Dominant remaining failure:

```text
crotch/pelvis boundary too high
-> torso/chin→boundary too short
-> inseam too long
```

Do not lower the 7.2 target or recalibrate the official Body gates unless the author explicitly orders it.

## Test 6 active implementation

Detailed preregistration:

`tools/yura-master-benchmark/TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`

Active Test 6 files:

```text
tools/yura-master-benchmark/config_test6.json
tools/yura-master-benchmark/codex_instruction_test6.md
tools/yura-master-benchmark/run_test6_once.py
```

Test 6 is derived from Test 5 and changes only the causal pieces required to edit the Working Master directly and enforce the normalized structural boundary.

Image API reference order:

```text
IMAGE 1 = YURA_VISUAL_MASTER.png
          AUTHOR-SELECTED WORKING MASTER / VISUAL EDIT BASE

IMAGE 2 = YURA_BODY_GEOMETRY_GUIDE.png
          BODY GEOMETRY CORRECTION AUTHORITY
```

The Face Reference remains sealed Authority metadata but is not supplied as Image API pixel input for Test 6. Preserve the Working Master's existing Face Identity.

Target anchor:

```text
boundary from structural crown = 53.7037% of crown→soles
equivalent crotch→soles        = 46.2963%
boundary definition            = central medial-thigh bifurcation / upper-lower body boundary
garment-line authority         = DENIED
```

Only causal intervention:

```text
explicit normalized pelvis/boundary lock
```

Hair-length increase is NOT part of Test 6.

## Test 6 paid-series rule

Test 6 is a bounded replication series:

```text
minimum samples = 1
maximum samples = 5
```

All samples must use the same Git/config/compiler instruction/Working Master/Body Guide. Each sample is measured and author-reviewed before another is justified.

Stop early on exact accepted support. Continue identical-condition replications only to determine whether directional/no-change behavior is reproducible. Never exceed five samples and never reroll merely to select a lucky output.

If the 1–5 series shows no reproducible material improvement, the author has decided to promote Sample 9 as the formal YURA full-body Master while retaining the numeric discrepancy as audit history rather than falsely converting it into a measured PASS.

## Approved later hair refinement

The author wants the Sample 9 hair slightly longer:

```text
same hair identity
slightly longer only
reach the waist area more clearly
not dramatically longer
not substantially below the waist
```

This is deferred until the Test 6 body decision is complete.

## Fixed downstream sequence after Test 6

After Test 6 concludes, proceed in this exact order:

```text
1. choose/promote the accepted corrected full-body candidate, OR promote Sample 9 if Test 6 has no material effect
2. derive detailed per-part specifications from the formal full-body Master
3. create/refine the Production Visual MD from the Master image without inventing absent traits
4. test GPT reproduction using formal full-body Master + Production Visual MD
5. only after whole-body reproduction is demonstrated, isolate the Face ear-enlargement problem
6. generate a corrected Face Reference/Master designed to prevent ear inflation while preserving Face Identity
7. perform approximately 10 fixed-condition Face-only generations
8. if Face-only stability passes, promote the corrected Face Master/Reference
9. re-test full-body generation using new Face Master + formal full-body Master + Production Visual MD
10. archive benchmark/Test/Master-generation materials away from normal YURA Production generation without deleting them
```

The final archive must prevent old benchmark/test materials from being auto-loaded by normal Production generation while preserving rollback/audit access.

## Next action

No paid call yet.

Synchronize current `main`, then run:

```text
python tools/yura-master-benchmark/run_test6_once.py --preflight-only
```

After `PREFLIGHT_OK`, inspect the generated `compiled_prompt.txt` and `prompt_invariant_check.json` before any paid Test 6 RAW.

## Mandatory preservation

Current official Body QA remains unchanged:

```text
head target 7.2
acceptable head 7.1–7.3
inseam 46.0–46.5%
>=47.0% hard fail
chin→boundary 2.7985–2.942 heads
structural crown uncertainty
crotch/pelvis boundary uncertainty
3×3 uncertainty combination
REVIEW_OVERLAP blocks Composition
```

Current author visual gates remain relevant:

```text
overall build
chest
hair
thigh feminine volume/curve
knee position
overall leg vertical balance
skin
```

Composition remains blocked during Test 6. Do not use Composition to repair anatomy.
