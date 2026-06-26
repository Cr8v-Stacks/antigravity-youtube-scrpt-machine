#!/usr/bin/env python3
"""Lightweight quality gate for YouTube script packs.

This checks structural failures that repeatedly cause weak scripts. It is not a
replacement for editorial judgment; it is a pre-delivery tripwire.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "misconception map",
    "opening targets",
    "opening attack ladder",
    "script control brief",
    "target runtime",
    "word budget",
    "viewer starting belief",
    "retention engine",
    "scene ladder",
    "retention beat map",
    "re-hook plan",
    "forbidden drift",
    "narrative texture rules",
]

WEAK_TRUTH_PHRASES = [
    "the real answer is",
    "before money, humans relied on",
    "this shows that",
    "this means that",
    "in conclusion",
    "at the end of the day",
    "the key takeaway is",
    "the main point is",
    "the important thing to understand is",
]

WEAK_OPENING_PATTERNS = [
    r"^imagine\b",
    r"^most people think\b",
    r"^have you ever wondered\b",
    r"^in this video\b",
    r"^today we're going to\b",
    r"^since the beginning of time\b",
    r"^throughout history\b",
]

ARTICLE_VOICE_PHRASES = [
    "it is important to note",
    "it is worth noting",
    "in today's world",
    "in modern society",
    "throughout history",
    "since ancient times",
    "as we know it",
    "plays a crucial role",
    "complex and multifaceted",
    "this article",
    "this essay",
    "let's dive in",
    "delve into",
    "when we think about",
]

SCRIPT_FALLBACK_BOUNDARIES = [
    "thumbnail text options",
    "thumbnail options",
    "thumbnail prompt",
    "thumbnail prompts",
    "best thumbnail prompt",
    "seo description",
    "seo meta description",
    "hashtags",
    "tags",
    "research anchors",
    "research material",
    "sources used",
    "shot by shot image prompts",
    "shot-by-shot image prompts",
]

OPENING_PRESSURE_WORDS = [
    "wrong",
    "incomplete",
    "problem",
    "myth",
    "but",
    "except",
    "stranger",
    "not",
    "never",
    "missing",
    "too simple",
    "evidence",
    "clue",
]

VISIBLE_ACTION_WORDS = [
    "hold",
    "holds",
    "holding",
    "walk",
    "walks",
    "share",
    "shares",
    "sharing",
    "give",
    "gives",
    "giving",
    "take",
    "takes",
    "repair",
    "build",
    "record",
    "records",
    "recorded",
    "write",
    "writes",
    "mark",
    "marks",
    "press",
    "presses",
    "measure",
    "measures",
    "weigh",
    "weighs",
    "stamp",
    "stamps",
    "carry",
    "carries",
    "trade",
    "trades",
    "pay",
    "pays",
    "watch",
    "watches",
    "notice",
    "notices",
    "sit",
    "sits",
    "stand",
    "stands",
]

SCRIPT_METADATA_START_PATTERNS = (
    "target runtime",
    "target word",
    "estimated word",
    "actual word",
    "estimated runtime",
    "word count",
)


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w'-]+\b", text.replace(chr(8217), "'"))


HEADING_RE = re.compile(
    r"(?im)^\ufeff?\s*(?:(?:#{1,6}\s*)|(?:(?:\*\*)?\s*\d+\.\s*))"
    r"([A-Za-z][A-Za-z0-9 /&:,\-'()]+?)\s*(?:\*\*)?\s*$"
)


def normalize_heading(value: str) -> str:
    value = value.strip().strip("*# ")
    value = re.sub(r"^\d+\.\s*", "", value)
    value = value.replace(chr(8217), "'")
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def section_spans(text: str) -> list[tuple[str, int, int]]:
    spans: list[tuple[str, int, int]] = []
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        heading = normalize_heading(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        spans.append((heading, start, end))
    return spans


def find_section(text: str, names: list[str]) -> str | None:
    wanted = {normalize_heading(name) for name in names}
    for heading, start, end in section_spans(text):
        if heading in wanted:
            return text[start:end].strip()
    return None


def strip_script_metadata(script: str) -> str:
    lines = script.splitlines()
    first_body_index = 0
    for index, line in enumerate(lines):
        stripped = line.strip().strip("*_`").lower()
        if not stripped:
            continue
        if any(stripped.startswith(pattern) for pattern in SCRIPT_METADATA_START_PATTERNS):
            first_body_index = index + 1
            continue
        first_body_index = index
        break
    return "\n".join(lines[first_body_index:]).strip()


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip().strip("*_`")
        if stripped:
            return stripped
    return ""


def find_script_body(text: str) -> str:
    section = find_section(text, ["script"])
    if section:
        return strip_script_metadata(section)

    match = re.search(r"(?im)^#{0,3}\s*script\s*$", text)
    if not match:
        return text
    body = text[match.end() :]
    boundary_patterns = [r"^#{1,6}\s+\S"]
    for boundary in SCRIPT_FALLBACK_BOUNDARIES:
        boundary_patterns.append(rf"^\s*{re.escape(boundary)}\s*$")
    boundary_re = re.compile("|".join(boundary_patterns), flags=re.I | re.M)
    next_section = boundary_re.search(body)
    if next_section:
        return strip_script_metadata(body[: next_section.start()])
    return body


def first_spoken_line(script: str) -> str:
    for line in script.splitlines():
        stripped = line.strip().strip("*_`")
        if not stripped:
            continue
        if stripped.startswith("#") or stripped.endswith(":"):
            continue
        return stripped.lower()
    return ""


def count_timestamp_beats(text: str) -> int:
    return len(re.findall(r"\b\d{1,2}:\d{2}\s*(?:-|\u2013)\s*\d{1,2}:\d{2}\b", text))


def timestamp_to_seconds(value: str) -> int:
    minutes, seconds = value.split(":")
    return int(minutes) * 60 + int(seconds)


def declared_runtime_seconds(text: str) -> int | None:
    candidates: list[int] = []
    for line in text.splitlines():
        if "runtime" not in line.lower():
            continue
        for match in re.finditer(
            r"\b(\d{1,2}):(\d{2})(?:\s*(?:-|\u2013)\s*(\d{1,2}):(\d{2}))?",
            line,
        ):
            if match.group(3) is not None:
                candidates.append(int(match.group(3)) * 60 + int(match.group(4)))
            else:
                candidates.append(int(match.group(1)) * 60 + int(match.group(2)))
        for match in re.finditer(r"\b(\d+(?:\.\d+)?)\s*minutes?\b", line, flags=re.I):
            candidates.append(int(float(match.group(1)) * 60))
    if not candidates:
        return None
    return max(candidates)


def last_beat_end_seconds(text: str) -> int | None:
    matches = re.findall(
        r"\b\d{1,2}:\d{2}\s*(?:-|\u2013)\s*(\d{1,2}:\d{2})\b",
        text,
    )
    if not matches:
        return None
    return max(timestamp_to_seconds(match) for match in matches)


def paragraph_word_counts(script: str) -> list[int]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", script) if part.strip()]
    return [len(words(paragraph)) for paragraph in paragraphs]


def first_n_words(text: str, count: int) -> str:
    found = words(text)
    return " ".join(found[:count]).lower()


def has_opening_pressure(opening_text: str) -> bool:
    lower = opening_text.lower()
    return any(word in lower for word in OPENING_PRESSURE_WORDS)


def visible_paragraph_ratio(script: str) -> float:
    paragraphs = [part.strip().lower() for part in re.split(r"\n\s*\n", script) if part.strip()]
    substantial = [paragraph for paragraph in paragraphs if len(words(paragraph)) >= 18]
    if not substantial:
        return 0.0
    visible = 0
    for paragraph in substantial:
        has_number_or_date = bool(re.search(r"\b\d{2,4}\b|bce|bc|ce|ad|century", paragraph))
        has_action = any(re.search(rf"\b{re.escape(word)}\b", paragraph) for word in VISIBLE_ACTION_WORDS)
        has_quote_or_question = "?" in paragraph or '"' in paragraph or chr(8220) in paragraph
        if has_number_or_date or has_action or has_quote_or_question:
            visible += 1
    return visible / len(substantial)


def lint(
    text: str,
    target_min: int | None,
    target_max: int | None,
    min_beats: int,
    target_duration_sec: int | None,
) -> list[str]:
    lower = text.lower()
    issues: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in lower:
            issues.append(f"Missing required planning/control item: {section}")

    raw_script_section = find_section(text, ["script"]) or ""
    raw_script_first = first_nonempty_line(raw_script_section).lower()
    if raw_script_first and any(
        raw_script_first.startswith(pattern) for pattern in SCRIPT_METADATA_START_PATTERNS
    ):
        issues.append(
            "Script section starts with production metadata; move runtime/word-count notes "
            "to Runtime or Script Control Brief so # Script begins with spoken narration"
        )

    script = find_script_body(text)
    word_count = len(words(script))
    paragraph_counts = paragraph_word_counts(script)
    if target_min is not None and word_count < target_min:
        issues.append(f"Script body is under target: {word_count} words < {target_min}")
    if target_max is not None and word_count > target_max:
        issues.append(f"Script body is over target: {word_count} words > {target_max}")

    if word_count >= 500 and paragraph_counts:
        short_paragraphs = sum(1 for count in paragraph_counts if count <= 8)
        short_ratio = short_paragraphs / len(paragraph_counts)
        if short_ratio > 0.35:
            issues.append(
                "Script body is too fragmented: "
                f"{short_paragraphs}/{len(paragraph_counts)} paragraphs have 8 words or fewer"
            )

    opening = first_spoken_line(script)
    for pattern in WEAK_OPENING_PATTERNS:
        if re.search(pattern, opening):
            issues.append(f"Weak opening pattern detected: {opening}")
            break

    opening_window = first_n_words(script, 120)
    if word_count >= 500 and not has_opening_pressure(opening_window):
        issues.append(
            "Opening lacks visible pressure in the first 120 words; "
            "attack a belief, contradiction, myth, problem, or evidence gap faster"
        )

    for phrase in WEAK_TRUTH_PHRASES:
        if phrase in lower:
            issues.append(f"Potential abstract truth phrase detected: {phrase}")

    article_hits = [phrase for phrase in ARTICLE_VOICE_PHRASES if phrase in lower]
    if len(article_hits) >= 2:
        issues.append(
            "Article/robotic voice detected; replace essay phrasing with scenes and pressure: "
            + ", ".join(article_hits[:6])
        )

    if word_count >= 700:
        ratio = visible_paragraph_ratio(script)
        if ratio < 0.45:
            issues.append(
                f"Script may read like an article: only {ratio:.0%} of substantial paragraphs "
                "contain visible action, dates/numbers, questions, or scene anchors"
            )

    if lower.count("scene") < 4:
        issues.append("Scene language appears thin; scene ladder or scene-based script may be missing")

    retention_section = find_section(text, ["retention beat map"])
    beat_source = retention_section if retention_section else text
    beat_count = count_timestamp_beats(beat_source)
    if "retention beat map" in lower and beat_count < min_beats:
        issues.append(
            f"Retention Beat Map appears too thin: found {beat_count} timestamped beats < {min_beats}"
        )

    declared_duration_sec = declared_runtime_seconds(text)
    effective_duration_sec = target_duration_sec
    if declared_duration_sec is not None:
        effective_duration_sec = max(effective_duration_sec or 0, declared_duration_sec)

    if effective_duration_sec is not None and "retention beat map" in lower:
        last_end = last_beat_end_seconds(beat_source)
        min_end = int(effective_duration_sec * 0.95)
        if last_end is None:
            issues.append("Retention Beat Map has no parseable timestamp end points")
        elif last_end < min_end:
            issues.append(
                "Retention Beat Map stops too early for the declared runtime: "
                f"last beat ends at {last_end}s < {min_end}s"
            )

    if "re-hook plan" not in lower and lower.count("re-hook") < 1 and lower.count("rehook") < 1:
        issues.append("Re-hook planning appears thin")

    misconception_section_present = "misconception map" in lower or "viewer starting belief" in lower
    misconception_detail_present = (
        "wrong answer" in lower
        or "partial answer" in lower
        or "opening targets" in lower
        or "viewer starting belief" in lower
    )
    if not (misconception_section_present and misconception_detail_present):
        issues.append("Misconception mapping appears thin")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Script pack text/markdown file, or '-' for stdin")
    parser.add_argument(
        "--preset",
        choices=["standard-8"],
        default=None,
        help="Apply a built-in quality target preset.",
    )
    parser.add_argument("--target-min", type=int, default=None)
    parser.add_argument("--target-max", type=int, default=None)
    parser.add_argument(
        "--min-beats",
        type=int,
        default=16,
        help="Minimum timestamped retention beats expected for the pack.",
    )
    parser.add_argument(
        "--target-duration-sec",
        type=int,
        default=None,
        help="Target runtime in seconds; beat map should reach at least 90 percent of it.",
    )
    args = parser.parse_args()

    if args.preset == "standard-8":
        if args.target_min is None:
            args.target_min = 1080
        if args.target_max is None:
            args.target_max = 1350
        if args.min_beats == 16:
            args.min_beats = 16
        if args.target_duration_sec is None:
            args.target_duration_sec = 480

    if args.path == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.path).read_text(encoding="utf-8")

    issues = lint(
        text,
        args.target_min,
        args.target_max,
        args.min_beats,
        args.target_duration_sec,
    )
    if issues:
        print("FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
