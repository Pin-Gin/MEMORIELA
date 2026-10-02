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
Router-only化は「Authorityを解決できれば何でも生成してよい」という意味ではない。

Authority resolution後は、`../gate-core/EXECUTION_PAYLOAD_PROTOCOL.md` に従い、active Execution Payloadの実際の生成意味を画像生成へ渡す。

重要:
- `TEXT_ONLY` は **画像参照を使わないSource Mode**
- `TEXT_ONLY` を direct-prompt API の有無で禁止してはならない
- 会話コンテキストから画像指示を構成する生成インターフェースでは `CONTEXT_DERIVED_TEXT_EXECUTION` を使用できる
- その場合もGitパスだけ、"Git準拠"、"前回と同じ" だけで生成してはならない
- active Execution Payloadの実際の生成意味を生成直前のcontextへ搬送する

今回のような `MASTER_CREATION / TEXT_ONLY_ROOT_MASTER` が明示されている場合、PRODUCTION Gateへ誤ルーティングしない。

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
