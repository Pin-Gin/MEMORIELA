# Project YURA — Pin-Gin Creation START HERE

Status: **CANONICAL PINGIN CREATION ENTRYPOINT**

Purpose:
ぴんぎん / Pin-Gin に関する画像生成、Visual Identity、Master、BODY、派生生成、QA判断をYURAから分離して扱うための入口。

Pin-Gin作業ではYURAのVisual Identity仕様をPin-Gin Authorityとして使用してはならない。
YURAとPin-Ginが同一画像に登場する場合も、それぞれのAuthorityを独立して読む。

---

## 1. Current Authority Read Order

Pin-Ginのmaterial generation / identity judgmentでは、必要な範囲で以下を読む。

1. `identity/VISUAL_IDENTITY.md`
2. `identity/master/VISUAL_MASTER.md`
3. `identity/BODY_SPEC.md`
4. `generation/VISUAL_TEXT_REFERENCE.md`
5. `generation/IMAGE_GENERATION_GOVERNANCE.md`
6. current derivative request

Current Gitに存在しない旧Revision・旧Spec・過去チャットを通常Authorityとして読まない。

---

## 2. Directory Roles

### `identity/`
Pin-Gin自身の恒常Identity / BODY authority。

### `identity/master/`
承認済みwhole-character visual master manifestおよび将来のMASTER binary配置。

Expected MASTER binary path:
`docs/assistant-context/creation/pingin/identity/master/PINGIN_VISUAL_MASTER.png`

### `generation/`
派生生成時のcompile order、anti-drift、generation governance。

### `reference-materials/`
将来配置するsupporting referenceや非Master資料。

Expected supporting reference path:
`docs/assistant-context/creation/pingin/reference-materials/PINGIN_VISUAL_REFERENCE.png`

Reference material never overrides the current Identity / Master / BODY authority.

---

## 3. Version Rule

Current AuthorityのファイルPathへRevision番号を付けない。

Revisionは文書内部に保持する。

例:
- current file: `identity/BODY_SPEC.md`
- document metadata: `Current Revision: v1.0`

Revisionが更新されてもcurrent pathは固定する。

Superseded revisionはcurrent Gitへ残さない。
履歴確認が必要な場合はGit historyまたはGit外Archiveを使用する。

---

## 4. Domain Separation

Do not:
- load YURA BODY/FACE/HAIR rules as Pin-Gin identity
- make Pin-Gin mascot anatomy inherit YURA human anatomy
- treat Background authority as Pin-Gin identity
- promote a derivative image to MASTER automatically

When YURA + Pin-Gin appear together:
- YURA → `visuals/yura/START_HERE.md`
- Pin-Gin → this file
- Background → `creation/background/START_HERE.md`

---

## 5. Master Status

The approved Pin-Gin MASTER identity is already recorded in the current Master manifest.

Repository binary placement must use:
`identity/master/PINGIN_VISUAL_MASTER.png`

Do not regenerate a substitute MASTER merely because the binary is not yet present.

---

## 6. Change Control

Material changes to:
- Identity
- BODY
- MASTER
- generation governance
- rendering direction
- seasonal accessory system

require explicit Owner approval.

Routine derivative generation does not change Formal Authority.
