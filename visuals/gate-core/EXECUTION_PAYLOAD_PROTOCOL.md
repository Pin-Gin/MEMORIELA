# VISUAL EXECUTION PAYLOAD PROTOCOL

Status: **PROTECTED / MANDATORY / PROJECT-WIDE**

Purpose:
Authorityを「読むこと」と、画像生成モデルへ「何を実行命令として渡すか」を分離する。

## Core rule
Authority / Gate / QA documents are for resolution and validation.

The image-generation execution receives only the active **mode-specific Execution Payload** plus explicitly authorized request variables.

Do not pass raw Governance / Gate / QA documents directly into the image-generation execution.

## Execution carrier — MANDATORY

Authority resolution is not execution transport.

Before image generation, resolve one actual `EXECUTION_CARRIER`:

### DIRECT_PROMPT_CARRIER
Use only when the image-generation interface exposes a real prompt/instruction field whose text is passed to the image model.

For a `PROTECTED FIXED EXECUTION BLOCK`:
- pass the fixed generation block through that field without semantic rewrite
- Git path / connector retrieval alone does not count
- the actual model-facing input must contain the protected generation semantics

### CONVERSATION_CONTEXT_CARRIER
Use when the image-generation interface does **not** expose a controllable prompt field and instead derives generation instructions from the active conversation context.

In this carrier:
- Git / connector / tool retrieval output is **resolution evidence only**
- merely reading a file does **not** prove that its semantics reached image generation
- immediately before the image-generation call, materialize the active fixed generation block into the generation-visible conversation context
- for a fixed payload, copy the payload's `FIXED EXECUTION BLOCK` semantics without ad-hoc paraphrase, omission or substitution
- do not replace the block with phrases such as "use Git", "follow YURA rules", "same as before" or file paths
- do not append QA / Gate / batch / retry prose to the handoff
- the handoff exists only to carry generation semantics across the tool boundary

If the active image-generation interface cannot provide either carrier:
`EXECUTION_CARRIER = NONE`
`GENERATION_ALLOWED = NO`

### Explicit invalid carrier
`EXTERNAL_RETRIEVAL_ONLY` is never a valid execution carrier.

A Git read, connector result, file path, memory, or prior successful generation is not by itself evidence that the image model received the protected payload.

## Compile stage
Required order:

```text
AUTHORITY RESOLUTION
        ↓
MODE RESOLUTION
        ↓
EXECUTION PAYLOAD SELECTION / COMPILE
        ↓
EXECUTION PAYLOAD VALIDATION
        ↓
EXECUTION CARRIER / SEMANTIC HANDOFF VALIDATION
        ↓
SINGLE IMAGE GENERATION
        ↓
POST-GENERATION QA
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
- batch evaluation instructions
- history / migration notes
- candidate-selection discussion
- rejection rationale
- comparison results
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
After every generation, run the active Domain QA and the project-wide Post-Generation Acceptance Protocol before presenting the image as a completed result.

A generated image is not accepted merely because the tool returned an image.

Rendering hard fail, identity hard fail, reference-policy fail, or execution-integrity fail:
`PRESENTATION_ALLOWED = NO`


## Fixed-block execution mode
A Domain may declare an Execution Payload as:
`PROTECTED FIXED EXECUTION BLOCK`

For that mode:
- the file content is the actual image-generation semantic input
- do not paraphrase it at runtime
- do not append Gate / QA / batch text
- do not mutate it between runs of one stability batch
- any modification requires a new batch

## Text-only stochastic retry boundary
Without a fixed visual/pixel carrier, stochastic full-image regeneration cannot guarantee unaffected domains remain fixed.

Therefore, in a text-only full-generation mode:
- `TARGETED_RETRY = FORBIDDEN`
- failed candidate = whole-candidate reject
- next run = full independent regeneration using the same fixed block
- all protected domains are re-QA'd

Scope-targeted retry may only be claimed where the active execution route can actually preserve unaffected domains.
