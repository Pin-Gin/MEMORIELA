# YURA Visual Work — DECISIONS

Status: **CURRENT AUTHOR DECISIONS / PROJECT-MANAGEMENT RECORD / NOT VISUAL AUTHORITY**

This file records decisions so a new chat does not re-open settled direction by default.

## Authority decision

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md` is the active, highest-priority YURA visual text authority and must be followed.

It remains unchanged by this repository cleanup.

## Face decision

The face selected in the 2026-10-17 redesign work is the current formal face direction.

The detailed current specification remains:

`visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md`

Legacy Face Reference geometry is not current face authority and must not be blended back into the new design.

Face geometry must not be altered to solve later body, proportion, ear, or generation problems.

## Ear decision

Ear visibility must never be improved by making the ear longer, larger, farther outward, more camera-facing, or by clearing natural hair.

The current focused ear rules are:

`visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md`

First create a hairless structural ear Master; then use that approved geometry when creating the normal-hair Face-up Master.

## Body / chest decision

The current chest specification inside `YURA_VISUAL_TEXT.md` is retained.

Key design intent:

```text
slender body
chest moderately fuller relative to the frame
natural soft bowl-like rounded form
compact / relatively high-set volume
upper-chest volume retained
not flattened because the body is slender
not exaggerated oversized
```

This is character-design and body-balance verification.

Do not add age-category wording to generation instructions as a workaround for this body-design requirement.

Do not sexualize the presentation, pose, camera, clothing, or QA focus.

## Body proportion decision

Do not solve head-to-body ratio by stretching the entire body.

Do not:

- lengthen the face;
- shrink or redesign the approved face;
- lengthen only the torso;
- lengthen only the legs;
- enlarge shoulders / skeleton / ribcage merely to reach a ratio;
- create a tall model-like silhouette.

Follow the current `YURA_VISUAL_TEXT.md` target and preserve the compact YURA impression.

## Layer ownership decision

```text
visuals/**
= current visual specifications and author-approved visual Masters

tools/**
= paid generation code, runs, prompts, hypotheses, QA experiments, costs, historic generation outputs

project-management/yura-visual/**
= current progress, sequencing, handoff, settled decisions

novel/story layer
= never a YURA visual fallback
```

## Legacy decision

The previous Face Reference, Body Guide, Sample-9 full-body Master, measurement records, audits, and candidate records are historical only.

They may be kept under tools for audit / provenance but are denied as current visual-generation authority.

## Protected old sequencing documents

Older files that encode repository read order / phase sequence are intentionally left byte-identical when protected by the author's instruction.

They may contain stale historical references after the cleanup.

Do not treat those stale references as permission to reactivate archived visual assets or old paid routes.

Do not edit or delete those protected sequencing documents without a new explicit author instruction.

## Paid generation decision

The old paid route must remain disabled until the current free ear / Face-up Master sequence is complete and the author explicitly requests a new paid-route build.

Do not pay for a run merely because old runner scripts still exist in Git history or archive.
