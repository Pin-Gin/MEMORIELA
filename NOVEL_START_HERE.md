# MEMORIELA Novel — START HERE

このリポジトリの現行目的は、MEMORIELAの小説制作と、そのためのビジュアル制作である。

## Authority
小説世界の人物・経歴・家族・関係・時系列は本小説資料を正本とする。

## 作業開始時
最低限、次を読む。
1. NOVEL_START_HERE.md
2. rules/WRITING_RULES.md
3. rules/CANON_RULES.md
4. story/STORY_CORE.md

人物を扱う場合は characters/ の該当人物を読む。
話数を扱う場合は manuscript/ の該当話数と、必要に応じて story/TIMELINE.md / KNOWLEDGE_STATE.md を読む。

## Character Visual Authority
MEMORIELA本編キャラクターの画像生成では、**`visuals/` をVisual Authorityの正本とする。**

Current domains:
- 久遠ゆら → `visuals/yura/`
- 一ノ瀬栞 → `visuals/shiori/`
- 共通描画タッチ → `visuals/CHARACTER_RENDERING_STYLE.md`

各キャラクター生成では、その人物のVisual Master / Visual Text / generation rule / QAを必要範囲で読み、キャラクター固有Identityを維持する。
キャラクター画像生成では、キャラクター固有Visual Authorityに加えて `visuals/CHARACTER_RENDERING_STYLE.md` を必ず読み、MEMORIELA共通の描画タッチ **Matte Natural Anime / マット・ナチュラルアニメ** を適用する。

### YURA hard boundary
`characters/YURA.md` は **小説専用Authority** であり、YURA画像生成から完全に切断する。

YURA画像生成時に `characters/YURA.md` を:
- 読み込まない
- Visual Authorityとして解決しない
- Prompt / Execution Payloadへ変換しない
- 欠落Visual情報のfallbackに使用しない
- Visual QA / Reference判定に使用しない

`characters/YURA.md` 内の外見記述は小説本文の整合性のためのNovel Canonであり、画像生成条件ではない。

YURA Visual側の定義が不足・未定義・RESET中の場合は、Novel Canonから補完せず生成を停止する。

`NOVEL_CANON != VISUAL_AUTHORITY`

## AIの役割
作者はユーザーである。AIは壁打ち、初見読者QA、ストーリー/整合性/POV/情報開示QA、演出稿から小説稿への変換補助、添削・校正を担当する。
作者が確定していない設定・感情・過去を「小説らしくするため」に勝手に確定しない。
