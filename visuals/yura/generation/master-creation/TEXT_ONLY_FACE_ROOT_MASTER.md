# YURA TEXT-ONLY FACE ROOT MASTER CREATION PROFILE

Status: **PROTECTED / FIXED INPUT PROFILE / FACE-FIRST IDENTITY STABILIZATION**

Master Creation Submode:
`TEXT_ONLY_FACE_ROOT_MASTER`

Purpose:
全身Rootより先に、画像参照なしでYURAのFACE / EYE / EAR / face-framing hair identityを高解像度のFace Root候補として確立する。

This submode creates an identity carrier candidate for later full-body generation.
It does not define BODY, full hair length, outfit, or pose authority.

## Generation-time reference policy
`VISUAL_REFERENCES_ALLOWED = NONE`

No image may be supplied to the Face Root generation execution.

Edit source carrier:
`NONE`

## Authority resolution inputs
Resolve only the protected sources needed for the Face Root:
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md`
- `visuals/yura/identity/face/FACE_SPEC.md`
- `visuals/yura/identity/ears/EAR_SPEC.md`
- `visuals/yura/identity/eyes/EYE_SPEC.md`
- `visuals/yura/identity/hair/HAIR_SPEC.md` — face-framing / color / material only
- `visuals/yura/identity/skin/SKIN_SPEC.md`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md`
- `visuals/CHARACTER_RENDERING_STYLE.md`

Do not import BODY, full hair-length, validation-clothing, pose, or production-reference semantics into the Face Root generation payload.

## Execution package
Image-generation semantic input only:
`visuals/yura/execution/face-root/PAYLOAD.txt`

Controller only:
`visuals/yura/execution/face-root/RUN.md`

Source-integrity lock only:
`visuals/yura/execution/face-root/SOURCE_LOCK.md`

Only `PAYLOAD.txt` enters the generation-facing semantic context.

## Candidate target
- exactly one YURA face
- front-facing
- head vertical
- head top fully visible
- crop concentrated on head / face / neck with only minimal upper-shoulder boundary
- white / warm-white background
- neutral to extremely subtle soft expression
- no ornament / jewelry
- no generation-time image reference

## Ear observability rule
Ear visibility is not a generation target and must never cause geometry compensation.

For direct adoption as a Face Root Master, at least one ear must be sufficiently observable to evaluate protected EAR geometry without enlarging, rotating, moving, or forcing bilateral exposure.

A candidate with both ears naturally hidden may still be a valid YURA face, but it is **NOT SUITABLE FOR FACE_ROOT ADOPTION** because it cannot anchor EAR geometry.
It is also not refinement-eligible merely because the ear is hidden; the refinement route must not force exposure.

## Refinement eligibility boundary
After generation, `FACE_ROOT_QA.md` may classify the candidate as `REFINEMENT_ELIGIBLE` only when:
- FACE = PASS
- EYE = PASS
- HAIR FRAMING = PASS
- SKIN = PASS
- RENDERING = PASS
- single-image / composition constraints = PASS
- at least one ear is observable
- EAR geometry alone materially fails protected size / placement / projection / tilt
- no other protected-domain FAIL exists

`REFINEMENT_ELIGIBLE` means only that the candidate may be used by the protected `FACE_ROOT_GEOMETRY_REFINEMENT` route as a non-reference `EDIT_SOURCE_CARRIER`.

It does not mean:
- accepted
- author-approved
- Authority
- Identity Reference
- Production Reference

If any non-EAR protected domain fails, the candidate is rejected and not eligible for refinement.

## Adoption target
After QA PASS and explicit author approval, the adopted artifact is:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

Its manifest is:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

Declared role when used by later full-body generation:
`FACE_DETAIL_REFERENCE`

The Face Root may control only:
- face outline
- cheek / chin balance
- eye identity / placement
- nose / mouth placement
- ear geometry
- face-framing hair boundary

It must not control:
- BODY ratio / dimensions
- chest
- shoulder width
- pelvis / legs
- full hair length / total full-body hair silhouette
- outfit
- full-body pose
- scene

## Candidate status
Every output is `CANDIDATE / NOT AUTHORITY` until explicit author approval and Git registration.
A candidate used as an `EDIT_SOURCE_CARRIER` remains `NOT AUTHORITY / NOT REFERENCE`.
