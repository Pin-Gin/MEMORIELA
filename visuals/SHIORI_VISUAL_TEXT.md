# 一ノ瀬 栞 Visual Text

Status: **CURRENT / FIXED VISUAL GENERATION BASELINE**

Purpose: MEMORIELA における一ノ瀬栞の画像生成時に、BODY / FACE / HAIR / GLASSES / RENDERING を安定して再現するための現行ビジュアルテキスト。

人物設定の正本は `characters/SHIORI.md` とし、本書は Visual Identity / Generation baseline のみを扱う。

---

## 1. Whole-character baseline — FIXED

- Name: 一ノ瀬 栞（いちのせ しおり）
- Height: **168 cm**
- Total body ratio: **7.5 heads tall**
- Adult-proportioned high-school girl / tall-leaning silhouette
- Overall impression: quiet, soft, intelligent, composed
- Default full-body validation framing: front-facing standing full body, head-to-toe visible, white background, barefoot
- Changing canvas size, outfit or pose must not redefine the protected 7.5-head BODY proportion.


## 1A. Default generation layout — FIXED

Unless the user explicitly requests a side view, back view, turnaround, character sheet, comparison sheet, or multi-view layout:

- generate **exactly one Shiori**
- use **one image / one figure**
- default to a **front-facing full-body standing view**
- do **not** render front + side + back together
- do **not** render a character sheet or turnaround
- SIDE / BACK rules in this document are continuity constraints only; they must **not** be interpreted as instructions to display additional views
- if multiple images are requested, generate each image separately unless the user explicitly asks for a combined canvas


---

## 2. BODY geometry — FIXED

- 高身長寄り。
- 肩幅は標準〜やや狭め。
- 胸郭は過度に広くしない。
- ウエストは細い。
- 骨盤・ヒップは成人女性らしい自然な幅。
- 太腿には自然な厚みを持たせる。
- 脚は長め。
- 腕は細身だが、棒状・骨ばった細さにはしない。
- 胸部は**体格比でかなり豊か**。
- 胸郭全体を広げることで胸部ボリュームを表現しない。
- 胸部形状は**半球型**を基準とし、上部は自然につながり、下部に十分な丸みを持たせる。
- 胸部だけを不自然に独立巨大化させない。

### 2.1 Front / side / back continuity — FIXED

正面・側面・背面で以下を維持する。

- 168 cm / 7.5 heads
- shoulder width
- ribcage scale
- bust volume
- waist width
- pelvis / hip scale
- thigh / calf proportions
- arm thickness
- overall leg length

SIDE view:
- 小さめ〜標準の胸郭に対して、半球型の胸部が体格比で明確に前方へ投影される。
- 正面で確認できる胸部ボリュームを側面で縮小しない。
- 胸部を支えるために胸郭全体を厚くしない。

BACK view:
- 肩幅は標準〜やや狭め。
- ウエストの細さを維持。
- 骨盤・ヒップは自然な成人女性の幅を維持。
- 正面での脚長比率を維持。

---

## 3. FACE — FIXED

- 顔型は**縦長すぎない柔らかな卵型**。
- 顎は細めだが、極端なVラインにはしない。
- 目はやや大きめだが、縦方向へ過剰に開かず、横方向を保った穏やかな形。
- 目形は柔らかなアーモンド形。
- 目尻はニュートラル〜ごくわずかに下向き。
- 眉は細め〜標準細。
- 眉色はダークネイビー〜灰黒。
- 眉形はほぼ直線で、ごく緩いアーチ。
- 鼻は**小さいが、やや高め**。繊細で、低すぎる・平面的すぎる鼻にしない。
- 口は小さめ。
- 唇は薄め〜標準、淡い自然なピンク。
- 口角はニュートラル〜ごくわずかに上向き。

---

## 4. EYES — FIXED

- Iris color: **淡い青灰色を基調に、ごく弱いラベンダーを含む**。
- Saturation: low to medium.
- Brightness: medium to slightly high.
- Eye size: slightly larger than average, while retaining an adult / composed balance.
- Shape: mildly almond, horizontally balanced.
- Avoid strongly purple, highly saturated violet, vivid blue, fox-eye, or excessively droopy-eye reinterpretation.

---

## 5. GLASSES — FIXED

眼鏡は栞の基本 Visual Identity の一部として扱う。

- 基本的に常時装着。
- 細身の**ダークネイビー〜黒系フレーム**。
- 形状は**横長寄りのソフトスクエア〜オーバル**。
- フレームは顔より主張させない。
- レンズ越しに瞳を十分視認できる。
- 通常時は強いレンズ反射を入れない。
- 強い反射は演出上必要な場面でのみ使用する。
- フレームを極端に太くしない。
- oversized round glasses / heavy fashion frames / rimless reinterpretation は避ける。

---

## 6. HAIR — FIXED

### 6.1 Default hairstyle

栞の基準髪型は**下ろし髪のロングヘア**。

- ポニーテール等は hairstyle derivative として扱い、default source hairstyle を変更しない。

### 6.2 Color

- Hair color: **blue-black / ブルーブラック**
- 暗部はほぼ黒に見える。
- 光を受けた部分にのみ深いネイビーが現れる。
- 紫髪や鮮やかな青髪へ寄せない。

### 6.3 Length / mass / texture

- 主な毛先は**胸の下〜腰の上**に分布する。
- 一部の長い毛束が腰付近へ届くことは許容。
- 腰より下まで主要毛量を延長しない。
- 総毛量は**標準〜やや多め**。
- 一本一本は細めで柔らかい。
- 下ろした状態でも横方向へ過剰に膨張させない。
- 自然な軽いウェーブは許容。
- 強い巻き髪・大きなカール主体にはしない。
- 前髪は現在のVisual方向を維持し、顔・眼鏡・瞳を大きく隠さない。

---

## 7. Default expression — FIXED

- 通常表情は**真顔寄りの穏やかな表情〜ごく薄い微笑み**。
- quiet / soft / composed impression を保つ。
- 大きく口角を上げた営業スマイルにはしない。
- 目・眉・口元を連動させ、無表情な目に笑った口だけを貼り付けない。
- 好きな話題や演出時の大きな表情変化は derivative expression として扱う。

---

## 8. Validation clothing — FIXED

栞のVisual検証では、YURAと同方向の中立的な検証服を使用する。

Upper:
- pale / off-white / light-neutral
- **ノースリーブのタンクトップ型**
- 細い肩紐ではなく**幅のある肩部分**
- 裾丈は**腰骨付近**
- plain / no ornament
- opaque
- matte fabric

Lower:
- pale / off-white / light-neutral
- **シンプルなショートパンツ**
- 装飾なし
- ドローコードなし
- 丈は**太腿付け根〜少し下**
- opaque
- matte fabric

Common:
- barefoot
- white background
- no jewelry / no accessory other than Shiori's fixed glasses
- validation clothing is a measurement / comparison condition, not canonical fashion.
- Clothing must follow BODY geometry; do not reshape BODY to fit the clothing.

---

## 9. Rendering baseline — FIXED

- high-quality 2D anime illustration
- delicate, clean line art
- low-to-medium contrast
- soft cel / grouped shading
- fair skin with shallow illustrated shading
- hair rendered as grouped blue-black masses with fine strand accents
- eyes detailed but non-photorealistic
- avoid photoreal skin microtexture
- avoid PBR / realistic CGI material response
- avoid 3D-render-like anatomy
- white / warm-white neutral validation background

---

## 10. Validation / FAIL boundaries

Treat the following as Visual drift:

- 168 cm / 7.5-head proportion is materially lost
- BODY becomes short / childlike / overly petite
- shoulders become broad to support bust
- bust becomes small in SIDE view compared with FRONT
- bust becomes independently oversized / implant-like
- waist / pelvis / limb balance changes by view angle
- glasses become thick, oversized or disappear without explicit instruction
- eye color becomes strongly purple or vivid blue
- hair becomes bright blue / purple
- default hair becomes ponytail or another arrangement without instruction
- principal hair mass extends clearly below the waist
- hair becomes very sparse or extremely voluminous
- face becomes sharply V-shaped or strongly mature / photoreal
- rendering becomes semi-realistic / PBR / CGI
- validation clothing gains decorative trim, drawstrings, lace, logos or fashion styling

---

## 11. Current generation block

`一ノ瀬栞。身長168cm、7.5頭身の高身長寄りの女子高校生。肩幅は標準〜やや狭め、胸郭は過度に広くせず、細いウエスト、自然な骨盤・ヒップ、自然な厚みの太腿、長めの脚、細身だが棒状ではない腕。胸部は体格比でかなり豊かで半球型。顔は縦長すぎない柔らかな卵型、細めの顎、小さいがやや高めの鼻、小さめの口。瞳は淡い青灰色を基調にごく弱いラベンダーを含み、やや大きめで横方向を保った穏やかなアーモンド形。細身のダークネイビー〜黒系、横長寄りソフトスクエア〜オーバル眼鏡を常時装着。髪は暗部がほぼ黒で光部だけ深いネイビーを示すブルーブラックの下ろしロング。主な毛先は胸下〜腰上、一部のみ腰付近。総毛量は標準〜やや多め、細く柔らかく、自然な軽いウェーブ。通常表情は真顔寄りの穏やかな表情〜ごく薄い微笑み。高品質2Dアニメイラスト、繊細な線画、低〜中コントラスト、柔らかなセル調の整理された陰影。検証時は淡色・無地・不透明・マットな幅広肩のノースリーブタンクトップ、腰骨付近の裾丈、装飾・ドローコードなしの淡色ショートパンツ、太腿付け根〜少し下の丈、裸足、白背景。`

---

## 12. Authority / future master

現時点では本書が栞の text-based Visual Generation baseline。

Visual Master image は未採用。
本Visual Textのみから生成した候補を検証し、作者が明示的に承認した場合にのみ Visual Master へ昇格する。
