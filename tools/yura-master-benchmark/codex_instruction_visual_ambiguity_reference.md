# Codex Instruction — YURA Visual Ambiguity Diagnostic References

Use current `main` only.

## Read first

```text
tools/yura-master-benchmark/CURRENT_HANDOFF.md
tools/yura-master-benchmark/PIPELINE_STATE.md
visuals/yura/identity/master/YURA_VISUAL_AMBIGUITY_PROTOCOL.md
tools/yura-master-benchmark/VISUAL_AMBIGUITY_REFERENCE_GENERATION_SPEC_20261013.md
tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py
tools/yura-master-benchmark/visual_ambiguity_reference_config.json
```

Do not use old Body Geometry Guide, Test 5/6 outputs, old Master images, story/manuscript/characters appearance, Memory-derived appearance, or Git-history visual fallbacks.

## Phase A — FREE preflight only

Do not call the Image API.

```bash
git fetch origin main
git status --short
git rev-parse HEAD
git rev-parse origin/main
python -m py_compile tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py

python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view FRONT --preflight-only
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view FRONT_3Q --preflight-only
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view SIDE --preflight-only
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view REAR_3Q --preflight-only
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view BACK --preflight-only
```

Require all five to PASS.

Verify for every view:

```text
PREFLIGHT_OK
paid_model_calls = 0
HEAD == origin/main
Master SHA256 exact match
Face SHA256 exact match
status = DIAGNOSTIC / CANDIDATE ONLY
known ear defect not promoted = true
rear-hair unverified not promoted = true
image reference order = Master, Face
transport config = dedicated ambiguity config
prompt invariants complete
denied-source list complete
```

If any check fails, STOP. Do not generate an image and do not weaken the check.

Return the five run directories and a compact PASS/FAIL table.

## Phase B — diagnostic image generation

Do this only after the author explicitly approves paid diagnostic generation after reviewing Phase A.

Generate one view at a time, never as an automatic five-image batch:

```bash
python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view FRONT
# review FRONT before continuing

python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view FRONT_3Q
# review

python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view SIDE
# review

python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view REAR_3Q
# review

python tools/yura-master-benchmark/run_visual_ambiguity_reference_once.py --view BACK
# review
```

Each output remains:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

Route/view-behavior PASS is not ear PASS and not rear-hair PASS.

After the five-view route passes, stop generation and move to:

```text
1. ear ACTUAL / VISIBLE / HAIR OCCLUSION analysis and correction
2. rear-hair / back-view mass / silhouette / layer-order analysis and correction
```

Do not silently repair a discovered defect by changing a gate after seeing the output.
