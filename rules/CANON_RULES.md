# Canon Rules

設定は以下で区別する。

- **FIXED**: 作者が正式決定した正史。変更時は明示的に更新する。
- **PROVISIONAL**: 現時点の採用案。物語との整合で変更可能。
- **UNDECIDED**: まだ決めていない。
- **IDEA**: 壁打ちで出た候補。正史として扱わない。

会話で案が出ただけではFIXEDにしない。
矛盾時は現行GitのFIXED記述を優先し、作者へ矛盾を提示する。

## Domain isolation — YURA Novel / Visual
`characters/YURA.md` のFIXEDは **Novel Canon** であり、YURA画像生成のVisual Authorityではない。

YURA画像生成では、`characters/YURA.md` をAuthority、Prompt/Payload source、fallback source、Visual QA source、Reference-selection sourceとして使用してはならない。

Novel CanonとVisual Canonは別Domainとして扱い、Novel側のFIXEDを理由にVisual側を補完・上書き・推測してはならない。

Visual側が未定義・RESET中・不足している場合:
`GENERATION_ALLOWED = NO`

`NOVEL_CANON != VISUAL_AUTHORITY`
