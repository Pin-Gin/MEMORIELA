# YURA Protected Pixel Preservation Protocol

Status: **CANONICAL / MANDATORY EXACT-PRESERVATION EXECUTION PROTOCOL**
Adopted: 2026-09-20
Character: 久遠ゆら / YURA
Parent authority:
`docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`

Protected BODY geometry companion protocol:
`docs/assistant-context/creation/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

Purpose: 「差分なし」「変更しない」「維持」「寸分の狂いなし」「完全一致」等の要求を、プロンプト上の努力目標ではなく、画像生成・画像編集の実行可否を決めるFail-Closed条件として扱う。

---

## 1. Absolute rule

When the user does **not** authorize a protected visual region to change, that region is not a generative variable.

It must be preserved from the approved current source rather than re-created from text, memory, resemblance, or stochastic regeneration.

A production tool call is permitted only when the execution route can guarantee that all non-authorized protected pixels remain unchanged.

Required state:

`PROTECTED_PIXEL_PRESERVATION_GUARANTEED`

If that state cannot be established before execution:

`BLOCKED — PROTECTED PIXELS CANNOT BE GUARANTEED`

Do not substitute "visually similar", "MASTER-like", "same character", "high fidelity", or prompt strength for exact preservation.

---

## 2. Trigger conditions

This protocol is mandatory when any of the following applies:

- user says 差分なし / 変更なし / そのまま / 維持 / 固定 / 寸分の狂いなし / 完全一致 or equivalent;
- user identifies a protected region that must not change;
- a validation task explicitly requires unchanged comparison conditions;
- a retry is intended to repair one domain while preserving already-passing protected regions exactly;
- project governance or a protected workflow marks a region as immutable for the operation.

If ambiguity exists between "same identity" and "pixel-identical preservation", the stronger explicit user instruction controls.

---

## 3. Source authority

Exact preservation source must be the current approved production source resolved through Git authority.

For neutral YURA:

- canonical source = current `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png`;
- Bridge FULL / PORTRAIT may recover / inspect the MASTER, but do not become independent canon;
- generated outputs, rejected candidates, prior derivatives, chat attachments, 3D references and memory are not exact-preservation identity sources unless explicitly promoted through protected Git change control.

The exact source artifact and source hash must be captured before editing.

---

## 4. Authorized-change mask

Before execution, classify the image into:

### A. IMMUTABLE PROTECTED REGION

Pixels / regions not authorized to change.

Examples when applicable:
- FACE / EYE identity
- protected HAIR regions
- protected BODY regions
- rendering details that must remain exact
- any other user-designated "no difference" area

### B. AUTHORIZED CHANGE REGION

Only pixels / regions the user explicitly permitted to change.

Examples:
- specified clothing region
- specified background region
- explicitly requested accessory
- explicitly requested local correction

### C. DEPENDENCY REGION

Pixels that physically must change because the authorized change necessarily alters occlusion / edge blending / contact.

Dependency regions must be:
1. identified before execution;
2. minimized;
3. explicitly justified by the requested change;
4. never expanded for generator convenience.

If the operation requires changing a protected region outside A/B/C classification, stop and obtain a new authorized change definition rather than silently regenerating it.

When an authorized layer overlaps protected BODY in the raster image, apply the BODY geometry protocol independently. Pixel authorization and BODY authorization are separate.

---

## 5. Execution-route requirements

`PROTECTED_PIXEL_PRESERVATION_GUARANTEED` requires all of the following:

1. current source artifact is identified and verified;
2. authorized-change mask is defined;
3. immutable protected region is defined;
4. execution surface supports an edit path that constrains modification to the authorized / dependency region;
5. the surface does not require stochastic full-image re-rendering of immutable protected regions;
6. no automatic reference or style transfer may redefine protected identity;
7. output pixels are available for post-operation verification;
8. unchanged-region equality can be checked against the exact source.

If any item is unavailable, state remains NOT_GUARANTEED and execution is blocked for an exact-preservation task.

A text-to-image regeneration of the entire character cannot satisfy this protocol.

A generic image-to-image edit that may redraw unmasked protected regions also cannot satisfy this protocol unless the execution surface provides a reliable preservation guarantee and the result passes pixel verification.

---

## 6. Preflight state machine

Use these states:

1. `PIXEL_PRESERVATION_UNMAPPED`
2. `CHANGE_MASK_DEFINED`
3. `PRESERVATION_ROUTE_VERIFIED`
4. `PROTECTED_PIXEL_PRESERVATION_GUARANTEED`

Only state 4 permits execution of an exact-preservation production operation.

Per-call required record:

- source artifact path / id
- source hash
- immutable protected regions
- authorized change regions
- dependency regions
- execution method
- reference-input state
- preservation state
- expected post-operation comparison method

This state is per tool call and must be recomputed on every retry.

---

## 7. Post-operation verification

Exact-preservation acceptance requires comparison against the exact approved source.

For all immutable protected pixels:

- pixel equality must be exact;
- no geometry shift, resampling, recoloring, sharpening, antialias drift, lighting drift, texture drift, or compression-induced change is accepted as "same";
- if the output canvas / encoding requires unavoidable global resampling or recompression, exact preservation is not established.

Preferred verification:
- deterministic pixel diff outside authorized + dependency mask;
- unchanged-pixel count must equal the immutable-region pixel count;
- maximum channel delta = 0;
- immutable-region diff hash = empty / zero-change result.

If exact comparison cannot be performed, final status is not PASS.

Required disposition:

`REJECT — EXACT PRESERVATION NOT VERIFIED`

---

## 8. Retry rule

A retry is not permission to redraw YURA.

If one domain fails:

- keep the same approved source;
- preserve all passing immutable regions exactly;
- modify only the failed authorized region;
- rerun reference-input and pixel-preservation preflight;
- reject any retry that changes an immutable pixel.

Generated / rejected retry outputs remain evidence only and do not become the next identity source.

---

## 9. Relationship to reference-input gate

Production exact-preservation flow:

**current Git authority**
→ **GIT_VERIFIED**
→ **REFERENCE_INPUT_GUARANTEED**
→ **authorized-change mask**
→ **PROTECTED_PIXEL_PRESERVATION_GUARANTEED**
→ execution
→ exact pixel diff
→ QA / acceptance

`REFERENCE_INPUT_GUARANTEED` answers:
"Which visual identity source reaches the tool?"

`PROTECTED_PIXEL_PRESERVATION_GUARANTEED` answers:
"Can the tool change only what the user authorized and leave every other protected pixel untouched?"

Both are required when exact-preservation mode is active.

When the authorized change can alter / occlude the projected BODY region — especially outfit changes — also require `BODY_GEOMETRY_GUARANTEED`. The pixel mask never suspends the BODY lock.

---

## 10. No false guarantee rule

Never claim exact preservation merely because:

- the prompt says "same face";
- the result looks similar;
- the MASTER was used as reference;
- the generator is high quality;
- the output passes ordinary visual QA.

Exact preservation is a binary technical property.
If it cannot be proven, treat it as not guaranteed and block / reject accordingly.
