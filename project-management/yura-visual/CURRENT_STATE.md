# YURA Visual Work — CURRENT STATE

Status: **ACTIVE / EAR GEOMETRY MASTER PROMOTED / NORMAL-HAIR FACE-UP CANDIDATE NEXT**

## Current objective

Rebuild the YURA visual pipeline around the current author-approved face design and the current `YURA_VISUAL_TEXT.md`, while removing old paid-generation outputs and old experimental records from the active visual layer.

## Current authority state

```text
YURA_VISUAL_TEXT.md
= ACTIVE / HIGHEST YURA VISUAL TEXT AUTHORITY / MUST FOLLOW

YURA_FACE_REDESIGN_SPEC.md
= CURRENT AUTHOR-APPROVED FACE DETAIL SPEC / NEW FACE DIRECTION

YURA_EAR_BASIC_RULES.md
= SUPPORTING RULE FOR EAR / FACE-UP WORK

YURA_EAR_GEOMETRY_MASTER.png
= AUTHOR-PASS / VERIFIED / REPOSITORY PROMOTED
```

## Current face decision

The face selected in the 2026-10-17 redesign work is the current formal face direction.

Do not restore the legacy Face Reference geometry by averaging, blending, or fallback.

Do not lengthen the face, lengthen the midface, lengthen the chin, narrow the cheeks, shrink the eyes, or otherwise reinterpret the approved face to satisfy later body or generation constraints.

The legacy Face Reference file remains at its old visual-layer path only because the protected Visual Text still names that path. It is not a geometry source for the current face redesign.

## Current Ear Geometry Master decision

The final hairless ear-geometry candidate received explicit author **PASS** and has been promoted to the repository.

Approval record:

`project-management/yura-visual/EAR_GEOMETRY_MASTER_APPROVAL.md`

Promoted path:

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

Approved source SHA-256:

`8949c5febef99850f7cccd849064c9dfe774e3b722f1658c967b0ecf2c5c7b50`

Repository evidence:

```text
promotion commit = c0878854937103236a2902abf80912182f191ead
Git blob SHA      = efba2f34097c4fa6e3f2a45e66a235da57253e3f
```

Accepted result:

- ear size and position = PASS;
- no visibility-driven vertical elongation;
- no visibility-driven outward projection;
- current face geometry / eyes / cheeks / chin retained;
- slightly compacted upper cranium accepted.

The Ear Geometry Master phase is complete.

## Current body / chest decision

The body definition in `YURA_VISUAL_TEXT.md` remains active.

The chest relationship must remain the current author-approved design:

```text
slender overall frame
+
chest moderately fuller relative to that frame
+
natural soft rounded bowl-like silhouette
+
compact / relatively high-set volume
+
no flattening merely because the body is slender
+
no exaggerated enlargement
```

This is treated as **character-design / body-balance validation**, not as sexual emphasis.

Do not add age-category wording as a workaround for chest or body generation.

The current visual-layer Body Geometry Guide remains physically present because `YURA_VISUAL_TEXT.md` still names it. It is not used in the current ear / Face-up phases. Before the later full-body phase, its role must be resolved from the then-current Visual Text and explicit author direction. This project-management file does not supersede the Visual Text.

## Current generation state

```text
paid YURA route        = DISABLED / REBUILD REQUIRED
hairless ear candidate = AUTHOR PASS
Ear Geometry Master    = AUTHOR PASS / VERIFIED / REPOSITORY PROMOTED
normal-hair Face-up    = NEXT
active Face-up Master  = NONE
active full-body Master for new route = NONE
```

The old full-body Master has been removed from the active visual layer and archived under tools.

## Next exact task

Use free GPT image generation to create the **normal-hair Face-up candidate** using:

```text
visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
visuals/yura/identity/master/YURA_VISUAL_TEXT.md
visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md
visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
```

Requirements for this stage:

- restore YURA's normal silver-white super-long hair from the Visual Text;
- preserve the approved Ear Geometry Master head / face / ear structural geometry;
- natural hair occlusion may hide the ears;
- do not expose, lengthen, enlarge, move, or rotate the ears for readability;
- do not alter face geometry, eye placement, cheeks, jaw, chin, nose, or neutral-expression baseline;
- do not use the legacy Face Reference, Body Geometry Guide, or archived full-body Master as an image input.

After generation:

1. author review;
2. PASS -> promote to `YURA_FACE_UP_MASTER.png`;
3. create `YURA_FACE_UP_MASTER.md` from the approved image;
4. only then proceed to the full-body generation phase.

## Promotion sequence

```text
Hairless ear-geometry candidate
-> AUTHOR PASS [DONE]
-> YURA_EAR_GEOMETRY_MASTER.png [PROMOTED / VERIFIED]

Ear Geometry Master + YURA Visual Text + current Face Spec
-> normal-hair Face-up candidate [NEXT]
-> author PASS
-> YURA_FACE_UP_MASTER.png
-> create YURA_FACE_UP_MASTER.md

then
-> full-body generation phase
```

## Forbidden fallback

Do not use:

- legacy Face Reference as new-face geometry;
- archived old full-body Master;
- rejected generations;
- novel/story/manuscript appearance;
- memory-derived appearance;
- old Git history as active appearance authority.

Historic assets remain available under the tools archive for audit only.
