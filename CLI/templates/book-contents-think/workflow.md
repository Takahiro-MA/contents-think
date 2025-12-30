 # 📘 AI共著アドバンス手法ロードマップ（決定版）

この文書は、AI（CLI型LLM）と人間が「議論 → 思考の集積 → 編集 → 執筆」を通じて、平均点に陥らない独自性の高い書籍を共著するためのプロセス定義書である。

---

## 0. ディレクトリ構造

```text
Books/プロジェクト名/
├── project_rules.md       # AIへの役割定義と運用ルール（憲法）
├── thinking-hub.md        # 思考の庭（Wiki）。ここを育てていく
├── workflow.md            # この手順書
├── log/                   # 生の会話ログ置き場
│   └── YYYY-MM-DD-session.md
└── notes/                 # トピック別の詳細ノート
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
    * **AIの3ロール定義:**
        1.  **Sparring Partner:** 反論者・発掘者（合意しない、掘り下げる）
        2.  **Archivist / Gardener:** 記録係・庭師（Hubの更新、整理）
        3.  **Editor / Author Assistant:** 編集者・著者補助（構成案、執筆）
    * **更新ルール:** Session後は必ずHubを更新すること等の明文化。

2.  **`thinking-hub.md`** (思考ハブ)
    * 構成は「3. thinking-hubフェーズ」参照。

---

## 2. 思考フェーズ（議論を育てる）

**重要:** 書籍化を急がず、思考の解像度を上げることに集中するフェーズ。

### 2-1. セッション開始手順（儀式）
CLIツール起動時、**必ず以下の2ファイルをコンテキストに読み込ませる。** これを忘れると文脈が断絶する。

**コマンド例（イメージ）:**
```bash
# Claude Code / Gemini CLI 等
> /read project_rules.md
> /read thinking-hub.md
> "Let's start a Sparring Partner session based on these rules. Topic: [今日のテーマ]"
```

### 2-2. セッションの進め方
1.  **ワンテーマ:** 議題を1つだけ投げる。
2.  **Sparring Mode:** AIに「意地悪な編集者」「壁打ち相手」として振る舞わせる。
    * 人間：体験、感情、違和感を遠慮なく話す。
    * AI：安易にまとめず、矛盾を突き、深掘りする。
3.  **終了と記録:** 議論が煮詰まったら、AIに **Archivist Mode** への切り替えを宣言し、以下を実行させる。

---

## 3. thinking-hub（Wiki/庭）フェーズ

セッション終了後、AI（Archivist）に以下の構造に従って `thinking-hub.md` を更新させる。

### `thinking-hub.md` の構造定義

```markdown
# Project: <書籍名候補> - Thinking Hub

## 1. Core Thesis（核となる仮説）
- 議論を通して強度が増した「揺るがない主張」
- 日付や出典ログへのリンクを含める

## 2. Floating Ideas（未整理アイデア）
- 面白いがまだ論理が通っていないもの
- 保留中の仮説

## 3. Killer Phrases & Metaphors（キラーフレーズ）
- タイトル候補、章タイトルに使えそうな強い言葉
- 独自の比喩表現

## 4. Counter Arguments（反論と応答）
- 想定される読者からの反論
- それに対する論理的・感情的な回答

## 5. Structure Seeds（構成のタネ）
- 「章になりそう」なアイデアの塊
- まだ目次としては確定させない

## 6. Links to Topic Notes（トピックノート）
- 個別テーマの詳細ノートへのリンク一覧 ([[notes/xxx]])

## 7. Recent Raw Logs（直近ログ）
- log/YYYY-MM-DD-session.md へのリンクと3行要約

## 8. Next Discussion Candidates（次の議論候補）
- 次回話すべきテーマ、未解決の論点リスト
- **次回起動時はここを見てテーマを決める**
```

---

## 4. 編集フェーズ（構成を作る）

ネタが十分に育った（Core Thesisが固まった）段階で移行する。

1.  **Mode Change:** AIを **Editor Mode** に切り替える。
2.  **Context:** `thinking-hub.md` と主要な `notes/*.md` を読み込ませる。
3.  **Prompt:**
    > "このMDファイル群にある情報**のみ**を根拠に、絶対に伝えるべきCore Thesisを3つ選び、それを軸にした章立て案を作成せよ。一般的なビジネス書のテンプレートは使用禁止。"
4.  **Refinement:** 人間が「感情ベース」でフィードバックし、構成を確定させる。

---

## 5. 執筆フェーズ（章ごとに書く）

1.  **Mini-Structure:** 書きたい章のタイトルを伝え、まず章内部の骨子（ミニ構成）を作らせる。
2.  **Drafting:** AIに素案（Draft）を書かせる。
3.  **Writing:** 人間が介入する。
    * 体験談を差し込む。
    * 「自分の口調」に書き換える。
    * AI特有の「まとめ感」を削除する。
4.  **Feedback Loop:** 完成した章から生まれた新しいアイデアやフレーズを、`thinking-hub.md` に逆流（更新）させる。

---

## 6. 仕上げフェーズ（全体の一貫性）

1.  **Critique:** AIに「意地悪な編集者」として全原稿を読ませる。
    * 矛盾、論理の飛躍、退屈な箇所を指摘させる。
2.  **Tone Check:** 文体や用語の統一を行う。
3.  **Hook & Landing:** `Killer Phrases` リストを活用し、「はじめに」と「おわりに」を最強の強度で仕上げる。