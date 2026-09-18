# MEMORIELA Homepage Decision Log

Purpose: ユーザーと明示的にFIXしたホームページ仕様だけを、後からAIの推測で上書きされない形で保存する。

## 運用ルール

- この文書は **append-only**。既存の決定を削除・書き換えない。
- 仕様変更があった場合は、新しいDecisionを追加し、`Supersedes` で旧Decisionを明示する。
- 優先順位は **最新の明示的なユーザー指示 > このDecision LogのACTIVE決定 > MASTER文書 > 現在の実装コード > AIの推測**。
- MASTER画像は視覚レイアウト参照。Decision Logにある機能・導線・配置の決定を上書きしない。
- 現在のコードは実装結果であり、仕様の根拠ではない。
- Git履歴は、Decision LogやMASTERが誤って変更された場合の復元・検証に使う。
- スクリーンショットは現状確認用。ユーザーが明示しない限り、それだけで仕様変更とはみなさない。

## ACTIVE Decisions

### D-001 — Hero LATEST TOPICS
- Status: ACTIVE
- Area: Homepage Hero
- Decision: DesktopではHero右側に **LATEST TOPICSの小窓** を配置する。
- Mobile: 横並びで押し込まず、Hero下部または画像下に自然に再配置する。
- TOPICSは外向けのお知らせ。Development Historyとは別役割。
- Source history: 2026-09-19 MASTER初版。Git commit `1b1014d24f8e9d8905dd86536baca7128f34eb96` で記録済み。
- Supersedes: none

### D-002 — Homepageから独立ページへ移す項目
- Status: ACTIVE
- Area: Homepage / Header navigation
- Decision: About / Project.YURA、Technology、Gallery、Development Historyはトップページ本文に展開せず、ヘッダーから独立ページへ遷移して表現する。
- Routes: `/about`, `/technology`, `/gallery`, `/history`
- Supersedes: 旧トップページ内6ブロック構成の該当部分

### D-003 — Hero右上コピー削除
- Status: ACTIVE
- Area: Homepage Hero
- Decision: 「つくろう、ずっとそばに。 / Creating a future with you.」はHeroから削除する。
- Supersedes: MASTER画像上の当該コピー表示

### D-004 — Homepage作業中の画像生成禁止
- Status: ACTIVE
- Area: MEMORIELA website workflow
- Decision: ホームページ作業中は新規画像生成を行わない。画像生成禁止を解除した明示的な別依頼がない限り `image_gen` を使わない。
- Supersedes: none
