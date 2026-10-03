# YURA TEXT-ONLY ROOT SOURCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / SOURCE INTEGRITY LOCK / FINAL VERIFICATION DEFERRED**

Purpose:
`PAYLOAD.txt` がどの現行Authorityからコンパイルされたかを固定し、Authority変更後に古いPayloadをそのまま実行しないための記録。

This file is **NOT image-generation input**.

## Compiled-from repository state
Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Rendering authority hardening commit: `237016e1304b5e15cf2423eca6accf8bbe7a7969`
Payload recompile commit: `75828e1fe69dbf2c7de16e01975663744be5351e`
Payload blob: `58b6343bfce281bad79f454731ab5c88fb43b6e1`

## Approved completion provenance
Author-approved completion image SHA-256 used for transcription:
`2487b8c8ad4cdc4358fe4d69b57b9a4ea50e23fd2359613f82c7de7d68fa449a`

`COMPLETION_IMAGE_ROLE = TRANSCRIPTION_PROVENANCE_ONLY`
`COMPLETION_IMAGE_GENERATION_REFERENCE = NONE`
`COMPLETION_IMAGE_POST_GENERATION_REFERENCE = NONE`
`REPOSITORY_YURA_VISUAL_MASTER_PNG_USED_FOR_THIS_TEXT_ONLY_TARGET = NO`

## Current workflow classification
`PREVIOUS_TEXT_ONLY_BATCH_STATUS = STOPPED`
`STOP_REASON = FACE_EAR_IDENTITY_DRIFT_AND_RENDERING_TOUCH_DRIFT`
`FACE_FIRST_STABILIZATION_REQUIRED = YES`
`FINAL_TEXT_ONLY_VERIFICATION_STATUS = DEFERRED`

The fixed TEXT_ONLY payload is now rendering-hardened and source-locked, but the active workflow first creates and approves a Face Root, then validates a face-anchored full-body Root, before returning to final reference-free TEXT_ONLY stability verification.

## Protected source blobs
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md` — `2ede5c28484f8de787724cec31bbb9ffffabde21`
- `visuals/yura/identity/body/BODY_SPEC.md` — `d0288314f8d5dbc1cf6c2c1b719058eb525d629c`
- `visuals/yura/identity/face/FACE_SPEC.md` — `ecfcbf2b95216c54d6390b19b8fdbd664740b14e`
- `visuals/yura/identity/ears/EAR_SPEC.md` — `f5c61c138c051ebd4aebf7d01c1c140afea3b655`
- `visuals/yura/identity/eyes/EYE_SPEC.md` — `53cc19918471e3b54c77ea1b1db43293bee98f57`
- `visuals/yura/identity/hair/HAIR_SPEC.md` — `a1f259ee396f192aad635e7b7f4433822981e1f0`
- `visuals/yura/identity/hair/styles/NORMAL_SUPER_LONG.md` — `f2f0101f29f0036c47225e40af16a2146bfaed27`
- `visuals/yura/identity/skin/SKIN_SPEC.md` — `22860c4d0b1a2a20612d4c83fd5a0e17a746e83b`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md` — `365cf79a475619c14d8d0e3d73b7f0aaa8c4912f`
- `visuals/CHARACTER_RENDERING_STYLE.md` — `345e779c72664a50e2f099199a3950e0115576b8`
- `visuals/yura/qa/VALIDATION_CLOTHING.md` — `207acb3419278490d54dfc017a9ae28cc458929c`

## Rendering compile emphasis
The payload now explicitly preserves:
- clearly readable fine 2D-anime linework
- grouped soft-cel shadow shapes
- diffuse gradients as mild support only
- low-to-medium, not ultra-low, contrast
- no white-background washout
- grouped anime hair masses
- matte / low-gloss quality
- no watercolor / ethereal / pastel-faded reinterpretation

## Recompile trigger
If any protected source blob listed above changes:
`PAYLOAD_SOURCE_LOCK = STALE`
`GENERATION_ALLOWED = NO`

Before final protected TEXT_ONLY_ROOT_MASTER verification:
1. complete the face-first stabilization workflow
2. reread current protected source blobs
3. if any blob changed, deliberately recompile `PAYLOAD.txt`
4. update this lock
5. begin a new final TEXT_ONLY stability batch

Do not silently patch `PAYLOAD.txt` during an active batch.
