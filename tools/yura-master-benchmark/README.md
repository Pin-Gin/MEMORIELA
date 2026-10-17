# YURA Master Benchmark — Current Paid Full-body Route

Status: **CURRENT / AUTHOR-AUTHORIZED / SEALED CURRENT AUTHORITY ROUTE**

This directory executes the current YURA paid full-body Master-generation experiment.

## Flow

```text
Git current main
-> verify configured current Authorities
-> sealed_authority_bundle.json
-> Codex prompt compile
-> manifest + prompt invariant verification
-> OpenAI Image API
-> result.png
-> cost.json / qa.json
-> manual head-ratio QA
-> author review
```

Codex is a prompt compiler. It is not allowed to invent YURA appearance or use non-sealed sources.

## Current Authority order

Defined by `config.json`:

```text
YURA_VISUAL_TEXT.md
YURA_FACE_REDESIGN_SPEC.md
YURA_FACE_UP_MASTER.md
YURA_FACE_REFERENCE.png
YURA_EAR_BASIC_RULES.md
YURA_EAR_GEOMETRY_MASTER.png
YURA_BODY_GEOMETRY_GUIDE.png
```

## Current Image API reference order

```text
1. YURA_BODY_GEOMETRY_GUIDE.png
2. YURA_FACE_REFERENCE.png
```

## Current hard full-body target

```text
7.0–7.2 heads
152–153 cm height impression
```

Legacy `7.1–7.3` is not active.

Legacy `89% / 88–90% / 5–6%` Composition percentage gates are not active.

## Install

```powershell
python -m pip install -r tools/yura-master-benchmark/requirements.txt
```

Required local tools:

```text
Python
Codex CLI
OpenAI Python SDK
Git working copy
OPENAI_API_KEY for paid run
```

Do not store keys in Git or chat.

## Syntax check

```powershell
python -m py_compile tools/yura-master-benchmark/run_raw_once.py
python -m py_compile tools/yura-master-benchmark/run_once.py
python -m py_compile tools/yura-master-benchmark/run_batch.py
python -m py_compile tools/yura-master-benchmark/body_geometry_qa.py
```

## Free preflight

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

No paid model call occurs.

Expected core output:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
head_ratio_gate = 7.0–7.2
```

## One paid run

After preflight review:

```powershell
python tools/yura-master-benchmark/run_once.py
```

Successful technical output creates a run directory under:

```text
tools/yura-master-benchmark/runs/
```

Typical artifacts:

```text
run_meta.json
sealed_authority_bundle.json
sealed_authority_bundle.sha256
codex_input.sha256
authority_manifest.json
codex_trace.jsonl
codex_stderr.log
codex_usage_candidates.json
compiled_prompt.txt
compiled_prompt.sha256
prompt_invariant_check.json
result.png
image_response.json
cost.json
qa.json
```

Generated output starts as:

```text
candidate = QA_PENDING
master_promotion = NO
```

## Head-ratio QA

Measure actual structural crown, not outer hair volume:

```powershell
python tools/yura-master-benchmark/body_geometry_qa.py <RUN_DIR> `
  --structural-crown-min-y <Y> `
  --structural-crown-best-y <Y> `
  --structural-crown-max-y <Y> `
  --chin-y <Y> `
  --soles-y <Y> `
  --confirm-measurement-reviewed
```

Current numeric PASS range:

```text
7.0–7.2
```

This script does not rewrite body geometry and does not auto-promote.

## Batch

After one reviewed seed run and cost review:

```powershell
python tools/yura-master-benchmark/run_batch.py `
  --seed-run tools/yura-master-benchmark/runs/<RUN_DIR> `
  --runs 10 `
  --confirm-seed-reviewed `
  --allow-estimate
```

Use `--allow-estimate` only when explicitly accepting the stored estimate snapshot. Prefer authoritative run-specific cost attribution where available.

Each item is a separate run.

## Current prompt compile gates

`codex_instruction.md` requires the current Face-up / ear / body / pose / clothing / hair / skin rules and exact current head-count range.

`run_raw_once.py` fails closed before Image API if required current invariant lines are missing or retired legacy numeric gates leak into the compiled prompt.

## Full-body execution condition

Current validation presentation is:

```text
front-facing
full body
completely upright
arms down
legs near together
both feet flat
heels down
full sole contact
barefoot
white background
centered
plain opaque matte camisole
plain undecorated shorts
```

Hair ends around the waist, not substantially below it.

Skin is clearly white-leaning, but must not be over-whitened.

## Master promotion

Numeric PASS is not sufficient.

Explicit author PASS is mandatory.

Paid-run prompts, manifests, costs, traces, candidates and QA remain under `tools/**`.

Only the author-approved final Master belongs under `visuals/**`.
