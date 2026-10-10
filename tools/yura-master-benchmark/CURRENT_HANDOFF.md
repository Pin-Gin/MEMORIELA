# YURA Master Benchmark — Current Handoff

Status: **ACTIVE / AUTHOR-SELECTED WORKING MASTER / BODY GEOMETRY REFINEMENT / COMPOSITION BLOCKED**

This file is operational documentation only. It is not a YURA visual Authority.

## Scope lock

Current scope is YURA Master image completion only.

Do not begin uniforms, outfit Masters, pose packs, other characters, SHIORI/MIO work, story work, or downstream Production work unless the author explicitly redirects the project.

Do not alter or touch:

`manuscript/episode-001/EP001_DRAFT.txt`

Do not use `git reset --hard` and do not force-push.

## Current Git-era checkpoint

The completed 10-run fixed-condition variance study used:

```text
generation baseline commit
cc38457dc39e509adcd44da10c75f354c49c8844

sealed_authority_bundle_sha256
11f3626d7eb140cec8f344fa5e78ac8258861d6a45ef648922bd42dc037f4b28
```

Full result:

`tools/yura-master-benchmark/VARIANCE_STUDY_RESULT_20261011.md`

## Working Master selected

The author selected variance-study **Sample 9** as the current visual Master baseline.

Canonical target path:

`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

The selection is fixed. The exact Sample 9 original local RAW is now committed there unchanged; do not substitute another sample or derivative.

Working Master binary commit:

```text
c20ffc31fe5ccd16323ce36b129af93014d269ee
```

The previously recorded `b804...` SHA belonged to the chat-upload copy. The canonical original local run artifact / committed Master SHA is the value below.

RAW SHA-256:

```text
81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
```

Sample 9 was the author's best-balanced image of the ten-run series and received PASS for:

```text
hair length
skin
chest
knee position
thigh feminine volume/curve
overall leg visual balance
overall build
```

Detailed status:

`visuals/yura/identity/master/YURA_VISUAL_MASTER_STATUS.md`

This is an author-selected **working Master visual baseline**.

Do not falsely relabel its current numeric Body Geometry result as PASS.

Production Authority switch and final Composition remain blocked.

## Current unresolved geometry

The ten-run study produced:

```text
RAW success                  10 / 10
Official Body PASS            0 / 10
Visual all-PASS               4 / 10
Full PASS                     0 / 10

Head best mean              ≈ 7.036
Boundary best mean          ≈ 48.628%
Guide boundary               53.7037%
Inseam best mean            ≈ 51.372%
Target                        46.0–46.5%
Chin→boundary mean          ≈ 2.421 heads
Target                        2.7985–2.942 heads
```

The dominant remaining failure is systematic:

```text
crotch/pelvis boundary too high
-> torso/chin→boundary too short
-> inseam too long
```

Do not respond by lowering the 7.2 target or recalibrating the existing Body gate without explicit author instruction.

## Hair decision

The author wants the Sample 9 hair **slightly longer**.

Frozen intent:

```text
same hair identity
slightly longer only
reach the waist area more clearly
not dramatically longer
not substantially below the waist
```

This is approved but deliberately deferred from the next Body test so that the next paid RAW remains one-hypothesis.

## Active next hypothesis

The only active next hypothesis is:

> Can an explicit normalized crotch/pelvis boundary anchor at the approved Body Guide position make an edit of the Sample 9 working Master honor the intended upper/lower-body structural split without redesigning the already-approved visual traits?

Detailed preregistration:

`tools/yura-master-benchmark/TEST6_PELVIS_BOUNDARY_LOCK_SPEC_20261011.md`

Target anchor:

```text
boundary from structural crown = 53.7037% of crown→soles
equivalent crotch→soles        = 46.2963%
boundary definition            = central medial-thigh bifurcation / upper-lower body boundary
garment-line authority         = DENIED
```

## Next implementation rule

Do not make another paid call until Test 6 implementation is reviewed against the preregistered spec.

When Test 6 is implemented:

```text
working Master Sample 9 = visual/edit baseline
Body Guide              = geometry authority
Face Reference          = face identity authority if needed by the implementation
only causal intervention = explicit normalized pelvis/boundary lock
hair-length increase     = NOT part of Test 6
Composition              = deferred
```

Run free preflight before any paid image call.

Then run exactly one paid Test 6 RAW, measure it, and record one decision.

## Mandatory preservation

Current official Body QA remains unchanged unless the author explicitly orders a recalibration:

```text
head target 7.2
acceptable head 7.1–7.3
inseam 46.0–46.5%
>=47.0% hard fail
chin→boundary 2.7985–2.942 heads
structural crown uncertainty
crotch/pelvis boundary uncertainty
3×3 uncertainty combination
REVIEW_OVERLAP blocks Composition
```

Current author visual gates remain relevant:

```text
overall build
chest
hair
thigh feminine volume/curve
knee position
overall leg vertical balance
skin
```

## Composition

Composition remains blocked until the Body Geometry decision allows it.

Do not use Composition to repair anatomy.
