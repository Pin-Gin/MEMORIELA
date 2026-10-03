# YURA MASTER CREATION FLOW

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

Purpose:
YURA Face Root / full-body Root / final TEXT_ONLY stability / BODY View Mastersを、依存順序と実行境界を崩さず作成する。

## Required order
1. `TEXT_ONLY_FACE_ROOT_MASTER`
2. author-approved and Git-registered Face Root
3. `FACE_ANCHORED_ROOT_MASTER`
4. author-approved stable face-anchored full-body Root
5. `TEXT_ONLY_ROOT_MASTER` final reference-free stability verification
6. explicit author approval of TEXT_ONLY Root stability
7. `BODY_VIEW_MASTER`

Do not skip forward.

The Face Root is an intermediate identity-stabilization carrier.
It does not make a face-anchored full-body generation count as TEXT_ONLY success.

## Submode 1 — TEXT_ONLY_FACE_ROOT_MASTER
Purpose:
画像参照を使わず、FACE / EYE / EAR / face-framing hair / SKIN / RENDERING text AuthoritiesからYURAのFace Root候補を先に作る。

Generation-time visual references:
`NONE`

Mandatory profile:
`../generation/master-creation/TEXT_ONLY_FACE_ROOT_MASTER.md`

Mandatory execution package:
- `../execution/face-root/PAYLOAD.txt` — generation semantics only
- `../execution/face-root/RUN.md` — controller only
- `../execution/face-root/SOURCE_LOCK.md` — source lock only

Required QA:
`../qa/FACE_ROOT_QA.md`

Adoption target after QA PASS + explicit author approval:
- `../identity/master/face-root/YURA_FACE_ROOT.png`
- `../identity/master/face-root/YURA_FACE_ROOT.md`

Declared later-use role:
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

The Face Root, face-anchored Root, repository Root Master PNG, and previous generations must not enter this final TEXT_ONLY generation call.

## Submode 4 — BODY_VIEW_MASTER
Allowed only when:
- final Root stability status = `APPROVED`
- approved Face Root exists and is registered

Purpose:
approved Root + Face identityを保持したままBODY projection anchorsを角度別に作成する。

## Promotion rule
No candidate becomes Authority because it looks good.

Promotion requires:
1. applicable QA
2. explicit author approval
3. canonical Git placement
4. hash / source registration
5. manifest update
6. Gate revalidation
