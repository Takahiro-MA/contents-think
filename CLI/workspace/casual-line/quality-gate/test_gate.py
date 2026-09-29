"""gate.py の解析部分のテスト（pytest）。"""
from pathlib import Path

import pytest

import gate


@pytest.mark.parametrize("text,expected", [
    ("まず開きます。次に打ちます！送りますか？", 3),
    ("「これで。いいですか。」と聞きます。", 1),
    ("最後に句点がない", 1),
])
def test_split_sentences(text, expected):
    assert len(gate.split_sentences(text)) == expected


def test_strip_quotes_removes_nested():
    assert gate.strip_quotes("彼は「『本』だ」と言いました。") == "彼は「」と言いました。"


@pytest.mark.parametrize("s,n", [("10", 10), ("１２", 12), ("三", 3), ("二十", 20), ("六十", 60), ("十二", 12)])
def test_to_int(s, n):
    assert gate.to_int(s) == n


def test_extract_numbers_units_ranges_and_skips():
    nums = gate.extract_numbers("第3章の図3-1。週2〜3日、5〜10回×3セット、58.8%。")
    assert ("2", "日") in nums and ("3", "日") in nums
    assert ("5", "回") in nums and ("58.8", "%") in nums
    assert not any(v == "3" and u == "" for v, u in nums)  # 第3章・図3-1 は外す


def test_juubun_is_not_ten_minutes():
    assert gate.extract_numbers("それで十分です。十分に使えます。") == []


def test_dearu_detection():
    assert gate.DEARU_END.search("これは大事だ。")
    assert gate.DEARU_END.search("そういうものである。")
    assert not gate.DEARU_END.search("これは大事です。")


def test_parse_chapter(tmp_path: Path):
    md = tmp_path / "03-ch03.md"
    md.write_text("# 第3章　題\n\n**太字だけ**\n\n本文です。\n\n## 節\n\n- 箇条\n\n［図3-1　図］\n\n締めです。\n",
                  encoding="utf-8")
    ch = gate.parse_chapter(md)
    assert ch.number == 3
    kinds = [b.kind for b in ch.blocks]
    assert kinds == ["heading", "caption", "para", "heading", "list", "figure", "para"]
    assert [b.line for b in ch.sections[-1]] == [9, 11, 13]


def test_count_in_chapter_ignores_quotes(tmp_path: Path):
    md = tmp_path / "01-ch01.md"
    md.write_text("# 第1章\n\n「気にしなくていい」と書いてあります。ここは読まなくていいです。\n", encoding="utf-8")
    ch = gate.parse_chapter(md)
    assert len(gate.count_in_chapter(ch, "なくていい")) == 1


def test_config_book_override(tmp_path: Path):
    cfg = tmp_path / "c.yaml"
    cfg.write_text("defaults:\n  stage: draft\n  banned_words: [A]\nbooks:\n  CXX_x:\n    stage: publish\n"
                   "    banned_words_extra: [B]\n", encoding="utf-8")
    loaded = gate.load_config(tmp_path / "CXX_x", cfg)
    assert loaded["stage"] == "publish"
    assert loaded["banned_words"] == ["A", "B"]


def test_report_info_only_never_fails():
    rep = gate.Report()
    rep.check("g", "n", 5, 0, info_only=True)
    rep.check("g", "m", 5, 0)
    assert [r.result for r in rep.rows] == [gate.INFO, gate.FAIL]
