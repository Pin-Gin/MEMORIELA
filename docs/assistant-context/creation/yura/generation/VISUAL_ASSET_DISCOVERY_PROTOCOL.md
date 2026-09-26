# YURA Visual Asset Discovery Protocol

Status: **CANONICAL / MANDATORY GIT VISUAL-RECOVERY PROTOCOL**
Adopted: 2026-09-20
Updated: 2026-09-20 — Git recovery + reference/pixel preservation gates
Applies to: YURA protected visual MASTERs and any YURA production task whose identity depends on a protected visual reference.

Parent authority:
`docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`

Canonical neutral MASTER manifest:
`docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`

Canonical Git transport fallback:
`docs/assistant-context/creation/yura/identity/master/bridge/BRIDGE_PROTOCOL.md`

Purpose: 新規チャットや別コンテキストでも、YURAのproduction visualをcurrent Git branchから復元し、実画像を視覚確認してから生成する。

---

## 1. Absolute production rule

Before material YURA production generation:

1. resolve the exact current visual authority from Git;
2. visually recover that current Git authority;
3. actually inspect recovered pixels;
4. apply current protected domain owners;
5. only then generate.

Do not reconstruct YURA from chat memory, arbitrary derivatives, or deleted / superseded revisions.

A Git filename, gen_id, blob SHA, manifest match, or Base64-file existence check is metadata only.
It is not visual inspection.

---

## 2. Mandatory recovery state

For a protected YURA visual MASTER/reference, use these states:

1. `UNRESOLVED` — current Git artifact not yet identified
2. `IDENTIFIED` — current Git path / metadata resolved, but no pixels recovered
3. `GIT_PIXELS_RECOVERED` — actual pixels recovered directly from Git or from a current Git-declared SHA-matched Bridge
4. `GIT_PIXELS_INSPECTED` — recovered pixels actually visually inspected
5. `GIT_VERIFIED` — inspected pixels are tied to the current Git authority by direct canonical retrieval or verified Git Bridge provenance
6. `REFERENCE_INPUT_GUARANTEED` — the imminent generator call is verified to use only approved current-MASTER identity reference(s), with every other reference role-isolated or excluded
7. `PROTECTED_PIXEL_PRESERVATION_GUARANTEED` — when exact-preservation mode applies, the imminent operation is verified to preserve every non-authorized protected pixel exactly

**Production image generation requires `REFERENCE_INPUT_GUARANTEED`.**
`REFERENCE_INPUT_GUARANTEED` may only be reached after `GIT_VERIFIED`.
When the request requires exact unchanged protected regions, production additionally requires `PROTECTED_PIXEL_PRESERVATION_GUARANTEED`.

The following do not satisfy the gate:

- current filename found;
- gen_id found;
- Git blob SHA found;
- Bridge manifest found;
- Bridge source SHA matched;
- FULL / PORTRAIT Base64 files found;
- dimensions / byte size read;
- textual MASTER description read;
- assistant memory of an earlier MASTER.

Before any production image-generation tool call:

- if visual recovery state != `GIT_VERIFIED`, **DO NOT GENERATE**;
- continue the Git recovery procedure;
- if Git recovery fails, return **`BLOCKED — GIT VISUAL MASTER NOT VERIFIED`**;
- after `GIT_VERIFIED`, run the reference-input preflight defined by `docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`;
- if the imminent tool call cannot guarantee approved identity-reference routing, return **`BLOCKED — REFERENCE INPUT NOT GUARANTEED`**;
- only set final state = `REFERENCE_INPUT_GUARANTEED` immediately before a tool call whose reference inputs satisfy that preflight;
- if exact-preservation mode applies, continue through `docs/assistant-context/creation/yura/generation/preservation/PIXEL_PRESERVATION_PROTOCOL.md`;
- if immutable protected pixels cannot be guaranteed unchanged, return **`BLOCKED — PROTECTED PIXELS CANNOT BE GUARANTEED`**.

---

## 3. Resolve the exact current Git target

For the neutral MASTER read:

1. `YURA_START_HERE.md`
2. `docs/assistant-context/creation/yura/generation/IMAGE_GENERATION_GOVERNANCE.md`
3. `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.md`
4. current task-specific protected owner / sub-spec as needed

Capture current metadata when available:

- canonical repository path;
- generation / source id;
- Git blob SHA;
- exported SHA-256;
- dimensions / byte size;
- authority role;
- current status.

Always resolve current values dynamically from the current Git authority.

---

## 4. Production visual recovery order

### Route A — direct current Git visual

If the environment can visually retrieve the current canonical repository PNG:

1. retrieve the current Git artifact;
2. verify it is the artifact identified by the current manifest;
3. visually inspect the pixels;
4. set state = `GIT_VERIFIED`.

### Route B — current Git Bridge

If direct repository-image inspection is unavailable:

1. read `docs/assistant-context/creation/yura/identity/master/bridge/BRIDGE_PROTOCOL.md`;
2. read the current Bridge manifest;
3. compare Bridge `source.path` and `source.git_blob_sha1` to the current MASTER;
4. use the Bridge only on exact source match;
5. fetch the FULL Base64 text from Git;
6. decode it to actual image pixels;
7. verify decoded hash against the Bridge manifest;
8. visually inspect the FULL pixels;
9. fetch the PORTRAIT Base64 text from Git;
10. decode it to actual image pixels;
11. verify decoded hash against the Bridge manifest;
12. visually inspect the PORTRAIT pixels;
13. set state = `GIT_VERIFIED` only after all required checks pass.

For ordinary neutral whole-character production, both FULL and PORTRAIT are mandatory.

Bridge metadata existence without decode + hash verification + visual inspection is incomplete and generation remains blocked.

---

## 5. Git Bridge authority boundary

The Bridge is a Git transport/cache derivative, not a second MASTER.

Authority remains:

**current Git `docs/assistant-context/creation/yura/identity/master/VISUAL_MASTER.png`**
+ **current protected BODY / FACE / EYE / HAIR / RENDERING owners**

The Bridge exists only to recover observable pixels when the Git connector cannot expose the canonical PNG directly.

Where preview resolution cannot prove an exact micro-detail, the protected text owner remains authoritative.

---

## 5A. Post-recovery reference-input gate

`GIT_VERIFIED` is a visual-recovery result, not permission by itself to call the generator.

After Git verification and immediately before each generation / retry:

1. identify the approved current-MASTER identity source(s);
2. enumerate every image that the execution surface may supply or auto-select;
3. assign non-identity references an explicit role;
4. confirm generated outputs / rejected candidates / historical derivatives are not identity inputs;
5. use reliable explicit tool-native binding when the surface supports it;
6. if automatic selection or other execution behavior prevents verification that identity inputs are restricted to the approved current MASTER, stop;
7. set `REFERENCE_INPUT_GUARANTEED` only for the specific imminent call.

The gate is **per tool call**. It must be rerun for every retry even inside the same chat.

Generated candidates remain QA evidence / rollback candidates only unless the user explicitly assigns a non-identity derivative role. They never become YURA identity authority without protected Git promotion.

---

## 6. Production failure behavior

If direct Git inspection fails and the current Git Bridge is:

- missing;
- stale;
- source-SHA mismatched;
- corrupt;
- undecodable;
- decoded-hash mismatched;
- or not visually inspectable;

then state remains below `GIT_VERIFIED`.

Required behavior:

1. stop production generation;
2. report the exact Git artifact requested;
3. report current manifest identity;
4. report which Git recovery stage failed;
5. repair the Git production transport before resuming generation.

Do not substitute an older Git revision.

---

## 7. Other protected visual MASTERs

For a protected hairstyle MASTER / room MASTER / other protected Git visual artifact:

1. resolve the current Git manifest/spec first;
2. use direct current Git visual inspection when supported;
3. otherwise use only a current Git-declared verified transport if one exists;
4. if no production transport exists, report a specific **Git transport gap** and block that MASTER-dependent production task.

---

## 8. New-chat invariant

For YURA production generation:

**current Git authority**
→ **current Git visual artifact identity**
→ direct Git visual if possible
→ otherwise **current SHA-matched Git Bridge**
→ FULL decode + hash verification + visual inspection
→ PORTRAIT decode + hash verification + visual inspection
→ **GIT_VERIFIED**
→ reference-input preflight
→ **REFERENCE_INPUT_GUARANTEED**
→ exact-preservation trigger check
→ **PROTECTED_PIXEL_PRESERVATION_GUARANTEED** when applicable
→ protected domain specs
→ generation / edit
→ exact unchanged-region pixel verification when applicable
→ QA

A new chat must complete this chain before production generation.

---

## 9. Change-control invariant

Any future change to production visual recovery must preserve:

- Git current branch as production identity authority;
- dynamic current-source verification;
- actual pixel inspection before production generation;
- no deleted / superseded revision recovery during ordinary generation.

If a proposed convenience path weakens these guarantees, do not adopt it.
