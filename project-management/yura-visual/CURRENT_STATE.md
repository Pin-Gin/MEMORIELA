# YURA Visual Work — CURRENT STATE

Status: **ACTIVE / EAR GEOMETRY MASTER AUTHOR-PASS / BINARY PROMOTION PENDING**

## Current objective

Rebuild the YURA visual pipeline around the current author-approved face design and the current `YURA_VISUAL_TEXT.md`, while removing old paid-generation outputs and old experimental records from the active visual layer.

## Current authority state

```text
YURA_VISUAL_TEXT.md
= ACTIVE / HIGHEST YURA VISUAL TEXT AUTHORITY / MUST FOLLOW

YURA_FACE_REDESIGN_SPEC.md
= CURRENT AUTHOR-APPROVED FACE DETAIL SPEC / NEW FACE DIRECTION

YURA_EAR_BASIC_RULES.md
= SUPPORTING RULE FOR CURRENT EAR MASTER WORK
```

## Current face decision

The face selected in the 2026-10-17 redesign work is the current formal face direction.

Do not restore the legacy Face Reference geometry by averaging, blending, or fallback.

Do not lengthen the face, lengthen the midface, lengthen the chin, narrow the cheeks, shrink the eyes, or otherwise reinterpret the approved face to satisfy later body or generation constraints.

The legacy Face Reference file remains at its old visual-layer path only because the protected Visual Text still names that path. It is not a geometry source for the current face redesign.

## Current Ear Geometry Master decision

The final hairless ear-geometry candidate has received explicit author **PASS**.

Approval record:

`project-management/yura-visual/EAR_GEOMETRY_MASTER_APPROVAL.md`

Approved target path:

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

Approved source SHA-256:

`8949c5febef99850f7cccd849064c9dfe774e3b722f1658c967b0ecf2c5c7b50`

Accepted result:

- ear size and position = PASS;
- no visibility-driven vertical elongation;
- no visibility-driven outward projection;
- current face geometry / eyes / cheeks / chin retained;
- slightly compacted upper cranium accepted.

Author approval is fixed. Repository binary promotion is still pending until the exact approved PNG is present at the target path and verified.

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
Ear Geometry Master    = AUTHOR APPROVED / BINARY PROMOTION PENDING
active full-body Master for new route = NONE
active Face-up Master   = NONE
```

The old full-body Master has been removed from the active visual layer and archived under tools.

## Next exact task

1. Place and verify the exact approved binary as:
   `visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`
2. Then use the approved Ear Geometry Master + current `YURA_VISUAL_TEXT.md` + current face specification to create the **normal-hair Face-up candidate** with free GPT image generation.
3. Author PASS -> promote to `YURA_FACE_UP_MASTER.png`.
4. Create `YURA_FACE_UP_MASTER.md` from the approved Face-up image.
5. Only then proceed to the full-body generation phase.

For the Face-up stage, do not use the legacy Face Reference, Body Geometry Guide, or archived full-body Master as an image input.

## Promotion sequence

```text
Hairless ear-geometry candidate
-> AUTHOR PASS [DONE]
-> YURA_EAR_GEOMETRY_MASTER.png [BINARY PROMOTION PENDING]

Ear Geometry Master + YURA Visual Text
-> normal-hair Face-up candidate
-> author PASS
-> YURA_FACE_UP_MASTER.png
-> create YURA_FACE_UP_MASTER.md from the approved image

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
