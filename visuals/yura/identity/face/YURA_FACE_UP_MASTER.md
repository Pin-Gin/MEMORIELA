# YURA FACE-UP MASTER

Status: **AUTHOR-APPROVED FACE-UP MASTER / ACTIVE TEXT AUTHORITY / REPOSITORY PROMOTED / VERIFIED**

## Purpose

この文書は、作者が正式PASSとした現在のYURA Face-up画像を、YURAの正式な顔・頭部・目・表情・Face-up時の髪と耳の見え方の基準として固定する。

正式Face-up画像:

`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

Repository-promoted Face-up Master verification:

```text
width     = 1145 px
height    = 1374 px
mode      = RGBA
size      = 1,922,890 bytes
SHA-256   = c71111887ff96ebabd47b6ef9318a41b6fa50b060eafdeabdebf75382dc48e09
Git blob  = 496d7da8a1769808917383598624d3c03fa18163
commit    = 0b8a8a106593688928870ffd1a6340d8034d5818
```

上記PNGは作者PASS済みFace-up Masterとしてrepositoryへ正式昇格済みである。

耳の実Geometryについては、以下の正式Masterを併用する。

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

最上位YURA Visual Text:

`visuals/yura/identity/master/YURA_VISUAL_TEXT.md`

本書は `YURA_VISUAL_TEXT.md` と競合してはならない。競合がある場合は `YURA_VISUAL_TEXT.md` を優先し、平均化・補間・独自解釈を行わない。

---

## 1. Face identity

現在作者PASSとなったFace-up画像に描かれているFace Identityを維持する。

基底は以下とする。

- 愛嬌
- 可愛さ
- 適度な若さ
- 柔らかい2Dアニメ表現

顔を大人びたモデル顔、美人系、成熟方向へ再設計しない。

「高品質化」「自然化」「整える」「美しくする」等を理由に、顔Geometryや各パーツを変更してはならない。

---

## 2. Face contour

現在の正式Face-up画像の顔輪郭を基準とする。

採用Geometry:

- A contour
- A2 cheeks
- B2 jaw / chin

輪郭は柔らかく、縦方向を長く見せない。
顔全体は短めでコンパクトな印象を維持する。

禁止:

- 面長化
- 縦長化
- 細長い卵型化
- 顔幅の過度な縮小
- 頬の削り
- 頬骨の強調
- 下顔面の延長
- 顎の延長
- 尖ったV字顎への変更

```text
NOT LONG FACE.
NOT VERTICALLY ELONGATED FACE.
NOT NARROW ELONGATED OVAL.
NOT LONG MIDFACE.
NOT LONG CHIN.
NOT SHARP V-LINE FACE.
```

---

## 3. Cheeks

現在のFace-up画像の頬の丸みを維持する。

- ややふっくらした自然な丸み
- 柔らかな横方向のボリューム
- 頬骨を目立たせない
- 頬をこけさせない
- 過度な赤ちゃん顔・極端な丸顔にはしない

頬を細くして顔を成熟方向へ寄せてはならない。

---

## 4. Jaw / chin / lower face

現在のFace-up画像の下顔面を固定する。

- 下顔面はコンパクト
- 顎は短め
- 顎先は小さい
- 顎先には自然な丸みを残す
- 頬から顎へなだらかに収束

禁止:

- 顎を下へ伸ばす
- 顎先を鋭くする
- V-line化
- 下顔面を縦長にする
- 口から顎までの距離を増やす

---

## 5. Midface

現在のFace-up画像の中顔面長を維持する。

目から鼻、鼻から口、目から口までの縦方向バランスを変更しない。

禁止:

- 中顔面延長
- 鼻位置を下げる
- 口位置を下げる
- 目位置を上げて中顔面を長く見せる
- 顔を成熟させるための縦方向再配置

---

# 6. Eyes

目はYURA Face Identityの最重要パーツの一つとして扱う。

**現在作者PASSとなった正式Face-up画像に描かれている目の形状そのものを正式基準とする。**

テキストから別の一般的アニメ目へ再解釈してはならない。

---

## 6.1 Eye size

採用サイズ:

**C2**

- 明確に大きめ
- 最大級にはしない
- 縦方向へ過度に拡大しない
- 丸く見開いた目にしない
- 極端なデフォルメ目にしない

現在Face-up画像の目サイズを維持する。

---

## 6.2 Eye placement

目位置は、作者が比較検証で採用したC2基準から、

**0.3% 内側**

へ配置した状態を正式基準とする。

```text
C2 baseline -> 0.3% inward
```

この0.3%は比較テスト時の選定基準に対する相対値である。
別の測定系へ勝手に換算しない。

禁止:

- 0.3%を別の絶対ピクセル値へ勝手に変換する
- 目間隔を広げる
- 左右の目を外側へ移動する
- 「自然な顔バランス」などを理由に位置を再調整する

**The selected 0.3% inward placement must be preserved.**

---

## 6.3 Eye shape — CURRENT APPROVED IMAGE SHAPE IS AUTHORITATIVE

目の形は、**現在作者PASSとなったFace-up画像に描かれている形状そのもの**を正式仕様とする。

新しい目形状を生成側で考案してはならない。

現在の形状の特徴:

- 柔らかなアーモンド形を基底とする
- アニメ的な丸みを適度に含む
- 横方向の幅をしっかり保つ
- 縦方向の開きは控えめ
- 丸く見開いた円形目ではない
- 強いつり目ではない
- 強いたれ目ではない
- 目尻を過度に上げない
- 目尻を過度に下げない
- 上まぶたはなだらかな連続曲線
- 上まぶた中央付近には自然な厚みがある
- 下まぶたは強く丸めず、浅く柔らかなカーブ
- 目頭・目尻とも鋭角化しない
- 横幅に対して縦幅を大きくしすぎない

**The existing approved Face-up image eye contour must be preserved as-is.**

禁止:

- 目を丸くする
- 目を縦長にする
- 目を細くする
- 目尻角度を変更する
- つり目化
- たれ目化
- almond shape を別形状へ再設計する
- 「かわいくする」ために縦幅を増やす
- 「美人化」するために切れ長へ変更する
- 左右の目形状を生成都合で作り直す

**目形状について、正式Face-up画像が最も具体的なGeometry Sourceである。**

テキストは画像形状を説明するためのものであり、画像形状を変更する許可ではない。

---

## 6.4 Upper eyelid

現在画像の上まぶた形状を維持する。

- 滑らか
- 柔らかい
- 過度な角度を付けない
- 目尻を跳ね上げない
- 強いアイライン形状へ変更しない

まつげと上まぶたを一体化して、目形状そのものを変形させてはならない。

---

## 6.5 Lower eyelid

下まぶたは現在画像の浅いカーブを維持する。

- 強い円弧にしない
- 下側へ膨らませない
- 目を縦方向へ大きく見せない
- 写実的な涙袋表現を追加しない

---

## 6.6 Double eyelid

二重あり。

- 繊細
- 薄い
- 2Dアニメ表現へ自然に馴染ませる
- 強い写実的な二重線にしない
- 二重線によって目形状を変更しない

---

## 6.7 Eyelashes

現在画像のまつげ量・方向・柔らかさを基準とする。

- 黒寄りの濃いグレー
- 純黒の強いインク線にしない
- 輪郭をわずかに柔らかくする
- 存在は明確
- 濃密にしない
- 華美にしない
- メイク的にしない
- 長く盛らない
- 目尻を強調しすぎない

まつげを増やして目の外形を変更してはならない。

---

## 6.8 Iris color

瞳色:

**gray-blue**

優先:

```text
gray > blue
```

- グレー感を強めにする
- 彩度は控えめ
- 鮮やかな青にしない
- 宝石色へ寄せない

---

## 6.9 Iris structure

虹彩:

**柔らかい上下グラデーション + ごく薄い放射状模様**

- 上部をわずかに暗くする
- 下部をわずかに明るくする
- 滑らかに接続
- 放射状模様は非常に薄い
- グラデーションより目立たせない

禁止:

- 密なスポーク
- 写実的な虹彩繊維
- 星
- 花
- 幾何学模様
- 高密度宝石テクスチャ
- 過剰な虹彩情報

---

## 6.10 Pupil

瞳孔:

**小さめ真円・輪郭ややぼかし**

- 真円
- 小さめ
- 輪郭は少し柔らかい
- 純黒で強く抜かない
- グレーブルーの虹彩へ自然に馴染ませる
- 左右の瞳孔は対称性を維持する
- 左右で、瞳孔の大きさ・真円形状・暗さ・輪郭のぼかし強度を同等にする
- 片側だけ瞳孔を薄く、弱く、小さく、または強くぼかさない
- 光やハイライトの影響で、片側の瞳孔の存在感だけが弱く見える状態も避ける

```text
PUPILS MUST BE BILATERALLY SYMMETRIC IN SIZE, SHAPE, DARKNESS, AND EDGE SOFTNESS.
DO NOT WEAKEN ONE PUPIL RELATIVE TO THE OTHER.
```

瞳孔を縦長・楕円・装飾形状へ変更しない。

---

## 6.11 Eye highlights

正式構成:

**中サイズ主光1 + 小さい副光1**

- 主光 1個
- 副光 1個
- 丸みのある単純形状
- 柔らかい
- 細かな光点を増やさない

現在Face-up画像のハイライト位置・バランスを尊重する。

---

# 7. Eyebrows

現在Face-up画像の眉形状を維持する。

- 細め
- 柔らかい
- 自然な横方向
- ニュートラル

禁止:

- 困り眉
- 眉頭を上げる
- 内側を持ち上げる
- 悲しげな眉
- 儚げな眉
- 強いアーチ眉
- 美人系の細長い眉

---

# 8. Nose

現在Face-up画像の鼻を維持する。

- 小さい
- 控えめ
- 2Dアニメ表現
- 鼻筋を強調しない
- 鼻梁を立体化しない
- 写実的な鼻へ変更しない
- 鼻を長くしない

---

# 9. Mouth

現在Face-up画像の口を正式基準とする。

- 小さい
- 閉じた口
- 真顔
- ニュートラル
- 控えめな線

禁止:

- 開口
- 微笑み
- 悲しい口角
- 困り口
- 口角を勝手に上げる
- 口角を勝手に下げる
- 唇を厚くする

---

# 10. Expression

正式基準表情:

**真顔 / TRUE NEUTRAL**

表情差分は作者の明示指示がある場合のみ許可する。

禁止:

- smile
- sad
- worried
- wistful
- melancholic
- fragile
- vulnerable-looking
- 儚い
- 物憂げ
- 悲しげ
- 困った表情

**Do not infer emotion from the neutral face.**

生成側が独自に感情を付加することを禁止する。

---

# 11. Upper cranium / head shape

Ear Geometry Masterで作者承認された、**頭蓋上部をわずかにコンパクト化した形状**を正式基準とする。

髪のボリュームやFace-up構図を理由に、頭頂部を縦方向へ膨張・延長しない。

顔Geometry、額高、中顔面、下顔面、顎を変更して頭蓋形状を調整しない。

頭蓋上部のコンパクトさは、顔を縮小・縦伸ばしすることで作らない。

**Do not increase upper-cranium height to accommodate hair volume.**

補助Hard Rule:

```text
VISIBLE HAIR VOLUME != SKULL HEIGHT
HAIR VOLUME MUST NOT REDEFINE HEAD GEOMETRY
DO NOT LENGTHEN THE FACE TO BALANCE HAIR VOLUME
```

現在のFace-up画像で髪の外形が大きく見える場合でも、それを実頭蓋高として解釈してはならない。

頭蓋上部Geometryについては、作者承認済みEar Geometry Masterのコンパクト化結果を優先する。

---

# 12. Ears

耳の実Geometryは、

`visuals/yura/identity/ears/YURA_EAR_GEOMETRY_MASTER.png`

を正式基準とする。

耳の可視性と耳Geometryを分離する。

耳は:

- 小さめ
- 縦方向にコンパクト
- 頭部側面に近い
- 外へ張り出さない
- カメラ方向へ回転させない

耳を見せる必要はない。

許可:

- 一部のみ見える
- ごく小さく見える
- 左右非対称に見える
- 髪で完全に隠れる

禁止:

- 耳を見せるために縦へ伸ばす
- 耳を大きくする
- 耳を外へ出す
- 耳をカメラ側へ傾ける
- 耳を正面向きにする
- 髪を避ける
- 顔まわり毛束を耳の後ろへ移動する
- 左右の耳を同程度見せようとする

```text
EAR VISIBILITY SHORTAGE IS NOT A FAILURE.
NO VISIBILITY COMPENSATION.
```

---

# 13. Hair — Face-up relationship

髪はYURA Visual Textに従う。

- 銀白色
- ストレート主体
- SUPER-LONG
- 胸下を越える
- 全身時は腰付近
- 腰より大きく下へ伸ばさない
- 薄い前髪
- 額が少し透ける
- 細い自然な顔まわり毛束
- 髪飾りなし

Face-upでは髪全長が画面外へ続いてよい。

禁止:

- 肩丈化
- ボブ化
- ミディアム化
- 強いウェーブ
- 巻き髪
- 三つ編み
- 編み込み
- 耳を見せるための髪避け

---

# 14. Skin

- 標準より白寄り
- 明るい色白
- 病的な白にはしない
- ごく薄い自然な血色
- マット感強め
- アニメ調強め
- 毛穴なし
- 写実肌なし
- 油脂感なし
- 濡れ感なし
- プラスチック光沢なし

---

# 15. Face-up framing

正式Face-up基準:

- exactly one YURA
- 1人1枚
- 正面
- 直立
- 頭を傾けない
- 肩から上
- 頭部全体を収める
- 頭頂を切らない
- 中央配置
- 真顔
- 閉じた口
- 正方形キャンバス基準

Face-up画像のキャンバス占有率から、全身時の頭身や身体サイズを推定してはならない。

---

# 16. No interpretation rule

本Masterに記述されていない外見要素を、生成モデルが独自解釈で追加・変更してはならない。

特に以下を禁止する。

- 顔Geometryの最適化
- 目形状の再設計
- 表情の付加
- 頭蓋高の増加
- 耳可視性補正
- 髪型の装飾
- 成熟化
- 美人化
- 感情表現の追加

生成時に曖昧な部分がある場合、新しい造形を補完するよりも、正式Face-up画像と本Masterを維持することを優先する。

```text
DO NOT IMPROVISE YURA'S FACE.
DO NOT REINTERPRET APPROVED GEOMETRY.
PRESERVE THE AUTHOR-APPROVED FACE-UP IMAGE.
```

---

## Promotion state

Author approval for this Face-up design is complete.

Repository binary promotion is also complete and verified.

Canonical repository asset:

`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

```text
SHA-256 = c71111887ff96ebabd47b6ef9318a41b6fa50b060eafdeabdebf75382dc48e09
size    = 1,922,890 bytes
Git blob = 496d7da8a1769808917383598624d3c03fa18163
commit   = 0b8a8a106593688928870ffd1a6340d8034d5818
```

This Face-up image is the repository-promoted canonical Face Reference.
