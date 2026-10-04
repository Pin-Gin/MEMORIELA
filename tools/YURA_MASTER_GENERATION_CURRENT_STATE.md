# YURA MASTER GENERATION — CURRENT STATE

Status: **ACTIVE / FIRST SEALED RUN COMPLETE / PRECEDENCE FIX COMMITTED**

Last updated: **2026-10-04 JST**

This file is an operational continuation note. It is **NOT** a YURA visual Authority and MUST NOT be used as an appearance source.

Read together with:

- `tools/YURA_MASTER_GENERATION_WORKLOG.md`
- `tools/yura-master-benchmark/README.md`
- `tools/yura-master-benchmark/config.json`
- `tools/yura-master-benchmark/codex_instruction.md`
- `tools/yura-master-benchmark/run_once.py`
- the active Authority files listed by `config.json`

---

## 1. Current objective

Produce a reproducible, auditable YURA full-body Master candidate from explicitly separated Face / Body Geometry / Composition / Master-generation Authorities.

The benchmark exists to answer:

```text
Which exact Git commit was used?
Which exact Authorities were used and in what order?
Were their SHA-256 values verified?
Was the Codex compiled prompt stable?
What did one complete run cost?
Did the image pass Body Geometry / Composition / Face Identity QA?
```

Do not promote any generated image automatically.

---

## 2. Novel-side isolation remains mandatory

The unrelated local draft is:

```text
manuscript/episode-001/EP001_DRAFT.txt
```

It must not be modified, discarded, committed, reset, or used as YURA visual input.

Safe sync pattern:

```powershell
git stash push -m "WIP EP001 before YURA benchmark sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Do not use `git reset --hard` or force push.

Visual fallback remains denied from:

```text
characters/YURA.md
story/**
manuscript/**
Git history / old branches / old YURA visual files
Memory-derived appearance
past/rejected generated YURA images unless explicitly promoted to active Authority
```

---

## 3. OpenAI / local environment already verified

Known working setup:

```text
Python: 3.12
openai Python SDK: 3.24.0
Codex CLI: 0.160.0
Codex auth: API key
OPENAI_API_KEY: set in PowerShell session when benchmark was run
OPENAI_PROJECT_ID: set in PowerShell session when benchmark was run
```

Benchmark Project name is approximately:

```text
creator-master-benchmark
```

Never commit or expose the actual API key.

---

## 4. Two initial Codex-only attempts failed before Image API

Before sealed-bundle mode, two paid Codex attempts failed because the model did not receive usable local filesystem/shell/tool execution.

Important accounting:

```text
failed Codex-only attempts = 2
image generations from those attempts = 0
```

The second failed attempt showed no shell/tool call in the JSONL trace. It also showed unrelated local MCP/config warnings. This established that the benchmark should not depend on Codex local-tool availability.

Those attempts are diagnostic overhead, not successful image benchmark runs.

---

## 5. SEALED AUTHORITY BUNDLE architecture

The benchmark was redesigned so Python, not Codex, owns Git/file verification.

Current flow:

```text
Git working copy
  -> Python verifies HEAD == origin/main
  -> Python checks configured Authority paths are clean
  -> Python reads ONLY configured Authority files
  -> Python computes SHA-256
  -> Python embeds text Authorities + PNG metadata into sealed_authority_bundle.json
  -> Codex receives only instruction + sealed bundle through stdin
  -> Codex compiles manifest + Image API prompt without filesystem/shell/MCP
  -> Python re-verifies commit/order/role/SHA/denied sources/reference order
  -> Python verifies required compiled-prompt invariants
  -> only then Image API may run
```

Codex is invoked with user config ignored so unrelated MCP/local configuration does not enter the benchmark compile step.

PNG handling remains separated:

```text
YURA_FACE_REFERENCE.png -> FACE IDENTITY ONLY
YURA_BODY_GEOMETRY_GUIDE.png -> BODY GEOMETRY ONLY
```

Codex receives PNG path/hash/role metadata during prompt compilation; the actual PNG files are passed directly to the Image API later.

---

## 6. Free sealed preflight succeeded

A free preflight was executed from commit:

```text
eafdb033c3fc9b19ce69fd2a8223ebea85bf3779
```

Observed result:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
authority_count = 7
sealed_authority_bundle_sha256 = f19e574677ee05afed1282fc4f5a61bb7f44ff9d538b472d9ebb7bd74d747e4a
codex_input_sha256 = 77c2de140bc4d0f173ecb26378cb6db58f96ec30af00eeb51f43873291a7eb6a
```

This proved the local Git/Authority/hash/bundle path without spending on Codex or Image API.

---

## 7. First complete sealed paid run succeeded technically

After the free preflight, `run_once.py` completed through Codex compile and Image API generation.

This was the first successful end-to-end image benchmark run.

The Image API response reported:

```text
size = 1440x2560
quality = high
background = opaque
output_format = png
input_tokens = 3406
  image_tokens = 2004
  text_tokens = 1402
output_tokens = 1843
```

The actual saved PNG was independently checked locally with `System.Drawing` and confirmed:

```text
RESULT_SIZE = 1440x2560
```

Therefore canvas size handling was correct. A previous visual inspection of a chat/UI copy that appeared to be 1152×2048 was only a display/downscaled copy and must not be treated as the original API output size.

Image-only estimated cost stored by the runner:

```text
$0.078332
```

Codex usage candidates for the successful run:

```text
input_tokens = 20025
cached_input_tokens = 1408
output_tokens = 2116
reasoning_output_tokens = 0
```

`authoritative_total_project_cost_usd` is still unset until Project cost is queried with the appropriate admin credentials/tooling.

---

## 8. First generated candidate is NOT approved Master

The generated image exists and is visually useful, but it is not approved for Master promotion.

Author observation:

```text
overall figure looks too long / vertically stretched
```

The candidate therefore requires formal Body Geometry and Composition QA and must remain:

```text
candidate = QA_PENDING
master_promotion = NO
```

Do not feed this candidate back as a future generation reference.

---

## 9. Compiled prompt inspection found a precedence weakness

The successful run's `authority_manifest.json` correctly recorded:

- ready=true
- exact Git commit
- seven Authority entries
- exact Authority order
- exact SHA-256 values
- denied-source list
- Face then Body image-reference order

The compiled prompt correctly included the main 7.2-head, body, composition, canvas, occupancy, margin, face/reference-separation constraints.

However, it did not preserve a sufficiently explicit conflict-precedence rule such as:

```text
BODY GEOMETRY IS RESOLVED FIRST.
BODY GEOMETRY HAS PRIORITY OVER COMPOSITION.
BODY GEOMETRY WINS; COMPOSITION MAY FAIL.
```

The older wording said Composition must not change Body Geometry, but did not force Codex to preserve an explicit resolution order if the model perceived Body Geometry and Composition as difficult to satisfy simultaneously.

---

## 10. UTF-8 prompt integrity was verified

PowerShell `Get-Content` displayed mojibake for characters such as `×` and en-dashes, but the underlying compiled prompt file was confirmed to be valid UTF-8.

A Python check returned:

```text
canvas_ok = True
occupancy_ok = True
ear_ok = True
head_ratio_dash_ok = True
mojibake_present = False
```

Therefore the successful Image API call did not receive a corrupted prompt. The visible PowerShell mojibake was only console decoding/display behavior.

---

## 11. Authority/compiler/runner precedence fix now committed

The next benchmark condition strengthens precedence without using the failed candidate as a reference.

### Composition Authority

`visuals/yura/identity/composition/YURA_COMPOSITION_AUTHORITY.md` now explicitly states:

```text
BODY GEOMETRY IS RESOLVED FIRST.
BODY GEOMETRY HAS PRIORITY OVER COMPOSITION.
WHOLE-FIGURE UNIFORM SCALING ONLY.
DO NOT ALTER INTERNAL BODY LANDMARK POSITIONS TO SATISFY OCCUPANCY OR MARGINS.
BODY GEOMETRY WINS; COMPOSITION MAY FAIL.
```

It also states that Composition may move/uniformly scale only the already-proportioned complete figure and must not independently alter head, neck, torso, waist, leg, knee, ankle, or other internal landmark distances.

Relevant commit:

```text
afb44312f512fd8c22f961701c8bd31dcb9a2d8e
Make body geometry precedence explicit in YURA composition authority
```

### Codex compiler instruction

`tools/yura-master-benchmark/codex_instruction.md` now requires that exact precedence block verbatim in every compiled Image API prompt and requires literal retention of:

```text
7.2 heads
7.1–7.3
1440 × 2560
89%
88–90%
5–6%
```

Relevant commit:

```text
14bac9685b386b92e08c43936351cdc931795ed9
Require YURA body geometry precedence block in compiled prompt
```

### Runner hard gate

`tools/yura-master-benchmark/run_once.py` now verifies the required compiled-prompt invariants before any Image API request.

It writes:

```text
prompt_invariant_check.json
```

If any required phrase/value is missing:

```text
phase = compiled_prompt_invariant_check
image_api_called = false
```

and generation stops before Image API spend.

Relevant commit:

```text
6c400994973e5cad3c7c0155c17c9945e884770a
Gate YURA image generation on compiled prompt invariants
```

---

## 12. Model condition remains unchanged

For controlled comparison, the benchmark still uses the same configured Codex and Image models as the previous successful sealed run.

Do not silently migrate models at the same time as testing the precedence fix. A model change should be a separate committed benchmark condition.

---

## 13. Exact next step

The local working copy will be behind the commits above. Preserve the unrelated novel draft and sync latest main:

```powershell
git stash push -m "WIP EP001 before YURA precedence-fix sync" -- manuscript/episode-001/EP001_DRAFT.txt
git pull --rebase origin main
git stash pop
```

Then verify:

```powershell
git log -1 --oneline
git status --short
python -m py_compile tools/yura-master-benchmark/run_once.py
```

Expected dirty file remains only:

```text
manuscript/episode-001/EP001_DRAFT.txt
```

Then run the FREE preflight again because the Authority and compiler inputs changed:

```powershell
python tools/yura-master-benchmark/run_once.py --preflight-only
```

Expected:

```text
status = PREFLIGHT_OK
paid_model_calls = 0
authority_count = 7
```

The sealed bundle and Codex input hashes should differ from the previous run because Composition Authority and compiler instruction changed. That is expected and represents a new explicit benchmark condition.

Do not start a 10-run batch.

Before another paid image generation, inspect/record the first successful run cost as far as available and confirm the new free preflight passes.

---

## 14. What must NOT happen

Do not:

- use the first generated candidate as a correction reference
- modify face identity merely to fix full-body geometry
- deform body landmarks to hit Composition occupancy
- silently change model IDs while evaluating the precedence fix
- run 10 generations before one corrected single-run result and cost review
- use novel/manuscript/Memory/old visual history as fallback
- auto-promote any candidate to Master
- touch or lose `EP001_DRAFT.txt`
- expose API/Admin keys

---

## 15. Short resume instruction

```text
YURA Authority architecture is established and the benchmark now uses SEALED AUTHORITY BUNDLE mode.
Two early Codex-only attempts failed before Image API; then a free sealed preflight passed and the first complete sealed paid run succeeded technically.
The saved API image is truly 1440×2560. The author judged the figure too long/vertically stretched, so the candidate remains QA_PENDING and must not be reused as a reference.
Compiled prompt UTF-8 integrity was verified; PowerShell mojibake was display-only.
A weakness was found in conflict precedence: the prompt did not force BODY Geometry to win over Composition.
Composition Authority, Codex compiler instruction, and run_once.py have now been strengthened with an exact BODY-GEOMETRY-first precedence block and a runner invariant gate that stops before Image API if required phrases/numbers are missing.
Next: safely sync latest main while preserving EP001_DRAFT.txt, py_compile run_once.py, run --preflight-only (paid_model_calls=0), then review first-run cost before considering exactly one corrected paid run.
```
