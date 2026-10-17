# YURA Master / Production Specification — Current Handoff

Status: **FULL-BODY MASTER PROMOTED / RECOVERY PREFLIGHT VERIFIED / PAID ROUTE FROZEN**

This is an operational restart document, not Visual Authority.

## Purpose

Preserve enough operational state to reproduce or recover the current YURA full-body generation route in a future chat without treating historical paid outputs as current appearance Authority.

The normal current use is derivative generation from the official Full-body Master. This document is mainly for recovery / regeneration.

## Completion state

```text
Ear Geometry Master = promoted
Face-up Master = promoted
Full-body Master = promoted
7.0-head Body Geometry Guide = current support asset
paid generation = completed and stopped by author
paid batch = not executed / not required
recovery route = frozen
recovery preflight = verified PASS
paid model calls during recovery preflight = 0
```

## Official Full-body Master

```text
visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
promotion commit = 3ce89e33193effa627ea794e803d9a3b50cb085b
SHA-256 = CCBE315659DAC02169C833F8140096322725E85250FAB73214D30FBBC835EDF1
```

Body-directory synchronized copy:

`visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png`

The two files are expected to remain identical binaries.

## Current Body Geometry Guide

```text
visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
SHA-256 = C23D1D2C348102B4ED9D75C422E1C2323800565B94E27A7FF13AF7C624EBDF95
role = 7.0-head proportion / recovery support only
```

It must not override the official Full-body Master or face / ear local Authorities.

## Current hard standard

```text
TARGET HEAD COUNT RANGE = 7.0–7.2 heads
TARGET HEIGHT IMPRESSION = 152–153 cm
ONE HEAD = structural crown / skull top to chin
VISIBLE HAIR VOLUME != SKULL HEIGHT
```

Face Geometry, eye geometry / placement, ear geometry, body definition, chest-to-frame relationship, and promoted integrated full-body proportions remain locked.

## Current read order

For current YURA full-body work read:

```text
1. project-management/yura-visual/START_HERE.md
2. project-management/yura-visual/CURRENT_STATE.md
3. project-management/yura-visual/DECISIONS.md
4. project-management/yura-visual/WORKFLOW.md
5. visuals/yura/identity/master/YURA_VISUAL_TEXT.md
6. visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
7. visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
8. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
9. visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
10. visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
11. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png when recovery/body proportion is relevant
```

For recovery implementation also read:

```text
tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md
tools/YURA_MASTER_GENERATION_CURRENT_STATE.md
tools/YURA_MASTER_GENERATION_WORKLOG.md
tools/yura-master-benchmark/PAID_ROUTE_STATUS.md
tools/yura-master-benchmark/README.md
tools/yura-master-benchmark/config.json
tools/yura-master-benchmark/codex_instruction.md
```

## Recovery method

```text
current Git main
-> verify configured Authority files and SHA-256
-> verify primary Full-body Master and body-directory synchronized copy match
-> verify Body Geometry Guide hash
-> build sealed Authority bundle
-> Codex prompt compile
-> manifest / invariant verification
-> OpenAI Image API
-> direct image QA using structural crown / chin / soles
-> explicit author visual QA
```

Current recovery Image API reference order:

```text
1. visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
2. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
3. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
```

## Verified recovery preflight

The latest verified preflight was run against:

```text
git_commit = 690218017a0c3dedba7f34907b97454a53643e41
run_dir = tools/yura-master-benchmark/runs/run_20261017T200301Z
status = PREFLIGHT_OK
paid_model_calls = 0
paid_generation_allowed = false
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
authority_count = 8
sealed_authority_bundle_sha256 = dfa026cc8049c238fa553e2adac01fd422f399ec747082a01bee11fc2d3dd068
codex_input_sha256 = 8a82a534da6ce227bf5ea961c260926671ae1971eb530c7ab42d13a47ffd9553
head_ratio_gate = 7.0–7.2
height_impression_cm = 152–153
legacy_composition_percentage_gates = RETIRED
```

This confirms the frozen recovery route can verify the current Authority set without making any paid model call.

## Paid route state

```text
PAID_GENERATION_ALLOWED = NO
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
```

A successful preflight does not authorize billing. The frozen route must not proceed to Codex / Image API paid execution until the author explicitly reopens regeneration and deliberately updates authorization.

## Normal derivative use

For temporary clothing changes or other ordinary full-body derivatives, start from:

`visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png`

The validation camisole / shorts are not permanent wardrobe Authority. Preserve the approved body / identity and change only the explicitly requested derivative variable.

## Full-body QA method

Head ratio is determined directly from the generated image:

```text
structural skull top / crown -> chin = head height
structural skull top / crown -> soles = full-body height
head count = full-body height / head height
```

Do not use visible hair volume as structural crown and do not require a pre-existing `body_geometry_qa.json` merely to perform this measurement.

## Retired legacy active gates

```text
7.1–7.3
89% occupancy
88–90%
5–6% margins
legacy Test 5 contract
```

Historical files remain audit only.

## Next normal action

No paid-generation action is pending.
Use the official Full-body Master for future derivative work.
Reopen the paid recovery route only after explicit author authorization.
