# YURA Protected Body Geometry Preservation Protocol

Status: **CANONICAL / MANDATORY BODY-GEOMETRY PRESERVATION PROTOCOL**
Adopted: 2026-09-20
Character: 久遠ゆら / YURA

Parent authority:
`visuals/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`

Protected BODY authorities:
- `visuals/yura/identity/body/BODY_MASTER.md`
- `visuals/yura/identity/body/BODY_SPEC.md`

Purpose: 衣装・背景・髪・表情・小物などの派生変更が、YURAの承認済みBODY geometryを再解釈・再生成・変形することを防ぐ。特に「服だけ変更」「髪だけ変更」「差分なし」等で、変更対象の見た目とBODYの変更権限を混同しないためのFail-Closed実行規則。

---

## 1. Absolute rule

**Derivative-layer authorization never authorizes BODY change.**

Changing clothing pixels, garment silhouette, background, hair, expression, lighting, pose reference, canvas or another derivative layer does not permit changing the protected underlying BODY geometry.

The following remain protected unless the user explicitly approves a BODY canon change:

- 153 cm petite adult scale concept
- exactly 7.25-head protected design ratio
- head-to-body relationship
- neck / shoulder width and relationship
- ribcage width / depth
- bust volume / placement / projection relative to the petite frame
- torso length
- waist position / width relationship
- pelvis / hip geometry
- thigh / calf thickness and proportions
- arm thickness and proportions
- hand / foot scale
- front / side / back continuity rules

Outfit must fit / drape / occlude around the protected BODY.
BODY must never be regenerated to fit the outfit.

---

## 2. Trigger conditions

The strict BODY geometry gate is mandatory when any of the following applies:

- user says 「服だけ変更」「衣装だけ変更」 or equivalent;
- user says 「髪だけ変更」「背景だけ変更」「表情だけ変更」 or any other single-domain-only change;
- user says 差分なし / 変更なし / 維持 / 固定 / 寸分の狂いなし / 完全一致 or equivalent;
- controlled MASTER / BODY / HAIR / FACE validation is being performed;
- a retry repairs one non-BODY domain while BODY has already passed;
- the requested derivative is supposed to preserve the existing pose / camera / full-body silhouette baseline.

For ordinary creative derivatives without an exact-preservation instruction, BODY canon is still protected semantically and Gate 2 QA remains mandatory.  
For the triggers above, semantic intent alone is insufficient: the execution route must support a verifiable BODY lock.

---

## 3. BODY and garment are separate layers

Treat these as independent domains:

### BODY GEOMETRY — protected

The underlying anatomy and approved proportions.

### GARMENT GEOMETRY — derivative

Fabric shape, cut, seam, volume, drape, hem, sleeves, waistband, folds, padding or compression effects that the user actually requested.

### COMPOSITE SILHOUETTE — observed result

What the raster image shows after garment occlusion / drape.

A garment can hide or extend beyond the BODY silhouette.
That does **not** mean the BODY underneath may change.

A clothing edit mask may overlap the projected BODY region in 2D, but this overlap authorizes only the garment / necessary compositing pixels. It never authorizes anatomy changes.

---

## 4. BODY LOCK definition

Before strict execution, define a `BODY_LOCK` from current BODY authorities.

Required protected anchors include, when applicable to the view:

- crown-to-sole = exactly 7.25 head heights
- head size relative to whole body
- shoulder span
- ribcage span
- bust base / volume / projection relationship
- torso length
- anatomical waist position
- waist-to-ribcage relationship
- waist-to-pelvis relationship
- pelvis / hip width
- upper-thigh width
- knee position
- calf width / taper
- ankle width
- upper-arm / forearm thickness
- wrist width
- hand and foot scale

If pose and camera are also specified as unchanged, lock:

- joint locations
- body orientation
- head orientation
- shoulder / pelvis rotation
- stance / support
- camera direction / height / perspective
- character scale and position in frame

A derivative request may change one of these only when the user explicitly authorizes that specific domain change.

---

## 5. BODY geometry carrier requirement

For a strict BODY-preservation operation, the execution route must have a reliable **BODY geometry carrier**.

Acceptable examples include:

- an approved layered body asset beneath clothing;
- an approved body rig / mesh / landmark map whose proportions are locked to the current BODY authority;
- a deterministic edit operation that preserves the existing body geometry while replacing only the garment layer;
- another verifiable structural representation explicitly approved for YURA.

A prompt, textual measurement list, or visual resemblance alone is **not** a BODY geometry carrier.

The FRONT BODY MASTER is authoritative evidence, but merely showing it to a stochastic full-image generator does not guarantee identical geometry.

If hidden / occluded BODY geometry would have to be invented again by the model and there is no reliable geometry carrier, strict BODY preservation cannot be guaranteed.

---

## 6. Garment-change rule

For 「服だけ変更」 / outfit-only:

Allowed to change:
- garment pixels
- fabric volume / folds consistent with the requested garment
- minimal edge / occlusion / contact pixels required to composite the garment

Not allowed to change:
- BODY geometry
- pose
- FACE / EYE
- HAIR unless garment physically requires a user-authorized occlusion interaction
- camera / framing unless explicitly requested
- visible skin geometry outside necessary garment contact

Never:
- widen / narrow shoulders to fit sleeves;
- enlarge / shrink ribcage to fit a top;
- enlarge / flatten bust to make a garment read correctly;
- pinch / widen waist to fit waistband;
- widen / narrow pelvis for shorts / skirt;
- thicken / thin thighs because hem or shorts changed;
- change arm thickness because sleeves changed;
- lengthen legs because outfit proportions changed.

The garment adapts to YURA. YURA does not adapt to the garment.

If the garment itself intentionally compresses / pads / structures the visible silhouette, record that as a **garment effect**. The protected underlying BODY still remains unchanged.

Loose or opaque clothing may make a BODY anchor unobservable. That is occlusion, not permission to alter the anchor.

---

## 7. Strict BODY preservation state machine

Use these states:

1. `BODY_GEOMETRY_UNMAPPED`
2. `BODY_LOCK_DEFINED`
3. `BODY_GEOMETRY_CARRIER_VERIFIED`
4. `BODY_GEOMETRY_GUARANTEED`

Only state 4 permits a strict BODY-preservation production operation.

Per-call preflight record:

- BODY authority versions
- BODY MASTER id
- current whole-character MASTER id
- protected BODY anchors
- pose / camera lock state
- BODY geometry carrier
- authorized derivative domain
- garment effect, if any
- verification method
- final BODY geometry state

If state 4 cannot be reached:

`BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED`

Do not replace this with "the prompt says keep the same body."

---

## 8. Relationship to protected pixel preservation

Pixel and BODY locks solve different problems.

`PROTECTED_PIXEL_PRESERVATION_GUARANTEED` means:
- pixels outside authorized / dependency regions remain exactly unchanged.

`BODY_GEOMETRY_GUARANTEED` means:
- protected anatomy remains unchanged even where clothing pixels legitimately replace / occlude BODY-visible pixels.

For outfit-only exact-preservation, both are required.

Example:

Face / hair / exposed skin outside the clothing edit region:
- exact pixel preservation may apply.

Torso / bust / waist / pelvis underneath the new clothing:
- BODY geometry preservation applies even though the raster garment pixels change.

The clothing mask never cancels the BODY lock.

---

## 9. Production flow for outfit-only exact preservation

**current Git authority**
→ **GIT_VERIFIED**
→ **REFERENCE_INPUT_GUARANTEED**
→ **BODY_LOCK_DEFINED**
→ **BODY_GEOMETRY_CARRIER_VERIFIED**
→ **BODY_GEOMETRY_GUARANTEED**
→ authorized garment-change mask
→ **PROTECTED_PIXEL_PRESERVATION_GUARANTEED** for all immutable visible regions
→ constrained garment execution
→ pixel + BODY verification
→ QA

If the execution surface can only regenerate the whole character stochastically:

`BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED`

---

## 10. Post-operation verification

When pose / camera are unchanged, verify every observable protected BODY anchor against the locked source / geometry carrier.

For exact structural routes, use deterministic geometry / landmark equality rather than visual impression.

Required principle:

- no BODY anchor may move because of an outfit change;
- no protected width / length relationship may be recomputed by the generator;
- hidden anchors must remain fixed in the geometry carrier even when not visible in final raster;
- clothing-caused visual contour changes must be attributable to garment geometry, not BODY changes.

If BODY equality cannot be verified:

`REJECT — BODY GEOMETRY PRESERVATION NOT VERIFIED`

Do not classify unverified hidden BODY as PASS merely because the final clothed silhouette looks plausible.

---

## 11. Retry rule

A failed garment / derivative retry returns to:

- the same approved BODY geometry carrier;
- the same current MASTER identity;
- the same BODY_LOCK;
- the same immutable pixel source.

Do not chain BODY from a failed generated candidate.

Change only the failed derivative layer.

Any retry that silently changes BODY is rejected even if the outfit looks better.

---

## 12. No false guarantee rule

Never claim BODY preservation merely because:

- BODY SPEC text was included in the prompt;
- the current MASTER was referenced;
- the result looks petite / slender;
- the 7.25-head ratio appears approximately correct;
- clothing hides the area that may have drifted;
- the generator usually follows anatomy prompts.

Strict BODY preservation is an execution property, not a stylistic intention.
If it cannot be guaranteed and verified, block or reject the strict operation.
