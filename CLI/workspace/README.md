# CLI Workspace

このフォルダは、CLI版（Claude Code CLI / Gemini CLI）で実際にプロジェクトを進める作業エリアです。

## 使い方

1. `../templates/` から必要な雛形フォルダをコピー
2. プロジェクト名にリネーム
3. ターミナルでそのフォルダに移動
4. CLI ツールを起動してセッション開始

## 例

```bash
# app-contents-think の雛形をコピー
cp -r ../templates/app-contents-think ./my-todo-app

# プロジェクトフォルダに移動
cd my-todo-app

# CLI ツール起動
claude-code  # または gemini-cli

# セッション開始
/read project_rules.md thinking-hub.md
```

## 注意

- このフォルダ内のプロジェクトは `.gitignore` で管理されています
- 成果物は別途適切な場所にcommitしてください
- 雛形は `templates/` から取得し、このフォルダ内で作業してください
