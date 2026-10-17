# YURA Visual Work — DECISIONS

Status: **CURRENT AUTHOR DECISIONS / PROJECT-MANAGEMENT RECORD / NOT VISUAL AUTHORITY**

This file records decisions so a new chat does not re-open settled direction by default.

## Authority decision

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md` is the active, highest-priority YURA visual text authority and must be followed.

It remains unchanged by this repository cleanup.

Project-management documents may not override it.

## Face decision

The face selected in the 2026-10-17 redesign work is the current formal face direction.

The detailed current specification remains:

`visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md`

Legacy Face Reference geometry is not current face authority and must not be blended back into the new design.

Face geometry must not be altered to solve later body, proportion, ear, or generation problems.

The legacy Face Reference file remains physically present at its visual-layer path only because the protected Visual Text still names that path. Its presence is not permission to use it as geometry for the current face redesign.

## Ear decision

Ear visibility must never be improved by making the ear longer, larger, farther outward, more camera-facing, or by clearing natural hair.

The current focused ear rules are:

`visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md`

The final hairless ear-geometry candidate received explicit author **PASS** on 2026-10-17.

Approval record:

`project-management/yura-visual/EAR_GEOMETRY_MASTER_APPROVAL.md`

Promoted Master path:

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

Approved source SHA-256:

`8949c5febef99850f7cccd849064c9dfe774e3b722f1658c967b0ecf2c5c7b50`

Repository promotion is complete and verified.

```text
promotion commit = c0878854937103236a2902abf80912182f191ead
Git blob SHA      = efba2f34097c4fa6e3f2a45e66a235da57253e3f
```

Accepted ear-stage geometry includes:

- ear size = PASS;
- ear position = PASS;
- no visibility-driven vertical elongation;
- no visibility-driven outward projection;
- the final slightly compacted upper-cranium result is accepted;
- the approved current face geometry / eyes / cheeks / chin remain the reference state for this structural Master.

The next normal-hair Face-up candidate must use this promoted Ear Geometry Master together with the current Visual Text and face specification.

## Body / chest decision

The current body and chest specification inside `YURA_VISUAL_TEXT.md` is retained.

Key chest design intent:

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

## Body Geometry Guide status

The current protected Visual Text still explicitly names:

`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

Therefore this progress layer does **not** declare that asset deleted, superseded, or inactive for every future purpose.

Current decision is narrower:

- it is not an input for the current hairless ear phase;
- it is not an input for the current normal-hair Face-up phase;
- an audit copy is stored under tools for provenance;
- before full-body generation, its role must be resolved from the then-current Visual Text and explicit author instruction.

Do not use the archived tools copy as a shortcut or alternate Authority.

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

The previous full-body Master, old measurement records, audits, and candidate records are historical only and are archived under tools.

Legacy Face Reference and Body Guide audit copies also exist under tools for provenance, but their visual-layer compatibility copies are handled only according to the protected Visual Text and current stage rules above.

## Protected old sequencing documents

Older files that encode repository read order / phase sequence are intentionally left byte-identical when protected by the author's instruction.

They may contain stale historical references after the cleanup.

Do not treat those stale references as permission to reactivate archived visual assets or old paid routes.

Do not edit or delete those protected sequencing documents without a new explicit author instruction.

## Paid generation decision

The old paid route must remain disabled until the current free ear / Face-up Master sequence is complete and the author explicitly requests a new paid-route build.

Do not pay for a run merely because old runner scripts still exist in Git history or archive.
