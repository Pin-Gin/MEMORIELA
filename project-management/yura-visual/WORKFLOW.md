# YURA Visual Work — WORKFLOW

Status: **CURRENT POST-PROMOTION WORKFLOW / PROJECT-MANAGEMENT ONLY / NOT VISUAL AUTHORITY**

## Governing principle

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md` is the highest YURA visual text authority.

The official integrated full-body visual baseline is:

`visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png`

This workflow controls sequencing and operational method only. It must not redefine appearance.

## 1. Completed production sequence

The current YURA visual sequence has completed through Full-body Master promotion:

```text
Ear Geometry Master
-> Face-up Master
-> Face-up descriptive MD
-> free full-body calibration
-> rebuilt paid full-body route
-> iterative paid seed generation / QA
-> author-selected candidate
-> direct 7.0–7.2 head-ratio validation
-> explicit author PASS
-> Full-body Master promotion
-> replacement 7.0-head Body Geometry Guide creation
-> paid route freeze
-> recovery preflight verification
```

The paid batch stage was not executed and is not required for the current promoted Master.

## 2. Method used

### Ear / face stages

Ear geometry was isolated and verified before normal-hair face integration. Ear visibility compensation was treated as failure; zero visibility under natural hair is acceptable.

Face-up work preserved the approved face geometry and produced the current repository-promoted Face Reference / Face-up text Authority.

### Full-body stage

Full-body work used the current Visual Text, current face and ear Authorities, and body constraints. Head-ratio correction was handled as whole-head physical scale relative to the body, not by changing internal face geometry or vertically stretching body regions.

Paid-route architecture:

```text
current Git
-> verify configured Authority files / hashes
-> sealed Authority bundle
-> Codex prompt compile
-> runner manifest / invariant verification
-> OpenAI Image API
-> generated candidate
-> direct image QA
-> explicit author decision
```

### Head-ratio QA method

Measure directly from the generated image:

```text
structural skull top / crown -> chin = one head
structural skull top / crown -> soles = full body
head count = full-body height / head height
```

Visible outer hair volume must not be used as skull height.

The current promoted result passed the intended 7.0–7.2 range before Master promotion.

## 3. Current standards

```text
TARGET HEAD COUNT RANGE = 7.0–7.2 heads
TARGET HEIGHT IMPRESSION = 152–153 cm
```

Locked domains:

```text
Face Geometry / facial parts
Eye shape / size / placement
C2 baseline -> 0.3% inward
Pupil bilateral symmetry
Ear actual geometry / no visibility compensation
Body definition
Current chest-to-frame relationship
Official integrated Full-body Master proportions
```

Never solve proportion by:

```text
face / midface / chin elongation
torso-only elongation
leg-only elongation
shoulder widening
ribcage enlargement
tall model-like conversion
```

## 4. Body Geometry Guide role

Current support reference:

`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

Purpose:

```text
7.0-head proportion reference
body-geometry recovery support
insurance for future Master regeneration
```

It is subordinate to the official Full-body Master and current Visual Text. It must not become Face Identity Authority and must not override face / ear local Authorities.

## 5. Normal future derivative workflow

For ordinary derivative work such as temporary clothing changes:

```text
1. read current YURA Visual Text
2. use official YURA_FULL_BODY_MASTER.png as the primary integrated visual reference
3. preserve face / body / hair / proportion identity
4. change only the explicitly requested derivative variable
5. do not treat validation camisole / shorts as permanent wardrobe
6. review the result as a candidate; do not auto-promote
```

The Body Geometry Guide is optional support, not the primary reference for ordinary derivative work.

## 6. Future Full-body Master regeneration workflow

Only if the author explicitly reopens regeneration:

```text
1. sync current Git main
2. verify current Authority set and hashes
3. verify primary and body-directory Full-body Master copies match
4. verify current Body Geometry Guide
5. review frozen recovery config
6. run free recovery preflight
7. confirm PREFLIGHT_OK and 0 paid model calls
8. explicitly reauthorize paid generation
9. update paid_generation_allowed deliberately
10. run exactly one paid seed first
11. direct head-ratio QA from generated image
12. explicit author visual QA
13. promote only after explicit PASS
```

Current recovery Image API reference order:

```text
1. YURA_FULL_BODY_MASTER.png
2. YURA_BODY_GEOMETRY_GUIDE.png
3. YURA_FACE_REFERENCE.png
```

A preflight PASS alone never authorizes billing.

## 7. Current paid state

```text
PAID_GENERATION_ALLOWED = NO
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
```

The runner is intentionally fail-closed before Codex / Image API paid execution while this flag remains false.

## 8. Rejection rule

A FAIL image:

```text
is not Authority
is not a Master
is not a future identity reference
must not be fed back automatically
```

## 9. One change at a time

When diagnosing a specific failure, change only the minimum intended variable. Do not combine face redesign, ear correction, body correction, rendering change, and composition correction into one uncontrolled test.
