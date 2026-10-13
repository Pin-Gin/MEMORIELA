# YURA Visual Ambiguity — Codex Text-Only Diagnostic Generation Spec

Status: **AUTHOR-DIRECTED / DIAGNOSTIC GENERATION SPEC / NOT VISUAL AUTHORITY**

Governing protocol:

`visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md`

## Purpose

Test whether the current YURA Visual Text alone can suppress ambiguity failures before any OpenAI image-generation phase.

Primary near-term question:

```text
Can the current Visual Text repeatedly suppress ear elongation / inflation and visibility compensation without image references?
```

Rear-hair behavior is also observed in the five-view baseline, but is not frozen yet.

## Generation engine

Current phase:

```text
GENERATOR = Codex-native image generation
OPENAI IMAGE API = FORBIDDEN
OPENAI_API_KEY = NOT USED
```

If Codex-native image generation is unavailable in the execution environment, STOP and report that condition. Do not silently substitute OpenAI Image API or another generator.

## Appearance input — strict

The only YURA appearance specification passed for generation is:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

Do not provide these as image references:

```text
YURA_VISUAL_MASTER.png
YURA_FACE_REFERENCE.png
YURA_BODY_GEOMETRY_GUIDE.png
any old Master / candidate / Test 5 / Test 6 image
```

Do not add new YURA appearance prose outside the Visual Text during this phase.

The ambiguity protocol, handoff, measurement files, and Face Reference Rules may be read for workflow/QA, but they must not be copied into the appearance prompt. This phase is intentionally a Visual-Text-strength test.

## Allowed operational test envelope

The generation request may add only non-identity operational instructions:

```text
view
crop
one character
neutral upright pose
neutral calm expression when face is visible
eye-level camera
plain unobtrusive background
no dramatic action
DIAGNOSTIC / CANDIDATE ONLY
```

These instructions may control presentation but may not redefine YURA appearance.

## Baseline five-view set

Generate one image at a time:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

Do not use a five-panel composite for the primary test.

Recommended crop for the baseline set:

```text
waist-up
entire head visible
waist region visible when possible so long-hair behavior can be observed
```

## Inspection after every image

Record at minimum:

```text
view achieved: PASS / FAIL
YURA-like text-only identity: PASS / SOFT FAIL / FAIL
ear elongation / inflation: NONE / MILD / CLEAR
ear outward projection: NONE / MILD / CLEAR
visibility compensation: NONE / SUSPECTED / CLEAR
hair moved behind ear only to expose ear: NO / SUSPECTED / YES
naturalness: PASS / MINOR ISSUE / FAIL
rear-hair mass / silhouette note when applicable
```

Minor unrelated awkwardness may be accepted during this diagnostic phase if the tested ambiguity behavior is meaningfully improved and the image remains interpretable.

## Ear suppression threshold

A qualifying ear result requires:

```text
no CLEAR ear elongation / inflation
no CLEAR outward-projection compensation
no CLEAR visibility-compensation behavior
no forced hair clearing for ear exposure
ear remains low-prominence and visually natural enough for diagnosis
```

This is not yet the final numeric ear gate.

## Repeated-result transfer gate

After the five-view baseline:

1. `FRONT_3Q` is the primary repeat condition because it exposes both face identity and hair/ear interaction.
2. Keep `YURA_VISUAL_TEXT.md` unchanged.
3. Count the baseline `FRONT_3Q` if it qualifies.
4. Generate additional independent `FRONT_3Q` samples until there are **three qualifying FRONT_3Q results under the identical Visual Text condition**.
5. The baseline `SIDE` must also show no major ear elongation / outward-projection failure.

A material Visual Text edit resets the qualifying count to zero and begins a new fixed condition.

## If Codex reveals a weak specification

Do not patch the individual output.

Instead:

```text
identify the failure mode
-> strengthen YURA_VISUAL_TEXT.md at the specification level
-> record why the wording changed
-> restart the fixed condition
-> regenerate the five-view baseline or the affected minimum subset as appropriate
```

The goal is to strengthen weak specification, not to cherry-pick a lucky image.

## OpenAI transfer checkpoint

Only after the Codex repeated-result transfer gate passes:

```text
generator = OpenAI image generation
appearance input = YURA_VISUAL_TEXT.md only
image reference = NONE
first test = Face-up Pilot 1
```

The OpenAI Face-up Pilot tests whether the same text-only control transfers to the target generator.

Do not add the current Face Reference merely to rescue a weak text-only result.

## Diagnostic status

Every Codex baseline/repeat image and the first OpenAI transfer pilot remain:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

After transfer behavior is understood, proceed to detailed ear ACTUAL / VISIBLE / HAIR OCCLUSION work, then rear-hair / back-view mass / silhouette / layer-order work.
