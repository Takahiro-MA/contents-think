# Article Creation Workflow (Web-Chat Based)

Web版LLM（ChatGPT, Gemini, Claude等）を使って、記事の構成と内容を素早く作成するためのフローです。

## 1. 準備 (Setup)
1.  `article-contents-think` フォルダを開く。
2.  `topic-ideas.md` から書きたいネタを選ぶ（または新しく思いつく）。
3.  **`article-brainstorming-prompt.md` をエディタで開く。**

## 2. コンテキスト入力 (Input Context)
1.  `article-brainstorming-prompt.md` 内の **「## Current Topic / Context」** セクションを編集する。
    *   今回のテーマ、ターゲット、言いたいこと（仮）を書き込む。
    *   前の記事の続きなら、その要約を入れても良い。

## 3. セッション開始 (Start Session)
1.  `article-brainstorming-prompt.md` の **全文をコピー** する。
2.  Web版LLMのチャット欄に **ペーストして送信** する。

## 4. 議論・構成 (Brainstorming)
*   AIは「Webメディア編集者」として振る舞うので、質問に答えたり、提案された切り口を選んだりして議論する。
*   **ポイント**: 
    *   「もっと鋭くして」
    *   「読者が共感するポイントはどこ？」
    *   「タイトル案を10個出して」
    *   といった指示で深掘りする。

## 5. 執筆・出力 (Drafting)
1.  構成が固まったら、「この構成で本文のドラフトを書いて（マークダウン形式で）」と指示する。
2.  出力されたテキストをコピーする。

## 6. 保存 (Save)
1.  `drafts/` フォルダ内に新しいファイルを作成する（例: `YYYY-MM-DD-テーマ名.md`）。
2.  コピーした内容をペーストして保存する。
3.  必要であれば `topic-ideas.md` のネタを「消化済み」にする。
