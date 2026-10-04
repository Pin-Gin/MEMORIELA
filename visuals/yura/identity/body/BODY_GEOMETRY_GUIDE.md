# YURA BODY GEOMETRY GUIDE — CANDIDATE SPEC

Status: **CANDIDATE / NOT AUTHORITY / AUTHOR REVIEW REQUIRED**

Candidate image:
`YURA_BODY_GEOMETRY_GUIDE_CANDIDATE.png`

## Purpose

This candidate makes the upper/lower-body boundary explicit and encodes the author-approved
YURA long-leg balance without changing the total **7.2-head** target.

It is intended to replace the active guide **only after explicit author approval**.

## Fixed geometry

- canvas: **1200 × 1600 px**
- crown: **y = 160**
- chin: **y = 340**
- one head: **180 px**
- soles: **y = 1456**
- total: **7.2 heads**

## Explicit upper/lower-body boundary

The standing full-body boundary is:

**CROTCH / PELVIS LINE = UPPER / LOWER BODY BOUNDARY**

Candidate boundary:
- crotch / pelvis-line proxy: **y = 856**
- crown→crotch: **3.8667 heads**
- chin→crotch: **2.8667 heads**

This boundary must be visible in the guide image and named in the text Authority.

## Author-approved YURA inseam proxy

Definition:

```text
inseam_proxy_ratio = (soles_y - crotch_y) / (soles_y - crown_y)
```

Candidate value:

- **46.2963%**

Required YURA QA target:

- **PASS = 46.0–46.5%**
- **46.5% < ratio < 47.0% = FAIL**
- **47.0% or more = HARD FAIL / too model-like**

This is a YURA-specific image-space geometry proxy, not a universal human-body standard.

## Torso-specific intent

The guide must communicate:

- compact torso
- no vertically elongated ribcage→waist→pelvis stack
- waist must not read unnaturally low
- pelvis/crotch slightly high
- lower body subtly longer
- do not obtain the target by stretching only the legs
- do not obtain the target by compressing only the torso

The approved total/inseam ranges imply an audit envelope for chin→crotch.
The runtime QA should continue to enforce its configured torso-specific numeric gate.

## Knee / lower-leg inspection

Candidate knee proxy:
- knee y: **1156**
- crown→knee: **5.5333 heads**
- thigh share of crotch→soles: **50.00%**

The knee marker is primarily a QA landmark. A roughly balanced thigh/lower-leg split is useful
for detecting thigh-only or shin-only stretching, but it should not override the approved
Body Geometry Guide silhouette.

## Promotion procedure

Do **not** overwrite the active Authority immediately.

1. Author visually reviews this candidate.
2. If approved, replace:
   `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`
3. Recompute SHA-256 and Git blob SHA.
4. Update `BODY_GEOMETRY_GUIDE.md` with the approved image hashes and explicit boundary.
5. Run free benchmark preflight.
6. Only then perform another paid RAW generation.

Until step 2–4 are completed, this file is not an active visual Authority.
