# YURA TEXT-ONLY FACE ROOT SOURCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / SOURCE INTEGRITY LOCK**

This file is **NOT image-generation input**.

Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Base commit used for this compile: `33f317a1adc61cd8c1974c3536ffa6255c82c6f4`
Payload creation commit: `c09f4b53c22a9294f7152727500f352f373dd85e`
Payload blob: `94d629feb5239b241bbf667483d2a236cb0e00c8`

## Protected source blobs
- `visuals/yura/identity/master/YURA_VISUAL_TEXT.md` — `2ede5c28484f8de787724cec31bbb9ffffabde21`
- `visuals/yura/identity/face/FACE_SPEC.md` — `ecfcbf2b95216c54d6390b19b8fdbd664740b14e`
- `visuals/yura/identity/ears/EAR_SPEC.md` — `f5c61c138c051ebd4aebf7d01c1c140afea3b655`
- `visuals/yura/identity/eyes/EYE_SPEC.md` — `53cc19918471e3b54c77ea1b1db43293bee98f57`
- `visuals/yura/identity/hair/HAIR_SPEC.md` — `a1f259ee396f192aad635e7b7f4433822981e1f0`
- `visuals/yura/identity/skin/SKIN_SPEC.md` — `22860c4d0b1a2a20612d4c83fd5a0e17a746e83b`
- `visuals/yura/identity/rendering/YURA_RENDERING_SPEC.md` — `365cf79a475619c14d8d0e3d73b7f0aaa8c4912f`
- `visuals/CHARACTER_RENDERING_STYLE.md` — `345e779c72664a50e2f099199a3950e0115576b8`

## Scope lock
This payload compiles only:
- FACE
- EYE
- EAR
- face-framing HAIR / hair color / hair material
- SKIN
- RENDERING
- face-close-up composition

It intentionally does not compile:
- BODY geometry
- full hair length
- validation clothing
- full-body pose
- scene / production reference semantics

## Recompile trigger
If any protected source blob above changes:
`FACE_ROOT_PAYLOAD_SOURCE_LOCK = STALE`
`GENERATION_ALLOWED = NO`

Before the next protected Face Root generation:
1. reread changed Authority
2. deliberately recompile `PAYLOAD.txt`
3. update this lock
4. start a new Face Root batch
