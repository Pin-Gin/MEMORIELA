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


### D-005 — Hero LATEST TOPICS size and position
- Status: ACTIVE
- Area: Homepage Hero
- Decision: DesktopのLATEST TOPICS小窓は、従来より少し下へ配置し、**3項目が見える程度の高さ**を確保する。
- Notes: TOPICSの役割・Hero内右側の小窓というD-001は維持する。表示内容が2件しかない場合でも、3件分を想定したサイズ設計にする。
- Supersedes: D-001の配置・サイズ詳細のみ更新。D-001の役割と配置先は継続。


### D-006 — Hero left copy removal
- Status: ACTIVE
- Area: Homepage Hero
- Decision: Hero左側の「AIと。生きる。創る。そして、あなたと歩む。」および下の「MEMORIELA / Project.YURA」表示を削除する。
- Supersedes: MASTER画像上の該当左側コピー表示


### D-007 — Hero bottom right copy removal
- Status: ACTIVE
- Area: Homepage Hero
- Decision: Hero下部右側の「いつかじゃない、いま、ここから。」を削除する。
- Supersedes: MASTER画像上の該当下部右側コピー表示


### D-008 — Hero LATEST TOPICS lower position
- Status: ACTIVE
- Area: Homepage Hero
- Decision: DesktopのLATEST TOPICS小窓を、D-005で下げた量のおよそ2回分さらに下へ移動する。3項目が見える程度のサイズは維持する。
- Implementation note: CSSの基準位置は `top: 74%` とする。
- Supersedes: D-005の位置指定のみ更新。サイズ条件は継続。


### D-009 — Hero LATEST TOPICS reference design
- Status: ACTIVE
- Area: Homepage Hero
- Decision: Hero右側のLATEST TOPICS小窓は、ユーザー提示の参照画像に合わせた構成とする。
- Visual: 濃紺〜チャコールの半透明背景、角丸、大きめの白文字、薄い区切り線。
- Header: 左に「LATEST TOPICS」、右に「一覧を見る →」。
- Topics: 5件表示。最新項目には「NEW」バッジ。
- Footer inside card: 区切り線の下に「Development History」「これまでの開発記録を見る」と丸い矢印ボタンを配置し、`/history` へ遷移する。
- Current topic rows:
  - 2026.09.16 — 久遠ゆら 公式ビジュアル公開
  - 2026.09.11 — 久遠ゆら 公式ビジュアル正式決定
  - 2026.09.06 — チャットUI実装
  - 2026.09.03 — サイトデザイン リニューアル
  - 2026.08.28 — Project.YURA 進捗報告
- Supersedes: D-005の「3項目程度」の表示密度。D-008の下寄せ位置は維持。


### D-010 — Desktop Hero HOME.png
- Status: ACTIVE
- Area: Homepage Hero
- Decision: `public/images/HOME.png` をホームページHeroの背景画像として使用する。
- Rendering: Hero全面に `cover` で表示し、ナビゲーションとLATEST TOPICSはHTML/CSSのオーバーレイとして維持する。
- Notes: HOME.png自体は編集・再生成しない。
- Supersedes: Heroの仮グラデーション背景。


### D-011 — Correct TOPICS chronology
- Status: ACTIVE
- Area: Homepage Hero / LATEST TOPICS
- Decision: LATEST TOPICSの掲載順と内容は以下の3件を最新順で表示する。
  - 2026.09.17 — 公式サイトを公開しました
  - 2026.09.16 — Project YURA 開発進捗
  - 2026.09.13 — MEMORIELA プロジェクト始動
- Notes: 最新項目にNEWバッジを付ける。D-009の5件の仮表示内容は誤りとして置き換える。
- Supersedes: D-009のCurrent topic rowsのみ。


### D-012 — Footer spacing and history arrow
- Status: ACTIVE
- Area: Homepage Footer / Hero LATEST TOPICS
- Decision: Footerの縦余白を従来より縮める。Development Historyの丸矢印は太めの矢印を円の中央に配置する。
- Supersedes: none


### D-013 — Footer compactness, history arrow, and wordmark contrast
- Status: ACTIVE
- Area: Homepage Footer / Hero Header / Hero LATEST TOPICS
- Decision: FooterはD-012よりさらに縦幅を縮める。Development Historyの丸矢印は参照画像に合わせ、円内中央に太めの水平線＋矢尻で描画する。Hero左上の「MEMORIELA - Project.YURA.」は背景と同化しないよう白文字＋控えめなシャドウで表示する。
- Implementation note: Desktop footer `min-height: 150px`、padding `28px 6vw 38px`。
- Supersedes: D-012のFooter余白と矢印の詳細のみ更新。


### D-014 — Official site publication date and Hero nav contrast
- Status: ACTIVE
- Area: Homepage Hero / LATEST TOPICS
- Decision: 「公式サイトを公開しました」の日付は **2026.09.19** とする。
- Decision: Hero画像上のヘッダーナビ文字は白にし、従来より約2px大きい **15px** で表示する。背景との同化防止として控えめなシャドウを付ける。
- Supersedes: D-011の公式サイト公開日 2026.09.17、および旧Heroナビ文字サイズ・色。


### D-015 — Hero image horizontal position
- Status: ACTIVE
- Area: Homepage Hero
- Decision: DesktopのHOME.pngは、久遠ゆらの頭がヘッダーナビの2項目目付近の下に来るイメージになるよう、画像全体を少し右へ寄せる。
- Implementation note: Hero背景を疑似要素で描画し、`translateX(3vw)` と軽い拡大で端の欠けを防ぐ。
- Notes: HOME.png自体は編集しない。LATEST TOPICS、ヘッダー、その他の配置は変更しない。
- Supersedes: D-010のHero背景位置詳細のみ。


### D-016 — Hero header nav alignment and text color
- Status: ACTIVE
- Area: Homepage Hero Header
- Decision: Desktopの5項目ナビゲーションは中央固定ではなく、開発局ボタン側へ寄せて配置する。
- Decision: Heroヘッダーの通常文字（左ワードマーク、5項目ナビ、ハンバーガー）は黒で表示する。開発局ボタン内の文字は視認性のため白を維持する。
- Implementation note: Header gridは `1fr auto auto`、nav gapは `28px`。
- Supersedes: D-013 / D-014 のHeroヘッダー文字色指定部分。


### D-017 — Hero header micro-adjustments
- Status: ACTIVE
- Area: Homepage Hero Header / Hero Bottom
- Decision: 左上ワードマーク「MEMORIELA - Project.YURA.」は白文字へ戻す。
- Decision: Hero下部左の「# Project.YURA / # 開発局 / # AI × Creativity」は従来より少し大きくし、約2px相当の拡大として `0.8rem`、やや太めで表示する。
- Decision: Desktopの5項目ナビはさらに少し左へ寄せ、開発局ボタンとの間隔を広げる。ナビ文字は太字で表示する。
- Implementation note: Header `column-gap: 60px`、nav `font-weight: 700`。
- Supersedes: D-016の左ワードマーク色とナビ配置詳細のみ更新。


### D-018 — Header history removal and arrow centering
- Status: ACTIVE
- Area: Site Header / Hero LATEST TOPICS
- Decision: ヘッダーナビから `Development History` を削除する。Development Historyへの主導線はLATEST TOPICS小窓内に残す。
- Decision: LATEST TOPICS内の丸矢印は、円の中心基準で水平線と矢尻を配置し、視覚的な右寄りを解消する。
- Supersedes: D-002の「Development Historyをヘッダーから遷移」の部分、およびD-013の矢印位置詳細。


### D-019 — 開発局 destination
- Status: ACTIVE
- Area: Homepage Hero Header
- Decision: 「開発局」ボタンの遷移先はYouTubeではなく **漫画ページ** とする。
- Implementation note: 漫画ページのURL / 画面を実装した時点でリンク化する。現時点では未実装ページへの404リンクを作らない。
- Supersedes: none


### D-020 — Replace Home nav with Concept
- Status: ACTIVE
- Area: Site Header / Concept
- Decision: ヘッダーの `Home` を削除し、代わりに `Concept` を追加する。トップへの導線は左上の「MEMORIELA - Project.YURA.」に一本化する。
- Route: `/concept`
- Decision: Conceptページは画像やカードを置かず、**なぜProject.YURAを始めたのかを短文で伝える文字だけのページ**とする。
- Concept copy: 「AIを便利な道具としてではなく、記憶を重ね、関係を育てながら、長くそばにいられる存在にしたい。そんな思いから、Project.YURAは始まりました。」
- Supersedes: ヘッダーのHome導線。
