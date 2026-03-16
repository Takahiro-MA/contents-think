# Codex CLI vs Claude Code 機能・体験差分調査レポート

## 調査日: 2026-03-16

## 調査目的

Codex CLI入門書で「何を書くか」を決定するため、Claude Codeとの具体的な機能・体験差分を洗い出す。
3つの異なるLLMに同一プロンプトを投入し、一次情報ベースで回答を求めた。

---

## 統合結論

### 差分の中心は4つの軸

1. **実行面**: CLI単体ではなく Cloud / App / IDE / exec を含む「Codex実行基盤」
2. **安全制御の実装**: hooks（イベント駆動）vs sandbox + 承認モード（境界駆動）
3. **設定・標準・エコシステムの作法**: AGENTS.md（オープン標準）、profiles、TOML
4. **実際の手触り**: セットアップ、日常フロー、デバッグ、並列実行の体験差

---

## カテゴリA：Codex CLI固有の機能

### 書籍化優先度マトリクス（3調査の合意）

| 機能 | 調査1 | 調査2 | 調査3 | 合意 | CC本重複 |
|------|-------|-------|-------|------|----------|
| **A1. Codex Cloud** | 高 | 高 | 高 | **最高** | なし |
| **A2. Desktop App** | 高 | 高 | 高 | **最高** | なし |
| **A3. codex exec（非対話モード）** | 高 | 高 | 高 | **最高** | なし |
| **A4. Web検索（cached/live）** | 高 | 高 | 中 | **高** | なし |
| **A5. AGENTS.md（オープン標準）** | 最高 | 高 | 高 | **最高** | テーマ重複あり（CLAUDE.md）、標準化文脈は新規 |
| **A6. Skills クロスプラットフォーム** | 高 | 中 | 中 | **中高** | テーマ重複あり |
| **A7. Profiles（--profile）** | 高 | 中 | 中 | **中高** | なし |
| **A8. ターミナル読み取り** | 中高 | 中 | 高 | **中高** | なし |
| **A9. app-server / MCP server** | 中 | 中 | - | **中** | なし |

### A1. Codex Cloud（クラウドサンドボックス実行）

**概要**
- OpenAI公式: 「Delegate to Codex in the cloud」
- CLI から `codex cloud` / `codex cloud exec` でクラウドタスクを起動
- GitHub接続前提、並列にタスクを流せる
- ローカル環境を汚さない隔離実行

**ユースケース**
- ローカル環境を汚したくない検証
- 複数タスクの投げ分け・長時間バックグラウンド委任
- レビュー待ちの間に別作業を進める

**Claude Codeとの差**: Claude CodeにはCLI→クラウドタスクを「コマンド1本で起動・結果反映」する設計がない

**書籍での扱い**: 章の柱にすべき。「ローカルCLIとクラウドの使い分け」はCodex本の独自性の最重要候補

### A2. Codex Desktop App

**概要**
- 専用デスクトップアプリ（macOS、Windows beta）
- parallel threads / built-in worktree support / automations / Git機能
- integrated terminal でdev serverの状態確認が可能
- CLI/IDE/Cloudとの橋渡し

**ユースケース**
- IDEから離れて並列にagentを回す
- worktree単位で作業を分離
- terminal outputを踏まえた会話

**Claude Codeとの差**: Claude Codeは「Claude DesktopのCode tab」であり、Codexのような「専用アプリ」ではない

**書籍での扱い**: 「どこまでCLIで、どこからAppか」を整理する章として有効

**注意**: ブリーフの「キャプチャを使わない」方針との整合性を要検討。Appの解説はテキストベースで可能か？

### A3. 非対話モード（codex exec）

**概要**
- `codex exec` で対話UIなしの非対話実行
- stdout / JSONL出力 / resume対応
- `codex exec resume --last "..."` / `codex exec resume <session-id> "..."` で再開可能

**ユースケース**
- CI/CDパイプライン組み込み
- PR前の自動修正・夜間の一括解析
- レビューコメント対応の自動化

**Claude Codeとの差**: Claude Codeにも非対話モードはあるが、exec + resume + JSON出力を1つのコマンド体系で抽象化している設計はCodex固有

**書籍での扱い**: CI/CD統合の章として独立させる価値あり

### A4. Web検索統合（cached / live mode）

**概要**
- ローカルタスクでWeb検索がデフォルト有効
- cached mode（既定）: OpenAI管理のインデックス経由、prompt injection露出を低減
- live mode: `--search` または `web_search = "live"` で切替
- disabled も選択可能

**ユースケース**
- 安全性を優先した最新情報参照
- 依存関係やエラーメッセージの検索
- 外部仕様確認

**Claude Codeとの差**: Claude CodeにはMCP経由のWeb検索はあるが、cached/liveの二段階運用概念はない

**書籍での扱い**: 安全設計やCI/CDの文脈で紹介

### A5. AGENTS.md のオープン標準

**概要**
- Linux Foundation傘下の Agentic AI Foundation に寄贈
- 60,000+のOSSプロジェクトで採用
- `~/.codex/AGENTS.md` / `AGENTS.override.md` と repo内の `AGENTS.md` を階層的に読込
- Codex, Cursor, GitHub Copilot, Amp, Windsurf, Gemini CLI等で共通利用可能

**Claude Codeとの差**: CLAUDE.mdはAnthropic固有。機能としては類似だが、標準化・移植性が根本的に異なる

**書籍での扱い**: 章の柱。「持ち運べるプロジェクトルール」として、CLAUDE.mdとは切り口を変えて書ける

### A6. Codex Skills（クロスプラットフォーム標準）

**概要**
- SKILL.md + オプションのスクリプト・リファレンスで構成
- CLI / IDE extension / App で共通利用
- metadata先読み → 必要時に本文ロード（progressive disclosure）
- オープンエージェントスキル標準に基づく

**Claude Codeとの差**: Claude Codeのskillsも強力だが、Anthropic独自拡張。Codexは標準準拠・横断利用が前面

**書籍での扱い**: AGENTS.mdと合わせて「標準化エコシステム」の文脈で

### A7. Profiles（--profile設定切替）

**概要**
- `config.toml` に `[profiles.<name>]` を定義
- `codex --profile <name>` で起動時に切替
- model / approval_policy / reasoning などを定義可能
- 現時点ではexperimental

**ユースケース**
- レビュー用、実装用、軽量探索用、危険作業用など作業モードの分離

**Claude Codeとの差**: Claude Codeは階層スコープ型で、profileのような名前付き切替はない

**書籍での扱い**: 実運用ノウハウとしてコラムまたはセクション

### A8. ターミナル読み取り・統合UI

**概要**
- Codex App: integrated terminal の出力を読み取り可能
- CLI: `!` でシェルコマンド実行、結果をコンテキストに取込
- `@` でワークスペース検索

**ユースケース**
- dev server監視、再ビルド確認、ログ起点デバッグ

**Claude Codeとの差**: Claude CodeのMCPやBash toolで同様のことは可能だが、`!` コマンドの直感的UXはCodex固有

**書籍での扱い**: 実践ワークフロー章で例として

---

## カテゴリB：同じ目的だが実現方法が異なる機能

### 対応関係サマリー

| 目的 | Claude Code | Codex CLI | 差分の本質 | 書籍価値 |
|------|------------|-----------|-----------|----------|
| プロジェクトルール | CLAUDE.md | AGENTS.md | プロプライエタリ vs オープン標準 | **最高** |
| 安全制御 | hooks（17イベント、アプリ層） | sandbox + 承認モード（カーネル層） | イベント駆動 vs 境界駆動 | **高** |
| カスタム自動化 | Skills + custom commands | Skills（クロスプラットフォーム） | 独自拡張 vs 標準準拠 | **中高** |
| 並列実行 | Subagent + git worktree（手動） | 並列agent + worktree自動分離 + Cloud | ローカル手動 vs ローカル+Cloud自動 | **高** |
| 設計レビュー | Plan mode（Shift+Tab） | Plan/Pair/Execute（/plan） | UIキーバインド vs slash command | **中** |
| 外部ツール連携 | MCP servers（MCPクライアント） | MCP + Agents SDK + app-server（MCPサーバーにもなれる） | クライアント vs クライアント+サーバー | **高** |
| 設定管理 | JSON + スコープ階層 | TOML + profiles | 階層型 vs プロファイル切替型 | **中高** |

### 特記：安全制御の設計差（書籍の差別化ポイント）

**Claude Code**: hooks 17イベントでアプリ層の細粒度制御
- SessionStart, PreToolUse, PostToolUse, Stop 等
- シェルスクリプトを差し込める柔軟性
- 学習コストは高いが、企業内ワークフロー制御に強い

**Codex CLI**: sandbox + 承認モードでカーネル層の境界制御
- sandbox_mode: danger-full-access / workspace-write / full
- approval_policy: never / on-request / untrusted
- `--full-auto` は workspace-write + on-request のエイリアス
- 導入しやすく直感的だが、カスタム性はhooksに劣る

**書籍での扱い**: 「安全に実験する仕組み」として、Claude Code本のhooks章とは完全に別の切り口で書ける

### 特記：外部ツール連携の非対称性

**Claude Code**: MCPクライアントとして外部ツールを接続する
**Codex CLI**: `codex mcp` でCodex自体がMCPサーバーになれる（他のagentからCodexを呼べる）

→ Codexは「エージェント基盤としての再利用性」を設計に組み込んでいる

---

## カテゴリC：エコシステム・課金体系の違い

| 観点 | Claude Code | Codex CLI | 書籍価値 |
|------|------------|-----------|----------|
| 価格 | Pro $20/月、Max 5x $100/月、Max 20x $200/月 | Plus $20/月に含まれる | **高** |
| APIキー | Anthropicアカウント + 別途API課金 | ChatGPTアカウント統合、既存課金流用可能 | **高** |
| モデル | Opus 4.6 / Sonnet 4.6 / Haiku 4.5 | GPT-5.4 / GPT-5.3-Codex / codex-mini | **高** |
| OSS | プロプライエタリ（71.5K stars） | Apache-2.0（62.4K stars） | **高** |
| コミュニティ | Anthropicエコシステム | AGENTS.md標準 + Linux Foundation | **中** |
| IDE | VSCode / Cursor / JetBrains / Desktop / Web | VSCode / Cursor / Windsurf / JetBrains | **中高** |

### 特記：$20の敷居の低さ

- Codexは既存のChatGPT Plus ($20/月) に含まれる → 追加課金なしで始められる
- Claude Codeは Pro ($20/月) でも使えるがヘビーユースでMax誘導が強い
- **ターゲット読者（ChatGPTユーザー）にとって「今の課金のまま始められる」は最大の訴求点**

### 特記：OSSの実利

- Codex CLI: Apache-2.0で商用利用・改変・再配布可能
- Claude Code: プロプライエタリライセンスで改変・再配布は原則禁止
- 読者にとっての実利: 挙動追跡・issue確認・将来の拡張可能性・自社製品組み込み

---

## カテゴリD：ワークフロー・体験の違い

| 観点 | Claude Code | Codex CLI | 書籍価値 |
|------|------------|-----------|----------|
| 初回セットアップ | curl/Homebrew + APIキー設定 | npm install + ChatGPTログイン | **高** |
| 日常フロー | ローカル対話で即時フィードバック | CLI + App + Cloud の使い分け | **最高** |
| エラー/デバッグ | hooks前後処理、GUIレビュー型 | sandbox内ロールバック、ターミナル読取型 | **高** |
| レスポンス速度 | モデル切替でコスト最適化 | Rust実装、skills progressive disclosure、25%高速化 | **中高** |
| 大規模コードベース | Subagent + context partitioning | Cloud + 1M context + tool search | **高** |
| チーム運用 | Enterprise admin controls | AGENTS.md標準 + profiles + codex exec | **高** |

### 特記：日常フローの構造的な違い

**Claude Code**: 同じengineが各surface（terminal / IDE / desktop / web）で動く一貫性
**Codex CLI**: CLI / App / IDE / Cloud / exec を場面で使い分ける多面体

→ Codex本では「**どのsurfaceをいつ使うか**」が章立ての自然な軸になる

---

## 書籍化すべき差分の優先順位（最終版）

### Tier 1：章の柱にすべき差分（必須）
1. **Codex Cloud とローカルの使い分け** — CC本に完全に未重複
2. **AGENTS.md のオープン標準** — CC本のCLAUDE.md章と「材料」は同じだが「料理」が完全に違う
3. **sandbox + 承認モードの安全設計** — CC本のhooksとは根本的に異なるアプローチ
4. **codex exec と非対話モード** — CC本にCI/CD特化なし
5. **surfaceの使い分け（CLI/App/Cloud/IDE）** — CC本は「同一engine」前提、Codexは「多面体」

### Tier 2：章やコラムで厚く扱う差分
6. **profiles / TOML設定管理** — 実運用ノウハウとして映える
7. **Web検索（cached/live）** — Codex固有、安全設計と接続
8. **モデル選択（GPT-5.4 / 5.3-Codex / mini）** — subscription消費と直結
9. **Codex App + integrated terminal** — 体験の差分が大きい
10. **並列実行の自動化** — CC本のSubagentと目的は同じだが手触りが違う

### Tier 3：触れるが深入りしない差分
11. 価格モデル・APIキー統合（導入章で軽く）
12. OSS / Apache-2.0の意味（コラム向き）
13. Skills クロスプラットフォーム互換（AGENTS.mdと合わせて言及）
14. IDE連携の対応表（付録向き）
15. コミュニティ規模（おわりに向き）

---

## 次のアクション

1. 本レポートと設計思想レポートを統合し、**構成案（章立て）**を策定
2. 題材（作るもの）の決定
3. thinking-hub.md の作成開始
