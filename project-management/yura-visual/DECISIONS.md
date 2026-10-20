# YURA Visual Work — DECISIONS


> **2026-10-20 AUTHOR CORRECTION — GIT MASTER BINARY MISMATCH / MIGRATION PENDING.** The author has designated an exact original Full-body Master PNG with SHA-256 `07e26596642f4953393f1f09d3d5a0923627f532c8ff1b8b85595ae9058503e3` as canonical. Git currently holds the old `CCBE315...` binary at both full-body paths. Until the two PNGs are actually replaced and docs/config reconciled, **do not mistake the old Git PNG, old preflight PASS, or older promotion status for verification of the newly designated original**. READ FIRST: `project-management/yura-visual/FULL_BODY_MASTER_HASH_CORRECTION_PENDING.md`. Paid route remains frozen; do not trigger billable generation.

Status: **CURRENT AUTHOR DECISIONS / POST-PROMOTION HANDOFF / NOT VISUAL AUTHORITY**

This file records settled author decisions so a new chat does not reopen completed direction by default.

## 1. Authority decision

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md` is the active highest-priority YURA visual text authority.

The current official integrated full-body visual Master is:

`visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png`

Project-management documents may not override these visual Authorities.

## 2. Full-body Master decision

The author explicitly promoted the current Full-body Master.

```text
path = visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
promotion commit = 3ce89e33193effa627ea794e803d9a3b50cb085b
SHA-256 = CCBE315659DAC02169C833F8140096322725E85250FAB73214D30FBBC835EDF1
```

Synchronized body-directory copy:

`visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png`

The two files are the same Master binary and are not competing Authorities.

The validation camisole / shorts visible in the Master are not permanent wardrobe Authority.

## 3. Face decision

Current face image Authority:

`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

Current face text Authorities:

```text
visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md
```

The current Face Reference is repository-promoted and active. Do not fall back to older face geometry from archived candidates or Git history.

Face geometry must not be altered to solve body ratio, ear visibility, or generation problems.

Current eye placement remains:

```text
C2 baseline -> 0.3% inward
```

Pupil bilateral symmetry remains required.

## 4. Ear decision

Current ear image Authority:

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

Current supporting rule:

`visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md`

Approved Ear Geometry Master SHA-256:

`8949c5febef99850f7cccd849064c9dfe774e3b722f1658c967b0ecf2c5c7b50`

Ear visibility is not required. Natural hair may fully hide one or both ears.

Do not improve readability by lengthening, widening, moving outward, rotating, exposing, or clearing hair around the ear.

## 5. Body / chest decision

The body and chest definition in `YURA_VISUAL_TEXT.md` remains locked.

Key intent:

```text
slender overall frame, not excessively frail
relatively narrow shoulders / waist
natural soft hips / thighs
chest moderately fuller relative to the slender frame
natural soft bowl-like rounded form
compact / centered
slightly high-set with natural upper volume
not flattened because the body is slender
not exaggerated oversized
```

This is character-design and body-balance verification. Do not sexualize pose, camera, clothing, or QA focus.

## 6. Body Geometry Guide decision

The previous obsolete Body Geometry Guide was removed and replaced by a newly generated 7.0-head mannequin reference aligned with current YURA body intent.

Current path:

`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

Current SHA-256:

`C23D1D2C348102B4ED9D75C422E1C2323800565B94E27A7FF13AF7C624EBDF95`

Its role is deliberately limited to:

```text
7.0-head proportion reference
body-geometry recovery support
insurance for future Full-body Master regeneration
```

It is not the primary YURA visual reference and must not override the official Full-body Master, Visual Text, Face Authorities, or Ear Authorities.

## 7. Body proportion decision

Current target:

```text
7.0–7.2 heads
152–153 cm height impression
```

Head measurement uses structural skull top / crown to chin. Visible hair volume is not skull height.

Do not reach the ratio by:

- lengthening the face, midface, lower face, or chin;
- torso-only elongation;
- leg-only elongation;
- enlarging shoulders, skeleton, or ribcage;
- tall model-like conversion.

Whole-head physical scale relative to the body may be adjusted only as one intact unit when regeneration requires it; internal face geometry must remain unchanged.

## 8. Full-body QA decision

For head-count QA, measure directly from the generated image using:

```text
structural crown / skull top
chin
soles
```

Do not require `body_geometry_qa.json` merely to decide head count when the image itself can be measured directly.

The promoted Full-body Master passed the intended 7.0–7.2 range before author promotion.

## 9. Paid generation decision

The Full-body Master-generation phase is complete and the author stopped further paid generation.

```text
PAID_GENERATION_ALLOWED = NO
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
```

No paid batch was executed.

The recovery runner remains in Git only as frozen regeneration tooling and must fail closed before billable Codex / Image API execution while authorization is false.

A future successful preflight does not itself authorize billing.

## 10. Recovery method decision

If the author explicitly reopens Master regeneration, the current recovery reference order is:

```text
1. visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
2. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
3. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
```

The route must verify current Git, hashes, Authority order, sealed bundle, prompt invariants, and the synchronized body-directory Master copy before any generation.

## 11. Normal derivative-use decision

For temporary clothing changes or other ordinary full-body derivatives, use the official Full-body Master as the primary integrated visual reference.

Change only the explicitly requested derivative variable. Do not use the Body Geometry Guide alone as a substitute for YURA identity.

### 2026-10-21: Default for 「ラフな服装」

Author selected home-casual B outfit as the **default clothing specification for subsequent generations** using the unqualified prompt 「ラフな服装」. Full detail and explicit material choices are recorded in:

`visuals/yura/generation/profiles/YURA_HOME_CASUAL_B_PROFILE.md`

Key choices: loose long open-front ice-blue **lightweight cotton-knit** cardigan (hem above shorts hem); **opaque white sleeveless cotton** top with soft frill and small pale-blue bow; **soft woven-fabric pale-blue half-pants** with thin white piping; **bare feet**. Palette: blue + white. User-specific costume details override this default. Design remains **provisional / no promoted outfit Master**. Body, face, hair identity, chest placement and proportion Authorities remain unchanged.

## 12. Layer ownership decision

```text
visuals/**
= current visual specifications and author-approved visual Masters

tools/**
= paid generation code, runs, prompts, QA, costs, historical and recovery tooling

project-management/yura-visual/**
= current progress, decisions, workflow, cross-chat handoff

novel/story layer
= never a YURA visual fallback
```

## 13. Promotion / rejection decision

Generated images are candidates only.

Explicit author PASS and repository registration are mandatory for promotion.

A rejected image is not Authority, not a Master, and must not be automatically fed back as identity reference.
