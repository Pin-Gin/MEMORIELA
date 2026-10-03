# YURA FACE ROOT GEOMETRY REFINEMENT SOURCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / SOURCE INTEGRITY LOCK**

This file is **NOT image-generation input**.

Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Protected-source snapshot validated at commit: `de3680344730a30aa090b9c546f7dc07f68f94f1`
Payload creation commit: `0e99a053ed866ff061a59393e4660da612f7c1d0`
Payload blob: `ea35806883a92aedc733984cc92587327be69d38`

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
- image-edit instruction for an eligible Face Root candidate

It intentionally does not compile:
- BODY geometry
- full hair length
- validation clothing
- full-body pose
- scene / production reference semantics

## Runtime edit-source lock
The edit source is not a protected semantic source and is not Authority.
It is a runtime `EDIT_SOURCE_CARRIER` only.

Before every execution:
- candidate must be `REFINEMENT_ELIGIBLE`
- exact actual image must be available
- exact runtime SHA-256 must be recorded in the Load Receipt
- no other image may be supplied

The runtime candidate hash is intentionally not stored as Canon in this source lock.

## Recompile trigger
If any protected source blob above changes:
`FACE_ROOT_REFINEMENT_PAYLOAD_SOURCE_LOCK = STALE`
`GENERATION_ALLOWED = NO`

Before the next protected refinement execution:
1. reread changed Authority
2. deliberately recompile `PAYLOAD.txt`
3. update this lock
4. start a new refinement batch

If only the runtime eligible edit-source candidate changes, do not rewrite protected Canon; instead complete a new Load Receipt with that candidate's exact hash and eligibility.
