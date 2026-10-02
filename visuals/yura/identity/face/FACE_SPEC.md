# 久遠ゆら FACE SPEC

Status: **PROTECTED / CURRENT / HARD-LOCKED**

This file is a direct execution constraint. Do not soften, average, beautify, reinterpret, or replace its geometry with generic anime defaults.

## HARD LOCK — face identity
The following must remain simultaneously true:
- visual age read = **15–18 years old**
- youthful teenage girl, but **not childlike**
- soft / refined / delicate
- clearly anime-stylized
- face is **small**
- face shape = **soft oval**
- face vertical length = **standard to slightly short**
- visible face remains **vertically compact**
- no vertically elongated / oblong impression
- face width = slightly narrow
- slight cheek softness
- cheekbones not emphasized
- contour narrows smoothly from temples / cheeks toward the chin
- lower face remains compact
- chin is **small, narrow, and softly rounded**
- face is not round / childlike
- face is not long / fashion-model-like
- no extreme V-line
- head remains slightly small inside the protected 7.25-head BODY balance

The target is a natural 15–18-year-old teenage facial read: youthful, calm and refined, without drifting toward either a younger child face or a mature adult face.

If the face becomes visibly rounder, sharper, longer, older, younger/childlike, wider-jawed, or more generic than this identity, treat it as **FACE FAIL**, not acceptable variation.

## Head / outline — geometry lock
Preserve:
- small face
- soft oval outer contour
- vertical face length = standard to slightly short
- eye-area-to-chin distance remains compact
- no vertically elongated / oblong impression
- slightly narrow face width
- modest cheek softness
- smooth taper from temples / cheeks toward the chin
- compact lower face
- small narrow softly rounded chin
- mature-teen-balanced head scale

Do not:
- enlarge the head to express petite stature or youth
- widen the lower face
- sharpen the jaw
- create a short round child face
- create a vertically elongated / oblong face
- create a long mature fashion-model face
- make the chin pointed
- inflate cheeks into a childlike round face
- create an extreme V-line

## Ear authority boundary
Ear size, placement guides, tilt, projection and visibility behavior are controlled only by:
`../ears/EAR_SPEC.md`

FACE geometry must not be modified to expose or enlarge an ear.
A hidden ear is allowed and does not imply missing anatomy.

## Face-detail visual anchor
Production YURA generation uses the dedicated Face Close-up Master defined by `../../gate/AUTHORITY_MANIFEST.md`.

The Face Close-up Master stabilizes:
- face outline
- cheek / chin balance
- eye placement
- nose / mouth placement
- naturally visible ear appearance, only when observable without compensation
- face-framing hair boundary

Precise FACE / EAR / EYE text rules remain authoritative for their domains.

If the dedicated Face Close-up Master is unavailable in PRODUCTION:
`GENERATION_ALLOWED = NO`

Do not substitute a derivative, previous-chat image, or similar face.

## Eyes — geometry only
Exact color and pupil identity are controlled by `../eyes/EYE_SPEC.md`.

Geometry lock:
- slightly larger than average, but balanced for a 15–18-year-old anime face
- horizontally elongated
- restrained vertical height
- mild almond shape
- clean gently curved upper eyelid
- shallow lower eyelid curve
- visible sclera remains on both sides of the iris
- outer corners neutral to very slightly downturned
- no circular / childlike oversized-eye reinterpretation
- no vertically oversized eye
- no sharp fox-eye reinterpretation
- no strong droop
- no narrow mature fashion-eye reinterpretation

## Brows
- fine
- cool gray / silver-gray compatible with hair
- nearly straight
- only a very gentle natural arch
- calm expression baseline
- brow tail does not kick sharply upward

Do not thicken or strongly arch the brows to create a different character impression.

## Nose
- very small and delicate
- narrow bridge
- low-to-medium bridge height
- softly readable in minimal 2D-anime shading
- must not disappear completely
- must not project strongly
- no realistic nostril detail
- no realistic nose-tip modeling

## Mouth / lips
- **very small and short mouth**
- closed by default
- lips thin to standard-thin
- soft natural pale pink
- neutral to extremely subtle soft expression by default
- mouth corners must not rise into a broad smile by default
- no glossy / volumetric realistic lips

## Default expression
- neutral to extremely soft
- calm
- gentle
- composed
- no broad smile by default
- no exaggerated cute / childlike expression

Expression derivatives may move brows / eyelids / mouth only.
They must not alter face geometry.

## Face framing boundary
Hair-specific structure remains controlled by `../hair/HAIR_SPEC.md`.

For FACE identity:
- thin long fringe may cross the forehead naturally
- long side bangs frame the cheeks / jaw area
- face framing must not widen or round the perceived face

## FAIL boundaries
FACE FAIL if materially present:
- childlike round face
- enlarged head
- broad lower face
- sharp jaw
- pointed chin
- extreme V-line
- vertically elongated / oblong face
- long mature fashion-model face
- visibly mature-adult facial read
- generic cute-anime face replacing YURA geometry
- strongly realistic nose / lips
- oversized symbolic anime eyes
- vertically oversized circular eyes
- sharp fox-eye
- strongly droopy childlike eye
- broad default smile changing the face impression
- EAR_SPEC violation used to alter the face or head for ear visibility
- facial geometry changes due to pose, outfit, lighting, or rendering

When in doubt, preserve the protected 15–18-year-old mature-teen geometry rather than adding expressive exaggeration.
