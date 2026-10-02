# REFERENCE ROLE RULES

Status: **PROTECTED / PROJECT-WIDE**

Every visual reference must be declared with one role.

## Roles
### IDENTITY_ROOT_REFERENCE
Whole-character identity anchor.

### BODY_VIEW_REFERENCE
Angle-specific BODY projection / silhouette anchor.

May control:
- projected shoulder / ribcage / waist / pelvis reading
- body depth / silhouette
- protected volume continuity

Must not control:
- face redesign
- hair redesign
- outfit
- expression
- rendering style

### FACE_DETAIL_REFERENCE
Face close-up anchor.

May control:
- face outline
- cheek/chin balance
- eye placement
- nose/mouth placement
- ear geometry
- face-framing hair boundary

Must not control:
- BODY ratio
- outfit
- scene
- body pose

### OUTFIT_REFERENCE
Garment anchor.

May control garment design only.
Must not control character BODY / FACE / EYE / HAIR / SKIN.

### POSE_ONLY_REFERENCE
May control:
- joints
- segment orientation
- support/contact
- camera / placement

Must not control identity, BODY dimensions, hair identity, outfit identity or rendering.

### SCENE_REFERENCE
May control environment / composition only.

## Deny rules
- rejected / intermediate generations are not Identity references
- no automatic previous-image fallback
- no undeclared role
- no single reference silently controlling multiple protected scopes
- Git existence alone does not prove the image reached the generation execution
