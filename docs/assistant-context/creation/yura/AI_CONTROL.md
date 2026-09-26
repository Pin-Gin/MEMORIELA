# Project YURA — YURA Creation AI Control

Status: **CANONICAL YURA CREATION CONTROL**

Purpose:  
久遠ゆら / YURAの画像生成・編集・Visual Identity・採否判定・QAにおいて、AIが現行Visual Authorityを無視した生成、Reference汚染、Protected Domainの無断変更、未検証採用を行えないよう制御する。

本書はYURAのVisual Specificationそのものを定義しない。

BODY / FACE / EYE / HAIR / RENDERING / MASTER / Generation QA等の詳細仕様は、Git current branch上の既存Visual Authorityを正本とする。

基本原則:

**YURAをAIの記憶から再構築しない。  
現在のGit正本からYURAを復元し、今回許可された差分だけを扱う。**

---

## 1. Creation Mode Classification

YURA Creation作業は、実作業開始前に必ず以下のどちらかへ分類する。

- `DESIGN_SPEC`
- `PRODUCTION_DERIVATIVE`

分類基準は、

**今回の作業結果を、今後も再利用する正式なYURA Authorityとして確定するか**

とする。

画像の内容そのものではなく、その結果を正式仕様・Master・恒常ルールへ昇格させる意図があるかで判定する。

正式化の意図が明示されていない場合は、原則 `PRODUCTION_DERIVATIVE` とする。

---

## 2. DESIGN_SPEC Mode

`DESIGN_SPEC` は、YURAの再利用可能な正式仕様・Master・Visual Authorityを新規作成または変更する作業とする。

例:

- 新しい髪型を正式差分として定義する
- 髪型の構造・長さ・まとめ位置等を正式変更する
- 新しいポーズ基準を恒常ルールとして定義する
- Visual Masterを変更する
- BODY / FACE / EYE / HAIR / RENDERINGを変更する
- 新しいHairstyle Masterを作る
- SNS生成時の恒常的な許容ルールを変更する
- Generation / QA Ruleそのものを変更する
- Ownerが明示的に「仕様化」「正式化」「Master化」等を要求する

### TASK_ID

`DESIGN_SPEC` では **TASK_ID REQUIRED**。

Task管理・Active Task Spec・Ownerレビュー・Verification / QA・Closureを使用する。

TASK_IDがない場合:

**BLOCKED — DESIGN TASK ID REQUIRED**

---

## 3. PRODUCTION_DERIVATIVE Mode

`PRODUCTION_DERIVATIVE` は、既に確定しているYURA Visual Authorityを使用し、その時点のテーマ・衣装・表情・ポーズ・シチュエーション・用途に応じた画像を生成または編集する作業とする。

例:

- 秋をテーマにSNS用画像を生成する
- 既存Normal Super-Longでドレス姿を生成する
- 白背景で微笑んだ立ち絵を生成する
- 既存の正式髪型で外出シーンを生成する
- 座る・本を読む等の単発ポーズを生成する
- 表情差分
- 衣装差分
- SNS用画像
- シチュエーション画像

### TASK_ID

通常の `PRODUCTION_DERIVATIVE` では **TASK_ID NOT REQUIRED**。

TASK_IDがないことだけを理由にProduction GenerationをBLOCKしてはならない。

ただしVisual Authority / Master / Reference / QA Gateは省略してはならない。

---

## 4. Temporary Current Creation Request

`PRODUCTION_DERIVATIVE` では、Task Specの代わりに、その生成・編集作業中だけ有効な `Current Creation Request` を整理する。

Current Creation RequestはGitへ保存しない。

最低限以下を整理する。

- `MODE`
- `PURPOSE`
- `THEME`
- `IDENTITY`
- `HAIR`
- `OUTFIT`
- `POSE`
- `EXPRESSION`
- `BACKGROUND / SCENE`
- `PROTECTED`
- `OUTPUT`
- `REQUIRED AUTHORITY`
- `QA`

Current Creation RequestはGeneration Scopeを固定するための一時情報であり、Formal Authorityではない。

生成・編集作業終了後は破棄する。

---

## 5. Authority Order

YURA Creationで判断が競合する場合は、以下をAuthorityとする。

1. Ownerの最新の明示的な確定判断
2. Project-wide `AI_BEHAVIOR_CONTROL.md`
3. Current Git上のProtected Visual Master / Formal Visual Specification
4. `docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
5. DESIGN_SPECの場合はActive Task Spec
6. Task / Requestに適用されるDomain Owner / Protected Sub-Spec
7. `docs/assistant-context/creation/yura/qa/GENERATION_QA.md`
8. Current derivative request
9. 過去の生成物・候補・履歴
10. AI自身の提案・記憶

下位Authorityで上位Authorityを上書きしてはならない。

過去の生成画像が現在のMasterより魅力的に見えることを理由として、Identity Authorityを変更してはならない。

---

## 6. Scope / Protected Lock

YURA Creation実作業では、今回許可された変数だけを変更する。

変更対象ではないProtected Domainは固定する。

禁止:

- Scope外のVisual Identity変更
- FACEの無断変更
- BODY geometryの無断変更
- EYE signatureの無断変更
- HAIR coreの無断変更
- RENDERING grammarの無断変更
- Masterの無断置換
- 未要求の恒常仕様追加
- 生成結果に合わせたFormal Specificationの書き換え

生成結果がCanonと合わない場合、Canonを生成結果へ合わせてはならない。

---

## 7. Required Authority Gate

今回のCreation RequestまたはActive Task Specに必要な既存Visual Authorityを明示する。

必要に応じて以下の現行正本へルーティングする。

- `docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
- `docs/assistant-context/creation/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md`
- `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`
- BODY Authority
- FACE Authority
- EYE Authority
- HAIR Authority
- Hairstyle-specific Authority
- RENDERING Authority
- Outfit / Pose / Framing等のTask-specific Authority
- `docs/assistant-context/creation/yura/qa/GENERATION_QA.md`

AIは必要なAuthorityをMemoryから再現して代用してはならない。

必要なAuthorityが未読または解決不能の場合:

**BLOCKED — REQUIRED YURA AUTHORITY NOT VERIFIED**

---

## 8. Visual Master / Reference Gate

Production Generation / Editingでは、現行Git current branchのVisual Masterを使用する。

Visual Masterの取得・復元・検証方法は、

`docs/assistant-context/creation/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md`

および

`docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`

に従う。

Git上のPath・SHA・Manifestを確認しただけでVisual Masterを視認した扱いにしてはならない。

既存Governanceが要求するVisual recovery / Reference Input Gateを満たせない場合、そのGovernanceが定義するBLOCKED状態をそのまま適用する。

---

## 9. Reference Isolation

画像Referenceはすべて役割を限定する。

YURA Identity Referenceとして使用できるものは、既存Generation GovernanceのAllowlistに従う。

以下を理由なくIdentity Referenceとして使用してはならない。

- 直前の生成結果
- 採用候補
- rejected image
- failed generation
- 過去のDerivative
- SNS用生成画像
- Validation output
- 任意のチャット添付画像
- Pose / mannequin reference
- Background reference
- Historical / superseded Git artifact

PoseはPoseのみ、BackgroundはBackgroundのみ等、Non-Identity Referenceの役割境界を維持する。

Generated candidateを次のRetryのIdentity Sourceへ昇格してはならない。

---

## 10. Exact Preservation Routing

Ownerが以下に相当する要求をした場合:

- 変更しない
- 差分なし
- 完全維持
- 固定
- 完全一致
- 指定部分だけ変更

通常Generationとして処理してはならない。

既存の

`docs/assistant-context/creation/yura/generation/preservation/PIXEL_PRESERVATION_PROTOCOL.md`

および必要に応じて

`docs/assistant-context/creation/yura/generation/preservation/BODY_GEOMETRY_PRESERVATION_PROTOCOL.md`

へルーティングする。

使用する実行手段が要求されたPreservationを保証できない場合、推測で実行してはならない。

---

## 11. DESIGN_SPEC Read / QA Gate

`DESIGN_SPEC` ではActive Task Specを繰り返し確認する。

### READ-1 — Before Production / Validation

最初の検証Generation / Edit前に全文読む。

### READ-2 — Before Formal QA

候補生成・編集後、正式QAへ入る直前に全文再読する。

### READ-3 — Before Closure / Adoption

最終QA後、TaskをCLOSEDにする、Masterへ昇格する、正式採用する等の確定処理前に全文再読する。

必須READを省略してはならない。

---

## 12. PRODUCTION_DERIVATIVE Execution Flow

通常Derivativeでは以下の順序で進む。

1. `PRODUCTION_DERIVATIVE` と分類
2. Current Creation Requestを整理
3. Required Visual Authorityを確認
4. Visual Master / Reference Gateを通過
5. Taskで許可されたDerivative変数のみCompile
6. Generation / Editing
7. `docs/assistant-context/creation/yura/qa/GENERATION_QA.md` に基づくQA
8. Ownerの用途に応じて投稿候補 / Stock / Hold / Reject等を判定
9. Current Creation Requestを破棄

通常Derivativeを理由なくDESIGN_SPECへ昇格させてはならない。

---

## 13. Generation / Retry Discipline

Production Generation / Editingでは以下を守る。

- 今回指定された変更対象だけを変更する
- Protected Domainを維持する
- Visual MasterをIdentity Anchorとして維持する
- Non-Identity Referenceの役割を限定する
- Scope外の装飾を追加しない
- 不要な変数を同時に変更しない
- Retry時もCanon Lockを維持する
- QA前に印象だけで採用しない

QA Failure後はFailure Domainを特定する。

既存 `docs/assistant-context/creation/yura/qa/GENERATION_QA.md` の判定に従い、LOCAL REPAIR / TARGETED RETRY / REJECT等の最小対応を行う。

Retryごとに既存Governanceで要求されるPer-call Gateを再実行する。

---

## 14. Formal QA Gate

Material outputは `docs/assistant-context/creation/yura/qa/GENERATION_QA.md` に従ってFormal QAを行う。

QAは既存Domain Authorityに対して判定する。

QAが新しいCanonを発明してはならない。

観測できないProtected Detailを自動PASSとして扱ってはならない。

魅力的な画像であることを理由としてProtected Failureを許容してはならない。

---

## 15. Canon Promotion Lock

Derivative Generationの結果は、以下を理由としてFormal Authorityへ昇格してはならない。

- 出来が良い
- Ownerが画像を気に入った
- SNS投稿に採用された
- Stockへ保存された
- 何度も使用された
- AIが再利用した方が良いと判断した

Formal Authorityへの昇格にはOwnerの明示的な意思が必要。

例:

- 「これを正式差分にする」
- 「今後この髪型を使う」
- 「Masterにする」
- 「仕様化する」
- 「このポーズを正式基準にする」

この意思が確認された時点で、

`PRODUCTION_DERIVATIVE`
→ `DESIGN_SPEC`

へ切り替える。

既存生成物は候補Evidenceとして使用できるが、それだけでAuthorityにはならない。

---

## 16. Ambiguous Request Rule

正式化の意図が明示されていない場合、原則 `PRODUCTION_DERIVATIVE` として扱う。

AIが通常のGeneration Requestを勝手にFormal Spec変更として解釈してはならない。

Example:

「新しい髪型で生成して」
→ その画像だけのDerivative

「この新しい髪型を今後使う正式差分として決めたい」
→ DESIGN_SPEC

---

## 17. Classification Examples — Non-Exhaustive

以下は分類理解のための**非網羅的な例**であり、一覧に存在しない依頼も1章の分類原則で判定する。

| Owner Request | Mode | TASK_ID |
|---|---|---|
| 秋テーマでSNS画像を4枚 | PRODUCTION_DERIVATIVE | 不要 |
| 既存ハーフアップでドレス姿 | PRODUCTION_DERIVATIVE | 不要 |
| ジト目の立ち絵 | PRODUCTION_DERIVATIVE | 不要 |
| 新しい髪型を1枚試したい | PRODUCTION_DERIVATIVE | 不要 |
| その髪型を正式差分にしたい | DESIGN_SPEC | 必須 |
| 新しいローシニヨン仕様を決める | DESIGN_SPEC | 必須 |
| ポーズ許容範囲を今後のルールとして定義 | DESIGN_SPEC | 必須 |
| Visual Masterを差し替える | DESIGN_SPEC | 必須 |
| SNS画像をStock採用 | PRODUCTION_DERIVATIVE | 不要 |
| Stock画像を正式Masterに昇格 | DESIGN_SPEC | 必須 |

---

## 18. Classification Fail-Closed

以下の場合のみMode分類を理由としてCreation実作業を開始してはならない。

- Modeを判定できない
- DESIGN_SPECなのにTASK_IDがない
- PRODUCTION_DERIVATIVEなのにCurrent Creation Requestが整理されていない
- Required Visual Authorityを確認できない
- Visual Master / Reference Gateを満たせない
- Current RequestとFormal Authorityが衝突している

通常Derivativeについて、TASK_IDがないことだけを理由にBLOCKしてはならない。

---

## 19. Existing Governance Supremacy

本書は既存Visual Authorityを簡略化・置換するための文書ではない。

以下の詳細ルールは、それぞれ既存正本をAuthorityとする。

- Visual recovery
- Reference-input preflight
- Protected pixel preservation
- BODY geometry preservation
- Domain ownership
- Generation compile order
- Framing / size profile
- Generation QA
- Master change control

本書と既存Visual Authorityの間に重大な競合が見つかった場合、AIが独自解釈で解消してはならない。

競合箇所を明示し、Owner確認まで該当作業を **BLOCKED** とする。

---

## 20. Rule Growth Control

個別の失敗画像や一時的な生成事故ごとにGlobal YURA Creation Ruleを追加してはならない。

新しい問題はまず以下で処理できるか確認する。

- Current Creation Request
- Active Task Spec
- Existing Visual Authority
- Existing Generation Governance
- Existing Generation QA
- Existing Preservation Protocol

YURA Creation全体に恒常的に必要な制御である場合のみ、本書へ追加する。

目標は、

**既存の強いVisual Authorityを維持し、そのAuthorityを必ず通過させる少数のControlを保つこと。**
