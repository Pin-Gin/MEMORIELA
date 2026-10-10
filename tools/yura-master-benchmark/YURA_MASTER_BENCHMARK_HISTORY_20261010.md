# YURA Master Benchmark History — 2026-10-10

Status: **NON-AUTHORITY / HISTORICAL AUDIT RECORD / PRE-AUDIT-V2 CHECKPOINT**

This file is an operational history record only. It is **NOT** Face Identity Authority, Body Geometry Authority, Master construction Authority, Composition Authority, or a QA gate definition.

Its purpose is to preserve the experiment history before starting Body Geometry Audit v2 so that later measurements can be compared without rewriting the past.

---

## 1. Active project objective and authority separation

The sole active deliverable is the final high-quality YURA visual Master, with generation drift and stochastic variance reduced as far as practical.

The active separation is:

```text
FACE IDENTITY / FACE-LOCAL GEOMETRY
  -> visuals/yura/identity/face/YURA_FACE_REFERENCE.png
  -> visuals/yura/identity/face/FACE_REFERENCE_RULES.md

BODY GEOMETRY
  -> visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
  -> visuals/yura/identity/body/BODY_GEOMETRY_GUIDE.md

MASTER CONSTRUCTION TEXT
  -> visuals/yura/identity/master/YURA_VISUAL_TEXT.md

COMPOSITION
  -> visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md
```

`characters/YURA.md`, story/manuscript material, old/rejected images, Git-history-only visual settings, Memory-derived appearance, and unrelated generated images are not permitted to override current visual Authority.

The working discipline is:

```text
one paid RAW
= one explicit hypothesis
= one measurable result
= one decision
```

Composition remains blocked until Body Geometry QA is accepted.

---

## 2. Initial promising RAW used as calibration evidence

Earlier calibration sample:

```text
run_20261004T133603Z
original local size: 1440x2560
SHA256: d166d25d56b6af4326f4ba69dc87d7accf33c9ab18d5491d39b3610de1a9c90a
```

Legacy / pre-v2 landmark estimate:

```text
crown   ≈ 74 original px
chin    ≈ 450
crotch  ≈ 1250
knee    ≈ 1710
soles   ≈ 2470

head ratio          ≈ 6.37 heads
inseam proxy        ≈ 50.9%
chin->crotch         ≈ 2.13 heads
crotch->knee share   ≈ 37.7%
knee->soles share    ≈ 62.3%
```

Author/visual interpretation at the time:

- torso no longer read as obviously elongated;
- pelvis/crotch read higher;
- lower body read longer;
- internal upper/lower-body balance was substantially better than earlier attempts.

This image was never promoted to Master or visual Authority. It remains calibration evidence only.

Important later finding: these legacy head-ratio figures used a visible-hair-crown interpretation. Audit v2 is being introduced specifically because visible hair volume may inflate the crown-to-chin head unit and make the old approximately 6.4-6.6-head readings systematically low.

---

## 3. Test 1 — Face Reference scale-separation enforcement

### Hypothesis

The Face Reference might be leaking apparent head size / crop scale into full-body geometry. The test strengthened the contract that Face Reference pixels control facial identity only, while Body Geometry controls full-body head scale and total head count.

Relevant setup commits include:

```text
792ac1fb1c373e32e98a5998a934de6ff1a16f07  Lock YURA handoff to Master-image-only scope
b9ea99d29a5e8f18f8a853e4ab0a0302a6f70715  Strengthen YURA Test 1 face-scale isolation
eeeccfa80d6727c3b7ccc987a9b116489b4d4a64  Record YURA Test 1 head-scale result
```

### First paid attempt / moderation stop

The first paid Test 1 attempt reached the Image API but was blocked by moderation and produced no RAW.

```text
request id: req_500c16b9b07943538e8c1441eab05081
```

The exact blocked substring was **not** identified. It must not be claimed that a specific phrase was proven to be the cause.

Author-approved non-sexual-purpose context was then added. The approved lines include:

```text
性的な強調を目的としない
これは性的表現を目的としない、キャラクターMaster作成のためのBody Geometry検証です。
上半身前面のシルエットと体積バランスのみです。
```

Commit:

```text
eb40a1dd1e413b57f6f50c3e1c9f9d89a31be8bf  Clarify non-sexual Body Geometry validation context
```

### Successful paid RAW

A later Test 1 run succeeded. Local original size was confirmed as 1440x2560. Composition was not run.

Legacy / pre-v2 estimate from the uploaded proportional display copy:

```text
head ratio      ≈ 6.51 heads
inseam proxy    ≈ 51.8%
chin->crotch     ≈ 2.13 heads
```

Under the then-current gates this failed the 7.1-7.3 head-ratio, 46.0-46.5% inseam, and 2.7985-2.9420 chin-to-crotch checks.

Decision at the time: stronger textual separation alone did not move the legacy measured head ratio toward 7.2 enough to support the hypothesis.

---

## 4. Test 2 — diagnostic removal of Face Reference image input

Setup/result commits:

```text
a14b18ddf239e5efeabd7f4695f7bf87e162c7c1  Set up YURA Test 2 Face-reference isolation
6eb1f089f7988a077b8b7c8ca43d677afcb0c3c4  Record YURA Test 2 diagnostic result
```

Test 2 kept Face Reference provenance in the sealed Authority bundle but removed the Face Reference image from the Image API reference order, leaving the Body Guide as the image reference for the diagnostic A/B.

Observed result:

- Face Identity clearly changed and became unacceptable;
- legacy visual estimate remained roughly around 6.5 heads rather than moving clearly toward 7.2;
- therefore the hypothesis that the Face Reference image *alone* directly forces approximately 6.4-6.5 heads was not supported;
- Face Reference image isolation was rejected because Identity retention became worse.

This did **not** prove that Face Reference has zero indirect effect. It only weakened the simple direct-cause hypothesis.

`tools/yura-master-benchmark/TEST2_RESULT_20261010.md` records this diagnostic decision.

---

## 5. Test 3 — explicit Body Guide landmark-lock enforcement with Face Reference restored

Setup/fix commit:

```text
e185b7f3ef268e6ef177ca53dbad21ab415b445e  Apply YURA Test 3 setup and remove accidental empty file
```

The active Image API reference order was restored to:

```text
1. Face Reference — Face Identity only
2. Body Geometry Guide — Body Geometry only
```

Test 3 made the already-approved Body Guide numeric landmarks explicit as scale-independent relative geometry anchors in the compiled prompt, including crown, chin, crotch, knee, soles, one-head size, total 7.2 heads, crown-to-crotch, chin-to-crotch, and 1:1 crotch-to-knee : knee-to-soles relations.

Free preflight before the paid run reported:

```text
status: PREFLIGHT_OK
paid_model_calls: 0
git_commit: e185b7f3ef268e6ef177ca53dbad21ab415b445e
authority_count: 7
sealed_authority_bundle_sha256: 4a2f71a47d3e79e3bd0f34752e0a38b787a99908b3792c1055e55e8cda889b2e
codex_input_sha256: 9f37160645cbbe1ca2830042a9480621f6118c5b4e8ca29afed653536762166e
```

Result-record commits:

```text
8ff7c9a33ac8e795b1d2e25a8c18b589496518b6  Record YURA Test 3 landmark enforcement result
b0f4292e061a57d852a3c901928722ff8719daab  Update YURA handoff after Test 3
```

Legacy / pre-v2 display-copy landmark estimate:

```text
crown  ≈ 35
chin   ≈ 338
crotch ≈ 1006
knee   ≈ 1390
soles  ≈ 1996

head ratio          ≈ 6.47 heads
inseam proxy        ≈ 50.48%
chin->crotch         ≈ 2.205 heads
crotch->knee         ≈ 1.267 heads
knee->soles          ≈ 2.000 heads
lower split          ≈ 38.8% : 61.2%
```

Author evaluation retained for the next audit stage:

```text
overall body thickness / build: comparatively good
chest / upper-front volume: NG-leaning / problem remained
```

Face Identity was substantially better than in Test 2 because Face Reference had been restored.

Important: all numeric values in this section are legacy/pre-v2 measurements and must be re-measured under the same Audit v2 protocol before any gate change is considered.

---

## 6. Test 4 — Body Guide first in reference order

### Hypothesis

The remaining error might come from reference-order / multi-image weighting rather than from the Face Reference image itself. Test 4 changed the reference priority so that Body Geometry Guide became image 1 and Face Reference image 2, while preserving their authority roles and existing Body Geometry requirements.

Setup commit:

```text
994e336a3769d5e868a198f920885f340afcb14d  Set up YURA Test 4 body-first reference order
```

No mask-based local edit was adopted for the formal Test 4 run. The intended variable was reference order / priority, not a redesign of Body Authority.

### Initial run stop

The first Test 4 execution did not reach the Image API because the prompt invariant validator found a punctuation mismatch: an approved Japanese sentence required the Japanese full stop `。`, while the compiled output used ASCII `.`.

This was treated as a deterministic validation-normalization problem, not as permission to change the approved body specification.

After author approval, punctuation normalization was applied without changing the approved semantic wording.

Commit:

```text
fa1cd912b48b477897a2c150c33bbc738fbd4210  Normalize YURA Test 4 invariant punctuation
```

### Formal paid Test 4 RAW

The paid RAW then completed. The recorded project cost for this formal Test 4 generation was:

```text
USD 0.079787
```

The run used the same intended Authority bundle across its preflight/paid execution. Exact local run-artifact SHA values that were not committed into Git at this checkpoint are intentionally not reconstructed from memory; this history record does not fabricate them.

Legacy / pre-v2 display-copy estimate:

```text
crown  ≈ 39
chin   ≈ 333
crotch ≈ 960
soles  ≈ 1971

head ratio          ≈ 6.57 heads
inseam proxy        ≈ 52.5% around the then-estimated landmarks
chin->crotch         ≈ 2.16 heads around the then-estimated landmarks
```

The previous sensitivity check around the estimated landmarks put the legacy result approximately in the following neighborhood:

```text
head ratio:   about 6.53-6.62
dependent on 1-2 px landmark choices in the displayed copy
```

Author evaluation retained for Audit v2:

```text
chest / upper-front volume: PASS relative to Test 3
whole-body build: too thin
```

Therefore Test 4 improved the chest-specific author judgment but introduced or exposed a body-width / body-volume failure that the then-current vertical-landmark QA did not measure.

---

## 7. Git operational incident that must remain documented

During the Test 3 write sequence, an erroneous GitHub contents operation temporarily created an empty top-level path:

```text
__invalid__
```

Intermediate commit:

```text
95c185c39fe5157dd8588811b830d5307fbe7fbb
```

The final Test 3 commit removed that accidental path and applied the intended Test 3 tree:

```text
e185b7f3ef268e6ef177ca53dbad21ab415b445e
```

No force push was used. The accidental intermediate commit remains in history and must **not** be removed by history rewriting. The current tree does not contain `__invalid__`.

---

## 8. Existing Body QA structure and its known blind spot

The active Body Geometry QA was designed primarily around vertical landmarks:

```text
crown
chin
crotch
knee
soles
```

and derived values such as:

```text
total head ratio
inseam proxy
chin-to-crotch span
crotch-to-knee / knee-to-soles relation
```

This is useful for vertical proportion but it does not numerically encode the author-visible differences that separated Test 3 and Test 4, especially:

```text
shoulder / chest-ribcage width
waist width
pelvis / hip width
upper-thigh width
body-volume continuity
chest-front silhouette / volume relation
```

That omission is central to the Audit v2 work. No gate should be changed merely because the old vertical-only measurements disagree with the author judgment.

---

## 9. Newly identified measurement problem: visible hair crown vs structural crown

The active Face Reference image is 372x364.

Repository/current-file identity values previously recorded include:

```text
Face Reference blob SHA: 4c96c4ec42f996807248be1aff60ec8a090fd570
```

A local audit copy used during the measurement investigation had SHA256:

```text
3f7fddee8c08087484ca1bd48b8ba9eb1acf8221727ef396001091f531c4f030
```

The two identifiers are different hash systems/objects and must not be conflated.

In the visible Face Reference crop, the visible hair crown to chin span was approximately:

```text
visible crown y ≈ 8
chin y          ≈ 252
visible span    ≈ 244 px
```

The hair shell visibly extends above the inferred structural skull crown. A plausible structural-crown correction on this reference is on the order of roughly 24-36 px, with a central working neighborhood around 28-32 px pending Audit v2 specification.

If a full-body image was measured with the visible hair top as the head-unit crown, the head unit can be inflated by roughly 9-12% in the plausible correction range. A legacy apparent result around 6.47-6.57 heads can therefore map close to roughly 7.0-7.3 structural-head units depending on the structural-crown estimate.

Illustrative sensitivity already computed before this checkpoint:

```text
structural-crown correction on Face Reference
28 px -> scale factor about 1.089
32 px -> scale factor about 1.109

legacy Test 3 6.47 -> about 7.05 to 7.18
legacy Test 4 6.57 -> about 7.16 to 7.29
```

These are **not final Audit v2 results**. They are the reason Audit v2 must distinguish:

```text
visible hair crown
structural skull crown estimate
uncertainty band
```

before deciding whether a real 6.5-head geometry problem still exists.

---

## 10. Face Reference indirect-influence hypothesis after Tests 1-4

Current evidence does not support the simple claim:

```text
Face Reference image directly forces the whole body to approximately 6.5 heads.
```

Reason: Test 2 removed the Face Reference image from the Image API input and still did not visibly move the body to 7.2 under the old measurement method, while Face Identity degraded.

However, the weaker indirect hypothesis remains open:

```text
Face Identity reproduction
+ hair/head-shell appearance
+ full-body model prior
-> may indirectly reinforce an apparent large-head silhouette
```

The distinction is important:

```text
FACE REFERENCE direct Body Authority = denied
FACE REFERENCE indirect appearance entanglement = not yet ruled out
```

Audit v2 must therefore measure the Face Reference itself, the active Body Guide, Test 3, and Test 4 under one crown-definition protocol before assigning causal weight.

---

## 11. Four unresolved issues at this checkpoint

The active uncertainty is deliberately separated into four questions:

```text
A. The "6.5-head problem"
   Is this a real generated Body Geometry error, or partly/mostly a crown-definition measurement artifact?

B. Test 4 "too thin"
   Can the author-visible thinness be detected by width / silhouette / volume metrics absent from the old QA?

C. Test 3 chest problem
   Can chest/ribcage/front-silhouette metrics distinguish Test 3 from the author-approved chest result in Test 4?

D. Face Reference indirect influence
   Does structural-crown / head-shell analysis explain the repeated apparent head-ratio behavior without claiming Face Reference is direct Body Authority?
```

No Test 5 should be designed until these are measured under Audit v2 and compared to the author evaluations.

---

## 12. Fixed work order after this history checkpoint

The author fixed the next sequence as:

```text
1. Freeze Audit v2 specification.
2. Measure Face Reference with v2.
3. Measure active Body Guide with v2.
4. Re-measure Test 3 with v2.
5. Re-measure Test 4 with v2.
6. Check agreement with author evaluation.
7. Disclose the results.
8. Obtain explicit approval only for QA-gate changes that are actually necessary.
9. Only after that may Test 5 begin.
```

Rules for this stage:

- Audit v2 is diagnostic first; it does not silently rewrite Authority.
- Existing Body Geometry Authority, Face Identity Authority, Master text, generator setup, and QA gates stay unchanged while measurements are being established.
- Old/pre-v2 numeric results remain historical data and must not be overwritten to make them look as if they used v2.
- Any future gate change requires a separately disclosed diff and explicit author approval.
- Test 5 is blocked until the sequence above reaches step 8.

---

## 13. Repository state at this checkpoint

Remote `main` immediately before creating this history record:

```text
fa1cd912b48b477897a2c150c33bbc738fbd4210
Normalize YURA Test 4 invariant punctuation
```

This history checkpoint itself must add only this file and must not modify existing Authority, benchmark configuration, QA code, prompt compiler, runner, or unrelated manuscript files.
