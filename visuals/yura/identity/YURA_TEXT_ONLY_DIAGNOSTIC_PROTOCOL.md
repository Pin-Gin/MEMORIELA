# YURA TEXT-ONLY DIAGNOSTIC PROTOCOL

Status: **AUTHOR-APPROVED / ACTIVE FREE VALIDATION ROUTE / NOT VISUAL AUTHORITY**

## 1. Purpose

This is the free / text-only validation route for YURA visual specification work.

Repository boundary:

```text
visuals/yura/identity/**
= text-only visual definition / ambiguity validation / diagnostic rules

tools/yura-master-benchmark/**
= paid-generation execution route after the text-only gate passes
```

Do not use the paid-generation tool route to perform the current text-only validation.

## 2. Generation source

For Codex diagnostic generation, YURA appearance comes from:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

Use **Visual Text only** as YURA appearance input.

Do not supply YURA image references during this phase.

Do not append appearance rescue wording from Face Reference, Master image, Detailed Part Spec, Ambiguity Protocol, Memory, story, manuscript, or past generated images.

Allowed extra generation instructions are presentation-only:

```text
requested view
crop
single character
neutral pose / expression
eye-level camera
plain background
DIAGNOSTIC / CANDIDATE ONLY
```

## 3. Generator boundary

Current phase:

```text
Codex-native image generation = USE
OpenAI paid image generation = DO NOT USE
YURA image reference = NONE
```

If Codex-native image generation is unavailable, stop. Do not silently substitute the paid route.

## 4. Baseline views

Generate one image at a time:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

Do not use a five-panel composite for the primary validation set.

## 5. Inspection

After each image, inspect at minimum:

```text
view achieved
YURA-like text-only identity
ear elongation / inflation
ear outward projection
visibility compensation
hair moved / cleared only to expose ear
naturalness
rear-hair behavior where applicable
```

Minor unrelated awkwardness is acceptable if the tested ambiguity behavior is clearly improved and the result remains diagnostically usable.

A qualifying ear-behavior result requires:

```text
no CLEAR ear elongation / inflation
no CLEAR outward-projection compensation
no CLEAR visibility-compensation behavior
no forced hair clearing solely to expose the ear
ear remains low-prominence and visually natural enough for diagnosis
```

This is an early behavioral gate, not the final numeric ear gate.

## 6. Repeatability gate

Primary repeat condition:

```text
view = FRONT_3Q
Visual Text = unchanged
```

Require:

```text
3 qualifying FRONT_3Q results total
+ SIDE result with no major ear elongation / outward-projection failure
```

The baseline FRONT_3Q may count if it qualifies.

A material edit to `YURA_VISUAL_TEXT.md` starts a new fixed condition and resets the qualifying count to zero.

If a weakness is found, strengthen the Visual Text specification. Do not patch one output with ad-hoc rescue wording.

## 7. PASS -> paid generation boundary

Only after the text-only repeatability gate passes:

```text
TEXT-ONLY GATE = PASS
-> switch to tools/yura-master-benchmark paid-generation route
-> first paid check = OpenAI text-only Face-up Pilot 1
-> appearance input = YURA_VISUAL_TEXT.md only
-> image reference = NONE
```

The paid Face-up Pilot remains diagnostic. It tests whether the text-only behavior transfers to the paid generator.

Do not activate image-reference rescue before this transfer check.

## 8. Authority status

All Codex text-only diagnostic outputs remain:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

PASS validates specification strength and repeatability. It does not by itself promote a Face Master, ear geometry, or rear-hair structure.
