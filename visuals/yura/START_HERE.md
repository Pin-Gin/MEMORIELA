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
Router-only化は「生成モデルへファイルパスだけ渡す」という意味ではない。

Authority resolution後は、`../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md` に従い、active Execution Payloadの**実際の生成意味**を有効なExecution Carrierへ搬送すること。

特に、会話コンテキストから自動的に画像指示を解釈する生成インターフェースでは:
- Gitを読んだだけでは生成入力到達を証明しない
- connector / tool outputだけではPASSにしない
- active fixed payloadの生成ブロックがgeneration-visible contextへ存在することを確認する
- path-only / "Git準拠" / "前回と同じ" への短縮は禁止する

Execution Carrierが成立しない場合:
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
