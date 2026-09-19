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


### D-021 — Technology core tagline
- Status: ACTIVE
- Area: Technology / About
- Decision: Technologyページの主見出しは **「AIと、心が通う物語を。」** とする。
- Decision: 同文言の重複を避けるため、Aboutページのプロフィール内にあった「AIと、心が通う物語。」は削除する。
- Notes: 「を」まで含める表記を正式採用する。
- Supersedes: Technologyページの旧見出し「記憶が、人格を形作る。」およびAbout内の旧コピー。


### D-022 — Absorb Concept into Technology
- Status: ACTIVE
- Area: Site Header / Technology / About
- Decision: standaloneの `Concept` ページとヘッダー項目は廃止し、Conceptの役割をTechnologyへ吸収する。
- Decision: 「なぜProject.YURAを始めたのか」という短文はTechnologyページ内で、主見出し「AIと、心が通う物語を。」とMemory / Personality / Relationshipの間をつなぐ説明として使用する。
- Decision: ヘッダーは `About / Technology / Gallery` とし、トップへの導線は左上の「MEMORIELA - Project.YURA.」に残す。
- Notes: Aboutで世界観を見せる案は方向性候補。具体的な世界観コピー・構成は未FIXのため、このDecisionでは実装しない。
- Supersedes: D-020のstandalone ConceptページとヘッダーConcept項目。


### D-023 — Final primary navigation roles
- Status: ACTIVE
- Area: Site Header / Primary navigation / Brand wordmark
- Decision: サイトの主要導線は以下とする。
  - `MEMORIELA - Project.YURA` → Home
  - `About` → 久遠ゆら + 世界観
  - `Technology` → 思想 + 技術
  - `Gallery` → ビジュアル
  - `World` → 漫画・物語・日常
  - `Contact` → お問い合わせ
- Decision: 旧「開発局」ボタンは `Contact` に置き換える。漫画への導線は `World` に集約する。
- Decision: ブランド表記は **MEMORIELA - Project.YURA** とし、末尾のピリオドは付けない。
- Routes: `/about`, `/technology`, `/gallery`, `/world`, `/contact`
- Notes: Contactの具体的なメールアドレス / フォーム仕様は未FIX。現時点では問い合わせページのみ用意する。
- Supersedes: D-019の「開発局 → 漫画」導線、およびD-022のヘッダー3項目構成。


### D-024 — Mobile homepage direction
- Status: ACTIVE
- Area: Homepage / Mobile
- Decision: スマホ版ホームページは、2026-09-19にユーザー提示の縦長MEMORIELA参考画像を**レイアウト・情報設計の基準**として採用する。
- Decision: Desktop版の白寄りの開発局Heroとは明確に差別化し、Mobile版は**黒を基調としたヴィクトリア朝テイスト**を前面に出す。
- Decision: Mobile Heroのメインビジュアルは、参考画像にある白系ドレスのまま使用せず、黒を主役にしたヴィクトリア朝衣装の久遠ゆらへ差し替える。
- Decision: 参考画像そのものや、参考画像内のロゴ・文言・装飾をそのままWebへ貼り付けるのではなく、現在の正式ナビゲーション・ブランド表記・公式素材で再構成する。
- Notes: 黒系ヴィクトリア朝の正式Mobile Hero素材は未提供のため、現時点では仕様FIXのみ。画像生成は行わない。
- Supersedes: Mobile Heroの旧「白系ドレス姿を使用する」方向性。


### D-025 — Mobile wordmark contrast
- Status: ACTIVE
- Area: Homepage / Mobile Header
- Decision: Mobile版では、黒を基調とした背景と金系装飾に対してブランドロゴ / ワードマークの文字色を**白**にする。
- Decision: 白文字でロゴを強調し、黒＋金のヴィクトリア朝デザインの中で視認性とブランド存在感を確保する。
- Notes: ロゴ画像自体の加工・再生成は行わず、正式素材またはCSSで白表現できる範囲で実装する。
- Supersedes: Mobile参考画像上の黒文字ロゴ表現。


### D-026 — News entry and World band
- Status: ACTIVE
- Area: Primary navigation / Mobile homepage
- Decision: スマホ版にはDesktopのLATEST TOPICS小窓を置かないため、主要ナビゲーションの `World` 項目を `News` に置き換え、最新情報への入口とする。
- Decision: `News` は `/news` へ遷移し、DesktopのLATEST TOPICS内「一覧を見る →」も同じ `/news` へ接続する。
- Decision: `World` は主要ナビゲーション項目から外し、Mobileホーム下部の大きな帯から入る導線とする。
- Decision: Worldの役割は引き続き「漫画・物語・日常」。
- Notes: Mobile World帯の具体的なレイアウトと素材は未実装。黒系ヴィクトリア朝Mobile Hero素材が揃った段階で実装する。
- Supersedes: D-023の主要ナビゲーション `World` 項目。


### D-027 — Brand wordmark role
- Status: ACTIVE
- Area: Brand / Header / Home navigation
- Decision: `MEMORIELA - Project.YURA` はPC・Mobile共通で **Homeへ戻るブランド導線** とする。
- Decision: `MEMORIELA` はブランド名、`Project.YURA` はその配下の現行プロジェクト名として扱う。
- Decision: 将来2人目など別プロジェクトを展開する場合、`Project.YURA` 部分は別のプロジェクト名へ置き換わり得るが、ブランド名 `MEMORIELA` は維持する。
- Notes: 端末ごとにクリック先や役割を変えず、ブランド導線の意味は一貫させる。
- Supersedes: none


### D-028 — Official YouTube link
- Status: ACTIVE
- Area: Homepage Footer / Official links
- Decision: Footerの `YouTube` を、MEMORIELA公式YouTubeチャンネルへの外部リンクとして有効化する。
- Channel: `MEMORIELA開発局`
- URL: `https://youtube.com/@MEMORIELA`
- Notes: 新しいタブで開く。
- Supersedes: Footerの未リンク `YouTube` 表示。


### D-029 — News is mobile-only primary navigation
- Status: ACTIVE
- Area: Desktop Header / Mobile primary navigation / News
- Decision: `News` は **Mobile版の主要ナビゲーション専用** とし、Desktopのヘッダーナビには表示しない。
- Decision: Mobile版の4分割主要ナビでは、旧 `World` があった4番目の位置に `News` を置く。
- Decision: `World` はMobile版の4分割ナビには置かず、その下の大きなWorld帯から `/world` へ遷移する。
- Decision: Desktopでは最新情報への入口はHero内 `LATEST TOPICS` と、その「一覧を見る →」から `/news` へ遷移する導線を使用する。
- Supersedes: D-026のうち、Newsを端末共通の主要ナビゲーションとして解釈し得る部分。


### D-030 — Exact desktop/mobile navigation split
- Status: ACTIVE
- Area: Desktop Header / Mobile homepage navigation
- Decision: Desktop版の主要ナビゲーションは **About / Technology / Gallery / Contact / World** の5項目とする。
- Decision: Mobile版ホームの4分割帯は **About / Technology / Gallery / News** とする。Newsは旧Worldの位置に置く。
- Decision: Mobile版のWorldは4分割帯に置かず、別の大きなWorld帯から `/world` へ遷移する。
- Decision: DesktopではNewsを主要ナビゲーションに表示せず、HeroのLATEST TOPICSおよび「一覧を見る →」から `/news` へ入る。
- Implementation: PC / Mobileの切り替えは接続元情報やサーバー側UA判定ではなく、画面幅に応じたCSS media queryで行う。HomeのMobile 4分割帯はスマホ幅でのみ表示する。
- Supersedes: D-029、およびD-023/D-026の主要ナビゲーション配置詳細。


### D-031 — Mobile homepage reference skeleton
- Status: ACTIVE
- Area: Mobile homepage
- Decision: 2026-09-19にユーザーが再提示した縦長イメージ図を、Mobileホームの**骨組みをそのまま再現する基準**とする。
- Order: Mobile Header → 大きなHero / Project.YURA導線 → 4分割ナビ帯 → 大きなWorld帯 → Footer。
- Decision: 4分割ナビ帯は `About / Technology / Gallery / News`。Worldはこの帯には置かず、その下の大きなWorld帯から `/world` へ接続する。
- Decision: Desktopホームは既存構成を維持し、Mobileのみ別レイアウトとしてCSS media queryで切り替える。
- Decision: イメージ図そのものをWebへ貼り付けず、HTML/CSSと正式素材で再構成する。
- Decision: イメージ図内の文章は最終FIXではなく、Mobile Homeのコピーは後から調整可能とする。
- Asset constraint: 黒を主役にしたヴィクトリア朝衣装の久遠ゆら正式素材はまだ未提供。白系ドレスを代用せず、Hero/Worldのビジュアル領域は構造だけ先に実装する。画像生成は行わない。
- Supersedes: D-024/D-026/D-030のMobileレイアウト詳細を、この骨組みに合わせて具体化する。黒＋金、白ワードマーク、Mobile News、World帯の役割は継続。


### D-032 — Mobile footer and World band compactness
- Status: ACTIVE
- Area: Mobile homepage / World band / Footer
- Decision: Mobile Footerは情報量を減らさず、Desktop版に近い密度へコンパクト化する。Mobileではブランド情報を左、Official X / YouTubeを右へ配置し、縦方向の余白を縮める。
- Decision: Mobileの大きなWorld帯は、現状より明確に短くし、見せ場を残したまま従来高の約75〜80%程度を基準とする。
- Decision: Mobile HeaderのMEMORIELA表示は現時点では文字のまま維持し、正式ロゴ差し替えは別工程で行う。
- Notes: 今回は骨組み・余白・高さのみ調整し、コピー内容や画像素材は変更しない。
- Supersedes: D-031のMobile Footer / World帯のサイズ詳細のみ。


### D-033 — Mobile World band copy and visual width
- Status: ACTIVE
- Area: Mobile homepage / World band
- Decision: Mobile World帯の大見出し `World` は削除する。Worldの役割は `漫画・物語・日常` の表示で担保する。
- Decision: World帯全体の高さは維持しつつ、左側の画像 / ビジュアル領域だけを横方向に狭める。
- Implementation: Mobile World帯の左右比率は `44 / 56` から `34 / 66` へ変更する。
- Notes: `MEMORIELA WORLD` の小ラベル、`漫画・物語・日常`、`詳しく見る →` は維持する。
- Supersedes: D-032のWorld帯内部レイアウト詳細のみ。


### D-034 — Mobile About label and duplicate CTA removal
- Status: ACTIVE
- Area: Mobile homepage / About
- Decision: Mobile Hero内の `Project YURAへ` ボタンは、4分割帯の `About` と遷移先が重複するため削除する。
- Decision: Mobile 4分割帯の `About` の補助表記は `久遠ゆら` から **`キャラクター`** へ変更する。
- Decision: Aboutの遷移先は久遠ゆら単独ではなく、キャラクターを扱うページとして構成し、久遠ゆらに加えて **Pin銀** も含める方向で進める。
- Notes: Aboutページ本文の具体的な構成・デザインは、遷移先ページを仕上げる工程で決定する。今回の変更はHome骨組みのみ。
- Supersedes: D-023のAboutを久遠ゆら単独中心として読める部分、およびD-031のMobile Hero内Project.YURA導線。


### D-035 — About becomes Characters
- Status: ACTIVE
- Area: Primary navigation / Character page
- Decision: 主要ナビゲーションの `About` は **`Characters`** に変更する。
- Decision: 正式ルートは `/characters` とし、旧 `/about` は互換性のため `/characters` へリダイレクトする。
- Decision: Charactersは久遠ゆら単独ではなく、**MEMORIELA / Project.YURAに登場するキャラクターをまとめる入口**として扱う。
- Decision: 現時点で久遠ゆらに加えて **Pin銀** を掲載対象に含め、将来2人目以降のキャラクター追加にも対応できる役割とする。
- Decision: Desktop主要ナビは `Characters / Technology / Gallery / Contact / World`、Mobile 4分割帯は `Characters / Technology / Gallery / News` とする。
- Notes: Charactersページ本文の最終レイアウトとPin銀の具体的な見せ方は、遷移先ページを仕上げる工程で決定する。
- Supersedes: D-023 / D-030 / D-034 の `About` 表記・役割・ルート。
