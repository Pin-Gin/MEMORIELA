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
6. `identity/rendering/YURA_RENDERING_SPEC.md`
7. `../CHARACTER_RENDERING_STYLE.md`
8. `generation/GENERATION_RULES.md`

必要時のみ:
- 動的ポーズ → `generation/POSE_RULES.md`
- 衣装変更 → `generation/OUTFIT_RULES.md`
- 検証生成 → `qa/VALIDATION_CLOTHING.md` + `qa/GENERATION_QA.md`

## Authority rule
Visual Masterはwhole-character visual anchor。BODY / FACE / EYE / HAIRは各領域の固定仕様。YURA RenderingはYURA固有補正。Matte Natural AnimeはMEMORIELA共通描画タッチ。Outfit / pose / expression / sceneは派生レイヤーでありIdentityを再設計しない。

## Default generation rule
- exactly one YURA per image
- default hair: Normal Super-Long
- userが明示しない限り髪型差分を勝手に適用しない
- 検証時は白背景・検証服・裸足
- 未承認生成物をVisual Masterへ自動昇格しない

## Novel boundary
年齢、人物関係、時系列、制服、場面設定など物語Canonは `characters/` / `story/` を正とする。このVisual Domainは人物の外見と生成安定性のみを扱う。
