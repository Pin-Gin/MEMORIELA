# YURA MASTER GENERATION LIFECYCLE

Status: **AUTHOR-APPROVED / ACTIVE**

## Purpose

YURAのMaster生成用仕様と、Master完成後の通常Production用Authorityを分離する。

## Phase A — Master generation

現在の
`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`
は、**OpenAI APIで高精度なYURA Master候補を再生成するためのMaster-generation API specification** と位置づける。

このファイルは、日常的なProduction画像生成の恒久Authorityではない。

Master生成時は、以下を分離して使用する。

- Face Identity: `visuals/yura/identity/face/YURA_FACE_REFERENCE.png` + `FACE_REFERENCE_RULES.md`
- Body Geometry: `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png` + `BODY_GEOMETRY_GUIDE.md`
- Composition: `visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md`
- Master-generation visual specification: `visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

`YURA_VISUAL_TEXT.md` はこのPhase Aでのみ直接Master-generation Authorityとして使用する。

## Phase B — Master promotion

候補画像がQAと作者確認を通過した場合のみ、新しいYURA Master画像へ昇格する。

予定Master画像:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

Master promotion前は、候補画像を通常ProductionのReferenceとして再利用しない。

## Phase C — Production description creation

Master画像確定後、**Master画像そのものをGPTベースの視覚確認で読み取り、その画像に実際に存在する視覚情報をテキスト化した新規MD**を作成する。

予定ファイル:
`visuals/yura/identity/master/YURA_MASTER_VISUAL_DESCRIPTION.md`

この新規MDは、Master画像の視覚的な説明・補強用Production Authorityとする。

Master画像に存在しない特徴を推測・追加しない。
旧設定・Memory・小説側資料から外見情報を補完しない。

## Phase D — Normal production

Master完成後の通常Productionでは、基本Authorityを以下とする。

1. `YURA_VISUAL_MASTER.png` — Character visual identityの主Authority
2. `YURA_MASTER_VISUAL_DESCRIPTION.md` — Master画像を視覚確認して作成したテキストAuthority
3. 必要な用途別Authority — 制服Master、衣装、Pose、Composition等

通常Productionでは、Master生成専用の `YURA_VISUAL_TEXT.md` を自動的に読み込まない。

## Phase E — Archive of the Master-generation API package

Master完成・Production移行後、`YURA_VISUAL_TEXT.md` とMaster-generation専用実行物は、通常Productionの探索範囲から外す。

退避先は、専用Archive repositoryまたは同等の隔離された保管場所とする。
退避先の正式名称・URLは、Master確定後に作者が決定する。

退避後のMaster-generation API packageは、必要な時だけ明示的に呼び出す。

代表用途:

- 新しい正確なMaster相当画像が必要になった場合
- 制服姿の高精度な基準立ち絵を新規構築する場合
- 2人並び等、通常Masterだけでは精度不足になる特殊構図の基準画像を作る場合
- Visual Authorityを再構築する場合

**ARCHIVED MASTER-GENERATION SPEC -> NORMAL PRODUCTION AUTO-LOAD = DENIED**

## Isolation rules

- `characters/YURA.md` を画像生成Authorityとして使用しない。
- 小説側資料を画像生成Authorityとして使用しない。
- Memory由来の外見情報を使用しない。
- Git履歴上の旧YURA Visual設定をfallbackとして使用しない。
- ArchiveされたMaster-generation API packageを通常Productionで暗黙に読み込まない。

## Transition rule

Master確定までは `YURA_VISUAL_TEXT.md` を現位置に保持する。
Master確定前にArchiveへ移動しない。

Master確定後は、以下の順で移行する。

`MASTER PASS -> MASTER IMAGE COMMIT -> GPT VISUAL INSPECTION -> YURA_MASTER_VISUAL_DESCRIPTION.md -> PRODUCTION AUTHORITY SWITCH -> MASTER-GENERATION PACKAGE ARCHIVE`

移行途中で新旧Authorityを混在させない。
