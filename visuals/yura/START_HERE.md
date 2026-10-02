# 久遠ゆら Visual START HERE

Status: **CANONICAL YURA VISUAL ENTRYPOINT / ROUTER ONLY**

Purpose: MEMORIELAで久遠ゆらを生成する際の唯一の入口。

## Mandatory route
画像生成を行う場合、この文書から直接生成してはならない。

必ず次へ進む:
1. `../gate-core/GATE_PROTOCOL.md`
2. `gate/GENERATION_GATE.md`

`identity/` / `generation/` / `qa/` を直接探索し、AIが独自に生成コンテキストを組み立てることは禁止する。

読むAuthorityは `gate/AUTHORITY_MANIFEST.md` が列挙した完全パスだけで決定する。

## Execution handoff boundary
Router-only化は「Authorityを解決できれば生成できる」という意味ではない。

Authority resolution後は、`../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md` に従い、active Execution Payloadを**検証可能なモデル向け入力経路**へ渡せることを確認する。

`PROTECTED FIXED EXECUTION BLOCK` では:
- Gitを読んだだけではPASSにならない
- connector / tool outputだけではPASSにならない
- 会話へ固定ブロックを展開しただけでもPASSにならない
- 会話コンテキストから画像指示を自動再構成する生成インターフェースは `CONTEXT_DERIVED_UNVERIFIED`
- model-facing prompt / instruction を直接固定・検証できない場合は Fail-Closed

`AUTHORITY_RESOLVED = YES` と `FIXED_PAYLOAD_TRANSPORT_GUARANTEE = PASS` は別条件。

後者を証明できない場合:
`GENERATION_ALLOWED = NO`

## Fail-closed
以下は生成許可にならない:
- 過去に読んだ
- メモリにある
- 前回と同じ
- 似たファイルがある
- ディレクトリ配下を読めば十分
- MasterがGitに存在するだけで実際の視覚参照へ渡っていない

Gate PASSとLoad Receipt完成前に画像生成を実行しない。

## Novel boundary
年齢、人物関係、時系列、制服、場面設定など物語Canonは `characters/` / `story/` を正とする。
このDomainはYURAのVisual Identityと生成安定性を扱う。
