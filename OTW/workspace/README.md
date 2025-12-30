# OTW (On The Web) Workspace

このフォルダは、**Claude Code on the Web** で実際にプロジェクトを進める作業エリアです。

## 使い方

### 1. プロジェクトの作成

```bash
# GitHubリポジトリをブラウザで開く
# OTW/templates/ から適切な雛形をコピー

# 例：アプリ要件検討プロジェクトを開始
cp -r OTW/templates/app-contents-think OTW/workspace/my-todo-app
```

### 2. セッションの開始

プロジェクトフォルダができたら、カスタムコマンドでセッションを開始：

```bash
/app-start    # アプリ要件検討の場合
/book-start   # 書籍執筆の場合
```

### 3. 作業の進め方

- **1セッション1テーマ**: 短時間集中型が最適
- **モード切替**: `/sparring`, `/architect`, `/archive` などを活用
- **終了時**: `/archive` で変更を保存してcommit & push

## 利用可能なテンプレート

| テンプレート | 用途 | 開始コマンド |
|:---|:---|:---|
| `app-contents-think` | アプリ要件検討 | `/app-start` |
| `app-ideas-think` | アプリアイデア発想 | `/brainstorm` |
| `book-contents-think` | 書籍内容検討 | `/book-start` |
| `book-ideas-think` | 書籍アイデア発想 | `/brainstorm` |
| `article-contents-think` | Web記事作成 | （手動起動） |

## Web版の特徴

### ✅ メリット
- GitHubと自動連携
- どこからでもアクセス可能
- 変更履歴が自動で残る

### ⚠️ 注意点
- セッション間のコンテキストは薄れる
- 長期プロジェクトは複数セッションに分割
- カスタムコマンドの活用が鍵

## Tips

- **テンプレートのカスタマイズ**: プロジェクトに合わせて `project_rules.md` を編集
- **GitHub連携**: 各セッションの成果はGitに自動commit
- **複数プロジェクト**: 同時に複数のプロジェクトを進行可能
