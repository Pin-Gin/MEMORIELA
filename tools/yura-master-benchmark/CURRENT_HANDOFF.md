# YURA Master / Production Specification — Current Handoff

Status: **SAMPLE 9 FORMAL FULL-BODY MASTER / PIXEL V1 COMPLETE / CODEX TEXT-ONLY AMBIGUITY VALIDATION NEXT**

This is the primary operational restart document. It is not itself Visual Authority.

## 1. Current objective

Newest author-approved order:

```text
Visual Ambiguity Protocol
-> Codex-native text-only generation
-> inspect generated images
-> confirm repeated ear-suppression behavior under unchanged Visual Text
-> OpenAI text-only Face-up Pilot 1
-> detailed ear ACTUAL / VISIBLE / HAIR OCCLUSION work
-> rear-hair / back-view mass / silhouette / layer-order work
```

The Codex phase does not use OpenAI Image API and does not use YURA image references.

## 2. Required read order

Read current `main` in this order:

```text
1. tools/yura-master-benchmark/CURRENT_HANDOFF.md
2. tools/yura-master-benchmark/PIPELINE_STATE.md
3. visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md
4. tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md
5. tools/yura-master-benchmark/codex_instruction_visual_ambiguity_reference.md
6. visuals/yura/identity/master/YURA_VISUAL_TEXT.md
7. visuals/yura/identity/face/YURA_FACE_MASTER_PHASE_PLAN_20261013.md
8. visuals/yura/identity/master/YURA_PRODUCTION_PART_SPEC_PROTOCOL.md
9. visuals/yura/identity/master/YURA_MASTER_PIXEL_MEASUREMENT_20261013.md
10. visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md
11. visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md
12. visuals/yura/identity/face/FACE_REFERENCE_RULES.md
13. tools/yura-master-benchmark/TEST6_RESULT_20261012.md only as historic audit context
```

The Visual Ambiguity Protocol is the newest sequencing rule where older files conflict.

## 3. Fixed visual sources / audit baseline

Formal full-body Master:

```text
path = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
formal author promotion = YES
```

Active Face Reference:

```text
path = visuals/yura/identity/face/YURA_FACE_REFERENCE.png
Git blob SHA = 4c96c4ec42f996807248be1aff60ec8a090fd570
SHA256 = 3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
ZIP ↔ current main = PASS
PNG integrity = PASS
known defect = overlong ear tendency in current reference
```

These images remain audit/authority context, but **they are not supplied to Codex generation in the current text-only phase**.

## 4. Current text-only fixed condition

Appearance specification:

```text
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
current starting Git blob SHA = b5565b10c1ba68bed3720fbc5360f0f7925799e9
```

Codex generation appearance input must be this Visual Text only.

Allowed extra generation text is limited to the operational test envelope:

```text
view
crop
single character
neutral pose / expression
eye-level camera
plain background
DIAGNOSTIC / CANDIDATE status
```

Do not add YURA appearance rescue wording outside the Visual Text.

## 5. Hard generator boundary

Current Codex validation phase:

```text
Codex-native image generation = USE
OpenAI Image API = FORBIDDEN
OPENAI_API_KEY = NOT USED
YURA image references = NONE
```

If Codex-native image generation is unavailable, STOP rather than silently falling back to OpenAI or another generator.

The previous `run_visual_ambiguity_reference_once.py` OpenAI/image-reference route is disabled and is not part of the current pipeline.

## 6. Baseline five-view test

Generate and inspect one image at a time:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

Primary purpose:

```text
Visual Text strength
view behavior
ear elongation / inflation suppression
ear visibility-compensation suppression
natural hair-over-ear behavior
initial rear-hair diagnostic behavior
```

All outputs remain:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

## 7. Inspection rule

Record for each image:

```text
view achieved
YURA-like text-only identity
ear elongation / inflation
ear outward projection
visibility compensation
hair-clearing-for-ear behavior
naturalness
rear-hair note where applicable
```

Minor unrelated awkwardness is tolerable in this early diagnostic phase if the tested ambiguity behavior is clearly improved and the output remains interpretable.

A qualifying ear result requires no CLEAR elongation/inflation, no CLEAR outward/visibility compensation, and no forced hair clearing solely to expose the ear.

## 8. Repeated-result transfer gate

After the five-view baseline:

```text
primary repeat condition = FRONT_3Q
Visual Text = unchanged
qualifying FRONT_3Q required = 3 total
SIDE baseline = no major ear elongation / outward-projection failure
```

The baseline FRONT_3Q counts if it qualifies.

Any material edit to `YURA_VISUAL_TEXT.md` resets the qualifying count to zero and creates a new fixed condition.

If the spec is weak, strengthen the Visual Text rather than patching individual images or adding ad-hoc rescue prompt wording.

## 9. OpenAI transfer checkpoint

Only after the Codex repeatability gate passes:

```text
generator = OpenAI image generation
appearance input = YURA_VISUAL_TEXT.md only
image reference = NONE
first test = Face-up Pilot 1
```

This is a separate phase and requires its own execution route. Do not reuse the disabled image-reference ambiguity runner.

The first OpenAI Face-up remains diagnostic; it tests whether the text-only behavior transfers between generators.

## 10. Ambiguity classification

Existing source classes:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

Ambiguity classes:

```text
MEASURED_VISIBLE_FACT
MEASURED_OCCLUSION_FACT
ESTIMATED_HIDDEN_GEOMETRY
AUTHOR_INTENT
VIEW_SPECIFIC_RULE
NON_COMPENSATION_RULE
```

Keep ACTUAL / STRUCTURAL GEOMETRY, VISIBLE GEOMETRY, OCCLUSION / LAYER ORDER, and VIEW separate.

Unknown hidden structure remains unknown.

## 11. Ear and rear-hair checkpoints

Current working ear rule remains:

```text
ear actual height target = 20–22% face vertical dimension
HARD MAX = 23%
ear visibility lower priority than natural size / placement
no visibility compensation
```

Detailed ear work after the OpenAI transfer checkpoint separates:

```text
EAR ACTUAL GEOMETRY
EAR VISIBLE GEOMETRY
HAIR OCCLUSION
```

Current Hair AUTHOR_OVERRIDE remains:

```text
SUPER-LONG mandatory
must clearly reach waist area
ordinary-long / mid-back = FAIL
modestly longer than Sample 9
not substantially below waist
```

Rear-hair / back-view geometry remains unresolved until its dedicated phase.

## 12. Current execution state

```text
Formal Sample 9 Master                    = COMPLETE
Full-body pixel measurement V1            = COMPLETE
Visual Ambiguity Protocol                 = ACTIVE / AUTHOR APPROVED
Codex text-only generation spec           = COMPLETE
Codex execution instruction               = COMPLETE
Old OpenAI/image-reference ambiguity runner = DISABLED
Codex five-view baseline                  = NEXT
Codex repeated FRONT_3Q qualification     = NOT YET
Codex -> OpenAI transfer gate             = NOT YET
OpenAI text-only Face-up Pilot 1          = NOT YET
Detailed ear correction                   = AFTER TRANSFER CHECKPOINT
Rear-hair / back-view correction          = AFTER EAR
Formal Face Master                        = NOT YET
Production Visual MD                      = NOT YET
```

## 13. Exact next action

Use:

`tools/yura-master-benchmark/codex_instruction_visual_ambiguity_reference.md`

In Codex, generate **FRONT first using `YURA_VISUAL_TEXT.md` as the only YURA appearance input**, save the image, inspect it, and only then continue to `FRONT_3Q`.

Do not call OpenAI image generation during this phase.

## 14. Repository safety

```text
no git reset --hard
no force-push
no unrelated file changes
no story/manuscript/Memory appearance as Visual Authority
no reactivation of Test 5/6 generation routes
no bypass of the text-only Codex gate with image-reference rescue
```
