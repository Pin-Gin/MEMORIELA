# YURA Master Benchmark

YURA Master候補を、固定Git Authority検証 → **sealed Authority bundle** → Codex prompt compile → OpenAI Image API生成 → cost/QA記録、の順で再現可能に実行するローカルベンチマーク。

## Authority lifecycle

`YURA_VISUAL_TEXT.md` は現在、**OpenAI API Master-generation specification** としてのみ使用する。
Master完成後の通常Productionでは自動読込しない。詳細:

`visuals/yura/identity/master/YURA_MASTER_GENERATION_LIFECYCLE.md`

## Core security / reproducibility boundary

Codexはリポジトリを直接探索しない。

Git/Authorityの事実確認はPython runnerが先にローカルで行う:

```text
current local Git
  -> git fetch origin main
  -> require HEAD == origin/main
  -> require configured Authority paths clean
  -> require all configured Authority files exist
  -> compute SHA-256 locally
  -> embed complete text Authority contents
  -> represent PNG Authorities by verified path/hash/role metadata
  -> write sealed_authority_bundle.json
  -> send that sealed bundle directly to Codex via stdin
```

Codex compile段階では:

```text
filesystem access = NOT REQUIRED
shell access      = NOT REQUIRED
Git access        = NOT REQUIRED
MCP               = NOT REQUIRED
user Codex config = IGNORED
```

`codex exec --ignore-user-config --sandbox read-only` を使用し、Codexにはsealed bundleだけを入力する。
これにより `characters/YURA.md`、`manuscript/**`、Git history、Memory等の禁止ソースはCodex入力に入らない。

PNGの画素はCodex compileには埋め込まない。Face Reference / Body Geometry Guideの実ファイルは、manifest検証後にrunnerがImage APIへ直接渡す。

## Why one successful run first

最初は**成功した完全runを1回だけ**得る。

目的:

1. sealed bundle / Authority順 / SHA-256を確認
2. Codex compiled promptとSHA-256を保存
3. Image API usageを保存
4. 専用OpenAI Projectの実課金額を確認
5. 1回総額が設定閾値未満なら10回batchを検討

デフォルトbatch閾値は `config.json` の `$1.00/run` 未満。
失敗したCodex-only attemptは成功runとして数えないが、Project costには含まれる可能性があるので別途記録する。

## Requirements

- Python 3.11+
- Codex CLI
- OpenAI Python SDK
- Git working copy of `Pin-Gin/MEMORIELA`
- benchmark用OpenAI Project API key
- 正確なドル課金照合を行う場合は Organization Admin API key

Install:

```powershell
python -m pip install -r tools/yura-master-benchmark/requirements.txt
```

## Billing isolation

CodexとImage APIは同じbenchmark OpenAI ProjectのAPI-key billingで実行する。
現在の汎用Project名は例として:

```text
creator-master-benchmark
```

PowerShell current session:

```powershell
$env:OPENAI_API_KEY="sk-..."
$env:OPENAI_PROJECT_ID="proj_..."
```

Project cost query用:

```powershell
$env:OPENAI_ADMIN_KEY="sk-admin-..."
```

秘密キーはGitにもチャットにも保存しない。
Codex CLIがAPI-key認証であることを実行前に確認する。

## One run

Repository root:

```powershell
python tools/yura-master-benchmark/run_once.py
```

処理順:

1. `git fetch origin main`
2. local `HEAD == origin/main` を要求
3. configured Authority対象に未コミット変更がないことを要求
4. 全Authority SHA-256をPythonでローカル計算
5. text Authority本文 + PNG path/hash/role metadataからsealed bundleを構築
6. bundleとbundle SHA-256をrun directoryへ保存
7. Codexへinstruction + sealed bundleをstdinで送信
8. Codexが `authority_manifest.json` と完全な `compiled_prompt` を出力
9. runnerがcommit・Authority順・ordinal・role・SHA・denied_sources・image reference orderを再検証
10. Image APIへFace Reference → Body Geometry Guideの順で実ファイルを渡す
11. configured Image model / size / qualityで1枚生成
12. usage/cost/QA pending状態を保存

各成功runには概ね:

```text
runs/run_YYYYMMDDTHHMMSSZ/
  run_meta.json
  sealed_authority_bundle.json
  sealed_authority_bundle.sha256
  codex_input.sha256
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

pre-image failure時は `failure.json` も保存する。
`runs/` はGit管理対象外。

## Sealed bundle invariants

固定Authority順は `config.json` の `authority_order` が唯一の順序定義。
runner内のdeterministic role mappingとも一致する必要がある。

Codexはmanifestで次をそのまま返さなければrunnerが停止する:

- `git_commit`
- Authority order
- ordinal
- path
- SHA-256
- declared role
- `denied_sources`
- `image_reference_order`

Codexがfilesystem/shellを使えないことはエラー条件ではない。sealed modeでは意図的に不要。

## Authoritative dollar cost

Image API responseにusageがある場合、runnerは参考推定値を `cost.json` に入れる。
ただし正式評価ではProject costを優先する。

成功run後:

```powershell
python tools/yura-master-benchmark/query_project_cost.py tools/yura-master-benchmark/runs/<RUN_DIR>
```

`OPENAI_ADMIN_KEY` と `OPENAI_PROJECT_ID` が必要。
Project cost集計には遅延があり得る。

## Ten-run batch

成功したseed runのProject cost確認後のみ:

```powershell
python tools/yura-master-benchmark/run_batch.py --seed-run tools/yura-master-benchmark/runs/<RUN_DIR> --runs 10 --query-costs
```

seed runのauthoritative costが `config.json` の閾値以上なら自動停止する。

`--allow-estimate` は明示的にImage API estimateだけで進めたい場合のoverrideで、正式なコスト評価には使用しない。

## What stability means

各runでCodex compileを再実行する。

`compiled_prompt.sha256` が10回すべて同一:

- sealed input / prompt compileが安定
- 画像差分は主にImage model側sampling差

hashがrun間で異なる:

- 同一sealed inputに対してCodex compileが揺れている可能性
- Image PASS率評価前にcompiler安定性を確認する

`sealed_authority_bundle.sha256` も比較し、入力Authority自体が同じだったかを必ず区別する。

## QA

生成直後は必ず:

```text
candidate = QA_PENDING
master_promotion = NO
```

最終PASSは作者承認必須。
少なくとも以下を確認する:

- Face Identity
- 7.1–7.3頭身 / target 7.2
- 耳20–22% / HARD MAX 23%
- Body Geometry / unwanted body enlargement or elongation
- 1440×2560 / 9:16
- figure occupancy 88–90% / target 89%
- 上下余白5–6%
- 中央配置
- hair / overall identity

`qa.json` の `author_pass=true` は作者が確認した場合だけ設定する。

## Frozen benchmark model condition

filesystem/tool問題の原因切り分け中はモデル条件を同時変更しない。
現在 `config.json` に固定されたCodex model / Image model / pricing snapshotを使う。

モデルや料金条件を変更する場合は `config.json` を明示的に変更し、そのcommitを別benchmark条件として扱う。
