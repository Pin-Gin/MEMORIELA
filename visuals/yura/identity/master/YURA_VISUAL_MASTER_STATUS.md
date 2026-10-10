# YURA VISUAL MASTER STATUS

Status: **AUTHOR-SELECTED WORKING MASTER / GEOMETRY-CALIBRATION PENDING**

## Current working Master selection

Canonical target path:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Required binary state:

```text
asset_source = Variance Study Sample 9 original RAW
asset_sha256 = b8048a7b5997783df20b0e36b59e9e3d319cd32f10acc0034fb8d376c33e1967
binary_commit = PENDING UNTIL THE EXACT RAW IS PRESENT AT THE TARGET PATH
```

Do not substitute another sample, a grid image, a screenshot, or a recompressed derivative.

Source:

```text
Variance Study Sample 9 / 10
run_dir = C:\Dev\MEMORIELA\tools\yura-master-benchmark\runs\run_20261010T201652Z
git_commit at generation = cc38457dc39e509adcd44da10c75f354c49c8844
sealed_authority_bundle_sha256 = 11f3626d7eb140cec8f344fa5e78ac8258861d6a45ef648922bd42dc037f4b28
compiled_prompt_sha256 = e87cb703d9cfd0e0be30231d764396193993577f74680d40cec96353796b22b8
RAW SHA256 = b8048a7b5997783df20b0e36b59e9e3d319cd32f10acc0034fb8d376c33e1967
```

## Author decision

Sample 9 is the author-selected visual baseline and is to be treated as the current YURA working Master for subsequent Master refinement.

Author visual review:

```text
hair length                  PASS
skin                         PASS
chest                        PASS
knee position                PASS
thigh feminine volume/curve  PASS
overall leg vertical balance PASS
overall build                PASS
overall balance              BEST OF THE 10-RUN SERIES
```

## Important QA distinction

This selection is an explicit **visual Master decision**, not a claim that the existing numeric Body Geometry gate passed.

Recorded study measurement for Sample 9:

```text
Head best              ≈ 7.214
Boundary best          ≈ 49.17%
Inseam best            ≈ 50.83%
Chin→boundary best     ≈ 2.547 heads
```

Current Body Guide / QA targets remain:

```text
Head                    7.1–7.3
Boundary from crown     53.7037% guide position
Inseam                  46.0–46.5%
Chin→boundary           2.7985–2.942 heads
```

Therefore:

```text
WORKING MASTER VISUAL SELECTION = YES
NUMERIC BODY QA PASS            = NO
FINAL COMPOSITION               = BLOCKED
PRODUCTION AUTHORITY SWITCH     = NOT YET
```

Do not erase or relabel the numeric failure merely because the image is visually preferred.

## Approved pending hair refinement

The current Master hair is accepted, but the author wants **slightly more length**.

Frozen intent:

```text
preserve the Sample 9 silver-white straight super-long hair identity
increase length only slightly
make the hair reach the waist area more clearly
do not make it dramatically longer
do not extend substantially below the waist
```

This refinement is deliberately **not combined with Test 6**, because Test 6 is restricted to one Body Geometry hypothesis.

After the pelvis/boundary problem is resolved, hair length may be handled as a separate micro-refinement.

## Current geometry priority

The next active experiment is limited to:

> Fixing the crotch/pelvis boundary to the approved Body Guide relative position while preserving the selected Master visual balance.

Detailed preregistration:

`tools/yura-master-benchmark/TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`
