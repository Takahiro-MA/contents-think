---
description: Spec Writer Mode に切り替え（仕様書・要件定義書作成モード）
---

**Spec Writer Mode** に切り替えます。応答時は `[MODE: Spec Writer]` を宣言してください。

- 思考モードの型（構造化・曖昧さの排除）: グローバルskill **spec-writer**（`~/.claude/skills/spec-writer/SKILL.md`）に従う
- このプロジェクトでの結線:
  - 書籍の仕様書は thinking-hub 形式（全16セクション。雛形 `CLI/templates/book-contents-think/thinking-hub.md`）で書く
  - セクション11（各章シーン分解）は `CLAUDE.md` の粒度要件（詳細型・5項目・各章4〜6シーン）に従う
