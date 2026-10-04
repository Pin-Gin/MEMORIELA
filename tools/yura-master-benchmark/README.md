# YURA Master Benchmark

YURA Master候補を、固定したGit Authority解決 → Codex manifest/prompt compile → OpenAI Image API生成 → cost/QA記録、の順で再現可能に実行するためのローカルベンチマーク。

## Authority lifecycle

`YURA_VISUAL_TEXT.md` は現在、**OpenAI API Master-generation specification** としてのみ使用する。
Master完成後の通常Productionでは自動読込しない。詳細は:

`visuals/yura/identity/master/YURA_MASTER_GENERATION_LIFECYCLE.md`

## Why one run first

最初は必ず1回だけ実行する。

1. Codexが読んだAuthority順とSHA-256を確認
2. Codex trace / usageを保存
3. Image APIのusageを保存
4. 専用OpenAI Projectの実課金額を確認
5. 1回総額が設定閾値未満なら10回batchへ進む

デフォルトbatch閾値は `config.json` の `$1.00/run` 未満。

## Requirements

- Python 3.11+
- Codex CLI
- OpenAI Python SDK
- Git working copy of `Pin-Gin/MEMORIELA`
- benchmark専用OpenAI ProjectのAPI key
- 正確なドル課金照合を行う場合は Organization Admin API key

Install:

```powershell
python -m pip install -r tools/yura-master-benchmark/requirements.txt
```

## Billing isolation — important

この実験では、CodexとImage APIを**同じ専用OpenAI Project**へ課金する。
例: `yura-master-benchmark`

通常のChatGPT認証のCodex利用枠ではなく、**API-key billingのCodex**を使用すること。
API-key利用時のCodexはAPI料金として課金される。ChatGPT認証のままでは「1回何ドル」の実験にならない。

PowerShell current session example:

```powershell
$env:OPENAI_API_KEY="sk-...benchmark-project-key..."
$env:OPENAI_PROJECT_ID="proj_..."
```

正確なproject cost queryを自動化する場合:

```powershell
$env:OPENAI_ADMIN_KEY="sk-admin-..."
```

API keyやAdmin keyをGitへ保存しないこと。

Codex CLIもbenchmark projectのAPI-key認証であることを実行前に確認する。

## One run

Repository rootで:

```powershell
python tools/yura-master-benchmark/run_once.py
```

処理順:

1. `git fetch origin main`
2. local `HEAD == origin/main` を要求
3. Authority対象ファイルに未コミット変更がないことを要求
4. 全Authority SHA-256をローカル計算
5. `codex exec --json` で指定順のみ読ませる
6. Codexが `authority_manifest.json` と完全な `compiled_prompt` を出力
7. runnerが順番・commit・SHAを再検証
8. Image APIへFace Reference → Body Geometry Guideの順で参照画像を渡す
9. `gpt-image-2.5-sunburst-2026-09-08` / `1440x2560` / `high` で1枚生成
10. usage/cost/QA pending状態を保存

各runは:

```text
runs/run_YYYYMMDDTHHMMSSZ/
  run_meta.json
  authority_manifest.json
  codex_trace.jsonl
  codex_stderr.log
  codex_usage_candidates.json
  compiled_prompt.txt
  compiled_prompt.sha256
  result.png
  image_response.json
  cost.json
  qa.json
```

`runs/` はGit管理対象外。

## Authoritative dollar cost

Image API responseにusageがある場合、runnerは参考推定値を `cost.json` に入れる。
ただし**課金の正解はProject cost**とする。

1回生成後:

```powershell
python tools/yura-master-benchmark/query_project_cost.py tools/yura-master-benchmark/runs/<RUN_DIR>
```

`OPENAI_ADMIN_KEY` と `OPENAI_PROJECT_ID` が必要。
Organization costs APIのproject-filtered結果を取得し、`authoritative_total_project_cost_usd` に保存する。
課金集計が遅延している場合はデフォルト90秒までpollする。

## Ten-run batch

1回目のproject cost確認後:

```powershell
python tools/yura-master-benchmark/run_batch.py --seed-run tools/yura-master-benchmark/runs/<RUN_DIR> --runs 10 --query-costs
```

seed runのauthoritative costが `config.json` の閾値以上なら自動停止する。

どうしてもAdmin cost未取得の段階で試験する場合のみ:

```powershell
python tools/yura-master-benchmark/run_batch.py --allow-estimate --runs 10
```

この場合の判定はImage API estimateのみなので、正式なコスト評価には使用しない。

## What stability means

各runでCodexを再実行する。

`compiled_prompt.sha256` が10回すべて同一:
- Authority解決/Prompt compileは安定
- 画像差分は主にImage model側のsampling差

`compiled_prompt.sha256` がrun間で異なる:
- Codex compile段階が揺れている
- 画像PASS率を評価する前にPrompt compilerを固定すべき

## QA

生成直後は必ず:

- `candidate = QA_PENDING`
- `master_promotion = NO`

最終PASSは作者承認を必須とする。
少なくとも以下を確認する:

- Face Identity
- 7.1–7.3頭身 / target 7.2
- 耳20–22% / HARD MAX 23%
- BODYの横幅・縦伸び
- 胸部の体格比と形状
- 1440×2560 / 9:16
- figure occupancy 88–90% / target 89%
- 上下余白5–6%
- 中央配置

`qa.json` の `author_pass=true` は作者が確認した場合だけ設定する。

## Current API choices

Benchmark開始時点の固定値:

- Image model: `gpt-image-2.5-sunburst-2026-09-08`
- output: `1440x2560`, PNG, opaque, quality=`high`
- Codex model: `gpt-5.3-codex`

モデルや料金を変更する場合は `config.json` を変更し、そのcommitを別benchmark条件として扱う。
