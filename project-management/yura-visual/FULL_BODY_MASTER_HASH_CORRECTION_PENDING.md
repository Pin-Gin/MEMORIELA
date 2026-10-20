# YURA Full-body Master — 作者指定原本のSHA-256確認とGitバイナリ置換待ち

Status: **AUTHOR DESIGNATED CANONICAL SOURCE / GIT BINARY REPLACEMENT PENDING**
Decision date: 2026-10-20
Owner: author. This is a handoff and correction record, **not** a replacement PNG file.

## 作者が正として指定したファイル

2026-10-20、作者はチャット添付の `YURA_FULL_BODY_MASTER(2).png` を「これがマスタ画像」と明示し、この添付ファイルと同じSHA-256を正とするよう指定した。ファイルは直接読み込み、以下を確認した。

```text
CANONICAL / AUTHOR-SELECTED SHA-256
07e26596642f4953393f1f09d3d5a0923627f532c8ff1b8b85595ae9058503e3

image size: 1152 x 2048
color mode: RGBA
file size: 2,156,473 bytes
Git blob SHA-1 if committed as-is: 5c434b94040e8d9b18395a6098c4178401f2eb7d
```

**Authoritative binary intent is the exact image bytes that yield this SHA-256.**
Do not substitute a resized, re-encoded, re-exported or visually similar image. Those changes alter the SHA-256.

## 確認時点でGitに残っている旧バイナリ

```text
visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png
visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png

Git blob SHA-1 for BOTH OLD files:
10ecaed9527a5f25791ff3c9c00eb2321f083d70

previously documented SHA-256 (OLD BINARY):
CCBE315659DAC02169C833F8140096322725E85250FAB73214D30FBBC835EDF1

Git binary size: 2,225,290 bytes
```

The old Git binary does **not** equal the author-selected exact file. The old binary and old SHA remain in prior operational documents and frozen paid-route config **until replaced and reconciled**.

## 正しい移行手順・完了条件

1. Author-designated original PNG file (SHA-256 `07e265...`) must be available on local working PC exactly, **not a screenshot or JPEG**.
2. Verify source file using `Get-FileHash -Algorithm SHA256` and ensure the **complete** hash matches.
3. Replace BOTH Git files **with identical original bytes**:
   - `visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png`
   - `visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png`
4. Verify both target SHA-256 values are exactly `07e26596642f4953393f1f09d3d5a0923627f532c8ff1b8b85595ae9058503e3`; verify both Git blob IDs are `5c434b94040e8d9b18395a6098c4178401f2eb7d`.
5. Commit + push image files to Git `main` (or approved merging workflow), verify remotely.
6. **Only after remote image update**, synchronize all live references previously naming `CCBE315...`: `project-management/yura-visual/START_HERE.md`, `CURRENT_STATE.md`, `DECISIONS.md`, `WORKFLOW.md` where applicable, `tools/yura-master-benchmark/config.json`, `tools/yura-master-benchmark/CURRENT_HANDOFF.md`, `tools/yura-master-benchmark/PAID_ROUTE_STATUS.md`, runbooks/worklogs and other CURRENT operational text. Do not rewrite historical evidence as if it had been born under the new hash; retain provenance.
7. Rebuild/re-run the **non-billable** recovery preflight to verify consistency. Previously recorded `PREFLIGHT_OK` was for a **different** binary and Git commit: it does not attest to this new master.
8. Mark migration COMPLETED only when both Git image binaries and all active references/hashes are consistent. Until then, do **not** claim Git Master is already the new author-selected binary.

## 暫定運用ルール（最重要）

- **正しい作者指定原本は `07e265...` のPNG。**
- **Git上の旧 `CCBE315...` PNGは、原本同期が終わるまで不一致。**
- Gitの旧画像を「現行の作者指定原本」と誤認して新規生成に使用しない。
- 添付画像を使う場合はその場で実バイナリのSHA-256を検証する。
- 有料フルボディ再生成ルートは従来通り**凍結**。この作者指定は有料呼び出しやRunner設定の再許可ではない。
- Face/Ear/Text Authorities、17表情差分の感情定義には変更なし。

## Windows PowerShellでの実行例（ユーザーPC）

保存した原本PNGのファイルパスを `$src` に設定し、`C:\Dev\MEMORIELA` で以下を実行する。**元ファイルが本当に同一ハッシュであることを確認してからコピー**する。

```powershell
cd C:\Dev\MEMORIELA
git pull --ff-only origin main
$src = 'C:\PATH\TO\YURA_FULL_BODY_MASTER.png'
$expected = '07E26596642F4953393F1F09D3D5A0923627F532C8FF1B8B85595AE9058503E3'
if ((Get-FileHash -Algorithm SHA256 $src).Hash -ne $expected) { throw 'SOURCE HASH MISMATCH: STOP' }
Copy-Item -LiteralPath $src -Destination 'visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png' -Force
Copy-Item -LiteralPath $src -Destination 'visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png' -Force
Get-FileHash -Algorithm SHA256 'visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png'
Get-FileHash -Algorithm SHA256 'visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png'
git add visuals/yura/identity/master/YURA_FULL_BODY_MASTER.png visuals/yura/identity/body/YURA_FULL_BODY_MASTER.png
git commit -m "Restore author-designated original YURA Full-body Master binary"
git push origin main
```

After push, update ACTIVE docs/config as a distinct verified step, and then run non-billable preflight. Do not run paid generation.
