# POST-GENERATION ACCEPTANCE PROTOCOL

Status: **PROTECTED / MANDATORY / PROJECT-WIDE / FAIL-CLOSED FOR ACCEPTANCE**

Purpose:
生成ツールが画像を返したことと、その画像を候補として採用・Authority化してよいことを分離する。

## Required order

```text
IMAGE GENERATED
      ↓
DOMAIN QA
      ↓
HARD-FAIL CHECK
      ↓
ACCEPTANCE CLASSIFICATION
      ↓
PASS → ACCEPTED CANDIDATE
FAIL → REJECTED CANDIDATE / RETRY / REPORT FAILURE
```

## Core rule
A generated image is **CANDIDATE ONLY** until post-generation QA passes.

Default before QA:
`ACCEPTANCE_ALLOWED = NO`

Only after all mandatory hard gates pass:
`ACCEPTANCE_ALLOWED = YES`

## Visibility / acceptance separation — MANDATORY
Generation-tool or UI visibility is **not** acceptance.

`USER_VISIBLE != ACCEPTED`
`USER_VISIBLE != AUTHORITY`

This protocol does **not** require:
- hidden pre-presentation staging
- caller-side interception before the generation UI displays the image
- suppressing a generated candidate from the user before QA

If the active image-generation interface displays the generated image immediately, that does not invalidate the generation run by itself.

After the image is generated, run the required QA and classify the candidate.

If the candidate FAILS:
- mark it as `REJECTED CANDIDATE`
- `ACCEPTANCE_ALLOWED = NO`
- do not describe it as PASS / accepted / completed
- do not promote it to Authority
- do not use it as a future Identity / production reference
- follow the active retry semantics

Fail-Closed applies to **acceptance, Authority promotion, and future reference use**.
It does not convert unavoidable generation-UI visibility into a pre-generation blocker.

Post-generation QA is therefore compatible with image interfaces that return or display the image before caller-side QA can be completed.

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
`ACCEPTANCE_ALLOWED = NO`

The image remains a rejected candidate only.

## Other hard fails
Also block acceptance / Authority promotion on:
- reference-policy violation
- execution-integrity violation
- wrong protected identity color / geometry when the active Domain marks it hard
- multi-panel / multi-figure output when single-run mode is required
- missing required Master / reference in a mode that requires it

## Retry behavior
When retry is allowed:
- preserve the active Authority
- do not silently alter Authority
- do not promote the failed candidate to reference

If automatic retry is not performed, report the failed domain succinctly and keep the candidate rejected.

## Text-only candidate failure
When active mode is a text-only stochastic full-generation mode:
- any protected-domain FAIL keeps `ACCEPTANCE_ALLOWED = NO`
- reject the entire candidate
- do not accept it as Authority
- do not use it as a generation-time reference
- do not perform scope-only targeted regeneration while claiming other visual domains are fixed
- regenerate a new whole candidate with the unchanged fixed Execution Block
- rerun all mandatory QA
