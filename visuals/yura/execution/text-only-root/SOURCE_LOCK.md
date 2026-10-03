# YURA TEXT-ONLY ROOT SOURCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / SOURCE INTEGRITY LOCK**

Purpose:
`PAYLOAD.txt` がどの現行Authorityからコンパイルされたかを固定し、Authority変更後に古いPayloadをそのまま実行しないための記録。

This file is **NOT image-generation input**.

## Compiled-from repository state
Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Base commit used for this compile: `1aa207031cfd0b3ed47d02b6f54546c92738eeb2`
Payload recompile commit: `9157531766396c5f7b83ed429e620a4e947a7c0d`
Payload blob: `bfe61b10316129a5e84d57a4aa55f3ae1b4f7c1d`

## Approved completion provenance
Author-approved completion image SHA-256 used for transcription:
`2487b8c8ad4cdc4358fe4d69b57b9a4ea50e23fd2359613f82c7de7d68fa449a`

`COMPLETION_IMAGE_ROLE = TRANSCRIPTION_PROVENANCE_ONLY`
`COMPLETION_IMAGE_GENERATION_REFERENCE = NONE`
`COMPLETION_IMAGE_POST_GENERATION_REFERENCE = NONE`
`REPOSITORY_YURA_VISUAL_MASTER_PNG_USED_FOR_THIS_TEXT_ONLY_TARGET = NO`

## Recompile classification
`AUTHORITY_CHANGE = YES`
`PAYLOAD_RECOMPILE = YES`
`PREVIOUS_BATCH_STATUS = STOPPED`
`PREVIOUS_BATCH_STOP_REASON = AUTHOR_APPROVED_COMPLETION_TARGET_REALIGNMENT`
`NEW_STABILITY_BATCH_REQUIRED = YES`
`NEW_STABILITY_BATCH_STATUS = READY`

Reason:
The author designated a final completion image as the target that TEXT_ONLY generation must reproduce.
The repository Root Master PNG was explicitly excluded from this task.
Protected text Authorities were synchronized to the author-approved completion target, including BODY silhouette, Normal Super-Long length distribution, and validation clothing.
`PAYLOAD.txt` was then rebuilt from those synchronized positive semantics instead of accumulating prior failure-specific debug wording.

## Protected source blobs
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md` — `2ede5c28484f8de787724cec31bbb9ffffabde21`
- `visuals/yura/identity/body/BODY_SPEC.md` — `d0288314f8d5dbc1cf6c2c1b719058eb525d629c`
- `visuals/yura/identity/face/FACE_SPEC.md` — `ecfcbf2b95216c54d6390b19b8fdbd664740b14e`
- `visuals/yura/identity/ears/EAR_SPEC.md` — `f5c61c138c051ebd4aebf7d01c1c140afea3b655`
- `visuals/yura/identity/eyes/EYE_SPEC.md` — `53cc19918471e3b54c77ea1b1db43293bee98f57`
- `visuals/yura/identity/hair/HAIR_SPEC.md` — `a1f259ee396f192aad635e7b7f4433822981e1f0`
- `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md` — `f2f0101f29f0036c47225e40af16a2146bfaed27`
- `visuals/yura/identity/skin/SKIN_SPEC.md` — `22860c4d0b1a2a20612d4c83fd5a0e17a746e83b`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md` — `8f088f354938ae5081cd9a067e1444afe747b243`
- `visuals/CHARACTER_RENDERING_STYLE.md` — `345e779c72664a50e2f099199a3950e0115576b8`
- `visuals/yura/qa/VALIDATION_CLOTHING.md` — `207acb3419278490d54dfc017a9ae28cc458929c`

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
- prior failed-generation descriptions

Detailed source Authorities remain authoritative for validation and QA.
The concise payload does not delete or weaken those protected specifications.

## Current compile emphasis
The current payload is organized around the approved completion target rather than prior failure history:
- exact 7.25-head petite / slender whole-body balance
- compact ribcage with clearly fuller relative chest volume without torso widening
- small soft-oval vertically compact face
- blue-gray eyes
- slightly-small restrained ears with no visibility-driven enlargement
- silver-white Normal Super-Long whose dense principal mass continues through the waist into the upper-hip / hip-bone region, then tapers to sparse upper-thigh tips
- pale fitted tank-style validation top with medium-width integrated shoulder panels and rounded scoop neckline
- pale simple fitted shorts with a clean waistband
- no ornament / jewelry / hair accessory
- neutral upright front-facing full-body pose
- white background
- Matte Natural Anime / high-quality 2D anime rendering

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
