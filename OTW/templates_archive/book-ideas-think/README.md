# Book Ideas Brainstorming: Operation Manual (Web版)

このフォルダは、**Claude Code on the Web** との「次に何の本を書くか」を決めるためのワークスペースです。

> **注意**: これはWeb版に最適化されたテンプレートです。CLI版は `CLI/templates/book-ideas-think/` にあります。

**テーマが決まったら**: `OTW/workspace/` に `book-contents-think` テンプレートをコピーして内容を深掘りしてください。

## 必須ファイル構成

* `project_rules.md`: AIへの役割定義・運用ルール
* `ideas-hub.md`: アイデアの集積地
* `workflow.md`: 全体の流れ

---

## セッションの始め方 (Start Routine)

Web版では、カスタムコマンドまたは手動でセッションを開始します。

### 1. カスタムコマンドで開始

```bash
/brainstorm
```

### 2. 手動で開始する場合

```text
OTW/workspace/[プロジェクト名]/project_rules.md と ideas-hub.md を読み込んで、
Brainstorm Mode で開始してください。書きたい本のアイデアを自由に発散させましょう。
```

---

## 運用コマンド (Operational Commands)

| コマンド | 動作 | 使うタイミング |
| :--- | :--- | :--- |
| `/brainstorm` | **Brainstorm Mode** へ切替 | アイデアを発散させたいとき |
| `/evaluate` | **Evaluator Mode** へ切替 | アイデアを評価・比較したいとき |
| `/decide` | **Decision Mode** へ切替 | 優先度を決めて「次に書くもの」を選ぶとき |
| `/archive` | **Archivist Mode** へ切替 | セッション終了時、hubを更新するとき |

> **Note**: カスタムコマンドは `.claude/commands/` で定義されています。

---

## 終了時の作法 (End Routine)

Web版では、変更をGitHubにpushして終了します。

1. `/archive` または「Archivistモードでideas-hub.mdを更新して」と指示
2. AIが `ideas-hub.md` の更新案を提示
3. 内容を確認して承認
4. **変更をcommit & push**（AIが実行）
5. 次のステップへ：決まったテーマは `OTW/workspace/` に `book-contents-think` をコピー

---

## Web版の特徴

### ✅ メリット
- GitHubと自動連携でアイデアが蓄積される
- ブラウザからどこでもアクセス可能
- 短時間でサクッとアイデア出し

### ⚠️ 注意点
- 1セッション = 1回のアイデア出しを推奨
- 評価フェーズは別セッションでもOK
- 長時間の議論より、短時間で集中

---

## Tips
* **質より量**: 書きたいことを最初は判断せずに出し切る
* **「書きたいか」優先**: 「自分に書けるか」は後で考える
* **発散と収束を分ける**: Brainstorm → Evaluate → Decide の順で
* **決まったら即深掘り**: `book-contents-think` でテーマを展開
