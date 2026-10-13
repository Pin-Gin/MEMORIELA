# YURA Master / Production Specification — Current Handoff

Status: **SAMPLE 9 FORMAL FULL-BODY MASTER / PIXEL V1 COMPLETE / AMBIGUITY PROTOCOL VALIDATED / FREE FIVE-VIEW PREFLIGHT NEXT**

This is the primary operational restart document. It is not itself Visual Authority.

## 1. Current objective

Newest author-approved order:

```text
Visual Ambiguity Protocol
-> protocol validation
-> shortest reproducible Codex-side diagnostic reference route
-> free preflight for five independent views
-> five DIAGNOSTIC / CANDIDATE generations
-> route + view-behavior PASS
-> ear problem
-> rear-hair / back-view problem
-> corrected multi-view reference promotion only after author review
```

The multi-view images generated before ear/rear-hair correction are diagnostic candidates only. They must not canonize current overlong ears or unverified rear-hair structure.

## 2. Required read order

Read current `main` in this order:

```text
1. tools/yura-master-benchmark/CURRENT_HANDOFF.md
2. tools/yura-master-benchmark/PIPELINE_STATE.md
3. visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md
4. tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md
5. visuals/yura/identity/face/YURA_FACE_MASTER_PHASE_PLAN_20261013.md
6. visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md
7. visuals/yura/identity/master/YURA_MASTER_PIXEL_MEASUREMENT_20261013.md
8. visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md
9. visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md
10. visuals/yura/identity/face/FACE_REFERENCE_RULES.md
11. visuals/yura/identity/master/YURA_VISUAL_TEXT.md only for still-active rules not replaced by newer Production Authority
12. tools/yura-master-benchmark/TEST6_RESULT_20261012.md only as historic audit context
```

Where older files say to proceed directly to Face measurement, the newer Visual Ambiguity Protocol controls the current sequencing.

## 3. Fixed visual sources

Formal full-body Master:

```text
path = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
source = Variance Study Sample 9 original local RAW
formal author promotion = YES
```

Active Face Reference:

```text
path = visuals/yura/identity/face/YURA_FACE_REFERENCE.png
Git blob SHA = 4c96c4ec42f996807248be1aff60ec8a090fd570
SHA256 = 3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
canvas = 372 x 364 RGBA
ZIP ↔ current main = PASS
PNG integrity = PASS
```

The current Face Reference contains a known author-identified ear-longation defect. Its current ear dimensions are diagnostic evidence, not automatically the corrected target.

## 4. Full-body Production baseline

Canonical full-body pixel measurement V1 is complete. The Sample 9 Production baseline is sufficiently detailed to prevent Face references from redefining BODY geometry.

Historic Body Guide / Test 6 mismatches remain audit history. Do not silently reactivate them as current Production gates.

## 5. Source and ambiguity classification

Existing source classes:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

Additional ambiguity classes:

```text
MEASURED_VISIBLE_FACT
MEASURED_OCCLUSION_FACT
ESTIMATED_HIDDEN_GEOMETRY
AUTHOR_INTENT
VIEW_SPECIFIC_RULE
NON_COMPENSATION_RULE
```

For occluded structure, keep these separate:

```text
ACTUAL / STRUCTURAL GEOMETRY
VISIBLE GEOMETRY
OCCLUSION / LAYER ORDER
VIEW
```

Unknown hidden structure remains unknown. Do not invent unsupported 3D geometry as Authority.

## 6. Naturalness / non-compensation rule

Low visibility alone is not a defect.

Do not improve visibility by enlarging, elongating, widening, moving outward, rotating toward camera, clearing natural occlusion, forcing bilateral symmetry, or unnaturally fanning hair.

Final acceptance requires:

```text
STRUCTURAL CONSISTENCY
IDENTITY CONSISTENCY
VISUAL NATURALNESS
```

## 7. Protocol validation result

`visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md`

Validation against current Face/BODY separation, ear rule, Hair SUPER-LONG override, and Production measurement governance:

```text
PASS
```

The only sequencing conflict was the older direct-to-Face-measurement instruction. The new protocol explicitly inserts diagnostic multi-view validation first.

## 8. Diagnostic multi-view generation route

Generation contract:

`tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md`

Dedicated one-view runner:

`tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py`

Dedicated image transport config:

`tools/yura-master-benchmark/visual_ambiguity_reference_config.json`

Five independent views:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

One view is generated per invocation. A five-panel single image is not used.

The runner uses only:

```text
image 1 = formal YURA_VISUAL_MASTER.png
image 2 = active YURA_FACE_REFERENCE.png
```

It explicitly denies Body Geometry Guide, old Masters, Test 5/6 outputs, past generated candidates, story/manuscript/characters appearance, Memory-derived appearance, and Git-history fallback visuals.

Image transport settings are isolated in `visual_ambiguity_reference_config.json`; no legacy Test 5 authority order, Body Guide gate, historic pelvis/inseam gate, Body QA, or composition gate is imported.

## 9. Diagnostic status rule

Before ear and rear-hair correction:

```text
status = DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

Route/view-behavior PASS means the requested view, source tracking, prompt invariants, and non-compensation contract behave correctly. It does not mean the generated visual becomes Authority.

## 10. Ear checkpoint after route PASS

Current working ear rule remains:

```text
ear actual height target = 20–22% face vertical dimension
HARD MAX = 23%
ear visibility lower priority than natural size / placement
no visibility compensation
```

Then measure/resolve separately:

```text
EAR ACTUAL GEOMETRY
EAR VISIBLE GEOMETRY
HAIR OCCLUSION
```

## 11. Rear-hair checkpoint after ear

Current Hair AUTHOR_OVERRIDE remains:

```text
SUPER-LONG mandatory
must clearly reach waist area
ordinary-long / mid-back = FAIL
modestly longer than Sample 9
not substantially below waist
```

Rear-hair / back-view mass, silhouette, and layer ordering remain unresolved until that phase. Generated rear views before then are diagnostic hypotheses only.

## 12. Current execution state

```text
Formal Sample 9 Master                    = COMPLETE
Full-body pixel measurement V1            = COMPLETE
Visual Ambiguity Protocol                 = ACTIVE / AUTHOR APPROVED
Protocol-vs-authority validation           = PASS
Five-view generation spec                 = COMPLETE
Dedicated one-view runner                 = COMPLETE / GIT-LEVEL REVIEWED
Dedicated image transport config          = COMPLETE
Free five-view preflight                   = NEXT
Five-view diagnostic generation           = NOT YET
Route / view-behavior PASS                 = NOT YET
Ear correction                             = AFTER PASS
Rear-hair / back-view correction           = AFTER EAR
Corrected multi-view promotion             = NOT YET
Paid Face-only Pilot 1                     = NOT YET
Formal Face Master                         = NOT YET
Production Visual MD                       = NOT YET
```

## 13. Exact next action

Run **free** syntax check + preflight with zero paid model calls, starting with FRONT:

```text
python -m py_compile tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view FRONT --preflight-only
```

Review:

```text
preflight.json
compiled_prompt.txt
source_hashes.json
current origin/main equality
exact Master / Face SHA-256
dedicated image transport config
ambiguity prompt invariants
known ear defect not promoted
rear-hair structure not promoted
denied-source list
```

If FRONT passes, repeat free preflight for FRONT_3Q, SIDE, REAR_3Q, and BACK.

Do not start paid diagnostic image generation until this five-view preflight set is reviewed.

## 14. Repository safety

```text
no git reset --hard
no force-push
no unrelated file changes
no story/manuscript/Memory appearance as Visual Authority
no reactivation of Test 5/6 generation routes for current work
```
