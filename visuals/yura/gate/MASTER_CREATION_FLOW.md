# YURA MASTER CREATION FLOW

Status: **PROTECTED / MANDATORY / FAIL-CLOSED**

Purpose:
YURA Root Master / Face Master / BODY View Mastersを、依存順序と実行境界を崩さず作成する。

## Required order
1. `TEXT_ONLY_ROOT_MASTER`
2. author-approved stable Root Master
3. `FACE_MASTER`
4. author-approved Face Master
5. `BODY_VIEW_MASTER`

Do not skip forward.

## Submode 1 — TEXT_ONLY_ROOT_MASTER
Purpose:
画像参照を使わず、現行Text Authorityからコンパイルした純粋な生成Payloadで、作者承認済み完成ターゲットをTEXT_ONLY再構築する。

Resolution / compile route:
```text
Protected Text Authorities
        ↓
SOURCE_LOCK.md
        ↓
PAYLOAD.txt
        ↓
Payload validation
        ↓
RUN.md controller validation
        ↓
one independent single-image call
        ↓
post-generation text-authority QA / acceptance classification
```

Generation-time visual references:
`NONE`

Post-generation visual comparison reference for the current completion target:
`NONE`

Mandatory execution package:
- `../execution/text-only-root/PAYLOAD.txt` — image-generation semantic input only
- `../execution/text-only-root/RUN.md` — controller only; never image-generation input
- `../execution/text-only-root/SOURCE_LOCK.md` — source-integrity controller only; never image-generation input

Required QA:
`../qa/ROOT_MASTER_STABILITY_QA.md`

For the current author-approved TEXT_ONLY completion target, the repository Root Master PNG is not loaded, inspected, described, or used as a generation or post-generation comparison reference.

## Submode 2 — FACE_MASTER
Allowed only when:
`../identity/master/ROOT_MASTER_STABILITY_STATUS.md`
is `APPROVED`.

Purpose:
approved stable Root MasterからFace Close-up Masterを作成する。

## Submode 3 — BODY_VIEW_MASTER
Allowed only when:
- Root Master stability status = `APPROVED`
- approved Face Master exists and is registered

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
