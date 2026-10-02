# MEMORIELA Character Rendering Style

Status: **CANONICAL / MANDATORY / PROJECT-WIDE**

Style name: **Matte Natural Anime / マット・ナチュラルアニメ**

Purpose:
MEMORIELAに登場するすべてのキャラクター画像で、
共通の描画タッチ・陰影・表面質感・コントラスト・写実度を維持する。

本書はキャラクター固有のBODY / FACE / EYE / HAIR / SKIN / GLASSES /
outfit / pose等を定義しない。

キャラクター固有差は各キャラクターのVisual Authorityが支配し、
本書は**全キャラクター共通のレンダリング品質と質感**を支配する。

---

## 0. HARD EXECUTION LOCK — 2D ANIME FIRST

This section is **execution-critical**.

The phrase **Matte Natural Anime** MUST be interpreted in this order:

1. **2D ANIME ILLUSTRATION**
2. **ANIME CHARACTER DESIGN / ANIME FACIAL GRAMMAR**
3. **SOFT CEL / GROUPED ILLUSTRATION SHADING**
4. **MATTE / LOW-GLOSS SURFACE QUALITY**
5. only then, a slight increase in natural dimensionality

**"Matte" describes surface gloss. It does NOT permit photorealism, semi-photorealism, live-action appearance, realistic portrait rendering, CGI, game-engine rendering, or PBR.**

Required execution reading:
`HIGH-QUALITY 2D ANIME ILLUSTRATION ONLY.`

Required exclusions:
- NOT photoreal
- NOT semi-photoreal
- NOT live-action
- NOT realistic portrait
- NOT CGI
- NOT 3D render
- NOT game-engine render
- NOT PBR
- NOT photographic skin
- NOT photographic hair

If an output reads primarily as a real person / semi-real portrait / CGI character instead of a 2D anime illustration:
`RENDERING HARD FAIL`

A rendering hard fail cannot be accepted because gloss is low or "matte".

---

## 1. Core definition

**高品質2Dアニメイラストを基礎に、
光沢を抑えたマットな表面感と、
わずかに自然寄りの立体・陰影・毛束表現を加える。**

- アニメキャラクターとしての造形を維持する。
- 写実化・半実写化しない。
- 完全なフラットセル塗りにも寄せすぎない。
- 強い光沢ではなく、柔らかな明暗差で立体を表現する。
- **全体をしっとり柔らかく見せる。**
- キャラクターごとに描画タッチを変えない。

**「少しリアル」＝写実化ではない。**

アニメ表現の中で、
立体・光・毛束・布の自然さを一段だけ増やす。

---

## 2. Line — FIXED

- 線画は細く繊細。
- クリーンな2Dアニメ線を維持する。
- 黒く重いアウトラインにしない。
- 顔・髪・BODY・衣服で線の強さを急変させない。
- 線画を消すほどペインタリーにしない。
- 線だけで立体を作らず、塗りと陰影も併用する。
- キャラクターごとに線密度・線幅・線の主張を変えない。

---

## 3. Shading — FIXED

- **soft cel / grouped shading** を基礎とする。
- 弱い拡散グラデーションを適度に混ぜる。
- 影境界は硬くしすぎず、自然に柔らかくつなぐ。
- 完全なフラットセル塗りにはしない。
- 強い立体陰影・深すぎる影・劇的な陰影を標準にしない。
- BODYや顔の立体感は、穏やかな明暗差で表現する。
- 光と影によってキャラクター固有のBODY geometryを変更しない。
- キャラクターごとに陰影ロジックを変えない。

---

## 4. Contrast / brightness — FIXED

- 全体コントラストは **低〜中程度**。
- 極端な黒つぶれを作らない。
- 明部を過度に持ち上げて白飛びさせない。
- 明るい背景でもキャラクターの輪郭と立体が自然に読める状態を維持する。
- 生成ごとに極端に淡く／濃くならない。
- キャラクターごとにコントラスト帯を変えない。
- 全体の空気感は落ち着いて柔らかく保つ。

---

## 5. Surface quality — FIXED

全体の表面感は **マット寄り** とする。

- 肌・髪・衣服をテカテカさせない。
- 強い鏡面反射を標準にしない。
- プラスチック・ビニール・ワックス・濡れたような表面にしない。
- 立体感は光沢ではなく、明暗差・厚み・重なりで表現する。
- ハイライトは形状説明に必要な範囲に抑える。
- ハイライトは細く鋭いものより、広く弱いものを優先する。
- **全体をしっとり柔らかく見せる。**

---

## 6. Skin rendering — FIXED

肌色そのものは各キャラクターの `SKIN_SPEC` を正とする。

共通レンダリングとして:

- 肌表面はなめらかで、さらっとしたマット寄り。
- 自然な立体感は柔らかな光と影で表現する。
- 強い艶・濡れ感・油膜感・ワックス感を出さない。
- 肌を発光体のように見せない。
- 毛穴・産毛・血管・肌荒れ等の写真級マイクロテクスチャを描かない。
- 写実的な皮膚質感へ寄せない。
- 顔・腕・脚など部位によって質感を大きく変えない。

---

## 7. Hair rendering — FIXED

- アニメ的な大きな毛束構造を優先する。
- 毛束の重なり・厚み・明暗差・毛流れで質感を表現する。
- 細い毛のアクセントは補助的に使用する。
- 一本一本をフォトリアルに描き込まない。
- 強い艶リングを標準にしない。
- 細く鋭いガラス状ハイライトを多用しない。
- 金属的な光沢にしない。
- ハイライトは広く弱く、毛束の面に沿って柔らかく表現する。
- キャラクター差は髪色・毛量・髪型で表現し、
  レンダリング差では表現しない。

---

## 8. Clothing rendering — FIXED

- 基本の布質感はマット寄り。
- 布の厚み・皺・重なりは自然に表現する。
- サテン・シルク・ビニール・ラバーのような強い反射を
  指定なしで付与しない。
- 衣服の立体感は自然な皺と陰影で表現する。
- 過剰な皺密度で情報量を増やしすぎない。
- BODY geometryを衣服の陰影で変更して見せない。
- キャラクターごとに衣服のレンダリング品質を変えない。

※ 衣装設定として明示的に光沢素材が指定された場合は、
素材固有の反射を許容するが、
作品全体の描画タッチから逸脱しない。

---

## 9. Lighting behavior — FIXED

ライティングの色・方向・強さはシーンによって変化してよい。

ただしライティングは:

- キャラクター固有色を別の色へ再定義しない。
- 表面質感を別のレンダリングスタイルへ変えない。
- 強いHDR感を標準にしない。
- 極端なリムライトを標準にしない。
- ハイライトを過剰に増やさない。
- シーンが変わっても Matte Natural Anime の質感を維持する。

光源条件が変わっても、
**全体をしっとり柔らかく見せる基本質感は維持する。**

---

## 10. Slight natural realism — boundary

許容する自然さ:

- 肩・胸郭・腕・腰・骨盤・脚などの柔らかな立体感
- 顔の頬・鼻・顎・首周りの軽い自然な陰影
- 毛束の厚み・重なり・重力方向
- 布の自然な皺・厚み
- 柔らかな光の回り込み

許容しない方向:

- photorealism
- semi-photoreal portrait rendering
- live-action look
- realistic CGI
- PBR material rendering
- game-engine rendering
- photographic skin
- photographic hair
- realistic pore / lip texture

---

## 11. Multi-character consistency — MANDATORY

MEMORIELAの複数キャラクターを同一画面に配置した場合、
以下のレンダリング特性をキャラクターごとに変えてはならない。

- 線画の細さ・密度・主張
- soft cel の基本強度
- 拡散陰影の柔らかさ
- コントラスト帯
- ハイライト強度
- 表面のマット感
- 描画密度
- 写実度
- 光沢の基本強度

キャラクター差は以下で表現する:

- FACE
- BODY
- EYE
- HAIR
- SKIN color
- GLASSES
- outfit
- expression
- pose

**Rendering Styleそのものをキャラクター差として使用しない。**

---

## 12. Rendering stability lock — MANDATORY

BODY / FACE / EYE / HAIR / SKIN / outfit / pose / expression /
scene等を変更・修正しても、
共通Rendering Styleを再解釈しない。

局所修正時も以下を維持する:

- line delicacy
- shading softness
- contrast range
- highlight strength
- matte surface impression
- rendering density
- realism level

一つの領域を修正するために、
画像全体の描画タッチを変更しない。

---

## 13. Explicit prohibitions

標準状態では以下を禁止する。

- glossy / wet-looking skin
- plastic / waxy skin
- excessive specular highlights
- metallic-looking hair
- glass-like hair highlights
- photographic hair strand field
- pore-level skin detail
- heavy HDR
- excessively hard cel shadows
- overly flat no-volume cel rendering
- character-specific rendering-style drift
- generation-to-generation rendering-style drift

---

## 14. Authority rule

Project-wide character rendering order:

1. character Visual Master / Visual Authority
2. character-specific Identity Specs
3. requested pose / outfit / expression / scene
4. **this CHARACTER_RENDERING_STYLE**
5. scene lighting adaptation

本書はキャラクター固有Identityを上書きしない。

ただし、
**線・陰影・コントラスト・表面質感・写実度については
本書をMEMORIELA全キャラクター共通の正本とする。**

個別キャラクター側で、
本書と重複するRendering Styleを再定義しない。
