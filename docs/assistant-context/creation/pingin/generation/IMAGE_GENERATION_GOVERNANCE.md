# PINGIN Image Generation Governance

Status: **CANONICAL / MANDATORY GENERATION WORKFLOW**
Adopted: 2026-09-19
Character: ぴんぎん (Pin-Gin)
Parent identity authority:
`docs/assistant-context/creation/pingin/identity/VISUAL_IDENTITY.md`

Purpose: ぴんぎんをサムネイル、ロゴ派生、日常イラスト、YURA共演、将来の漫画で長期運用しても別個体化しないよう、生成前参照・差分設計・生成後QAを固定する。

## 1. Absolute generation procedure

Material ぴんぎん generation must follow this order:

**Git protected text**
→ **manually attached canonical MASTER visual**
→ **current derivative request**
→ **generation**
→ **identity / derivative QA**

Mandatory ordinary-generation rules:

1. Read `docs/assistant-context/creation/pingin/identity/VISUAL_IDENTITY.md`.
2. Read `docs/assistant-context/creation/pingin/identity/master/VISUAL_MASTER.md`.
3. Read current BODY authority: `docs/assistant-context/creation/pingin/identity/BODY_SPEC.md`.
4. Read `docs/assistant-context/creation/pingin/generation/VISUAL_TEXT_REFERENCE.md`.
5. Visually inspect the manually attached exact canonical `PINGIN_VISUAL_MASTER.png`.
6. When technically practical, verify attached bytes against the MASTER SHA-256 recorded in `docs/assistant-context/creation/pingin/identity/master/VISUAL_MASTER.md`.
7. Apply only the requested derivative variables.
8. Generate.
9. QA against the attached MASTER + protected text + current request.
10. Reject or retry any output with material identity drift.

Do not reconstruct ぴんぎん from chat memory alone.
Do not use an arbitrary derivative as identity authority.
Do not promote a successful derivative to MASTER without explicit approval.

Supporting `PINGIN_VISUAL_REFERENCE.png` is secondary. Read/inspect it when side/back continuity, existing expression examples, or winter-accessory detail materially helps the task. It is not mandatory for every ordinary front/scene generation when the canonical MASTER is attached.

## 2. Visual transport / new-chat policy

Current approved operating mode is **manual MASTER attachment**.

New-chat reproduction path:

1. the canonical PNG remains the Git-owned target artifact at:
   `docs/assistant-context/creation/pingin/identity/master/PINGIN_VISUAL_MASTER.png`
2. the user manually attaches that exact MASTER image to the new chat
3. the assistant reads the protected Git text authorities
4. the attached MASTER supplies visual identity
5. the Git text supplies anti-drift / derivative constraints

A future SHA-verified bridge may be added for automation, but it is **not required for the current approved manual-attachment workflow**.

If no canonical MASTER is attached and the environment cannot visually inspect the Git PNG, do not silently substitute memory or a random derivative. Ask for the canonical MASTER attachment or use an explicitly approved recovery method.

The manual attachment is a transport copy only. The canonical identity remains the approved MASTER recorded by Git manifest/spec.

## 3. Pose policy

Default production strategy:
- simple, readable poses
- small silhouette changes
- expression-led variation
- no complex action pose unless the story explicitly needs it

Preferred camera/body directions:
- front
- mild front three-quarter
- side
- mild rear three-quarter when needed for manga continuity

Avoid as routine assets:
- acrobatics
- extreme foreshortening
- complex multi-limb contact
- anthropomorphic human hand gestures
- standing upright like a human with long legs

Flippers remain flippers. Gestures are created by flipper angle, head tilt, body lean, eye/eyelid change and scene placement.

## 4. Core expression library

The following are approved production categories. They are expression derivatives, not identity changes.

1. **Neutral / listening**
   - relaxed eyes
   - neutral beak
   - balanced posture

2. **Gentle smile**
   - softened / slightly closed eyes
   - light cheek warmth
   - minimal body lift

3. **Happy / broad smile**
   - closed smiling eyes allowed
   - stronger cheek expression
   - flippers may lift slightly

4. **Amused / chuckle**
   - asymmetrical soft eye response
   - small forward body lean

5. **Surprised**
   - widened eyes
   - slight head/body recoil
   - beak may open slightly

6. **Confused / question**
   - head tilt
   - one eyelid/brow cue or question-mark scene symbol allowed
   - do not redesign eye geometry

7. **Thinking**
   - mild head tilt/downward gaze
   - one flipper near lower face/beak is allowed
   - no human chin-grab hand pose

8. **Worried / troubled**
   - softened downturned eyelid cues
   - compact posture
   - slight inward flipper position

9. **Sad / disappointed**
   - lowered gaze
   - subdued posture
   - avoid melodramatic human tears as default

10. **Irritated / side-eye**
    - narrowed eyelids
    - slight head turn
    - restrained, comic-readable annoyance

11. **Angry / glare**
    - stronger narrowed eyes
    - forward-facing compact posture
    - never transform the face into a different sharp/aggressive species design

12. **Embarrassed / shy**
    - stronger blush
    - eyes averted or gently closed
    - slight body turn

13. **Sleepy**
    - drooped eyelids
    - lowered head
    - may lean on desk/cushion

14. **Satisfied / smug-lite**
    - half-lidded eyes
    - small lifted posture
    - restrained; avoid villain-like redesign

## 5. Manga / thumbnail utility scene library

Priority is reusable situational difference, not elaborate posing.

### Primary production assets

- standard standing / neutral
- standing / speaking-listening reaction
- mild side view looking up toward YURA or another taller character
- seated at PC / neutral
- seated at PC / focused on screen
- seated at PC / working with flippers positioned naturally near keyboard or desk
- seated at PC / tired-slumped
- thinking beside or in front of PC
- sleeping / dozing on desk
- reading a book / paper / screen
- beside a mug or drink
- peeking from behind monitor / panel / object
- mild flipper-point / indicating gesture
- eating / \"もぐもぐ\" simple food scene

### PC-specific rules

- use a small desk / keyboard / monitor scaled to the scene
- do not give ぴんぎん human fingers for typing
- flippers may rest near or tap the keyboard in simplified mascot logic
- seated body remains round and low; do not create a human hip/knee sitting anatomy
- monitor/desk must not hide so much of the character that identity cannot be checked unless the panel specifically requires it

### Manga continuity rule

For repeated panels:
- preserve body scale, face geometry and accessory mode
- change only expression, gaze, small flipper position, head tilt and body lean where possible
- reuse the same camera axis for dialogue sequences when practical
- do not let ぴんぎん gradually become taller, slimmer, more human or more baby-like across panels

## 6. Seasonal routing

Use scene context, not arbitrary date assumptions.

- cold-weather scene → thick blue-gray striped muffler + restrained floral ornament
- warm-weather / summer scene → thin compact blue-gray neckerchief + restrained floral ornament
- ambiguous mild weather → use the option already established by the current sequence; if no sequence exists, use neckerchief as the lighter default derivative
- no third permanent seasonal design without explicit approval

MASTER remains season-neutral and wears neither.

## 7. Logo / silhouette usage

For MEMORIELA logo derivatives:
- the official primary MEMORIELA logo remains independent
- ぴんぎん may appear in extended/key-visual versions as a subtle background silhouette or secondary motif
- silhouette must preserve the protected round body / crown tuft / short-flipper identity
- do not make a seasonal muffler the only silhouette identifier
- do not reduce logo readability

## 8. Generation QA

Evaluate each material output independently.

### Gate 1 — Identity
PASS only when:
- same round silhouette
- same face-mask relationship
- same crown tuft
- same short beak / rounded feet / short flippers
- same core palette
- no species or human-body drift

### Gate 2 — Rendering
PASS only when:
- soft 2D illustration identity is preserved
- no dominant photoreal / 3D / glossy toy look
- no infant mascot redesign

### Gate 3 — Seasonal accessory
PASS only when:
- correct muffler or neckerchief mode is used
- accessory weight matches season
- floral accent is restrained
- accessory does not hide identity

### Gate 4 — Expression / pose request
PASS only when:
- requested expression reads clearly
- pose remains simple and physically coherent for the mascot body
- no human hands/fingers are invented

### Gate 5 — Scene / prop hygiene
PASS only when:
- PC / desk / mug / book etc. are not malformed enough to distract
- no unintended text/logo
- no duplicate flippers / feet / props

### Gate 6 — Batch continuity
For manga / expression batches:
- same ぴんぎん across all assets
- only intended expression/pose variables change
- no gradual scale, face or rendering drift

Final states:
- **PRODUCTION PASS**
- **LOCAL REPAIR**
- **TARGETED RETRY**
- **REJECT — IDENTITY DRIFT**
- **BLOCKED — MASTER/REFERENCE NOT RECOVERABLE**

## 9. MASTER adoption status

Completed:
1. neutral MASTER candidate generated
2. user explicitly approved gen_id `93344db6-b23c-4c8c-868d-fbab56a7cc54`
3. BODY v1.0 promoted
4. MASTER manifest created
5. integrated Visual Text v1.0 created
6. manual-attachment new-chat workflow fixed

Remaining repository step:
- manually place the approved PNG at `docs/assistant-context/creation/pingin/identity/master/PINGIN_VISUAL_MASTER.png`
- then record its Git blob SHA in `docs/assistant-context/creation/pingin/identity/master/VISUAL_MASTER.md`

The approved image must not be regenerated merely to replace this manual Git binary placement step.

## 10. Change control

Do not silently change:
- MASTER-first identity order
- manual canonical MASTER attachment requirement for ordinary new-chat reproduction
- expression-led/simple-pose strategy
- seasonal muffler / neckerchief split
- mascot anatomy
- rendering direction
- QA identity gate

Material changes require explicit user approval and Git update.
