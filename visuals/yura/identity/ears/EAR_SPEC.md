# 久遠ゆら EAR SPEC

Status: **PROTECTED / CURRENT / HARD-LOCKED**

This file defines YURA's ear geometry, placement, tilt, projection, and visibility behavior.
Do not average it with generic anime-ear conventions or enlarge it for readability.

## HARD LOCK — size

YURA's ears are **slightly small**.

Vertical ear length:
- target = approximately **28–30% of the face vertical length**
- face vertical length reference = forehead to chin tip
- this corresponds to slightly smaller than the general one-third proportion
- **EAR LENGTH HAS PRIORITY over endpoint alignment**

Do not:
- enlarge the ear to make it easier to see
- lengthen it to force both the upper and lower placement guides to match
- reinterpret "slightly small" as standard-large
- create long / elf-like / vertically stretched ears

## Placement — guide, not absolute endpoint lock

Approximate placement guides:
- upper ear rim: around eyebrow height
- lower ear rim: around nose-tip to subnasal height

These are **placement guides only**.

They are not absolute locks on both endpoints.
If exact endpoint alignment would require changing the protected ear length:
- preserve the protected ear length
- allow the upper / lower alignment to vary naturally
- do not stretch the ear

## Tilt

Ear long axis:
- slightly tilted backward relative to vertical
- approximately **5–10 degrees posterior tilt**
- restrained and natural

Do not:
- rotate the ear toward camera for visibility
- flare the ear outward
- exaggerate the tilt

## Projection

- projection from the head = restrained
- ear stays visually close to the side of the head
- no outward displacement for readability
- no exaggerated rim exposure

## Visibility / occlusion — HARD LOCK

Ear visibility is determined by:
- camera angle
- actual head orientation
- hairstyle
- natural / local hair placement and occlusion

**The ear is allowed to be visible, partially hidden, or fully hidden.**

`HIDDEN != MISSING`

Visibility is not a target.
Hair placement is not locked for the purpose of ear visibility: local hair may naturally shift, separate, or settle so the ear becomes more or less visible.
Do not require the hair to expose the ear, and do not require the hair to hide the ear.

Strictly forbidden:
- rotating the head merely to reveal the ear
- rotating the ear toward camera
- moving the ear outward
- enlarging / lengthening the ear because it is hidden
- exposing both ears for symmetry
- increasing ear size / projection / rotation for readability
- any other visibility-driven EAR or head-geometry compensation

If the ear is hidden, preserve the protected EAR geometry without enlarging it.
If the ear is visible because of natural hair placement, keep the same protected EAR geometry.

## Relationship to FACE / HAIR

- FACE controls face geometry, not ear size
- HAIR controls source hair structure, length and mass; local placement around the ear may vary naturally
- EAR_SPEC controls ear size / placement guide / tilt / projection / visibility behavior

FACE geometry must not be modified to make the ear visible.
HAIR source length / mass / identity must not be changed for ear visibility, but local hair placement around the ear may vary.

## HARD FAIL

EAR FAIL if materially present:
- ear visibly too large relative to the face
- ear vertical length materially exceeds the slightly-small target
- long / stretched ear
- outward-flared ear
- excessive projection from the head
- endpoint alignment achieved by stretching the ear
- source hair length / mass / identity changed to expose the ear
- head rotated merely to expose the ear
- ear rotated toward camera for readability
- ear enlarged because it is partially hidden
- forced bilateral ear visibility
- any visibility-driven ear enlargement, displacement, projection increase or rotation

Never change FACE or HAIR canon to rescue an ear-visibility failure.
