# 久遠ゆら・髪型基準

Status: **PROTECTED HAIRSTYLE SPECIFICATION / CURRENT HAIR DOMAIN OWNER**
Current Revision: **v1.3**
Adopted: 2026-09-15
Updated: 2026-09-19 — Strong Braided Half-Up protected sub-spec linked
Applies to: 久遠ゆら / YURA の画像生成・立ち絵・表情差分・衣装差分・公開用ビジュアル

## 1. Purpose

本書は、久遠ゆら / YURA の髪色・基本長・毛量・髪質・前髪・顔まわり・背面連続性・重力挙動を文章仕様から安定再生成するための、現在の **HAIR domain 正本** です。

髪型生成では本書を current HAIR domain owner として使用し、通常生成ではGit履歴上の旧HAIR仕様や過去派生画像から再構成しないでください。

通常の下ろし髪 / arrangement指定のない基本髪型は、本書のコア値を具体化した protected sub-spec:

`docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`

を併用します。このsub-specは本書を置き換えず、Normal Super-Longのシルエット・正面 / 背面分布・通常時の具体的な見え方のみを固定します。

ポニーテール、ローシニヨン、ハーフアップ、編み込み等の派生アレンジ構造は `docs/assistant-context/creation/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md` を併用します。本書が髪のコアを所有し、アレンジガイドは結び位置・収束・収納・重力・カメラ投影のみを所有します。`ハーフアップ + 編み込み強め` / `Strong Braided Half-Up` が明示された場合は、さらに protected specialized sub-spec `docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/SPEC.md` を必ず適用します。

---

## 2. Fixed core elements

原則として維持する髪型コア要素:

- 髪色: **銀白色**
- 長さカテゴリ: **スーパーロング**
- 基準長: **主な毛先が自然なウエストライン付近〜わずかに下まで届く**
- 最長の細い毛先: **腰の上部〜上臀部手前までを許容**
- 明確な上限: **臀部中央や太ももまで通常状態で伸ばさない**
- 髪質: **一本一本は細く柔らかい**
- 総毛量: **標準よりやや多め**
- 全体印象: 上品・柔らかい・大人っぽい
- ウェーブ: ごく緩やかで自然
- 前髪: 重すぎない薄めのロングバング
- 顔まわり: 頬に沿う長めのサイドバング + 柔らかなレイヤー
- 毛先: 下方へ進むほど自然に量が抜け、軽く繊細に収束

### 2.1 Length interpretation — protected

YURAにおける `スーパーロング` は、一般的なカテゴリ名だけで自由解釈しません。

正式基準:

- 主体となる毛先群は **自然なウエストライン付近〜わずかに下**。
- 最も長い細い毛先のみ **腰の上部〜上臀部手前**まで自然に届いてよい。
- 胸下で大部分が終わる場合は短すぎる。
- 臀部中央、臀部下部、太ももまで大きな毛量が伸びる場合は長すぎる。

したがって、生成QAでは:

- ウエスト付近 = 基準 PASS
- ウエストを少し越える = 許容 PASS
- 最長の繊細な毛先だけが上臀部手前 = 許容 PASS
- 胸下中心 = FAIL — too short
- 臀部中央〜太ももへ主要毛量が到達 = FAIL — too long

と解釈します。

---

## 3. Hair mass / texture — protected eight conditions

以下の8条件は正式な保護仕様です。

1. 毛量: **標準よりやや多め**
2. 一本一本: **細く柔らかい**
3. 上部: **長さの自重で自然に落ち着く**
4. 中間〜背中: **十分な密度を保つ**
5. 横幅: **あまり広がらない**
6. 毛先: **徐々に量が抜け、軽く繊細に収束する**
7. **「細い髪 = 少毛」と解釈しない**
8. **ポニーテール・シニヨン・ハーフアップ等のまとめ髪でも総毛量を勝手に減らさない**

### Intended silhouette

- 頭頂部・側頭部を毛量だけで過度に膨らませない。
- 長さの自重により頭頂〜上部は比較的落ち着く。
- 中間部には十分な髪密度を残す。
- 主たる流れは背中側へ縦方向に落ちる。
- 毛量がやや多くても左右へ扇状・三角形状に大きく張り出さない。
- 下方へ進むほど自然にテーパーし、毛先は軽く細く収束する。
- 一本一本の細さと、総毛量がやや多いことを両立する。

---

## 4. Gravity / physical behavior

長い髪ほど総重量の影響が大きいため、YURAのスーパーロングでは次を標準物理挙動とします。

- 長さの自重で上部は落ち着きやすい。
- 短い髪のように全体が軽く大きく跳ねない。
- 毛先を過度に外へ飛び散らせない。
- 肩、背中、腰、腕、衣装、家具との接触を無視して浮遊させない。
- 姿勢と重力方向に従い、接触面に沿って垂れる・乗る・流れる。
- 接触で局所的な流れは変わっても、根元から毛先までの連続性を失わない。
- 一枚板のような硬い塊にはせず、細く柔らかな束分離を残す。

---

## 5. Bangs

- 前髪は重すぎない薄めのロングバング。
- 中央付近から自然に左右へ流す。
- 長さは目元にわずかにかかる程度。
- 額を完全に隠すほど厚くしない。
- 強いぱっつん感は避ける。
- 前髪だけが独立せず、顔まわりのレイヤーへ自然につなぐ。

---

## 6. Face-framing layers

- 左右に頬へ沿う長めのサイドバングを残す。
- フェイスラインを柔らかく包む配置。
- 前髪・サイドバング・後ろ髪は柔らかなレイヤーでつなぐ。
- 顔を隠しすぎない。
- まとめ髪でも、この指定された前髪・顔まわりは原則維持する。

---

## 7. Back hair / neutral down style

基本形は髪を下ろした状態です。

通常の下ろし髪の具体的な見え方・Iライン寄りシルエット・正面 / 背面の主毛量分布・毛先処理は:

`docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`

を併用します。

- 主な毛先はウエストライン付近〜わずかに下まで。
- 最長の細い毛先は腰の上部〜上臀部手前まで許容。
- 全体にごく緩やかな自然な波感。
- 毛先は切り揃えすぎず、繊細な束として自然にほどける。
- 過度に重い一枚板や、横へ広がる巨大シルエットにしない。

### 7.1 Back-view continuity — protected

背面・後ろ向きでは、**長い後ろ髪の大部分を背中側へ自然に垂らす**。

- 後ろ髪は肩の後ろ〜背中中央へ自然に落ちる。
- 背面だからという理由で後ろ髪を胸側へ回し込まない。
- 背中や衣服を見せるためだけに髪を不自然に前へ退避させない。
- 少量の前髪・サイドバング・顔まわりの毛は前側に存在してよい。
- front / side / back で毛量・長さ・重力方向・根元から毛先までの連続性を保つ。

### 7.2 Back-view mass / occlusion — protected

ニュートラルな直立背面では、主たる毛量の重心を後頭部中央から背中中央へ保ちます。

- 中心量を左右へ大きく割って背中中央を見せる構図にしない。
- ウエスト周辺は髪で大きく覆われてよい。
- 最長の繊細な毛先が上臀部手前へ達することは許容する。
- ただし主要毛量を臀部中央や太ももまで延長しない。
- BODYを見せる目的だけで後ろ髪を胸側へ逃がしたり、左右へ不自然に開いたりしない。
- 身体確認が必要なら髪型そのものを変形せず、検証専用条件として明示的に分離する。

---

## 8. Hair arrangements

ポニーテール、ローシニヨン、ハーフアップ、団子、編み込み等の構造は:

`docs/assistant-context/creation/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`

を正本として併用します。

アレンジをしても、本書の以下は変わりません。

- 銀白色
- 元のスーパーロング長
- 総毛量
- 細く柔らかな髪質
- 前髪 / 顔まわり
- 重力挙動

特に **まとめ髪だからという理由で、元の長さや総毛量を消失させてはならない**。

Production priority update: Normal Super-Longの視覚基準は確立済み。2026-09-19に **Strong Braided Half-Up** の正式テキスト仕様化とvisual-master候補制作を明示的に再開した。専用正本は `docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/SPEC.md`。Strong Braided Half-Upのvisual MASTERは未採用 / 制作中。Low Chignon / Mid Ponytail / Low Ponytailのvisual-master productionは引き続きOctober 2026以降を予定する。

---

## 9. Avoid by default

- 極端な姫カット
- 強いぱっつん前髪
- 重すぎる前髪
- 過度に特徴的な外ハネ・内巻き
- コテ感の強い大きな巻き髪
- 過度な頭頂・側頭部ボリューム
- 幼く見えやすい強いツインテール
- 派手すぎる装飾
- 特定キャラクターを想起させるほど記号性の強い特殊シルエット
- 背面で後ろ髪の大部分を不自然に前へ回すこと
- BODYや衣装を見せるためだけに後ろ髪を左右へ大きく割ること
- 細い髪質を少毛として生成すること
- 主要毛量を臀部中央〜太ももまで延ばすこと
- まとめ髪で総毛量を理由なく減らすこと

---

## 10. Generation priority

髪型生成で条件が競合した場合は、次を優先します。

1. 銀白色 + 正式スーパーロング長
2. 標準よりやや多めの総毛量 + 細く柔らかな髪質
3. 長さの自重 / 重力挙動
4. 薄めのロングバング
5. 頬に沿う長めのサイドバング
6. 中間部の十分な密度 + restrained lateral spread
7. 軽く繊細に収束する毛先
8. 背面中央に主たる毛量を残す連続性
9. 上品・柔らかい・大人っぽい全体印象
10. 派生アレンジ / 装飾

通常の下ろし髪では、上記に加えて `docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md` のfront / back distributionとI-line silhouetteを適用する。

---

## 11. Prompt baseline

画像生成時は、少なくとも次の意味内容を含めます。

`銀白色のスーパーロングヘア。主な毛先は自然なウエストライン付近〜わずかに下まで届き、最長の細い毛先のみ腰の上部〜上臀部手前まで許容する。主要毛量を臀部中央や太ももまで伸ばさない。一本一本は細く柔らかいが、総毛量は標準よりやや多め。長さの自重で頭頂〜上部は自然に落ち着き、中間〜背中には十分な密度を残す。横方向にはあまり広がらず、重力に従って背中側へ縦方向に自然に落ちる。毛先へ向かって徐々に量が抜け、軽く繊細に収束する。細い髪質を少ない毛量として解釈しない。前髪は薄めのロングバングで中央付近から自然に左右へ流し、頬に沿う長めのサイドバングと柔らかなレイヤーを残す。身体・衣服・家具との接触を無視して浮遊させない。まとめ髪の場合も元の総毛量と長さを勝手に減らさない。`

通常の下ろし髪では、さらに `docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md` のPrompt baseline / anti-drift guardを適用する。

---

## 12. Relationship to other authorities

- whole-character appearance cross-check → `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md` + `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png`
- BODY → `docs/assistant-context/creation/yura/identity/body/BODY_MASTER.md` + `docs/assistant-context/creation/yura/identity/body/BODY_SPEC.md`
- FACE → `docs/assistant-context/creation/yura/identity/face/FACE_SPEC.md`
- EYE SIGNATURE → `docs/assistant-context/creation/yura/identity/eyes/EYE_SIGNATURE_SPEC.md`
- HAIR core → **this file**
- normal down-style / Normal Super-Long implementation → `docs/assistant-context/creation/yura/identity/hair/styles/NORMAL_SUPER_LONG_SPEC.md`
- Normal Super-Long validation conditions → `docs/assistant-context/creation/yura/qa/templates/NORMAL_SUPER_LONG_VALIDATION_TEMPLATE.md`
- hair arrangements → `docs/assistant-context/creation/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`
- Strong Braided Half-Up specialized implementation → `docs/assistant-context/creation/yura/identity/hair/styles/strong-braided-half-up/SPEC.md`
- RENDERING → `docs/assistant-context/creation/yura/identity/rendering/RENDERING_STYLE_SPEC.md`
- practical integrated generation → `docs/assistant-context/creation/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`
- OUTFIT → `docs/assistant-context/creation/yura/generation/outfit/OUTFIT_GENERATION_GUIDELINE.md`

If the current visual MASTER artifact visually differs from this more precise HAIR specification, **this file controls the HAIR domain** until a later explicitly approved MASTER replacement is adopted.

If a normal-down visual candidate differs from this file, do not redefine HAIR v1.3 to fit the candidate; reject or retry the failed HAIR criterion instead.

---

## 13. Provenance principle

YURAの髪型は、この文章仕様とYURA自身の承認済み生成物を基準に生成します。

特定の既存作品・既存キャラクターの髪型をトレースしたり、その固有シルエットを生成元として扱いません。
参考画像を用いる場合も、一般的な構造原理の確認に限定します。

---

## 14. Change control

本書は保護対象です。

次の変更はユーザーの明示承認なしに行いません。

- 銀白色
- スーパーロングという基本長カテゴリ
- 主な毛先 = ウエストライン付近〜わずかに下
- 最長の細い毛先 = 腰の上部〜上臀部手前まで
- 主要毛量を臀部中央 / 太ももまで伸ばさない上限
- 標準よりやや多めの総毛量
- 細く柔らかな髪質
- 8つの毛量 / 物理条件
- 薄めのロングバング
- 長めのサイドバング
- 背面中央へ主たる毛量を残す連続性
- 上品・柔らかい・大人っぽい基本印象

Normal Super-Longの具体的なシルエット / front-back distributionだけを調整する場合でも、親である本書のcore値に矛盾する変更は行わない。
