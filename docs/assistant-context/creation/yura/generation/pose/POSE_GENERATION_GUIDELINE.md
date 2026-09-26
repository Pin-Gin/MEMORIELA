# YURA Pose Generation Guideline

Status: PROTECTED GENERATION GUIDELINE
Adopted: 2026-09-12
Updated: 2026-09-20 — SNS pose tolerance rule added
Applies to: 久遠ゆら / YURA の立ち絵・座り・寄りかかり・寝姿・接触ポーズ・家具 / 柵 / 机などを伴う複雑ポーズ

## 1. Purpose

この文書は、YURAの派生画像でポーズ構造が曖昧になった際に発生する、腕・手・肘・首・頭・家具接触の不自然さを減らすための正本ルールです。

ポーズはMASTER identityの上に追加する派生レイヤーであり、ポーズ失敗を理由にYURA本人のBODY / FACE / EYE / HAIR仕様を変更しません。

## 2. Authority

ポーズ生成では、Project / Image Generation Governanceのdomain ownershipを前提として次の現行正本を使用します。

1. `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`
2. `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png`
3. `docs/assistant-context/creation/yura/identity/body/BODY_MASTER.md`
4. `docs/assistant-context/creation/yura/identity/body/BODY_SPEC.md`
5. `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md`
6. `docs/assistant-context/creation/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
7. `docs/assistant-context/creation/yura/identity/hair/HAIRSTYLE_SPEC.md`
8. `docs/assistant-context/creation/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
9. `docs/assistant-context/creation/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`
10. `docs/assistant-context/creation/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md`
11. 本書
12. `docs/assistant-context/creation/yura/generation/GENERATION_TEMPLATE.txt`
13. 現在のユーザー指示 / PoseMy.Art / Daz等の構造参照

ポニーテール、シニヨン、ハーフアップ、編み込み等の髪型アレンジが同時にある場合は `docs/assistant-context/creation/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md` を併用します。通常生成ではGit履歴上の旧HAIR仕様を取得しません。


## 3. Core principle — visible structure first

AI画像生成では、見えない関節・隠れた手・複数物体の接触が増えるほど構造破綻リスクが上がります。

したがって、複雑なポーズでは「雰囲気」より先に以下を固定します。

- 支持点
- 荷重点
- 接触面
- 肩 / 肘 / 手首 / 首 / 膝の向き
- 見えるべき手足
- 隠れてよい部分
- 手前 / 奥の重なり順

## 4. Ambiguous words must be decomposed

以下のような曖昧語だけで生成しません。

- 腕組み
- 寄りかかる
- 頭を乗せる
- もたれる
- くつろぐ
- 頬杖

代わりに、物理構造へ分解します。

例:

`柵に腕組みしている`

ではなく、

`ベランダの水平な柵の上に両前腕を自然に置く。左右の肘は柵の上にあり、手首は無理に折れない。肩の力を抜き、上半身の重量を軽く前腕へ預ける。両手の位置が読み取れる。`

とする。

## 5. Contact / load rules

複雑ポーズでは必ず以下を考えます。

### 5.1 Support point

体重を支える箇所を明示します。

例:
- 足裏
- 椅子の座面と骨盤
- ソファと背中 / 骨盤
- 柵と前腕
- 枕と側頭部
- 手のひらと頬

### 5.2 Head support

頭をどこかへ預ける場合は、次のどれか一つを主支持として明示します。

- 枕 / クッション
- 手のひら
- 前腕
- 壁 / 背もたれ

複数を曖昧に混ぜない。

### 5.3 Hidden load prohibition

見えない側の手・腕・脚に、説明されていない荷重を持たせない。

### 5.4 Joint plausibility

- 手首を極端に折らない
- 肘があり得ない方向へ曲がらない
- 肩をすくめすぎない
- 首を過度に曲げない
- 膝・足首の向きが矛盾しない

## 6. Occlusion rules

3つ以上の要素が同じ場所で重なる構図は高リスクです。

例:
- 柵 + 両腕 + 頭
- 枕 + 手 + 頬
- 髪 + 手 + 首

その場合は、どの要素が手前か、どの関節が見えるかを指定します。

できるだけ以下を見せます。

- 少なくとも片方の肘
- 前腕の流れ
- 手首の方向
- 頭が何に支えられているか

HAIR v1.3のスーパーロングが関節を隠す場合、ポーズを見せるためだけに髪のコア長・総毛量を削減しません。必要ならカメラ、局所的な自然な毛流れ、補助参照角度で構造を読みやすくします。

## 7. Pose complexity classes

### A — Low risk

- 自然な立ち姿
- 歩行
- 椅子に普通に座る
- 柵に前腕を置く
- ソファに背中を預ける

### B — Medium risk

- 頬杖
- 片肘を机につく
- 両前腕を柵に置き、頬を近づける
- 脚を重ねて座る
- 横向きでクッションにもたれる

### C — High risk

- 腕組み + 柵 + 頭を完全に乗せる
- 手がほぼ隠れた状態で顔を支える
- 髪で関節が多数隠れる
- 家具・腕・顔が三重以上に重なる
- 見えない腕で荷重を支える

C相当は文章だけで無理に生成せず、PoseMy.Art / OpenPose / Daz等の3D構造参照を推奨します。

## 8. PoseMy.Art / Daz / 3D reference usage

PoseMy.Art、Daz等の構造参照は、YURA本人を定義するためではなく以下を固定するために使用します。

- 骨格
- 接触位置
- 関節角度
- 重心
- カメラ
- 家具 / 柵 / 机の位置

Basic Shapes等で作った簡易オブジェクトでも、テキストで意味を明示します。

例:

`3D参照内の細長い水平直方体はベランダの柵。YURAはその柵の上に両前腕を置いている。`

YURAの顔・EYE SIGNATURE・BODY・HAIR v1.3・2D描画文法は必ずMASTER / protected text specsを優先します。

### 8.1 Fixed safety/reference clothing for 3D pose images

3Dポーズ画像を画像生成参照として使用する前に簡易衣服を追加する場合、参照衣装は原則として以下に固定します。

- MASTERと同思想の**装飾なし・無地のシンプルなインナー**
- **装飾なし・無地のシンプルなショートパンツ**
- 淡色 / ニュートラルカラー
- ロゴ・文字・柄・レース・リボン・アクセサリーなし
- 身体に過度に密着した性的表現や透け表現を避ける
- 肩・肘・手首・骨盤・膝など、ポーズ判定に必要な主要関節を不必要に隠さない

この衣装は完成画像の衣装ではなく、**ポーズ構造を安全かつ明確に画像生成側へ渡すための参照用カバー**です。

参照衣装を追加するときは、元3Dポーズの以下を変更しません。

- 関節位置
- 支持点 / 接触点
- 重心
- 体幹の傾き
- 手足の前後関係
- カメラ位置 / 画角

完成YURA画像では、ユーザー指定の本来の衣装へ置き換えます。3D参照用のインナー / ショートパンツを完成衣装として引き継がないでください。

Daz等で最初から衣服を着せた3Dモデルを使う場合も、その衣服はユーザーが最終衣装として明示した場合を除き、ポーズ参照用外観としてのみ扱います。

### 8.2 Pose-reference isolation rule — protected

3D / PoseMy.Art / Daz / mannequin / depth / normal-map 等の参照画像からは、**ポーズに関係する情報だけを抽出して適用**します。

参照してよい情報:

- 骨格の向き
- 肩 / 肘 / 手首 / 骨盤 / 膝 / 足首などの関節配置
- 四肢の前後関係
- 体幹の傾き
- 支持点 / 接触点
- 荷重方向 / 重心
- 頭・顔の向き
- カメラ位置 / 画角 / 構図
- ポーズ成立に必要な家具・柵・机などの相対位置

参照してはいけない情報:

- 参照モデル固有の体型 / 頭身 / 胸郭 / 腰 / 脚 / 腕の太さ
- 顔 / 目 / 鼻 / 口 / 年齢感
- 瞳色 / EYE SIGNATURE
- 髪型 / 髪色 / 毛量 / 長さ
- 参照用衣装（最終衣装として明示された場合を除く）
- 3Dレンダリング / CGI / PBR / 写実質感
- ライティング / 色調 / マテリアル
- 背景デザイン（ユーザーが構図参照として明示した場合を除く）

生成時の優先関係:

**YURA MASTER / protected text specs = identity・BODY・FACE・EYE SIGNATURE・HAIR v1.3・2D描画文法**

**3D pose reference = pose・joint placement・contact・load・camera only**

3D参照の外観がMASTER / protected specsと競合した場合は、必ずYURA側を優先します。

推奨固定文:

`添付画像はポーズ・関節配置・接触位置・重心・カメラ構図のみ参照する。添付画像の体型、顔、瞳、髪、衣装、3Dレンダリング、質感、ライティング、色調は参照しない。YURA本人の外観と描画はYURA MASTERおよび保護されたビジュアルテキスト仕様を厳守する。`

## 9. Objects and props

柵・机・椅子・ソファなどを伴う場合は、オブジェクト自体も構造の一部として扱います。

明示する項目:

- オブジェクトの高さ
- 人物との距離
- 接触面
- 人物より手前 / 奥
- 人体のどこが隠れるか

Production qualityでは、小物の重複・持ち手の増殖・脚の本数などのscene artifactと、YURA identity driftを分けて評価します。

## 10. Pre-generation rewrite requirement

YURA画像生成では、原則としてユーザーのラフな指示をそのまま生成モデルへ渡しません。

生成前にAssistantが:

1. 指示を構造化
2. 曖昧な接触 / 荷重を具体化
3. YURAの固定条件を保護
4. 生成モデル向けの自然な文章へ添削
5. 必要なら破綻リスクを示す

その後、ユーザーの認識確認を得て生成します。

詳細は `docs/assistant-context/creation/yura/generation/PROMPT_REWRITE_WORKFLOW.md` に従います。

ユーザーが明示的に即時生成を依頼した場合は確認表示を省略できますが、CANON LOCK / protected domain rulesは維持します。

## 10A. SNS production pose tolerance — user-approved

When the user requests an image specifically for **SNS / X / social posting**, small pose deviations are acceptable unless the user explicitly requests strict pose matching.

Allowed tolerance includes minor, natural variation in:

- arm / elbow / wrist angle
- hand position or finger arrangement
- walking step phase / leg spacing
- torso lean / shoulder angle
- head tilt / gaze direction
- natural clothing / hair interaction caused by the pose

Priority in SNS mode:

1. YURA identity and protected CANON remain exact in authority
2. BODY proportions and anatomy remain valid
3. requested scene / mood / action remain clearly readable
4. pose should look natural and production-usable
5. exact joint-by-joint reproduction is secondary unless explicitly requested

Not allowed under this tolerance:

- extra / missing limbs or fingers caused by generation artifacts
- impossible joints / broken load or contact structure
- BODY proportion drift
- FACE / EYE / HAIR / RENDERING drift
- changing the intended action into a materially different pose

If the user provides a precise pose reference, says the pose is fixed, or requests exact / strict reproduction, this SNS tolerance is disabled for that request and the normal strict pose/reference rules apply.

## 11. Do not over-iterate

小さなポーズ修正のために全体を何度も再生成すると、良かった顔・雰囲気・衣装が離れる場合があります。

- BODY / identityが安定しているなら、失敗箇所を限定して評価する
- scene / prop artifactだけでMASTERを変更しない
- 生成を重ねて全体が悪化し始めたら、最後の良好候補へ戻る

## 12. Change control

このガイドラインは保護対象です。

YURAのMASTER / BODY / FACE / EYE SIGNATURE / HAIR v1.3 / RENDERINGをポーズ側の都合で変更してはいけません。

ポーズ生成の重要な新知見が恒常ルールを変更する場合のみ、DESIGN_SPECとして本書または適切なcurrent Authorityへ反映します。単なる検証履歴はcurrent Git Authorityへ蓄積せず、Git history / external archiveへ残します。
