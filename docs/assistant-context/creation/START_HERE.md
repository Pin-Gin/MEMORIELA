# Project YURA — Creation START HERE

Status: **CANONICAL CREATION ENTRYPOINT**

Purpose:  
Project YURAのCreation作業を開始する際の唯一のCreation共通入口とする。

本書は画像生成仕様、Visual Identity、背景仕様、キャラクター仕様その他の詳細な制作ルールを保持しない。

役割は、Creation作業の対象を判定し、対応するDomain START_HEREへルーティングすることに限定する。

---

## 1. Entry Condition

本書はProject YURA共通入口からCreation作業へルーティングされた場合のみ使用する。

`docs/assistant-context/YURA_START_HERE.md`

本書を読了する前に、生成・編集・採用判定・QAその他のCreation実作業へ進んではならない。

未読状態では **BLOCKED** とする。

---

## 2. Creation Domain Routing

現在のCreation対象を確認し、該当するDomain START_HEREへ進む。

### YURA

久遠ゆら本人の画像生成、編集、衣装、髪型、表情、ポーズ、Visual Identity、Master、Reference、生成QAその他のYURAビジュアル作業。

→ `docs/assistant-context/creation/yura/START_HERE.md`

### Pin-Gin

ぴんぎん / Pin-Gin のVisual Identity、Master、BODY、派生画像、Generation Governanceその他のPin-Gin制作作業。

→ `docs/assistant-context/creation/pingin/START_HERE.md`

### Background

生活空間、室内、建物、間取り、家具配置、背景Master、カメラ位置、空間整合性その他の背景制作作業。

→ `docs/assistant-context/creation/background/START_HERE.md`

---

## 3. Domain Separation

Creation DomainごとのControl・Task・Spec・Master・QAを理由なく混在させてはならない。

YURA固有のVisual IdentityルールをPin-GinまたはBackground作業へ適用しない。

Pin-Gin固有のmascot Identity / BODYルールをYURAまたはBackgroundへ適用しない。

Background固有の空間・構造ルールをYURA Identityの定義として扱わない。

YURAとBackgroundの双方を含む制作物が必要な場合は、それぞれのDomain Authorityを明示し、どの要素をどちらが支配するかを分離して扱う。

---

## 4. Existing Authority Preservation

本ルーティング構造は既存のCreation Authorityを置き換えない。

既存のVisual Master、Generation Governance、Protected Specification、QAその他の現行正本は、各Domain START_HEREから必要な範囲だけ参照する。

既存正本を新しいディレクトリへ移動する場合は、参照元・Script・Workflow・Public document等への影響を確認してから別Taskとして行う。

---

## 5. Routing Lock

選択していないDomainのSTART_HEREおよびControlを理由なく読み込んではならない。

対象DomainのSTART_HEREが存在しない、または必要なAuthorityへ到達できない場合は **BLOCKED** とする。

AIが過去会話やMemoryだけからDomain固有ルールを再構築して作業を開始してはならない。

---

## 6. Completion Boundary

本書はCreation Taskの完了条件を定義しない。

生成・編集・採否・QA・Closureは、選択したDomainのControl、Task Spec、および既存Authorityに従う。

本書だけを根拠としてCreation Taskを完了扱いにしてはならない。
