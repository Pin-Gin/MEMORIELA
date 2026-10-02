# YURA ROOT MASTER STABILITY STATUS

Status: **READY_FOR_TEXT_ONLY_STABILITY_RUN**

Current Root Master remains:
`visuals/yura/identity/master/YURA_VISUAL_MASTER.png`

## Current state
`TEXT_ONLY_ROOT_STABILITY = READY_FOR_TEXT_ONLY_STABILITY_RUN`

## Confirmed execution findings
- TEXT_ONLY source mode: ACTIVE
- generation-time visual references: NONE
- current context-derived image interface may be used through CONTEXT_DERIVED_TEXT_EXECUTION
- payload semantics handoff is required before each generation
- single-run / one-person / one-image orchestration: PASS
- generation-time visual references: NONE
- project-wide 2D-anime-first Rendering Hard Gate: ACTIVE
- post-generation Acceptance Classification: ACTIVE
- generation-tool/UI visibility before QA is not acceptance and is not a pre-generation blocker
- failed candidates remain rejected and cannot become Authority / protected references
- prior scope-only retry semantics for text-only full regeneration: INVALID DESIGN, now removed
- FACE target refined to a small soft oval face whose vertical length is standard to slightly short and remains vertically compact
- eye / nose / mouth geometry and default-expression constraints were strengthened
- EAR is a dedicated protected Authority with a slightly-small 28–30% face-length target, length-priority placement, restrained tilt / projection, and no visibility-driven EAR/head geometry compensation
- local hair placement around the ear may vary naturally; ear visibility itself is not a generation target
- fixed `TEXT_ONLY_ROOT_EXECUTION.md` was deliberately recompiled from the updated protected Authorities

## Current text-only execution policy
- generation source = current text Authorities only
- generation-time visual references = NONE
- active fixed payload = `TEXT_ONLY_ROOT_EXECUTION.md`
- current context-derived image interface is allowed through `CONTEXT_DERIVED_TEXT_EXECUTION`
- actual payload semantics must be carried immediately before each generation
- direct raw-prompt API is not a prerequisite for TEXT_ONLY mode
- fixed block must remain semantic-equivalent within a batch
- no runtime paraphrase / per-run correction
- `TARGETED_RETRY = FORBIDDEN`
- any failed protected domain rejects the whole candidate
- rejected candidate is never promoted to Authority or future protected reference
- next attempt is a new independent full candidate using the same unchanged block
- every new candidate is re-evaluated across all protected domains

## Known drift to re-test
- EYE color
- EAR size / length / placement / visibility-driven EAR/head geometry compensation
- HAIR color / length / mass
- BODY bust relation
- FACE consistency
- validation clothing
- rendering consistency

No one-off failed image is sufficient to justify changing canon.

## Blocked downstream
- FACE_MASTER creation = BLOCKED
- BODY_VIEW_MASTER creation = BLOCKED

## Next action
Start a new TEXT_ONLY Root stability batch using:
- `REFERENCE_POLICY = NONE`
- current text Authorities only
- active `TEXT_ONLY_ROOT_EXECUTION.md`
- one person / one image per run
- post-generation full QA / acceptance classification

Minimum 3 valid runs; preferred 5.

Only after stable protected executions are explicitly approved may Root stability become APPROVED.
