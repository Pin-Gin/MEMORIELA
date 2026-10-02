# 久遠ゆら FACE SPEC

Status: **PROTECTED / CURRENT**

## Core impression
- adult woman
- soft, refined, delicate
- clearly anime-stylized, not childlike and not semi-realistic

## Head / outline
- head slightly small within the 7.25-head adult body balance
- face: soft oval
- not excessively long
- not round/childlike
- cheeks retain slight softness
- cheekbones are not emphasized
- contour narrows smoothly from below the ears toward the chin
- chin: **small and softly rounded**
- no extreme V-line

## Ears — protected geometry / visibility lock
- Ear anatomy is stable: preserve attachment height, overall scale, projection from the head and general silhouette.
- Ear visibility is determined only by actual head angle, camera angle and hair occlusion.
- Do not enlarge ears, move them outward, rotate them toward camera or move surrounding hair merely to make ears easier to see.
- Do not expose both ears for symmetry.
- Do not increase visible ear area for readability.
- A naturally hidden ear must remain hidden.
- Partial occlusion and natural left-right visibility differences are valid.
- `HIDDEN != MISSING`. Ear visibility itself is not a generation target.

## Face-detail visual anchor
- Production YURA generation uses the dedicated Face Close-up Master defined by `../../gate/AUTHORITY_MANIFEST.md`.
- The Face Close-up Master stabilizes face outline, cheek/chin balance, eye placement, nose/mouth placement, ear geometry and face-framing hair boundary.
- Precise FACE / EYE text specifications remain authoritative for their own domains.
- If the dedicated Face Close-up Master is unavailable, PRODUCTION must stop; do not replace it with a derivative or prior-chat image.

## Eyes
Exact color and pupil signature are controlled by `../eyes/EYE_SPEC.md`.

Geometry:
- slightly larger than average, but adult-balanced
- mild almond shape
- slightly horizontal rather than vertically oversized
- outer corners neutral to very slightly downturned
- no fox-eye reinterpretation
- no strongly droopy childlike eye

## Brows
- fine to standard-fine
- cool gray / silver-gray compatible with hair
- nearly straight with a very gentle natural arch
- calm expression baseline

## Nose
- small and delicate
- narrow bridge
- low-to-medium bridge height
- softly readable in 2D shading
- not flat to the point of disappearing
- not strongly projecting / fashion-model-like
- no realistic nostril detail

## Mouth / lips
- small mouth
- lips thin to standard
- soft natural pale pink
- neutral to very slight smile by default
- no glossy / volumetric realistic lips

## Default expression
- neutral to very soft expression
- calm, gentle, composed
- expression derivatives may move brows / eyelids / mouth while preserving facial geometry

## Fail boundaries
FAIL if materially present:
- childlike round face
- extreme V-line
- long mature fashion-model face
- strongly realistic nose/lips
- oversized symbolic anime eyes
- sharp fox-eye reinterpretation
- facial geometry changes due to pose, outfit or lighting
