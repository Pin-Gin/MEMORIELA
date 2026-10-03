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

### YURA domain isolation
`characters/YURA.md` は小説資料専用であり、YURA画像生成のVisual Authorityではない。

YURA画像生成、Prompt/Payload作成、Reference選択、Visual QA、Visual情報の補完に `characters/YURA.md` を使用してはならない。
Visual側の必要情報が未定義の場合も `characters/YURA.md` へfallbackせず、生成を停止する。

`NOVEL_CANON != VISUAL_AUTHORITY`

作者はユーザー。AIは壁打ち、QA、整合性確認、POV/情報開示確認、演出稿→小説稿変換補助、添削・校正を担当する。
