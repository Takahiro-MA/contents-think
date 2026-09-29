#!/usr/bin/env python3
"""カジュアルライン 品質ゲート 第1層（機械チェック）。

使い方:
    python3 gate.py ../../../../../kindle2/C02_kintore-50s \
        --facts notes/2026-09-29-c02-factpack.md --facts c02-kintore-50s/thinking-hub.md \
        --out ../../../../../kindle2/C02_kintore-50s/quality/gate-report.md

閾値は gate-config.yaml（defaults と books.<フォルダ名> の上書き）。
結果は Markdown の点数表。不合格が1件でもあれば終了コード1。
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import difflib
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
EPUBCHECK_JAR = Path.home() / "epubcheck-5.2.1" / "epubcheck.jar"

PASS, FAIL, INFO = "合格", "**不合格**", "参考"

KANJI_DIGITS = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
UNITS = ("mmHg|kcal|kg|km|cm|%|％|パーセント|メッツ|キロ|グラム|セット|ページ|か月|カ月|ヶ月|時間|往復|"
         "回|日|分|秒|歳|代|年|月|歩|円|週|割|人|か所|倍|字|杯|品|種目|問")
ARABIC_NUM = re.compile(r"\d+(?:\.\d+)?")
KANJI_NUM = re.compile(r"[一二三四五六七八九十百]+(?=(?:" + UNITS + r"))")
# 番号として使う数字（事実ではない）は照合から外す
NUMBER_SKIP_BEFORE = re.compile(r"(?:第|図|表|段|例|手順|ステップ|項目|v|No\.?)\s*$")
NUMBER_SKIP_AFTER = re.compile(r"^(?:[-－‐]\d|章|節|\.\s)")


# --------------------------------------------------------------------------
# 原稿の読み込み
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Block:
    kind: str       # heading / para / list / quote / table / image / figure
    text: str
    line: int       # 1始まり
    level: int = 0  # heading のレベル


@dataclass
class Chapter:
    name: str
    blocks: list[Block]
    title: str = ""
    number: int | None = None           # 「# 第N章」の N
    sections: list[list[Block]] = field(default_factory=list)


def classify_line(line: str) -> tuple[str, int]:
    s = line.strip()
    if m := re.match(r"^(#{1,6})\s", s):
        return "heading", len(m.group(1))
    if re.match(r"^!\[.*\]\(.*\)$", s):
        return "image", 0
    if re.match(r"^\*\*[^*]+\*\*$", s):
        return "caption", 0  # 太字だけの行（サブタイトル・Q見出し）は段落として数えない
    if re.match(r"^[［\[]図", s):
        return "figure", 0
    if re.match(r"^([-*]|\d+[.)])\s", s) or s.startswith("- ["):
        return "list", 0
    if s.startswith(">"):
        return "quote", 0
    if s.startswith("|"):
        return "table", 0
    if re.match(r"^(---+|\*\*\*+)$", s):
        return "hr", 0
    return "para", 0


def parse_chapter(path: Path) -> Chapter:
    blocks: list[Block] = []
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        kind, level = classify_line(raw)
        if kind == "hr":
            continue
        text = re.sub(r"^(#{1,6}|>|[-*]|\d+[.)])\s*", "", raw.strip())
        blocks.append(Block(kind, text, i, level))
    ch = Chapter(path.name, blocks)
    for b in blocks:
        if b.kind == "heading" and b.level == 1:
            ch.title = b.text
            if m := re.match(r"第([0-9０-９一二三四五六七八九十]+)章", b.text):
                ch.number = to_int(m.group(1))
            break
    ch.sections = split_sections(blocks)
    return ch


def split_sections(blocks: list[Block]) -> list[list[Block]]:
    sections: list[list[Block]] = [[]]
    for b in blocks:
        if b.kind == "heading":
            sections.append([])
        else:
            sections[-1].append(b)
    return [s for s in sections if s]


def to_int(s: str) -> int:
    s = unicodedata.normalize("NFKC", s)
    if s.isdigit():
        return int(s)
    total, cur = 0, 0
    for c in s:
        if c in KANJI_DIGITS:
            cur = KANJI_DIGITS[c]
        elif c == "十":
            total += (cur or 1) * 10
            cur = 0
        elif c == "百":
            total += (cur or 1) * 100
            cur = 0
    return total + cur


def strip_quotes(text: str) -> str:
    """「」『』の中身を除く（地の文だけにする）。入れ子に対応。
    括弧は「」として残し、前後の語が引っついて誤検出しないようにする。"""
    out, depth = [], 0
    for c in text:
        if c in "「『":
            if depth == 0:
                out.append("「")
            depth += 1
            continue
        if c in "」』":
            depth = max(0, depth - 1)
            if depth == 0:
                out.append("」")
            continue
        if depth == 0:
            out.append(c)
    return "".join(out)


def split_sentences(text: str) -> list[str]:
    out, buf, depth = [], [], 0
    for c in text:
        buf.append(c)
        if c in "「『（(":
            depth += 1
        elif c in "」』）)":
            depth = max(0, depth - 1)
        elif c in "。！？" and depth == 0:
            out.append("".join(buf).strip())
            buf = []
    if "".join(buf).strip():
        out.append("".join(buf).strip())
    return out


def plain(text: str) -> str:
    return re.sub(r"\*\*|__|`", "", text)


def body_chars(ch: Chapter) -> int:
    n = 0
    for b in ch.blocks:
        if b.kind in ("image", "figure"):
            continue
        t = plain(b.text).replace("|", "")
        n += len(re.sub(r"\s", "", t))
    return n


# --------------------------------------------------------------------------
# 設定と結果
# --------------------------------------------------------------------------

def load_config(book: Path, path: Path) -> dict:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    cfg = dict(raw.get("defaults", {}))
    over = (raw.get("books") or {}).get(book.name, {})
    cfg.update({k: v for k, v in over.items() if k != "banned_words_extra"})
    cfg["banned_words"] = list(cfg.get("banned_words", [])) + list(over.get("banned_words_extra", []))
    return cfg


@dataclass(frozen=True)
class Row:
    group: str
    name: str
    value: str
    threshold: str
    result: str


class Report:
    def __init__(self) -> None:
        self.rows: list[Row] = []
        self.details: list[tuple[str, list[str]]] = []

    def check(self, group: str, name: str, value: float, limit: float | None,
              info_only: bool = False, fmt: str = "{:g}", op: str = "<=") -> None:
        if limit is None or info_only:
            result = INFO
        elif op == "<=":
            result = PASS if value <= limit else FAIL
        else:
            result = PASS if value >= limit else FAIL
        thr = "—" if limit is None else f"{op} {fmt.format(limit)}"
        self.rows.append(Row(group, name, fmt.format(value), thr, result))

    def add_row(self, row: Row) -> None:
        self.rows.append(row)

    def detail(self, title: str, lines: list[str]) -> None:
        self.details.append((title, lines))

    @property
    def failed(self) -> list[Row]:
        return [r for r in self.rows if r.result == FAIL]


def loc(ch: Chapter, b: Block) -> str:
    return f"{ch.name}:{b.line}"


# --------------------------------------------------------------------------
# 形式
# --------------------------------------------------------------------------

def read_chapter_files(book: Path) -> list[str] | None:
    script = book / "build" / "build_epub.py"
    if not script.exists():
        return None
    tree = ast.parse(script.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "CHAPTER_FILES" for t in node.targets):
            return list(ast.literal_eval(node.value))
    return None


def run_epubcheck(epub: Path) -> tuple[int, int, list[str]]:
    proc = subprocess.run(["java", "-jar", str(EPUBCHECK_JAR), str(epub)],
                          capture_output=True, text=True, timeout=300)
    out = proc.stdout + proc.stderr
    m = re.search(r"Messages:\s*(\d+) fatals? / (\d+) errors? / (\d+) warnings?", out)
    if m:
        fatals, errors, warnings = map(int, m.groups())
    else:
        fatals, errors, warnings = 0, len(re.findall(r"^(?:ERROR|FATAL)", out, re.M)), \
            len(re.findall(r"^WARNING", out, re.M))
    msgs = [l for l in out.splitlines() if re.match(r"^(FATAL|ERROR|WARNING)", l)]
    return fatals + errors, warnings, msgs


def check_format(book: Path, rep: Report, cfg: dict, skip_epubcheck: bool) -> None:
    files = read_chapter_files(book)
    on_disk = sorted(p.name for p in (book / "epub").glob("*.md"))
    if files is None:
        rep.add_row(Row("形式", "CHAPTER_FILES と epub/*.md の一致", "build_epub.py なし", "一致", FAIL))
    else:
        missing = [f for f in on_disk if f not in files]
        ghost = [f for f in files if f not in on_disk]
        ok = not missing and not ghost
        rep.add_row(Row("形式", "CHAPTER_FILES と epub/*.md の一致",
                        "一致" if ok else f"漏れ {missing} / 実在しない {ghost}", "一致", PASS if ok else FAIL))
    epubs = sorted((book / "release").glob("*.epub"), key=lambda p: p.stat().st_mtime)
    if not epubs:
        rep.add_row(Row("形式", "epubcheck", "EPUBなし", "0", FAIL))
        return
    latest = epubs[-1]
    if skip_epubcheck:
        rep.add_row(Row("形式", f"epubcheck（{latest.name}）", "未実行", "0", INFO))
        return
    errors, warnings, msgs = run_epubcheck(latest)
    rep.check("形式", f"epubcheck エラー（{latest.name}）", errors, cfg["epubcheck_max_errors"])
    rep.check("形式", "epubcheck 警告", warnings, cfg["epubcheck_max_warnings"])
    if msgs:
        rep.detail("epubcheck のメッセージ", msgs[:30])


# --------------------------------------------------------------------------
# 文体
# --------------------------------------------------------------------------

DEARU_END = re.compile(r"(?:だ|である|だった|であった|だろう|であろう|のだ|ではない|じゃない)[。！]?$")


def para_sentences(ch: Chapter):
    for b in ch.blocks:
        if b.kind == "para":
            for s in split_sentences(plain(b.text)):
                yield b, s


def check_style(chs: list[Chapter], rep: Report, cfg: dict) -> None:
    dearu, longp, oneliners = [], [], []
    for ch in chs:
        for b, s in para_sentences(ch):
            narr = strip_quotes(s).strip()
            if narr and DEARU_END.search(narr):
                dearu.append(f"{loc(ch, b)} {s}")
        for b in ch.blocks:
            if b.kind == "para":
                n = len(split_sentences(plain(b.text)))
                if n >= cfg["long_paragraph_sentences"]:
                    longp.append(f"{loc(ch, b)}（{n}文） {b.text[:40]}…")
        for sec in ch.sections:
            last = sec[-1]
            if last.kind != "para":
                continue
            sents = split_sentences(plain(last.text))
            if len(sents) == 1 and len(sents[0]) <= cfg["section_end_oneliner_max_chars"]:
                oneliners.append(f"{loc(ch, last)} {sents[0]}")
    rep.check("文体", "「だ・である」調の文末（地の文）", len(dearu), cfg["dearu_max"])
    rep.check("文体", f"{cfg['long_paragraph_sentences']}文以上の段落", len(longp), cfg["long_paragraph_max"])
    per10k = len(oneliners) * 10000 / max(sum(body_chars(c) for c in chs), 1)
    rep.check("文体", f"1文段落で節を終える（{cfg['section_end_oneliner_max_chars']}字以下・決め台詞の候補）"
              f" 1万字あたり（{len(oneliners)}か所）", round(per10k, 1), cfg["section_end_oneliner_per_10k_max"])
    rep.detail("「だ・である」調の文末", dearu)
    rep.detail("長い段落", longp)
    rep.detail("節を1文段落で終える箇所（決め台詞の候補）", oneliners)


# --------------------------------------------------------------------------
# AIっぽさ
# --------------------------------------------------------------------------

def count_in_chapter(ch: Chapter, pattern: str, kinds=("para", "list", "quote", "table")) -> list[str]:
    """書き手の地の文だけを数える（「」内の引用・例文・会話は除く）。"""
    rx = re.compile(pattern)
    hits = []
    for b in ch.blocks:
        if b.kind in kinds:
            text = strip_quotes(plain(b.text))
            for m in rx.finditer(text):
                hits.append(f"{loc(ch, b)} …{text[max(0, m.start() - 15):m.end() + 10]}…")
    return hits


def check_aiism(chs: list[Chapter], rep: Report, cfg: dict) -> None:
    total_chars = sum(body_chars(c) for c in chs)
    comfort_rx = "|".join(f"(?:{p})" for p in cfg["comfort_patterns"])
    per_ch = {c.name: count_in_chapter(c, comfort_rx) for c in chs}
    worst = max(per_ch.items(), key=lambda kv: len(kv[1]))
    rep.check("AIっぽさ", f"慰め・許可の言葉 1章の最多（{worst[0]}）", len(worst[1]), cfg["comfort_per_chapter_max"])
    rep.check("AIっぽさ", "慰め・許可の言葉 合計", sum(len(v) for v in per_ch.values()), cfg["comfort_total_max"])
    rep.detail("慰め・許可の言葉（章ごとの回数）",
               [f"{k}: {len(v)}" for k, v in per_ch.items()] + [h for v in per_ch.values() for h in v])

    simple = [("「AではなくB」（ではなく／じゃなく）", r"(?:では|じゃ)なく(?!て)", "not_a_but_b_max", False),
              ("「のです」（1万字あたり。「ものです」を除く）", r"(?<!も)のです", "noda_per_10k_max", True),
              ("「つまり」", r"つまり", "tsumari_max", False),
              ("「むしろ」", r"むしろ", "mushiro_max", False)]
    for label, pat, key, per10k in simple:
        hits = [h for c in chs for h in count_in_chapter(c, pat)]
        value = len(hits) * 10000 / max(total_chars, 1) if per10k else len(hits)
        rep.check("AIっぽさ", label + (f"（{len(hits)}回）" if per10k else ""), round(value, 1), cfg[key])
        rep.detail(label, hits)

    disc_rx = "|".join(re.escape(p) for p in cfg["disclaimer_patterns"])
    # 表の出典欄は断り書きを集約する正しい置き場所なので数えない（writing-checklist 4.）
    disc = [h for c in chs for h in count_in_chapter(c, disc_rx, kinds=("para", "list", "quote"))]
    rep.check("AIっぽさ", "断り書き定型（表の出典欄を除く）", len(disc), cfg["disclaimer_max"])
    rep.detail("断り書き定型", disc)

    check_duplicates(chs, rep, cfg)
    check_openings(chs, rep, cfg)
    check_chapter_ref_counts(chs, rep, cfg)


def norm_sentence(s: str) -> str:
    return re.sub(r"[\s、。！？「」『』（）()・…—\-*]", "", s)


def check_duplicates(chs: list[Chapter], rep: Report, cfg: dict) -> None:
    items = []
    for ch in chs:
        for b, s in para_sentences(ch):
            n = norm_sentence(s)
            if len(n) >= cfg["duplicate_sentence_min_chars"]:
                items.append((n, ch.name, b.line, s))
    items.sort(key=lambda x: len(x[0]))
    pairs = []
    for i, (a, ca, la, sa) in enumerate(items):
        for b, cb, lb, sb in items[i + 1:]:
            if len(b) > len(a) * 1.12 + 1:
                break
            if ca == cb:
                continue
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            if sm.real_quick_ratio() < cfg["near_duplicate_ratio"] or sm.quick_ratio() < cfg["near_duplicate_ratio"]:
                continue
            r = sm.ratio()
            if r >= cfg["near_duplicate_ratio"]:
                kind = "同一" if a == b else f"ほぼ同一 {r:.2f}"
                pairs.append(f"{kind}: {ca}:{la} 「{sa}」 ／ {cb}:{lb} 「{sb}」")
    rep.check("AIっぽさ", "章をまたぐ同一・ほぼ同一の文", len(pairs), cfg["duplicate_cross_chapter_max"])
    rep.detail("章をまたぐ同一・ほぼ同一の文", pairs)


def first_sentence(ch: Chapter) -> tuple[Block, str] | None:
    for b, s in para_sentences(ch):
        return b, s
    return None


def check_openings(chs: list[Chapter], rep: Report, cfg: dict) -> None:
    numbered = [c for c in chs if c.number is not None]
    openings = [(c, fs) for c in numbered if (fs := first_sentence(c))]
    konoshou = [f"{loc(c, b)} {s}" for c, (b, s) in openings if s.startswith("この章では")]
    prefixes = Counter(norm_sentence(s)[:6] for _, (_, s) in openings)
    top = prefixes.most_common(1)[0] if prefixes else ("", 0)
    rep.check("AIっぽさ", f"章の書き出しが同じ型（最初の6字「{top[0]}」）", top[1], cfg["opening_same_prefix_max"])
    rep.check("AIっぽさ", "「この章では」で始まる章", len(konoshou), cfg["opening_konoshou_max"])
    rep.detail("章の書き出し（1文目）", [f"{loc(c, b)} {s}" for c, (b, s) in openings])


CHREF = re.compile(r"第([0-9０-９一二三四五六七八九十]+)章")


def chapter_refs(chs: list[Chapter]):
    for ch in chs:
        for b in ch.blocks:
            if b.kind == "heading" and b.level == 1:
                continue
            for m in CHREF.finditer(b.text):
                yield ch, b, to_int(m.group(1))


def check_chapter_ref_counts(chs: list[Chapter], rep: Report, cfg: dict) -> None:
    per = Counter(ch.name for ch, _, _ in chapter_refs(chs))
    total = sum(per.values())
    per10k = total * 10000 / max(sum(body_chars(c) for c in chs), 1)
    worst = per.most_common(1)[0] if per else ("—", 0)
    rep.check("AIっぽさ", f"「第N章」1万字あたり（総数{total}、章見出しを除く）", round(per10k, 1),
              cfg["chapter_ref_per_10k_max"])
    rep.check("AIっぽさ", f"「第N章」1章の最多（{worst[0]}）", worst[1], cfg["chapter_ref_per_chapter_max"])
    rep.detail("「第N章」の章ごとの回数", [f"{c.name}: {per.get(c.name, 0)}" for c in chs])


# --------------------------------------------------------------------------
# 参照
# --------------------------------------------------------------------------

def check_refs(book: Path, chs: list[Chapter], rep: Report, cfg: dict, publish: bool) -> None:
    existing = {c.number for c in chs if c.number is not None}
    bad = [f"{loc(ch, b)} 第{n}章" for ch, b, n in chapter_refs(chs) if n not in existing]
    rep.check("参照", f"実在しない章への参照（実在: 第{min(existing, default=0)}〜{max(existing, default=0)}章）",
              len(bad), cfg["bad_chapter_ref_max"])
    rep.detail("実在しない章への参照", bad)

    figs = [f"{loc(c, b)} {b.text[:50]}" for c in chs for b in c.blocks if b.kind == "figure"]
    rep.check("参照", "図の仮枠（［図…］）", len(figs), cfg["figure_placeholder_max"], info_only=not publish)
    rep.detail("図の仮枠", figs)

    missing = []
    for c in chs:
        for b in c.blocks:
            if b.kind == "image":
                m = re.search(r"\]\((.+?)\)", b.text)
                if m and not ((book / "epub" / m.group(1)).exists() or (book / m.group(1)).exists()):
                    missing.append(f"{loc(c, b)} {m.group(1)}")
    rep.check("参照", "画像ファイルの欠落", len(missing), cfg["missing_image_max"])
    rep.detail("画像ファイルの欠落", missing)


# --------------------------------------------------------------------------
# 数字
# --------------------------------------------------------------------------

def normalize_numbers(text: str) -> str:
    t = unicodedata.normalize("NFKC", text)
    t = re.sub(r"(?<=\d),(?=\d{3})", "", t)
    return KANJI_NUM.sub(kanji_to_arabic, t)


def kanji_to_arabic(m: re.Match) -> str:
    # 「十分（じゅうぶん）」は数字ではない
    if m.group(0) == "十" and m.string[m.end():m.end() + 1] == "分":
        return m.group(0)
    return str(to_int(m.group(0)))


def extract_numbers(text: str) -> list[tuple[str, str]]:
    """(数値, 単位) の組。範囲（5〜10回）は両端に同じ単位をつける。"""
    t = normalize_numbers(text)
    out = []
    for m in ARABIC_NUM.finditer(t):
        before, after = t[max(0, m.start() - 4):m.start()], t[m.end():m.end() + 3]
        if NUMBER_SKIP_BEFORE.search(before) or NUMBER_SKIP_AFTER.match(after):
            continue
        if re.match(r"^\s*[.)]\s", t[m.end():]) and m.start() == 0:
            continue
        rest = t[m.end():]
        chain = re.match(r"^(?:\s*[〜~～ー\-－、・と]\s*\d+(?:\.\d+)?)*\s*(" + UNITS + ")", rest)
        out.append((m.group(0), chain.group(1) if chain else ""))
    return out


def check_numbers(chs: list[Chapter], facts: list[Path], rep: Report, cfg: dict, publish: bool) -> None:
    if not facts:
        found = Counter()
        for c in chs:
            for b in c.blocks:
                for v, u in extract_numbers(b.text):
                    found[f"{v}{u}"] += 1
        rep.add_row(Row("数字", "出所の照合（事実ファイルなし）", f"{len(found)}種類", "—", INFO))
        rep.detail("本文の数字（種類と回数）", [f"{k} ×{n}" for k, n in found.most_common()])
        return
    src = "\n".join(normalize_numbers(p.read_text(encoding="utf-8")) for p in facts)
    src_nums = set(ARABIC_NUM.findall(src))
    allow = {normalize_numbers(a) for a in cfg.get("number_allow", [])}
    unknown, weak = [], []
    for c in chs:
        if c.name.endswith("references.md"):
            continue
        for b in c.blocks:
            for v, u in extract_numbers(b.text):
                if (u and f"{v}{u}" in src) or f"{v}{u}" in allow:
                    continue
                if v in src_nums:
                    if u:
                        weak.append(f"{loc(c, b)} {v}{u}")
                    continue
                unknown.append(f"{loc(c, b)} {v}{u} …{b.text[:40]}…")
    names = ", ".join(p.name for p in facts)
    rep.check("数字", f"出所不明の数字（{names} に無い）", len(unknown), cfg["unknown_number_max"],
              info_only=not (publish and cfg.get("numbers_gate", True)))
    rep.add_row(Row("数字", "数値は資料にあるが単位つきでは無い（要目視）", str(len(weak)), "—", INFO))
    rep.detail("出所不明の数字", unknown)
    rep.detail("単位つきでは資料に無い数字", weak)


# --------------------------------------------------------------------------
# 禁止語・字数
# --------------------------------------------------------------------------

def check_banned(chs: list[Chapter], rep: Report, cfg: dict, exclude_quotes: bool) -> None:
    hits = []
    for c in chs:
        for b in c.blocks:
            text = strip_quotes(b.text) if exclude_quotes else b.text
            for w in cfg["banned_words"]:
                if w in text:
                    hits.append(f"{loc(c, b)} 「{w}」 …{b.text[:40]}…")
    note = "（「」内を除く）" if exclude_quotes else ""
    rep.check("禁止語", f"使わない言葉{note}: {'／'.join(cfg['banned_words'])}", len(hits), 0)
    rep.detail("使わない言葉", hits)


def check_length(chs: list[Chapter], rep: Report, cfg: dict) -> None:
    per = [(c.name, body_chars(c)) for c in chs]
    total = sum(n for _, n in per)
    ok = cfg["total_chars_min"] <= total <= cfg["total_chars_max"]
    rep.add_row(Row("字数", "本文合計（空白・記号を除く）", f"{total:,}",
                    f"{cfg['total_chars_min']:,}〜{cfg['total_chars_max']:,}", PASS if ok else FAIL))
    rep.detail("章ごとの字数", [f"{n}: {k:,}" for n, k in per])


# --------------------------------------------------------------------------
# 出力
# --------------------------------------------------------------------------

def render(book: Path, cfg: dict, rep: Report, facts: list[Path]) -> str:
    verdict = "合格" if not rep.failed else f"不合格（{len(rep.failed)}項目）"
    lines = [f"# 品質ゲート 第1層レポート: {book.name}", "",
             f"- 実行日: {dt.date.today().isoformat()}",
             f"- 段階: {cfg['stage']}（draft は図の仮枠・数字の照合を「参考」表示のみ）",
             f"- 事実ファイル: {', '.join(str(p) for p in facts) or 'なし'}",
             f"- 判定: **{verdict}**", "",
             "| 区分 | 項目 | 実測 | 閾値 | 判定 |", "|---|---|---:|---|---|"]
    lines += [f"| {r.group} | {r.name} | {r.value} | {r.threshold} | {r.result} |" for r in rep.rows]
    lines += ["", "---", "", "## 明細", ""]
    for title, items in rep.details:
        lines.append(f"### {title}（{len(items)}）")
        lines.append("")
        lines += [f"- {i}" for i in items] if items else ["（なし）"]
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book", type=Path, help="本のフォルダ（kindle2/CNN_xxx）")
    ap.add_argument("--facts", type=Path, action="append", default=[], help="事実パック・hub（複数可）")
    ap.add_argument("--config", type=Path, default=HERE / "gate-config.yaml")
    ap.add_argument("--stage", choices=["draft", "publish"], help="設定の stage を上書き")
    ap.add_argument("--banned", action="append", default=[], help="使わない言葉を追加（複数可）")
    ap.add_argument("--exclude-quotes", action="store_true", help="禁止語の判定で「」内を除く")
    ap.add_argument("--skip-epubcheck", action="store_true")
    ap.add_argument("--out", type=Path, help="出力先（省略時は <book>/quality/gate-report.md）")
    args = ap.parse_args()

    book = args.book.resolve()
    if not (book / "epub").is_dir():
        print(f"epub/ がありません: {book}", file=sys.stderr)
        return 2
    cfg = load_config(book, args.config)
    if args.stage:
        cfg["stage"] = args.stage
    cfg["banned_words"] += args.banned
    publish = cfg["stage"] == "publish"
    for f in args.facts:
        if not f.exists():
            print(f"事実ファイルがありません: {f}", file=sys.stderr)
            return 2

    order = read_chapter_files(book) or sorted(p.name for p in (book / "epub").glob("*.md"))
    chs = [parse_chapter(book / "epub" / n) for n in order if (book / "epub" / n).exists()]

    rep = Report()
    check_format(book, rep, cfg, args.skip_epubcheck)
    check_style(chs, rep, cfg)
    check_aiism(chs, rep, cfg)
    check_refs(book, chs, rep, cfg, publish)
    check_numbers(chs, args.facts, rep, cfg, publish)
    check_banned(chs, rep, cfg, args.exclude_quotes)
    check_length(chs, rep, cfg)

    out = args.out or book / "quality" / "gate-report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(book, cfg, rep, args.facts), encoding="utf-8")
    print(f"{out}: {'合格' if not rep.failed else '不合格 ' + str(len(rep.failed)) + '項目'}")
    for r in rep.failed:
        print(f"  - [{r.group}] {r.name}: {r.value}（{r.threshold}）")
    return 1 if rep.failed else 0


if __name__ == "__main__":
    sys.exit(main())
