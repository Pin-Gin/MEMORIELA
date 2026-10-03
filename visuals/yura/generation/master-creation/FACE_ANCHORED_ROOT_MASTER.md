# YURA FACE-ANCHORED ROOT MASTER CREATION PROFILE

Status: **PROTECTED / BLOCKED UNTIL FACE ROOT ADOPTED**

Master Creation Submode:
`FACE_ANCHORED_ROOT_MASTER`

Purpose:
作者承認済みFace RootをFACE_DETAIL_REFERENCEとして実際に画像生成へ渡し、FACE / EYE / EAR identityを視覚キャリアで固定しながら、BODY / full hair length / validation clothing / pose / compositionを保護テキストから全身Rootへ展開する。

This is not TEXT_ONLY.

## Required visual reference
Exactly one:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

Role:
`FACE_DETAIL_REFERENCE`

The actual approved image must be available to the image-generation execution.
Git existence alone is insufficient.

## Reference scope
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
- pelvis / hips / legs
- full hair length / full-body hair silhouette
- validation clothing
- full-body pose
- scene

## Text authority scope
The full-body text payload controls:
- BODY
- full HAIR length / mass / silhouette
- SKIN
- validation clothing
- full-body pose / composition
- RENDERING

Precise FACE / EYE / EAR text rules remain active validation constraints and must not conflict with the approved Face Root.

## Execution package
Image-generation semantic input:
`visuals/yura/execution/face-anchored-root/PAYLOAD.txt`

Controller only:
`visuals/yura/execution/face-anchored-root/RUN.md`

Source / reference lock only:
`visuals/yura/execution/face-anchored-root/SOURCE_LOCK.md`

Required QA:
`visuals/yura/qa/FACE_ANCHORED_ROOT_QA.md`

## Permission
Until the approved Face Root PNG and its manifest are present and the SOURCE_LOCK records their exact hash:
`GENERATION_ALLOWED = NO`

## Candidate status
Every full-body output remains `CANDIDATE / NOT AUTHORITY` until QA PASS and explicit author approval.

## Final TEXT_ONLY objective
A stable Face-Anchored Root is an intermediate identity-stabilization carrier.
It does not count as final TEXT_ONLY success.
After identity / BODY / rendering are stable, `TEXT_ONLY_ROOT_MASTER` remains the reference-free final verification route.
