---
description: Decision Mode に切り替え（優先度決定・意思決定モード）
---

**Decision Mode** に切り替えます。応答時は `[MODE: Decision]` を宣言してください。

- 思考モードの型（決定の原則・最終決定はユーザーが下す）: グローバルskill **decide**（`~/.claude/skills/decide/SKILL.md`）に従う
- このプロジェクトでの結線:
  - 対象プロジェクトの `ideas-hub.md` と `CLI/workspace/book-priorities.md` の評価結果を材料にする
  - 決定結果は該当ファイル（book-priorities / thinking-hub）に書き戻す
