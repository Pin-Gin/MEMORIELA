# MEMORIELA YouTube Production Rules

Status: **CANONICAL / MANDATORY**
Adopted: 2026-09-18
Purpose: MEMORIELA公式YouTube動画を、AI・編集ソフト・担当チャットが変わっても同じ品質基準で制作する。

## 1. First principle

ユーザーからラフな依頼を受けた場合、AIはその文面をそのまま動画生成ツールへ投げません。

次の順で処理します。

**rough request**
→ **intent interpretation**
→ **production brief**
→ **canon / asset / rights check**
→ **script / storyboard**
→ **production**
→ **edit**
→ **QA**
→ **metadata**
→ **user approval**
→ **publish**

ユーザーが明示的に即制作を求めた場合も、内部では必要な確認を行います。

## 2. Preserve intent

AIが制作指示を書き直す際は、ユーザーの目的を変えません。

許可される整理:

- 曖昧な順序を整理する
- カット単位へ分解する
- 尺・画角・音・テロップを構造化する
- 技術的に実行可能な表現へ置き換える
- 重複した指示を統合する
- 欠落している制作上の前提を合理的に補う

禁止:

- 勝手にストーリーの意味を変える
- 勝手にYURAの人格を変える
- 勝手に派手な演出を追加する
- 勝手にブランド表記を変える
- ユーザーが求めていない宣伝文句を追加する
- 「伸びそう」という理由だけで内容をクリックベイト化する

## 3. Best-first creative direction

複数案が考えられる場合、第一候補を最初に提示します。

第一候補は以下を総合して選びます。

1. 動画の目的への適合
2. YURA / MEMORIELAとの整合
3. 視聴開始直後の理解しやすさ
4. 独自性
5. 制作コスト
6. 素材・権利リスク
7. 将来のシリーズ展開
8. 再利用可能性

理由なく後から別案へ乗り換えません。

## 4. Required production brief

原則として各動画に以下を定義します。

- Working title
- Objective
- Audience
- Format: Short / long-form / other
- Core message
- Hook
- YURA role
- Visual concept
- Story / information flow
- Required shots
- Voice / dialogue
- Music / SFX
- On-screen text
- CTA
- Required assets
- Rights / license status
- AI-generation / edit tools
- Deliverables
- Explicit constraints

未確定項目は未確定として扱い、勝手に恒久仕様へしません。

## 5. Hook rule

Shortsでも長尺でも、冒頭は内容と一致する見せ場・疑問・変化から始めます。

ただし、実際の動画内容と一致しない誇張・虚偽・誤認誘導は使いません。

「強い導入」と「釣り」は区別します。

## 6. One-video-one-core rule

一本の動画で最も伝えたいものを一つ決めます。

情報を増やすことで主題が弱くなる場合は分割を優先します。
シリーズ化できるものを一動画に詰め込みすぎません。

## 7. YURA-specific rule

YURAが登場する動画制作では、制作前に必要なProject YURA正本を読みます。

特に画像・映像生成では:

- Visual Identity Masterを起点にする
- 顔・髪・瞳・身体比率を動画ごとに再解釈しない
- 派生衣装やポーズはMASTERから派生させる
- 参照画像の役割を限定する
- 3Dモデルを使う場合もキャラクター同一性を維持する

YouTube側の都合でYURAを別キャラクター化しません。

## 8. Shot / scene instruction rule

動画生成AIへ渡す指示は、長い一文ではなくシーン単位に分けます。

各シーンで必要に応じて:

- duration
- subject
- action
- camera
- framing
- environment
- lighting
- expression
- continuity from previous shot
- forbidden changes

を明示します。

継続ショットでは特に:

- 同一人物
- 同一衣装
- 同一髪型
- 同一アクセサリー
- 時間帯
- 光源方向
- 背景位置
- カメラ軸

の連続性を確認します。

## 9. Editing rule

編集は「何かを常に動かす」ことを目的にしません。

優先順位:

1. 内容が伝わる
2. YURAの魅力が伝わる
3. テンポが崩れない
4. 視線誘導が自然
5. 音が聞き取りやすい
6. 演出が内容を邪魔しない

不要なズーム、過剰な効果音、過剰な字幕、意味のないトランジションを自動追加しません。

## 10. Subtitle / text rule

テロップは音声の完全な複製を必須としません。

- 理解に必要な語
- 固有名詞
- 強調したい一文
- 無音視聴でも必要な情報

を優先します。

誤字、Project名、キャラクター名、URL、ハンドルの表記揺れを公開前に確認します。

## 11. Audio rule

音声・BGM・SEは映像と同じく権利資産として扱います。

- 出所不明音源を使用しない
- 「ネットにあった」は使用根拠にしない
- 商用利用条件・YouTube利用条件・クレジット条件を確認する
- 他者の声の無断クローンを使用しない
- YURA用音声方式が正式決定した場合は正本へ接続する

BGMより台詞・ナレーションの明瞭性を優先します。

## 12. Asset provenance rule

外部公開する動画では、使用素材の出所を追える状態にします。

最低限、重要素材について以下を保持します。

- asset name
- source / creator
- generated or third-party
- tool / service
- license / permission
- modification
- date acquired/generated

AI生成物でも、使用サービスの規約上公開可能かを必要時に確認します。

## 13. AI use rule

AIは企画、脚本、絵コンテ、画像、動画、音声、字幕、編集補助などに使用できます。

ただし:

- 量産だけを目的にしない
- 動画ごとに独自の企画価値を持たせる
- 出力を無検証で公開しない
- 不自然な人物・文字・物理破綻を確認する
- 実在人物・現実の出来事をリアルに改変する場合は、YouTubeの最新AI開示要件を確認する

「AI使用」と「YouTubeで公開時に開示が必要か」は同一ではありません。
公開時の開示判定は最新のYouTube公式ルールに従います。

## 14. No mass-template rule

同じテンプレートへ台詞や背景だけを差し替えた動画を大量投稿する運用を標準にしません。

共通OP / ED /シリーズフォーマットは使用可能ですが、動画本編には各回固有の:

- story
- information
- commentary
- demonstration
- character interaction
- development

のいずれかを持たせます。

## 15. Metadata rule

タイトル・サムネイル・説明文は、動画本編と一致させます。

禁止:

- 動画に存在しない出来事をサムネイルへ描く
- 誤認させるタイトル
- 関係のない人気キーワードの詰め込み
- 虚偽の公式性・提携・実績の主張
- 実在人物が関与しているように見せる無断AI表現

CTR最適化は許可しますが、内容一致を前提にします。

## 16. Format specifications

解像度、尺、容量、エンコード、Shorts判定等のYouTube依存仕様は変化し得ます。

そのため、この正本では不変値として固定しません。
実制作・投稿時に必要な場合はYouTube公式仕様を確認します。

社内制作上の推奨値を固定する場合は、別途明示的に決定して本書へ追加します。

## 17. Approval boundary

公開判断はユーザーが行います。

AIは以下を明確に分けます。

- draft
- ready for review
- approved
- published

「動画ファイルが完成した」だけで公開承認済みとは扱いません。

## 18. Reuse rule

過去動画を再利用する場合:

- 元動画の権利状態を確認する
- 単純再投稿ではなく目的を確認する
- Short化、再編集、総集編等では新しい価値を追加する
- 古いブランド表記や旧YURA仕様をそのまま再公開しない

## 19. Failure handling

生成・編集結果に問題がある場合は、全体を無条件で作り直す前に原因を特定します。

- prompt ambiguity
- model limitation
- reference conflict
- continuity failure
- asset issue
- edit issue
- source material issue

局所修正で直る場合は局所修正を優先します。
YURAの正本自体を失敗出力へ合わせて変更しません。
