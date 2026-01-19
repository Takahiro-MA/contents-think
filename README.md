# Contents Think - AI協働コンテンツ制作ワークスペース

LLM（Claude Code / Gemini CLI / Claude on the Web）を活用したコンテンツ制作のためのワークスペース集です。

## リポジトリ構成

```
contents-think/
├── CLI/                    # CLI版（Claude Code CLI / Gemini CLI）
│   ├── templates/          # CLI版雛形
│   └── workspace/          # CLI版作業エリア
│
├── OTW/                    # On The Web版（Claude Code on the Web）
│   ├── templates/          # Web版雛形（最適化済み）
│   └── workspace/          # Web版作業エリア
│
└── .claude/
    └── commands/           # カスタムスラッシュコマンド（OTW版用）

~/.claude/skills/               # グローバルSkills（CLI版用・別途セットアップ）
├── sparring/SKILL.md          # 議論・壁打ち
├── brainstorm/SKILL.md        # アイデア発散
├── architect/SKILL.md         # 設計・技術選定
├── evaluate/SKILL.md          # アイデア評価
├── spec-writer/SKILL.md       # 仕様書作成
└── decide/SKILL.md            # 意思決定
```

## 2つのバージョン

### CLI版（CLI/）
**対象**: Claude Code CLI / Gemini CLI ユーザー

- ターミナルから起動
- 長時間セッションに最適
- ローカルファイルを継続的に更新
- **Skills対応**: 自然言語で呼び出せる専門スキル（後述）
- 詳細は `CLI/templates/[テンプレート名]/README.md` を参照

### OTW版（OTW/）
**対象**: Claude Code on the Web ユーザー

- ブラウザから起動
- 短時間集中セッションに最適
- GitHubと自動連携
- カスタムスラッシュコマンド対応
- 詳細は `OTW/templates/[テンプレート名]/README.md` を参照

## 利用可能なテンプレート

### アプリ開発系
| テンプレート | 用途 | CLI版 | OTW版 |
|:---|:---|:---:|:---:|
| `app-ideas-think` | アプリアイデア発想 | ✅ | ✅ |
| `app-contents-think` | アプリ要件検討 | ✅ | ✅ |

### 書籍執筆系
| テンプレート | 用途 | CLI版 | OTW版 |
|:---|:---|:---:|:---:|
| `book-ideas-think` | 書籍アイデア発想 | ✅ | ✅ |
| `book-contents-think` | 書籍内容検討 | ✅ | ✅ |

### 記事執筆系
| テンプレート | 用途 | CLI版 | OTW版 |
|:---|:---|:---:|:---:|
| `article-contents-think` | Web記事作成 | ✅ | ✅ |

## クイックスタート

### CLI版を使う場合

```bash
# 1. 雛形をコピー
cd CLI/workspace
cp -r ../templates/app-contents-think ./my-project

# 2. プロジェクトフォルダに移動
cd my-project

# 3. CLI起動
claude  # または gemini-cli

# 4. セッション開始
/read project_rules.md thinking-hub.md

# 5. Skillsを自然言語で呼び出し
「壁打ちしたい」「アイデア出しして」「設計を考えて」など
```

### OTW版を使う場合

```bash
# 1. GitHubリポジトリをブラウザで開く
# 2. Claude Code on the Web で開く

# 3. プロジェクト作成（初回のみ）
# OTW/templates/ から雛形をコピーして OTW/workspace/ に配置

# 4. カスタムコマンドで開始
/app-start    # アプリ要件検討
/book-start   # 書籍執筆
/brainstorm   # アイデア発想
```

## カスタムスラッシュコマンド（OTW版）

| コマンド | 用途 |
|:---|:---|
| `/app-start` | アプリ要件検討プロジェクト開始 |
| `/book-start` | 書籍執筆プロジェクト開始 |
| `/sparring` | 議論・壁打ちモード |
| `/architect` | 設計・技術選定モード |
| `/brainstorm` | アイデア発散モード |
| `/evaluate` | アイデア評価モード |
| `/archive` | 議論内容を保存 |

## Skills（CLI版）

CLI版では、`~/.claude/skills/` にインストールされたSkillsを自然言語で呼び出せます。
Claudeが文脈から適切なSkillを自動判断してロードします。

| Skill | 呼び出しワード例 | 用途 |
|:---|:---|:---|
| `sparring` | 「壁打ち」「議論しよう」「批判的に見て」 | 建設的な批判と提案 |
| `brainstorm` | 「アイデア出し」「発散」「ブレスト」 | アイデアを自由に発散 |
| `architect` | 「設計」「アーキテクチャ」「技術選定」 | 技術的な設計検討 |
| `evaluate` | 「評価して」「比較して」「分析して」 | 選択肢の客観的評価 |
| `spec-writer` | 「仕様書」「要件定義」「まとめて」 | 構造化されたドキュメント作成 |
| `decide` | 「決める」「優先度」「意思決定」 | 最終的な意思決定支援 |

### Skillsのセットアップ

Skillsは `~/.claude/skills/` に配置することで、このマシン上の全プロジェクトで利用可能になります。

```bash
# セットアップ済みかの確認
ls ~/.claude/skills/
```

## どちらを使うべきか？

### CLI版が向いている場合
- 長時間（1時間以上）のセッションを想定
- 同じプロジェクトに何度も戻ってくる
- ローカル環境でファイルを直接編集したい
- ターミナル操作が快適
- **Skillsを活用したい**（自然言語で専門スキルを呼び出し）

### OTW版が向いている場合
- 短時間（30分程度）のセッションが中心
- ブラウザからアクセスしたい
- GitHubと自動連携したい
- カスタムコマンドで効率化したい

### 機能比較

| 機能 | CLI版 | OTW版 |
|:---|:---:|:---:|
| Skills（自動ロード） | ✅ | - |
| Slash Commands | ✅ | ✅ |
| ローカルファイル編集 | ✅ | - |
| GitHub自動連携 | - | ✅ |

## ライセンス

このリポジトリは個人利用を目的としています。

## 貢献

個人プロジェクトのため、外部からのPRは受け付けていません。
