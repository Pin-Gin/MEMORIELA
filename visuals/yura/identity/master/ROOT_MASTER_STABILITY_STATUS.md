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
- generation payload and controller/QA text are physically separated
- image-generation semantic input = `visuals/yura/execution/text-only-root/PAYLOAD.txt` only
- run control = `visuals/yura/execution/text-only-root/RUN.md`
- source integrity = `visuals/yura/execution/text-only-root/SOURCE_LOCK.md`
- `RUN.md` / `SOURCE_LOCK.md` / Gate / QA / retry / batch text must never enter the image-generation semantic handoff
- stale source lock blocks generation until deliberate payload recompilation
- FACE target remains a small soft oval face whose vertical length is standard to slightly short and remains vertically compact
- EYE identity remains BLUE-GRAY ONLY
- EAR remains a dedicated protected Authority with a slightly-small 28–30% face-length target and no visibility-driven geometry compensation
- HAIR remains silver-white Normal Super-Long with principal mass ending at waist to slightly below
- BODY remains exact 7.25-head petite/slender with compact ribcage and moderate relative chest fullness without widening the body

## Current text-only execution policy
- generation source = current protected text Authorities only
- generation-time visual references = NONE
- active image-generation payload = `visuals/yura/execution/text-only-root/PAYLOAD.txt`
- current context-derived image interface is allowed through `CONTEXT_DERIVED_TEXT_EXECUTION`
- actual payload semantics must be carried immediately before each generation
- direct raw-prompt API is not a prerequisite for TEXT_ONLY mode
- payload must remain unchanged within an active stability batch
- no runtime paraphrase / per-run correction
- no controller / QA / history / retry / batch prose mixed into generation semantics
- `TARGETED_RETRY = FORBIDDEN`
- any failed protected domain rejects the whole candidate
- rejected candidate is never promoted to Authority or future protected reference
- next attempt is a new independent full candidate using the same unchanged `PAYLOAD.txt`
- every new candidate is re-evaluated across all protected domains

## Known drift to re-test
- EYE color
- EAR size / length / placement / visibility-driven EAR/head geometry compensation
- HAIR color / length / mass
- BODY chest relation
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
- current protected text Authorities only
- current `SOURCE_LOCK.md`
- `PAYLOAD.txt` as the only generation semantic input
- `RUN.md` as controller-only material
- one person / one image per run
- post-generation full QA / acceptance classification

Minimum 3 valid runs; preferred 5.

Only after stable protected executions are explicitly approved may Root stability become APPROVED.
