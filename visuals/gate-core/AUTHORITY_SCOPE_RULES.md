# AUTHORITY SCOPE RULES

Status: **PROTECTED / PROJECT-WIDE**

Authority is separated by control Scope. A lower or different Scope must not mutate another protected Scope.

## Scopes
### CHARACTER_IDENTITY
Controls character identity as a whole.

### BODY
Controls proportions, dimensions, volumes and baseline anatomy.

### BODY_VIEW
Controls how the protected BODY projects / silhouettes at a specific viewing direction.
Does not create a new BODY.

### FACE_DETAIL
Controls face outline, feature placement, ear geometry and face-framing boundary.
Does not control BODY.

### OUTFIT
Controls garment design, colors, components, pattern and emblem.
Does not control character anatomy.

### CHARACTER_OUTFIT_PROFILE
Controls explicitly allowed character-specific wearing differences only.
Does not redesign the base outfit.

### POSE
Controls joint position, orientation, center of gravity, support/contact and camera projection.
Does not redesign anatomy.

### RENDERING
Controls line, shading, contrast, material impression and realism level.
Does not recolor / redesign protected identity.

### SCENE
Controls background / environment / props except protected character and outfit scopes.

## Novel / Visual domain boundary
Novel Canon and Visual Authority are separate Authority domains.

A file under `characters/`, `story/`, or `manuscript/` does not become image-generation Visual Authority merely because it contains appearance, age, clothing, scene, or other visually expressible information.

For YURA specifically:
- `characters/YURA.md` is **NOVEL ONLY**
- it must not participate in YURA Visual Authority resolution
- it must not be compiled into a YURA Execution Payload or Prompt
- it must not be used as fallback when YURA Visual Authority is missing
- it must not be used for YURA Visual QA or Reference selection

If the active YURA Visual Domain lacks a required definition, stop instead of importing Novel Canon.

`NOVEL_CANON != VISUAL_AUTHORITY`
`characters/YURA.md -> YURA_IMAGE_GENERATION = DENIED`

## Composite rule
When multiple domains are active, each controls only its Scope.

`GARMENT FOLLOWS CHARACTER BODY.`
`CHARACTER BODY NEVER FOLLOWS GARMENT MASTER.`

A pose reference does not become an Identity reference.
A garment mannequin does not become a BODY reference.
A body-view reference does not become a FACE reference.
