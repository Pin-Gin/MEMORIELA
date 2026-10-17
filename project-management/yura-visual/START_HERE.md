# YURA Visual Work — START HERE

Status: **CURRENT HANDOFF ENTRYPOINT / PROJECT-MANAGEMENT ONLY / NOT VISUAL AUTHORITY**

## Purpose

This directory is the current cross-chat handoff and progress-management layer for YURA visual work.

It exists so a new chat can recover:

- the current objective;
- the current approved method;
- which visual sources are active for the current stage;
- which old sources are forbidden;
- what stage is next;
- what must not be changed.

This directory does **not** define YURA appearance. Visual appearance authority remains under `visuals/`.

## Repository layer separation

```text
Novel / story layer
  characters/**
  story/**
  manuscript/**
  rules/**

Visual specification layer
  visuals/**
  YURA appearance authority -> visuals/yura/**

Paid generation / experiment layer
  tools/**
  YURA paid-generation history / code / results -> tools/yura-master-benchmark/**

Progress / handoff layer
  project-management/yura-visual/**
```

Novel material must not be used as a fallback source for YURA image generation.

## Current active YURA visual authority

Highest authority:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

Current face detail specification required by that Visual Text:

`visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md`

Current focused ear support rule for the next stage:

`visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md`

The author-selected 2026-10-17 face redesign is the current formal face direction.

The legacy Face Reference is not a geometry source for the new face redesign.

The existing visual-layer Body Geometry Guide is still named inside the protected `YURA_VISUAL_TEXT.md`. It is **not needed for the current ear / Face-up phases**. Its role for the later full-body phase must be resolved against the then-current Visual Text before generation; this project-management layer must not override that Visual Text decision.

The old full-body Master is archived under tools and is not a current generation reference.

## Current restart read order

For a new chat continuing the current YURA visual work, read:

```text
1. project-management/yura-visual/CURRENT_STATE.md
2. project-management/yura-visual/DECISIONS.md
3. project-management/yura-visual/WORKFLOW.md
4. visuals/yura/identity/master/YURA_VISUAL_TEXT.md
5. visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md
6. visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md   [when doing ear/face work]
```

Then read only the additional visual files required by the active stage.

## Frozen legacy sequencing documents

Some older repository documents contain historical read orders / phase sequences. By author instruction, those documents are preserved without editing or deletion in this cleanup even when they contain stale historical paths.

They are **not** allowed to override the current Visual Text or this current handoff state.

Do not repair those frozen files by silently editing them.

## Paid generation state

The old paid YURA runner is not the current route and must not be used for a new paid generation condition.

Read:

`tools/yura-master-benchmark/PAID_ROUTE_STATUS.md`

Paid generation remains disabled until the current free ear/face Master sequence is completed and the author explicitly instructs reconstruction of the paid route.

## Promotion rule

Generated images are candidates only.

No image becomes a Master, Face-up Master, Ear Geometry Master, or other Visual Authority without explicit author PASS and repository registration.
