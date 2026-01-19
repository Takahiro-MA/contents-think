# AI Co-Authoring Project: Operation Manual
 
このフォルダは、CLI型LLM（Claude Code / Gemini CLI）との共著プロジェクト用のワークスペースです。

## 必須ファイル構成
開始前に以下のファイルが存在することを確認してください。

* `project_rules.md`: AIへの役割定義・運用ルール（憲法）
* `thinking-hub.md`: 思考の庭（Wiki）
* `workflow.md`: 全体のロードマップ

## Skills（推奨）

`~/.claude/skills/` にSkillsがセットアップされている場合、自然言語で専門スキルを呼び出せます。

| 呼び出しワード | Skill | 説明 |
|:---|:---|:---|
| 「壁打ちしよう」「批判的に見て」 | sparring | 建設的な批判と提案 |
| 「アイデア出して」「ブレスト」 | brainstorm | アイデア発散 |
| 「仕様書にまとめて」 | spec-writer | ドキュメント化 |

Skillsは文脈に応じてClaudeが自動判断してロードします。

---

## セッションの始め方 (Start Routine)

ターミナルでこのディレクトリに移動し、ツール（Claude Code等）を起動した後、**必ず以下の手順を実行してください。**

### 1. コンテキストの読み込み
まず、ルールと現状をAIのメモリに入れます。以下のコマンドを入力：

```bash
/read project_rules.md thinking-hub.md
```

### 2. ブートアップ宣言（コピペ用）
読み込み完了後、以下のプロンプトをコピペして送信し、モードを確定させます。

```text
project_rules.md の BOOT BLOCK に従い、セッションを開始してください。
今日のテーマは「[ここに今日のテーマを入れる]」です。
[Mode: Sparring] でお願いします。
```

---

## 🕹️ 運用コマンド (Operational Commands)

会話中に使用する主な制御コマンドです（`project_rules.md` で定義済み）。

| コマンド | 動作 | 使うタイミング |
| :--- | :--- | :--- |
| `/sparring` | **Sparring Mode** へ切替 | 議論・壁打ちをしたいとき（デフォルト） |
| `/archive` | **Archivist Mode** へ切替 | 議論終了後、`thinking-hub.md` を更新して終わるとき |
| `/edit` | **Editor Mode** へ切替 | まとまった章の構成案や本文を書かせるとき |
| `/status` | ステータス確認 | 現在のモードや読み込み済みファイルを確認したいとき |

---

## 📝 終了時の作法 (End Routine)

セッションを終えるときは、必ず **Archivist Mode** でログを残してから終了してください。

1.  議論が一段落する。
2.  コマンド `/archive` を入力（または「Archivistモードでハブを更新して」と指示）。
3.  AIが `thinking-hub.md` の更新案と `log/` ファイルの作成案を提示。
4.  内容を確認して承認（Y）。
5.  更新完了を確認してツールを終了（`exit` / `Ctrl+C`）。

---

## 💡 Tips
* **`thinking-hub.md` は手動で修正してもOKです。** 人間の直感で「ここは違う」と思った箇所は、セッション外で直接エディタで修正・削除してください。
* 久しぶりに再開する場合は、`thinking-hub.md` の最下部にある **「8. Next Discussion Candidates」** を見てテーマを決めるとスムーズです。