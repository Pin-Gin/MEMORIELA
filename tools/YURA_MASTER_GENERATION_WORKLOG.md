# YURA MASTER GENERATION — CURRENT WORKLOG / HANDOFF

Status: **CURRENT PAID FULL-BODY ROUTE REBUILT / AUTHOR AUTHORIZED / PREFLIGHT NOT YET RECORDED**

This file is operational history, not Visual Authority.

## 1. Current objective

Generate a new YURA full-body Master candidate using the repository-promoted new Face-up Master and current `YURA_VISUAL_TEXT.md`, then target **7.0–7.2 heads** without changing face, ear, or body definitions.

Current author-approved sequence:

```text
free GPT full-body balance calibration = PASS
-> rebuild paid route for current Face / Visual Text
-> free sealed preflight
-> one paid seed run
-> QA
-> independent batch runs if justified
-> explicit author PASS
-> Master promotion
```

## 2. Architecture retained from the successful historical benchmark

The reliable architecture is retained:

```text
current Git
-> Python runner verifies current configured sources
-> SHA-256
-> sealed Authority bundle
-> Codex prompt compiler
-> runner validates manifest and prompt invariants
-> OpenAI Image API
-> result / usage / cost / QA artifacts
```

Codex does not independently wander through the repository.

The Python runner owns Git/file verification and passes a sealed current-source bundle to Codex.

## 3. Current Authority migration

Legacy active inputs were removed from the paid route.

Current configured sources:

```text
YURA_VISUAL_TEXT.md
YURA_FACE_REDESIGN_SPEC.md
YURA_FACE_UP_MASTER.md
YURA_FACE_REFERENCE.png
YURA_EAR_BASIC_RULES.md
YURA_EAR_GEOMETRY_MASTER.png
YURA_BODY_GEOMETRY_GUIDE.png
```

The current Face Reference is the repository-promoted new face.

Legacy Face Reference rules are not part of the active bundle.

There is no active `BODY_GEOMETRY_GUIDE.md` in the current visual body directory, so the current route does not pretend that missing legacy text file is still live Authority.

## 4. Current image-reference routing

OpenAI Image API receives:

```text
1. YURA_BODY_GEOMETRY_GUIDE.png
2. YURA_FACE_REFERENCE.png
```

Role separation is mandatory.

Ear Geometry Master is hash-verified in the sealed bundle but is not passed as a third full-body image reference.

## 5. Current head-count condition

Historical:

```text
7.2 target
7.1–7.3 acceptable
```

Current:

```text
7.0–7.2 required range
152–153 cm height impression
```

Face Geometry must not be changed to reach the range.

The structural skull top, not visible hair volume, defines the head measurement.

## 6. Legacy composition migration

Retired from the active prompt gate:

```text
89% occupancy
88–90%
5–6% margins
legacy deterministic composition percentage postprocess
```

Current presentation rule comes from current Visual Text + author-fixed full-body validation condition:

```text
full body
front
upright
feet fully planted
white background
centered
head and feet not cropped
```

Image request canvas size remains an operational API setting, not an anatomy rule.

## 7. Current full-body execution locks

Locked, not tunable through paid-route optimization:

```text
face geometry / face parts
eye geometry and 0.3% inward placement
pupil bilateral symmetry
ear geometry and ear suppression
body definition
current chest-to-frame relationship
```

Generation text may optimize execution clarity only.

## 8. Current validation clothing / pose

```text
plain opaque matte camisole
plain undecorated shorts
no drawstring or decoration
barefoot

front-facing
completely upright
arms down
legs near together
heels down
full sole contact
no crossed legs
no contrapposto
white background
```

## 9. Current skin / hair

```text
skin = clearly white-leaning pale
not over-whitened
not pure white / sickly / washed out

hair = silver-white
straight-dominant
super-long
around waist
not substantially below waist
```

## 10. Batch policy

The historical experiment design remains:

```text
one paid run first
-> inspect technical success and cost
-> then independent 10-run batch if appropriate
```

The batch does not request ten opaque images in one call. Each run has its own sealed bundle, compiled prompt, image, cost, and QA record.

## 11. Current status

```text
paid route author authorization = YES
paid route code rebuild = CURRENT
sealed current-authority architecture = CURRENT
legacy paid condition = RETIRED
free preflight on rebuilt route = NOT YET RECORDED
first rebuilt paid seed run = NOT YET
batch = NOT YET
final full-body Master = NOT YET
```

## 12. Next exact action

After syncing the local repository to current `main`:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Do not start a batch before this preflight and one reviewed paid seed run.
