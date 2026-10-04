# YURA MASTER GENERATION — CURRENT STATE

Status: **ACTIVE / SEALED-BUNDLE PREFLIGHT PENDING**

Last updated: **2026-10-04 JST**

This file is an operational continuation note. It is **NOT** a YURA visual Authority and MUST NOT be used as an appearance source.

Read together with:

- `tools/YURA_MASTER_GENERATION_WORKLOG.md`
- `tools/yura-master-benchmark/README.md`
- `tools/yura-master-benchmark/config.json`
- `tools/yura-master-benchmark/codex_instruction.md`
- `tools/yura-master-benchmark/run_once.py`

---

## 1. Current objective

Produce exactly one auditable YURA Master candidate first, measure the complete Codex + Image API cost, inspect QA, and only then decide whether to run 10 independent generations.

The author-approved visual Authority architecture is unchanged.

The current work is only about making the benchmark execution path reproducible and removing an unreliable Codex-local-tool dependency.

---

## 2. OpenAI / local environment state already verified

Known working state before the latest runner redesign:

```text
Python: 3.12
openai Python SDK: 3.24.0
Codex CLI: 0.160.0
Codex auth: API key
OPENAI_API_KEY: set in current PowerShell session
OPENAI_PROJECT_ID: set in current PowerShell session
```

The benchmark Project is intended to be a reusable creator/master benchmark project rather than YURA-only; the chosen name is approximately:

```text
creator-master-benchmark
```

Never commit or expose the actual API key.

---

## 3. Novel-side local change remains protected

The user's unrelated local draft remains:

```text
manuscript/episode-001/EP001_DRAFT.txt
```

This file must not be modified, discarded, committed, reset, or used as YURA visual input.

Safe sync pattern:

```powershell
git stash push -m "WIP EP001 before YURA benchmark sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Do not use `git reset --hard` or force push.

---

## 4. Two Codex-only benchmark attempts have failed before Image API

### Attempt 1

The first `run_once.py` attempt stopped because Codex reported that it could not retrieve `git rev-parse HEAD` or read Authority files under the available Windows tool environment.

Interpretation:

```text
Codex request started
  -> local tool/file verification unavailable to model
  -> ready=false
  -> runner stopped
  -> Image API NOT called
```

A Windows sandbox probe then showed that this machine itself can execute Git successfully with:

```powershell
codex sandbox -c 'windows.sandbox="elevated"' -- git rev-parse HEAD
```

The probe returned the expected commit, proving the host sandbox command path itself was viable.

### Attempt 2

After explicitly configuring read-only + Windows elevated sandbox, a second `run_once.py` attempt still stopped at Codex compile/Authority resolution.

Latest failed run directory reported locally:

```text
tools/yura-master-benchmark/runs/run_20261004T061634Z
```

`failure.json` recorded:

```text
phase = codex_authority_resolution
ready = false
image_api_called = false
```

The model response again stated that filesystem/tool execution was unavailable.

The JSONL trace is important:

```text
thread.started
configuration warnings/errors
turn.started
agent_message ready=false
turn.completed
```

There was **no shell/tool call item** between `turn.started` and the agent response.

Observed Codex usage for this second failed attempt:

```text
input_tokens  = 12823
output_tokens = 159
```

Therefore a small Codex API charge may exist, but there was no image-generation charge.

### Important accounting fact

Across these two failed attempts:

```text
successful image benchmark runs = 0
Image API generation calls that reached generation = 0
Codex API attempts = 2
```

Do not count either failed attempt as the one successful seed run.

---

## 5. Diagnostics from attempt 2

`codex_stderr.log` showed failed MCP transport attempts to:

```text
http://127.0.0.1:8080/mcp
```

The trace also reported:

```text
features.rmcp_client is unrecognized/ignored
configured service tier priority is not advertised for gpt-5.3-codex
model metadata for gpt-5.3-codex not found; fallback metadata used
```

The user's `~/.codex/config.toml` contains Windows sandbox/trust configuration and unrelated local runtime configuration.

Conclusion:

The benchmark should not depend on the model being able to use the user's local Codex filesystem/shell/MCP environment at all.

Repeated paid retries with different local tool flags would add cost without improving experimental isolation.

---

## 6. Architecture decision: SEALED AUTHORITY BUNDLE

The benchmark has now been redesigned.

Old path:

```text
Git
  -> Codex tries to run Git/read files itself
  -> Codex compiles prompt
```

New path:

```text
Git working copy
  -> Python runner verifies HEAD == origin/main
  -> Python runner checks configured Authority paths are clean
  -> Python runner reads ONLY configured Authority files
  -> Python runner computes SHA-256 locally
  -> Python runner embeds complete text Authority contents
  -> Python runner records PNG path/hash/declared role metadata
  -> sealed_authority_bundle.json
  -> Codex receives instruction + sealed bundle directly via stdin
  -> Codex compiles manifest + generation prompt WITHOUT filesystem/shell/MCP
  -> runner re-verifies manifest against local facts
  -> only then Image API may receive the actual Face + Body PNG files
```

This is a stronger audit boundary, not a relaxation.

Forbidden sources such as:

```text
characters/YURA.md
story/**
manuscript/**
Git history / old branches / old YURA visual files
Memory-derived appearance
rejected/past generations not explicitly active
```

are not included in the sealed Codex input.

Codex cannot use them as fallback if they are not supplied.

---

## 7. PNG handling in sealed mode

Codex does not need to visually inspect the PNGs during prompt compilation.

The sealed bundle contains deterministic metadata for them:

```text
YURA_FACE_REFERENCE.png
  role = FACE IDENTITY ONLY
  SHA-256 = runner-computed

YURA_BODY_GEOMETRY_GUIDE.png
  role = BODY GEOMETRY ONLY
  SHA-256 = runner-computed
```

The actual binary image files are passed directly by Python to the Image API only after the Codex manifest passes verification.

This preserves the Authority split:

```text
Face image -> Face Identity only
Body guide image -> Body Geometry only
```

---

## 8. Codex compile isolation

`run_once.py` now invokes Codex using a sealed prompt on stdin and:

```text
--ignore-user-config
--sandbox read-only
```

The compile instruction explicitly says:

```text
filesystem access = unnecessary
shell access = unnecessary
Git access = unnecessary
MCP/external tools = unnecessary
```

Codex must not return `ready=false` merely because those tools are unavailable.

`--ignore-user-config` is intentional: benchmark compile should not inherit unrelated MCP endpoints, experimental feature flags, local notification hooks, or other user configuration.
Authentication remains separate from ignored user configuration.

---

## 9. Model condition intentionally NOT changed yet

The filesystem/tool architecture was changed, but the configured Codex model is intentionally left unchanged for the next controlled comparison:

```text
gpt-5.3-codex
```

Reason:

Changing the model and the input architecture simultaneously would make the next result ambiguous.

First isolate whether sealed-input compilation fixes the failure mode.
Only after that should a model migration be treated as a separate benchmark condition and committed explicitly.

The Image model/config is also unchanged in this redesign.

---

## 10. Files changed for sealed-bundle mode

### `tools/yura-master-benchmark/codex_instruction.md`

Changed from "Codex must resolve Git/read repository files" to:

```text
Use ONLY the sealed Authority bundle supplied in the prompt.
Do not call tools.
Do not independently read Git/filesystem.
Do not fail because local tools are absent.
```

Relevant commit:

```text
c65c4e5fbcc487ebed6500045554a3780889ee9c
Switch YURA Codex compile to sealed authority bundle
```

### `tools/yura-master-benchmark/run_once.py`

Now:

- verifies Git/Authority locally
- computes SHA-256 locally
- builds `sealed_authority_bundle.json`
- writes `sealed_authority_bundle.sha256`
- writes `codex_input.sha256`
- sends the complete compile input to `codex exec` through stdin
- uses `--ignore-user-config`
- keeps sandbox read-only as defense in depth
- verifies ordinal/path/role/SHA/denied_sources/image-reference order
- calls Image API only after manifest verification

Initial sealed-mode runner commit:

```text
379741c2f0aebed0de1ff489d49f95eb6569c7f0
Feed Codex a sealed YURA authority bundle
```

### Free preflight mode

A later runner update added:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

This performs local Git/Authority verification and sealed-bundle construction, writes hashes, and exits with:

```text
paid_model_calls = 0
```

It does **not** call Codex and does **not** call Image API.

Relevant commit:

```text
ca30958c071150d6d1afcbf64860331d881af48f
Add free sealed-bundle preflight mode
```

### README

Benchmark documentation was updated to describe sealed mode.

Relevant commit:

```text
86e09d2d5da37294d38625b3e3f53fc17bbcfe0a
Document sealed authority bundle benchmark flow
```

This CURRENT_STATE commit comes after those changes; always sync latest `origin/main` instead of pinning to one of the intermediate SHAs above.

---

## 11. Exact next step — NO paid model call yet

The user's local repository was last synchronized before the sealed-mode commits, so first preserve the unrelated novel draft and pull latest main:

```powershell
git stash push -m "WIP EP001 before sealed YURA benchmark sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Then verify:

```powershell
git log -1 --oneline
git status --short
python -m py_compile tools/yura-master-benchmark/run_once.py
```

Expected working-tree condition:

```text
only manuscript/episode-001/EP001_DRAFT.txt is dirty
```

Then run the **free preflight only**:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Expected terminal payload includes:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
authority_count = 7
sealed_authority_bundle_sha256 = ...
codex_input_sha256 = ...
```

Do not run the paid form yet if this preflight fails.

---

## 12. After free preflight passes

Inspect the created preflight run directory:

```text
run_meta.json
sealed_authority_bundle.json
sealed_authority_bundle.sha256
codex_input.sha256
```

Confirm:

- commit is current main
- seven Authority entries are present in exact configured order
- only approved text Authority contents are embedded
- PNG entries contain metadata/role/hash, not arbitrary fallback content
- denied sources list is correct
- no `characters/YURA.md` / manuscript / old-history content leaked into the bundle

Only then consider exactly one paid run:

```powershell
python tools/yura-master-benchmark/run_once.py
```

If the paid run errors, do not automatically retry. Preserve terminal output and run artifacts.

---

## 13. Success criteria for the next paid run

The next paid run is successful only if:

```text
1. local Git validation PASS
2. sealed bundle created
3. Codex receives sealed input without requiring tools
4. Codex returns ready=true
5. manifest commit/order/roles/SHA/denied sources/reference order PASS runner verification
6. compiled_prompt is saved and hashed
7. Image API returns exactly one candidate
8. result remains QA_PENDING / master_promotion=NO
9. usage/cost artifacts are saved
```

The first two failed Codex-only attempts remain diagnostic overhead, not successful seed runs.

---

## 14. What must NOT happen

Do not:

- retry paid Codex merely to test flags
- re-enable repository-wide Codex exploration
- feed rejected generated YURA images back as references
- use novel/manuscript/Memory as visual fallback
- silently change `gpt-5.3-codex` during the sealed-input diagnosis
- silently change the Image model or endpoint
- run the 10-generation batch before one complete successful run and cost inspection
- auto-promote any generated candidate to Master
- touch or lose `EP001_DRAFT.txt`

---

## 15. Short resume instruction

```text
YURA Authority architecture is already established.
Two Codex-only attempts failed before Image API because local tool/filesystem access was not available to the model.
Image generation count is still zero.
The benchmark has now switched to SEALED AUTHORITY BUNDLE mode: Python verifies Git/files/hashes and passes only approved Authority data to Codex via stdin; Codex must not use local tools.
The Codex model remains gpt-5.3-codex for controlled diagnosis.
Next: sync latest main safely, py_compile run_once.py, then run --preflight-only. That preflight must report paid_model_calls=0 before any further paid run is considered.
```
