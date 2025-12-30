# Web Article Brainstorming Space (Web版)

このフォルダは、**Claude Code on the Web** でWeb記事（Blog, Note, Tech記事など）のネタ出し・構成検討を行うためのワークスペースです。

> **注意**: このテンプレートは元々Web-First設計なので、OTW版に最適です。CLI版は `CLI/templates/article-contents-think/` にあります。

## コンセプト
* **Lightweight**: 書籍ほど重厚な管理はせず、1記事1セッション完結を基本とします
* **Web-Optimized**: ブラウザからサクッとアクセスして記事のアイデアを練ります
* **Quick Iteration**: プロンプトテンプレートを使って素早く構成を固めます

## フォルダ構成
* `article-brainstorming-prompt.md`: 記事ネタ出しの「種」となるプロンプトテンプレート
* `topic-ideas.md`: 今後書きたいネタのストック置き場
* `workflow.md`: 作業手順書
* `drafts/`: 完成した記事の下書きを保存する場所（任意）

---

## セッションの始め方 (Start Routine)

### 1. 手動で開始（推奨）

```text
OTW/workspace/[プロジェクト名]/article-brainstorming-prompt.md を読み込んで、
記事のネタ出しと構成を手伝ってください。
テーマ：[ここに書きたいテーマを入れる]
```

### 2. プロンプトテンプレートを活用

`article-brainstorming-prompt.md` を開いて、テーマを編集してからコピペすることもできます。

---

## 運用の流れ

1. **ネタ決め**: `topic-ideas.md` から書きたいテーマを選ぶ（または新規）
2. **ブレスト**: Claude と会話しながら構成を練る
3. **下書き**: 構成が固まったら本文の下書きを作成
4. **保存**: `drafts/` に保存（または直接noteやブログに投稿）
5. **commit**: 変更をGitHubにpush

---

## Web版の特徴

### ✅ メリット
- **最軽量**: 他のテンプレートより気軽に使える
- **1記事完結**: 30分〜1時間で記事の骨子が完成
- **柔軟**: 厳格なモード管理なし、自由な会話スタイル

### ⚠️ 注意点
- 長期的な記録は残らない（その場限りでOK）
- 完成した記事は別途保存推奨
- Git履歴に残すかは自由

---

## Tips
* **気軽に**: 難しく考えず、思いついたらすぐ開始
* **テンプレート活用**: `article-brainstorming-prompt.md` を自分好みにカスタマイズ
* **ストック重視**: 思いついたネタは `topic-ideas.md` にメモ
