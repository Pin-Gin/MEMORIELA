# Project YURA — Background Creation START HERE

Status: **CANONICAL BACKGROUND CREATION ENTRYPOINT / SPECIFICATION PENDING**

Purpose:  
Project YURAの背景・生活空間・建物・間取り・家具配置・空間制作に関するCreation作業を開始する際のBackground入口とする。

本書はBackgroundの詳細仕様を定義しない。

現時点では、Background Domainの正式なMaster・Control・Task運用・QA・Authority構造は未確定とする。

---

## 1. Entry Condition

本書はCreation共通入口からBackground Domainへルーティングされた場合のみ使用する。

`docs/assistant-context/creation/START_HERE.md`

Background作業では、本書を読了する前に正式な背景仕様・Master・QAルールをAIが推測で作成してはならない。

---

## 2. Current State

Background Domainは現在、

**SPECIFICATION PENDING**

とする。

未確定項目には以下を含む。

- Background MasterのAuthority
- 間取り・建物構造のFormal Specification
- 家具配置ルール
- Camera / Framing Rule
- 2D / 3D連携ルール
- Background Generation Rule
- Background QA
- Task管理方式
- Archive / Master更新方式

これらはOwnerとの認識合わせ後に正式化する。

---

## 3. Existing YURA Authority Separation

YURA本人のVisual Identity AuthorityをBackground Specificationとして流用してはならない。

特に以下をBackgroundの正式仕様として扱わない。

- YURA BODY
- YURA FACE
- YURA EYE
- YURA HAIR
- YURA RENDERING identity
- YURA Visual Master

YURAとBackgroundを同一画像内で扱う場合も、それぞれのAuthorityを分離する。

---

## 4. Temporary Work

Backgroundの正式仕様が未整備の間でも、Ownerが明示的に依頼した場合は以下の作業を行うことができる。

- アイデア検討
- 構成案
- 試作
- 単発Background Generation
- Reference候補作成
- 仕様策定のための比較

ただし、これらの結果を自動的にFormal Background Master / Authorityとして扱ってはならない。

---

## 4.1 Reference Materials Before Formalization

Formal Background Authorityが未確定の間、将来の3D再構築・空間検証・イラスト化・正式仕様化の材料として保持する資料は以下へ隔離する。

`docs/assistant-context/creation/background/reference-materials/`

このディレクトリの内容は:

- **NON-AUTHORITATIVE**
- current Background Masterではない
- current Background Specificationではない
- AIが自動的にGeneration Authorityとして使用してはならない
- OwnerがBackground formal化・再構築を明示した場合のみ参考材料として使用できる

特に旧Room資料:

`reference-materials/YURA_ROOM_DAY_LEGACY_REFERENCE.md`

は、過去に承認された部屋コンセプト・レイアウト情報を保持するための材料であり、将来の3D生成 → multi-angle screenshot → illustration化の入力候補としてのみ保持する。

将来正式化する場合は、3D/2D検証後に必要な内容だけを `masters/` / `specs/` / `qa/` へOwner承認付きで昇格する。

---

## 5. Formalization Gate

Backgroundの仕様を正式化する場合は、Ownerとの認識合わせを行い、必要な構造を改めて定義する。

必要に応じて以下を追加する。

- `AI_CONTROL.md`
- `TASKS.md`
- `SPEC_TEMPLATE.md`
- `specs/`
- `masters/`
- `qa/`
- その他必要なAuthority

配置・命名・Authority関係は、仕様確定時にOwnerが承認した内容を採用する。

---

## 6. Reserved Placement

Background Domainの正式仕様が将来確定した場合、原則として以下の配下へ配置する。

`docs/assistant-context/creation/background/`

想定配置:

- `AI_CONTROL.md` — Background Creation共通制御
- `TASKS.md` — Background Task管理
- `SPEC_TEMPLATE.md` — Background Task Specテンプレート
- `specs/` — Active Background Task Spec
- `masters/` — 正式採用されたBackground Master / Manifest
- `qa/` — Background QA仕様・検証基準
- `reference-materials/` — 正式化前のNON-AUTHORITATIVE材料
- 必要に応じて `references/` — 正式化後に正式管理対象としたBackground Reference

この配置は**置き場所の予約のみ**を目的とする。

現時点で、各ファイルやディレクトリの存在・内容・Authorityを確定したものとは扱わない。

既存の背景関連ファイルを将来ここへ移動する場合は、参照元・Script・Workflow・Public document・他Authorityへの影響を確認し、Owner承認後に別作業として実施する。

---

## 7. Fail-Closed Rule

以下の場合、AIがBackground Formal Specificationを勝手に確定してはならない。

- Owner承認がない
- Authority構造が未確定
- Masterの正式採用が未確定
- QA基準が未確定
- 既存YURA Visual RuleをBackgroundへ流用しようとしている

未確定事項は未確定のまま扱い、推測でFormal Authorityを作成しない。
