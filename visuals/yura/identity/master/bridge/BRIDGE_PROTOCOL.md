# YURA Visual Master Bridge Protocol

Status: **PROTECTED GIT PRODUCTION VISUAL-RECOVERY PATH**
Adopted: 2026-09-13
Updated: 2026-09-20 — Git-production-only routing restored
Purpose: GitHub connector が current canonical `visuals/yura/identity/master/VISUAL_MASTER.png` の存在・Git blob SHAを確認できてもPNG binaryを直接視覚入力へ渡せない環境で、Git current branchからYURAの視覚参照を復元する。

Parent operational protocol:

`visuals/yura/generation/VISUAL_ASSET_DISCOVERY_PROTOCOL.md`

Parent authorities:

- `visuals/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
- `visuals/yura/identity/master/VISUAL_MASTER.md`
- `YURA_START_HERE.md`

Canonical source remains the **current** artifact identified by `visuals/yura/identity/master/VISUAL_MASTER.md`.
This protocol never creates a second MASTER.

---

## 1. Role

Files under:

`docs/assistant-context/visual-identity/visual-master-bridge/`

are non-authoritative Git transport/cache derivatives of the current canonical PNG.

They exist only because some Git connector paths expose UTF-8 text but not repository image bytes as visual input.

Bridge previews:
- never become identity authority;
- never override protected domain specs;
- never remain usable merely because their filenames exist;

---

## 2. Mandatory dynamic integrity check

Do not trust any hardcoded “current MASTER SHA” written outside the current manifest.

Every recovery attempt must:

1. read `visuals/yura/identity/master/VISUAL_MASTER.md`;
2. obtain the current canonical repository path and current Git blob SHA;
3. read `visuals/yura/identity/master/bridge/MANIFEST.json`;
4. compare manifest `source.path` and `source.git_blob_sha1` with the current MASTER;
5. use the Bridge only when they match exactly.

If they do not match:

**BRIDGE = STALE / INVALID**

Do not decode or visually use stale previews.
Do not fall back to an older MASTER.
Production remains blocked until the Git Bridge is regenerated or direct current-Git visual inspection becomes available.

---

## 3. Recovery procedure

### Direct Git path available

When direct canonical Git image inspection works:

1. inspect the current canonical PNG directly;
2. Bridge recovery is unnecessary.

### Direct Git binary path unavailable

For ordinary neutral YURA production, the Bridge route requires **both FULL and PORTRAIT** previews.

1. complete the dynamic source-integrity check above;
2. fetch `FULL.jpg.b64.txt` as UTF-8 text;
3. concatenate its Base64 lines;
4. decode to JPEG;
5. verify decoded SHA-256 against the FULL preview entry in the manifest;
6. visually inspect the decoded FULL pixels;
7. fetch `PORTRAIT.jpg.b64.txt` as UTF-8 text;
8. concatenate its Base64 lines;
9. decode to JPEG;
10. verify decoded SHA-256 against the PORTRAIT preview entry in the manifest;
11. visually inspect the decoded PORTRAIT pixels;
12. only after both preview chains pass, mark production visual recovery `GIT_VERIFIED`;
13. apply protected BODY / FACE / EYE / HAIR / RENDERING owners for exact decisions.

Stopping after source-SHA match or Base64-file existence confirmation is a protocol violation.

FULL preview role:
- whole-character identity
- BODY balance
- hair mass / length impression
- overall silhouette / visual cross-check

PORTRAIT preview role:
- FACE
- EYE
- bangs
- upper-hair / face-framing cross-check

Micro-details that compression or crop cannot prove remain governed by protected text specs.

---

## 4. Failure behavior

Failure of the Bridge is not permission to:

- say only “画像は見られない”;
- generate from text memory;
- restore a deleted / superseded Git MASTER.

Instead:

1. identify the exact failure stage;
2. report whether the problem is source mismatch, fetch, decode, hash, or visual inspection;
3. keep production generation **BLOCKED**;
4. repair / regenerate the Git Bridge before resuming normal production.

User re-upload is not the standard production fallback.
A user-provided emergency visual override may be used only when the user explicitly authorizes that one-off exception; it does not replace Git canon.

---

## 5. Automatic regeneration

Builder:
`scripts/tools/visual/Build-YuraVisualMasterBridge.py`

Workflow:
`.github/workflows/yura-visual-master-bridge.yml`

The Bridge should be regenerated whenever the canonical MASTER changes.

Generated bridge files must not be hand-edited.

A bridge-generation failure must never allow an older bridge to stand in for the new current MASTER.

---

## 6. Operational invariant

Normal production recovery architecture:

**current Git MASTER manifest**
→ **current Git artifact identity**
→ direct visual inspection if available
→ otherwise **current source-SHA-matched Git Bridge**
→ FULL decode + hash + visual inspection
→ PORTRAIT decode + hash + visual inspection
→ **GIT_VERIFIED**
→ protected domain specs
→ generation / QA

**HARD GATE:** path / SHA / manifest / Base64 existence are provenance metadata only. Production generation remains blocked until actual Git-derived pixels have been decoded/recovered and visually inspected.
