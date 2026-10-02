# YURA GENERATION RULES

Status: **CANONICAL / MANDATORY OPERATIONAL RULES**

Authorityの読込順・正式パス・Reference roleは本書では再定義しない。
必ず `../gate/AUTHORITY_MANIFEST.md` / `../gate/REFERENCE_GATE.md` / `../gate/VIEW_ROUTER.md` に従う。

## One-person rule
Unless explicitly requested otherwise:
- exactly one YURA
- one image / one figure
- no character sheet
- no multi-pose sheet
- no automatic front+side+back layout

複数枚は1人1枚として個別生成する。

## Identity lock
常に保護:
- 153 cm concept
- exact 7.25-head BODY
- YURA face
- blue-gray eyes
- silver-white hair
- default Normal Super-Long unless explicitly changed
- protected SKIN
- YURA-specific rendering

## No AI reinterpretation
Visual Master / Visual Text / BODY / FACE / EYE / HAIR / SKIN / renderingを:
- 要約して別の意味へ置換しない
- 一般的なアニメ表現へ置換しない
- 自然さを理由に再設計しない
- 未指定箇所を常識で補完しない
- 複数Authorityを平均化しない

`UNSPECIFIED != PERMISSION TO INVENT`

ユーザーが明示的にVariationを許可したScopeだけ変更可能。

## Text-only Root Master creation
When:
`MASTER_CREATION_SUBMODE = TEXT_ONLY_ROOT_MASTER`

follow exactly:
`master-creation/TEXT_ONLY_ROOT_MASTER.md`

No generation-time image reference is permitted.

The current Root Master may be used only for post-generation QA comparison.

Do not create Face Master or BODY View Masters until the Root Master stability status permits them.

## Pose route
意味のある動作・体幹回転・側面化・着座等では:
- `POSE_RULES.md` を読む
- `../gate/VIEW_ROUTER.md` でBODY viewを決定
- selected BODY view referenceを固定
- Face Detail Referenceを維持
- `../../gate-core/VISIBILITY_OCCLUSION_PROTOCOL.md` を適用

## Outfit route
衣装変更では `OUTFIT_RULES.md` を読む。
School Uniformの場合は `../../school-uniform/gate/GENERATION_GATE.md` を依存Gateとして通過する。

GARMENT FOLLOWS BODY.
BODY NEVER FOLLOWS GARMENT MASTER.

## Validation route
Controlled validation:
- white background
- barefoot
- `../qa/VALIDATION_CLOTHING.md`
- `../qa/GENERATION_QA.md`

## Retry lock
局所FAIL時はFAILしたScopeだけを修正する。
Gate PASS後のIdentity Reference / Face Reference / Body View Reference / Authority Manifest / Rendering grammarを再選定しない。

Rejected / intermediate generationは次回Identity Referenceへ昇格させない。
