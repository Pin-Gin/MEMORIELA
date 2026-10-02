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

## Composite rule
When multiple domains are active, each controls only its Scope.

`GARMENT FOLLOWS CHARACTER BODY.`
`CHARACTER BODY NEVER FOLLOWS GARMENT MASTER.`

A pose reference does not become an Identity reference.
A garment mannequin does not become a BODY reference.
A body-view reference does not become a FACE reference.
