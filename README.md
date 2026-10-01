# MEMORIELA

MEMORIELAの小説制作・設定管理・Visual制作リポジトリ。

## Start
小説・設定・執筆作業は [NOVEL_START_HERE.md](NOVEL_START_HERE.md) から開始する。

## Current Authority
- `characters/`: 小説世界の人物・経歴・家族・関係
- `story/`: 作品の核、時系列、Knowledge State
- `manuscript/`: 各話の原稿と制作メモ
- `rules/`: 執筆・Canon管理ルール
- `visuals/`: MEMORIELA本編キャラクターのVisual制作・Visual Authority

## Visual policy
MEMORIELA本編キャラクターの画像生成・Visual Identity・Visual Master・Visual Text・生成ルール・QAは、`visuals/` を正とする。

Current character Visual domains:
- 久遠ゆら → `visuals/yura/`
- 一ノ瀬栞 → `visuals/shiori/`
- project-wide rendering → `visuals/CHARACTER_RENDERING_STYLE.md`

背景（家・部屋・学校等の構造）は本リポジトリ内の旧Creation資料をAuthorityとして使用しない。背景担当Projectで別途管理する。
ぴんぎん / Pin-Gin はMEMORIELAのマスコットとして別Projectで管理し、本リポジトリのキャラクターVisual生成Authorityから外す。

旧AI版Project.YURAの人格・経歴・生活設定は現行小説Authorityではない。
久遠ゆらの既存Visual Identityは小説版へ継承し、`visuals/yura/` の現行Visual Authorityとして使用する。

作者はユーザー。AIは壁打ち、QA、整合性確認、POV/情報開示確認、演出稿→小説稿変換補助、添削・校正を担当する。
