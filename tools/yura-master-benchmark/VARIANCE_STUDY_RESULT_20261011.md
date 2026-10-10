# YURA Test 5 fixed-condition variance study result — 2026-10-11

Status: **COMPLETED / 10 OF 10 / AUTHOR DECISION RECORDED**

This document is an audit/result record. It is not a replacement for Face Identity, Body Geometry, or Composition Authority.

## Study condition

All ten paid runs used the same committed pipeline baseline:

```text
git_commit = cc38457dc39e509adcd44da10c75f354c49c8844
sealed_authority_bundle_sha256 = 11f3626d7eb140cec8f344fa5e78ac8258861d6a45ef648922bd42dc037f4b28
```

The condition included the approved non-sexual-intent clarification added after the earlier output-moderation block.

The study objective was fixed in advance:

```text
Run exactly 10 attempts.
Do not stop when a PASS appears.
Do not change Git / Authority / prompt-condition between samples.
Count how many samples satisfy the relevant criteria.
Observe end-to-end variance, including Codex prompt-compilation variance and Image generation variance.
```

All 10 attempts returned a RAW image. No moderation block occurred in this 10-run series.

## Measurement status

The numeric values below are the manual measurements recorded during the study from the proportional 1152×2048 uploaded/display copies.

They are **study measurements**, not a substitute for a formal `body_geometry_qa.py` report made against each original local RAW.

Current official numeric targets remain unchanged:

```text
head target = 7.2
head acceptable = 7.1–7.3

inseam proxy target = 46.0–46.5%
>= 47.0% = hard fail

chin→crotch/pelvis-boundary = 2.7985–2.942 heads

Body Guide normalized crotch/pelvis boundary position
= 53.7037% downward from structural crown within crown→soles height
```

## Ten-run table

| Sample | compiled_prompt_sha256 | RAW SHA256 | Head best | Boundary best | Inseam best | Chin→boundary best | Author visual result |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | `b4934512b3440433abb9e8fb25847fc756f569f49ec70d884d87d25f02246537` | `f82cf810333bf35ed09e11db6fd898e0c538509584f740fb1d5ce396459bef47` | 7.048 | 48.62% | 51.38% | 2.427 | mixed |
| 2 | `673b212b6ed5405b9223b14ace181b2ee5916e006833f59cdb504e6a218051fc` | `591016d4c2eccb82268fdaa4f3a52a491ab595e35fcfb2d7bad31ee1cccbe325` | 7.087 | 46.57% | 53.43% | 2.300 | mixed |
| 3 | `0fedd78e76f8a537a3ef9a39800b39b9e759a91d9b7ddd3fc735c2bc428d246b` | `660e5c006e05e81ca7c4941a0d758812c3fc42bb54f231575d5a73d0c5a53e2a` | 6.974 | 48.92% | 51.08% | 2.412 | mixed |
| 4 | `1e2c8773ee0464189ec9afaa84cc601b65a35f3fc57a9605e24cc5238a74223a` | `b81af0c784fe3e198606307e77f30654fc47fe67fa5885af527a08c89f0048bf` | 7.196 | 48.29% | 51.71% | 2.475 | mixed; chest PASS |
| 5 | `b8f246592e647768904819b220bcd3df45587d02bd938f1e5908562c6feb84f0` | `3807b9dc2b5f792d327a3393c6a63b6f0d6bafa8cd9cd495caac9a2baf702f39` | 7.026 | 49.47% | 50.53% | 2.475 | **all tracked visual items PASS** |
| 6 | `34afcf38d8c785f9c2f07782aaf90a030b5e47a9ca90d8ee75ce22e566c9ded7` | `f32a23888b4faa716f91e57fb1d23d4bc46d23b2f95534f70860f112807c7590` | 6.721 | 49.25% | 50.75% | 2.310 | PASS / PASS寄り mix |
| 7 | `b5609edc265ae65194eaf0156c526dbe6085310353df67d3a9fdc1e7140a452b` | `5c6b9194c274af37bf5aa44b69f4965c65254c724afbf0547ad61f301336156b` | 6.945 | 48.97% | 51.03% | 2.401 | **all tracked visual items PASS** |
| 8 | `aae3da4f9ffc73432fd877d61771397802d0d7fce47f984151280ea0dd17030d` | `882169199b7f6e5a2abebb1d74ee083e555dd01557ccdde2c7bd88c0c451a7fc` | 7.152 | 47.32% | 52.68% | 2.384 | **all tracked visual items PASS** |
| 9 | `e87cb703d9cfd0e0be30231d764396193993577f74680d40cec96353796b22b8` | `b8048a7b5997783df20b0e36b59e9e3d319cd32f10acc0034fb8d376c33e1967` | 7.214 | 49.17% | 50.83% | 2.547 | **all tracked visual items PASS; author judged best overall balance** |
| 10 | `f957537ef550ed8c2bc8035ef5730f5813b21edaff3187ac3488e0fb35319801` | `d3ccc02f3a1d6e50c9905e0b9ad63b3aee795e8e29559e5c76ed97a584052090` | ≈7.00 | ≈49.7% | ≈50.3% | ≈2.48 | chest FAIL; thigh curve FAIL |

## Aggregate

Using the recorded best-value measurements:

```text
RAW success                  10 / 10
Official Body PASS            0 / 10
Visual all-PASS               4 / 10
Full PASS                     0 / 10

Head best mean              ≈ 7.036
Head best median            ≈ 7.037
Head best min                 6.721
Head best max                 7.214

Boundary best mean          ≈ 48.628%
Body Guide boundary           53.7037%

Inseam best mean            ≈ 51.372%
Target                        46.0–46.5%

Chin→boundary best mean     ≈ 2.421 heads
Target                        2.7985–2.942 heads
```

One run, Sample 4, reached the study's manual `Head PASS_ROBUST` assessment. No sample passed the full official Body Geometry gate because the boundary-derived inseam/torso metrics remained outside target.

All ten `compiled_prompt_sha256` values were different. Therefore this study measures **end-to-end pipeline variance**:

```text
Codex prompt-compilation variance
+
Image generation variance
```

It is not a pure Image-model RNG-only experiment.

## Strongest conclusion

The repeated miss is directional and systematic, not merely an occasional random outlier.

Across all ten samples, the generated crotch/pelvis boundary remained materially above the Body Guide position:

```text
observed study center ≈ 48.63%
Body Guide             = 53.7037%
gap                    ≈ 5.08 percentage points
```

This explains the paired failure pattern:

```text
boundary too high
-> chin→boundary span too short
-> crotch→soles span too large
-> inseam proxy too high
```

The next experiment must therefore isolate **boundary placement itself** rather than changing Face Identity, chest, thigh shape, Composition, or the 7.2 target.

## Author visual decision

Sample 9 is selected by the author as the **working YURA Master visual baseline**.

Author judgment for Sample 9:

```text
hair length                 PASS
skin                        PASS
chest                       PASS
knee position               PASS
thigh feminine volume/curve PASS
overall leg vertical balance PASS
overall build               PASS
overall balance             BEST OF THE 10-RUN SERIES
```

Sample 9 original RAW SHA-256:

```text
b8048a7b5997783df20b0e36b59e9e3d319cd32f10acc0034fb8d376c33e1967
```

Canonical target path:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

The exact selected RAW must be copied to that path unchanged, with SHA-256
`b8048a7b5997783df20b0e36b59e9e3d319cd32f10acc0034fb8d376c33e1967`.
The author selection is canonical even if the binary asset commit is performed separately.

This author selection does **not** falsify the numeric QA result. The selected working Master still carries unresolved boundary/inseam/torso calibration debt. Production Authority switch and final Composition remain blocked until that debt is resolved or explicitly superseded by the author.

## Hair refinement decision

The author wants the selected Sample 9 hair **slightly longer**, while retaining the same overall hair identity.

Frozen refinement intent:

```text
current Sample 9 hair identity = preserve
hair length = slightly increase
direction = reach the waist area more clearly
do not make it dramatically longer
do not extend substantially below the waist
```

To preserve the one-paid-RAW / one-hypothesis discipline, this hair-length micro-refinement is **approved and recorded but deferred from the next Body Geometry experiment**.

The next paid geometry test must not combine hair-length editing with the pelvis/boundary intervention.

## Next active hypothesis

See:

`tools/yura-master-benchmark/TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`

No Composition run is authorized before the next Body Geometry decision.
