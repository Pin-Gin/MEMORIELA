# YURA Image Generation Governance

Status: **CANONICAL / MANDATORY / PROTECTED IMAGE-GENERATION GOVERNANCE**
Adopted: 2026-09-13
Updated: 2026-09-20 — protected pixel + BODY geometry gates synchronized
Character: 久遠ゆら / YURA
Purpose: YURA画像生成における参照順・領域別正本・競合解決・生成前コンパイル・生成後QAを一本化し、チャット・派生画像・ポーズ・衣装・髪型・キャンバス変更によるブレを抑える。

This document is the **single parent rule for all YURA image generation**. It routes authority; it does not replace detailed domain specifications.

Project-wide reasoning authority:
`docs/assistant-context/AI_BEHAVIOR_CONTROL.md`

Canonical post-generation QA:
`docs/assistant-context/creation/yura/qa/GENERATION_QA.md`

Exact-preservation execution protocol:
`docs/assistant-context/creation/yura/generation/preservation/PIXEL_PRESERVATION_PROTOCOL.md`

Protected BODY geometry execution protocol:
`docs/assistant-context/creation/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

---

## 1. Absolute generation rule

Before material YURA generation, do not reconstruct YURA from chat memory, an arbitrary derivative, or one attractive prior image.

Use current Git authorities.

Generation architecture:

**PROJECT GOVERNANCE**
→ **IMAGE GENERATION GOVERNANCE**
→ **PROTECTED DOMAIN OWNERS**
→ **PROTECTED DOMAIN SUB-SPECS when applicable**
→ **TASK GUIDELINES / WORKFLOWS**
→ **CURRENT DERIVATIVE REQUEST**
→ **REFERENCES limited to assigned role**

After generation:

**GENERATED OUTPUT**
→ **YURA_GENERATION_QA**
→ **PASS / LOCAL REPAIR / TARGETED RETRY / REJECT**

A lower layer must not silently redefine a higher protected layer.

---

## 2. Conflict authority order

When information conflicts:

1. latest explicit user-confirmed **finalized** decision
2. `docs/assistant-context/AI_BEHAVIOR_CONTROL.md`
3. this governance
4. protected domain-owner specification
5. protected domain sub-specification inside its parent boundary
6. task-specific guideline / workflow
7. current derivative request
8. pose / composition / scene reference within assigned role
9. historical derivative / rejected candidate / legacy image / chat memory

Important:

- casual suggestion ≠ canon
- ordinary one-image request ≠ permanent spec change
- one-image protected-trait exception stays local unless explicitly promoted
- never average contradictory values
- a sub-spec may narrow implementation details but may not contradict its parent owner
- explicit user target ratio / placement may override a size profile's default ratio, but never BODY-safe framing invariants

---

## 3. Domain ownership matrix

### 3.1 Whole-character identity / visual cross-check

Owners:
- `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`
- `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png`

Current approved MASTER:

- gen_id: `e942a217-75fd-4154-88cc-6c0f74e99d82`
- Git blob SHA: `2c99257f5ae8c2c878f649dd97474d6860a8d689`
- role: neutral full-body whole-character visual identity + approved Normal Super-Long visual anchor

A more precise protected domain spec overrides incidental details in the MASTER inside that domain.

### 3.2 BODY / anatomy / proportion / scale

Owners:
- `docs/assistant-context/creation/yura/identity/body/BODY_MASTER.md`
- `docs/assistant-context/creation/yura/identity/body/BODY_SPEC.md`

Own:
- 153 cm scale concept
- exact 7.25-head ratio
- shoulders / ribcage / waist / pelvis
- bust proportion
- torso / leg proportion
- limb thickness
- hands / feet
- scale invariance

Outfit, camera, canvas, pose, scene, 3D reference and margin never redefine BODY.

### 3.3 FACE geometry / adult identity

Owner:
- `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md`

### 3.4 Protected pupil / eye signature

Owner:
- `docs/assistant-context/creation/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`

Owns the lower-right pupil-edge notch and resolution-aware visibility behavior.

### 3.5 HAIR core geometry / continuity

Owner:
- `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md`

Owns silver-white color, protected super-long source length, source mass, fine / soft strands, bangs, face framing, restrained lateral spread, gravity / contact behavior and back-view continuity.

Protected normal-down sub-spec:
- `docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`

Role:
- applies when no alternate arrangement is requested
- fixes ordinary Normal Super-Long I-line leaning silhouette
- fixes front/back mass distribution and normal tip treatment
- does not alter parent HAIR v1.3 core values

Current visual cross-check for the approved Normal Super-Long baseline:
- current `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png` / gen_id `e942...`

Validation workflow:
- `docs/assistant-context/creation/yura/qa/templates/NORMAL_SUPER_LONG_VALIDATION_TEMPLATE.md`


### 3.6 Hair arrangement topology

Owner:
- `docs/assistant-context/creation/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`

Protected specialized sub-specs:
- `docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/SPEC.md` — applies only when Strong Braided Half-Up / ハーフアップ＋編み込み強め is explicitly requested
- `docs/assistant-context/creation/yura/identity/hair/styles/LOW_CHIGNON_SPEC.md` — applies when ordinary Low Chignon / ローシニヨン is explicitly requested

Current hairstyle visual MASTER:
- manifest: `docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/VISUAL_MASTER.md`
- paired image: `docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/VISUAL_MASTER.png`
- gen_id `0336bd46-16bf-4d17-823b-73d6204cba31`
- when repository-image inspection is available, inspect the paired PNG for Strong Braided Half-Up generation

The guideline owns generic tie / gather position, ponytail high/mid/low definitions, generic low-chignon / half-up / braid topology, root convergence, mass conservation and camera projection. The Strong Braided Half-Up and Low Chignon protected sub-specs narrow their respective arrangements without changing HAIR v1.3 core values.

Current production priority:
- Normal Super-Long baseline = established
- Strong Braided Half-Up = protected text sub-spec active; visual MASTER adopted / current as of 2026-09-19
- Low Chignon protected text spec v1.0 = active; visual MASTER not yet adopted
- Mid Ponytail / Low Ponytail visual-master production remains deferred until October 2026 or later unless explicitly reopened

### 3.7 RENDERING grammar

Owner:
- `docs/assistant-context/creation/yura/identity/rendering/RENDERING_STYLE_SPEC.md`

### 3.8 Practical integrated text assembly

Owner:
- `docs/assistant-context/creation/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`

### 3.9 Outfit

Owner:
- `docs/assistant-context/creation/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md`

Current baseline:
- named garment identity takes priority
- normal context-appropriate adult exposure
- no automatic extra covering layer merely to cover ordinary skin
- outfit never changes protected BODY / FACE / EYE / HAIR / RENDERING

### 3.9A Controlled validation clothing

Protected sub-spec:
- `docs/assistant-context/creation/yura/qa/VALIDATION_CLOTHING_SPEC.md`

Applies to MASTER / BODY / FACE-full-body / HAIR controlled validation and hairstyle MASTER candidates.

Owns:
- fixed neutral validation-clothing category
- generation wording = plain pale opaque sleeveless top + plain pale opaque simple shorts
- prompt compiler keeps detailed QA / rejection vocabulary out of the image-generation prompt
- comparison-condition FAIL semantics when clothing materially changes apparent anatomy

Validation clothing is a measurement condition, not fashion.
Detailed clothing / BODY comparability is evaluated after generation.
A validation-clothing mismatch must never be repaired by rewriting BODY canon.

### 3.10 Pose / contact / load / 3D reference

Owner:
- `docs/assistant-context/creation/yura/generation/pose/POSE_GENERATION_GUIDELINE.md`

3D references control pose structure only, never YURA identity / BODY / FACE / EYE / HAIR / RENDERING.

### 3.11 Generation conversation / rewrite

Owner:
- `docs/assistant-context/creation/yura/generation/PROMPT_REWRITE_WORKFLOW.md`

### 3.12 Structured generation input

Owner:
- `docs/assistant-context/creation/yura/generation/GENERATION_TEMPLATE.txt`

### 3.13 Room / environment routing

Background Authority is intentionally separate from YURA Visual Identity.

Current Background routing:
- `docs/assistant-context/creation/background/START_HERE.md`

No room/environment file inside YURA Visual Identity owns Background canon.
Legacy room material under `creation/background/reference-materials/` is non-authoritative and may be consulted only when explicitly requested for Background reconstruction/formalization.

### 3.14 Framing / margin / use-case layout

Owner:
- `docs/assistant-context/creation/yura/generation/framing/FRAMING_AND_MARGIN_SPEC.md`

Protected operational sub-spec:
- `docs/assistant-context/creation/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md`

The parent owns framing / margin / Quiet Zone / BODY-safe adaptation.
The Profile A–E sub-spec owns named use-case routing and profile defaults:

- A = MASTER / full-body validation
- B = standard full-body derivative
- C = smartphone wallpaper
- D = X / SNS thumbnail
- E = background / room / environment only

Layout never owns BODY geometry.
Explicit user ratio / placement may override a profile's default ratio while the parent framing invariants remain mandatory.

### 3.15 Post-generation QA

Owner:
- `docs/assistant-context/creation/yura/qa/GENERATION_QA.md`

QA judges against domain owners and applicable protected sub-specs; it does not invent new canon.

---

## 4. Protected CANON LOCK

Unless explicitly changed by the user, lock:

- current YURA identity using MASTER `e942...` as whole-character cross-check
- adult / early-twenties readability
- BODY geometry and exact 7.25-head system
- FACE geometry
- protected eye signature
- HAIR v1.3 core
- Normal Super-Long v1.0 when ordinary down hair is intended
- 2D rendering grammar
- separation of MASTER identity from outfit / pose / scene

Current anchors include:

- 153 cm
- exactly 7.25 heads tall
- petite / slender / delicate adult build, not skeletal
- bust moderately fuller relative to petite frame
- arms slender but not stick-thin
- silver-white super-long hair, main ends near waist to slightly below
- ordinary unarranged hair = Normal Super-Long vertical I-line leaning presentation
- blue-gray eyes
- extremely small lower-right pupil-edge notch
- high-quality 2D anime, low PBR / low CGI

Canonical BODY anchor:
`153cmの小柄・華奢 体格比で胸はやや豊かめ`

Outfit exposure is not part of this BODY anchor.

---

## 5. Normal derivative variables

Normally variable per image:

- outfit
- accessories
- footwear
- explicitly requested permitted hairstyle arrangement
- expression
- pose / gesture / gaze
- camera / framing within the applicable protected layout profile
- background / scene
- lighting within rendering grammar
- props

When no alternate hairstyle is requested, Normal Super-Long is the current protected default, not a free variable.

Derivative variables never authorize protected-domain drift.

---

## 6. Mandatory read profiles

### 6.1 New chat / recovered context

1. `YURA_START_HERE.md`
2. `docs/assistant-context/AI_BEHAVIOR_CONTROL.md`
3. `docs/assistant-context/YURA_START_HERE.md`
4. `YURA_STATE_SNAPSHOT.md`
5. this governance
6. `docs/assistant-context/creation/yura/START_HERE.md`

### 6.2 Ordinary YURA image generation

1. this governance
2. `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`
3. inspect `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png` when available
4. `docs/assistant-context/creation/yura/identity/body/BODY_MASTER.md`
5. `docs/assistant-context/creation/yura/identity/body/BODY_SPEC.md`
6. `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md`
7. `docs/assistant-context/creation/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
8. `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md`
9. `docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md` when no alternate arrangement is requested
10. `docs/assistant-context/creation/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
11. `docs/assistant-context/creation/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`
12. `docs/assistant-context/creation/yura/generation/framing/FRAMING_AND_MARGIN_SPEC.md` when layout matters
13. `docs/assistant-context/creation/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md` when selecting MASTER / standing / smartphone / X-SNS / background output behavior
14. `docs/assistant-context/creation/yura/qa/VALIDATION_CLOTHING_SPEC.md` when MASTER / BODY / FACE-full-body / HAIR controlled validation is intended
15. task-specific guidelines
16. current request

When accepting / publishing / reusing / retrying output, additionally apply `docs/assistant-context/creation/yura/qa/GENERATION_QA.md`.

---

## 7. Fixed generation compile order

### Block A — CANON LOCK

Compile:
- current VISUAL MASTER `e942...`
- BODY
- FACE
- EYE SIGNATURE
- HAIR v1.3
- Normal Super-Long v1.0 when ordinary down hair is intended
- RENDERING

Keep unchanged across retries unless a protected change is explicit.

### Block B — DERIVATIVE DESIGN

Compile requested outfit / accessories / explicit hairstyle arrangement / expression / scene / props only.

### Block C — PHYSICAL POSE

Resolve body/head orientation, shoulders/torso/pelvis, limbs, support/contact/load, center of gravity and front/back ordering.

### Block D — CAMERA / LAYOUT

Resolve:
- intended asset use
- applicable Profile A–E
- shot size
- camera direction
- perspective
- occupancy
- aspect ratio
- negative space
- margin / Quiet Zone

Use `docs/assistant-context/creation/yura/generation/framing/FRAMING_AND_MARGIN_SPEC.md` + `docs/assistant-context/creation/yura/generation/framing/IMAGE_SIZE_PROFILE_SPEC.md`.
Never change anatomy for layout.

### Block E — REFERENCE ISOLATION

Assign every reference one explicit role.

- current MASTER → whole-character identity + approved Normal Super-Long visual cross-check
- 3D / mannequin → pose / joints / contact / load / camera only
- room image → room geometry only
- hairstyle arrangement reference → arrangement topology only unless separately promoted
- derivative example → assigned derivative property only

### Block F — NEGATIVE / ANTI-DRIFT

Protect against:

- identity drift from current MASTER
- BODY drift
- eye-color / signature drift
- HAIR v1.3 length / mass drift
- Normal Super-Long lateral spread / front-loading / endpoint drift
- hairstyle relocation for camera readability
- CGI / photoreal leakage
- unrequested text / logos
- arbitrary decoration
- clothing-category fusion when explicit garments are specified
- reference-role leakage
- anatomy distortion from framing / profile adaptation

---

## 7A. Mandatory Git production visual recovery

Before **any YURA production image-generation tool call**, apply:

`docs/assistant-context/creation/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md`

Rules:

- production identity authority = current Git branch only;
- resolve the exact current MASTER from Git first;
- inspect the direct current Git visual when technically available;
- otherwise use only the current SHA-matched Git Bridge;
- for the neutral MASTER, Bridge production recovery requires both FULL and PORTRAIT decode + decoded-hash verification + actual visual inspection;
- Git path / gen_id / blob SHA / manifest match / Base64 existence are metadata only and do not count as visual inspection;
- production state must reach **`GIT_VERIFIED`** before generation;
- if `GIT_VERIFIED` cannot be reached, production is **BLOCKED**;
- ordinary production must never retrieve deleted / superseded Git revisions as fallback.

---

## 7B. VISUAL MASTER GATE — production blocker

For a protected YURA visual MASTER/reference:

- `UNRESOLVED` → generation prohibited
- `IDENTIFIED` → generation prohibited
- `GIT_PIXELS_RECOVERED` → generation prohibited
- `GIT_PIXELS_INSPECTED` → generation prohibited until current-Git provenance is verified
- `GIT_VERIFIED` → production generation may proceed

The gate is satisfied only when actual pixels recovered from the **current Git production source or its current SHA-matched Git Bridge** have been visually inspected and tied back to the current Git authority.

A Bridge source-SHA match alone does not satisfy the gate.

**No production image-generation tool call may occur before this gate reaches `GIT_VERIFIED`.**

---

## 7C. EXPLICIT REFERENCE GATE — production blocker

Purpose: bridge verified Git visual recovery to the **actual image-generation tool invocation**.
`GIT_VERIFIED` proves which current visual authority was recovered and inspected. It does **not** by itself prove that the generator will use only that authority as YURA's identity reference.

Before **every** YURA production image-generation tool call, including every retry, perform a `REFERENCE_INPUT_PRECHECK`.

Required preflight fields:

- current MASTER repository path
- current MASTER Git blob SHA
- current MASTER exported / Bridge source SHA identity as applicable
- visual recovery state = `GIT_VERIFIED`
- approved identity-reference source(s)
- execution-surface reference-binding mode
- every image reference that may be visible to / selected by the generator
- explicit role of every non-identity reference
- derivative / rejected / generated-output identity-reference count
- final reference-input state

### Identity-reference allowlist

For ordinary neutral YURA production, identity authority is limited to:

- the current canonical `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png`; or
- when direct Git PNG transport is unavailable, the current source-SHA-matched Git Bridge FULL + PORTRAIT recovered from that same MASTER.

FULL and PORTRAIT are transport views of the same canonical MASTER. They are not independent authorities.

The following are **never eligible as YURA identity references** merely because they exist in the chat or are recent / attractive:

- generated outputs from the current or earlier attempts
- rejected candidates
- historical derivatives
- validation-environment outputs
- arbitrary chat attachments
- 3D / mannequin / pose references
- superseded / deleted Git visuals
- chat memory

### Tool-binding rule

If the execution surface provides a reliable tool-native method to bind image references, use it to bind **only the approved identity-reference allowlist** for YURA identity. Tool-specific parameter names are implementation details and are not project canon.

If the execution surface selects images automatically, or if the assistant cannot verify that non-allowlisted images are excluded from YURA identity conditioning, then:

`REFERENCE_INPUT_STATE = NOT_GUARANTEED`

and production generation is **BLOCKED**.

Required blocked result:

`BLOCKED — REFERENCE INPUT NOT GUARANTEED`

Do not proceed on the assumption that the generator will "probably" choose the MASTER.

### Non-identity references

A pose / room / arrangement / object reference may be supplied only when:

1. its role is explicitly assigned;
2. the execution surface can preserve that role boundary without making it an uncontrolled identity source; and
3. current MASTER identity remains authoritative.

A user's explicit request to use a derivative as a derivative / pose / composition reference does **not** promote that image to YURA identity authority. Promotion to identity authority still requires the protected Git MASTER change-control process.

### Production permit

Production generation is permitted only when both are true:

- visual recovery state = `GIT_VERIFIED`
- reference-input state = `REFERENCE_INPUT_GUARANTEED`

Every retry reruns this gate from the current tool-call conditions.
A previous successful preflight does not automatically carry over to a later call.
When exact-preservation mode is active, the retry must also rerun the Protected Pixel Preservation Gate.

Generated outputs must not be fed back as YURA identity references.
The phrase **"strongest prior candidate as rollback"** means QA comparison / rollback selection only, not generator identity-reference injection.

---

## 7D. PROTECTED PIXEL PRESERVATION GATE — exact-change blocker

When the user requires any protected region to remain unchanged — including "差分なし", "変更なし", "維持", "固定", "寸分の狂いなし", "完全一致" or equivalent — apply:

`docs/assistant-context/creation/yura/generation/preservation/PIXEL_PRESERVATION_PROTOCOL.md`

In exact-preservation mode, a protected region that is not authorized to change is **not a generative variable**.

Before every production execution:

1. resolve the exact approved source;
2. define the authorized-change mask;
3. define immutable protected regions;
4. define only physically necessary dependency pixels;
5. verify that the execution surface can modify only authorized / dependency pixels;
6. verify that immutable protected regions will not be stochastically redrawn, resampled or recompressed;
7. set `PROTECTED_PIXEL_PRESERVATION_GUARANTEED` only when exact preservation can be technically guaranteed.

If not:

`BLOCKED — PROTECTED PIXELS CANNOT BE GUARANTEED`

A whole-character text-to-image rerender does not satisfy an exact-preservation request.
A generic edit path that may redraw unmasked protected regions also does not satisfy it.

For exact-preservation operations, production permission requires all applicable hard gates:

- `GIT_VERIFIED`
- `REFERENCE_INPUT_GUARANTEED`
- `PROTECTED_PIXEL_PRESERVATION_GUARANTEED`

After execution, exact unchanged-region pixel comparison is mandatory.
Visual similarity is not proof of preservation.

---

## 7E. PROTECTED BODY GEOMETRY GATE — derivative/body-separation blocker

Apply:
`docs/assistant-context/creation/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

Derivative authorization never authorizes BODY change.

In particular, "服だけ変更", "髪だけ変更", "背景だけ変更", "表情だけ変更", other single-domain-only requests, controlled validation, and exact-preservation retries must preserve current protected BODY geometry independently from the changed visual layer.

For strict BODY-preservation operations:

1. define the current `BODY_LOCK`;
2. identify a reliable BODY geometry carrier;
3. verify that the execution route preserves protected BODY anchors independently from clothing / other derivative pixels;
4. set `BODY_GEOMETRY_GUARANTEED` only when this is technically guaranteed.

If not:

`BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED`

A clothing edit mask may overlap the BODY projection but does not authorize changing anatomy.
Garment geometry adapts to BODY; BODY never adapts to garment.

For outfit-only exact preservation, both are required:

- `BODY_GEOMETRY_GUARANTEED`
- `PROTECTED_PIXEL_PRESERVATION_GUARANTEED`

After execution, if BODY equality cannot be verified:

`REJECT — BODY GEOMETRY PRESERVATION NOT VERIFIED`

---

## 8. Reference-role isolation

### Current production MASTER

`docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png` / `e942...` is the primary whole-character production visual reference and the approved Normal Super-Long visual anchor.

Precise domain specs still override incidental artifact details in the MASTER inside their own domains.

### Non-current Git visual sources

Normal generation uses current-branch authorities only. Do not search Git history or deleted revisions during ordinary generation / QA. Historical inspection is allowed only when the user explicitly requests provenance or history.

### 3D / mannequin

Extract only pose / joints / support / contact / load / limb ordering / camera / relevant structural object relation.
Never inherit BODY, FACE, EYE, HAIR, temporary clothing, CGI/PBR style, materials, lighting or grading.

### Derivative images

A derivative controls only the property explicitly assigned to it. Attractive or recent does not mean canonical.

---

## 9. Conflict-resolution algorithm

1. identify exact conflict
2. classify domain
3. determine whether latest user statement is finalized canon change, temporary exception, or derivative request
4. route to Section 3 owner
5. apply protected sub-spec only inside parent domain boundary
6. preserve unaffected domains
7. never average contradictions
8. never compensate one domain by changing another
9. if active protected owners truly conflict, repair Git before generation

Examples:

- prop error ≠ BODY failure
- clothing concealment ≠ anatomy change
- full-body eye notch not resolvable ≠ automatic identity failure
- wrong visible eye color = FACE/EYE failure
- Normal Super-Long main mass at thigh length = HAIR failure
- wrong ponytail height = HAIR arrangement failure
- CGI leakage from 3D reference = rendering/reference-isolation failure
- Profile D default 16:9 + explicit user 1:1 request = use 1:1, keep Profile D margin/readability behavior
- creating Profile C Quiet Zone by changing leg/head proportions = BODY + layout failure

---

## 10. Retry / anti-drift

A retry is a correction, not a fresh redesign.

- keep Block A fixed
- classify failed Gate / domain first
- change minimum necessary variables
- preserve passed domains
- prefer local correction for isolated production artifacts
- do not accumulate speculative prompt changes
- keep strongest prior candidate as rollback for QA comparison / rollback selection only; do not feed it back as a YURA identity reference
- reject a retry that creates a new protected failure
- never promote a reroll to MASTER without explicit approval + Git logging

---

## 11. Mandatory post-generation QA

Material outputs intended for acceptance, publication, reuse, UI assets, derivative reference, or further iteration use `docs/assistant-context/creation/yura/qa/GENERATION_QA.md`.

Canonical Gates remain:

0. authority / evaluation context
1. WHOLE-CHARACTER IDENTITY
2. BODY / SCALE / ANATOMY
3. FACE / EYE / PROTECTED SIGNATURE
4. HAIR GEOMETRY / CONTINUITY
5. RENDERING GRAMMAR
6. DERIVATIVE REQUEST FIDELITY
7. POSE / PHYSICAL STRUCTURE / CAMERA
8. SCENE ARTIFACT / OUTPUT HYGIENE

Statuses: PASS / FAIL / NOT OBSERVABLE / N/A.

Gates 1–5 protect canon; Gates 6–8 evaluate derivative / production execution.

---

## 12. Promotion / canon-change rule

To materially alter protected canon:

1. require explicit user approval
2. identify changed domain
3. update domain owner / master manifest first
4. update protected sub-spec if implementation routing changes
5. update this governance if routing / anchors changed
6. sync `YURA_STATE_SNAPSHOT.md`
7. sync `docs/assistant-context/creation/yura/START_HERE.md`
8. record historical reasoning when useful
9. ensure `YURA_START_HERE.md` still routes correctly
10. conceptually run `docs/assistant-context/creation/yura/AI_CONTROL.md`
11. keep QA aligned

Do not leave finalized canon change solely in chat memory.

---

## 13. One-line authority summary

**Project governance decides how to reason. This file routes image-generation authority. Domain specs own their domains. Protected sub-specs narrow implementation inside those domains. The current `e942...` MASTER anchors whole-character appearance. Profile A–E route layout use cases without changing BODY. References stay role-limited. QA routes failed domains back for correction.**

---

## 14. Change control

Do not silently:

- reorder global authority
- let a derivative override protected canon
- let a task guideline redefine another domain
- alter CANON LOCK across retries without cause
- reintroduce a default low-exposure BODY anchor
- bypass protected Profile A–E routing when its use case is clearly applicable
- use layout adaptation to change BODY
- bypass Gate-based QA for material acceptance

Material changes require explicit user approval and Git logging.
