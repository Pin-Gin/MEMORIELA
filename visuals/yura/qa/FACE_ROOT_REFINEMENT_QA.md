# YURA FACE ROOT REFINEMENT QA

Status: **PROTECTED / MANDATORY FOR FACE_ROOT_GEOMETRY_REFINEMENT**

Purpose:
EAR geometry correction after an eligible Face Root candidate edit, while re-validating all protected Face Root domains.

## Gate 0 — Execution integrity
PASS only if:
- submode = `FACE_ROOT_GEOMETRY_REFINEMENT`
- exact `visuals/yura/execution/face-root-refinement/PAYLOAD.txt` used
- exact one eligible `EDIT_SOURCE_CARRIER` supplied
- all visual Reference roles = NONE
- edit-source runtime SHA-256 recorded
- `RUN.md` controller-only
- `SOURCE_LOCK.md` current
- no Gate / QA / controller / retry text in generation semantics
- exactly one YURA / one face / one canvas / one composition

## Gate 1 — Input eligibility
PASS only if the input candidate was classified `REFINEMENT_ELIGIBLE` by `FACE_ROOT_QA.md` before the edit.

Required prior state:
- FACE PASS
- EYE PASS
- HAIR FRAMING PASS
- SKIN PASS
- RENDERING PASS
- composition PASS
- at least one ear observable
- EAR geometry FAIL only
- no other protected-domain FAIL

If not:
`REFINEMENT_QA = FAIL`

## Gate 2 — FACE
PASS:
- small soft-oval face
- standard-to-slightly-short vertical length
- vertically compact
- slightly narrow width
- modest cheek softness
- compact lower face
- small narrow softly rounded chin
- no round-face drift
- no oblong / fashion-model-long drift
- no extreme V-line

Any material change away from the protected FACE target is FAIL.

## Gate 3 — EYE
PASS:
- blue-gray only with clear gray component
- mild horizontally elongated almond geometry
- restrained vertical height
- visible sclera on both sides
- neutral to very slightly downturned outer corners
- stable bilateral identity

Any material EYE identity drift is FAIL.

## Gate 4 — EAR — HARD
PASS:
- ears read slightly small
- vertical length approximately 28–30% of forehead-to-chin face vertical length
- restrained projection
- approximately 5–10 degree posterior tilt when observable
- no visibility-driven enlargement / lengthening / outward movement / camera-facing rotation
- bilateral equal exposure not required

Immediate FAIL:
- materially oversized ear
- elongated ear
- flared / projected ear
- visibility-driven geometry compensation
- FACE or HAIR changed merely to expose the ear

At least one ear must be sufficiently observable for adoption suitability.

## Gate 5 — Hair framing
PASS:
- silver-white only
- thin long separated fringe
- forehead partly visible
- long side sections frame cheeks / jaw / neck
- no ornament / ribbon / clip / headband
- face framing does not widen or round the face
- no hair-identity change introduced by the edit

## Gate 6 — SKIN
PASS:
- bright fair / slightly white-leaning
- subtle natural blood color
- no white clipping
- matte / smooth anime surface

## Gate 7 — RENDERING
PASS only if:
- unmistakable high-quality 2D anime illustration
- clean fine but clearly readable linework
- linework remains visible
- soft cel / grouped shadow shapes remain readable
- diffuse gradients are supporting, not dominant airbrush rendering
- low-to-medium contrast, not washed-out ultra-low contrast
- white-background separation between face / skin / silver-white hair / linework remains clear
- hair reads as grouped anime masses, not translucent fiber haze
- matte / low-gloss
- not watercolor-like / pastel-faded / ethereal-faded

HARD FAIL:
- photoreal
- semi-photoreal
- live-action
- CGI / 3D / PBR
- photographic skin / hair

## Gate 8 — Composition / single-image suitability
PASS only if:
- front-facing
- head vertical
- face and head fully readable
- head top not cropped
- no body pose or outfit dominates the image
- no text / label / panel
- exactly one YURA / one canvas / one composition
- no before / after pair or comparison layout

## Decision
`PASS_FOR_AUTHOR_REVIEW` only if Gates 0–8 all PASS.

If any Gate fails:
- `ACCEPTANCE_ALLOWED = NO`
- output remains `REJECTED CANDIDATE`
- do not promote to Authority
- do not use the failed refinement output as the next edit source

No refinement output becomes Face Root Authority without explicit author approval and Git registration.
