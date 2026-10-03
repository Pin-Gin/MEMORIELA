# YURA TEXT-ONLY ROOT SOURCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / SOURCE INTEGRITY LOCK**

Purpose:
`PAYLOAD.txt` がどの現行Authorityからコンパイルされたかを固定し、Authority変更後に古いPayloadをそのまま実行しないための記録。

This file is **NOT image-generation input**.

## Compiled-from repository state
Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Base commit used for this compile: `b9720702324a94ac7aa10f41a27389a01e045de8`
Payload recompile commit: `57d01c583f3e0bdb288885fc1b1b146f8cdbc34f`
Payload blob: `b544989cc88f1f6cfdd3d43e9adcf184eea52eab`

## Recompile classification
`AUTHORITY_CHANGE = NO`
`PAYLOAD_RECOMPILE = YES`
`PREVIOUS_BATCH_STATUS = STOPPED`
`PREVIOUS_BATCH_STOP_REASON = EAR_SYSTEMATIC_DRIFT`
`NEW_STABILITY_BATCH_REQUIRED = YES`
`NEW_STABILITY_BATCH_STATUS = READY`

Reason:
After the previous FACE / EAR reprioritization, a new valid isolated generation still reproduced the same material EAR enlargement on one visible ear.
This establishes repeated EAR size / visibility drift across isolated runs and requires payload refinement outside the stopped batch.
The protected Authorities below were not changed.
`PAYLOAD.txt` was recompiled only to strengthen the existing EAR Authority semantics: protected small ear geometry has priority over visibility, bilateral ear visibility is not required, natural partial / full hair occlusion is valid, and visibility-driven enlargement / projection / rotation / outward displacement remains forbidden.

## Protected source blobs
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md` — `81bb0de02d7417f6bbdb22882894b2751618ed38`
- `visuals/yura/identity/body/BODY_SPEC.md` — `d44450f0d23495f447b15c2c24442be0e63c2fce`
- `visuals/yura/identity/face/FACE_SPEC.md` — `ecfcbf2b95216c54d6390b19b8fdbd664740b14e`
- `visuals/yura/identity/ears/EAR_SPEC.md` — `f5c61c138c051ebd4aebf7d01c1c140afea3b655`
- `visuals/yura/identity/eyes/EYE_SPEC.md` — `53cc19918471e3b54c77ea1b1db43293bee98f57`
- `visuals/yura/identity/hair/HAIR_SPEC.md` — `6f89c48849ccd15e952b984596adc0c9ccb519ce`
- `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md` — `54007f7e82d632fe2b41935d37b6ef034d227841`
- `visuals/yura/identity/skin/SKIN_SPEC.md` — `22860c4d0b1a2a20612d4c83fd5a0e17a746e83b`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md` — `8f088f354938ae5081cd9a067e1444afe747b243`
- `visuals/CHARACTER_RENDERING_STYLE.md` — `345e779c72664a50e2f099199a3950e0115576b8`
- `visuals/yura/qa/VALIDATION_CLOTHING.md` — `ef07fbe289f00f2787ee71744d33bf4e29e61a83`

## Compile rule
`PAYLOAD.txt` is a concise operational projection of the protected sources above.

It intentionally contains generation-relevant semantics only.
It must not contain:
- Gate workflow
- QA scoring / verdict logic
- retry procedure
- batch instructions
- Git history
- candidate-selection language
- Authority promotion rules

Detailed source Authorities remain authoritative for validation and QA.
The concise payload does not delete or weaken those protected specifications.

## Current compile emphasis
The current payload gives generation-facing priority to existing protected constraints that repeatedly drifted:
- FACE vertical length remains standard to slightly short and visibly vertically compact; no oblong / elongated / long fashion-model-like reinterpretation
- EAR SIZE HAS PRIORITY OVER VISIBILITY
- EAR remains slightly small at approximately 28–30% of face vertical length
- EAR projection remains restrained and the long axis remains only approximately 5–10 degrees posterior from vertical
- either ear may be visible, partially hidden, or fully hidden by natural local hair placement
- bilateral ear visibility / equal exposure is not a target
- no visibility-driven EAR enlargement, lengthening, outward displacement, projection increase, flaring, or camera-facing rotation
- if visibility conflicts with protected ear geometry, preserve the protected ear geometry and allow natural occlusion
- exact waist-level termination of dense principal hair mass before the hairstyle label is introduced
- explicit rapid taper below the waist and sparse-tip-only continuation toward the upper-buttock boundary
- explicit broad-shoulder sleeveless validation-top construction and rejection of camisole/thin-strap reinterpretation
- explicit neutral upright reference-pose geometry, with both hands visible beside the thighs and no contrapposto / hands-behind-back reinterpretation
- explicit fully unadorned character state with no hair ornament / ribbon / jewelry / accessory invention

These are compilation emphases only and do not create new Canon.

## Recompile trigger
If any protected source blob listed above changes:
`PAYLOAD_SOURCE_LOCK = STALE`
`GENERATION_ALLOWED = NO`

Before the next protected TEXT_ONLY_ROOT_MASTER generation:
1. reread the changed Authority
2. deliberately recompile `PAYLOAD.txt`
3. update the blob list in this file
4. start a new stability batch

Do not silently patch `PAYLOAD.txt` during an active batch.
