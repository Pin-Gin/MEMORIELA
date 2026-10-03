# YURA TEXT-ONLY ROOT SOURCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / SOURCE INTEGRITY LOCK**

Purpose:
`PAYLOAD.txt` がどの現行Authorityからコンパイルされたかを固定し、Authority変更後に古いPayloadをそのまま実行しないための記録。

This file is **NOT image-generation input**.

## Compiled-from repository state
Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Base commit used for this compile: `b9aca2b09a03ef26cd36eb41b3583a6c89354292`

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
