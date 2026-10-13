# YURA VISUAL AMBIGUITY PROTOCOL

Status: **AUTHOR-APPROVED / ACTIVE WORK PROTOCOL / NOT BY ITSELF VISUAL AUTHORITY**

This protocol is the newest author-approved sequencing rule for ambiguous-structure work. Where an older Face-phase document says to proceed directly to Face measurement or image-reference generation, this protocol inserts text-only ambiguity validation first.

Repository route boundary:

```text
visuals/execution/text-only-root/**
= shared temporary free / text-only validation workspace

visuals/yura/identity/**
= YURA formal visual authority / final consolidation target

tools/yura-master-benchmark/**
= paid-generation execution route after text-only PASS
```

Current free diagnostic entry point:

`visuals/execution/text-only-root/TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md`

Current YURA text-only execution copy:

`visuals/execution/text-only-root/YURA_VISUAL_TEXT.md`

Do not use the paid-generation tools route to perform the current text-only validation.

## 1. Purpose

This protocol governs any YURA feature whose actual structure, visible appearance, or camera-dependent presentation can diverge because of occlusion, overlap, perspective, or generative visibility compensation.

Primary high-risk areas currently include:

```text
ears
temple / ear-cover hair
side / rear hair
back-view hair mass
neck / shoulder / back overlap
```

The goal is not to force every structure to be visible. The goal is to preserve YURA identity and structural consistency while allowing natural occlusion and natural view-dependent appearance.

## 2. Existing source-type labels remain mandatory

Every claim still uses the existing source classification:

```text
MEASURED_MASTER_FACT
AUTHOR_OVERRIDE
TEST / HYPOTHESIS
```

The ambiguity labels below are an additional axis. They do not replace the source-type labels.

## 3. Mandatory ambiguity labels

For any ambiguous or occluded feature, use only these labels:

```text
MEASURED_VISIBLE_FACT
= directly visible and measurable in the source image

MEASURED_OCCLUSION_FACT
= directly supported front/behind or covering relationship

ESTIMATED_HIDDEN_GEOMETRY
= hidden continuation inferred only as min / best / max
= NOT Authority by itself

AUTHOR_INTENT
= explicit author correction or intended final behavior

VIEW_SPECIFIC_RULE
= allowed appearance / visibility for a named camera view

NON_COMPENSATION_RULE
= forbidden change whose only purpose is making a hidden feature easier to see
```

Unknown structure remains unknown. Do not convert missing visibility into invented geometry.

## 4. View set

When multi-view control is needed, use these named views:

```text
FRONT
FRONT_3Q
SIDE
REAR_3Q
BACK
```

A rule measured in one view does not automatically become exact geometry in another view.

Do not interpolate unsupported hidden 3D anatomy or hair structure between views.

## 5. Visible structure and actual structure are separate

For an occluded part, record separately:

```text
ACTUAL / STRUCTURAL GEOMETRY
VISIBLE GEOMETRY
OCCLUSION / LAYER ORDER
VIEW
```

Example:

```text
ear actual size = within target
ear visible fraction = low
hair occlusion = high
result = valid if visually natural
```

Low visibility alone is not a defect.

## 6. Generic non-compensation rule

Do not improve visibility by silently changing identity-defining structure.

Forbidden compensation includes, where applicable:

```text
enlarging
elongating
widening
moving outward
moving toward camera
rotating toward camera
separating the part from the head/body
clearing or moving the natural occluder
pushing a hidden part outside hair/clothing
spreading or fanning hair only to expose structure
forcing left/right visibility symmetry
```

If a correct structure is naturally hidden, keep it hidden.

## 7. Text-only diagnostic generation rule

The current first validation phase is **Codex text-only generation** under the shared temporary route:

`visuals/execution/text-only-root/TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md`

Generation appearance input for the current YURA run:

```text
visuals/execution/text-only-root/YURA_VISUAL_TEXT.md
```

The execution copy is temporary and does not replace YURA's formal identity-side source.

No YURA image reference is supplied during this phase.

The only allowed extra generation instructions are the operational test envelope:

```text
requested view
crop / framing as specified by the Run
neutral pose / expression
plain background
single-character constraint
DIAGNOSTIC / CANDIDATE status
```

Do not add new YURA appearance prose outside `YURA_VISUAL_TEXT.md` during generation. The purpose is to test the strength of the Visual Text itself.

`YURA_VISUAL_AMBIGUITY_PROTOCOL.md` is used for **YURA-specific interpretation / inspection**, not appended wholesale as extra appearance prompt text in the text-only generation phase.

Do not use the paid-generation tool route in this phase. If Codex-native image generation is unavailable, classify the Run as `ENVIRONMENT_BLOCKED`; do not silently fall back to paid generation.

## 8. Diagnostic output status

Before ear and rear-hair defects are resolved, all outputs are:

```text
DIAGNOSTIC / CANDIDATE ONLY
AUTHORITY PROMOTION = NO
```

They must not promote:

```text
current overlong ear geometry
unsupported hidden ear geometry
unverified rear-hair structure
```

into YURA Authority.

## 9. One-view-per-image default

For ambiguity validation, prefer one image per view rather than one five-panel composite.

Default diagnostic set:

```text
01 FRONT
02 FRONT_3Q
03 SIDE
04 REAR_3Q
05 BACK
```

Reason:

```text
independent generation
independent replacement
clearer PASS / FAIL per view
less cross-panel contamination
```

A composite sheet may be created later for convenience, but it does not replace the individual diagnostic images.

## 10. Naturalness gate

A result is not accepted only because a numeric ratio passes.

Evaluation uses all three:

```text
STRUCTURAL CONSISTENCY
IDENTITY CONSISTENCY
VISUAL NATURALNESS
```

Examples of FAIL even with nominal numeric compliance:

```text
hair unnaturally moved behind the ear to expose it
ear rotated toward camera only for visibility
rear hair unnaturally fanned away from the back
forced bilateral symmetry that removes natural overlap
```

The target is natural generation with correct structure, not maximal structural visibility.

Minor unrelated visual awkwardness may be tolerated during the early Codex diagnostic phase if the ambiguity behavior being tested is clearly improved and the image remains usable for diagnosis.

## 11. Codex -> paid-generation transfer gate

The Codex phase is a specification-strength test, not the final generator benchmark.

Before switching to the paid route, require repeated evidence under **unchanged Visual Text** that:

```text
no obvious ear elongation / inflation
no ear visibility compensation
natural hair-over-ear behavior is preserved
ear remains low-prominence
identity remains recognizably YURA-like from text alone
```

Current YURA working threshold:

```text
three qualifying FRONT_3Q results under the same unchanged Visual Text
+ one SIDE result with no major ear elongation / outward-projection failure
```

The initial five-view set may supply the first FRONT_3Q and SIDE samples. If either fails materially, strengthen the relevant Visual Text specification first and restart the fixed condition.

A material Visual Text change resets the repeated-result count.

This YURA-specific gate is a Run rule layered on top of the shared `TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md`; it does not make the shared protocol YURA-specific.

## 12. Paid text-only Face-up checkpoint

Only after the text-only transfer gate passes:

```text
switch to tools/yura-master-benchmark paid-generation route
appearance input = YURA_VISUAL_TEXT.md only
image reference = NONE
initial output = Face-up Pilot 1
```

The first paid Face-up is still diagnostic. It tests whether the Visual Text behavior transfers to the paid generator without relying on the existing Face Reference image.

Do not silently add image references or generator-specific appearance corrections merely to obtain a pass.

## 13. Current application order

```text
1. Visual Ambiguity Protocol = fixed
2. stage YURA Visual Text in visuals/execution/text-only-root
3. Codex text-only generation from the shared temporary execution route
4. inspect each generated image
5. tolerate minor unrelated awkwardness, but require meaningful ear-visibility-compensation suppression
6. obtain repeated qualifying results under unchanged Visual Text
7. TEXT-ONLY GATE = PASS
8. switch to tools/yura-master-benchmark paid route
9. paid text-only Face-up Pilot 1
10. inspect generator-transfer behavior
11. resolve / freeze ear ACTUAL / VISIBLE / OCCLUSION specification
12. resolve rear-hair / back-view mass / silhouette / layer-order specification
13. consolidate accepted rules into YURA identity part directories
14. remove obsolete YURA temporary execution copy when no longer needed
```

No formal Visual Authority promotion is implied by a Codex or paid diagnostic image alone.
