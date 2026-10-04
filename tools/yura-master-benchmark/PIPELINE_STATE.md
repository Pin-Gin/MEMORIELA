# YURA Master Benchmark — Pipeline State

Status: **ACTIVE / BODY-GEOMETRY-FIRST / COMPOSITION-DEFERRED**

This file is operational documentation only. It is **NOT** a YURA visual Authority.

## Current execution order

```text
current Git main
  -> local runner verifies HEAD == origin/main
  -> configured Authority files only
  -> sealed Authority bundle + SHA-256
  -> Codex compiles RAW Body-Geometry-first Image API prompt
  -> runner rejects prompt if final Composition numeric targets leaked into it
  -> Image API generates result_raw.png only
  -> Body Geometry QA
     -> FAIL: stop; no result.png
     -> PASS: explicit confirmation required
  -> normalize_composition.py
  -> uniform whole-raster scale + x/y translation only
  -> result.png at final Composition target
  -> final QA / author confirmation
  -> Master promotion remains NO until explicit final PASS
```

## RAW Image API responsibility

The RAW Image API prompt contains Face Identity, Body Geometry, appearance, pose and complete full-body visibility requirements.

It does **not** contain final Composition numeric targets such as 1440×2560, 89% occupancy, 88–90%, or 5–6% margins. Those values remain in the active Composition Authority and operational postprocess config, but are intentionally withheld from the RAW generation prompt so the image model does not optimize anatomy for canvas fitting.

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

## Body Geometry gate

Composition normalization is not allowed until RAW Body Geometry has been reviewed and explicitly passed.

Plan only, no final image:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR>
```

After explicit Body Geometry PASS:

```powershell
python tools/yura-master-benchmark/normalize_composition.py <RUN_DIR> --confirm-body-geometry-pass
```

The second command creates `result.png` and updates `qa.json` only if deterministic Composition QA passes.

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

Sync latest main while preserving the unrelated local novel draft, then run syntax checks and the free preflight only. Do not make another paid Image API call until the new preflight shows the deferred-composition mode and zero paid calls.
