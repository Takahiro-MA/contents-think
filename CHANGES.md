# CHANGES.md — 再設計（redesign-2026-07）の変更記録

計画: `/home/takahiroma/REDESIGN_PLAN.md` §5.3（Phase 4）。ブランチ: `redesign-2026-07`。

## 2026-07-07 Phase 4 実施内容

### CLAUDE.md
- 「全体地図」（3リポジトリの役割・台帳の正典=book-status.md）と「執筆方式の2系統」（A系統/B系統の定義。docs/21準拠とテンプレ禁止の矛盾を適用対象の違いとして解消）を追加
- thinking-hub「全16セクションが正」を明記、「コマンドの責務」節を追加
- H1を「田中さんシリーズ 執筆プロジェクト」→「Kindle執筆システム」に変更（藤井さんシリーズ等も対象のため）
- 文体ルール・章テンプレ・粒度要件・品質チェックリスト・ワークフロー・レビュー体制は**無変更**

### .claude/commands/
- モード系6本（sparring/brainstorm/evaluate/decide/architect/spec）をグローバルskills参照のラッパーに書き換え（型の正典を一本化。二重定義ドリフト防止）。旧本文の要点（Context Absolutism・修正策なき否定の禁止等）は結線側に保持。archive.md はプロジェクト固有のため無変更
- 実行系5本（write-chapter/review-book/review-thinkinghub/fix-review/check-consistency）に**完了条件**を追記（本文プロセスは無変更）
- book-start/app-start: 参照先を `OTW/workspace/` → `CLI/workspace/` に修正（**発見: 実書籍はCLI配下にありOTW/workspaceは空**）。project_rulesが無いA系統向けのフォールバック注記を追加

### テンプレート
- `CLI/templates/book-contents-think/thinking-hub.md`: 8セクション→**16セクション**に拡張（雛形元=最新出版のkiro-cli実例。§11に粒度要件を埋め込み）
- `CLI/workspace/book-writing-framework.md`: 「必須の10セクション」→16に整合（行11-16を追加）
- book/app両テンプレの project_rules.md: BOOT BLOCKのモード列挙を本文のモード数に一致（Analyst追加）
- `OTW/templates/` → `OTW/templates_archive/` に移動し、ポインタREADMEを設置（2026-02から未使用のCLI版コピーだったため）

### workspace管理ファイル
- `book-status.md`: 「執筆方式の系統（A/B）」節を追加。**計画からの変更**: 各テーブルへの列追加ではなく専用節にした（複数テーブル×20行超の改変はミス混入リスクが高いため。判別不能なX系は「未分類」と明記）
- `shared-characters.md`: 重複見出し「## 10. Book 9」→「## 10.0. Book 9」に変更。**計画からの変更**: 後続の連番ずらしはせず最小変更にした（10A/10Bは配下小見出しとbook-statusから参照されており波及するため）
- `book-priorities.md`: 冒頭にスナップショット注記（2026-02-13時点）
- `.claude/settings.local.json`: 一回性コマンド22件を削除、恒常20件のみ残す

### 削除していないもの
- 各書籍の実thinking-hub・原稿・review-log・kindle2の章ファイル（すべて無変更）
- B系統の project_rules 実体（04_tdd-book / X3_LLM_in_office）
