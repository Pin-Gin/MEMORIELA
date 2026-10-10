# YURA Master Benchmark — Test 2 実行結果

日付: 2026-10-10
状態: **TEST 2 COMPLETE / REJECT FACE-REFERENCE IMAGE ISOLATION / COMPOSITION BLOCKED**

このファイルは運用上の実験記録であり、YURA Visual Authorityではない。

## Test 2 の目的

Test 1で総頭身が約6.51頭身に留まったため、Face Reference画像のピクセル入力が全身の頭身を約6.4付近へ引っ張っているかを診断する。

Test 2では、Face ReferenceのAuthority上の存在とroleは維持したまま、Image APIへのFace Reference画像ピクセル入力だけを一時的に外し、Body Geometry Guideを唯一の画像Referenceとして1回の診断RAWを生成した。

## 実行結果

- Image API生成は成功した。
- 添付された表示コピーは1152×2048。
- Face Reference画像を外した結果、顔IdentityがTest 1 / active Face Referenceから明確に変化した。
- 著者判断: Face Reference画像を分離する方式は採用しない。
- 表示コピー上の総頭身は概ね約6.5頭身付近に留まり、Test 1（約6.51頭身）から7.2方向への明確な改善は確認できない。
- Compositionは実行しない。

## 診断判断

```text
Face Reference画像を外す
-> Face Identityが悪化
-> 総頭身は約6.5付近のまま
-> 7.2方向への明確な改善なし
```

したがって、次を採用する。

```text
「Face Reference画像そのものが約6.4頭身へ強く引っ張っている」
-> Test 2では支持されない

Face Reference画像
-> Face Identity維持のため次の生成から復帰させる

残る原因候補
-> Body Geometry enforcementの効き方
-> モデル側の全身生成バイアス
```

Test 2 RAWは診断用のみであり、Visual Authority、Master、Master候補として昇格させない。

## 次のactive test

**Test 3 — 特定された層だけを解く。**

Test 3では:

```text
Face Reference画像を復帰する
既存Face Identityを変更しない
既存Body情報を変更しない
Compositionを変更しない
renderingを同時変更しない
7.2頭身が生成結果へ反映されないBody Geometry enforcement層だけを検証する
```

Test 3の具体的差分は著者へ先に開示し、明示承認後にのみGitへ反映する。
