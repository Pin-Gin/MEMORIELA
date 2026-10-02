# POST-GENERATION ACCEPTANCE PROTOCOL

Status: **PROTECTED / MANDATORY / PROJECT-WIDE / FAIL-CLOSED**

Purpose:
生成ツールが画像を返したことと、その画像をユーザーへ完成結果として提示してよいことを分離する。

## Required order

```text
PRE-PRESENTATION QA CAPABILITY CHECK
      ↓
PASS → IMAGE GENERATED
      ↓
DOMAIN QA
      ↓
HARD-FAIL CHECK
      ↓
PRESENTATION GATE
      ↓
PASS → PRESENT
FAIL → REJECT / RETRY / REPORT FAILURE
```

## Core rule
A generated image is **CANDIDATE ONLY** until post-generation QA passes.

Default before QA:
`PRESENTATION_ALLOWED = NO`

Only after all mandatory hard gates pass:
`PRESENTATION_ALLOWED = YES`

## Pre-presentation QA capability — MANDATORY PRECHECK
Before any protected generation, resolve whether the active image-generation interface can keep the generated candidate from user visibility until mandatory QA completes.

Required:
`PRE_PRESENTATION_QA_CAPABILITY = PASS`

PASS only if all are true:
- the generated candidate can be received / inspected without being automatically presented to the user
- presentation can remain withheld while Domain QA and hard-fail checks run
- a failed candidate can be rejected / discarded without user-visible image presentation
- only a QA-passed candidate is presented

If the interface automatically presents the generated image as soon as generation returns, or the caller cannot guarantee withholding before QA:
`PRE_PRESENTATION_QA_CAPABILITY = FAIL`
`GENERATION_ALLOWED = NO`

`UNKNOWN` or unverifiable capability is treated as FAIL.

This is an execution-environment limitation, not an Authority / Execution Payload failure.

Do not generate first to test whether the interface exposes the candidate. The capability must be resolved before the generation call.

## Project-wide rendering hard fail
Any of the following is immediate hard fail when Matte Natural Anime is active:
- photoreal person
- semi-photoreal portrait
- live-action look
- realistic CGI
- 3D-render dominant appearance
- game-engine rendering
- PBR skin / hair / clothing
- photographic skin texture
- photographic hair-fiber field
- realistic portrait facial rendering that overrides anime grammar

Low gloss / matte surface does not rescue a realism failure.

On rendering hard fail:
`RENDERING = HARD_FAIL`
`PRESENTATION_ALLOWED = NO`

Do not present the failed image as a completed or accepted generation.

## Other hard fails
Also block presentation on:
- reference-policy violation
- execution-integrity violation
- wrong protected identity color / geometry when the active Domain marks it hard
- multi-panel / multi-figure output when single-run mode is required
- missing required Master / reference in a mode that requires it

## Retry behavior
When retry is allowed:
- preserve all passing protected domains
- correct only the failed Scope
- do not silently alter Authority
- do not promote the failed candidate to reference

If automatic retry is not performed, report the failed domain succinctly instead of presenting the rejected output as success.


## Text-only candidate failure
When active mode is a text-only stochastic full-generation mode:
- any protected-domain FAIL keeps `PRESENTATION_ALLOWED = NO`
- reject the entire candidate
- do not present it as accepted
- do not perform scope-only targeted regeneration while claiming other visual domains are fixed
- regenerate a new whole candidate with the unchanged fixed Execution Block
- rerun all mandatory QA
