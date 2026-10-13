# YURA Visual Ambiguity — Diagnostic Multi-View Reference Generation Spec

Status: **AUTHOR-DIRECTED / DIAGNOSTIC GENERATION SPEC / NOT VISUAL AUTHORITY**

Governing protocol:

`visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md`

## Purpose

Generate five independent waist-up diagnostic views so camera/view behavior, occlusion, ear visibility, and rear-hair layering can be inspected before ear and rear-hair correction is promoted.

These outputs are **DIAGNOSTIC / CANDIDATE only**.

They must not canonize:

```text
current overlong ear geometry
unsupported hidden ear geometry
unverified rear-hair structure
```

## Exact image inputs

Use only:

```text
1. visuals/yura/identity/master/YURA_VISUAL_MASTER.png
   role = formal full-body visual baseline

2. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
   role = Face Identity / face-local geometry only
   known defect = current ear elongation must not be promoted
```

Do not use Body Geometry Guide, old Masters, Test 5/6 images, past generated candidates, story/manuscript/characters appearance, Memory-derived appearance, or Git-history fallback images.

## Text rules to obey

```text
visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md
visuals/yura/identity/face/FACE_REFERENCE_RULES.md
visuals/yura/identity/face/YURA_FACE_MASTER_PHASE_PLAN_20261013.md
visuals/yura/identity/master/YURA_DETAILED_PART_SPEC.md
```

Current ear rule carried into diagnostics:

```text
ear actual height target = 20–22% face vertical dimension
HARD MAX = 23%
ear visibility lower priority than natural size / placement
no visibility compensation
```

Current Hair AUTHOR_OVERRIDE carried into diagnostics:

```text
SUPER-LONG mandatory
must clearly reach waist area
modest extension vs Sample 9 only
not substantially below waist
```

## Fixed diagnostic framing

For all five views:

```text
single character
waist-up reference view
entire head visible
waist region visible so total hair endpoint can be judged
neutral upright posture
neutral calm expression when face is visible
eye-level camera
minimal perspective distortion
plain unobtrusive background
no dramatic pose
no accessories added
no wind / hair-flare effect
no attempt to expose hidden anatomy
```

This crop is diagnostic and has no authority over full-body head count, BODY scale, or canvas occupancy.

## Five independent views

```text
01 FRONT
straight-on front view; head and torso facing camera

02 FRONT_3Q
30–45 degree front three-quarter view; head and torso share the same natural yaw

03 SIDE
true side/profile view near 90 degrees; head and torso share the same rotation

04 REAR_3Q
rear three-quarter view near 135 degrees; rear hair mass and side-layer ordering readable

05 BACK
true back view near 180 degrees; face not forced into view; rear hair mass, neck overlap, shoulder overlap, and endpoint readable
```

## Non-compensation invariants

Do not change structure merely to make it easier to see.

```text
DO NOT enlarge / elongate / widen ears for visibility.
DO NOT move ears outward or rotate them toward camera.
DO NOT move natural hair behind ears merely to expose ears.
DO NOT force equal left/right ear visibility.
DO NOT fan or spread rear hair away from neck/back merely to show layers.
DO NOT invent hidden 3D geometry and treat it as canonical.
```

Natural occlusion is valid.

## PASS definition for this phase

PASS here means **route/view-behavior PASS**, not visual-authority promotion.

Each view must satisfy:

```text
requested camera view is unambiguous
input/reference hashes are recorded
prompt is recorded
output PNG is recorded
no denied source is used
Face reference does not redefine BODY scale
no obvious visibility-compensation behavior is intentionally requested
output remains DIAGNOSTIC / CANDIDATE
```

Visual defects discovered in the diagnostic images are recorded for the later ear and rear-hair correction phases rather than silently repaired by changing the gate after generation.
