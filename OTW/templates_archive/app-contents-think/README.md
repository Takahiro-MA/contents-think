# AI Co-Design Project: Operation Manual (Web版)

このフォルダは、**Claude Code on the Web** とのアプリ要件検討プロジェクト用のワークスペースです。

> **注意**: これはWeb版に最適化されたテンプレートです。CLI版は `CLI/templates/app-contents-think/` にあります。

## 必須ファイル構成
開始前に以下のファイルが存在することを確認してください。

* `project_rules.md`: AIへの役割定義・運用ルール（憲法）
* `thinking-hub.md`: 思考の庭（Wiki）
* `workflow.md`: 全体のロードマップ

---

## セッションの始め方 (Start Routine)

Web版では、GitHubリポジトリから直接セッションを開始します。

### 1. セッション開始コマンド
リポジトリのルートから、以下のカスタムコマンドを実行：

```bash
/app-start
```

このコマンドは自動的に以下を実行します：
- `project_rules.md` と `thinking-hub.md` の読み込み
- Sparring Mode での起動
- 今日のテーマの確認

### 2. 手動で開始する場合（コマンド未設定時）
カスタムコマンドが設定されていない場合は、以下を手動で実行：

```text
OTW/workspace/[プロジェクト名]/project_rules.md と thinking-hub.md を読み込んで、
project_rules.md の BOOT BLOCK に従いセッションを開始してください。
今日のテーマは「[ここに今日のテーマを入れる]」です。
[Mode: Sparring] でお願いします。
```

---

## 運用コマンド (Operational Commands)

会話中に使用する主な制御コマンドです。

| コマンド | 動作 | 使うタイミング |
| :--- | :--- | :--- |
| `/app-start` | プロジェクト開始 | セッション開始時 |
| `/sparring` | **Sparring Mode** へ切替 | 議論・壁打ちをしたいとき |
| `/architect` | **Architect Mode** へ切替 | 設計案や技術選定を詰めるとき |
| `/spec` | **Spec Writer Mode** へ切替 | 要件定義書や仕様書を書かせるとき |
| `/archive` | **Archivist Mode** へ切替 | 議論終了後、`thinking-hub.md` を更新するとき |

> **Note**: カスタムコマンドは `.claude/commands/` で定義されています。

---

## 終了時の作法 (End Routine)

Web版では、変更をGitHubにpushして終了します。

1. 議論が一段落する
2. `/archive` または「Archivistモードでthinking-hub.mdを更新して」と指示
3. AIが `thinking-hub.md` の更新案を提示
4. 内容を確認して承認
5. **変更をcommit & push**（AIが実行）
6. セッションを終了

---

## Web版の特徴

### ✅ メリット
- GitHubと自動連携で変更履歴が残る
- ブラウザからどこでもアクセス可能
- commit/pushが自動化される

### ⚠️ 注意点
- セッションをまたぐとコンテキストが薄れる（自動要約あり）
- 長期プロジェクトは1セッション1テーマを推奨
- モード切替は明示的に指示する必要あり

---

## Tips
* **1セッション1テーマ**: Web版は短時間集中型が最適です
* **thinking-hub.mdは手動編集OK**: 直接GitHubで編集してもOK
* **Next Discussion Candidates**: `thinking-hub.md` の最下部を見て次のテーマを決定
