# YURA Visual Work — CURRENT STATE

Status: **ACTIVE / FACE-UP MASTER PROMOTED / FREE FULL-BODY CALIBRATION PASS / PAID FULL-BODY ROUTE REBUILT**

## Current objective

Create the new YURA full-body Master from the current repository-promoted Face-up Master and current `YURA_VISUAL_TEXT.md`.

Current author-directed sequence:

```text
Ear Geometry Master = DONE
Face-up Master = DONE
Face-up descriptive MD = DONE
free GPT full-body balance calibration = PASS
paid full-body route rebuild = DONE
free paid-route preflight = NEXT
one paid seed run = AFTER PREFLIGHT
7.0–7.2 head-ratio QA + author visual QA
PASS -> full-body Master promotion
```

## Current visual authority state

```text
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
= ACTIVE / HIGHEST YURA VISUAL TEXT AUTHORITY

visuals/yura/identity/face/YURA_FACE_REFERENCE.png
= AUTHOR-PASS / REPOSITORY-PROMOTED CURRENT FACE REFERENCE

visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
= ACTIVE CURRENT FACE-UP TEXT AUTHORITY

visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
= AUTHOR-PASS / VERIFIED / REPOSITORY PROMOTED

visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
= ACTIVE EAR SUPPORTING RULE

visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
= BODY-GEOMETRY SUPPORT IMAGE; CURRENT VISUAL TEXT WINS ON CONFLICT
```

## Locked domains

The following must not be rewritten merely to make paid generation pass:

```text
Face Geometry / facial parts
Eye shape / size / placement
C2 baseline -> 0.3% inward
Pupil bilateral symmetry
Ear Geometry / no visibility compensation
Body definition
Current chest-to-frame relationship
```

## Current full-body target

```text
TARGET HEAD COUNT RANGE = 7.0–7.2
TARGET HEIGHT IMPRESSION = 152–153 cm
```

Do not satisfy the range by face elongation, torso-only elongation, leg-only elongation, shoulder widening, ribcage enlargement, or tall model-like conversion.

## Current free GPT calibration result

The latest free GPT full-body validation image received author **PASS**.

Its role is:

```text
balance / presentation calibration indicator
```

It is **not** a Git Authority and is not automatically passed to the paid Image API.

Accepted current presentation condition includes:

```text
front-facing full body
completely upright
arms down
legs near together
both feet flat / heels down / full sole contact
barefoot
pure white background
centered
plain opaque matte camisole
plain undecorated shorts
silver-white straight-dominant super-long hair ending around waist
white-leaning skin without over-whitening
true neutral expression
```

## Current paid route state

```text
legacy paid route = RETIRED
current sealed-bundle paid route = REBUILT
author paid-generation permission = YES
billable call before current preflight = DENIED
```

Current operational documents:

```text
tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md
tools/YURA_MASTER_GENERATION_CURRENT_STATE.md
tools/YURA_MASTER_GENERATION_WORKLOG.md
tools/yura-master-benchmark/PAID_ROUTE_STATUS.md
tools/yura-master-benchmark/README.md
```

Current architecture:

```text
current Git main
-> local Python Authority/hash verification
-> sealed Authority bundle
-> Codex prompt compile
-> runner manifest / invariant verification
-> OpenAI Image API
-> result.png
-> head-ratio QA
-> author QA
```

## Retired active-route numeric gates

Historical paid-route values below are not current hard gates:

```text
7.1–7.3
89% occupancy
88–90%
5–6% margins
legacy Test 5 contract
legacy composition percentage postprocess
```

Historical records remain under `tools/**` for audit only.

## Next exact task

Sync local repository to current `main`, then run:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Required preflight result:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
head_ratio_gate = 7.0–7.2
```

Only after reviewing that preflight should exactly one paid seed run be executed.
