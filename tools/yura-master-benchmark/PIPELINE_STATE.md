# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / BODY-GEOMETRY-FIRST / NUMERIC-GATED / COMPOSITION-DEFERRED**

This file is operational documentation only. It is **NOT** a YURA visual Authority.

## Current execution order

```text
current Git main
  -> local runner verifies HEAD == origin/main
  -> configured Authority files only
  -> sealed Authority bundle + SHA-256
  -> Codex compiles RAW Body-Geometry-first Image API prompt
  -> runner rejects prompt if required Body Geometry measurement contract is missing
  -> runner rejects prompt if final Composition numeric targets leaked into it
  -> Image API generates result_raw.png only
  -> body_geometry_qa.py
       manual reviewed crown/chin/soles Y landmarks
       ratio = (soles - crown) / (chin - crown)
       target = 7.2
       acceptable = 7.1–7.3
       raw SHA-256 is bound into body_geometry_qa.json
     -> numeric FAIL: stop; Composition blocked
     -> numeric PASS: remaining Body Geometry/silhouette visual review
  -> explicit Body Geometry confirmation
  -> normalize_composition.py verifies numeric PASS + RAW SHA match
  -> uniform whole-raster scale + x/y translation only
  -> result.png at final Composition target
  -> final QA / author confirmation
  -> Master promotion remains NO until explicit final PASS
```

## Why numeric Body Geometry QA is now mandatory

A RAW run with final Composition numeric targets removed from the Image API prompt reduced the earlier vertical-stretch tendency, but the generated candidate still measured visually near ~6 heads rather than the Authority target 7.2.

Therefore the current diagnosis is:

```text
Composition conflict was a real confounder,
but removing it is not sufficient to guarantee Body Geometry compliance.
```

Body Geometry is now measured independently before any Composition normalization.

## RAW Image API responsibility

The RAW Image API prompt contains Face Identity, Body Geometry, appearance, pose and complete full-body visibility requirements.

It does **not** contain final Composition numeric targets such as 1440×2560, 89% occupancy, 88–90%, or 5–6% margins. Those values remain in the active Composition Authority and operational postprocess config, but are intentionally withheld from the RAW generation prompt so the image model does not optimize anatomy for canvas fitting.

The RAW Body Geometry prompt now also states explicitly:

```text
ONE HEAD IS CROWN TO CHIN.
CROWN TO SOLES MUST BE 7.2 HEADS.
BODY-GEOMETRY REFERENCE SCALE OVERRIDES DEFAULT LARGE-HEAD ANIME BODY PROPORTIONS.
DO NOT ACHIEVE 7.2 BY LENGTHENING ONLY LEGS OR ONLY TORSO.
```

These are generation-stage geometry constraints, not Composition targets.

## Hard prompt gate

Before Image API is called, the runner requires the RAW-stage invariants and rejects any compiled prompt that contains deferred final-Composition literals.

Failure at this gate means:

```text
Image API called = false
```

## Files produced by a successful RAW run

```text
result_raw.png
composition_deferred.json
qa.json
cost.json
compiled_prompt.txt
compiled_prompt.sha256
prompt_invariant_check.json
```

`result.png` is intentionally absent at this stage.

## Numeric Body Geometry gate

Landmarks are intentionally reviewed manually. Crown and soles can often be detected from background separation, but chin is not safely inferable from generic raster segmentation, so the benchmark does not pretend to auto-measure it.

Record reviewed pixel Y positions:

```powershell
python tools/yura-master-benchmark/body_geometry_qa.py <RUN_DIR> `
  --crown-y <Y> `
  --chin-y <Y> `
  --soles-y <Y> `
  --confirm-landmarks-reviewed
```

The tool writes:

```text
body_geometry_qa.json
```

with:

```text
head_height     = chin_y - crown_y
figure_height   = soles_y - crown_y
heads           = figure_height / head_height
PASS            = 7.1 <= heads <= 7.3
```

The report also stores the SHA-256 of `result_raw.png`.
A PASS report for a different RAW image cannot unlock Composition.

Numeric PASS is necessary but not sufficient: internal landmark placement, silhouette and Face Identity remain separate visual QA checks.

## Body Geometry -> Composition gate

Plan only, no final image:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR>
```

Final normalization is allowed only when all of the following hold:

```text
body_geometry_qa.json exists
pass == true
status == PASS
landmarks_reviewed == true
head ratio is inside 7.1–7.3
body_geometry_qa.raw_sha256 == current result_raw.png SHA-256
qa.json body_geometry_status == PASS_NUMERIC
--confirm-body-geometry-pass was explicitly supplied
```

Then:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR> --confirm-body-geometry-pass
```

creates `result.png` only if deterministic Composition QA also passes.

## Allowed final Composition transforms

Only:

- uniform whole-raster scaling
- x/y translation
- white-background crop/pad implied by final canvas placement

Never:

- nonuniform scaling
- body-part scaling
- warp
- content-aware deformation
- inpainting/body reshaping
- face regeneration

## Current next step

Sync latest main while preserving the unrelated local novel draft. Run syntax checks for:

```text
body_geometry_qa.py
normalize_composition.py
run_raw_once.py
run_once.py
```

Then run the free preflight only.
Do not make another paid Image API call until the preflight confirms the numeric Body Geometry gate and zero paid calls.
