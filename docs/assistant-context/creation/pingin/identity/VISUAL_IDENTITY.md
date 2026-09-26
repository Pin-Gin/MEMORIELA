# PINGIN Visual Identity Master

Status: **PROTECTED CHARACTER IDENTITY / CURRENT SPEC**
Character: ぴんぎん (Pin-Gin)
Updated: 2026-09-20
Master artifact status: **APPROVED / REPOSITORY PNG PLACEMENT PENDING**

## 1. Identity

- Public avatar / public form of Pin-Gin.
- Character name: **ぴんぎん (Pin-Gin)**.
- ぴんぎん represents the user in visual works, thumbnails, logos, illustrations and future manga.
- Character motif: a small deformed penguin with a soft plush-like visual texture.
- The plush-like appearance is a rendering/design quality; ぴんぎん is treated as an active avatar character, not an inanimate toy.
- Tone: friendly, calm, cozy and adult-facing. Cute, but not an infant/baby mascot.

## 2. Protected core appearance

The following define ぴんぎん and must remain stable across derivatives unless the user explicitly changes canon:

- very round compact body with low center of gravity
- small rounded head/body silhouette with no long neck
- dark charcoal to soft black outer plumage/body
- warm ivory-white face mask and belly
- warm yellow-orange short beak
- warm yellow-orange rounded feet; simplified, no claws
- short rounded flippers; **never human hands or fingers**
- small soft cheek blush
- small feather tuft on the crown
- small rear tail visible when the angle allows
- small, gentle dark eyes; expressions may change eyelids/eye shape but must preserve the same face identity
- overall silhouette must still read immediately as the same ぴんぎん when accessories are removed

Species-drift prohibition:
- do not turn ぴんぎん into a chick, duck, realistic penguin, generic bird mascot or human-bodied kemono character
- do not add human fingers, human arms, long legs, claws or a long duck-like bill

## 3. Scale policy

Protected physical-size range:
- approximately **15–50 cm tall**

There is no single mandatory default height inside this range. The concrete size may be selected per scene, composition, thumbnail, illustration or interaction requirement.

Rules:
- any size from approximately 15 cm through 50 cm is valid without changing character identity
- scale changes are uniform; do not redesign head/body ratio, face geometry, flippers, feet or beak
- size selection must serve scene readability / interaction rather than create a new body design
- within a manga scene/sequence, relative scale must remain consistent between panels unless an explicit visual gag or explicit scene requirement changes it

## 4. Rendering identity

Canonical direction:
- **2D illustration-first**
- soft hand-painted / gently textured illustration
- subtle plush-like feather/fabric softness
- delicate low-contrast linework
- soft grouped shading
- restrained warm blush
- subdued, elegant color handling
- low photographic realism
- low CGI / 3D-render feeling
- readable at small thumbnail/icon size

Avoid:
- photoreal penguin rendering
- glossy PBR / toy-product 3D rendering
- hard plastic/vinyl texture
- heavy black manga outlines as the default master style
- hyper-detailed individual feather fibers
- baby-chick proportions or giant infant-like eyes

## 5. Protected identity motif and seasonal neckwear

The protected motif is **blue-gray neck styling + restrained floral ornament**, not one all-season winter scarf.

### Cold-weather mode
- thick, soft **blue-gray striped muffler/scarf**
- restrained stripe contrast
- small gold-toned floral ornament / clasp
- cozy but not oversized enough to hide the face or body identity

### Warm-weather / summer mode
- small, lightweight **blue-gray neckerchief**
- thin fabric, compact knot or fold
- visually cool/light, never winter-weight
- same restrained floral motif may appear as a small clasp or accent

### Spring / autumn routing
- choose cold-weather muffler or warm-weather neckerchief according to scene temperature / clothing context
- do **not** invent a third permanent seasonal neck design without explicit approval

Accessory rules:
- season changes neckwear only; they do not change ぴんぎん's body, face, palette or proportions
- floral motif remains small and secondary
- neckwear is a derivative layer and must never become the sole identity anchor

## 6. Canonical image architecture

Future production must use two image authorities with distinct roles.

### A. Canonical identity master
Target path:
`docs/assistant-context/creation/pingin/identity/master/PINGIN_VISUAL_MASTER.png`

Manifest:
`docs/assistant-context/creation/pingin/identity/master/VISUAL_MASTER.md`

Approved source:
- gen_id: `93344db6-b23c-4c8c-868d-fbab56a7cc54`
- exported PNG SHA-256: `5322c41532ed163adba40ff2e9ea864ac82f8eaac6149ef770d79b8571c55dc0`
- explicit user approval: **「はい、この立ち絵で確定します！」**

Role:
- one canonical ぴんぎん
- neutral whole-character identity / proportions / face / core palette / body silhouette
- primary visual identity authority

Approved MASTER condition:
- exactly one ぴんぎん
- front-facing
- full body visible
- upright on both feet
- neutral-soft expression
- plain white background
- no text, logo, panels, props or scene
- no seasonal neckwear
- no floral accessory
- no dynamic pose

### B. Supporting visual reference sheet
Target path:
`docs/assistant-context/creation/pingin/reference-materials/PINGIN_VISUAL_REFERENCE.png`

Source:
- the currently approved ぴんぎん character-design sheet already used as the visual basis in this project
- it contains the approved soft illustration atmosphere, front / side / back continuity, expression examples, detail examples and the cold-weather muffler look

Role:
- rendering texture / atmosphere cross-check
- front / side / back continuity
- approved facial-expression vocabulary
- detail / proportion cross-check
- cold-weather muffler reference

The current design sheet does **not** canonize winter neckwear for all seasons. Warm-weather neckerchief behavior is defined by this text specification and future approved derivatives.

Do not generate a redundant replacement character sheet merely to duplicate the same information. The supporting reference never overrides the canonical master or this text specification.

Authority when conflict exists:
1. latest explicit finalized user decision
2. this protected identity specification
3. current canonical `PINGIN_VISUAL_MASTER.png` + `docs/assistant-context/creation/pingin/identity/master/VISUAL_MASTER.md`
4. `docs/assistant-context/creation/pingin/identity/BODY_SPEC.md`
5. `docs/assistant-context/creation/pingin/generation/VISUAL_TEXT_REFERENCE.md`
6. supporting `PINGIN_VISUAL_REFERENCE.png` when available
7. current derivative request
8. older derivatives / chat memory

## 7. Master replacement rule

A derivative image never becomes a new master automatically.

Replacing `PINGIN_VISUAL_MASTER.png` requires:
- explicit user approval
- repository replacement
- new Git blob SHA recorded in a master manifest/adoption record
- reason for replacement
- confirmation that supporting reference and generation governance still agree

## 8. Interaction with YURA

When ぴんぎん appears with 久遠ゆら:

- preserve YURA and ぴんぎん as separate identities
- YURA identity follows the current YURA protected authorities
- ぴんぎん identity follows this file and its current master/reference
- do not inherit YURA anatomy or anime-human proportions into ぴんぎん
- do not use ぴんぎん as a replacement for YURA's Persona or visual identity

## 9. Change control

Protected without explicit user approval:
- current approved MASTER identity
- core species / silhouette
- face identity
- body proportions
- core palette
- crown tuft
- beak/feet design direction
- short rounded flippers
- 2D soft illustration direction
- seasonal system: cold muffler / warm neckerchief
- restrained blue-gray + floral accessory language

Normal derivative variables:
- expression
- gaze
- simple pose
- scene
- prop
- camera/framing
- cold/warm neckwear selection
- uniform physical scale within the allowed scale policy
