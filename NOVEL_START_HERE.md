# MEMORIELA Novel — START HERE

このリポジトリの現行目的は、MEMORIELAの小説制作と、そのためのビジュアル制作である。

## Authority
小説世界の人物・経歴・家族・関係・時系列は本小説資料を正本とする。
旧AI版Project.YURAの人格・経歴・生活設定は小説版へ継承しない。
ただし久遠ゆらの既存Visual Identity（顔・瞳・体型・髪・レンダリング・Visual Master等）は小説版ゆらへ継承する。

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

旧 `docs/assistant-context/creation/` はVisual Authorityとして使用しない。
背景（家・部屋・学校等）は背景担当Project、ぴんぎん / Pin-Gin はマスコット担当の別Projectで管理する。

## AIの役割
作者はユーザーである。AIは壁打ち、初見読者QA、ストーリー/整合性/POV/情報開示QA、演出稿から小説稿への変換補助、添削・校正を担当する。
作者が確定していない設定・感情・過去を「小説らしくするため」に勝手に確定しない。
