# YURA Master Benchmark — Test 3 実行結果

日付: 2026-10-10
状態: **TEST 3 COMPLETE / BODY GEOMETRY LANDMARK ENFORCEMENT FAIL / FACE REFERENCE RESTORED / COMPOSITION BLOCKED**

このファイルは運用上の実験記録であり、YURA Visual Authorityではない。

## Test 3 の目的

Test 2により、Face Reference画像を外しても総頭身が約6.5付近から7.2方向へ明確に改善せず、Face Identityだけが悪化することを確認した。

Test 3ではFace Reference画像を復帰したうえで、既存のAUTHOR-APPROVED Body Geometry Guideにすでに存在するランドマーク値を、Image API用compiled prompt内のrelative geometry anchorとして明示的に強制した。

既存Face Identity、既存Body情報、Body Geometry Authority、Composition、rendering条件は変更していない。

## Test 3 の追加enforcement

既存Body Geometry Guide由来の以下の値を使用した。

```text
crown   = 160
chin    = 340
crotch  = 856
knee    = 1156
soles   = 1456
1 head  = 180

crown→soles  = 7.2 heads
crown→crotch = 3.8667 heads
chin→crotch  = 2.8667 heads
crotch→knee : knee→soles = 1 : 1
```

これらは出力キャンバスの絶対pixel座標ではなく、承認済みBody Guide内部のrelative geometry anchorとして扱った。

## 実行結果

Image API生成は成功した。

添付された1152×2048表示コピーからの予備測定:

```text
crown   ≈ y 35
chin    ≈ y 338
crotch  ≈ y 1006
knee    ≈ y 1390
soles   ≈ y 1996

total head ratio ≈ 6.47 heads
inseam proxy     ≈ 50.5%
chin→crotch      ≈ 2.20 heads
```

この測定は表示コピーからの予備測定であり、原寸RAWによる正式pixel calibration値ではない。

## 現行gate判定

```text
total head ratio
target      = 7.2
acceptable  = 7.1–7.3
Test 3      ≈ 6.47
result      = FAIL

inseam proxy
target      = 46.0–46.5%
Test 3      ≈ 50.5%
result      = FAIL

chin→crotch
target      = 2.7985–2.9420 heads
Test 3      ≈ 2.20 heads
result      = FAIL
```

Compositionは実行しない。

## Face Identity判定

Face Reference画像を復帰したことで、Test 2で発生したFace Identityの明確な変化は改善した。

したがって:

```text
Face Reference画像を使用する
-> 継続

Face Reference画像を分離する
-> 不採用
```

## 診断判断

Test 1:

```text
約6.51 heads
```

Test 2:

```text
約6.5 heads
Face Identity悪化
```

Test 3:

```text
約6.47 heads
Face Identity復帰
landmark enforcement追加
```

Test 3でも総頭身は7.2方向へ実質的に改善しなかった。

したがって、

```text
単純な7.2頭身の文章指定不足
+
既存ランドマーク数値の文章上の明示不足
```

だけでは、約6.5頭身への収束を説明できない。

既存Body Guideのランドマークをcompiled promptへ明示的に運んでも生成Geometryがほぼ同じ領域へ収束したため、同種のprompt文言をさらに重ねるだけでは改善可能性が低い。

残る問題は、Image API生成段階でBody Geometry Guideの構造が期待する強さのGeometry拘束として反映されていないことにある可能性が高い。

これはBody Authority自体を変更する根拠ではない。

## Test 3 結論

```text
Face Identity preservation = PASS方向
7.2 total-head enforcement = FAIL
inseam gate                = FAIL
torso numeric gate         = FAIL
Composition                = BLOCKED
Test 3 RAW                 = QA / diagnostic sample only
Visual Authority promotion = NO
Master promotion           = NO
```

Test 3 RAWをVisual Authority、Master、Master候補へ昇格させない。

次の仮説・Test 4はこの記録から自動的に決定しない。
著者承認前に新しいBody仕様、Face仕様、Composition仕様を変更しない。
