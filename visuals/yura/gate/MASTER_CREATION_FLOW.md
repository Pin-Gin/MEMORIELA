# YURA MASTER CREATION FLOW

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

Purpose:
YURA Root Master / Face Master / BODY View Mastersを、依存順序を崩さず作成する。

## Required order
1. `TEXT_ONLY_ROOT_MASTER`
2. author-approved stable Root Master
3. `FACE_MASTER`
4. author-approved Face Master
5. `BODY_VIEW_MASTER`

Do not skip forward.

## Submode 1 — TEXT_ONLY_ROOT_MASTER
Purpose:
画像参照を一切使わず、現行YURA Text Authorityだけで正面YURAが安定再現できるか検証し、Root Master候補を作成する。

Generation-time visual references:
`NONE`

Required semantic text input:
`../generation/master-creation/TEXT_ONLY_ROOT_MASTER.md`

Required QA:
`../qa/ROOT_MASTER_STABILITY_QA.md`

Current Root Master image may be used only after candidate generation as:
`POST_GENERATION_COMPARISON_REFERENCE`

It must not be attached to or supplied to the generation call.

## Submode 2 — FACE_MASTER
Allowed only when:
`../identity/master/ROOT_MASTER_STABILITY_STATUS.md`
is `APPROVED`.

Purpose:
approved stable Root MasterからFace Close-up Masterを作成する。

Candidate remains non-authority until explicit author approval and Git registration.

## Submode 3 — BODY_VIEW_MASTER
Allowed only when:
- Root Master stability status = `APPROVED`
- approved Face Master exists and is registered in the Authority Manifest

Purpose:
approved Root + Face identityを保持したまま、BODY projection anchorを角度別に作成する。

Do not create BODY View Masters from an unstable Root or before Face Master adoption.

## Promotion rule
No Master candidate becomes Authority because it looks good.

Promotion requires:
1. applicable QA
2. explicit author approval
3. canonical Git placement
4. hash / source registration
5. manifest update
6. Gate revalidation
