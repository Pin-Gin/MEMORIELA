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

Ear visibility is determined only by:
- camera angle
- actual head orientation
- hairstyle
- natural hair occlusion

**The ear is allowed to be partially hidden or fully hidden.**

`HIDDEN != MISSING`

Visibility is not a target.

Strictly forbidden:
- moving hair away to reveal the ear
- thinning / separating hair to expose the ear
- rotating the head merely to reveal the ear
- rotating the ear toward camera
- moving the ear outward
- enlarging / lengthening the ear because it is hidden
- exposing both ears for symmetry
- increasing visible ear area for readability
- any other show-ear compensation

If the natural camera / head / hair relationship hides the ear, keep it hidden.

## Relationship to FACE / HAIR

- FACE controls face geometry, not ear size
- HAIR controls hair structure and natural occlusion, not ear exposure
- EAR_SPEC controls ear size / placement guide / tilt / projection / visibility behavior

FACE or HAIR must not be modified to make the ear visible.

## HARD FAIL

EAR FAIL if materially present:
- ear visibly too large relative to the face
- ear vertical length materially exceeds the slightly-small target
- long / stretched ear
- outward-flared ear
- excessive projection from the head
- endpoint alignment achieved by stretching the ear
- hair moved / thinned / separated to expose the ear
- head rotated merely to expose the ear
- ear rotated toward camera for readability
- ear enlarged because it is partially hidden
- forced bilateral ear visibility
- any visibility-driven ear enlargement or displacement

Never change FACE or HAIR canon to rescue an ear-visibility failure.
