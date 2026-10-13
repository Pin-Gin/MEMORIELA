# Codex Instruction — YURA Text-Only Validation / FRONT Baseline

Status: **EXECUTION INSTRUCTION / FREE TEXT-ONLY VALIDATION / FRONT FIRST**

## 1. Repository and working root

Use current `main` of:

`Pin-Gin/MEMORIELA`

Current validation root:

`visuals/yura/execution/text-only-root/`

Do not use `tools/yura-master-benchmark/**` during this phase.
That route is reserved for paid generation after the text-only gate passes.

## 2. Phase 0 — source verification MUST run before generator capability check

Read only:

```text
visuals/yura/execution/text-only-root/YURA_TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md
visuals/yura/execution/text-only-root/YURA_VISUAL_TEXT.md
```

Expected Git blob SHA values:

```text
YURA_TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md
= 3a356d96e2b757777f193aa1bb79e4c4e6b3d4b0

YURA_VISUAL_TEXT.md
= b5565b10c1ba68bed3720fbc5360f0f7925799e9
```

Before checking whether image generation is available:

```text
1. obtain current main commit SHA
2. confirm both files exist on current main
3. obtain and compare both blob SHAs
4. record the three SHAs
```

If either blob SHA differs:

```text
EXECUTION STATE = SOURCE_BLOCKED
```

STOP and report the mismatch. Do not generate.

## 3. Hard source boundary

For YURA appearance, use **only**:

`YURA_VISUAL_TEXT.md`

Do not use or inspect YURA image references as generation input.
Do not add appearance information from other YURA files.
Do not use Memory, story, manuscript, character files, old images, past generated images, Git history, or previous benchmark outputs as appearance input.

`YURA_TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md` is an execution / inspection rule. Do not append it wholesale to the image prompt as extra YURA appearance prose.

## 4. Phase 1 — generator capability check

After Phase 0 source verification passes, check whether this active Codex session exposes native image-generation capability.

Required route:

```text
Codex-native image generation only
```

Do not:

```text
call OpenAI Image API
use OPENAI_API_KEY
import or call the OpenAI SDK for image generation
run tools/yura-master-benchmark generation scripts
use another external image generator as fallback
```

If Codex-native image generation is unavailable:

```text
EXECUTION STATE = ENVIRONMENT_BLOCKED
FRONT RESULT = NOT EXECUTED
QUALIFICATION COUNT CHANGE = NONE
```

STOP after reporting the verified commit/blob SHAs and the unavailable capability.

Do **not** report `TEXT-ONLY FRONT = NOT QUALIFY` because no image was generated and no Visual Text quality test occurred.

## 5. Phase 2 — FRONT baseline generation

Only if Phase 0 = PASS and Codex-native image generation is available:

Generate exactly **one** image.

This first run is the cleanest text-only baseline.
Do not add a new view override or crop override beyond what `YURA_VISUAL_TEXT.md` already specifies.

Preserve its current validation composition:

```text
one YURA
front view
full body
upright neutral pose
white / plain background
```

Do not add ear-specific rescue wording outside `YURA_VISUAL_TEXT.md`.
Do not paraphrase, strengthen, weaken, or reinterpret the ear rules before seeing the result.

Generation status:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

## 6. Save result

Save the generated image under:

`visuals/yura/execution/text-only-root/results/`

Preferred filename:

`front_001.png`

Do not commit the generated image unless the author explicitly instructs you to do so.

## 7. Inspect the generated image

After generation, inspect the image without modifying it.

Report:

```text
VIEW ACHIEVED: PASS / FAIL
YURA TEXT-ONLY IDENTITY: PASS / SOFT FAIL / FAIL
EAR ELONGATION / INFLATION: NONE / MILD / CLEAR
EAR OUTWARD PROJECTION: NONE / MILD / CLEAR
VISIBILITY COMPENSATION: NONE / SUSPECTED / CLEAR
HAIR CLEARED ONLY TO EXPOSE EAR: NO / SUSPECTED / YES
NATURALNESS: PASS / MINOR ISSUE / FAIL
OTHER VISIBLE ISSUES: short factual note
```

For this early diagnostic run, minor unrelated awkwardness does not automatically fail the run.

The ear-behavior result is qualifying only if:

```text
no CLEAR ear elongation / inflation
no CLEAR outward projection
no CLEAR visibility compensation
no forced hair clearing solely to expose the ear
```

Then classify:

```text
EXECUTION STATE = GENERATED / QUALIFY
or
EXECUTION STATE = GENERATED / NOT QUALIFY
```

Only a generated and inspected image may receive QUALIFY / NOT QUALIFY.

## 8. Stop point

After the FRONT result, STOP.

Do not automatically generate FRONT_3Q, SIDE, REAR_3Q, or BACK.
Do not edit `YURA_VISUAL_TEXT.md`.
Do not enter the paid-generation route.

Return exactly this operational summary:

```text
current main commit SHA: <sha>
protocol blob SHA: <sha>
Visual Text blob SHA: <sha>
Codex-native image generation: AVAILABLE / UNAVAILABLE
EXECUTION STATE: SOURCE_BLOCKED / ENVIRONMENT_BLOCKED / GENERATED-QUALIFY / GENERATED-NOT-QUALIFY
generated image path: <path or NONE>
FRONT inspection result: <result or NOT EXECUTED>
qualification count change: +1 / 0
```
