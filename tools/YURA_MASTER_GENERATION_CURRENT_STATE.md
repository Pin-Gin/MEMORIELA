# YURA MASTER GENERATION — CURRENT STATE

Status: **ACTIVE / PRE-FIRST-SUCCESSFUL-RUN**

Last updated: **2026-10-04 JST**

This is an operational continuation note. It is **NOT** a YURA visual Authority and MUST NOT be used as an appearance source.

Read this together with:

- `tools/YURA_MASTER_GENERATION_WORKLOG.md`
- `tools/yura-master-benchmark/README.md`
- `tools/yura-master-benchmark/config.json`
- `tools/yura-master-benchmark/run_once.py`

## Current objective

Produce exactly one auditable YURA Master candidate first, measure the complete Codex + Image API cost, inspect QA, and only then decide whether to run 10 independent generations.

The one-run flow remains:

```text
current Git main
  -> Codex reads only approved Authorities in fixed order
  -> Codex discloses commit/read order/SHA-256
  -> Codex compiles exact image-generation prompt
  -> runner independently verifies manifest
  -> OpenAI Image API receives compiled prompt + approved Face/Body reference images
  -> result.png + usage/cost logs
  -> QA_PENDING
```

## OpenAI project/auth state

The user created a reusable benchmark OpenAI Project named approximately:

```text
creator-master-benchmark
```

The local PowerShell session has:

```text
OPENAI_API_KEY = set
OPENAI_PROJECT_ID = set
```

Codex CLI was installed and verified:

```text
codex-cli 0.160.0
```

Codex authentication was switched from ChatGPT login to API-key login successfully:

```text
Logged in using an API key
```

Do not expose or commit the actual key.

## Local repository state before the failed run

Local HEAD and origin/main were confirmed equal at:

```text
4cf7f6942a885aa028a1d8c35b0c483a3d6155af
Add YURA master generation worklog handoff
```

The only unrelated unstaged local change was:

```text
manuscript/episode-001/EP001_DRAFT.txt
```

That draft must remain untouched by YURA visual work.

Preflight passed:

- `openai` Python package = `3.24.0`
- `run_once.py` py_compile PASS
- `run_batch.py` py_compile PASS
- `query_project_cost.py` py_compile PASS
- `config.json` parse PASS
- Face reference exists
- Body Geometry Guide exists
- Composition Authority exists
- `YURA_VISUAL_TEXT.md` exists
- Codex API-key login PASS

## First attempted `run_once.py` result

One attempt was made:

```powershell
python tools/yura-master-benchmark/run_once.py
```

It stopped at the Codex Authority-resolution stage with:

```text
Codex reported ready=false:
Cannot complete requested verification because filesystem is read-only and shell access is unavailable for retrieving `git rev-parse HEAD` and reading required authority files.
```

Important interpretation:

```text
Codex started
  -> could not use the Windows shell inside the selected sandbox
  -> returned ready=false
  -> runner stopped
  -> Image API was NOT called
```

Therefore no image-generation charge was incurred by that attempt.

A small Codex API charge may still have occurred because Codex produced the `ready=false` response. Include this failed attempt when later inspecting Project-level cost if exact experiment accounting is desired.

Do NOT count this failed attempt as a completed benchmark image run.

## Sandbox diagnosis

A no-model Windows sandbox probe was executed:

```powershell
codex sandbox -c 'windows.sandbox="elevated"' -- git rev-parse HEAD
```

It succeeded and returned:

```text
4cf7f6942a885aa028a1d8c35b0c483a3d6155af
```

This demonstrated that the native Windows elevated sandbox can execute the required Git read command on this machine.

The intended security posture is:

```text
Codex filesystem policy = read-only
Windows sandbox backend = elevated
repository write access = NOT granted
```

Do not replace this with `danger-full-access` merely to make the benchmark work.

## Runner fix now committed

`tools/yura-master-benchmark/run_once.py` was updated remotely so that Codex is launched explicitly with:

```text
--sandbox read-only
-c windows.sandbox="elevated"
```

The run metadata now also records:

```json
{
  "codex_sandbox": {
    "mode": "read-only",
    "windows_backend": "elevated"
  }
}
```

If Codex returns `ready=false`, the runner now writes `failure.json` with:

```text
phase = codex_authority_resolution
image_api_called = false
```

The runner-fix commit is:

```text
c639e814d17e24f3457600b2293e7ca72460cbb1
Fix Codex Windows read-only sandbox for YURA benchmark
```

This current-state note is committed after that fix, so always resolve the latest `origin/main` rather than pinning blindly to `c639e81`.

## Exact next step

Do **not** rerun from the old local commit.

First safely sync current main while preserving the unrelated novel draft:

```powershell
git stash push -m "WIP EP001 before YURA sandbox-fix sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Then verify:

```powershell
git log -1 --oneline
git status --short
python -m py_compile tools/yura-master-benchmark/run_once.py
codex login status
```

Expected conditions:

- local HEAD == origin/main
- only `manuscript/episode-001/EP001_DRAFT.txt` is dirty
- `run_once.py` compiles
- Codex is still logged in using the benchmark API key
- `OPENAI_API_KEY` and `OPENAI_PROJECT_ID` remain set in the current PowerShell session

Only after those checks should the user run exactly one more attempt:

```powershell
python tools/yura-master-benchmark/run_once.py
```

If it errors again, do not retry automatically. Preserve the terminal output and run artifacts for diagnosis.

If it succeeds, inspect the generated run directory before any batch execution.

## After the first successful image run

Inspect at minimum:

- `authority_manifest.json`
- `compiled_prompt.txt`
- `compiled_prompt.sha256`
- `codex_trace.jsonl`
- `codex_usage_candidates.json`
- `image_response.json`
- `cost.json`
- `qa.json`
- `result.png`

Then obtain Project-level authoritative cost using the documented cost-query flow. If an Organization Admin key is used for automated cost querying, never commit or expose it.

Do not run the 10-run batch until:

1. Authority resolution is correct.
2. Prompt compilation is correct.
3. Image generation succeeds.
4. One-run cost is acceptable.
5. The user explicitly approves proceeding with the batch.

## Architecture decisions that remain unchanged

- Face Reference controls Face Identity only.
- Body Geometry Guide controls 7.2-head body geometry only.
- Composition Authority controls canvas/occupancy/margins/centering only.
- `YURA_VISUAL_TEXT.md` is currently the Master-generation API specification.
- Novel material, Memory-derived appearance, old Git visual history, old Masters, and rejected generated images are denied as fallback sources.
- Failed generated candidates are never fed back as correction references.
- Master promotion requires explicit author approval.
- After Master approval, create `YURA_MASTER_VISUAL_DESCRIPTION.md` by visually inspecting the approved Master, switch normal Production to Master + Master-derived description, and archive the Master-generation package outside normal auto-load.
