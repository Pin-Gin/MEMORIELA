# YURA Visual Work — START HERE


> **2026-10-20 AUTHOR CORRECTION — GIT MASTER BINARY MISMATCH / MIGRATION PENDING.** The author has designated an exact original Full-body Master PNG with SHA-256 `07e26596642f4953393f1f09d3d5a0923627f532c8ff1b8b85595ae9058503e3` as canonical. Git currently holds the old `CCBE315...` binary at both full-body paths. Until the two PNGs are actually replaced and docs/config reconciled, **do not mistake the old Git PNG, old preflight PASS, or older promotion status for verification of the newly designated original**. READ FIRST: `project-management/yura-visual/FULL_BODY_MASTER_HASH_CORRECTION_PENDING.md`. Paid route remains frozen; do not trigger billable generation.

Status: **CURRENT CROSS-CHAT HANDOFF / FULL-BODY MASTER PROMOTED / PAID ROUTE FROZEN**

This directory is the project-management handoff layer for YURA visual work. It does not define appearance; current appearance authority remains under `visuals/**`.

**ACTIVE NEXT TASK (2026-10-18):** YURAの表情差分17種（E01〜E17）のFace-up画像マスター制作。新規チャットは、下記の**作者確定3感情要素・17種一覧・品質ゲート・DoD**の引継ぎ仕様を、画像生成前に必ず全文読む。

`project-management/yura-visual/YURA_EXPRESSION_VARIATIONS_17_HANDOFF.md`

E00の真顔は既存Face Referenceであり新規生成対象外。表情定義はE00〜E17の18種、**新規制作する画像は17種**。感情定義は17/17確定、画像は現時点で0/17作者PASS。正式Face GeometryとMatte Natural Animeの品質は変更禁止。


## 1. Purpose

A new chat should be able to recover, without relying on chat memory:

- what has already been completed;
- which files are the current Authorities;
- the method used to reach the current state;
- the current validation standards;
- what is normal future use versus recovery-only tooling;
- what must not be reopened or changed by default.

Novel/story material is never a fallback visual source for YURA.

## 2. Completion state

```text
Ear Geometry Master            = DONE / AUTHOR PASS / PROMOTED
Face-up Master                  = DONE / AUTHOR PASS / PROMOTED
Face-up descriptive MD          = DONE / ACTIVE
Full-body generation            = DONE
7.0–7.2 head-ratio validation   = PASS on promoted result
Official Full-body Master       = DONE / AUTHOR PASS / PROMOTED
7.0-head Body Geometry Guide    = DONE / SUPPORT-ONLY RECOVERY REFERENCE
paid batch                      = NOT EXECUTED / NOT REQUIRED
paid generation                 = STOPPED BY AUTHOR
recovery paid route             = FROZEN / FAIL-CLOSED
recovery preflight              = VERIFIED PASS / 0 paid model calls
```

The latest verified recovery preflight was run against Git commit:

`690218017a0c3dedba7f34907b97454a53643e41`

with:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
paid_generation_allowed = false
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
authority_count = 8
```

## 3. Current visual Authority map

Highest YURA visual text authority:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

Primary integrated full-body visual Master:

`visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png`

Body-directory synchronized copy:

`visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png`

Face-local Authorities:

```text
visuals/yura/identity/face/YURA_FACE_REFERENCE.png
visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md
```

Ear-local Authorities:

```text
visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
```

Body recovery support only:

`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

The Body Geometry Guide is not a replacement for the official Full-body Master and must not override the Master, Face Authorities, Ear Authorities, or current Visual Text.

## 4. Verified promoted assets

Official Full-body Master:

```text
promotion commit = 3ce89e33193effa627ea794e803d9a3b50cb085b
SHA-256 = CCBE315659DAC02169C833F8140096322725E85250FAB73214D30FBBC835EDF1
```

Current 7.0-head Body Geometry Guide:

```text
SHA-256 = C23D1D2C348102B4ED9D75C422E1C2323800565B94E27A7FF13AF7C624EBDF95
```

## 5. Current standard

```text
TARGET HEAD COUNT RANGE = 7.0–7.2 heads
TARGET HEIGHT IMPRESSION = 152–153 cm
ONE HEAD = structural skull top / crown to chin
VISIBLE HAIR VOLUME != SKULL HEIGHT
```

Do not solve head ratio by face elongation, torso-only elongation, leg-only elongation, shoulder widening, ribcage enlargement, or conversion to a tall model-like body.

Face Geometry, eye geometry and placement, pupil bilateral symmetry, ear geometry, body definition, chest-to-frame relationship, and the promoted integrated Full-body Master proportions remain locked.

## 6. Normal future use

For ordinary full-body derivative work such as temporary clothing changes:

```text
primary reference = visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
```

The camisole and shorts shown in the Master are validation clothing, not permanent wardrobe Authority. Preserve the approved body / identity and replace clothing only as explicitly requested.

### Default when the author says 「ラフな服装」 (2026-10-21)

For ordinary derivative image generation, read:

`visuals/yura/generation/profiles/YURA_HOME_CASUAL_B_PROFILE.md`

This is the author's selected **home-casual outfit B default** (light ice-blue long loose open cotton-knit cardigan, white opaque sleeveless cotton top with subtle frill and small blue bow, pale-blue woven-fabric half-pants with white piping, barefoot). Apply it to **clothing only** whenever the user says 「ラフな服装」 without another outfit specification. Preserve the official YURA body and identity; explicit user overrides take priority. The outfit is currently a generation default / provisional design, **not** a promoted outfit Master image. This entrypoint must be read in future chats before interpreting that outfit request.

Use the Body Geometry Guide only when proportion / recovery support is actually needed.

## 7. Recovery / regeneration method

The retained recovery route is:

```text
current Git main
-> verify current Authority paths and SHA-256
-> verify primary Full-body Master and body-directory copy match
-> verify current Body Geometry Guide hash
-> build sealed Authority bundle
-> Codex prompt compile
-> manifest / invariant validation
-> OpenAI Image API
-> direct structural-crown / chin / soles head-ratio QA
-> explicit author visual QA
```

Current Image API recovery reference order is:

```text
1. visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
2. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
3. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
```

Paid execution is currently unauthorized. A future preflight may verify recovery integrity, but a successful preflight does not authorize a billable call.

## 8. Paid route state

```text
PAID_GENERATION_ALLOWED = NO
route_state = FROZEN_AFTER_FULL_BODY_MASTER_PROMOTION
```

Do not run paid generation unless the author explicitly reopens a Master-regeneration phase and the frozen config is deliberately reauthorized.

## 9. New-chat read order

For a new chat, read in this order:

```text
1. project-management/yura-visual/START_HERE.md
2. project-management/yura-visual/CURRENT_STATE.md
3. project-management/yura-visual/DECISIONS.md
4. project-management/yura-visual/WORKFLOW.md
5. visuals/yura/identity/master/YURA_VISUAL_TEXT.md
6. visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
7. visuals/yura/identity/face/YURA_FACE_UP_MASTER.md
8. visuals/yura/identity/face/YURA_FACE_REFERENCE.png
9. visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md
10. visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png
11. visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png   [when body proportion / recovery is relevant]
```

For paid-route recovery implementation only, additionally read:

```text
tools/yura-master-benchmark/CURRENT_HANDOFF.md
tools/yura-master-benchmark/PAID_ROUTE_STATUS.md
tools/YURA_MASTER_REPRODUCTION_RUNBOOK.md
tools/YURA_MASTER_GENERATION_CURRENT_STATE.md
tools/YURA_MASTER_GENERATION_WORKLOG.md
tools/yura-master-benchmark/config.json
tools/yura-master-benchmark/codex_instruction.md
```

## 10. Promotion rule

Generated images are candidates only. No candidate becomes a Master or visual Authority without explicit author PASS and repository promotion.
