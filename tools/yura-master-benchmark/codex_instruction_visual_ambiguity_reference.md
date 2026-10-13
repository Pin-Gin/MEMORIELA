# Codex Instruction — YURA Visual Ambiguity Text-Only Diagnostics

Use current `main` only.

## Read first

```text
tools/yura-master-benchmark/CURRENT_HANDOFF.md
tools/yura-master-benchmark/PIPELINE_STATE.md
visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md
tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
```

The current test is intentionally **text-only**.

## Hard execution boundary

During this Codex diagnostic phase:

```text
USE Codex-native image generation only
DO NOT call OpenAI Image API
DO NOT use OPENAI_API_KEY
DO NOT run Python code that imports `openai` for image generation
DO NOT use YURA image references
DO NOT silently fall back to another image generator
```

If Codex-native image generation is unavailable, STOP and report exactly that. Do not substitute another route.

## Appearance payload

For generation, YURA appearance must come from this file only:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

Do not append appearance corrections from:

```text
YURA_FACE_REFERENCE.png
YURA_VISUAL_MASTER.png
Body Geometry Guide
YURA_DETAILED_PART_SPEC.md
Face Reference Rules
Ambiguity Protocol
past generated images
Memory / story / manuscript / characters files
```

Those documents may be used only for workflow/inspection where applicable, not as extra YURA appearance prompt content.

## Allowed operational envelope

Add only the requested camera/test presentation:

```text
one YURA
requested view
waist-up crop for baseline views
entire head visible
neutral upright pose
neutral calm expression when face is visible
eye-level camera
plain unobtrusive background
no dramatic action
DIAGNOSTIC / CANDIDATE ONLY
```

Do not add ear-specific rescue wording outside the Visual Text. The purpose is to test whether the Visual Text already controls it.

## Phase A — five-view baseline

Generate and review **one image at a time** in this order:

```text
1. FRONT
2. FRONT_3Q
3. SIDE
4. REAR_3Q
5. BACK
```

Do not create one five-panel composite.

After every generation, save the image as an independent file and record:

```text
view achieved: PASS / FAIL
YURA-like text-only identity: PASS / SOFT FAIL / FAIL
ear elongation / inflation: NONE / MILD / CLEAR
ear outward projection: NONE / MILD / CLEAR
visibility compensation: NONE / SUSPECTED / CLEAR
hair moved behind ear only to expose ear: NO / SUSPECTED / YES
naturalness: PASS / MINOR ISSUE / FAIL
rear-hair note when applicable
```

Minor unrelated awkwardness is allowed at this stage if the ambiguity behavior is clearly improved and the output remains useful for diagnosis.

A qualifying ear result requires:

```text
no CLEAR ear elongation / inflation
no CLEAR outward-projection compensation
no CLEAR visibility-compensation behavior
no forced hair clearing for ear exposure
ear remains low-prominence and visually natural enough for diagnosis
```

If a major failure is found, STOP the fixed condition and report the weak Visual Text wording that likely needs strengthening. Do not patch the individual image or add ad-hoc prompt rescue text.

## Phase B — repeatability check

If the baseline is usable:

```text
primary repeat condition = FRONT_3Q
Visual Text = unchanged
```

Count the baseline FRONT_3Q if it qualifies, then generate additional independent FRONT_3Q images until there are:

```text
3 qualifying FRONT_3Q results total
```

Also require the baseline SIDE result to have no major ear elongation / outward-projection failure.

If `YURA_VISUAL_TEXT.md` changes materially, reset the qualifying count to zero and restart the fixed condition.

## Phase C — stop point

When the Codex transfer gate passes, STOP Codex generation and report:

```text
five-view baseline results
three qualifying FRONT_3Q results
SIDE ear check
exact Visual Text commit/blob used
all generated image paths
whether OpenAI transfer gate = PASS / FAIL
```

Do not call OpenAI image generation yourself in this phase.

The next author-approved phase is a separate OpenAI **text-only Face-up Pilot 1** using `YURA_VISUAL_TEXT.md` only and no image reference.

All generated images remain:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```
