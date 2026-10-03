# YURA ROOT MASTER STABILITY STATUS

Status: **FACE_ROOT_REFINEMENT_ROUTE_READY**

## Current state
`TEXT_ONLY_FACE_ROOT_MASTER = READY`
`FACE_ROOT_GEOMETRY_REFINEMENT = READY_FOR_ELIGIBLE_CANDIDATE`
`FACE_ROOT_MASTER = NOT_APPROVED`
`FACE_ANCHORED_ROOT_MASTER = BLOCKED_PENDING_FACE_ROOT_APPROVAL`
`TEXT_ONLY_ROOT_FINAL_VERIFICATION = DEFERRED_UNTIL_FACE_FIRST_STABILIZATION`
`BODY_VIEW_MASTER = BLOCKED`

## Reason for workflow transition
Repeated protected-domain drift was observed in Face Root text-only runs, specifically EAR vertical elongation despite protected EAR size rules and a dedicated EAR emphasis recompile.

The current workflow therefore separates the Face Root process into:
- initial `TEXT_ONLY_FACE_ROOT_MASTER` generation with no image input
- QA classification
- optional `FACE_ROOT_GEOMETRY_REFINEMENT` only when EAR geometry is the sole protected-domain failure and the candidate is otherwise valid
- explicit author approval and Git registration only after a candidate fully passes

This refinement route does not change YURA EAR Canon.
Protected EAR target remains approximately 28–30% of forehead-to-chin face vertical length, slightly small, restrained in projection, with approximately 5–10 degree posterior tilt when observable.

## Edit-source boundary
A refinement input candidate is used only as runtime `EDIT_SOURCE_CARRIER`.

It is:
- NOT Authority
- NOT Identity Reference
- NOT Production Reference
- NOT Canon evidence

No failed or intermediate image is added to the Face Root Authority slot merely because it is used as an edit-source carrier.
Only a fully passing image may be registered after explicit author approval.

## TEXT_ONLY Face Root stage
Submode:
`TEXT_ONLY_FACE_ROOT_MASTER`

Execution:
- `visuals/yura/execution/face-root/PAYLOAD.txt`
- `visuals/yura/execution/face-root/RUN.md`
- `visuals/yura/execution/face-root/SOURCE_LOCK.md`

QA:
`visuals/yura/qa/FACE_ROOT_QA.md`

Generation-time visual references:
`NONE`

Possible QA classifications:
- `PASS_FOR_AUTHOR_REVIEW`
- `REFINEMENT_ELIGIBLE`
- `REJECTED_CANDIDATE`

## Face Root refinement stage
Submode:
`FACE_ROOT_GEOMETRY_REFINEMENT`

Profile:
`visuals/yura/generation/master-creation/FACE_ROOT_GEOMETRY_REFINEMENT.md`

Execution:
- `visuals/yura/execution/face-root-refinement/PAYLOAD.txt`
- `visuals/yura/execution/face-root-refinement/RUN.md`
- `visuals/yura/execution/face-root-refinement/SOURCE_LOCK.md`

QA:
`visuals/yura/qa/FACE_ROOT_REFINEMENT_QA.md`

Visual Reference roles:
`NONE`

Required runtime edit source:
exactly one `REFINEMENT_ELIGIBLE` candidate as `EDIT_SOURCE_CARRIER`.

A refinement output is a new candidate and all Face Root protected domains are re-QA'd.
A failed refinement output must not become the next edit source.

## Face Root adoption target
Only after applicable QA PASS + explicit author approval:
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`
- `visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

Declared later-use role after adoption:
`FACE_DETAIL_REFERENCE`

## Face-anchored full-body stage
Blocked until Face Root is approved, registered, hash-locked, and the actual image is available to generation.

Submode:
`FACE_ANCHORED_ROOT_MASTER`

Only approved Face Root may be attached, and only as FACE_DETAIL_REFERENCE.

The Face Root must not control BODY, full hair length, clothing, pose, or rendering style.

## Rendering stability state
The YURA rendering adapter requires payloads to preserve:
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

Rendering FAIL blocks Face Root refinement eligibility.

## Final TEXT_ONLY objective
A passing Face-Anchored Root is an intermediate stabilization result, not final TEXT_ONLY completion.

After Face Root and full-body identity / rendering are author-approved and stable, return to:
`TEXT_ONLY_ROOT_MASTER`

Final verification requirements remain:
- generation-time visual references = NONE
- edit source carrier = NONE
- Face Root not attached
- face-anchored Root not attached
- repository Root Master PNG not attached
- exact fixed text-only payload
- minimum 3 valid independent runs; preferred 5
- all protected domains stable
- explicit author approval

## Next action
Classify the next Face Root candidate with `FACE_ROOT_QA.md`.

- PASS → author review
- EAR-only eligible geometry FAIL → `FACE_ROOT_GEOMETRY_REFINEMENT`
- any other FAIL → reject and do not use as edit source

Do not start `FACE_ANCHORED_ROOT_MASTER` until the author explicitly approves a Face Root and it is Git-registered.
