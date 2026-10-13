# YURA VISUAL AMBIGUITY PROTOCOL

Status: **AUTHOR-APPROVED / ACTIVE WORK PROTOCOL / NOT BY ITSELF VISUAL AUTHORITY**

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

## 7. Reference-generation rule

A generated reference must declare:

```text
view
allowed authority scope
denied authority scope
known unresolved defects
source image(s)
status: DIAGNOSTIC / CANDIDATE / AUTHOR-APPROVED
```

Before the ear and rear-hair defects are resolved, new multi-view images are **DIAGNOSTIC / CANDIDATE only**.

They must not promote:

```text
current overlong ear geometry
unsupported hidden ear geometry
unverified rear-hair structure
```

into YURA Authority.

## 8. One-view-per-image default

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
clearer source / hash tracking
simpler PASS / FAIL per view
less cross-panel contamination
```

A composite sheet may be created later for convenience, but it does not replace the individual source images.

## 9. Naturalness gate

A result is not accepted only because a numeric ratio passes.

Final evaluation must satisfy all three:

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

## 10. Current application order

Apply this protocol in the following order:

```text
1. validate this protocol against current YURA authorities
2. build the shortest reproducible reference-generation route
3. generate the five single-view DIAGNOSTIC / CANDIDATE references
4. verify the route and view behavior; PASS does not yet promote visual Authority
5. resolve the ear problem using ACTUAL / VISIBLE / OCCLUSION separation
6. resolve the rear-hair / back-view problem using mass / silhouette / layer-order separation
7. only then promote corrected multi-view reference material after author review
```

No paid-generation or formal visual promotion is implied by this protocol alone.
