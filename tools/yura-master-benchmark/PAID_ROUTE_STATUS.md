# YURA PAID ROUTE STATUS

Status: **AUTHOR-AUTHORIZED / CURRENT ROUTE REBUILT / FREE PREFLIGHT REQUIRED BEFORE PAID CALL**

## Permission

```text
PAID_GENERATION_ALLOWED = YES
```

This authorization applies only to the rebuilt current full-body route described by:

```text
tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md
tools/YURA_MASTER_GENERATION_WORKLOG.md
tools/YURA_MASTER_GENERATION_CURRENT_STATE.md
tools/yura-master-benchmark/README.md
tools/yura-master-benchmark/config.json
tools/yura-master-benchmark/codex_instruction.md
```

The archived pre-rebuild runner remains historical audit material.

## Current route

```text
current Git
-> local Python verification
-> sealed current Authority bundle
-> Codex prompt compile
-> runner verification
-> OpenAI Image API
-> QA
-> author decision
```

## Current Authority basis

```text
current YURA_VISUAL_TEXT.md
current Face Redesign Spec
current Face-up Master MD
repository-promoted current Face Reference
current ear rules / Ear Geometry Master
current visual-layer Body Geometry Guide
```

Do not restore the old Face Reference, old full-body Master, or archived runner assumptions.

## Current full-body target

```text
HEAD COUNT = 7.0–7.2
HEIGHT IMPRESSION = 152–153 cm
```

Face, ear and body definitions are locked.

## Retired active-route gates

```text
7.1–7.3
89% occupancy
88–90%
5–6% margins
legacy Test 5 prompt contract
legacy composition percentage postprocess
```

Historical files may retain those values for audit, but the rebuilt current runner must not compile them into the active paid prompt.

## Required preflight

Before the first billable call:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Required:

```text
PREFLIGHT_OK
paid_model_calls = 0
```

## First paid execution

Only after preflight review:

```powershell
python tools/yura-master-benchmark/run_once.py
```

Exactly one seed run first.

## Batch

Only after the seed run and its cost/technical artifacts have been reviewed.

Each batch item is an independent run.

## Promotion

Every generated result starts:

```text
QA_PENDING
master_promotion = NO
```

Explicit author PASS is mandatory for Master promotion.

All process artifacts remain under `tools/**`.
