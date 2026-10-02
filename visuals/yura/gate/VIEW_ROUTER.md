# YURA BODY VIEW ROUTER

Status: **PROTECTED / MANDATORY FOR VIEW SELECTION**

Purpose:
固定BODYを異なる視点で安定投影するため、生成時に最も近いBODY View Masterを1枚だけ選択する。

Route by **torso/body orientation relative to camera**, not face direction.

## Routing
- FRONT: around 0° / within ±22.5°
- FRONT_LEFT: 22.5°–67.5° toward left
- LEFT: 67.5°–112.5°
- BACK_LEFT: 112.5°–157.5°
- BACK: 157.5°–180° and equivalent opposite range
- BACK_RIGHT: 112.5°–157.5° toward right
- RIGHT: 67.5°–112.5° toward right
- FRONT_RIGHT: 22.5°–67.5° toward right

## Reference mapping
Exact paths are defined only in `AUTHORITY_MANIFEST.md`.

## Rules
- select exactly one BODY_VIEW_REFERENCE
- FRONT uses root YURA Visual Master
- non-front requires the corresponding approved BODY View Master in PRODUCTION
- if the routed view is missing, STOP
- do not fall back to neighboring angle
- do not synthesize a missing view from memory / text alone in PRODUCTION
- face/head orientation is independent from torso routing
- pose changes joints; body-view anchor stabilizes projected BODY geometry

## Significant pose
A front-facing seated / crouched / reaching pose may still route to FRONT if torso orientation remains front.
Torso rotation changes the route even if the face turns back toward camera.
