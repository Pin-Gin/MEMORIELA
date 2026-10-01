# MEMORIELA Character Rendering Style

Status: **CANONICAL / MANDATORY / PROJECT-WIDE**

Style name: **Matte Natural Anime / マット・ナチュラルアニメ**

Purpose: MEMORIELA のキャラクター画像生成で共通適用する標準レンダリングスタイルを定義する。

---

## 1. Mandatory application

MEMORIELA でキャラクター画像を生成する場合、特別な明示指示がない限り本スタイルを**必ず適用する**。

対象:
- Visual Master 候補
- 立ち絵
- 私服
- 制服
- 日常シーン
- 室内 / 屋外シーン
- 表情差分
- 髪型差分
- SNS 用画像
- 3D 再構築用の 2D 参照画像
- その他のキャラクター派生画像

キャラクター固有の BODY / FACE / EYES / HAIR / GLASSES / outfit / pose 等は各キャラクター Visual Authority が支配し、本書は**描画タッチ・表面質感・陰影・実在感の程度**を支配する。

---

## 2. Core definition

**高品質2Dアニメイラストを基礎に、光沢を抑えたマットな表面感と、わずかに自然寄りの立体・陰影・毛束表現を加える。**

アニメキャラクターとしての顔立ち、目、輪郭、プロポーション、線画、造形は維持する。

**「少しリアル」＝写実化ではない。**

狙いは写真・半実写・3DCGへ寄せることではなく、**アニメ表現の中で自然さを一段だけ増やすこと**。

---

## 3. Matte surface — FIXED

- 光沢は控えめ。
- 肌、髪、衣服をテカテカさせない。
- 強い鏡面ハイライトを常用しない。
- プラスチック、ビニール、濡れたような表面感にしない。
- 塗りはしっとり落ち着いた印象。
- 全体の表面感は柔らかい。
- コントラストは低〜中程度。
- ハイライトは形状説明に必要な範囲に抑える。
- 肌の発光感、過剰な艶、油膜状の反射を避ける。

---

## 4. Slight natural realism — FIXED

### 4.1 Skin / body

- 肌や身体の立体は、完全な平面アニメ塗りより自然寄り。
- 肩、胸郭、腕、腰、骨盤、太腿、膝、ふくらはぎ等のボリュームを自然な光と影で表現する。
- BODY geometry は各キャラクターの正本を優先し、陰影によって体型を変更しない。
- 筋肉や骨格を写実的に強調しすぎない。
- 毛穴、産毛、血管、肌荒れ等の写真級マイクロテクスチャは描かない。

### 4.2 Face

- アニメ的な顔立ちを維持する。
- 鼻、頬、顎、首周りにごく軽い自然な立体感を加える。
- 目の造形・比率はアニメ基準のまま。
- 実写顔、半実写顔、ファッション広告的な写実顔へ寄せない。

### 4.3 Hair

- アニメ的な大きな毛束構成を維持する。
- 毛束の重なり、厚み、重力方向、自然な毛流れをやや現実寄りにする。
- 細い毛のアクセントは使用してよいが、一本一本をフォトリアルに描き込まない。
- 過剰な艶リング、ガラス状ハイライト、金属的な光沢を避ける。

---

## 5. Shading — FIXED

- セル塗り一辺倒にはしない。
- soft cel / grouped shading を基礎とする。
- 影の境界を部分的に柔らかくし、自然なグラデーションを適度に混ぜる。
- 光源方向と立体に整合した陰影を使う。
- 強いHDR感、映画的な過剰コントラスト、極端なリムライトを標準にはしない。
- シーン照明が暖色・寒色でも、キャラクター固有色を失わせない。

---

## 6. Line / color treatment — FIXED

- 繊細でクリーンな2D線画。
- 線を硬く黒々としすぎない。
- 線画が消えるほどペインタリーにしない。
- 彩度は必要以上に上げない。
- キャラクター固有の髪色・瞳色・肌色を維持。
- 全体は落ち着きのある、柔らかい色調。

---

## 7. Explicit prohibitions

以下は標準スタイルからの逸脱とする。

- photorealism
- semi-photoreal portrait rendering
- live-action look
- PBR material rendering
- realistic 3DCG / game-engine look
- plastic / waxy skin
- glossy / wet-looking skin
- excessive specular highlights
- pore-level skin detail
- photographic hair strand rendering
- metallic-looking hair
- heavy HDR
- excessively hard cel shadows
- overly flat no-volume cel rendering

---

## 8. Short invocation block

画像生成時に短く指定する場合:

`マット・ナチュラルアニメ。高品質2Dアニメを基礎に、光沢を抑えたしっとり柔らかなマット質感。肌とBODYは自然寄りの立体感、髪はアニメ的な大きな毛束を維持しつつ重なり・厚み・毛流れをやや現実寄りにする。soft cel を基礎に柔らかな自然陰影を適度に混ぜる。少しリアルだが写実化しない。半実写、PBR、3DCG、プラスチック肌、過剰な艶、写真級マイクロテクスチャは禁止。`

---

## 9. Authority rule

Project-wide character image generation order:

1. character canon
2. character Visual Master / Visual Text
3. **this Rendering Style**
4. user-requested outfit / pose / hairstyle / expression / background / scene

本書はキャラクター固有のIdentityを上書きしない。
ただし描画タッチに関しては本書を MEMORIELA 共通の正本とする。

ユーザーが明示的に別のタッチを依頼した場合のみ、その単発生成では style derivative を許容する。
その派生画像が新しい標準スタイルになることはない。
