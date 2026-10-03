# YURA FACE-ANCHORED ROOT QA

Status: **PROTECTED / MANDATORY FOR FACE_ANCHORED_ROOT_MASTER**

Purpose:
承認済みFace RootをFACE_DETAIL_REFERENCEとして使用した全身Root候補が、顔Identityを保持しつつBODY / HAIR / clothing / pose / renderingを保護テキスト通りに展開できているかを判定する。

## Gate 0 — Execution integrity
PASS only if:
- submode = `FACE_ANCHORED_ROOT_MASTER`
- exact `face-anchored-root/PAYLOAD.txt` used
- exact approved Face Root image attached as the only `FACE_DETAIL_REFERENCE`
- Face Root image hash matches `SOURCE_LOCK.md`
- no other visual reference attached
- actual Face Root image reached generation execution
- one YURA / one figure / one canvas / one composition

## Gate 1 — Face carrier fidelity
PASS only if the full-body candidate preserves the Face Root in:
- face outline
- cheek / chin balance
- eye identity / placement
- nose / mouth placement
- ear geometry
- face-framing hair boundary

FAIL:
- long / oblong face drift from Face Root
- generic anime face replacement
- eye identity shift
- ear enlargement / lengthening / outward displacement / camera-facing rotation
- face reference causing head enlargement relative to protected BODY

## Gate 2 — Reference scope separation
PASS only if Face Root did **not** redefine:
- BODY ratio
- shoulder / ribcage width
- chest
- waist / pelvis / legs
- full hair length
- validation clothing
- pose
- rendering style

Any reference-scope leakage = execution-integrity FAIL.

## Gate 3 — BODY
Apply current BODY authority:
- exact 7.25 heads
- petite / slender
- somewhat narrow shoulders
- compact ribcage
- clearly fuller relative chest without torso widening
- slim natural waist
- natural restrained hips
- slender limbs with natural softness

## Gate 4 — HAIR full-length
PASS:
- silver-white
- principal dense mass through waist into upper-hip / hip-bone region
- clear taper through upper hip
- only sparse finest tips toward very upper-thigh boundary
- no dense curtain at mid-thigh or lower
- face-framing boundary compatible with Face Root

## Gate 5 — Validation clothing / pose
PASS:
- pale fitted tank-style sleeveless top with medium-width integrated shoulder panels
- rounded scoop neckline
- pale fitted simple shorts
- no drawstring / bow / lace / ornament
- barefoot
- front-facing full body
- upright neutral standing
- arms naturally lowered
- hands near outer thighs
- legs nearly together
- white / warm-white background

## Gate 6 — RENDERING
PASS only if:
- high-quality 2D anime
- Matte Natural Anime
- clean fine but clearly readable linework
- readable grouped soft-cel shadow shapes
- mild diffuse gradients only as support
- low-to-medium contrast, not washed-out ultra-low contrast
- face / skin / silver-white hair / pale clothing remain separated from white background
- hair reads as grouped anime masses, not translucent fiber haze
- matte / low-gloss
- not watercolor-like / pastel-faded / ethereal-faded

Photoreal / semi-photoreal / CGI / PBR = HARD FAIL.

## Decision
PASS requires all gates.

A passing candidate is still not Authority until explicit author approval.

This mode stabilizes production identity but does not count as final reference-free TEXT_ONLY success.
