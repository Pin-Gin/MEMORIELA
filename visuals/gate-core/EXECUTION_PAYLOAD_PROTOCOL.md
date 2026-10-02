# VISUAL EXECUTION PAYLOAD PROTOCOL

Status: **PROTECTED / MANDATORY / PROJECT-WIDE**

Purpose:
Authorityを「読むこと」と、画像生成モデルへ「何を実行命令として渡すか」を分離する。

## Core rule
Authority / Gate / QA documents are for resolution and validation.

The image-generation execution receives only the active **mode-specific Execution Payload** plus explicitly authorized request variables.

Do not pass raw Governance / Gate / QA documents directly into the image-generation execution.

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
