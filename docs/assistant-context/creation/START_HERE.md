# MEMORIELA — Creation START HERE

Status: **CANONICAL VISUAL CREATION ENTRYPOINT**

MEMORIELAの画像・Visual制作を開始するための共通入口。
物語設定のAuthorityはリポジトリ直下の `NOVEL_START_HERE.md` と `characters/` / `story/` にある。
Creation資料は人物の経歴・家族・物語Canonを上書きしない。

## Routing
- 久遠ゆら → `creation/yura/START_HERE.md`
- Pin銀 → `creation/pingin/START_HERE.md`
- Background → `creation/background/START_HERE.md`
- 今後追加する要・大和・美緒・栞等 → 各人物のCreation Domainを新設する。

## Domain Separation
人物Visual、Pin銀、Backgroundを理由なく混在させない。
複数Domainを含む制作物では、各要素を支配するAuthorityを分離して扱う。

## Novel / Visual Boundary
- 人物の人生、性格、関係、家族、時系列: Novel Authority
- 顔、髪、体型、瞳、衣装、レンダリング、Visual Master、生成QA: Creation Authority
- 小説側でVisual設定が正式変更された場合は、Creation Authorityとの整合を確認して更新する。

## Safety
未承認生成物や途中画像をVisual Masterへ自動昇格しない。
既存Masterの変更は明示的な作者承認を必要とする。
