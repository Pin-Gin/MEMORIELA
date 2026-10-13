# YURA Master / Production Pipeline State

Status: **FORMAL SAMPLE 9 MASTER / FULL-BODY PIXEL V1 COMPLETE / CODEX TEXT-ONLY AMBIGUITY VALIDATION ACTIVE**

This file records operational state. It is not Visual Authority.

## Fixed baseline

```text
Formal full-body Master = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
Master SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
full-body pixel measurement V1 = COMPLETE

Face Reference = visuals/yura/identity/face/YURA_FACE_REFERENCE.png
Face Git blob SHA = 4c96c4ec42f996807248be1aff60ec8a090fd570
Face SHA256 = 3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
Face ZIP ↔ current main = PASS
Face PNG integrity = PASS
known issue = current Face Reference has overlong-ear tendency
```

These image assets remain authority/audit context, but they are not supplied to the current Codex text-only generation test.

## Governing ambiguity rule

`visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md`

Current generation spec:

`tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md`

Codex execution instruction:

`tools/yura-master-benchmark/codex_instruction_visual_ambiguity_reference.md`

## Current fixed condition

Appearance source:

```text
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
starting blob SHA = b5565b10c1ba68bed3720fbc5360f0f7925799e9
```

Generator boundary:

```text
Codex-native image generation = REQUIRED
OpenAI Image API = FORBIDDEN in this phase
OPENAI_API_KEY = NOT USED
YURA image reference = NONE
```

Allowed extra prompt content is presentation-only: requested view, crop, neutral pose/expression, plain background, single-character constraint, diagnostic status.

Do not append appearance rescue wording outside the Visual Text.

## Baseline five-view route

One image at a time:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

All outputs are:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

Primary observations:

```text
text-only YURA identity
view control
ear elongation / inflation
ear outward projection
visibility compensation
hair-clearing-for-ear behavior
naturalness
rear-hair behavior for rear views
```

Minor unrelated awkwardness is tolerable if the ambiguity behavior under test is meaningfully improved and the output is still diagnostically usable.

## Ear suppression qualification

A qualifying result has:

```text
no CLEAR ear elongation / inflation
no CLEAR outward-projection compensation
no CLEAR visibility-compensation behavior
no forced hair clearing solely to expose the ear
ear remains low-prominence and natural enough for diagnosis
```

This is an early behavior gate, not the final numeric ear gate.

## Repeatability gate

After the baseline:

```text
primary repeat condition = FRONT_3Q
Visual Text = unchanged
qualifying FRONT_3Q required = 3 total
baseline SIDE must have no major ear elongation / outward-projection failure
```

A material Visual Text edit resets the count to zero and begins a new fixed condition.

If a weakness is found, strengthen `YURA_VISUAL_TEXT.md` at the specification level and rerun; do not patch a single image with ad-hoc rescue wording.

## OpenAI transfer gate

Only after Codex repeatability passes:

```text
generator = OpenAI image generation
appearance input = YURA_VISUAL_TEXT.md only
image reference = NONE
initial test = Face-up Pilot 1
```

This later route is not yet active.

The old `run_visual_ambiguity_reference_once.py` OpenAI + image-reference route is disabled and must not be used to bypass the current Codex text-only phase.

## Classification / naturalness

Keep:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

and ambiguity labels:

```text
MEASURED_VISIBLE_FACT
MEASURED_OCCLUSION_FACT
ESTIMATED_HIDDEN_GEOMETRY
AUTHOR_INTENT
VIEW_SPECIFIC_RULE
NON_COMPENSATION_RULE
```

For occluded parts, keep ACTUAL/STRUCTURAL GEOMETRY, VISIBLE GEOMETRY, OCCLUSION/LAYER ORDER, and VIEW separate.

Acceptance ultimately requires:

```text
STRUCTURAL CONSISTENCY
IDENTITY CONSISTENCY
VISUAL NATURALNESS
```

## Ear state

Current working rule remains:

```text
ear actual height target = 20–22% face vertical dimension
HARD MAX = 23%
ear visibility lower priority than natural size / placement
no visibility compensation
```

Detailed ACTUAL / VISIBLE / HAIR OCCLUSION measurement/freeze follows the generator-transfer checkpoint.

## Hair state

Current AUTHOR_OVERRIDE:

```text
SUPER-LONG mandatory
must clearly reach waist area
ordinary-long / mid-back = FAIL
modestly longer than Sample 9
not substantially below waist
```

Rear-hair / back-view structure remains unresolved and follows detailed ear work.

## Current execution state

```text
Formal Sample 9 Master                      = COMPLETE
Full-body pixel measurement V1              = COMPLETE
Visual Ambiguity Protocol                   = ACTIVE / AUTHOR APPROVED
Codex text-only generation spec             = COMPLETE
Codex execution instruction                 = COMPLETE
OpenAI/image-reference ambiguity runner     = DISABLED
Codex FRONT baseline                        = NEXT
Codex FRONT_3Q baseline                     = NOT YET
Codex SIDE baseline                         = NOT YET
Codex REAR_3Q baseline                      = NOT YET
Codex BACK baseline                         = NOT YET
3x qualifying FRONT_3Q                      = NOT YET
Codex -> OpenAI transfer gate               = NOT YET
OpenAI text-only Face-up Pilot 1            = NOT YET
Detailed ear correction                     = AFTER TRANSFER CHECKPOINT
Rear-hair / back-view correction            = AFTER EAR
Formal Face Master                          = NOT YET
Production Visual MD                        = NOT YET
```

## Exact next action

In Codex, read:

`tools/yura-master-benchmark/codex_instruction_visual_ambiguity_reference.md`

Then generate the **FRONT** diagnostic image using `YURA_VISUAL_TEXT.md` as the only YURA appearance specification.

Inspect the image before generating the next view.

Do not call OpenAI image generation in this phase.
