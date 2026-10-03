# YURA MASTER CREATION FLOW

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

Purpose:
YURA Face Root / full-body Root / final TEXT_ONLY stability / BODY View Mastersを、依存順序と実行境界を崩さず作成する。

## Required order
1. `TEXT_ONLY_FACE_ROOT_MASTER`
2. candidate classification by `FACE_ROOT_QA.md`
3. if direct PASS: author review; if eligible EAR-only geometry FAIL: `FACE_ROOT_GEOMETRY_REFINEMENT`
4. author-approved and Git-registered Face Root
5. `FACE_ANCHORED_ROOT_MASTER`
6. author-approved stable face-anchored full-body Root
7. `TEXT_ONLY_ROOT_MASTER` final reference-free stability verification
8. explicit author approval of TEXT_ONLY Root stability
9. `BODY_VIEW_MASTER`

Do not skip forward.

The Face Root is an intermediate identity-stabilization carrier.
It does not make a face-anchored full-body generation count as TEXT_ONLY success.

## Submode 1 — TEXT_ONLY_FACE_ROOT_MASTER
Purpose:
画像参照を使わず、FACE / EYE / EAR / face-framing hair / SKIN / RENDERING text AuthoritiesからYURAのFace Root候補を先に作る。

Generation-time visual references:
`NONE`

Edit source carrier:
`NONE`

Mandatory profile:
`../generation/master-creation/TEXT_ONLY_FACE_ROOT_MASTER.md`

Mandatory execution package:
- `../execution/face-root/PAYLOAD.txt` — generation semantics only
- `../execution/face-root/RUN.md` — controller only
- `../execution/face-root/SOURCE_LOCK.md` — source lock only

Required QA:
`../qa/FACE_ROOT_QA.md`

Possible outcomes:
- `PASS_FOR_AUTHOR_REVIEW`
- `REFINEMENT_ELIGIBLE`
- `REJECTED_CANDIDATE`

`REFINEMENT_ELIGIBLE` does not mean accepted, approved, Authority, or Reference.
It only allows the protected refinement route below.

## Submode 1R — FACE_ROOT_GEOMETRY_REFINEMENT
Purpose:
EAR geometry alone has failed while all other protected Face Root domains pass, and the ear is observable. Use the same candidate image as a non-reference edit-source carrier so ear size / placement / projection / tilt can be corrected in the face's existing spatial coordinate system.

Generation-time visual references:
`NONE`

Required non-reference edit source:
exactly one Gate-eligible Face Root candidate as `EDIT_SOURCE_CARRIER`.

The edit source is:
- NOT Authority
- NOT Identity Reference
- NOT Production Reference
- NOT Canon evidence

Mandatory profile:
`../generation/master-creation/FACE_ROOT_GEOMETRY_REFINEMENT.md`

Mandatory execution package:
- `../execution/face-root-refinement/PAYLOAD.txt`
- `../execution/face-root-refinement/RUN.md`
- `../execution/face-root-refinement/SOURCE_LOCK.md`

Required QA:
`../qa/FACE_ROOT_REFINEMENT_QA.md`

Refinement does not claim pixel-perfect preservation outside EAR.
The output is a new candidate and all protected Face Root domains are re-QA'd.

A failed refinement output must not become the next edit source.
A repeated refinement attempt, when allowed, starts again from the same originally eligible edit-source candidate using the unchanged active refinement payload.

Adoption target after QA PASS + explicit author approval:
- `../identity/master/face-root/YURA_FACE_ROOT.png`
- `../identity/master/face-root/YURA_FACE_ROOT.md`

Declared later-use role after adoption only:
`FACE_DETAIL_REFERENCE`

## Submode 2 — FACE_ANCHORED_ROOT_MASTER
Allowed only when the Face Root is author-approved, Git-registered, hash-locked, and the actual image is available to generation.

Purpose:
Face RootをFACE_DETAIL_REFERENCEとして実際に画像生成へ渡し、FACE / EYE / EAR identityを視覚キャリアで固定しながら、BODY / full HAIR / validation clothing / pose / renderingをテキストAuthorityから全身Rootへ展開する。

Required visual reference:
exactly one approved Face Root as `FACE_DETAIL_REFERENCE`.

Mandatory profile:
`../generation/master-creation/FACE_ANCHORED_ROOT_MASTER.md`

Mandatory execution package:
- `../execution/face-anchored-root/PAYLOAD.txt`
- `../execution/face-anchored-root/RUN.md`
- `../execution/face-anchored-root/SOURCE_LOCK.md`

Required QA:
`../qa/FACE_ANCHORED_ROOT_QA.md`

Face Root scope must not leak into BODY, full hair length, outfit, pose, or rendering authority.

## Submode 3 — TEXT_ONLY_ROOT_MASTER
Purpose:
Face-first identity stabilization後、画像参照を完全に外し、現行Text Authorityからコンパイルした固定Payloadだけで最終TEXT_ONLY再現安定性を検証する。

Generation-time visual references:
`NONE`

Edit source carrier:
`NONE`

Post-generation visual comparison reference for the current completion target:
`NONE`

Mandatory profile:
`../generation/master-creation/TEXT_ONLY_ROOT_MASTER.md`

Mandatory execution package:
- `../execution/text-only-root/PAYLOAD.txt` — image-generation semantic input only
- `../execution/text-only-root/RUN.md` — controller only
- `../execution/text-only-root/SOURCE_LOCK.md` — source-integrity controller only

Required QA:
`../qa/ROOT_MASTER_STABILITY_QA.md`

The Face Root, face-anchored Root, repository Root Master PNG, previous generations, and refinement edit-source carriers must not enter this final TEXT_ONLY generation call.

## Submode 4 — BODY_VIEW_MASTER
Allowed only when:
- final Root stability status = `APPROVED`
- approved Face Root exists and is registered

Purpose:
approved Root + Face identityを保持したままBODY projection anchorsを角度別に作成する。

## Promotion rule
No candidate becomes Authority because it looks good or because it was used as an edit source.

Promotion requires:
1. applicable QA
2. explicit author approval
3. canonical Git placement
4. hash / source registration
5. manifest update
6. Gate revalidation
