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

## Non-reference image carrier
### EDIT_SOURCE_CARRIER
`EDIT_SOURCE_CARRIER` is **NOT a reference role and NOT Authority**.

It may be used only when an active protected Gate explicitly defines an image-edit / refinement submode.

Purpose:
- provide the pixel / layout starting state of the same candidate being revised
- preserve spatial continuity needed for a bounded edit operation

It does not establish that any visible trait is correct.
It must not be treated as:
- IDENTITY_ROOT_REFERENCE
- FACE_DETAIL_REFERENCE
- BODY_VIEW_REFERENCE
- OUTFIT_REFERENCE
- POSE_ONLY_REFERENCE
- SCENE_REFERENCE
- Canon evidence
- Production Authority

A rejected or intermediate candidate may be used as `EDIT_SOURCE_CARRIER` only when the active Gate explicitly permits that exact refinement route.
Such use does **not** promote the candidate to Reference or Authority.

Mandatory boundaries:
- exactly the active Gate-authorized candidate may be used
- no silent fallback to another image
- the edit source must not override protected text Authority
- the edit result is a new candidate
- all protected domains required by the active QA must be re-evaluated after the edit
- a failed edit result must not become the next edit source unless an active Gate explicitly authorizes that chain

## Deny rules
- rejected / intermediate generations are not Identity references
- no automatic previous-image fallback
- no undeclared role
- no single reference silently controlling multiple protected scopes
- Git existence alone does not prove the image reached the generation execution
- `EDIT_SOURCE_CARRIER` must never be relabeled or treated as an Identity / Production reference merely because it was supplied to an image-edit operation
