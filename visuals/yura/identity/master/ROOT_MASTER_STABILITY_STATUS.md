# YURA ROOT MASTER STABILITY STATUS

Status: **FACE_ROOT_CREATION_READY**

## Current state
`FACE_ROOT_MASTER = READY_TO_CREATE`
`FACE_ANCHORED_ROOT_MASTER = BLOCKED_PENDING_FACE_ROOT_APPROVAL`
`TEXT_ONLY_ROOT_FINAL_VERIFICATION = DEFERRED_UNTIL_FACE_FIRST_STABILIZATION`
`BODY_VIEW_MASTER = BLOCKED`

## Reason for workflow transition
Repeated protected-domain drift was observed in full-body TEXT_ONLY runs, especially FACE / EAR identity stability, while rendering also drifted toward washed-out / airbrush-dominant high-key output.

The current workflow therefore separates the problems:
- FACE / EYE / EAR identity is stabilized first through a dedicated Face Root carrier
- Rendering/touch is hardened in the YURA rendering compilation contract and all active payloads
- full-body Root is then generated with the approved Face Root as FACE_DETAIL_REFERENCE
- final reference-free TEXT_ONLY verification remains a later required step

Failed prior candidates remain rejected and are not references.

## Face Root stage
Active next submode:
`TEXT_ONLY_FACE_ROOT_MASTER`

Execution:
- `visuals/yura/execution/face-root/PAYLOAD.txt`
- `visuals/yura/execution/face-root/RUN.md`
- `visuals/yura/execution/face-root/SOURCE_LOCK.md`

QA:
`visuals/yura/qa/FACE_ROOT_QA.md`

Generation-time visual references:
`NONE`

Adoption target after explicit author approval:
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

Declared later-use role:
`FACE_DETAIL_REFERENCE`

## Face-anchored full-body stage
Blocked until Face Root is approved, registered, hash-locked, and the actual image is available to generation.

Submode:
`FACE_ANCHORED_ROOT_MASTER`

Only approved Face Root may be attached, and only as FACE_DETAIL_REFERENCE.

The Face Root must not control BODY, full hair length, clothing, pose, or rendering style.

## Rendering stability state
The YURA rendering adapter now requires payloads to preserve:
- clearly readable fine 2D-anime linework
- soft cel / grouped shadow shapes
- mild diffuse gradients only as support
- low-to-medium, not ultra-low, contrast
- white-background separation
- grouped anime hair masses
- matte / low-gloss quality
- no washed-out / watercolor-like / pastel-faded / ethereal-faded drift

`BRIGHT != WASHED_OUT`
`SOFT != AIRBRUSH_ONLY`
`FINE_LINE != INVISIBLE_LINE`

## Final TEXT_ONLY objective
A passing Face-Anchored Root is an intermediate stabilization result, not final TEXT_ONLY completion.

After Face Root and full-body identity / rendering are author-approved and stable, return to:
`TEXT_ONLY_ROOT_MASTER`

Final verification requirements remain:
- generation-time visual references = NONE
- Face Root not attached
- face-anchored Root not attached
- repository Root Master PNG not attached
- exact fixed text-only payload
- minimum 3 valid independent runs; preferred 5
- all protected domains stable
- explicit author approval

## Next action
Generate a single `TEXT_ONLY_FACE_ROOT_MASTER` candidate using the current Face Root payload and no image reference.

Do not start `FACE_ANCHORED_ROOT_MASTER` until the author explicitly approves a Face Root and it is Git-registered.
