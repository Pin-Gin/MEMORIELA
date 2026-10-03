# VISUAL EXECUTION PAYLOAD PROTOCOL

Status: **PROTECTED / MANDATORY / PROJECT-WIDE**

Purpose:
Authorityを「読むこと」と、画像生成モデルへ「何を実行命令として渡すか」を分離する。

## Core rule
Authority / Gate / QA / controller documents are for resolution, validation, orchestration, and acceptance.

The image-generation execution receives only the active **mode-specific Execution Payload** plus explicitly authorized request variables.

Do not pass raw Governance / Gate / QA / controller / retry / batch documents directly into the image-generation execution.

## Payload / controller separation — MANDATORY
A Domain may physically separate:
- pure image-generation semantic payload
- run controller
- source-integrity lock
- QA / acceptance rules

When separated, only the declared pure payload may enter the generation-facing semantic handoff.

Controller-only files must never be concatenated, summarized, or paraphrased into the image-generation semantic input merely because they were required pre-read material.

`REQUIRED_TO_READ != REQUIRED_TO_SEND_TO_IMAGE_MODEL`

## Execution carrier — MANDATORY
Authority resolution and generation transport are separate concerns.

Do **not** redefine a Source / Reference Mode based on the transport implementation.

### Source-mode rule
`TEXT_ONLY` means:
- generation-time visual references = NONE
- generation semantics come from the active text Authorities / Execution Payload
- no Master PNG or other image is attached to generation

It does **not** mean:
- direct raw-prompt API required
- visual generation forbidden on context-derived image tools

### DIRECT_MODEL_INPUT
Use when the interface exposes a controllable model-facing prompt / instruction field.

The active Execution Payload should be passed through that field without ad-hoc semantic mutation.

### CONTEXT_DERIVED_TEXT_EXECUTION
Use when the image-generation interface derives image instructions from the active conversation context.

This route is valid for a `TEXT_ONLY` mode when all are true:
- all required text Authorities are resolved
- the active Execution Payload is resolved
- no generation-time visual reference is supplied
- the payload's actual generation semantics are materialized immediately before the image-generation call
- no unrelated Gate / QA / controller / retry / batch prose is mixed into the generation handoff
- the caller does not replace the payload with path-only shorthand such as "follow Git" or "same as before"

This carrier does **not** claim byte-for-byte preservation inside hidden model plumbing.
That limitation is handled by post-generation QA; it does not convert TEXT_ONLY into a blocked mode.

### EXTERNAL_RETRIEVAL_ONLY — INVALID
Git read, connector result, file path, memory, prior read, or prior successful generation by itself is not a generation handoff.

### Permission rule
For protected TEXT_ONLY generation:
- `DIRECT_MODEL_INPUT` may PASS
- `CONTEXT_DERIVED_TEXT_EXECUTION` may PASS
- `EXTERNAL_RETRIEVAL_ONLY` may not PASS

Generation remains Fail-Closed when:
- required text Authorities are missing
- active Execution Payload is missing
- required source-integrity lock is stale
- unauthorized visual references are attached
- payload semantics are not carried into the generation-facing context
- controller / QA / retry / batch prose contaminates a declared payload-only handoff
- active Gate / mode requirements otherwise fail

## Compile stage
Required order:

```text
AUTHORITY RESOLUTION
        ↓
MODE RESOLUTION
        ↓
SOURCE-INTEGRITY VALIDATION (when required)
        ↓
EXECUTION PAYLOAD SELECTION / COMPILE
        ↓
EXECUTION PAYLOAD VALIDATION
        ↓
EXECUTION CARRIER / SEMANTIC HANDOFF VALIDATION
        ↓
SINGLE IMAGE GENERATION
        ↓
POST-GENERATION QA / ACCEPTANCE CLASSIFICATION
```

The Execution Payload is not an independent canon source.
It is a deterministic operational projection of the current protected Authorities.

If the payload conflicts with protected Authority:
`GENERATION_ALLOWED = NO`

## Payload content
Include only generation-relevant semantics:
- character identity
- protected BODY geometry
- protected FACE / EYE / HAIR / SKIN
- active rendering grammar
- active outfit / pose / scene variables
- active composition
- a short anti-drift block only where needed

Do not include:
- QA scoring text
- PASS / FAIL tables
- retry policy
- Git workflow instructions
- source-lock bookkeeping
- run-controller instructions
- batch evaluation instructions
- history / migration notes
- candidate-selection discussion
- rejection rationale
- comparison results
- Authority-promotion rules
- unrelated Domain rules

## Positive-first rule
Execution Payload should use concise positive identity statements first.

Detailed QA / rejection vocabulary remains outside the generation payload.

A short negative constraint block is allowed only for known recurring drift that cannot be expressed clearly in positive form.

## Batch isolation
A request for 3 / 5 / N comparison images is an orchestration instruction, not image content.

The generation model must not receive:
- "batch"
- "comparison sheet"
- "three candidates"
- "five candidates"
- "triptych"
- "contact sheet"
- "variants side by side"

Each call receives a **single-run payload**:
- exactly one character
- exactly one composition
- exactly one canvas
- exactly one image

Multiple requested outputs are produced by repeating independent single-image executions.

## Reference separation
Reference policy is resolved before payload execution.

For text-only modes:
- generation-time image references = NONE
- do not mention or inject a PNG as active visual authority into the execution payload

For production modes:
- only Gate-approved reference roles may be attached
- text payload and image references are both required when the active Gate says so

## QA separation
Post-generation QA may compare against Masters and protected specs as permitted by the active Gate.

A comparison reference used after generation must never leak backward into a text-only generation call.

## Rendering hard-lock compilation
Every character Execution Payload that uses the project-wide Character Rendering Style must contain an explicit rendering hard-lock block.

At minimum, the payload must state:
- `HIGH-QUALITY 2D ANIME ILLUSTRATION ONLY`
- 2D anime facial / line / shading grammar
- soft cel / grouped illustration shading
- matte / low-gloss surface quality
- NOT photoreal
- NOT semi-photoreal
- NOT live-action
- NOT CGI / 3D render
- NOT PBR / game-engine render

The word `matte` by itself is insufficient.

If the compiled payload omits the 2D-anime-first lock or permits a realistic / CGI interpretation:
`EXECUTION_PAYLOAD_VALIDATION = FAIL`
`GENERATION_ALLOWED = NO`

## Mandatory post-generation acceptance
After every permitted generation, run the active Domain QA and the project-wide Post-Generation Acceptance Protocol.

A generated image is not accepted merely because the tool returned or displayed an image.

Generation-tool/UI visibility before caller-side QA is **not** a generation-integrity failure and is **not** a pre-generation blocker.

`USER_VISIBLE != ACCEPTED`
`USER_VISIBLE != AUTHORITY`

Rendering hard fail, identity hard fail, reference-policy fail, or execution-integrity fail:
`ACCEPTANCE_ALLOWED = NO`

A failed candidate may be visible because of the generation interface, but it remains rejected and must never be promoted to Authority or reused as a protected reference.

## Fixed-payload execution mode
A Domain may declare an Execution Payload as a protected fixed payload.

For that mode:
- the declared payload content is the actual image-generation semantic input
- do not paraphrase it at runtime
- do not append Gate / QA / controller / retry / batch text
- do not mutate it between runs of one stability batch
- any semantic modification requires a new batch

## Text-only stochastic retry boundary
Without a fixed visual/pixel carrier, stochastic full-image regeneration cannot guarantee unaffected domains remain fixed.

Therefore, in a text-only full-generation mode:
- `TARGETED_RETRY = FORBIDDEN`
- failed candidate = whole-candidate reject
- next run = full independent regeneration using the same fixed payload
- all protected domains are re-QA'd

Scope-targeted retry may only be claimed where the active execution route can actually preserve unaffected domains.
