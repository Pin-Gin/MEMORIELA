# YURA Normal Super-Long Spec

Status: **PROTECTED NORMAL-DOWN HAIR SUB-SPEC / CURRENT DEFAULT HAIRSTYLE IMPLEMENTATION**
Current Revision: **v1.0**
Adopted: 2026-09-15
Character: 久遠ゆら / YURA
Parent HAIR authority: `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
Applies to: YURAの通常時の下ろし髪、立ち絵、日常CG、衣装差分、公開用ビジュアル、Normal Super-Long検証

---

## 1. Purpose

本書は、YURAにおける通常時の基本髪型 **Normal Super-Long** の正式仕様を定義する。

Normal Super-Long は、YURAの髪をアレンジしていない通常状態の基準形であり、将来ポニーテール、ハーフアップ、シニヨン等を構成する際の source hairstyle でもある。

本仕様の目的は、通常の下ろし髪について次のブレを抑えることにある。

- 長さの過不足
- 毛量の不安定化
- 横方向への過剰な広がり
- 正面での過剰な前回り
- 背面での不自然な毛量減少
- 毛先の重すぎる / 薄すぎる処理
- 実写繊維・CG方向への質感ドリフト

---

## 2. Authority relationship

YURA HAIR domain の親正本は:

`visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`

本書はその値を変更せず、**Normal Super-Long / normal down style の具体的なシルエット・分布・正面 / 背面挙動を固定する sub-spec** とする。

競合時:

- core hair color / source length / total mass / texture / bangs / face framing / gravity → `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
- normal down-style silhouette / front-back distribution / default presentation → 本書
- ponytail / chignon / half-up / braid等のarrangement topology → `visuals/yura/identity/hair/HAIR_ARRANGEMENT_GUIDELINE.md`
- rendering grammar → `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md`

本書は `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md` を置き換えない。

---

## 3. Core definition

YURAの髪型に別のアレンジ指定がない場合、基本髪型は **Normal Super-Long** とする。

基本印象:

- 上品
- 柔らかい
- 大人っぽい
- 落ち着きがある
- 長髪らしい密度がある
- 横に広がりすぎない
- 長さと毛量を感じるが重苦しくない

髪は通常、結ばず、編まず、まとめず、銀白色のスーパーロングを自然に下ろした状態とする。

---

## 4. Length — protected

### 4.1 Standard range

- 髪の**主な毛先位置**は、自然に下ろした状態で **ウエストライン付近〜わずかに下** を基準とする。
- **最長の細い毛先**のみ、**上臀部手前**まで許容する。

### 4.2 Too-short / too-long boundary

- 大部分が胸下付近で終わる → **FAIL / too short**
- ウエスト付近 → **PASS baseline**
- ウエストを少し越える → **PASS**
- 最長の繊細な毛先のみ上臀部手前 → **PASS**
- 髪の主要毛量が臀部中央より下へ達する → **FAIL / too long**
- 太ももまで届く長さ → **FAIL / prohibited interpretation**

### 4.3 Interpretation rule

本仕様における `Super-Long` は「非常に長い髪」という自由解釈ではない。

**主体となる長さはウエスト付近に収まり、最長の細い毛先のみ上臀部手前まで許容される。主要毛量を臀部中央〜太ももへ延長しない。**

生成時は「ウエスト付近」を主指定とし、「臀部中央〜太ももへ延長しない」は上限ガードとして使用する。

---

## 5. Hair volume / strand quality — protected

Normal Super-Long は HAIR v1.3 の8条件をそのまま継承する。

1. 総毛量 = **標準よりやや多め**
2. 一本一本 = **細く柔らかい**
3. 上部 = **長さの自重で自然に落ち着く**
4. 中間〜背中 = **十分な密度を保つ**
5. 横幅 = **あまり広がらない**
6. 毛先 = **徐々に量が抜け、軽く繊細に収束する**
7. **細い髪 = 少毛 と解釈しない**
8. 将来まとめ髪にしても source total mass を勝手に減らさない

Normal Super-Longでは特に、毛量の多さを頭頂・側頭部の膨張ではなく、**中間〜背面側の十分な密度**として表現する。

---

## 6. Overall silhouette — protected

### 6.1 Main silhouette

全体シルエットは **縦長のIライン寄り** とする。

- 頭頂部・側頭部は長さの自重で比較的落ち着く。
- 中間部には十分な厚みと密度を保つ。
- 外側へ大きく張り出さない。
- 下方へ進むほど自然にテーパーする。
- 主たる流れは背中側へ縦方向に落ちる。

### 6.2 Lateral width

Normal Super-Long は `ふわっと横へ大きく広がる髪` ではない。

避ける:

- 扇状の大きな広がり
- 三角形状の巨大シルエット
- 頭周りだけの過剰なボリューム
- 静止状態での不自然な浮遊

---

## 7. Bangs / face framing — protected

### 7.1 Bangs

- 重すぎない**薄めのロングバング**。
- 中央付近から自然に左右へ流れる。
- 目元へわずかにかかる程度。
- 額を完全に塞ぐほど厚くしない。
- 強いぱっつん感を避ける。

### 7.2 Face framing

- 左右に、頬へ沿う**長めのサイドバング**を残す。
- フェイスラインを柔らかく包む。
- 前髪・サイドバング・後ろ髪は柔らかなレイヤーで自然につなぐ。
- 顔まわりも横へ大きく張り出しすぎない。

---

## 8. Front-view behavior — protected

正面では、**後ろ髪の主質量を背面側に保持する**。

- 前へ回り込む髪は、顔まわり〜胸付近の一部にとどめる。
- 後ろ髪の大半を左右の胸側へ持ってこない。
- 長髪であることが自然に読み取れる程度の前面量は許容する。
- 衣装やBODYを見せるためだけに、髪を左右へ不自然に逃がさない。
- 逆に前面へ過剰に回して胴体を不自然に覆い尽くさない。

正面で見える髪量はカメラ投影の結果であり、背面側の source mass を削減して作ってはならない。

---

## 9. Back-view behavior — protected

背面では、**主毛量が後頭部中央から背中中央〜腰方向へ自然に落ちる**。

- 長い後ろ髪の大部分を背中側へ保持する。
- 背中・腰・衣装を見せるためだけに髪を胸側へ退避させない。
- 主毛量を左右へ大きく割り、背中中央を意図的に露出させない。
- 背中やウエスト周辺が髪で大きく隠れることは正常。
- 最長の繊細な毛先のみ上臀部手前まで許容する。
- 主要毛量を臀部中央より下、特に太ももまで延長しない。

---

## 10. Flow / gravity / contact — protected

- 基本は**重力に従って下方向へ自然に落ちる**。
- 風がない通常状態では大きく暴れない。
- 大きなS字や過度な外ハネを標準にしない。
- 長さの自重により、短髪のような軽い跳ね方をしない。
- 肩、背中、腰、腕、衣装、椅子等との接触を無視して浮遊させない。
- 接触面に沿って垂れる / 乗る / 流れる。
- 接触で局所的な流れが変わっても、根元から毛先までの連続性を保つ。

---

## 11. Tips / end treatment — protected

- 毛先は切り揃えた重い直線にしない。
- 中間部の密度を保ちながら、下方へ進むほど徐々に量が抜ける。
- 最終部は**軽く繊細に収束**する。
- `厚いまま突然終わる` と `スカスカで消える` の両方を避ける。
- 一本一本の細さと、全体として十分な毛量を両立する。

---

## 12. Rendering relationship

Normal Super-Long は `visuals/yura/identity/rendering/RENDERING_STYLE_SPEC.md` に従う。

- 高品質2Dアニメイラスト
- grouped / illustrated hair locks
- 適度にまとまった毛束表現
- 細く柔らかな印象
- 硬い一枚板にはしない
- ハイライトは上品で控えめ
- 実写的な一本一本の毛髪繊維を主表現にしない
- 過度な濡れ感 / ワックス感 / PBR / CGI的硬質感を避ける

---

## 13. FAIL / prohibited interpretations

### Length

- 胸下程度が主体となる短さ
- 主要毛量が臀部中央より下へ到達
- 太ももまで届く髪

### Volume / silhouette

- 細髪を理由にした少毛化
- 横方向へ大きく広がる三角形 / 扇形シルエット
- 頭頂部・側頭部だけの過剰な膨張
- 静止時の大きな浮遊

### Distribution

- 正面で後ろ髪の大半を胸側へ回す
- 背面で主毛量を不自然に左右へ割る
- BODY / 衣装を見せるためだけに背面毛量を減らす

### Tips / texture

- 毛先まで均一な厚みのまま終わる
- 毛先が重い一枚板になる
- 毛先がスカスカすぎる
- 実写的繊維感が支配的になる
- CGI / PBR的な硬い髪になる

---

## 14. Prompt baseline

Normal Super-Long生成では、少なくとも次の意味内容を含める。

`銀白色のNormal Super-Long。主な毛先は自然なウエストライン付近〜わずかに下まで届き、最長の細い毛先のみ上臀部手前まで許容する。主要毛量を臀部中央より下や太ももまで延長しない。一本一本は細く柔らかいが総毛量は標準よりやや多め。長さの自重で頭頂〜上部は自然に落ち着き、中間〜背中には十分な密度を残す。全体は縦長のIライン寄りで横へ大きく広がらず、下方へ進むほど自然にテーパーして毛先は軽く繊細に収束する。正面でも主毛量は背面側に保持し、前へ回り込むのは顔まわり〜胸付近の一部のみ。背面では主毛量が背中中央〜腰方向へ自然に落ちる。`

Anti-drift guard:

`Do not extend the principal hair mass to mid-buttock or thigh length. Do not make fine hair sparse. Do not fan the hair widely sideways. Keep the main mass gravity-dominant and behind the shoulders/back.`

---

## 15. Visual validation / master-candidate rule

Normal Super-Long の視覚基準候補を生成する場合、原則として他の変数を固定する。

推奨比較条件:

- current YURA visual identity lock
- BODY v1.0 / exactly 7.25 heads
- FACE / EYE SIGNATURE lock
- RENDERING lock
- simple pale inner top + simple pale shorts
- bare feet
- no accessories
- no hair ornaments
- neutral / relaxed-to-soft expression
- front-facing full-body standing baseline
- 9:16 portrait
- minimal safe margin
- white / warm-white neutral background
- no text / logo / panel / character-sheet layout

生成された強い候補は **Normal Super-Long visual reference candidate** として評価できる。

ただし、Normal Super-Long候補を採用しただけでは `visuals/yura/identity/master/VISUAL_MASTER.png` を自動的に置き換えない。whole-character MASTER差し替えには別途明示的なユーザー承認が必要。

---

## 16. One-line summary

**YURAの Normal Super-Long は、主な毛先がウエスト付近〜わずかに下まで届く銀白色の上品なスーパーロングであり、標準よりやや多めの毛量を持ちながら一本一本は細く柔らかく、重力に従って縦長のIラインへ落ち、横に広がりすぎず、毛先へ向かって軽く繊細に収束する通常時の基準髪型である。**

---

## 17. Change control

本仕様は PROTECTED とする。

長さ・毛量・縦横シルエット・正面 / 背面分布・毛先・FAIL境界に関わる変更は、明示的な再検証とユーザー承認なしに変更しない。

本仕様の変更時は最低限次を再確認する。

- `visuals/yura/identity/hair/HAIRSTYLE_SPEC.md`
- `visuals/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
- `visuals/yura/generation/TEXT_ONLY_GENERATION_REFERENCE.md`
- `visuals/yura/qa/GENERATION_QA.md`
- `YURA_STATE_SNAPSHOT.md`
- `visuals/yura/START_HERE.md`

Normal Super-Long以外の髪型差分は、本仕様を無理に拡張せず、それぞれのarrangement rule / future visual referenceで扱う。
