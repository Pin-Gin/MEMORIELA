# YURA TEXT-ONLY ROOT SINGLE-RUN PROTOCOL

Status: **PROTECTED / MANDATORY**

Purpose:
Text-only Root stability batchを、画像生成モデル側では常に「1回 = 1人 = 1枚」として実行する。

## Orchestration boundary
Batch size belongs to the controller / QA layer only.

For a requested 3- or 5-image stability test:
- perform 3 or 5 independent generation calls
- never ask one generation call to produce multiple candidates
- never pass batch count into the image-generation content instruction
- never request a comparison sheet / contact sheet / triptych

## Per-call invariant
Every call:
- uses `TEXT_ONLY_ROOT_EXECUTION.md`
- uses no visual reference
- keeps the same text payload
- keeps the same aspect / framing class
- contains exactly one YURA
- contains exactly one composition
- contains exactly one canvas
- outputs exactly one image

## Invalid run
A run is invalid and excluded from stability QA if it contains:
- more than one YURA
- more than one panel
- multiple poses
- triptych / contact-sheet structure
- character-sheet structure
- labels / swatches / measurements
- altered execution payload
- any generation-time image reference

Invalid runs diagnose execution-control failure and must not be used as evidence of Text Authority instability.
