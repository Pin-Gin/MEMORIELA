# 久遠ゆら Visual START HERE

Status: **CANONICAL YURA VISUAL ENTRYPOINT**

Purpose: MEMORIELAの挿絵・漫画・立ち絵で、久遠ゆらを同一人物として安定生成するための入口。

## Read order
通常生成:
1. `identity/master/YURA_VISUAL_MASTER.md`
2. `identity/body/BODY_SPEC.md`
3. `identity/face/FACE_SPEC.md`
4. `identity/eyes/EYE_SPEC.md`
5. `identity/hair/HAIR_SPEC.md`
6. `identity/hair/styles/NORMAL_SUPER_LONG.md`
7. `identity/skin/SKIN_SPEC.md`
8. `identity/rendering/YURA_RENDERING_SPEC.md`
9. `../CHARACTER_RENDERING_STYLE.md`
10. `generation/GENERATION_RULES.md`

必要時のみ:
- 動的ポーズ → `generation/POSE_RULES.md`
- 衣装変更 → `generation/OUTFIT_RULES.md`
- 検証生成 → `qa/VALIDATION_CLOTHING.md` + `qa/GENERATION_QA.md`

## Generation priority — strict

画像生成時の優先順位は次の通り。

1. **Current YURA Visual Master PNG**
   - `identity/master/YURA_VISUAL_MASTER.png`
   - whole-character visual anchor
   - 顔・BODY・髪・全体シルエット・描画印象の基準
2. **Protected Identity Specs**
   - BODY / FACE / EYE / HAIR / NORMAL_SUPER_LONG / SKIN
   - 各領域の固定条件
   - Masterを別人へ再設計するためではなく、Masterからの逸脱を防ぐために使う
3. **Requested pose / camera / outfit / expression / scene**
   - 派生条件
   - IdentityやBODYを再設計しない
4. **YURA-specific Rendering**
   - `identity/rendering/YURA_RENDERING_SPEC.md`
   - YURA固有の描画制約
5. **Project-wide Matte Natural Anime**
   - `../CHARACTER_RENDERING_STYLE.md`
   - 表面質感・陰影・描画タッチ
6. **Generation hygiene / QA**
   - one-person rule / framing / validation condition / QA

### Conflict rule
- Master PNGがwhole-character identityの最上位視覚アンカー。
- BODY / FACE / EYE / HAIR / SKINは、それぞれの領域で明示された固定条件を守るための制約。
- 下位レイヤーは上位レイヤーを再解釈・再設計しない。
- rejected / intermediate generationをIdentity参照として混ぜない。

## Authority rule
Visual Masterはwhole-character visual anchor。BODY / FACE / EYE / HAIR / SKINは各領域の固定仕様。YURA RenderingはYURA固有補正。Matte Natural AnimeはMEMORIELA共通描画タッチ。Outfit / pose / expression / sceneは派生レイヤーでありIdentityを再設計しない。

## Default generation rule
- exactly one YURA per image
- default hair: Normal Super-Long
- userが明示しない限り髪型差分を勝手に適用しない
- 検証時は白背景・検証服・裸足
- 未承認生成物をVisual Masterへ自動昇格しない

## Novel boundary
年齢、人物関係、時系列、制服、場面設定など物語Canonは `characters/` / `story/` を正とする。このVisual Domainは人物の外見と生成安定性のみを扱う。
