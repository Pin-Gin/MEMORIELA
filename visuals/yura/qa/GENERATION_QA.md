# YURA Generation QA

Status: **CANONICAL / MANDATORY POST-GENERATION QA**
Adopted: 2026-09-13
Updated: 2026-09-20 — reference + exact-pixel + BODY-geometry hard gates integrated
Character: 久遠ゆら / YURA
Purpose: YURA画像生成後の評価を、感覚的な「良い / 悪い」ではなく、protected identity と derivative execution を分離した固定Gateで判定し、再生成による累積ドリフトを防ぐ。

Parent authority:

`visuals/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`

Project-wide authority:

`docs/assistant-context/AI_BEHAVIOR_CONTROL.md`

This QA does not redefine YURA. Each Gate must judge against the current domain-owner specification.

---

## 1. Core QA principle

Every generated YURA image must be evaluated by **separate domain gates**.

Do not use one overall visual impression to override a protected domain.
Do not use a numerical weighted score to average away a critical identity failure.
Do not modify protected specifications because one generated image failed.

The evaluation order is:

**AUTHORITY CHECK**
→ **PROTECTED CANON GATES**
→ **DERIVATIVE EXECUTION GATES**
→ **PRODUCTION DECISION**
→ **TARGETED RETRY ROUTING if needed**

The purpose is not to demand pixel-identical outputs. The purpose is to preserve the same approved character identity and protected geometry while allowing legitimate derivative variation.

---

## 2. Allowed QA statuses

Use only these statuses per Gate:

### PASS

The observable output is consistent with the applicable authority and current request.

### FAIL

A material observable contradiction exists.

A FAIL must name:

- failed domain
- observed problem
- governing authority
- whether it is protected-canon drift or derivative execution failure
- minimum corrective action

### NOT OBSERVABLE

The item exists in canon but cannot be responsibly verified in this output because of scale, crop, occlusion, lighting, or output resolution.

NOT OBSERVABLE is **not** PASS and is **not** FAIL.
It may only be used when the inability to inspect is genuinely caused by presentation conditions rather than evaluator uncertainty.

Examples:

- full-body image too small to resolve the pupil-edge notch → NOT OBSERVABLE
- waist fully hidden by a coat → some local waist contour details may be NOT OBSERVABLE

Do not use NOT OBSERVABLE to excuse visible contradictions.

### N/A

The criterion genuinely does not apply to this asset.

Example:

- room-geometry Gate for an image not using YURA's canonical room.

---

## 3. Severity classes

Failures are classified by what they are allowed to change.

### P0 — Protected canon failure

A protected YURA domain visibly drifted.

Examples:

- wrong BODY proportion
- materially different face identity
- wrong hair core
- resolvable protected pupil signature mirrored / replaced
- photoreal / CGI style replacing protected 2D grammar

Behavior:

- output is **not acceptable as final YURA production art**
- keep all unaffected protected domains locked
- repair only the failed protected domain plus any directly dependent derivative instruction
- do not rewrite canon to match the failed generation

### P1 — Derivative structural failure

YURA identity is preserved but requested pose / contact / composition / outfit behavior is materially wrong.

Examples:

- wrong hand support
- incorrect contact with a railing
- requested outfit element missing
- major crop / framing mismatch

Behavior:

- preserve CANON LOCK unchanged
- repair the failed derivative domain only

### P2 — Scene / artifact / local production failure

YURA is correct and the main derivative intent is substantially correct, but a local artifact prevents production acceptance.

Examples:

- cup has two handles
- extra object limb / duplicated prop
- accidental text / logo
- small malformed background object

Behavior:

- do not regenerate or redesign YURA unless necessary
- prefer targeted correction / local edit / constrained retry

### P3 — Non-blocking observation

A small visual difference is explainable by clothing, perspective, light, occlusion, or asset scale and does not contradict the protected authority.

Examples:

- structured clothing makes bust prominence appear lower while BODY relationships remain plausible
- full-body eye signature cannot be resolved at output scale

Behavior:

- record if useful
- do not modify canon
- do not force correction merely to make every derivative look identical

---

## 4. Gate 0 — Authority / evaluation-context check

Before judging the image, establish what the image is supposed to be.

Required context:

- pre-generation visual recovery state
- pre-generation reference-input state
- exact-preservation trigger / state when applicable
- strict BODY-preservation trigger / BODY geometry state when applicable
- BODY geometry carrier / BODY_LOCK provenance when applicable
- authorized-change / immutable / dependency region definition when applicable
- exact identity-reference provenance used by the generator
- role of every supplied / eligible image reference
- current VISUAL MASTER identity
- current BODY authority
- current FACE authority
- current EYE SIGNATURE authority
- current HAIR authority
- current RENDERING authority
- task-specific authority when applicable
- current user-approved derivative request
- intended asset use / display scale when known
- role of every reference image used

If the evaluation is being performed from stale / arbitrary references rather than current authorities, stop and restore the correct context first.

Do not compare a derivative against an unrelated old derivative as if that old image were canon.

### Gate 0 hard provenance rule

For YURA production output, Gate 0 requires evidence that the generating call reached:

- `GIT_VERIFIED`; and
- `REFERENCE_INPUT_GUARANTEED`;
- when exact-preservation mode applies, `PROTECTED_PIXEL_PRESERVATION_GUARANTEED`;
- when a single-domain / strict derivative must preserve BODY, `BODY_GEOMETRY_GUARANTEED`.

If the image was generated while reference-input provenance was automatic / unknown / not guaranteed, or if generated / rejected / historical derivative imagery could have acted as an uncontrolled YURA identity reference:

**Gate 0 = FAIL / production provenance invalid**

Final disposition:

`BLOCKED — REFERENCE INPUT NOT GUARANTEED`

Do not accept the asset as production YURA merely because it looks close to the MASTER.

### Exact-preservation Gate 0 rule

When exact-preservation mode applies, ordinary visual QA is insufficient.

The output must be compared against the exact approved source outside the authorized + dependency mask.

Required immutable-region result:

- changed pixel count = 0
- maximum channel delta = 0
- no resampling / antialias / color / compression drift

If the operation was executed without a guaranteed preservation route:

`BLOCKED — PROTECTED PIXELS CANNOT BE GUARANTEED`

If execution occurred but exact unchanged-region comparison cannot prove zero change:

`REJECT — EXACT PRESERVATION NOT VERIFIED`

A visually indistinguishable result is still not exact-preservation PASS without zero-delta verification.

---

## 5. Gate 1 — WHOLE-CHARACTER IDENTITY

Primary authority:

- `visuals/yura/identity/master/VISUAL_MASTER.md`
- `visuals/yura/identity/master/VISUAL_MASTER.png`

Supporting protected domain specs remain authoritative inside their own domains.

Check:

- unmistakably the same YURA overall
- adult / early-twenties readability
- petite / delicate adult impression
- overall face / body / hair balance remains coherent with current YURA
- derivative styling has not turned YURA into a different character
- no arbitrary legacy styling has become base identity

FAIL examples:

- overall character reads as materially different person even if hair color is similar
- apparent age is changed materially
- derivative styling redesigns base identity

Do not use this Gate to override a more precise BODY / FACE / HAIR ruling.

---

## 6. Gate 2 — BODY / SCALE / ANATOMY

Authority:

- `visuals/yura/identity/body/BODY_MASTER.md`
- `visuals/yura/identity/body/BODY_SPEC.md`

Protected anchors include:

- height concept: 153 cm petite adult scale
- exact design target: **7.25 heads tall** when the full proportion is assessable
- slender / delicate but not skeletal
- narrow natural shoulders
- slender compact ribcage
- bust moderately fuller relative to petite frame, not independently oversized
- slim natural waist
- natural adult pelvis / hips
- standard-to-slightly-long legs
- thighs slender with natural softness
- calves slender / naturally curved
- arms slender but not stick-thin
- stable head-to-body ratio / limb thickness

Check BODY relative to the requested perspective, pose, garment construction, and occlusion.

Do not declare BODY FAIL merely because clothing conceals anatomy or perspective changes apparent prominence.

FAIL examples:

- clearly different head-to-body ratio
- random overall slimming / thickening relative to YURA baseline
- stick-thin arms contrary to BODY authority
- materially altered shoulder / waist / pelvis relationship
- legs elongated to fit a tall canvas
- mannequin anatomy inherited from a 3D reference

Presentation-only apparent differences that remain anatomically plausible are P3, not BODY FAIL.

For strict BODY-preservation / single-domain-only operations, "plausible" is not enough. Gate 2 must also verify the locked BODY geometry against the approved carrier. Clothing overlap / occlusion does not authorize anatomy drift. If hidden BODY cannot be verified because no reliable geometry carrier exists, do not mark Gate 2 PASS; use the BODY geometry blocked / rejection state above.

---

## 7. Gate 3 — FACE / EYE / PROTECTED SIGNATURE

Authorities:

- FACE geometry: `visuals/yura/identity/face/FACE_SPEC.md`
- pupil signature: `visuals/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`

Check when observable:

- soft oval adult facial identity
- small softly rounded chin
- blue-gray eye identity
- adult-balanced eye geometry
- refined small nose / restrained mouth geometry
- healthy bright fair skin impression within rendering rules
- YURA-specific pupil signature behavior

Protected signature:

- extremely small teardrop-like notch on the **lower-right edge of the pupil**
- discreet, integrated, not a conspicuous symbol

Resolution-aware rule:

- close-up / face CG: signature should be deliberately preserved; omission / mirroring / replacement is FAIL
- bust-up / medium portrait: preserve when naturally resolvable; judge from actual asset resolution
- full-body / small UI: if the notch is below meaningful visible resolution, mark signature criterion NOT OBSERVABLE, not FAIL

Never enlarge the notch into a heart / star / logo merely to make it inspectable.

Visible eye color that materially departs from the protected blue-gray identity is Gate 3 FAIL. Precise hue / brightness tolerance remains subject to later explicit calibration and is not invented by this QA.

---

## 8. Gate 4 — HAIR GEOMETRY / CONTINUITY

Authority:

- `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
- arrangement topology when applicable: `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`

### Protected core checks

- silver-white color
- length category = **super-long**
- principal ends around the **natural waistline to slightly below**
- only the longest fine ends may approach the **upper waist / just before upper-buttock region**
- total hair mass = **slightly above standard**
- individual strands = **fine / soft**
- upper hair settles naturally under source-length weight
- middle / back retains sufficient density
- lateral spread remains restrained
- tips taper lightly / delicately rather than ending as a heavy slab
- thin long bangs remain consistent
- long cheek-framing side bangs remain consistent
- very gentle natural wave remains consistent
- fine strands are not interpreted as sparse total hair

### Length PASS / FAIL boundary

- natural waistline = PASS baseline
- slightly below waist = PASS
- only the longest fine ends approaching upper-buttock boundary = PASS
- dominant length ending only around below-chest = FAIL — too short
- principal hair mass reaching mid-buttock / lower buttock / thighs = FAIL — too long

### Back-view continuity

- majority of long back hair remains naturally behind the body
- dominant mass stays centered down the back
- hair is not moved to the chest merely to expose clothing / BODY
- waist-area occlusion by the principal hair mass is allowed
- do not split the mass widely merely to reveal the waist / back / hip silhouette

### Arrangement checks

If ponytail / chignon / half-up / braid or another arrangement is requested:

- anatomical gather / tie position must match the arrangement authority
- camera visibility does not move the tie point laterally
- source super-long length / total mass is physically accounted for
- a ponytail must not become unnaturally sparse merely because strands are fine
- a full chignon must credibly contain source length through wrapping / folding / internal overlap
- requested face-framing strands remain unless explicitly changed

FAIL examples:

- materially shorter or longer core length against formal v1.3 without explicit canon exception
- different core bang structure
- wrong base hair color
- fine hair rendered as visibly sparse total hair
- main mass spread laterally into an unintended fan shape
- back hair unnaturally split or pulled forward only to reveal the body
- arrangement silently deletes a large fraction of source hair mass
- centered rear ponytail / chignon shifted sideways merely so it is visible from the front

Formal v1.2 and v1.3 DRAFT are historical only and must not be used as current Gate 4 authority.

---

## 9. Gate 5 — RENDERING GRAMMAR

Authority:

- `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md`

Check:

- high-quality 2D anime illustration
- delicate visible low-contrast line art
- soft cel / grouped illustration shading
- simplified illustrated nose / lips
- low micro-texture
- low PBR / low CGI feel
- grouped illustrated hair locks rather than photoreal fibers
- detailed but non-photographic anime eyes
- adult-balanced anatomy

FAIL examples:

- 3D CGI / game-cinematic character rendering becomes dominant
- photoreal skin / pores / waxy PBR skin
- wet photographic eye rendering
- realistic individual hair-fiber rendering dominates
- heavy HDR / bloom materially changes the protected style
- chibi or giant symbolic-eye treatment changes the character grammar

If a 3D pose reference causes CGI leakage, classify this as RENDERING / REFERENCE-ISOLATION failure, not FACE or BODY redesign.

---

## 10. Gate 6 — DERIVATIVE REQUEST FIDELITY

Authorities:

- current user-approved request
- applicable task-specific guideline(s)

Check only requested derivative variables:

- outfit / accessories
- permitted hairstyle arrangement
- expression
- gaze
- scene / background
- time / season / mood
- props
- requested room variant
- specified exposure direction

Outfit-specific rules follow `visuals/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md`.
Background/room rules do not derive from YURA identity QA. Route Background continuity through `docs/assistant-context/creation/background/START_HERE.md`; non-authoritative legacy room material is not a QA authority.

FAIL examples:

- required cardigan missing
- wrong requested hair arrangement
- requested low-exposure direction ignored
- wrong time-of-day scene
- canonical room geometry materially redesigned when it was meant to remain fixed

This Gate may FAIL while Gates 1–5 PASS. That means YURA is correct; the derivative execution is not.

---

## 11. Gate 7 — POSE / PHYSICAL STRUCTURE / CAMERA

Authority:

- `visuals/yura/generation/pose/POSE_GENERATION_GUIDELINE.md`
- current approved structured pose interpretation

Check:

- body orientation
- head orientation
- shoulder / torso / pelvis relationship
- arm / elbow / wrist / hand placement
- leg / knee / foot placement
- support points
- contact points
- load direction
- center of gravity
- visible / hidden joint plausibility
- front / back ordering
- specified camera / framing

For 3D / PoseMy.Art references, verify that only permitted structural information transferred.

FAIL examples:

- head appears supported by no physical structure
- impossible wrist / elbow orientation
- hidden arm carries unexplained load
- railing / table contact does not match approved structure
- 3D mannequin body shape leaked into YURA
- camera framing materially violates the approved composition

A pose failure must not trigger BODY / FACE / HAIR redesign.

---

## 12. Gate 8 — SCENE ARTIFACT / OUTPUT HYGIENE

Authority:

- current derivative request
- scene / room authority when applicable
- production-quality expectations

Check:

- hands / fingers for obvious local generation artifacts
- duplicate or impossible prop geometry
- object count / handles / legs / supports
- unintended text / logos / labels
- malformed furniture / utensils / signage
- accidental extra body parts / objects
- crop errors
- obvious layer / occlusion accidents

Example:

A cup with two handles is Gate 8 FAIL / P2.
It is not BODY failure and not YURA identity drift.

When Gates 1–7 are strong, preserve the candidate and repair Gate 8 locally when practical.

---

## 13. Production acceptance states

Do not collapse all QA into one score.
Use the following final decisions.

### CANON PASS

Protected Gates 1–5 are all:

- PASS, or
- NOT OBSERVABLE only where the criterion is legitimately unresolvable at the asset scale / crop / occlusion.

No P0 failure exists.

### DERIVATIVE PASS

Gates 6–7 also PASS for the approved request.

### PRODUCTION PASS

Gates 1–8 are acceptable for the intended use.

P3 observations are allowed.
A tiny imperfection below the actual use-case visibility threshold does not require rejection.

### LOCAL REPAIR REQUIRED

CANON PASS is maintained, but a P1 or P2 failure exists.

Action:

- preserve CANON LOCK
- preserve unaffected successful derivative domains
- repair only the failed Gate

### REGENERATE / TARGETED RETRY REQUIRED

A material P0 or non-local P1 failure exists and cannot reasonably be fixed by a local edit.

Action:

- retain current approved authorities
- keep the last strong candidate as a QA comparison / rollback candidate only; do not inject it as a YURA identity reference
- change only instructions belonging to the failed domain

### BLOCKED — BODY GEOMETRY CANNOT BE GUARANTEED

The operation is supposed to preserve BODY while changing another domain, but no verified BODY geometry carrier / execution route can guarantee the protected anatomy.

Action:

- do not execute / do not accept full-image stochastic regeneration
- restore current BODY MASTER + BODY SPEC
- define BODY_LOCK
- use a route that preserves underlying BODY independently from garment / derivative pixels
- rerun BODY geometry preflight

### REJECT — BODY GEOMETRY PRESERVATION NOT VERIFIED

The operation was produced, but protected BODY equality was not verified.

Action:

- reject the output for strict BODY-preservation use
- return to the approved BODY geometry carrier
- do not promote the generated candidate as the next BODY source
- retry only the authorized derivative layer

### BLOCKED — PROTECTED PIXELS CANNOT BE GUARANTEED

Exact-preservation mode applies, but the execution route cannot guarantee that every immutable protected pixel remains unchanged.

Action:

- do not execute / do not accept the operation
- keep the exact approved source
- reduce the operation to an authorized-change mask
- use only a route that can preserve and verify all immutable pixels
- never substitute full-image regeneration

### REJECT — EXACT PRESERVATION NOT VERIFIED

An operation was produced, but zero-delta preservation of immutable protected pixels was not proven.

Action:

- reject the output as exact-preservation production art
- do not promote it as a new identity source
- return to the exact approved source
- use a verifiable constrained edit route

### BLOCKED — REFERENCE INPUT NOT GUARANTEED

The generation call lacks verified identity-reference routing, even if Git visual recovery itself succeeded.

Action:

- reject the output as production evidence
- do not use that output as a YURA identity reference
- restore current Git MASTER reference provenance
- rerun the reference-input preflight
- generate only after `REFERENCE_INPUT_GUARANTEED`

### BLOCKED — AUTHORITY CONFLICT

Two current protected authorities materially contradict each other.

Action:

- do not generate / approve
- identify conflict
- resolve Git authority according to Project Governance
- rerun QA after authority consistency is restored

---

## 14. Retry routing matrix

When a Gate fails, modify the corresponding domain only unless a direct dependency is demonstrated.

| Failed Gate | Primary correction target | Do NOT casually change |
|---|---|---|
| Gate 1 Identity | VISUAL identity assembly / reference selection | BODY numbers, unrelated outfit, room |
| Gate 2 BODY | BODY prompt / scale / reference leakage | FACE, HAIR, scene |
| Gate 3 FACE/EYE | FACE / EYE instructions | BODY, pose, outfit |
| Gate 4 HAIR | HAIR core / arrangement instructions | FACE, BODY, camera unless necessary |
| Gate 5 RENDERING | RENDERING / reference isolation | anatomy / facial geometry |
| Gate 6 Request | OUTFIT / SCENE / ROOM / expression request | protected identity |
| Gate 7 POSE | POSE / contact / camera structure | FACE / BODY canon / HAIR core |
| Gate 8 Artifact | local edit / prop / crop / object correction | all protected domains |

If one attempted fix introduces a new failure in a previously passing protected Gate, reject that attempt and return to the stronger prior candidate.

---

## 15. QA report format

For material YURA image evaluation, use this compact structure:

```text
YURA GENERATION QA
Asset / gen_id:
Intended use:
Evaluation authorities:

Gate 1 Identity: PASS / FAIL / NOT OBSERVABLE / N/A
- Evidence:
- Severity if failed:

Gate 2 BODY: ...
Gate 3 FACE / EYE: ...
Gate 4 HAIR: ...
Gate 5 RENDERING: ...
Gate 6 DERIVATIVE REQUEST: ...
Gate 7 POSE / PHYSICAL STRUCTURE: ...
Gate 8 SCENE ARTIFACT / HYGIENE: ...

CANON: PASS / FAIL / BLOCKED
DERIVATIVE: PASS / REPAIR REQUIRED
PRODUCTION: PASS / LOCAL REPAIR / TARGETED RETRY / REJECT

Failed domain(s):
Minimum next action:
Protected domains that must remain unchanged:
```

Do not fill the report with generic praise. State observable evidence and the minimum necessary correction.

---

## 16. Batch / standing-CG QA rule

For future galgame / standing-CG batches, evaluate both:

1. each asset individually through Gates 1–8
2. cross-asset consistency across the batch

Batch consistency checks include:

- same YURA identity across expressions
- stable BODY widths / head-to-body ratio
- stable FACE geometry
- stable eye-signature intent at source resolution
- stable formal HAIR v1.3 core
- stable RENDERING grammar
- requested variation changes only the intended variables

Do not accept a batch where every individual image looks plausible but YURA gradually evolves from asset to asset.

Use the approved neutral MASTER and strongest accepted batch asset as cross-check references, without promoting the batch asset to MASTER.

---

## Dynamic Pose QA Gate — mandatory for significant movement

Apply this gate whenever the requested image contains meaningful movement beyond neutral standing.

Evaluate each item independently:

### DP-1 Identity

PASS only if:
- FACE identity is preserved
- iris remains protected blue-gray
- hair remains silver-white
- adult readability is preserved

### DP-2 BODY geometry

PASS only if:
- 7.25-head system remains plausible for the projected pose
- segment lengths remain canonical
- shoulder / ribcage / waist / pelvis relationships are preserved
- bust volume is not incorrectly reduced by torso rotation
- thighs / calves / arms are not thickened merely due to crouch / foreshortening

### DP-3 Joint / skeleton

PASS only if:
- joint directions are anatomically plausible
- no impossible elbow / knee / wrist / ankle / neck configuration
- apparent shortening is projection, not segment redesign

### DP-4 Support / contact / load

PASS only if:
- support points are physically coherent
- contact compression is local and plausible
- hidden limbs do not carry unexplained load
- seated / squat compression does not become permanent BODY redesign

### DP-5 Hair conservation

PASS only if:
- source Normal Super-Long mass remains conserved
- principal source length remains protected
- longest-tip upper limit remains protected
- hair movement follows gravity / contact
- pose does not silently shorten or delete source mass

### DP-6 Camera / perspective

PASS only if:
- perspective explains apparent size changes
- camera behavior does not force anatomy distortion
- framing does not alter BODY proportions

### DP-7 Limb / hand / foot artifacts

FAIL if:
- extra / missing limb
- extra / missing major hand or foot
- impossible duplication
- materially broken hand / foot attachment
- severe structural artifact

### Dynamic Pose PASS rule

A significant-motion derivative passes only when all applicable DP gates pass.

If one gate fails:
- retry or repair the pose / projection / contact layer
- do **not** modify protected YURA canon to fit the failed output

---

## 17. Logging rule

Routine QA PASS results do not need to be added to project history.

Routine derivative evidence is not appended to a permanent current-Git validation log.

When a result materially changes a reusable Generation / QA rule, promote that rule through the applicable DESIGN_SPEC task and current Authority file. Historical validation evidence belongs to Git history / external archive rather than current Authority. Examples that may justify a formal rule review include:

- a new pose class passes / fails
- a new reference workflow finding is discovered
- a recurring artifact is identified
- a new stability boundary is established
- a QA rule needs refinement

Material changes to future authority, workflow, or QA behavior must be made through the current Formal Specification / Task control and remain traceable in Git history.

---

## 18. Change control

This QA is protected.

Do not silently:

- replace gate-based evaluation with an averaged score
- downgrade a visible protected contradiction because the rest of the image is attractive
- treat NOT OBSERVABLE as proof of PASS
- treat a scene artifact as BODY / identity failure
- treat clothing / perspective concealment as automatic anatomy drift
- change canon to fit a failed generation
- change multiple unrelated protected domains during a retry

Future material QA changes require explicit user approval and Git logging.


---

## Validation-clothing comparison condition — 2026-09-19

Authority:
`visuals/yura/qa/VALIDATION_CLOTHING_SPEC.md`

For MASTER / BODY / HAIR controlled validation:

- validation clothing must remain pale / plain / opaque / structurally neutral
- no lace / frills / bows / sheer / decorative trim
- no deep neckline or garment shaping that enhances / suppresses bust
- no waistband / shorts reinterpretation that materially changes pelvis / hip / thigh presentation

If validation clothing materially changes apparent anatomy:

**classification = comparison-condition FAIL**

This is not automatically a BODY failure.

Consequences:
- do not promote the candidate to MASTER / BODY / HAIR visual authority
- do not rewrite BODY canon to fit the image
- regenerate with the same protected identity and fixed validation-clothing condition
