# YURA 表情差分17種 — 新規チャット引継ぎ・制作仕様

Status: **EMOTION DEFINITIONS AUTHOR-CONFIRMED / FACE-UP IMAGE GENERATION NOT STARTED / NO EXPRESSION IMAGE PROMOTED**
Updated: 2026-10-18
Layer: **project-management / 運用・承認管理のみ（Visual Authorityそのものではない）**

## 0. この文書の目的

既存のYURA Face Identityを一切再設計せず、作者確定の「表情名＋3感情要素」に基づく**17種類の表情差分マスター画像**を、肩から上のFace-upとして制作・作者検収・テキスト化・Git登録する。

新規チャットや生成エンジンの変更後も、感情構成・入力Authority・構図・レンダリング品質・評価手順が変わらないようにする。過去チャットの暗黙の記憶ではなく、現在のGit `main` と本書に記録された**作者確定の表情一覧**を基準とする。

**重要な数え方**：E00「真顔」は既存の正式Face Referenceが基準画像として担うため、新規生成の対象外。既存E00を含めると表情定義は合計18種だが、**今回新規制作する表情差分はE01〜E17の17種**。追加確定した「寂しさ」を消したり、他の確定表情を無断で置き換えたりしない。

## 1. 現在の到達点と未完了項目

- DONE：YURAの正式 Face Reference / Face-up Masterテキスト、Ear Geometry Master、Full-body MasterがGitで正式登録済み。
- DONE：作者は本書のE00〜E17に記す表情名と**3感情要素の組合せ**を承認済み。
- DONE：今回の表情生成方式を「正式顔マスターを参照した、肩から上のFace-up・表情のみ差分」と決定。
- NOT STARTED：今回のE01〜E17各表情のマスター用生成・作者による個別画像PASS・視覚特徴の確定。
- NOT STARTED：E01〜E17の承認済みPNGと画像観察に基づく各表情のマスター記述の正式登録。
- NO CHANGE：既存の有料Full-body Master再生成ルートは凍結（`paid_generation_allowed=false`）。本計画は有料呼び出しの再許可ではない。

**感情定義の確定 ≠ 生成された画像の承認。** 各画像は作者が実物を見てPASSするまで候補にすぎない。

## 2. 必ず読み込むAuthorityと参照優先順位

現在の `Pin-Gin/MEMORIELA` リポジトリ `main` を起点とし、以下を確認する。すでにGit上で正式採用された画像はファイル名ではなく**その実際の画像内容**を参照する。

1. `project-management/yura-visual/START_HERE.md` — プロジェクトの引継ぎ入口。
2. `project-management/yura-visual/CURRENT_STATE.md` — 現在の完成・凍結状況。
3. `visuals/yura/identity/master/YURA_VISUAL_TEXT.md` — **YURA最高位Visual Text Authority**。
4. `visuals/yura/identity/face/YURA_FACE_REFERENCE.png` — **表情差分の主画像マスター**、作者承認済みのFace Identity / Face Geometry。
5. `visuals/yura/identity/face/YURA_FACE_UP_MASTER.md` — 承認済みFace-upの詳細な顔・目・フレーミング仕様。
6. `visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md` — 現行Faceの補足仕様。
7. `visuals/yura/identity/ears/YURA_EAR_BASIC_RULES.md` と `visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png` — 耳形状・髪の自然な遮蔽。
8. `visuals/CHARACTER_RENDERING_STYLE.md` — **作品共通のMatte Natural Animeレンダリング品質基準**。
9. **本書** — 今回の表情ID・感情3要素・作業方法・検収手順を拘束する運用仕様。外見Authorityの上書き権限はない。

`visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png` は正式全身統合マスターだが、**今回の肩上Face-upの主画像はFace Reference**。 `visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png` は全身比率の復旧補助であり、表情変更に使用して顔を作り直すことは禁止。

現行 `YURA_VISUAL_TEXT.md` に含まれる「新Face Referenceへの置換前」などの**歴史的な移行中記述**が、現在のGit上で承認・昇格済みのFace Referenceを無効化することはない。ただし、元テキストの外見定義自体を無断で改変・無視してはならない。整合できない場合は推測で埋めず作者に確認する。

## 3. 作者確定：表情定義一覧（IDと3感情要素を固定）

E00は既存基準。**新規生成対象はE01〜E17、計17種**。下表の「表現方向」は作者と調整するための意味説明であり、口の開き角度・目の閉じ具合・涙・赤面などの細部を先回りして確定するものではない。

| ID | 表情名 | **確定した3感情要素（表記固定）** | 表現方向（解釈補助） | 今回の画像 |
|---|---|---|---|---|
| E00 | 真顔（通常） | **愛嬌＋可愛さ＋少し幼さ** | 喜怒哀楽を付加しないYURAの基準顔。笑顔・困り顔ではない | **既存Face Referenceを使用／再生成対象外** |
| E01 | 微笑み | **愛らしさ＋穏やかさ＋親しみ** | 口元に小さな笑み | 未生成 |
| E02 | にっこり笑顔 | **愛らしさ＋素直な喜び＋明るさ** | 自然で明るい笑顔 | 未生成 |
| E03 | 満面の笑み（喜色満面） | **愛らしさ＋天真爛漫＋無垢** | 顔全体に現れる純粋な喜び。「口を最大限開ける」と同義ではない | 未生成 |
| E04 | はにかみ笑顔 | **愛らしさ＋照れ＋初々しさ** | 少し恥ずかしそうな笑顔 | 未生成 |
| E05 | いたずらっぽい笑顔 | **愛らしさ＋茶目っ気＋遊び心** | 遊び心を含む笑顔 | 未生成 |
| E06 | わくわく | **無垢＋好奇心＋期待** | 期待と好奇心が伝わる表情 | 未生成 |
| E07 | 驚き | **無垢＋驚き＋素直さ** | 思いがけない出来事への純粋な反応 | 未生成 |
| E08 | きょとん | **無垢＋不思議さ＋純真** | 状況を理解しかねる不思議そうな反応 | 未生成 |
| E09 | 困惑 | **素直さ＋戸惑い＋不安** | どうしてよいか分からない気持ち | 未生成 |
| E10 | すねる | **愛らしさ＋不満＋甘え** | 少しむくれた気持ち | 未生成 |
| E11 | 怒り | **素直さ＋反発＋負けん気** | 反発心を示す怒り | 未生成 |
| E12 | 真剣 | **集中＋意志＋ひたむきさ** | 何かに真剣に集中 | 未生成 |
| E13 | 心配 | **優しさ＋不安＋気遣い** | 相手への気遣いを伴う心配 | 未生成 |
| E14 | 悲しみ | **繊細さ＋儚さ＋我慢** | 悲しみを静かにこらえる。主成分は「我慢」 | 未生成 |
| E15 | 泣き顔 | **無垢＋悲しみ＋感情のあふれ** | 抑えきれない感情が泣く様子に表れる | 未生成 |
| E16 | 安堵 | **穏やかさ＋安心＋喜び** | 張りつめた気持ちがほぐれる | 未生成 |
| E17 | 寂しさ | **不安＋儚さ＋不満** | 満たされない気持ち・寂しさ。「我慢」中心のE14とは区別 | 未生成 |

**E14 悲しみ**（繊細さ＋儚さ＋我慢）と **E17 寂しさ**（不安＋儚さ＋不満）は別のマスターとして扱い、混同しない。

**E01 / E02 / E03** は笑顔の強度・性格が異なる。E03の作者確定語は「満面の笑み＝愛らしさ＋天真爛漫＋無垢」。一般的な笑顔という語に縮退させない。

ユーザーが今後明示的に修正しない限り、ID・名称・3要素・作品上の意味を自動変更しない。

## 4. 毎回固定するFace-up生成条件（品質維持のため必須）

- **正規の参照画像**：毎回、元の `YURA_FACE_REFERENCE.png` を新たに入力する。前回作った候補表情を次の表情の原本として連鎖使用しない（Identityの累積ドリフト防止）。
- **参照するテキスト**：現行Visual Text＋Face-up Master＋Face Redesign Spec＋耳ルール＋作品共通Rendering Style＋本書の対象ID／感情3要素。
- **構図**：YURA 1人、**肩から上**のFace-up、真正面、カメラ目線、頭を傾けない、頭部全体を完全に含む、頭頂・髪・顔・必要な肩を切らず、中央配置、**正方形キャンバス**、白背景。
- **髪**：Face Referenceが示す現在の髪型・前髪・顔まわりの毛束・銀白色を固定。指定がない限りシニヨン等への髪型差分、髪飾り、毛束の大幅変更は行わない。肩上のトリミングは本来の超ロングの長さを変える許可ではない。
- **顔Identity**：承認済みの顔輪郭・短めの縦印象・頬・顎・目の基本形・目位置（C2基準→0.3%内側）・虹彩グレーブルー・瞳孔の真円構造と左右対称性・鼻・耳の実形状を維持。成熟顔化・過剰幼児化・別キャラ化は禁止。
- **表情変化を許可する部分**：眉の表情運動、まぶたの開閉・細め、口の開閉・口角、頬・目元の表情に伴う自然な変化のみ。**眼球配置・顔骨格・目の基本設計を変更して「表情」を表現しない。**
- **E00との関係**：既存の`真顔／閉じた口`は中立基準。E01〜E17は作者が明示した表情例外であり、真顔へ強制的に戻さない。開口・涙・赤面などの視覚細部は各候補を作者が評価した時点で確定し、3感情要素だけを理由に自動固定しない。
- **描画**：高品質2Dアニメのみ。Matte Natural Animeを保持し、細く繊細な線、soft celを基礎とした柔らかな陰影、低〜中コントラスト、マットな肌・髪、明るく自然な色白。写実／半写実／3D／CGI、強いテカリ、過剰な美顔補正は禁止。
- **背景・装い**：表情比較が目的。白背景、顔以外の要素は可能な限りFace Referenceに揃え、服装・肩位置・ライティング・画角などの不要な差分を増やさない。
- **1回の制作対象＝1つの表情ID**。同じ画像内に複数の表情を並べたり、未承認候補を他表情へ流用しない。

このプロジェクトのFace-upは全身用の頭身・Body Geometry・衣装表現を検証する工程ではない。構図や身体比率の話を理由に顔を作り直さない。

## 5. 実制作手順（17回の作者承認ループ）

各E01〜E17について以下の順序を固定する。

1. **読み込み**：Git `main` の現行Authority、該当するFace Referenceの画像、対象表情IDの3感情要素を確認。参照が読めなければ生成せず不足を報告する。
2. **単独生成**：元のFace Referenceを参照して、肩上・正面・カメラ目線・正方形・白背景、対象表情だけ変更した候補を**1枚**生成。重要条件を省略した短縮プロンプトへ置き換えない。
3. **差分比較**：生成結果を公式Face Referenceと並べ、(a) Face Identity、(b) 3感情要素の印象、(c) 表情区別、(d) 顔部品の保持、(e) 耳の自然な遮蔽、(f) レンダリング、(g) Face-up構図を確認。
4. **作者判定**：作者に画像を提示し、**PASS / 修正 / FAIL** を得る。アシスタントは自己判定だけでPASSや正式Master昇格を宣言しない。
5. **修正が必要な場合**：失敗要因を特定し、必要な表情差分だけを最小変更する。顔の基本形やスタイルを再設計しない。FAIL画像を新たなIdentity原本として使わない。
6. **PASS後のテキスト化**：採用画像に実際に見える眉、まぶた、目元、口、頬、表情強度の具体的状態だけを文章化する。見えない情報、未確認の涙・赤面などを推測で追記しない。
7. **正式登録**：承認されたPNGと、ID・名称・3感情要素・観察された表情特徴・画像パス・作者PASS・コミット情報を記録する。Git上の保存パス・ファイル命名は作者と合意してから決定する。
8. **次へ**：前IDがPASS・記録済みになったことを確認してから次IDへ進む。表情一覧表の定義は勝手に書き換えない。

**品質ゲート：1件でもFace Identityまたはレンダリングが崩れた画像は、表情が良くてもFAIL。** 表情の3要素が不明瞭な画像も採用しない。劣化した候補を受け入れて17枚をそろえることを優先しない。

## 6. 各マスターの確定記録テンプレート

承認後に、以下を各表情の成果物テキストへ記録する（現時点ではまだ記入しない）。

```text
Expression ID:
Expression name:
Fixed emotional composition (3 factors):
Primary Face Reference path / revision:
Approved expression PNG path:
Visible eyebrow changes:
Visible eyelid / eye-expression changes:
Visible mouth / lip-corner changes:
Visible cheek / facial expression changes:
Expression strength / distinguishing characteristics:
Permitted expression-only deviations from E00:
Forbidden drift / confirmed non-changes:
Rendering / framing QA: PASS / FAIL
Author image judgment: PASS / FAIL / PENDING
Commit SHA / approved image SHA-256 (after registration):
```

このテンプレートの詳細記述は**作者PASS画像を観察した後**に埋める。画像生成前の感情ラベルを、観察済み形状データであるかのように記載しない。

## 7. 達成条件（Definition of Done）

以下が**全て**満たされた時点で表情差分プロジェクトを完了とする。

1. **E01〜E17の17枚**について各表情と指定3感情要素が保持され、相互の識別性がある。
2. 各採用画像が同一の承認済みYURA Face Identityを保ち、Face-upの構図とMatte Natural Anime品質を満たす。
3. 17枚**すべて**について作者が画像単位で明示的に**PASS**を出している。
4. 各PASS画像を観察して表情の見える特徴をテキスト化し、元の3感情要素と矛盾しない記録がある。
5. 画像・記録がGit `main` に正式配置され、対象ID・PNG・記述文・承認状態・コミット参照が対応づけられている。
6. E00の中立顔マスター、現行Visual Text、Face / Ear / Full-body Authorities、作品共通レンダリング、凍結中の有料ルートを無断で改変していない。
7. `project-management/yura-visual/` の進捗・新規チャット引継ぎが17件の実際の登録状態に更新されている。

**現時点の進捗**：感情仕様 **17/17 確定**、新規表情画像 **0/17 PASS・0/17正式登録**。E00真顔は既存正式顔マスターを使用。画像の生成・承認を完了と誤認しない。

## 8. 新規チャット開始用指示（そのまま貼り付け可）

> GitHub `Pin-Gin/MEMORIELA` の現在の `main` を正本として、まず `project-management/yura-visual/START_HERE.md` と `project-management/yura-visual/YURA_EXPRESSION_VARIATIONS_17_HANDOFF.md` を全文読み込んでください。次に文書の指定どおり現行 `YURA_VISUAL_TEXT.md`、正式 `YURA_FACE_REFERENCE.png`、`YURA_FACE_UP_MASTER.md`、耳ルール、`CHARACTER_RENDERING_STYLE.md` を確認してください。E00は真顔の既存マスター、E01〜E17が新規生成する17種類です。表情名と3感情要素は作者確定であり変更禁止。すべて肩から上のFace-up、同じFace Identityと描画品質、1表情1候補・作者PASS・観察に基づくテキスト化・Git登録を厳守してください。未承認画像や古いマスターに頼らず、まず完了／未完了状態と最初の対象IDを報告し、指示があるまで画像生成やファイル変更は行わないでください。
