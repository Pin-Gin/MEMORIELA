# YURA Master Benchmark — Frozen Recovery Route

Status: **FULL-BODY MASTER PROMOTED / PAID EXECUTION FROZEN / RECOVERY TOOLING RETAINED**

This directory now preserves the sealed-bundle implementation used during YURA Full-body Master generation and provides a recovery / regeneration route if the author explicitly reopens that phase.

The current paid-generation phase is complete.

```text
PAID_GENERATION_ALLOWED = NO
```

A successful preflight does not authorize a billable call.

## Current promoted visual baseline

```text
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
= highest YURA visual text authority

visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
= official integrated full-body visual Master

visuals/yura/identity/face/YURA_FACE_REFERENCE.png
= face-local identity / geometry reference

visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
= ear-local geometry reference

visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
= current 7.0-head body-geometry support / recovery guide only
```

Official Full-body Master promotion commit:

```text
3ce89e33193effa627ea794e803d9a3b50cb085b
```

## Recovery flow

If the author explicitly reopens Full-body Master regeneration:

```text
Git current main
-> verify configured current Authorities
-> sealed_authority_bundle.json
-> Codex prompt compile
-> manifest + prompt invariant verification
-> OpenAI Image API
-> result.png
-> cost.json / qa.json
-> image-based head-ratio QA
-> author review
```

Codex is a prompt compiler. It is not allowed to invent YURA appearance or use non-sealed sources.

## Current recovery Authority order

Defined by `config.json`:

```text
YURA_VISUAL_TEXT.md
YURA_FULL_BODY_MASTER.png
YURA_FACE_REDESIGN_SPEC.md
YURA_FACE_UP_MASTER.md
YURA_FACE_REFERENCE.png
YURA_EAR_BASIC_RULES.md
YURA_EAR_GEOMETRY_MASTER.png
YURA_BODY_GEOMETRY_GUIDE.png
```

## Current recovery Image API reference order

```text
1. YURA_FULL_BODY_MASTER.png
   primary integrated full-body visual reference

2. YURA_BODY_GEOMETRY_GUIDE.png
   7.0-head proportion / body-geometry recovery support only

3. YURA_FACE_REFERENCE.png
   face-local identity / geometry reference
```

The Body Geometry Guide must not override the official Full-body Master.
The validation clothing visible in the Full-body Master is not permanent wardrobe Authority.

## Current hard full-body standard

```text
7.0–7.2 heads
152–153 cm height impression
```

Legacy `7.1–7.3` is not active.
Legacy `89% / 88–90% / 5–6%` composition percentage gates are not active.

## Install

```powershell
python -m pip install -r tools/yura-master-benchmark/requirements.txt
```

Required local tools for a future reopened route:

```text
Python
Codex CLI
OpenAI Python SDK
Git working copy
OPENAI_API_KEY for an explicitly reauthorized paid run
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

The frozen route may still be checked without paid model calls:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Expected core output includes:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
paid_generation_allowed = false
head_ratio_gate = 7.0–7.2
```

The preflight output must indicate that paid execution remains frozen.

## Paid execution

Paid execution is currently disabled by config and runner guard.
Running without `--preflight-only` must fail closed while:

```text
PAID_GENERATION_ALLOWED = NO
```

Do not re-enable this flag merely because a technical preflight passes.
Explicit author authorization is required first.

## Run artifacts

Historical run directories remain under:

```text
tools/yura-master-benchmark/runs/
```

Typical artifacts include:

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

These are process records, not Visual Authority.

## Head-ratio QA

For a future regeneration candidate, measure actual structural crown, not outer hair volume.
The current standard remains:

```text
7.0–7.2
```

The project also uses direct image measurement during author / GPT review.
`body_geometry_qa.py` remains optional recovery tooling and does not auto-promote.

## Current prompt compile gates

`codex_instruction.md` preserves current Face-up / ear / body / pose / clothing / hair / skin rules and the current Full-body Master / Body Guide role separation.

`run_raw_once.py` fails closed before Image API if required current invariant lines are missing, retired legacy numeric gates leak into the compiled prompt, or paid execution is not explicitly enabled.

## Full-body Master presentation note

The official Full-body Master uses the validation presentation:

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

The validation camisole / shorts are not permanent wardrobe Authority. For temporary clothing changes, use the official Full-body Master as the integrated body / identity reference and apply the requested clothing separately.

## Master promotion state

The current author-approved Full-body Master has already been promoted to `visuals/**`.
Historical paid-run prompts, manifests, costs, traces, candidates and QA remain under `tools/**`.
