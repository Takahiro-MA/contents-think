# 書籍ステータス一覧

> 全書籍のthinking-hub（執筆仕様書）と執筆状態を一覧管理するファイル。
> 状態が変わったら都度更新すること。

Last Updated: 2026-07-04

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
| 8 | Kiro CLI | `kiro-cli/` | `../kindle2/10_kiro-cli-book/epub/` | **Published（2026-07-01）**。神谷PdMとの自治体プロダクト立て直し物語。Phase 5（著者五月雨レビュー：キャラ像調整・Codex技術監査・MCP/Steering/認証の公式照合・章接続修正等を多数反映）完了 |

### 執筆進行中

| # | テーマ | thinking-hub | 章数 | Phase | 通過済み | 出版先 | 備考 |
|---|--------|-------------|------|-------|---------|-------|------|
| 7 | Obsidian/PKM | `obsidian/` | 8 | Phase 6待ち | 1→1R→2→3→4→5→**6待ち** | `../kindle2/08_obsidian-book/epub/` | 著者レビュー24件+整合性チェック指摘を全件修正済み。付録追加。最終バランスチェック待ち |

### thinking-hub作成済み（初稿未着手）

| # | テーマ | thinking-hub | 章数 | Phase | 通過済み | 備考 |
|---|--------|-------------|------|-------|---------|------|
| 8 | 睡眠改善 | `sleep-improvement/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | 著者レビュー後に執筆可能 |
| 9 | デジタルデトックス | `digital-detox/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | 著者レビュー後に執筆可能 |
| 10 | SQL | `sql/` | 9 | Phase 1A待ち | 1→1R→**1A待ち** | 著者レビュー後に執筆可能 |
| 11 | レガシーコード改善 | `legacy-code/` | 8 | Phase 1A待ち | 1→1R→**1A待ち** | TDD本の続編的位置づけ |
| ~~12~~ | ~~Codex CLI~~ | — | — | Published | — | 出版済みセクションに移動 |
| 13 | キャリアピボット | `career-pivot/` | 10 | Phase 1A待ち（保留） | 1→1R→**1A待ち** | 主人公が中村さん。著者の熱量確認待ち |
| ~~14~~ | ~~Kiro CLI~~ | — | — | Published | — | 出版済みセクションに移動（2026-07-01） |
| 15 | 生成AIモバイルアプリ入門（C・入門） | `ai-mobile-app/` | 9 | Phase 1 | **1完了** | 田中さんシリーズ番外編（スピンオフ）。主人公=森田結衣（田中の姉・完全初心者）、田中はメンター。React Web試作→Expo移植→ローカル通知→App Store公開。2冊構想のC先行（BはE10初級・続編候補）。thinking-hub初稿済み、Phase 1R/1A未 |
| 16 | CI/CD（ストーリーで覚えるCI/CD入門） | `cicd/` | 9 | Phase 1R反映済 | 1→**1R反映済** | ideas-hub E5（14点）。主軸「AIがYAMLを書く時代、価値は環境選定と設計判断へ」。異動2部構成（第1部5章:クラウドGitHub×Actions / 第2部4章:製造業の閉域×GHES×self-hosted runner）。メンター山田＋工場情シス相沢涼子。3視点レビューの**A全項目＋B-3〜B-7＋C-1〜C-4を反映済**。残＝B-8（§12以降の未整備セクション新設）→Phase 1A。shared-characters §10B追加設定済 |
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
- 田中さんシリーズ: 出版済み8冊 + 執筆中1冊 + hub済み7冊（うちNO-GO 1, 保留1, 番外編1, CI/CD 1） + 旧作4冊
- 藤井さんシリーズ: 初稿済み1冊 + hub済み2冊
- ゲーム理論シリーズ: 企画段階2冊
- その他: 4件（Ruby, 釣りマンガ, LLM理論書, サンプル）
- アイデア段階（フォルダのみ・status未登録）: 4件（ai-driven-org, gluten-free, libre-diet, low-fat-diet）

### Phase別
- Published: 8冊（最新: Kiro CLI 2026-07-01）
- Phase 6待ち（最終バランスチェック待ち）: 1冊（Obsidian）
- Phase 3待ち（原稿 Claudeレビュー待ち）: 1冊（断酒）
- Phase 1R反映済（thinking-hub Claudeレビュー反映済、1A未）: 1冊（CI/CD）
- Phase 1（thinking-hub初稿済み、1R/1A未）: 1冊（モバイルアプリ入門C）
- Phase 1A待ち（thinking-hub 著者レビュー待ち）: 6冊
- Phase 0（企画段階）: 2冊
- NO-GO: 1冊
- Phase未定（旧作）: 4冊（X4〜X7）

### thinking-hub
- thinking-hub総数: 16（うちNO-GO 1）
- 1冊あたり平均: 約1,000行 / 16セクション

---

*このファイルは書籍の状態が変わるたびに更新してください。*
