# Codex Instruction — YURA Text-Only Validation / FRONT Baseline

Status: **EXECUTION INSTRUCTION / FREE TEXT-ONLY VALIDATION / FRONT FIRST**

## 1. Repository and working root

Use current `main` of:

`Pin-Gin/MEMORIELA`

Current validation root:

`visuals/yura/execution/text-only-root/`

Do not use `tools/yura-master-benchmark/**` during this phase.
That route is reserved for paid generation after the text-only gate passes.

## 2. Read only these two YURA specification files for this run

Read:

```text
visuals/yura/execution/text-only-root/YURA_TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md
visuals/yura/execution/text-only-root/YURA_VISUAL_TEXT.md
```

Expected Git blob SHA values:

```text
YURA_TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md
= 891fb7b6c48c5eaf5375b1f647733b610ecde01c

YURA_VISUAL_TEXT.md
= b5565b10c1ba68bed3720fbc5360f0f7925799e9
```

Before generation, confirm the files exist on current `main` and record the commit SHA and both blob SHAs.

If either blob SHA differs, STOP and report the mismatch. Do not generate.

## 3. Hard source boundary

For YURA appearance, use **only**:

`YURA_VISUAL_TEXT.md`

Do not use or inspect YURA image references as generation input.
Do not add appearance information from other YURA files.
Do not use Memory, story, manuscript, character files, old images, past generated images, Git history, or previous benchmark outputs as appearance input.

`YURA_TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md` is an execution / inspection rule. Do not append it wholesale to the image prompt as extra YURA appearance prose.

## 4. Generator boundary

Use Codex-native image generation only.

Do not:

```text
call OpenAI Image API
use OPENAI_API_KEY
import or call the OpenAI SDK for image generation
run tools/yura-master-benchmark generation scripts
use another external image generator as fallback
```

If Codex-native image generation is unavailable, STOP and report that condition.

## 5. FRONT baseline generation

Generate exactly **one** image.

This first run is the cleanest text-only baseline.
Do not add a new view override or crop override beyond what `YURA_VISUAL_TEXT.md` already specifies.

Therefore preserve its current validation composition:

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

## 8. Stop point

After reporting the FRONT result, STOP.

Do not automatically generate FRONT_3Q, SIDE, REAR_3Q, or BACK.
Do not edit `YURA_VISUAL_TEXT.md`.
Do not enter the paid-generation route.

Return to the author with:

```text
current main commit SHA
protocol blob SHA
Visual Text blob SHA
generated image path
FRONT inspection result
TEXT-ONLY FRONT = QUALIFY / NOT QUALIFY
```
