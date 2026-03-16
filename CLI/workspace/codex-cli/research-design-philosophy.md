# Codex CLI 設計思想調査レポート

## 調査日: 2026-03-16

## 調査目的

Codex CLI入門書の執筆にあたり、Claude Code本との差別化方針を決定するため、
Codex CLIの設計思想における「自律性（Autonomy）」の位置づけを検証する。

## 調査方法

3つの異なるLLMに同一の調査プロンプトを投入し、一次情報（公式ドキュメント・公式ブログ・GitHub・社員発言）に基づく回答を求めた。各項目について「事実」「解釈」「確信度」で整理し、反証も明示的に確認した。

---

## 統合結論

### 主張の検証：「Codex CLIの設計思想の軸は自律性である」

**評価：部分的に正しいが、言い切りは過大評価**（3調査で完全一致）

| 論点 | 調査1 | 調査2 | 調査3 | 合意 |
|------|-------|-------|-------|------|
| 「Codexの軸は自律性」は正しいか | 半分正しいがやや盛りすぎ | 中程度の妥当性 | 部分的に正しいが過大評価 | **三者一致** |
| デフォルトは自律寄りか | Auto（境界付き） | Auto（承認付き） | Auto（対話寄り） | **三者一致** |
| Full Autoの位置づけ | 低リスク自動化プリセット | 上級者向けオプション | 危険/オプション扱い | **三者一致** |
| Claude Codeとの差 | 語彙・ブランディングの違い | 協働 vs 自律の強調度の違い | 人間の役割の度合いの違い | **三者一致** |
| 二項対立は成立するか | しない（両方agenticだ） | しない（Codexにも協働要素あり） | しない（バランス型） | **三者一致** |

### より正確な表現

> Codex CLIの設計思想の軸は、「安全に境界づけられた自律性」と「人間による委任・監督付き協働」の両立である。
> Claude Codeよりは delegation / orchestration / agent autonomy を強く打ち出しているが、「自律一辺倒」ではない。

---

## 詳細ファクト

### 1. Codex CLI公式の設計思想

#### 公式定義
- OpenAIはCodexを「coding agent」と定義
- トップページ: 「One agent for everywhere you code」
- CLI docs: 「Pair with Codex in your terminal」
- 公式ブログ: 「a cloud-based software engineering agent that can work on many tasks in parallel」

#### キーワード使用状況

| キーワード | Codex CLI公式での使用 | 補足 |
|-----------|---------------------|------|
| autonomy / autonomous | 頻度は高くないが、sandbox docs「act autonomously」、GPT-5.3-Codex記事「iterated autonomously」で使用 | 性能向上の重要軸として扱われている |
| delegation / delegate | IDE docs「delegate tasks to Codex Cloud」、app記事「delegating work」で明示的に使用 | 「仕事を振る/任せる」語彙で説明されている |
| pair programming / collaboration | CLI docs「Pair with Codex」、blog「collaborate with agents」で使用 | ただしAnthropicほどブランド中核語として固定していない |
| developer-in-the-loop | **確認できず**。代わりに「review」「steer」「interact」「approval」「supervise」 | スローガン化していない |
| sandbox / isolation / safety | **非常に強い**。繰り返し出現 | 安全制御は設計の中心 |

### 2. 承認モード（自律度の設計）

#### 重要な事実：モード名の変遷
- **旧称**: Suggest / Auto Edit / Full Auto（初期TypeScript CLI時代）
- **現行**: Read-only / Auto / Full Access（Rust CLI移行後）
- OpenAI自身がGitHub issue #1248で「承認とサンドボックスを混同していた」と認め、現行では分離

#### 現行モードの位置づけ

| モード | デフォルト | 位置づけ | 自律度 |
|--------|----------|---------|--------|
| Read-only | - | 変更・コマンド実行は承認必須 | 低 |
| **Auto** | **デフォルト** | 作業ディレクトリ内は自動、外部は承認 | **中（推奨）** |
| Full Access | - | 制限なし。「Use with extreme caution」「Use sparingly」 | 高（上級者向け） |

- `--full-auto` は「convenience alias」「lower-risk local automation preset」
- `--yolo` / `dangerously-bypass-approvals-and-sandbox` は「not recommended」
- **デフォルトが「中間」であることが、「完全自律」を標準にしていないことの最大の証拠**

### 3. Claude Codeとの思想比較

#### 公式表現の対比

| 観点 | Claude Code | Codex CLI |
|------|------------|-----------|
| 公式の自己紹介 | 「agentic coding tool」 | 「coding agent」 |
| ブランド語彙 | collaborate, pair programming, thinking partner | agent, delegate, automate workflows |
| 自律性への言及 | 「working autonomously for longer」（研究記事） | 「act autonomously」（sandbox docs） |
| 人間の役割 | 「responsive to your input」「interruptibility」 | 「review」「steer」「approve」「supervise」 |
| 安全設計 | アプリ層（hooks 17イベント、細粒度制御） | カーネル層（sandbox、ネットワーク遮断、ファイルシステム隔離） |

#### 重要な発見
- **Claude Codeも実態は十分に自律的**（Anthropic自身が「users let Claude run autonomously, intervening only when needed」と記述）
- **Codexも協働要素は強い**（CLI docs「Pair with Codex」、GPT-5.3-Codex blog「Much like a colleague, you can steer and interact」）
- **二項対立は成立しない。違いは「どの語彙をブランド前面に出すか」にある**

### 4. 反証の確認結果

| 反証の問い | 結果 |
|-----------|------|
| Codexが「協働」を前面に出している証拠はあるか | **ある**。「Pair with Codex」「collaborate with agents」「steer and interact」 |
| 「自律は一機能に過ぎない」と読めるか | **ある程度読める**。Full Autoは注意喚起付きオプション、デフォルトはAuto |
| 初回体験は自律寄りか対話寄りか | **対話寄り**。インタラクティブUI起動、承認フロー前提 |

---

## 書籍構成への影響

### 確定した方針

#### 1. 著者スタンスの一貫性
- Claude Code本で確立した「AIと人間が協働してコードを書く」哲学はそのまま維持
- Codex本は「同じ哲学を、OpenAIの道具立てで実現するとどうなるか」
- 「ペアプロ vs 自律」の二項対立には**しない**

#### 2. 独立完結性
- Codex本だけ読んで、ゼロからCodex CLIを使えるようになる構成
- 本文中にClaude Code本への依存・参照を入れない
- 共通原則（プロンプティング等）はCodexの具体例で書き直す（選択肢B）
- クロスセルは「おわりに」や著者紹介で自然に触れる程度

#### 3. 差別化の軸（暫定）
「ペアプロ vs 自律」ではなく、以下の実装レベルの違いを軸にする:
- 安全の担保方法（hooks vs sandbox）
- カスタマイズの仕組み（CLAUDE.md vs AGENTS.md＝オープン標準）
- 承認の粒度（イベント駆動 vs モード選択）
- 並列実行の手触り
- エコシステム（OpenAI課金済みユーザーの受け皿）

### 未決定事項（差分調査で解決予定）
- 書籍化すべき具体的な機能・体験の差分一覧
- 章立て・構成案の確定
- 題材（作るもの）の決定
- キャラクター配置

---

## 次のアクション

1. **差分調査**: Claude CodeとCodex CLIの「書籍化すべき機能・体験の差分」を洗い出す
   - A. Codex固有の機能（Claude Codeに対応なし）
   - B. 同じ目的だが実現方法が異なる機能
   - C. エコシステム・課金体系の違い
   - D. ワークフロー・体験の違い
2. 差分調査の結果を踏まえて構成案を策定
3. thinking-hub.md の作成
