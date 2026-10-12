# YURA Test 6 Result — Pelvis/Boundary normalized-position lock

Status: **COMPLETE / NO SUPPORT / SERIES STOPPED AT 3 OF 5 MAX**

## Hypothesis

Test 6 asked whether the author-selected Sample 9 Working Master could be edited so that the crotch/pelvis structural boundary moved toward the Body Guide anchor at:

```text
boundary from structural crown = 53.7037% of crown→soles
crotch→soles                  = 46.2963%
```

while preserving the already-approved visual balance.

## Frozen condition

All three paid samples used the same:

```text
git_commit = 3388e126ed55400be51141c0327be04b1e4d5129
sealed_authority_bundle_sha256 = 8d3ba7f15de8cbf73e87fe4c76d8f1d5f7997b158808f1df8a8c707695405c72
Working Master = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
Working Master SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
Body Guide = visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png
```

No Git/config/Authority change occurred between Test 6 samples.

## Measurement note

The numeric values below are manual QA-equivalent estimates measured from the uploaded 1152×2048 RAW images using the active structural-crown / pelvis-boundary uncertainty definition. They are not claimed to be repository-generated `body_geometry_qa.py` reports.

## Sample 1

```text
run_dir = C:\Dev\MEMORIELA\tools\yura-master-benchmark\runs\run_20261012T134220Z
compiled_prompt_sha256 = e79cb035c3a10dcdf3bc1cf351f84c0626205f45fce231ad98b7732234536b77
uploaded RAW SHA256 = 9e21a7f7e64374cc3e620e5bc38c16234abb9a57d111bb09e913c54824dc5888

structural crown ≈ 70 / 74 / 78
chin             ≈ 349
boundary         ≈ 998 / 1006 / 1014
knee             ≈ 1348
soles            ≈ 1977

Head best        ≈ 6.920
Head interval    ≈ 6.835–7.007
Boundary best    ≈ 48.98%
Boundary interval≈ 48.45–49.50%
Inseam best      ≈ 51.02%
Inseam interval  ≈ 50.50–51.55%
Chin→boundary    ≈ 2.389 heads
Torso interval   ≈ 2.326–2.454 heads
```

Author visual review:

```text
hair length                  FAIL
skin                         PASS
chest                        PASS
knee position                PASS
thigh feminine volume/curve  PASS
overall leg vertical balance PASS
overall build                PASS
```

Author overall observation:

> Relative to Sample 9, the lower-body position reads lower, but the overall balance does not look unnatural.

Decision: **NO SUPPORT**.

The visible lower-body placement changed slightly, but the normalized structural boundary did not move toward 53.7037%.

## Sample 2

```text
run_dir = C:\Dev\MEMORIELA\tools\yura-master-benchmark\runs\run_20261012T141115Z
compiled_prompt_sha256 = 3870e5980a6f80df1ce9d37edf037db6b34b0d5c11126b7aba88a864bdb2319b
uploaded RAW SHA256 = 4924eeb7e0aff36a3debb81173467eb9f9edb869927a7280d63a1734bba65799

structural crown ≈ 70 / 74 / 78
chin             ≈ 347
boundary         ≈ 998 / 1006 / 1014
knee             ≈ 1348
soles            ≈ 1977

Head best        ≈ 6.971
Head interval    ≈ 6.884–7.059
Boundary best    ≈ 48.98%
Boundary interval≈ 48.45–49.50%
Inseam best      ≈ 51.02%
Inseam interval  ≈ 50.50–51.55%
Chin→boundary    ≈ 2.414 heads
Torso interval   ≈ 2.350–2.480 heads
```

Author review: materially the same as Sample 1.

Decision: **NO SUPPORT**.

## Sample 3

```text
run_dir = C:\Dev\MEMORIELA\tools\yura-master-benchmark\runs\run_20261012T142545Z
compiled_prompt_sha256 = 3106ff3eb628b73eddca7b6bf5e14cbc4da952cdf3d3ee762535973cf0ad208e
uploaded RAW SHA256 = e48097122e8f2bb400dbf7c702e890f44d05b53884caf41efbeac42e3133aa33

structural crown ≈ 70 / 74 / 78
chin             ≈ 347
boundary         ≈ 998 / 1006 / 1014
knee             ≈ 1348
soles            ≈ 1977

Head best        ≈ 6.971
Head interval    ≈ 6.884–7.059
Boundary best    ≈ 48.98%
Boundary interval≈ 48.45–49.50%
Inseam best      ≈ 51.02%
Inseam interval  ≈ 50.50–51.55%
Chin→boundary    ≈ 2.414 heads
Torso interval   ≈ 2.350–2.480 heads
```

Author review: unchanged from Sample 1 / Sample 2.

Decision: **NO SUPPORT**.

## Series conclusion

```text
Sample 1 = NO SUPPORT
Sample 2 = NO SUPPORT
Sample 3 = NO SUPPORT
Sample 4 = NOT RUN
Sample 5 = NOT RUN
```

Three independent paid outputs, with different compiled prompt hashes, converged to approximately the same normalized structural boundary region near 49% rather than the requested 53.7037% anchor.

Therefore the Test 6 hypothesis is rejected for the current edit pipeline:

> Explicit textual enforcement of the 53.7037% normalized crotch/pelvis structural anchor did not materially move the generated boundary to the approved Body Guide position.

The remaining two allowed samples were not run because 3/3 materially identical NO SUPPORT results were sufficient to establish the lack of reproducible effect.

## Author fallback decision activated

Per the preregistered fallback rule, the author explicitly approved ending further pelvis/boundary optimization and promoting variance-study Sample 9 as the formal YURA full-body Master.

This promotion does **not** rewrite the known numeric discrepancy as PASS.

```text
formal full-body Master = visuals/yura/identity/master/YURA_VISUAL_MASTER.png
asset SHA256 = 81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d
source = Variance Study Sample 9
numeric Body Guide discrepancy = retained as audit history
further Test 6 rerolling = STOP
```

## Hair requirement carried into next phase

Sample 9 is formally accepted as the full-body Master, but its hair is slightly shorter than the intended final YURA definition.

The next detailed per-part specification phase must strengthen **SUPER-LONG HAIR** as a mandatory identity requirement:

```text
SUPER-LONG is not a loose style label.
The Production specification must make the hair read unmistakably as super-long.
It must reach the waist area clearly.
Generation that shortens it to a merely long / mid-back impression is a FAIL.
The correction should be modest relative to Sample 9, not a dramatic extension substantially below the waist.
```

Do not modify the Master image itself merely to hide this known underlength. Encode the stronger hair-length requirement in the upcoming detailed part specification and Production Visual MD, then verify it in reproduction testing.

## Next phase

Proceed to detailed Master-derived per-part specifications, then Production Visual MD, then GPT reproduction verification from the formal full-body Master + Production Visual MD.
