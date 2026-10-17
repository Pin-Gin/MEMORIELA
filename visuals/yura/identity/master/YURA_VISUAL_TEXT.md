# YURA VISUAL TEXT — TEXT-ONLY BOOTSTRAP

Status: **AUTHOR-APPROVED / FACE REDESIGN TEXT UPDATED**

Purpose: YURAをTEXT_ONLYでも再現できるようにするVisual定義。

顔に関しては、2026-10-17に作者が選定したFace Redesign仕様を反映する。
顔の詳細仕様は以下を併用する。

`visuals/yura/identity/specs/YURA_FACE_REDESIGN_SPEC.md`

現行 `visuals/yura/identity/face/YURA_FACE_REFERENCE.png` は、今回採用した新Face画像へまだ置換されていない。
そのため、新Face Redesign作業では旧Face Referenceの顔Geometryを混入させない。
新しいFace Reference画像が作者承認のうえ正式に置換されるまでは、本テキストと `YURA_FACE_REDESIGN_SPEC.md` を新Face設計のテキスト基準とする。

## Overall
YURAは、銀白色のスーパーロングヘアを持つ、愛嬌と可愛さを基底にした若々しい少女として描く。
幼すぎる印象にはせず、大人びた美人・モデル顔を主軸にしない。
顔全体は可愛さと若さを優先し、目元など一部のパーツに限って20〜30%程度の整った美人要素を許容する。
高品質な2Dアニメ表現のみを基準とし、写実・半写実・3D・CGI方向へ寄せない。

## Hair
髪色は**銀白色**。
ベージュブロンド、ピンクブロンド、暖色クリーム系へ寄せない。
髪型はストレート主体のスーパーロングを基準とする。
長さは胸下を越え、腰付近まで届く程度とする。
過度に長くせず、腰より大きく下へ伸ばさない。
前髪は薄めで、額をやや透かす。
顔まわりには細い毛束が自然に落ちる。
髪飾りは付けない。

## Face
顔の基底Identityは**愛嬌 + 可愛さ + 適度な若さ**。
数値年齢は生成指示・最終Visual Identity Textへ明記しない。
幼児的にはせず、成人女性的・大人びたモデル顔にも寄せない。

採用輪郭は比較候補 **A**。
縦方向を長く見せない、柔らかく丸みのある短めの顔印象とする。
面長にしない。
細長い卵型にしない。
顔幅を削りすぎず、自然な横方向の柔らかさを残す。

頬は比較候補 **A2**。
ややふっくらした自然な頬の丸みを持たせる。
幼さと可愛さを残すが、過度な赤ちゃん顔・極端な丸顔にはしない。
頬骨を強調しない。
頬をこけさせない。

顎・下顔面は比較候補 **B2**。
下顔面はコンパクト。
顎は短めで小さく、自然な丸みを残す。
頬から顎へはなだらかに収束させる。
鋭いV字、長い顎、尖った顎にしない。

中顔面を長くしない。
目から口までを縦方向へ間延びさせない。
顔全体を美人・エレガント・成熟方向へ再解釈しない。

NOT long face.
NOT vertically elongated face.
NOT narrow elongated oval.
NOT long midface.
NOT long chin.
NOT sharp V-line face.
NOT mature model-like facial proportions.

### New face redesign authority handling
新Face Redesignでは、今回の作者選定仕様を優先する。
旧 `YURA_FACE_REFERENCE.png` は新Face画像へ未置換のため、新Face RedesignのGeometry Sourceとして使用しない。
旧Face Referenceを平均化・混合して新Faceへ戻さない。

新Face Reference画像が正式に置換・昇格された後は、その新Reference画像と本テキストを相互に整合させる。

## Eyes / Expression

### Eye size / placement
目サイズは比較候補 **C2**。
明確に大きめだが、最大級にはしない。
可愛さと若さを強く出しつつ、幼児的・極端なデフォルメ目にはしない。
縦方向へ丸く見開かない。

目位置は選定C2基準から**0.3%内側**。
この0.3%は今回の比較テスト基準に対する作者選定値であり、別の絶対測定系へ勝手に換算しない。
選定位置より目の間隔を広げない。

### Eye shape
採用Face-up画像の目形状を基準とする。
柔らかなアーモンド〜丸みを含むアニメ目。
横幅を保ちつつ、縦方向の開きは過剰にしない。
つり目すぎず、たれ目すぎない。
上まぶたはなだらかな曲線。
丸く見開いた目にしない。

### Double eyelid
二重あり。
二重線は繊細で、アニメ表現へ自然に馴染ませる。
写実的で強い二重線にしない。

### Eyelashes
まつげは黒寄りの濃いグレー。
純黒で強くインク化しない。
輪郭を少しぼかし、柔らかく馴染ませる。
存在は明確に残すが、濃密・華美・メイク的にしない。

### Iris color
瞳色は**グレーブルー**。
ブルーよりグレー感を強くする。
彩度は控えめ。
鮮やかな宝石色の青へ寄せない。

### Iris / pupil / highlight — explicit approved structure
比較用の略称・コード名だけでは仕様を解釈しない。以下の具体的構造をそのまま使用する。
瞳内部の情報量は少なめにする。

虹彩は**柔らかい上下グラデーション＋ごく薄い放射状模様**。
上部をわずかに暗く、下部をわずかに明るくする。
自然に滑らかにつなげる。
放射状模様はごく薄く、グラデーションより目立たせない。
放射状模様を強い線・密なスポーク・写実的な虹彩繊維へしない。
星・花・幾何模様・高密度の宝石状テクスチャは入れない。

瞳孔は**小さめ真円・輪郭ややぼかし**。
真円を維持する。
輪郭はわずかに柔らかくぼかす。
純黒で強く抜かず、全体のグレーブルーへ馴染む暗さとする。
左右の瞳孔は対称性を維持する。
左右で、瞳孔の大きさ・真円形状・暗さ・輪郭のぼかし強度を同等にする。
片側だけ瞳孔を薄く、弱く、小さく、または強くぼかさない。
光やハイライトの影響で、片側の瞳孔の存在感だけが弱く見える状態も避ける。

PUPILS MUST BE BILATERALLY SYMMETRIC IN SIZE, SHAPE, DARKNESS, AND EDGE SOFTNESS.
DO NOT WEAKEN ONE PUPIL RELATIVE TO THE OTHER.

ハイライトは**中サイズ主光1＋小さい副光1**。
主ハイライトは中サイズを1つ。
副ハイライトは小さいものを1つ。
形は単純で柔らかな丸形を基本とする。
細かな光点を大量に入れない。

瞳全体は、可愛い・素直・少し幼い・柔らかな透明感を優先する。

### Eyebrows
眉は採用Face-up画像の現状を維持する。
細めで柔らかい。
ニュートラルで自然な横方向を基準とする。
困り眉にしない。
眉頭を持ち上げて悲しさ・儚さを作らない。

### Nose
鼻は採用Face-up画像の現状を維持する。
小さく控えめな2Dアニメ表現。
鼻筋・鼻梁を写実的に強調しない。
立体的な美人鼻へ再設計しない。

### Mouth
口は採用Face-up画像の現状を維持する。
小さく、閉じた口。
真顔ではニュートラル。
作者の明示指示なしに口を開けない。
口角を勝手に上げたり下げたりせず、笑顔・悲しみ・困り顔へ変えない。

### Neutral expression baseline
基準表情は**真顔**。
笑顔ではない。
悲しい表情ではない。
儚い・物憂げ・困った表情を基準へ混ぜない。
困り眉は禁止。
作者が表情差分を明示した場合のみ、表情属性を追加する。

NOT round wide-open eyes.
NOT vertically enlarged eyes.
NOT worried eyebrows in neutral baseline.
NOT fragile / wistful / melancholic neutral expression.
NOT open mouth in neutral baseline.

## Face-up framing baseline
フェイスアップ基準生成は以下とする。

Exactly one YURA.
1人1枚。
正面。
直立。
頭を傾けない。
肩から上。
頭部全体をキャンバス内へ完全に収める。
頭頂を切らない。
人物を中央に配置する。
真顔。
口は閉じる。
正方形キャンバスを基準とする。

フェイスアップ画像のキャンバス占有率・トリミング・余白・ピクセル寸法から、全身時の頭部物理スケールや頭身を推定してはならない。

## Skin
肌色は**白寄りの明るい色白を強い基準**とする。
標準的な肌色やピンクベージュより、明確に白寄りに見えること。
ただし「白寄り」は純白化や白飛びを意味しない。白すぎる方向への強調・補正は禁止する。
真っ白、青白い無血色、病的な白さ、紙・陶器のような白さにしない。
ごく薄い自然な血色感を残す。
赤み・黄みを強くしすぎない。

SKIN TONE = CLEARLY WHITE-LEANING PALE SKIN.
DO NOT OVER-WHITEN.
NOT PURE WHITE.
NOT SICKLY PALE.
NOT WASHED-OUT SKIN.

質感は**マット感強め + アニメ調強め**。
表面はなめらかな2Dアニメ調とする。
写実的な毛穴・肌テクスチャを使わない。
濡れ感・油脂感・プラスチック的な強い光沢を出さない。
鼻・頬のハイライトは立体感を補助する程度に抑える。

## Body
全体として細身だが、極端に華奢にはしない。
肩とウエストは比較的細い。
腰から太腿にかけては細すぎず、自然でやわらかなラインを維持する。
太腿・ふくらはぎ・足首を極端に細くしない。

### Body proportion / head-to-body ratio
全身統合時の作者指定TARGETは **7.0〜7.2頭身** とする。
身長感は **152〜153cm程度** を目標とする。

頭頂から顎先までの頭部高を1.0とした場合、頭頂から足裏までの全身高は **7.0〜7.2** の範囲を基準とする。
**TARGET RANGE = 7.0〜7.2 heads**
**TARGET HEIGHT IMPRESSION = 152〜153 cm**

7.0〜7.2頭身は、YURAの全身における頭部と身体の相対比率として扱う。
フェイスアップ画像のキャンバス内サイズ、トリミング、余白、画面占有率から頭身・身長・BODYサイズを推定してはならない。

7.0〜7.2頭身を成立させるために、Face Geometryを変更しない。
完成Faceの頭部全体の物理スケールをBODY統合側で調整する。
胴体・脚・肩幅・腰幅・胸郭・四肢を不自然に大型化しない。
脚だけを不自然に長くしない。
胴だけを不自然に長くしない。
肩幅や骨格を大きくしない。
体格そのものを大きく見せない。

DO NOT INFER BODY PROPORTION FROM FACE REFERENCE CROP OR SCALE.
DO NOT USE FACE REFERENCE CANVAS OCCUPANCY AS BODY GEOMETRY.
DO NOT CREATE A TALL MODEL-LIKE BODY TO SATISFY 7.0–7.2 HEADS.
DO NOT INCREASE SHOULDER WIDTH OR BODY MASS TO SATISFY THE RATIO.

### Face identity / body geometry authority separation
顔Identityと全身Geometryは別Authorityとして扱う。

現行フェイス画像:
`visuals/yura/identity/face/YURA_FACE_REFERENCE.png`

現行BODY Geometryガイド画像:
`visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png`

ただし、現行フェイス画像は今回採用した新Face画像へ未置換である。
新Face Redesignでは旧Face画像のGeometryを新Faceへ混入させない。

新しいフェイス画像が正式置換された後、その画像は顔Identity・顔内部比率・目・眉・鼻・口・頬・顎・顔まわりの髪のIdentity確認に使用する。
フェイス画像は、頭身・BODYサイズ・身長感・肩幅・胴長・脚長・全身キャンバス占有率のAuthorityではない。

BODY Geometryガイドは、頭部と身体の相対スケール・全身Geometryを規定するために使用する。
BODY Geometryガイドは、顔内部の造形・目・眉・鼻・口・頬・顎のIdentityを変更するAuthorityではない。

**FACE_REFERENCE -> BODY_PROPORTION = DENIED**
**FACE_REFERENCE -> FULL_BODY_SCALE = DENIED**
**FACE_REFERENCE -> CANVAS_OCCUPANCY = DENIED**
**BODY_GEOMETRY_GUIDE -> FACE_GEOMETRY = DENIED**
**BODY_GEOMETRY_GUIDE -> FACE_IDENTITY = DENIED**

FACE GEOMETRY IS LOCKED AFTER AUTHOR APPROVAL.
顔の縦横比を変更しない。
目の大きさ・形・間隔を変更しない。
眉・鼻・口の相対位置を変更しない。
中顔面の長さを変更しない。
下顔面の長さを変更しない。
顎の形状を変更しない。
頬の幅と丸みを変更しない。
顔を面長化しない。
顔を横長化しない。

顔画像の見かけ上の頭部サイズを基準に、頭部またはBODYを機械的に拡大・縮小しない。
7.0〜7.2頭身はBODY Geometry側の全身配置として成立させる。

BODY Geometryガイド画像が存在しない場合、フェイス画像をその代替として使用してはならない。

FACE SHAPE MUST REMAIN IDENTICAL IN PROPORTION.
FACE REFERENCE CONTROLS IDENTITY, NOT FULL-BODY SCALE.
BODY GEOMETRY GUIDE CONTROLS PROPORTION, NOT FACE IDENTITY.

### Chest — Core priority
胸部は、細身の体格に対して**やや豊か**であることを基準とする。
細い肩・胸郭・ウエストとの対比の中で、胸部には明確なボリュームを残す。
細身体格であることを理由に、胸部まで小さく・平坦に縮小しない。

胸部形状は、自然かつ綺麗でやわらかな**形が整ったおわん型**を基準とする。
前方へ自然な丸みを持ち、上半身のシルエットとして認識できる程度のふくらみを維持する。
左右へ広がりすぎず、中央寄りの自然なまとまりを保つ。
輪郭は丸く連続させ、尖った形・角張った形・平坦な形へ変形させない。

胸部はやや高めの位置にまとまり、張りのある形状とする。
上胸にも自然なボリュームを残し、下側だけに重さが集中しない。
胸部の最も前方へ出る位置を低くしすぎない。
胸部下縁を必要以上に下げない。
左右それぞれがコンパクトに丸くまとまり、重力で下方向へ長く伸びた形にしない。

胸部のボリュームは、上部から中央、下部へ自然に連続する丸みとして形成する。
下半分だけが大きく膨らむ形状にはしない。

FIRM, HIGH-SET, ROUNDED CHEST SHAPE.
胸部は張りがあり、やや高めの位置にある丸い形状を優先する。

CHEST VOLUME RELATIVE TO BODY HAS PRIORITY OVER SLENDER-BODY SIMPLIFICATION.
胸部の体格比を、細身体格の単純化より優先する。

服装によって胸部の体格比を消さない。
検証用の軽装は身体の自然なシルエットに沿わせ、胸部を押し潰したり平坦化したりしない。

NOT flat chest.
NOT undersized chest relative to the body.
NOT reduced chest because the body is slender.
NOT exaggerated oversized chest.
NOT laterally spread chest.
NOT pointed chest.
NOT conical chest.
NOT flattened chest silhouette.
NOT clothing-compressed chest silhouette.
NOT sagging chest.
NOT drooping chest.
NOT low-set chest.
NOT bottom-heavy chest.
NOT elongated downward chest shape.
NOT deflated upper chest.
NOT flattened upper chest.
NOT excessively low breast contour.

## Ears

### Core priority
耳はYURAの視覚的特徴として強調しない。
耳はやや小さめを基準とし、頭部側面に近く沿わせる。
耳の存在感は弱く保つ。
現在の生成で見られた長めの耳傾向は抑制する。

EAR SIZE AND NATURAL PLACEMENT HAVE PRIORITY OVER EAR VISIBILITY.
耳の可視性より、耳の小ささ・自然な位置・自然な向きを優先する。

### Ear geometry status
耳の最終Geometryは、後に作成する髪なし頭部画像で確定する。
現段階では位置基準・縦方向コンパクトさ・低い存在感を固定し、髪ありFace-up画像だけから最終寸法を断定しない。

### Ear size ratio
顔の縦寸法を100%とする。
顔の縦寸法は、額上部から顎先までとする。

耳の実形状の縦寸法は、顔の縦寸法に対して**20〜22%**をTARGETとする。
**HARD MAX = 23%**とし、23%を超えてはならない。

この比率は、髪で隠れている部分を含む耳本体の推定全高に適用する。
見えている部分だけを基準に耳を拡大してはならない。

耳が髪に隠れて見えにくい場合でも、可視性を確保するために23%を超えて拡大しない。
耳の可視部分が小さくても問題としない。
耳のサイズ維持を可視性より優先する。

### Vertical compactness
「小さい耳」は、横幅が細いだけではなく、縦方向の高さ自体が短くコンパクトであることを意味する。
細くても縦に長い耳はYURAの耳として扱わない。
耳の上端から下端までの縦スパンを短く保ち、頭部側面にコンパクトに収める。

EAR SMALLNESS MUST INCLUDE SHORT VERTICAL HEIGHT.
NOT narrow-but-tall ears.
NOT vertically stretched ear silhouette.

### Placement landmarks
耳の付け根の上側は、おおむね目の高さを基準とする。
耳の付け根の下側は、おおむね鼻下の高さを基準とする。
耳全体の上端は眉付近を上限目安とする。

ただし、これらの基準線の間を埋めるために耳を縦へ伸ばしてはならない。
これは位置の基準であり、耳の高さを最大化するための範囲ではない。
YURAでは小型・縦方向コンパクト規則を優先する。

### Shape
耳を縦長にしない。
耳を横方向へ広げない。
耳たぶを長くしない。
耳の上端・下端を強調しない。
耳の輪郭を必要以上に明瞭に描かない。
耳介内部の構造を過度に描き込まない。

耳は頭部側面から大きく突出させない。
耳の外縁を頭部シルエットから大きく外へ出さない。

### Hair occlusion
髪による耳の遮蔽を積極的に許容する。
耳は一部だけ見えていてよい。
耳全体が見える必要はない。
耳がほぼ完全に髪で隠れてもよい。
左右の耳が同程度に見える必要はない。

耳が見えにくい場合は、そのまま隠れた状態を維持する。
耳を見せるために髪を避けない。
耳を見せるために髪束を耳の後ろへ移動させない。
耳を見せるために髪の流れを変更しない。

### No visibility compensation
耳の可視性を確保するための補正を禁止する。

耳を大きくしない。
耳を縦方向へ伸ばさない。
耳を横方向へ広げない。
耳を外側へ移動させない。
耳を顔から離さない。
耳をカメラ側へ回転させない。
耳を正面へ向けない。
耳を髪の外へ押し出さない。

耳が髪に隠れた場合、
「見えないから大きくする」
「見えないから外へ出す」
「見えないから向きを変える」
という補正を行わない。

### Front-view lock
正面視では、耳は特に控えめに扱う。
正面から耳全体を明瞭に見せない。
正面視で左右の耳を対称に完全露出させない。
耳が頭部の左右へ大きく張り出したシルエットにしない。

正面視で見える耳は、細い一部分だけでよい。
耳の外周全体を見せる必要はない。
髪の隙間からごく一部だけ見える状態を優先する。
髪によって耳が完全に見えなくても正常とする。

NO VISIBLE EAR IS ACCEPTABLE IN FRONT VIEW.
DO NOT EXPOSE THE EAR FOR READABILITY.

### Fail-safe
耳の可視性と自然なサイズが両立しない場合は、耳を大きくして見せるのではなく、髪で隠す。

耳の構造を明示するために、YURAの頭部・顔・髪の形状を変更してはならない。

NOT large ears.
NOT elongated ears.
NOT wide ears.
NOT protruding ears.
NOT outward-flared ears.
NOT camera-facing ears.
NOT front-facing ears.
NOT long earlobes.
NOT pointed ears.
NOT elf-like ears.
NOT fully exposed ears in front view.
NOT symmetrical full ear exposure.
NOT visibility-driven ear enlargement.
NOT visibility-driven ear repositioning.

## Validation Clothing
TEXT_ONLY検証時の服装は、白〜ごく薄いグレー系のシンプルな軽装。
装飾は最小限。
裸足。

## Pose / Composition
Exactly one YURA.
1人1枚。
正面。
全身。
完全な直立姿勢。
頭を傾けない。
両腕は左右とも自然に下ろす。
手を背中に回さない。
脚はほぼ揃える。
白背景。
人物を中央に配置する。

## Rendering
高品質な2Dアニメ表現。
アニメ調を強く保つ。
マット感を強めにする。
全体に明るく高キー。
線は細く繊細だが、消えるほど薄くしない。
陰影はやわらかく、アニメ的なまとまりを保つ。
写実的な肌・髪・立体表現へ寄せない。
NOT photoreal.
NOT semi-photoreal.
NOT realistic portrait.
NOT live-action.
NOT CGI / 3D render.