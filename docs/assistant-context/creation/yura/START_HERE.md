# Project YURA — YURA Creation START HERE

Status: **CANONICAL YURA CREATION ENTRYPOINT**

Purpose:  
久遠ゆら本人の画像生成・編集・Visual Identity・採否判定・生成QAを開始する際の唯一のYURA Creation入口とする。

本書はYURAの詳細なVisual Specificationを再定義しない。

役割は、YURA Creation作業を `DESIGN_SPEC` または `PRODUCTION_DERIVATIVE` に分類し、必要なControl・Task・Request・既存Visual Authorityへ正しい順序でルーティングすることに限定する。

---

## 1. Entry Condition

本書はCreation共通入口からYURA Domainへルーティングされた場合のみ使用する。

`docs/assistant-context/creation/START_HERE.md`

YURA Creation作業では、本書を読了する前に生成・編集・採用判定・正式QAへ進んではならない。

未読状態では **BLOCKED** とする。

---

## 2. Mandatory Initial Read Order

YURA Creation作業は以下の順序で開始する。

1. `docs/assistant-context/creation/yura/START_HERE.md`
2. `docs/assistant-context/creation/yura/AI_CONTROL.md`
3. `docs/assistant-context/creation/yura/AUTHORITY_INDEX.md`
4. Creation Modeを判定する

Mode判定後の読込は `AI_CONTROL.md` に従う。

必要な文書を読了できない場合は **BLOCKED** とする。

---

## 3. Creation Mode Routing

YURA Creation作業は以下のどちらかへ分類する。

### DESIGN_SPEC

今後も再利用する正式仕様・Master・Visual Authority・恒常ルールを新規作成または変更する作業。

→ `TASK_ID` REQUIRED  
→ YURA Creation `TASKS.md`  
→ Active Task Spec  
→ Required Visual Authority

### PRODUCTION_DERIVATIVE

既に確定しているYURA Visual Authorityを使用して、その時点のテーマ・衣装・表情・ポーズ・シチュエーション・用途に応じた画像を生成または編集する作業。

→ `TASK_ID` NOT REQUIRED  
→ Temporary Current Creation Request  
→ Required Visual Authority  
→ Visual Master / Reference Gate  
→ Generation / Editing  
→ Formal QA

正式化の意図が明示されていない場合は、原則 `PRODUCTION_DERIVATIVE` とする。

---

## 4. Existing YURA Authority Preservation

新しいCreation管理構造は、既存のYURA Visual / Generation Authorityを置き換えない。

Creation RequestまたはActive Task Specに応じてGit current branch上の現行正本を使用する。

主要Authority:

- `docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
- `docs/assistant-context/creation/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md`
- `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`
- `docs/assistant-context/creation/yura/qa/GENERATION_QA.md`
- 必要なBODY / FACE / EYE / HAIR / RENDERINGその他のprotected specification

---

## 5. Current Branch Authority

通常のYURA Creation作業では、Git current branchの現行正本のみをproduction Authorityとして使用する。

禁止:

- Git history上の旧Masterを通常生成へ使用する
- rejected imageをIdentity sourceへ昇格する
- intermediate generationをMasterとして扱う
- 過去チャット添付画像を根拠なく正本扱いする
- superseded specificationを現行Authorityとして使用する

過去資料を確認する必要がある場合は、履歴調査であることを明示する。

---

## 6. Authority Separation

Current Creation RequestまたはActive Task Specは「今回何を作るか」を定義する。

既存Visual Authorityは「久遠ゆらを誰として、どの固定仕様で作るか」を定義する。

通常Derivativeによって既存Visual Masterやprotected specificationを暗黙に変更してはならない。

Visual Identityそのものを正式変更する場合は `DESIGN_SPEC` とする。

---

## 7. Reference / Master Gate

生成または編集にVisual Master / Referenceが必要な場合、現行Git Authorityから解決する。

生成途中の画像、未承認候補、失敗画像、任意のチャット添付画像をReference Authorityへ昇格してはならない。

必要なGit由来Visual Masterを確認できない場合は、既存Generation GovernanceおよびAsset Discovery Protocolに従い **BLOCKED** とする。

---

## 8. Control Boundary

YURA Creation作業にはYURA Creation用Controlを適用する。

Background固有の間取り・家具配置・空間構造ルールをYURA Visual Identityへ混入させてはならない。

Background制作が必要になった場合はCreation共通入口からBackground Domainへルーティングする。

アプリケーション開発環境は終了済み。本リポジトリは画像制作を対象とし、開発再開時はOwnerの指示に基づいて別途入口を定義する。

---

## 9. Execution Lock

以下の共通条件が成立するまでYURA Creation実作業へ進んではならない。

- `YURA_START_HERE.md` 読了
- `AI_BEHAVIOR_CONTROL.md` 読了
- Creation共通 `START_HERE.md` 読了
- 本書読了
- YURA Creation `AI_CONTROL.md` 読了
- `AUTHORITY_INDEX.md` 読了
- Creation Mode判定済み
- 必要な既存YURA Authority読了
- 必要なVisual Master / Reference Gate確認

さらに `DESIGN_SPEC` では以下が必要。

- `TASK_ID` 確認
- `docs/assistant-context/creation/yura/TASKS.md` で対象Task確認
- Active Task Spec全文読了

さらに `PRODUCTION_DERIVATIVE` では以下が必要。

- Current Creation Request整理済み

必要条件が未完了の場合は **BLOCKED** とする。

---

## 10. Completion Boundary

生成または編集が完了しただけでは正式採用・Authority昇格を意味しない。

正式QA・採否・Protected Element確認・Definition of DoneはYURA Creation `AI_CONTROL.md`、Current Creation RequestまたはActive Task Spec、および指定された既存QA Authorityに従う。

通常Derivativeの完了を理由としてFormal Spec / Masterへ自動昇格してはならない。
