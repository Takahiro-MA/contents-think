# Web Article Brainstorming Space

このフォルダは、Web記事（Blog, Note, Tech記事など）のネタ出し・構成検討を行うためのワークスペースです。

## コンセプト
*   **Lightweight**: 書籍ほど重厚な管理はせず、1記事1セッション完結を基本とします。
*   **Web-First**: CLIではなく、Web版のChatGPT/Gemini/Claude等と会話して内容を詰めるスタイルです。
*   **Copy-Paste**: プロンプトのテンプレートをコピペして会話を開始します。

## Skills（CLI版で使う場合）

Claude Code CLIを使う場合、`~/.claude/skills/` にSkillsがセットアップされていれば、自然言語で専門スキルを呼び出せます。

| 呼び出しワード | Skill | 説明 |
|:---|:---|:---|
| 「アイデア出して」「ブレスト」 | brainstorm | アイデア発散 |
| 「壁打ちしよう」 | sparring | 建設的な批判と提案 |
| 「まとめて」 | spec-writer | ドキュメント化 |

## フォルダ構成
*   `article-brainstorming-prompt.md`: Web LLMに投げるための「種」となるプロンプトファイル。毎回これを編集してコピペします。
*   `topic-ideas.md`: 今後書きたいネタのストック置き場。
*   `workflow.md`: 作業手順書。
*   `drafts/`: 完成した記事の下書きを保存する場所。
