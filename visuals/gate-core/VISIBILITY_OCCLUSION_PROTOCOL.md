# VISIBILITY / OCCLUSION PROTOCOL

Status: **PROTECTED / MANDATORY**

Core:
`HIDDEN != MISSING`
`NOT VISIBLE != INCORRECT`

Visibility is an outcome of:
- camera angle
- body / head orientation
- pose
- hair
- clothing
- object / body overlap
- perspective

Visibility itself is not a target to maximize.

## Forbidden show-feature compensation
Do not:
- rotate anatomy merely to expose it
- widen BODY to reveal hidden volume
- separate limbs merely for readability
- pull hair away to reveal ears / face areas
- enlarge a partially hidden feature
- expose both left/right features for symmetry
- flatten or relocate overlapping forms to make every component visible
- modify pose because a hidden feature is known to exist

## Correct behavior
If a feature should be hidden at the requested camera / pose, keep it hidden.
Preserve the underlying protected geometry without forcing visual exposure.

## QA failure
Any material show-feature compensation is a targeted failure of the controlling Scope.
Do not change Identity canon to rescue it.
