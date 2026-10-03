# YURA FACE-ANCHORED ROOT SOURCE / REFERENCE LOCK

Status: **PROTECTED / CONTROLLER-ONLY / BLOCKED PENDING FACE ROOT ADOPTION**

This file is **NOT image-generation input**.

Repository: `Pin-Gin/MEMORIELA`
Branch: `main`
Payload creation commit: `82ef374dcb0fd2a29614fa1b6b153eef215a66ad`
Payload blob: `0a4d89743a2e006119913510f99102d002bb4cd6`

## Required Face Root dependency
Expected image:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.png`

Expected manifest:
`visuals/yura/identity/master/face-root/YURA_FACE_ROOT.md`

Required role:
`FACE_DETAIL_REFERENCE`

Current state:
`FACE_ROOT_APPROVED = NO`
`FACE_ROOT_IMAGE_HASH = UNRESOLVED`
`FACE_ROOT_MANIFEST_HASH = UNRESOLVED`
`FACE_ANCHORED_ROOT_GENERATION_ALLOWED = NO`

Do not replace these values by inference.
Do not use any previous full-body generation, repository Root Master PNG, or unapproved face candidate as fallback.

## Protected text source blobs
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

## Activation procedure
Only after explicit author approval of a Face Root candidate:
1. place exact approved PNG at the expected path
2. create `YURA_FACE_ROOT.md` with image hash / author approval / FACE_DETAIL_REFERENCE role
3. reread current protected text source blobs
4. record exact Face Root image hash and manifest blob here
5. confirm the actual image is available to generation
6. set `FACE_ROOT_APPROVED = YES`
7. set `FACE_ANCHORED_ROOT_GENERATION_ALLOWED = YES`

Any changed protected text source requires deliberate payload recompile before activation.
