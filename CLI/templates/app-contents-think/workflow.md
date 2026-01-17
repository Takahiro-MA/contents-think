# AI共同設計ロードマップ（アプリ要件検討版）

この文書は、AI（CLI型LLM）と人間が「議論 → 要件整理 → 設計 → 仕様化」を通じて、ユーザー視点に立った実装可能なアプリ要件を固めるためのプロセス定義書である。

---

## 0. ディレクトリ構造

```text
Apps/プロジェクト名/
├── project_rules.md       # AIへの役割定義と運用ルール（憲法）
├── thinking-hub.md        # 思考の庭（Wiki）。ここを育てていく
├── workflow.md            # この手順書
├── log/                   # 生の会話ログ置き場
│   └── YYYY-MM-DD-session.md
├── notes/                 # トピック別の詳細ノート
│   └── *.md
└── specs/                 # 確定した仕様書
    └── *.md
```

---

## 1. 準備フェーズ

### 1-1. 必須ツール
* **LLM CLI:** Claude Code / Gemini CLI 等（ローカルファイル操作が可能なもの）
* **Editor:** Obsidian（推奨）または VS Code

### 1-2. 基幹ファイルの作成
以下の2ファイルをルートに作成する。

1.  **`project_rules.md`** (AIへの指示書)
    * **AIの4ロール定義:**
        1.  **Sparring Partner:** 反論者・発掘者（要件の曖昧さを突く、深掘りする）
        2.  **Archivist / Gardener:** 記録係・庭師（Hubの更新、整理）
        3.  **Architect:** 設計者（技術選定、アーキテクチャ設計）
        4.  **Spec Writer:** 仕様化担当（要件定義書・仕様書の作成）
    * **更新ルール:** Session後は必ずHubを更新すること等の明文化。

2.  **`thinking-hub.md`** (思考ハブ)
    * 構成は「3. thinking-hubフェーズ」参照。

---

## 2. 発散フェーズ（課題と要件を育てる）

**重要:** 実装を急がず、「何を作るべきか」「なぜ作るのか」の解像度を上げることに集中するフェーズ。

### 2-1. セッション開始手順（儀式）
CLIツール起動時、**必ず以下の2ファイルをコンテキストに読み込ませる。**

**コマンド例:**
```bash
# Claude Code / Gemini CLI 等
> /read project_rules.md
> /read thinking-hub.md
> "Let's start a Sparring Partner session based on these rules. Topic: [今日のテーマ]"
```

### 2-2. セッションの進め方
1.  **ワンテーマ:** 議題を1つだけ投げる（例：「ログイン機能の要件」）
2.  **Sparring Mode:** AIに「厳しいプロダクトマネージャー」として振る舞わせる。
    * 人間：やりたいこと、課題、ユーザーの声を話す。
    * AI：曖昧さを突き、エッジケースを問い、優先度を問う。
3.  **終了と記録:** 議論が煮詰まったら、AIに **Archivist Mode** への切り替えを宣言し、Hubを更新させる。

---

## 3. thinking-hub（Wiki/庭）フェーズ

セッション終了後、AI（Archivist）に以下の構造に従って `thinking-hub.md` を更新させる。

### `thinking-hub.md` の構造定義

```markdown
# Project: <アプリ名> - Thinking Hub

## 1. Core Problem / Vision（解決したい課題・ビジョン）
- 議論を通して明確化した「なぜこのアプリが必要か」
- ユーザーのペインポイント

## 2. Target Users / Personas（ターゲットユーザー）
- 具体的なユーザー像
- 属性、課題、ゴール

## 3. Functional Requirements（機能要件）
- Must Have / Should Have / Could Have / Won't Have（MoSCoW法）

## 4. Non-Functional Requirements（非機能要件）
- パフォーマンス、セキュリティ、スケーラビリティ等

## 5. Technical Decisions（技術的決定事項）
- 決定した技術選定とその理由

## 6. Constraints & Assumptions（制約と前提）
- プロジェクトの制約条件、前提条件

## 7. Open Questions（未解決の問い）
- まだ答えが出ていない重要な問い

## 8. Links to Topic Notes（トピックノート）
- 個別テーマの詳細ノートへのリンク

## 9. Next Discussion Candidates（次の議論候補）
- 次回話すべきテーマ、未解決の論点リスト
```

---

## 4. 設計フェーズ（アーキテクチャを決める）

要件がある程度固まった段階で移行する。

1.  **Mode Change:** AIを **Architect Mode** に切り替える。
2.  **Context:** `thinking-hub.md` と主要な `notes/*.md` を読み込ませる。
3.  **Prompt例:**
    > "このMDファイル群にある要件を満たすアーキテクチャを提案せよ。トレードオフを明示し、複数案を比較すること。"
4.  **Refinement:** 人間がフィードバックし、技術選定を確定させる。
5.  **記録:** 決定事項は `thinking-hub.md` の Technical Decisions に追記。

---

## 5. 仕様化フェーズ（ドキュメントにする）

1.  **Mode Change:** AIを **Spec Writer Mode** に切り替える。
2.  **Mini-Structure:** 書きたい仕様のスコープを伝え、まずアウトラインを作らせる。
3.  **Drafting:** AIに仕様書のドラフトを書かせる。
4.  **Review:** 人間がレビューし、曖昧な箇所を指摘・修正。
5.  **Export:** 確定した仕様は `specs/` ディレクトリに保存。

### 仕様書に含めるべき項目
- 機能概要
- ユーザーストーリー
- 受け入れ条件（Acceptance Criteria）
- 画面遷移・ワイヤーフレーム（必要に応じて）
- API仕様（必要に応じて）
- スコープ外の明示

---

## 6. 振り返りフェーズ（全体の整合性）

1.  **Critique:** AIに「厳しいレビュアー」として全仕様を読ませる。
    * 矛盾、抜け漏れ、実装困難な箇所を指摘させる。
2.  **Gap Check:** 要件と仕様の整合性を確認。
3.  **Priority Review:** 本当に必要な機能だけが含まれているか再確認。

---

## 7. 次のステップへ

要件・仕様が固まったら、実装フェーズへ移行する。
このワークスペースで固めた内容を基に、実際のコーディングプロジェクトを開始する。

**このフォルダの成果物:**
- 明確な問題定義とビジョン
- 優先度付けされた機能要件
- 技術選定とその根拠
- 実装可能な仕様書群
