# App Ideas Brainstorming: Operation Manual

このフォルダは、CLI型LLM（Claude Code / Gemini CLI）との「次に何のアプリを作るか」を決めるためのワークスペースです。

**注意:** ここは「どのアプリを作るか」を決める場所です。決まったら `app-contents-think` に移動して要件を深掘りしてください。

## 必須ファイル構成

* `project_rules.md`: AIへの役割定義・運用ルール
* `ideas-hub.md`: アイデアの集積地
* `workflow.md`: 全体の流れ

## Skills（推奨）

`~/.claude/skills/` にSkillsがセットアップされている場合、自然言語で専門スキルを呼び出せます。

| 呼び出しワード | Skill | 説明 |
|:---|:---|:---|
| 「アイデア出して」「ブレスト」 | brainstorm | アイデア発散 |
| 「評価して」「比較して」 | evaluate | 選択肢の評価 |
| 「決めよう」「優先度を」 | decide | 意思決定支援 |

Skillsは文脈に応じてClaudeが自動判断してロードします。

---

## セッションの始め方 (Start Routine)

```bash
/read project_rules.md ideas-hub.md
```

```text
project_rules.md の BOOT BLOCK に従い、セッションを開始してください。
[Mode: Brainstorm] でお願いします。
```

---

## 運用コマンド (Operational Commands)

| コマンド | 動作 | 使うタイミング |
| :--- | :--- | :--- |
| `/brainstorm` | **Brainstorm Mode** へ切替 | アイデアを発散させたいとき（デフォルト） |
| `/evaluate` | **Evaluator Mode** へ切替 | アイデアを評価・比較したいとき |
| `/decide` | **Decision Mode** へ切替 | 優先度を決めて「次にやるもの」を選ぶとき |
| `/archive` | **Archivist Mode** へ切替 | セッション終了時、hubを更新するとき |
| `/status` | ステータス確認 | 現在のモードや進捗を確認したいとき |

---

## 終了時の作法 (End Routine)

1. `/archive` でhubを更新
2. 「次にやるアプリ」が決まったら、`app-contents-think` にコピーして深掘りを開始

---

## Tips
* アイデアは質より量。最初は判断せずに出し切る。
* 評価は後から。発散と収束を分けるのがコツ。
* 決まったアイデアは `app-contents-think` に持っていく。
