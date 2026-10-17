# YURA Visual Work — WORKFLOW

Status: **AUTHOR-DIRECTED CURRENT WORKFLOW / PROJECT-MANAGEMENT ONLY / NOT VISUAL AUTHORITY**

## Governing principle

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md` is the absolute YURA visual text authority.

This workflow controls sequencing only. It must not redefine appearance.

## Phase 1 — Ear Geometry Master / free GPT

Goal: remove ear visibility-compensation behavior before normal hair is involved.

Generation type:

```text
free GPT image generation
single image
face-up / front
hairless diagnostic presentation
neutral expression
```

Required visual sources:

```text
YURA_VISUAL_TEXT.md
YURA_FACE_REDESIGN_SPEC.md
YURA_EAR_BASIC_RULES.md
```

Do not attach the legacy Face Reference or Body Geometry Guide in this phase.

Hairless presentation is allowed only to inspect the complete ear geometry. It must not alter the approved face.

PASS requires, at minimum:

```text
approved face identity preserved
ear actual height within target / hard max
ear vertically compact
ear close to head
no outward flare
no camera-facing rotation
no geometry added merely for readability
```

A PASS image is promoted only by explicit author instruction to:

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

## Phase 2 — Face-up Master / free GPT

Only after the Ear Geometry Master is approved.

Generate the normal YURA face-up with hair restored.

Inputs:

```text
YURA_VISUAL_TEXT.md
YURA_FACE_REDESIGN_SPEC.md
YURA_EAR_BASIC_RULES.md
YURA_EAR_GEOMETRY_MASTER.png
```

Primary ear behavior:

```text
correct actual geometry
natural hair occlusion
no visibility compensation
partial or zero visible ear is acceptable
```

Face geometry must remain unchanged from the approved face design.

A PASS image is promoted only by explicit author instruction to:

`visuals/yura/identity/face/YURA_FACE_UP_MASTER.png`

## Phase 3 — Face-up descriptive MD

After `YURA_FACE_UP_MASTER.png` is approved, visually inspect the approved image and create:

`visuals/yura/identity/face/YURA_FACE_UP_MASTER.md`

Rules:

- describe only what is actually visible in the approved Face-up Master;
- do not invent hidden geometry;
- do not import novel settings;
- do not import rejected candidates;
- do not override `YURA_VISUAL_TEXT.md`;
- if a description conflicts with Visual Text, stop and report the conflict.

## Phase 4 — Full-body generation

Only after Face-up Master and its descriptive MD are complete.

The new full-body route must start from the current Visual Text and current approved face assets, not from the archived old full-body Master.

Before any full-body generation, explicitly re-resolve the visual-layer Body Geometry Guide because the protected `YURA_VISUAL_TEXT.md` currently names that asset. Do not use the archived tools copy as an automatic reference. If the author changes the Body Geometry route before this phase, update the active specification deliberately rather than letting project-management prose override Visual Text.

Mandatory preserved design constraints include:

```text
face geometry unchanged
compact / petite overall impression
7.0–7.2 head target from current Visual Text
no whole-body vertical stretching
no torso-only or leg-only elongation
slender but not excessively frail body
current chest-to-frame relationship preserved
```

The chest specification is evaluated as body-design silhouette / volume balance only. Do not turn the generation or QA into sexual emphasis.

The generation engine for this full-body phase is chosen later by the author.

If a paid route is used, every run, prompt compile, hypothesis, cost artifact, candidate record, and result belongs under `tools/`, not under `visuals/`.

## Rejection rule

A FAIL image:

```text
is not Authority
is not a Master
is not a future identity reference
must not be fed back automatically
```

## One change at a time

When diagnosing a specific failure, change only the minimum intended variable. Do not combine face redesign, ear correction, body correction, rendering change, and composition correction into one uncontrolled test.
