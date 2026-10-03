# YURA FACE ROOT QA

Status: **PROTECTED / MANDATORY FOR TEXT_ONLY_FACE_ROOT_MASTER**

Purpose:
全身生成前に使用するFACE_DETAIL_REFERENCE候補が、YURAのFACE / EYE / EAR identityとMatte Natural Anime renderingを高解像度で安定して保持しているかを判定する。

## Gate 0 — Execution integrity
PASS only if:
- submode = `TEXT_ONLY_FACE_ROOT_MASTER`
- exact `visuals/yura/execution/face-root/PAYLOAD.txt` used
- `RUN.md` controller-only
- `SOURCE_LOCK.md` current
- generation-time visual references = NONE
- one YURA / one face / one canvas / one composition
- no Gate / QA / controller / retry text in generation semantics

## Gate 1 — FACE
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

## Gate 2 — EYE
PASS:
- blue-gray only with clear gray component
- mild horizontally elongated almond geometry
- restrained vertical height
- visible sclera on both sides
- neutral to very slightly downturned outer corners
- stable bilateral identity

## Gate 3 — EAR — HARD
PASS:
- ears read slightly small
- vertical length approximately 28–30% of forehead-to-chin face vertical length
- restrained projection
- approximately 5–10 degree posterior tilt when observable
- no enlargement / lengthening / outward movement / camera-facing rotation for visibility
- bilateral equal exposure not required

Immediate FAIL:
- materially oversized ear
- elongated ear
- flared / projected ear
- visibility-driven geometry compensation

### Face Root adoption suitability
At least one ear must be sufficiently observable to evaluate its size / projection / tilt without any visibility-driven compensation.

If both ears are naturally hidden:
- this is not automatically an EAR identity failure
- but `FACE_ROOT_ADOPTION_SUITABILITY = FAIL`
- do not adopt that candidate as the Face Root carrier

## Gate 4 — Hair framing
PASS:
- silver-white only
- thin long separated fringe
- forehead partly visible
- long side sections frame cheeks / jaw / neck
- no ornament / ribbon / clip / headband
- face framing does not widen or round the face

Full hair length is out of scope for Face Root QA.

## Gate 5 — SKIN
PASS:
- bright fair / slightly white-leaning
- subtle natural blood color
- no white clipping
- matte / smooth anime surface

## Gate 6 — RENDERING
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

## Gate 7 — Master suitability
PASS only if:
- front-facing
- head vertical
- face and head fully readable
- head top not cropped
- no body pose or outfit dominates the image
- no text / label / panel
- at least one ear is evaluable without geometry compensation

## Decision
`PASS_FOR_AUTHOR_REVIEW` only if all protected identity gates and Master-suitability gate pass.

No candidate becomes Face Root Authority without explicit author approval and Git registration.
