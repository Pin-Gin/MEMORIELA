# YURA MASTER CREATION FLOW

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

Purpose:
YURA full-body Root / final TEXT_ONLY stability / BODY View Mastersを、依存順序と実行境界を崩さず作成する。

## Required order
1. `TEXT_ONLY_ROOT_MASTER` final reference-free stability verification
2. explicit author approval of TEXT_ONLY Root stability
3. `BODY_VIEW_MASTER`

Do not skip forward.

## Submode 1 — TEXT_ONLY_ROOT_MASTER
Purpose:
画像参照を完全に外し、現行Text Authorityからコンパイルした固定Payloadだけで最終TEXT_ONLY再現安定性を検証する。

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

The repository Root Master PNG and previous generations must not enter this final TEXT_ONLY generation call.

## Submode 2 — BODY_VIEW_MASTER
Allowed only when:
- final Root stability status = `APPROVED`

Purpose:
approved Rootを保持したままBODY projection anchorsを角度別に作成する。

## Promotion rule
No candidate becomes Authority because it looks good.

Promotion requires:
1. applicable QA
2. explicit author approval
3. canonical Git placement
4. hash / source registration
5. manifest update
6. Gate revalidation
