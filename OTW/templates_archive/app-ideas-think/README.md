# App Ideas Brainstorming: Operation Manual (Web版)

このフォルダは、**Claude Code on the Web** との「次に何のアプリを作るか」を決めるためのワークスペースです。

> **注意**: これはWeb版に最適化されたテンプレートです。CLI版は `CLI/templates/app-ideas-think/` にあります。

**アイデアが決まったら**: `OTW/workspace/` に `app-contents-think` テンプレートをコピーして要件を深掘りしてください。

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
Brainstorm Mode で開始してください。アイデアを自由に発散させましょう。
```

---

## 運用コマンド (Operational Commands)

| コマンド | 動作 | 使うタイミング |
| :--- | :--- | :--- |
| `/brainstorm` | **Brainstorm Mode** へ切替 | アイデアを発散させたいとき |
| `/evaluate` | **Evaluator Mode** へ切替 | アイデアを評価・比較したいとき |
| `/decide` | **Decision Mode** へ切替 | 優先度を決めて「次にやるもの」を選ぶとき |
| `/archive` | **Archivist Mode** へ切替 | セッション終了時、hubを更新するとき |

> **Note**: カスタムコマンドは `.claude/commands/` で定義されています。

---

## 終了時の作法 (End Routine)

Web版では、変更をGitHubにpushして終了します。

1. `/archive` または「Archivistモードでideas-hub.mdを更新して」と指示
2. AIが `ideas-hub.md` の更新案を提示
3. 内容を確認して承認
4. **変更をcommit & push**（AIが実行）
5. 次のステップへ：決まったアイデアは `OTW/workspace/` に `app-contents-think` をコピー

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
* **質より量**: 最初は判断せずに出し切る
* **発散と収束を分ける**: Brainstorm → Evaluate → Decide の順で
* **決まったら即実行**: `app-contents-think` で要件を深掘り
