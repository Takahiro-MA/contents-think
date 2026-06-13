# 書籍ステータス一覧

> 全書籍のthinking-hub（執筆仕様書）と執筆状態を一覧管理するファイル。
> 状態が変わったら都度更新すること。

Last Updated: 2026-06-13

---

## ステータス凡例

| Phase | 意味 |
|-------|------|
| Phase 0 | テーマ検証（GO / NO-GO / 保留） |
| Phase 1 | thinking-hub作成 |
| Phase 1R | thinking-hub Claudeレビュー＆修正反映（/review-thinkinghub） |
| Phase 1A | thinking-hub 著者レビュー＆承認（著者が通読し方向性・設定を最終確認） |
| Phase 2 | 初稿の並列執筆 |
| Phase 3 | 3視点Claudeレビュー（/review-book） |
| Phase 4 | レビュー修正反映（/fix-review） |
| Phase 5 | 著者レビュー＆対話的修正 |
| Phase 6 | 最終バランスチェック＆完成 |
| Published | Kindle出版済み |

---

## 田中さんシリーズ

### 出版済み

| # | テーマ | thinking-hub | 出版先 | 備考 |
|---|--------|-------------|-------|------|
| 1 | Git/GitHub | — | `../kindle2/01_git-github-book/epub/` | Published。thinking-hubフレームワーク導入前 |
| 2 | Docker | — | `../kindle2/02_docker-book/epub/` | Published。thinking-hubフレームワーク導入前 |
| 3 | アジャイル | — | `../kindle2/03_agile-book/epub/` | Published。thinking-hubフレームワーク導入前 |
| 4 | TDD | — | `../kindle2/04_tdd-book/epub/` | Published。レガシーコード本の前日譚。review-log.mdあり |
| 5 | Claude Code | `claude-code/` | `../kindle2/05_claudecode/epub/` | Published |
| 6 | Linux/CLI | `linux-cli/` | `../kindle2/07_linux-cli-book/epub/` | Published。review-log.mdあり |
| 7 | Codex CLI | `codex-cli/` | `../kindle2/09_codex-cli-book/epub/` | Published。review-log.mdあり。付録あり |

### 執筆進行中

| # | テーマ | thinking-hub | 章数 | Phase | 通過済み | 出版先 | 備考 |
|---|--------|-------------|------|-------|---------|-------|------|
| 7 | Obsidian/PKM | `obsidian/` | 8 | Phase 6待ち | 1→1R→2→3→4→5→**6待ち** | `../kindle2/08_obsidian-book/epub/` | 著者レビュー24件+整合性チェック指摘を全件修正済み。付録追加。最終バランスチェック待ち |
| 14 | Kiro CLI | `kiro-cli/` | 8 | Phase 5待ち | 1→1R→1A→2→3→4→**5待ち**（整合性チェック済み） | `../kindle2/10_kiro-cli-book/epub/` | 神谷PdMとの自治体プロダクト立て直し物語。Phase 3（3視点レビュー）→Phase 4（A級8件・B級8件反映：Hooks JSON公式準拠化・料金表・認証手順追加・MCP/Steeringパス修正等）→整合性チェック（5項目問題なし）完了。全12ファイル約13.6万字。著者通読（Phase 5）待ち |

### thinking-hub作成済み（初稿未着手）

| # | テーマ | thinking-hub | 章数 | Phase | 通過済み | 備考 |
|---|--------|-------------|------|-------|---------|------|
| 8 | 睡眠改善 | `sleep-improvement/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | 著者レビュー後に執筆可能 |
| 9 | デジタルデトックス | `digital-detox/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | 著者レビュー後に執筆可能 |
| 10 | SQL | `sql/` | 9 | Phase 1A待ち | 1→1R→**1A待ち** | 著者レビュー後に執筆可能 |
| 11 | レガシーコード改善 | `legacy-code/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | TDD本の続編的位置づけ |
| ~~12~~ | ~~Codex CLI~~ | — | — | Published | — | 出版済みセクションに移動 |
| 13 | キャリアピボット | `career-pivot/` | 10 | Phase 1A待ち（保留） | 1→1R→**1A待ち** | 主人公が中村さん。著者の熱量確認待ち |
| ~~14~~ | ~~Kiro CLI~~ | — | — | 執筆進行中へ | — | 執筆進行中セクションに移動（Phase 2完了） |
| — | AI仕事術 | `ai-work-style/` | — | NO-GO | — | Claude Code本と重複。出版予定なし |

### フレームワーク導入前の初稿（thinking-hubなし）

| # | テーマ | 出版先 | ファイル数 | 行数 | 主人公 | 備考 |
|---|--------|-------|-----------|------|--------|------|
| X4 | ゆるプログラミング入門 | `../kindle2/X4_yuru-programming-book/epub/` | 15 | 5,602 | 田中さん（営業部3年→プログラミング学習） | 2週間の学習物語。Phase未定 |
| X5 | タイムマネジメント | `../kindle2/X5_time-management-book/epub/` | 12 | 3,190 | 田中さん（残業→定時退社へ） | 山田さんがメンター。Phase未定 |
| X6 | 副業開始物語 | `../kindle2/X6_side-business-book/epub/` | 12 | 2,900 | 田中さん（32歳、月収28万） | 月5万副収入。ブログ/Kindle/個人開発。Phase未定 |
| X7 | ウォーターフォール開発 | `../kindle2/X7_waterfall-book/epub/` | 12 | 2,558 | 田中さん（SIer転職） | アジャイル→WF体験。Phase未定 |

---

## 藤井さんシリーズ

| # | テーマ | thinking-hub | 章数 | Phase | 通過済み | 出版先 | 備考 |
|---|--------|-------------|------|-------|---------|-------|------|
| 1 | 断酒 | `sobriety/` | 8 | Phase 5待ち | 1→1R→2→3→4→**5待ち** | `../kindle2/06_sobriety-book/epub/` | Claudeレビュー43件中12件修正済み。著者レビュー待ち |
| 2 | 食事改善 | `food-improvement/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | — | 著者レビュー後に執筆可能 |
| 3 | ストレスマネジメント | `stress-management/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | — | 著者レビュー後に執筆可能 |

---

## ゲーム理論シリーズ

| # | テーマ | ディレクトリ | 章数 | Phase | 備考 |
|---|--------|------------|------|-------|------|
| A | ビジネスパーソン向けゲーム理論入門 | `game-theory/` | — | Phase 0 | 広い市場向け。先行出版予定 |
| B | IT現場の構造分析 | `game-theory/` | — | Phase 0 | 深い市場向け。Book Aからの送客 |

---

## その他（非シリーズ・企画段階・サンプル）

| ディレクトリ | テーマ | 状態 | 備考 |
|-------------|--------|------|------|
| `../kindle2/X1_ruby-on-rails-book/` | Ruby on Rails入門 | 初稿あり（非物語型） | book1+book2の2構成。田中さんシリーズではない |
| `../kindle2/X2_fishing-manga/` | 釣りマンガ | プロット段階 | 主人公: 潮見なみ（大学2年）。キャラ設定+序章プロットのみ |
| `../kindle2/X3_LLM_in_office/` | 企業の生成AI活用 | thinking-hubあり | 理論書型（非物語）。セッションログ4件あり |
| `../kindle2/XX_sample-books/` | サンプルテンプレート | 参考用 | Go言語(3,891行)、Spring Boot(5,015行)のサンプル書籍 |

---

## 関連ファイル

| ファイル | 用途 |
|---------|------|
| `shared-characters.md` | 全書籍共通のキャラクター設定マスター |
| `book-writing-framework.md` | 執筆ワークフロー（Phase 0〜6）の定義 |
| `book-priorities.md` | テーマ検証（Phase 0）の結果蓄積 |
| `book-status.md` | 本ファイル。全書籍の状態管理 |

---

## 統計

### シリーズ別
- 田中さんシリーズ: 出版済み6冊 + 執筆中2冊 + hub済み5冊（うちNO-GO 1, 保留1） + 旧作4冊
- 藤井さんシリーズ: 初稿済み1冊 + hub済み2冊
- ゲーム理論シリーズ: 企画段階2冊
- その他: 4件（Ruby, 釣りマンガ, LLM理論書, サンプル）
- アイデア段階（フォルダのみ・status未登録）: 4件（ai-driven-org, gluten-free, libre-diet, low-fat-diet）

### Phase別
- Published: 7冊
- Phase 6待ち（最終バランスチェック待ち）: 1冊（Obsidian）
- Phase 5待ち（著者通読待ち、整合性チェック済み）: 1冊（Kiro CLI）
- Phase 3待ち（原稿 Claudeレビュー待ち）: 1冊（断酒）
- Phase 1A待ち（thinking-hub 著者レビュー待ち）: 6冊
- Phase 0（企画段階）: 2冊
- NO-GO: 1冊
- Phase未定（旧作）: 4冊（X4〜X7）

### thinking-hub
- thinking-hub総数: 14（うちNO-GO 1）
- thinking-hub合計行数: 約14,100行
- 1冊あたり平均: 約1,000行 / 16セクション

---

*このファイルは書籍の状態が変わるたびに更新してください。*
