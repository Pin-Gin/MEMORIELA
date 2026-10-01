# YURA Eye Signature Spec

Status: PROTECTED IDENTITY SIGNATURE
Current Revision: **v1.2**
Adopted: 2026-09-12
Updated: 2026-09-25 — v1.1 orientation / application resolved by explicit Owner decision (`CREATE-YURA-20260925-001`)
Updated: 2026-09-25 — v1.2 notch form (protrusion, not indentation) resolved by explicit Owner decision (`CREATE-YURA-20260925-003`)
Character: 久遠ゆら / YURA
Purpose: YURA固有の瞳内識別意匠を、通常のFACE細部より一段上のprotected identity signatureとして固定し、2D化・立ち絵量産・イベントCG・画角変更を跨いでも意図せず消失 / 別意匠化しないための正本。

## 1. Authority

This specification protects the YURA-specific pupil signature originally defined in `visuals/yura/identity/face/FACE_SPEC.md` section 2.8.

The signature is part of YURA's visual identity and must not be silently removed, mirrored, enlarged into a decorative symbol, or replaced by another pupil motif.

It does not replace the full eye geometry in `visuals/yura/identity/face/FACE_SPEC.md`; it elevates the identifying pupil detail to a separately protected rule.

## 2. Protected signature geometry

YURA's pupil baseline remains:

- very dark blue-gray to deep gray, close to black but not flat pure black
- natural / moderate pupil size
- almost circular
- very subtly vertically elongated

Protected identifying detail:

- add an **extremely small teardrop-like notch on the lower-right edge of the pupil**
- the notch must remain integrated into the pupil edge rather than floating inside the iris
- it must be subtle enough that the pupil still reads as natural at ordinary viewing size
- it should become clearly inspectable mainly in close-up / high-resolution face views
- do not convert it into a heart, star, crescent, logo, rune, obvious droplet icon, or conspicuous fantasy pupil
- do not add a matching notch on the opposite side unless a later explicit protected revision says so

The lower-right orientation follows the existing FACE specification. If a future controlled visual validation reveals orientation ambiguity, do not silently flip it; resolve the orientation explicitly with the user and update this protected specification.

### 2.1 Orientation / application — resolved 2026-09-25

Explicit Owner decision 2026-09-25:

- **Orientation:** "lower-right" means **lower-right as seen by the viewer** (viewer-relative), judged on the neutral front-facing face.
- **Application:** **both eyes**. Each pupil carries one notch, and in the neutral front-facing view each notch appears at the pupil's lower-right as seen by the viewer.

This resolves the orientation ambiguity noted above. It does not change the notch's size, shape, subtlety or scale-dependent visibility rules.

"do not add a matching notch on the opposite side" continues to mean: no second notch on the opposite edge of the same pupil.

### 2.2 Form (polarity) — resolved 2026-09-25

Explicit Owner decision 2026-09-25:

- The "teardrop-like notch" is a **small dark teardrop-like part of the pupil that protrudes from the pupil edge outward into the iris**.
- It is continuous with the pupil in colour and attached to the pupil edge; this is what "integrated into the pupil edge rather than floating inside the iris" means.
- It is **not** an indentation / cut into the pupil through which the iris colour shows.

The reversed form (an indentation into the pupil) is a replacement of the signature, i.e. eye-signature drift under §8.

This does not change the notch's orientation / application (§2.1), extremely small size, subtlety or scale-dependent visibility rules.

## 3. Visibility by framing / asset type

The signature is a protected design rule, but its **visible readability depends on image scale**.

### Close-up / face CG / event CG

- the notch should be intentionally preserved
- it should be inspectable when the eye is large enough in the final asset
- do not omit it merely because the rendering style is more strongly 2D / anime-oriented

### Bust-up / medium portrait / dialogue CG

- preserve the notch when practical
- it may remain extremely subtle
- do not enlarge it beyond the protected scale merely to make it obvious

### Full-body standing image / small UI sprite / thumbnail

- the underlying design remains protected even if the notch is not visibly resolvable at final display size
- do not enlarge or exaggerate the notch to force visibility
- absence of visible readability caused purely by scale / raster resolution is **not by itself identity drift**
- when producing a higher-resolution master source for such assets, preserve the intended pupil signature where practical

## 4. Rendering-style invariance

The signature survives rendering-style refinement inside the current protected YURA rendering grammar.

Changing from a more modeled look to the current high-quality 2D anime illustration style must not be interpreted as permission to remove the signature.

The following may change naturally with scene rendering:

- highlight position
- iris brightness
- local contrast
- apparent sharpness due scale / depth of field

The following must not change silently:

- existence of the lower-right pupil notch as YURA's identity cue
- notch side / orientation
- conversion into another symbolic pupil design

## 5. Relationship to highlights / iris detail

The notch is independent from scene-light highlights.

- primary + secondary eye highlights may move naturally with lighting
- the pupil notch is a character-design feature, not a light reflection
- do not erase or relocate the notch merely to accommodate a highlight
- do not confuse the notch with a specular sparkle or iris reflection

## 6. Purpose / anti-copy limitation

This signature functions as:

- a discreet YURA-specific visual identity marker
- a provenance-supporting design cue
- a consistency check in close-up assets

It is **not** a cryptographic watermark, invisible watermark, forensic fingerprint, or guaranteed anti-copy mechanism.

A copied image can still be copied. The value of this feature is that approved YURA artwork contains a small, deliberate, repeatable identifying design detail that can support visual provenance and identity consistency.

## 7. Generation rule

When generating YURA and the face / eyes are large enough for pupil detail to matter:

1. load / respect the current YURA MASTER and FACE specification
2. preserve the protected blue-gray eye identity
3. preserve the dark, subtly vertically elongated pupil
4. include the extremely small lower-right teardrop-like pupil-edge notch
5. keep it discreet and natural
6. never sacrifice overall eye anatomy to make the notch conspicuous

For full-body or small-scale outputs, identity and natural eye rendering take priority over artificially enlarging the notch.

## 8. Validation rule

When reviewing a derivative:

- close-up missing / mirrored / replaced signature = eye-signature drift and should be corrected
- full-body image where the notch is simply below visible resolution = not automatically a failure
- repeated close-up failure to preserve the signature should trigger prompt / face-generation correction, not redesign of the signature itself

## 9. Change control

Status: PROTECTED.

Do not remove, mirror, replace, or materially resize the YURA eye signature without explicit user approval.

Any future revision must record:

- explicit user approval
- exact geometry / orientation change
- reason for the change
- relationship to `visuals/yura/identity/face/FACE_SPEC.md`
- impact on existing standing CG / close-up / promotional assets

## 10. Revision record

### v1.2 — 2026-09-25

- explicit user approval: Owner decision 2026-09-25 — adopt the protruding form (dark teardrop-like part extending from the pupil edge into the iris), recorded as the formal interpretation of the signature
- exact geometry / orientation change: none to size / orientation / application / subtlety; §2.2 fixes the form (polarity) of the existing "teardrop-like notch" wording
- reason: during the YURA 3D test-model production (`YURA3D-TEST-20260925-01`) the §2 wording supported both a protrusion and an indentation reading, and the MASTER cannot resolve the detail; both forms were shown to the Owner as decision evidence (test renders, not authority)
- relationship to `visuals/yura/identity/face/FACE_SPEC.md`: FACE §2.8 wording unchanged; this file remains the protected authority for its interpretation
- impact on existing standing CG / close-up / promotional assets: not audited by this revision

### v1.1 — 2026-09-25

- explicit user approval: Owner decision 2026-09-25 — orientation = lower-right as seen by the viewer; application = both eyes
- exact geometry / orientation change: none to size / shape / subtlety; §2.1 fixes the reference frame (viewer-relative, neutral front-facing face) and application (both eyes) of the existing "lower-right" wording
- reason: orientation ambiguity reported during YURA 3D test-model pre-production audit (historical 3D production OPEN-001; 3D documents retired by Owner request)
- relationship to `visuals/yura/identity/face/FACE_SPEC.md`: FACE §2.8 "lower-right edge of the pupil" wording unchanged; this file remains the protected authority for its interpretation
- impact on existing standing CG / close-up / promotional assets: not audited by this revision
