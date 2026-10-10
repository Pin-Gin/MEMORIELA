# YURA Body Geometry Audit v2

Status: **NON-AUTHORITY / DIAGNOSTIC ONLY / PARALLEL TO CURRENT QA**

This document does not replace `BODY_GEOMETRY_GUIDE.md`.
This document does not modify any current Body Authority value.
This document does not authorize Composition or Master promotion.

## Purpose

Audit v2 exists to test whether current Body Geometry QA is conflating rendered hair-shell size with structural head scale, and to retain author-visible body-build differences that the current vertical-only QA cannot represent.

It is designed to:

- separate visible hair silhouette from structural head scale;
- propagate crown uncertainty instead of forcing a false exact landmark;
- separate global body build from local chest/front-volume evaluation;
- keep horizontal measurements diagnostic until author-approved thresholds exist;
- compare current QA and Audit v2 before any gate replacement.

The current official QA remains `body_geometry_qa.py` until explicit author approval promotes a replacement.

---

## 1. Coordinate convention

Image coordinates use:

```text
origin = upper-left
x increases rightward
y increases downward
```

All landmark values are image-space measurements in pixels.

Hidden landmarks must not be represented as exact ground truth.

---

## 2. Head landmark separation

### `visible_hair_crown_y`

The highest persistent visible point of the main hair shell.

Use it for:

- rendered apparent-head-silhouette analysis;
- Face Reference indirect-pull diagnostics;
- measuring visible hair-shell inflation.

Do not use it for:

- structural head-unit calculation;
- 7.2-head pass/fail calculation;
- torso or inseam normalization.

Single stray hairs or isolated anti-aliased pixels are not the main hair shell.

### `structural_crown_proxy_y`

A diagnostic proxy for the top of the underlying structural head, excluding visible hair-shell inflation.

Because this point can be hidden by hair, Audit v2 records an uncertainty interval:

```text
structural_crown_min_y
structural_crown_best_y
structural_crown_max_y
```

With Y increasing downward:

```text
min_y  = upper bound of plausible structural crown position
best_y = central reviewed estimate
max_y  = lower bound of plausible structural crown position
```

Required ordering:

```text
structural_crown_min_y <= structural_crown_best_y <= structural_crown_max_y
```

The interval is diagnostic uncertainty, not permission to move or redesign the Face Reference.

---

## 3. Structural head calculations

For each structural-crown candidate independently:

```text
head_height_px
= chin_y - structural_crown_y

figure_height_px
= soles_y - structural_crown_y

total_head_ratio
= figure_height_px / head_height_px
```

Do not estimate a structural result by multiplying an old visible-crown head ratio by a correction factor.

Changing crown position changes both the head-height denominator and the full-figure numerator, so all metrics must be recomputed from landmarks.

### Head-ratio interval status

The current official acceptable range remains **7.1â€“7.3 heads**.

Audit v2 diagnostic states:

```text
EXACT_PASS
  min_y = best_y = max_y and the resulting value is inside 7.1â€“7.3

PASS_ROBUST
  the full uncertainty interval is inside 7.1â€“7.3

REVIEW_OVERLAP
  the uncertainty interval intersects 7.1â€“7.3 but is not fully contained

FAIL_ROBUST
  the uncertainty interval does not intersect 7.1â€“7.3
```

These labels do not replace the current official QA gate.

---

## 4. Face Reference indirect head-shell diagnostic

Face Reference remains **FACE IDENTITY AUTHORITY ONLY**.

Audit v2 may nevertheless compare visible and structural head-shell spans:

```text
visible_head_height
= chin_y - visible_hair_crown_y

structural_head_height
= chin_y - structural_crown_proxy_y

hair_shell_inflation_ratio
= visible_head_height / structural_head_height
```

This ratio is diagnostic evidence of apparent-head-shell inflation.

It must not be interpreted as:

- Body Authority;
- proof that Face Reference directly controls full-body proportion;
- permission to resize, replace, or redesign the Face Reference;
- a universal anatomical head ratio.

`head-shell` mode never executes a 7.2 full-body pass/fail calculation.

---

## 5. Crotch / pelvis boundary landmark

Primary Audit v2 body landmark:

```text
crotch_pelvis_boundary_proxy_y
```

Definition:

> the structural upper/lower-body boundary at the central medial-thigh bifurcation: the vertical level where the left and right inner thighs separate into independent legs beneath the pelvis.

This point is intended to correspond to the Active Body Guide's author-approved `CROTCH / PELVIS LINE = UPPER / LOWER BODY BOUNDARY` concept.

Do not derive this point from garment graphics or garment construction alone. The following have **no landmark authority**:

- underwear seam;
- shorts hem;
- garment crotch fabric or its lowest point;
- decorative clothing line;
- V-shaped garment edge.

**GARMENT LINE AUTHORITY = DENIED.**

The boundary must be visually reviewed from the structural body/inner-thigh separation. If the boundary is partially obscured, Audit v2 records uncertainty instead of forcing a false exact point:

```text
crotch_pelvis_boundary_min_y
crotch_pelvis_boundary_best_y
crotch_pelvis_boundary_max_y
```

With Y increasing downward:

```text
min_y  = upper bound of plausible boundary position
best_y = central reviewed estimate
max_y  = lower bound of plausible boundary position
```

Required ordering:

```text
chin_y
< crotch_pelvis_boundary_min_y
<= crotch_pelvis_boundary_best_y
<= crotch_pelvis_boundary_max_y
< knee_y
```

The current author-approved Body Guide value `crotch / pelvis-line proxy = y 856` is not changed. For the Active Body Guide exact reference test:

```text
crotch_pelvis_boundary_min_y  = 856
crotch_pelvis_boundary_best_y = 856
crotch_pelvis_boundary_max_y  = 856
```

---

## 6. Body vertical calculations and uncertainty propagation

Structural-crown uncertainty and crotch/pelvis-boundary uncertainty are independent diagnostic dimensions.

For all body metrics that depend on both landmarks, Audit v2 evaluates the full **3 Ã— 3 = 9 combination set**:

```text
structural crown min / best / max
Ã—
crotch-pelvis boundary min / best / max
```

The reported `best` value uses:

```text
structural_crown_best_y
+
crotch_pelvis_boundary_best_y
```

The reported interval uses the minimum and maximum across all 9 combinations.

Head ratio does not depend on the crotch/pelvis boundary and therefore uses structural-crown uncertainty only.

For each crown/boundary combination:

```text
inseam_proxy_ratio
= (soles_y - crotch_pelvis_boundary_y)
  / (soles_y - structural_crown_y)

chin_to_crotch_pelvis_boundary_heads
= (crotch_pelvis_boundary_y - chin_y)
  / (chin_y - structural_crown_y)

crotch_pelvis_boundary_to_knee_heads
= (knee_y - crotch_pelvis_boundary_y)
  / (chin_y - structural_crown_y)

knee_to_soles_heads
= (soles_y - knee_y)
  / (chin_y - structural_crown_y)
```

Lower-body split is also reported with uncertainty:

```text
boundary_to_knee_share
= (knee_y - boundary_y) / (soles_y - boundary_y)

knee_to_soles_share
= (soles_y - knee_y) / (soles_y - boundary_y)
```

Current official Body Guide gates are read from existing `config.json`; Audit v2 does not invent replacements.

Current values at creation time remain:

```text
head target                  7.2
head acceptable range        7.1â€“7.3
inseam target                46.0â€“46.5%
inseam model-like hard fail  >= 47.0%
chinâ†’crotch current envelope 2.7985â€“2.9420 heads
```

---

## 7. Diagnostic horizontal geometry

Optional manually reviewed measurements:

```text
shoulder_width_px
ribcage_width_px
chest_outer_width_px
waist_width_px
pelvis_hip_width_px
upper_thigh_left_width_px
upper_thigh_right_width_px
calf_left_width_px
cal_right_width_px
ankle_left_width_px
ankle_right_width_px
```

Measurements must exclude hair and obvious garment flare where possible.

If a body contour is hidden or contaminated enough that it cannot be distinguished reliably, leave the measurement absent. Missing values are `NOT_MEASURED`; they are never converted to zero.

Widths are normalized to best-estimate structural figure height:

```text
normalized_width = width_px / structural_figure_height_best_px
```

When the required inputs exist, Audit v2 also reports:

```text
shoulder / hip
rı¥‰…”€¼¡¥À)İ…¥ÍĞ€¼¡¥À)…Ù•É…”ÕÁÁ•ÈÑ¡¥ €¼¡¥À)…Ù•É…”…±˜€¼¡¥À)¡•ÍĞ€¼É¥‰…”)¡•ÍĞ€¼İ…¥ÍĞ)€()Q¡•Í”É…Ñ¥½Ì…É”€¨©%9=MQ%=91d¨¨¸()9¼¹Õµ•É¥ŒAMLÑ¡É•Í¡½±¥Ì™É½é•¸‰äÕ‘¥ĞØÈ¸()±½Ñ¡¥¹œ½¹Ñ…µ¥¹…Ñ¥½¸°¡…¥È½Ù•É±…À°Á•ÉÍÁ•Ñ¥Ù”°…¹ÍÑå±¥é•É•¹‘•É¥¹œµÕÍĞÉ•µ…¥¸Á…ÉĞ½˜¡Õµ…¸É•Ù¥•Ü¸()¼¹½ĞÁÉ½µ½Ñ”„‘¥…¹½ÍÑ¥Œİ¥‘Ñ É…Ñ¥¼¥¹Ñ¼„!…É…Ñ”İ¥Ñ¡½ÕĞ•áÁ±¥¥Ğ…ÕÑ¡½È…ÁÁÉ½Ù…°¸((´´´((ŒŒ€à¸ÕÑ¡½ÈÙ¥ÍÕ…°…Ñ•Ì()Õ‘¥ĞØÈÉ•½É‘ÌÑİ¼¥¹‘•Á•¹‘•¹Ğ…ÕÑ¡½ÈµÉ•Ù¥•Ü‘¥µ•¹Í¥½¹ÌÉ•ÅÕ¥É•Ñ¼‘¥ÍÑ¥¹Õ¥Í Q•ÍĞ€Ì…¹Q•ÍĞ€Ğ™…¥±ÕÉ”µ½‘•Ì¸((ŒŒŒ½Ù•É…±±}‰Õ¥±‘}¹½Ñ}Ñ½½}Ñ¡¥¹€()¡•­ÌÑ¡”İ¡½±”µ‰½‘äµ…ÍÌ€¼Í¥±¡½Õ•ÑÑ”¸()Q¡¥Ì¥Ì¹½Ğ•ÅÕ¥Ù…±•¹ĞÑ¼è((´Í¡½Õ±‘•Èİ¥‘Ñ ½¹±äì(´¡¥Àİ¥‘Ñ ½¹±äì(´	5$µ±¥­”¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ì(´•¹•É¥Œ¡Õµ…¸…¹…Ñ½µä¸((ŒŒŒ¡•ÍÑ}™É½¹Ñ}Ù½±Õµ•}µ…Ñ¡•Í}…ÕÑ¡½É}¥¹Ñ•¹Ñ€()¡•­Ì¡•ÍĞ½™É½¹ĞµÙ½±Õµ”…ÁÁ•…É…¹”É•±…Ñ¥Ù”Ñ¼Ñ¡”İ¡½±”eUI‰Õ¥±¸()Q¡¥Ì¥Ì¹½Ğ•ÅÕ¥Ù…±•¹ĞÑ¼è((´¡•ÍĞİ¥‘Ñ …±½¹”ì(´„Í¥¹±”…‰Í½±ÕÑ”Í¥é”Ù…±Õ”ì(´•¹•É¥Œ…¹…Ñ½µ¥…°Ñ…É•ÑÌ¸()Q¡¥ÌÙ…±¥‘…Ñ¥½¸¥Ì™½È¡…É…Ñ•È5…ÍÑ•È	½‘ä•½µ•ÑÉä…¹Í¥±¡½Õ•ÑÑ”É•Ù¥•Ü°¹½ĞÍ•áÕ…°•µÁ¡…Í¥Ì¸()±±½İ•É•Ù¥•ÜÍÑ…Ñ•Ìè()Ñ•áĞ)AML)%0)9=Q}IY%])9=Q}5MUI	1)€()Õ‘¥ĞØÈ­••ÁÌÑ¡•Í”Ñİ¼ÍÑ…Ñ•ÌÍ•Á…É…Ñ”¸‰½‘äµ‰Õ¥±™…¥±ÕÉ”µÕÍĞ¹½Ğ½Ù•ÉİÉ¥Ñ”„¡•ÍĞÉ•ÍÕ±Ğ°…¹„¡•ÍĞ™…¥±ÕÉ”µÕÍĞ¹½Ğ½Ù•ÉİÉ¥Ñ”„‰½‘äµ‰Õ¥±É•ÍÕ±Ğ¸((´´´((ŒŒ€ä¸5½‘•Ì((ŒŒŒ¡•…µÍ¡•±±€()I•ÅÕ¥É•è((´¥µ…”Á…Ñ ì(´Ù¥Í¥‰±”¡…¥ÈÉ½İ¸ì(´ÍÑÉÕÑÕÉ…°É½İ¸µ¥¸€¼‰•ÍĞ€¼µ…àì(´¡¥¸¸()AÉ½‘Õ•Ì¡•…µÍ¡•±°‘¥…¹½ÍÑ¥Œµ•ÑÉ¥Ì½¹±ä¸()½•Ì¹½Ğ…±Õ±…Ñ”„€Ü¸È™Õ±°µ‰½‘ä…Ñ”¸((ŒŒŒ‰½‘å€()I•ÅÕ¥É•è((´¥µ…”Á…Ñ ì(´ÍÑÉÕÑÕÉ…°É½İ¸µ¥¸€¼‰•ÍĞ€¼µ…àì(´¡¥¸ì(´É½Ñ ½Á•±Ù¥Ì‰½Õ¹‘…Éäµ¥¸€¼‰•ÍĞ€¼µ…àì(´­¹•”ì(´Í½±•Ì¸()Ù¥Í¥‰±•}¡…¥É}É½İ¹}å€€¥Ì½ÁÑ¥½¹…°…¹…‘‘Ì…ÁÁ…É•¹Ğµ¡•…µÍ¡•±°‘¥…¹½ÍÑ¥Ìİ¡•¸ÍÕÁÁ±¥•¸()=ÁÑ¥½¹…°¡½É¥é½¹Ñ…°•½µ•ÑÉä…¹…ÕÑ¡½ÈÙ¥ÍÕ…°É•Ù¥•Üµ…ä…±Í¼‰”É•½É‘•¸((´´´((ŒŒ€ÄÀ¸…¥°µ±½Í•Ù…±¥‘…Ñ¥½¸()Õ‘¥ĞØÈÉ•©•ÑÌ¥¹Ù…±¥±…¹‘µ…É¬½É‘•È¸()I•ÅÕ¥É•ÍÑÉÕÑÕÉ…°½É‘•É¥¹œè()Ñ•áĞ(À€ğôÍÑÉÕÑÕÉ…±}É½İ¹}µ¥¹}ä)ÍÑÉÕÑÕÉ…±}É½İ¹}µ¥¹}ä€ğôÍÑÉÕÑÕÉ…±}É½İ¹}‰•ÍÑ}ä€ğôÍÑÉÕÑÕÉ…±}É½İ¹}µ…á}ä)ÍÑÉÕÑÕÉ…±}É½İ¹}µ…á}ä€ğ¡¥¹}ä)€()½È‰½‘äµ½‘”è()Ñ•áĞ)¡¥¹}ä(ğÉ½Ñ¡}Á•±Ù¥Í}‰½Õ¹‘…Éå}µ¥¹}ä(ğôÉ½Ñ¡}Á•±Ù¥Í}‰½Õ¹‘…Éå}‰•ÍÑ}ä(ğôÉ½Ñ¡}Á•±Ù¥Í}‰½Õ¹‘…Éå}µ…á}ä(ğ­¹••}ä(ğÍ½±•Í}ä(ğô¥µ…•}¡•¥¡Ğ)€()%˜Ù¥Í¥‰±•}¡…¥É}É½İ¹}å€¥ÌÍÕÁÁ±¥•è()Ñ•áĞ(À€ğôÙ¥Í¥‰±•}¡…¥É}É½İ¹}ä€ğ¡¥¹}ä)€()]¥‘Ñ µ•…ÍÕÉ•µ•¹ÑÌµÕÍĞ‰”Á½Í¥Ñ¥Ù”¥˜ÍÕÁÁ±¥•¸((´´´((ŒŒ€ÄÄ¸Ñ¥Ù”	½‘äÕ¥‘”É•™•É•¹”Ñ•ÍĞ()Q¡”ÕÉÉ•¹ĞÑ¥Ù”	½‘äÕ¥‘”•á…Ğ±…¹‘µ…É­ÌÉ•µ…¥¸è()Ñ•áĞ)ÍÑÉÕÑÕÉ…°É½İ¸€€€€€€€€€€€€€€ô€ÄØÀ)¡¥¸€€€€€€€€€€€€€€€€€€€€€€€€€€ô€ÌĞÀ)É½Ñ ½Á•±Ù¥Ì‰½Õ¹‘…Éäµ¥¸€€€€ô€àÔØ)É½Ñ ½Á•±Ù¥Ì‰½Õ¹‘…Éä‰•ÍĞ€€€ô€àÔØ)É½Ñ ½Á•±Ù¥Ì‰½Õ¹‘…Éäµ…à€€€€ô€àÔØ)­¹•”€€€€€€€€€€€€€€€€€€€€€€€€€€ô€ÄÄÔØ)Í½±•Ì€€€€€€€€€€€€€€€€€€€€€€€€€ô€ÄĞÔØ)€()áÁ•Ñ•Õ‘¥ĞØÈ½ÕÑÁÕÑÌè()Ñ•áĞ)Ñ½Ñ…°¡•…É…Ñ¥¼€ô€Ü¸È)¥¹Í•…´ÁÉ½áä€€€€€ô€ĞØ¸ÈäØÌ”)¡¥»ŠI‰½Õ¹‘…Éä€€€€ô€È¸àØØÜ¡•…‘Ì)‰½Õ¹‘…ÉçŠI­¹•”€€€€ô€ÌÀÀÁà)­¹•—ŠIÍ½±•Ì€€€€€€€ô€ÌÀÀÁà)±½İ•ÈÍÁ±¥Ğ€€€€€€ô€ÔÀ€è€ÔÀ)€()…¥±ÕÉ”Ñ¼É•ÁÉ½‘Õ”Ñ¡•Í”Ù…±Õ•Ìµ•…¹ÌÑ¡”Õ‘¥ĞØÈ…±Õ±…Ñ¥½¸¥µÁ±•µ•¹Ñ…Ñ¥½¸¥Ì¥¹Ù…±¥¸()Q¡¥Ì•á…ĞÑ•ÍĞ‘½•Ì¹½Ğµ½‘¥™äÑ¡”	½‘äÕ¥‘”¸((´´´((ŒŒ€ÄÈ¸A…É…±±•°µ½Á•É…Ñ¥½¸ÉÕ±”()U¹Ñ¥°•áÁ±¥¥Ñ±äÁÉ½µ½Ñ•‰ä…ÕÑ¡½È…ÁÁÉ½Ù…°è()Ñ•áĞ)‰½‘å}•½µ•ÑÉå}Å„¹Áä(ôUII9P=%%0E()‰½‘å}•½µ•ÑÉå}Å…}ØÈ¹Áä(ôAI110%9=MQ%E)€()¸Õ‘¥ĞØÈÉ•ÍÕ±Ğ…¹¹½Ğ‰ä¥ÑÍ•±˜…ÕÑ¡½É¥é”è((´½µÁ½Í¥Ñ¥½¸•á•ÕÑ¥½¸ì(´5…ÍÑ•ÈÁÉ½µ½Ñ¥½¸ì(´Y¥ÍÕ…°ÕÑ¡½É¥ÑäÁÉ½µ½Ñ¥½¸ì(´	½‘äÕÑ¡½É¥Ñä¡…¹•Ìì(´…”ÕÑ¡½É¥Ñä¡…¹•Ì¸()±°Õ‘¥ĞØÈÉ•Á½ÉÑÌµÕÍĞÑ¡•É•™½É”É•Ñ…¥¸è()Ñ•áĞ)½µÁ½Í¥Ñ¥½¹}•á•ÕÑ¥½¹}…±±½İ•€ô™…±Í”)µ…ÍÑ•É}ÁÉ½µ½Ñ¥½¸€ô9<)…ÕÑ¡½É¥Ñå}ÍÑ…ÑÕÌ€ô%9=MQ%}=91d)€((´´´((ŒŒ€ÄÌ¸Y…±¥‘…Ñ¥½¸Í•ÅÕ•¹”‰•™½É”…¹äÁÉ½µ½Ñ¥½¸()IÕ¸İ¥Ñ¡½ÕĞÁ…¥•¹•É…Ñ¥½¸è()Ñ•áĞ(Ä¸AåÑ¡½¸Íå¹Ñ…à¡•¬(È¸Ñ¥Ù”	½‘äÕ¥‘”•á…ĞÉ•™•É•¹”Ñ•ÍĞ(Ì¸…”I•™•É•¹”¡•…µÍ¡•±°Ñ•ÍĞ(Ğ¸Q•ÍĞ€Ì‰½‘ä…Õ‘¥Ğİ¥Ñ ‰½Õ¹‘…ÉäÕ¹•ÉÑ…¥¹Ñä(Ô¸Q•ÍĞ€Ğ‰½‘ä…Õ‘¥Ğİ¥Ñ ‰½Õ¹‘…ÉäÕ¹•ÉÑ…¥¹Ñä(Ø¸I•½É…ÕÑ¡½ÈÙ¥ÍÕ…°…Ñ•Ì(Ü¸½µÁ…É”ÕÉÉ•¹ĞE…¹Õ‘¥ĞØÈ(à¸I•Ù¥•ÜÉ•ÍÕ±ÑÌİ¥Ñ Ñ¡”…ÕÑ¡½È)€()=¹±ä…™Ñ•ÈÑ¡…Ğ½µÁ…É¥Í½¸µ…ä„Í•Á…É…Ñ”…ÕÑ¡½Èµ…ÁÁÉ½Ù•¡…¹”ÁÉ½µ½Ñ”…¹äÕ‘¥ĞØÈ‘•™¥¹¥Ñ¥½¸¥¹Ñ¼½™™¥¥…°E¸()Q•ÍĞ€Ô¥Ì½ÕÑÍ¥‘”Ñ¡¥ÌÍÁ•¥™¥…Ñ¥½¸…¹µÕÍĞ¹½Ğ‰”ÍÑ…ÉÑ•µ•É•±ä‰•…ÕÍ”Õ‘¥ĞØÈÉÕ¹ÌÍÕ•ÍÍ™Õ±±ä¸(