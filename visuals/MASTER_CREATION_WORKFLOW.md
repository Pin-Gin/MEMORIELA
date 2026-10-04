# Character Visual Master Creation Workflow

Status: **ACTIVE WORKFLOW / REUSABLE ACROSS CHARACTERS**

This document records the workflow for creating high-quality character visual Masters while minimizing stochastic drift. It is a process document, not a character appearance Authority.

## Primary objective

Create a high-quality, author-approved character Master while keeping generation variance and unintended visual drift as small as practicable.

The workflow must optimize for both:

- **quality**: the resulting Master should look correct, attractive, coherent, and faithful to author intent;
- **stability**: repeated work should converge around the same identity and geometry rather than depending on lucky one-off generations.

Neither objective is sufficient alone. A stable but mediocre image is not a successful Master, and a beautiful one-off image that cannot be reproduced or audited is not a reliable Master.

## Additional objectives

The workflow also aims to:

1. **Convert subjective visual intent into measurable constraints where useful.**
   Author judgment remains final, but head ratio, body landmarks, internal proportions, composition, and other suitable properties should be measured when measurement improves repeatability.

2. **Separate independent variables.**
   Face Identity, Body Geometry, appearance text, Composition, rendering/style, and later local refinements should be treated as separate concerns so a change in one area does not silently change another.

3. **Keep author intent above generic defaults.**
   Generic anime anatomy, generic beauty conventions, or model defaults must not override character-specific author-approved geometry or identity.

4. **Prevent reference contamination.**
   Rejected or failed generated candidates are never promoted into visual Identity Authority merely because they exist. A failed RAW may be measured as a QA/calibration sample, but it is not a future appearance reference unless the author explicitly promotes it.

5. **Make every promotion auditable.**
   Active Authority files, hashes, benchmark inputs, QA results, Git commit, and author approval should make it possible to reconstruct why a Master was accepted.

6. **Use paid generation efficiently.**
   Local verification, sealed Authority assembly, prompt invariants, syntax checks, and free preflight should happen before paid model calls. Paid generations should be deliberate experiments with a clear hypothesis.

7. **Avoid solving composition by deforming anatomy.**
   Body Geometry is solved first. Final canvas occupancy and margins are solved afterward by deterministic whole-raster scaling and translation only.

8. **Support controlled iteration rather than prompt accumulation.**
   When a generation misses, diagnose the specific failure, change the corresponding Authority/gate, preflight again, and test one controlled RAW. Do not add unrelated instructions in response to every failure.

9. **Create a reusable method for the cast without copying character-specific values.**
   YURA, SHIORI, MIO, and later characters should use the same workflow architecture, but each character must have their own approved Face Identity, Body Geometry, numeric targets, and visual decisions. YURA-specific measurements must not automatically become SHIORI- or MIO-specific measurements.

## Core architecture

```text
Character-specific Authorities
  -> local Git / Authority verification
  -> sealed Authority bundle with hashes
  -> deterministic prompt compiler
  -> prompt invariant gate
  -> paid RAW generation
  -> measurable geometry / identity QA
  -> author visual review
  -> revise only the failed layer if necessary
  -> repeat until RAW is stable and high quality
  -> deterministic Composition postprocess
  -> final QA
  -> explicit author PASS
  -> Master promotion
  -> Master-derived production description
```

## Authority separation

Use separate sources for separate jobs.

```text
Face Identity Authority
  -> face identity only

Body Geometry Authority
  -> proportions, landmarks, silhouette geometry only

Visual Text Authority during Master construction
  -> character-specific textual appearance requirements

Composition Authority
  -> final canvas, occupancy, margins, centering

Rendering / shared style rules
  -> project-level rendering consistency where explicitly allowed
```

An Authority must not silently expand beyond its declared role.

## Body-geometry-first rule

For full-body Master construction, internal body geometry is resolved before final Composition.

The RAW generator should not be asked to alter anatomy to satisfy final canvas occupancy. Final Composition must be deferred until Body Geometry passes.

Where useful, Body Geometry should be represented by an explicit geometry guide image plus a text specification that names the same landmarks and numeric relationships. Important internal boundaries should be visible and labeled in the guide rather than left implicit.

## Measurement-driven calibration

Numeric targets are tools for reproducing author intent, not immutable truths.

A useful iteration pattern is:

```text
1. Define an initial author-approved range.
2. Generate one controlled RAW.
3. Measure the RAW.
4. Compare the measured geometry with author visual judgment.
5. If the image looks better than the current numeric target predicts,
   treat that as evidence that the numeric target may need recalibration.
6. Change the target only through explicit author approval.
7. Update Authority + QA + prompt invariants together.
8. Free-preflight the new state.
9. Generate one new paid RAW and test reproducibility.
```

This prevents a numeric gate from becoming detached from the actual visual goal.

A visually promising RAW may therefore be used as a **measurement/calibration sample** without becoming a visual reference or Master candidate by default.

## One-variable-at-a-time refinement

When a major layer is unstable, defer unrelated refinements.

Example:

```text
full-body geometry unstable
  -> stabilize full-body geometry first
  -> then refine local Face Identity issues
  -> then final Composition
  -> then final Master selection
```

This makes causality visible. If Face Identity and Body Geometry are changed simultaneously, a better or worse result cannot be attributed cleanly to either change.

## QA philosophy

Use both numeric and visual gates.

Numeric gates are good at detecting measurable drift. Visual review is required for properties that are not safely reducible to a single number.

A candidate can fail even if its headline number passes. For example, total head ratio may pass while torso distribution, waist position, knee placement, or silhouette remains wrong.

Conversely, if repeated author-approved visual judgments conflict with an existing numeric target, investigate the target instead of forcing the image to satisfy a bad number.

## Failed-candidate policy

A failed generated image:

- may be retained in benchmark run artifacts for diagnosis;
- may be measured to understand failure or calibrate numeric targets;
- must not become Face Identity or Body Geometry visual Authority automatically;
- must not be used as a future generation reference unless explicitly promoted by the author.

This policy minimizes drift caused by self-referential generations.

## Paid-run discipline

Before each paid RAW generation:

```text
Git state verified
Authority paths verified
Authority hashes sealed
prompt invariants PASS
forbidden/deferred data absent from RAW prompt
preflight reports paid_model_calls = 0
experiment purpose is explicit
```

After each paid RAW:

```text
measure first
review second
change only what the evidence supports
never normalize Composition before Body Geometry PASS
never auto-run another paid generation after a failure
```

## Composition rule

After Body Geometry passes, final Composition may use only deterministic whole-raster operations:

- uniform scale;
- x/y translation;
- crop/pad against the intended background/canvas.

Do not use Composition processing to reshape anatomy, regenerate the face, stretch body parts, warp, or inpaint the character.

## Promotion rule

A generated image is not a Master merely because it looks promising.

Master promotion requires:

```text
all required measurable gates PASS
required visual gates PASS
final Composition PASS
Authority provenance is known
run artifacts are bound to the exact RAW/final files
explicit author PASS
```

After promotion, production should use the approved Master image and Master-derived description according to the character lifecycle rules. Master-construction-only material should not remain an uncontrolled production input.

## Reuse for SHIORI, MIO, and later characters

Reuse the **architecture and discipline**, not YURA's character-specific geometry.

For each new character:

```text
1. establish Face Identity Authority;
2. establish character-specific Body Geometry guide + text;
3. label important internal boundaries explicitly;
4. define initial measurable ranges only where justified;
5. set up sealed preflight and prompt invariants;
6. generate one controlled RAW;
7. measure and compare against author judgment;
8. recalibrate character-specific numbers if the evidence supports it;
9. stabilize full-body generation;
10. refine local face/details afterward;
11. apply deterministic Composition;
12. promote only after explicit author PASS.
```

The expected benefit is that later characters start with a proven process rather than repeating YURA's exploratory failures.
