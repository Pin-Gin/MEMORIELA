# YURA Prompt Rewrite Workflow

Status: PROTECTED WORKFLOW
Adopted: 2026-09-12
Updated: 2026-09-12 — cross-chat continuity / 3D pose-reference separation clarified
Purpose: YURA画像生成時に、ユーザーの自然言語指示を生成モデルが誤解しにくい構造化指示へ変換し、認識一致を確認してから生成するための正式フロー。

## 1. Default workflow

YURA画像生成の標準手順は以下とする。

**User rough request**
→ **Assistant rewrite / structure pass**
→ **User recognition check**
→ **Image generation**

原則として、構図・ポーズ・接触・家具・複数条件を含むYURA生成では、この確認ステップを省略しない。

新しいチャットでは、生成前に `docs/assistant-context/YURA_START_HERE.md` と `docs/assistant-context/creation/yura/START_HERE.md` を読み、現在の正本状態を復元してから本フローを使用する。

## 2. Step 1 — User rough request

ユーザーは自然な言葉で希望を書いてよい。

例:

`朝のベランダで柵に腕を組んで、横を向いて頭を腕に乗せている。ラフな服＋カーディガン。低いポニーテール。微笑んでいる。`

この段階では曖昧さがあってよい。

## 3. Step 2 — Assistant rewrite

Assistantはユーザー意図を変えず、画像生成モデルが解釈しやすい形へ整理する。

### 必須確認項目

- YURA MASTER identityを維持すること
- BODY比率 / 7.25頭身
- 顔 / 目 / 髪 / 描画文法
- シーン
- 時間帯
- 衣装
- 髪型
- 表情
- 体の向き
- 顔の向き
- 腕 / 手 / 脚
- 接触物
- 荷重点
- 支持点
- カメラ / 画角
- 余白 / 用途
- 避けるべき破綻

### Rewrite rule

曖昧語は具体化する。

`腕組み` → どの腕がどこにあるか

`寄りかかる` → どの身体部位が何に接触し、どこへ荷重しているか

`頭を乗せる` → 頭のどの部分を、何の上に、どの程度預けるか

`くつろぐ` → 背中・骨盤・脚・肩の状態

ただし、ユーザーが指定していない重要な意匠を勝手に追加しない。

## 4. Step 3 — Recognition check

Assistantは生成前に、整理後の解釈を短く提示する。

理想形:

- YURA固定条件
- シーン
- 衣装 / 髪
- ポーズの物理構造
- 表情
- カメラ
- 破綻防止条件

ユーザーが以下のように承認したら生成へ進む。

- OK
- その認識で合ってる
- それで
- 生成して
- 問題なし

修正が入った場合は、修正後の認識を反映し、必要なら再度短く確認する。

## 5. Risk labeling for complex poses

複雑ポーズでは必要に応じて3段階で提示してよい。

### 安定案

人体構造・接触面が十分見える。生成成功率優先。

### 少し複雑な案

構図の魅力と安定性の中間。

### 高リスク案

隠れた関節・多重接触・荷重不明が多い。PoseMy.Art / OpenPose等を推奨。

ユーザーが高リスク案を明示的に選べば、その意図を尊重して生成する。

## 6. Pose reference workflow

PoseMy.Art / OpenPose / 3D画像がある場合:

1. 画像からポーズ・関節・接触構造・重心・カメラを読む
2. 参照内の簡易shape / furnitureに必要な意味を付ける
3. YURA MASTER identityを別レイヤーとして維持する
4. テキストで接触・荷重・隠れた支持構造を補足する
5. ユーザー確認
6. 生成

### 6.1 Extract from 3D reference only

参照してよい情報:

- 関節配置
- 腕 / 脚の構成
- 体幹の傾き / ひねり
- 頭の向き
- 重心
- 支持点
- 接触点
- 荷重方向
- 手足の前後関係
- カメラ位置 / 画角 / フレーミング
- 家具 / 柵 / 机などの構造的位置

### 6.2 Do not inherit from 3D reference

参照してはいけない情報:

- 3Dモデルの体型 / 頭身 / BODY比率
- 顔
- 髪
- 簡易参照衣装
- CGI / 3Dレンダリング文法
- マテリアル / 質感
- ライティング表現
- 色調

完成画像ではYURA MASTER / protected FACE / BODY / HAIR / RENDERINGが常に優先される。

生成モデル向けには必要に応じて次の意味を明示する:

`添付画像はポーズ・関節配置・重心・接触位置・カメラ構図のみ参照する。添付画像の3Dレンダリング、体型、顔、髪、簡易衣装、質感、ライティング表現は参照しない。描画はYURA MASTER準拠の高品質2Dアニメイラストを優先する。`

### 6.3 Fixed simple reference clothing

裸に見える3Dマネキンを生成参照へ変換するときは、原則として:

- 無地・装飾なしのシンプルインナー
- 無地・装飾なしのシンプルショートパンツ
- 淡色 / ニュートラル
- ロゴ / 文字 / 柄 / アクセサリーなし

を使用する。

これは参照用カバーであり、完成YURAの衣装ではない。

簡易服化するときも元3Dポーズの関節・支持点・接触点・重心・体幹の傾き・手足の前後・カメラを変えない。

詳細は `docs/assistant-context/creation/yura/generation/pose/POSE_GENERATION_GUIDELINE.md` を正本とする。

## 7. Rewrite output style

生成前の確認文は長すぎない。

推奨:

`認識はこう。YURA本人はMASTER固定。朝のベランダ、低いポニーテール、装飾なし。ラフなトップス＋カーディガン。両前腕を水平な柵に置き、左右の肘と手の位置が読める状態で軽く体重を預ける。頭は腕へ完全には乗せず、横向きに頬を近づける。こちらへ柔らかく微笑む。カメラは目線付近。これで生成する。`

ユーザーが違う部分を直しやすい文章にする。

## 8. No silent reinterpretation

Assistantは、複雑ポーズを安定化するためにユーザーの意図を勝手に別ポーズへ変更しない。

変更を提案する場合は:

- 何が不安定か
- どう変更すると安定するか

を明示し、ユーザーの承認を得る。

## 9. Immediate-generation exception

ユーザーが明確に:

- 確認いらない
- そのまま生成して
- 即生成して

などと指示した場合は、内部で構造化した上で確認文を省略して生成してよい。

ただし、MASTER / BODY / FACE / HAIR / RENDERINGの保護条件は省略しない。

## 10. Relationship to generation template

具体的な入力欄は `docs/assistant-context/creation/yura/generation/GENERATION_TEMPLATE.txt` を使用する。

複雑ポーズの物理ルールは `docs/assistant-context/creation/yura/generation/pose/POSE_GENERATION_GUIDELINE.md` を使用する。

本書は、**生成前にどう会話を進めるか**を規定する。

## 11. Change control

このワークフローは保護対象です。

今後YURA画像生成では、ユーザーのラフな自然言語を尊重しつつ、誤解しやすい構造を明文化してから生成する。

重要な変更はGitへ記録する。
