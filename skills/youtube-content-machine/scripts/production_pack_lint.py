#!/usr/bin/env python3
"""Quality gate for full YouTube production packs.

This catches failures that can look acceptable in text but break production:
thin shot lists, oversized timestamps, missing narration coverage, one-prompt
"shot" labels, weak prompt depth, and visual-style inconsistency.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from script_quality_lint import find_script_body, find_section, normalize_heading, section_spans, words


FULL_PACK_SECTIONS = [
    "title",
    "runtime",
    "script control brief",
    "opening attack ladder",
    "retention beat map",
    "narrative texture rules",
    "channel visual identity lock",
    "selected visual system",
    "thumbnail",
    "script",
    "shot by shot image prompts",
    "seo meta description",
    "hashtags",
    "tags",
    "research material",
]

CHANNEL_LOCK_REQUIRED = [
    "channel/niche identity",
    "default episode visual system",
    "identity preset",
    "approved",
    "style dna",
    "thumbnail art dna",
    "forbidden drift",
]

CAMERA_TERMS = [
    "close-up",
    "medium shot",
    "wide shot",
    "overhead",
    "top-down",
    "macro",
    "foreground",
    "background",
    "framing",
    "composition",
    "centered",
    "split frame",
    "side view",
    "point of view",
    "shallow focus",
    "depth of field",
    "full frame",
    "map-like",
    "diagram layout",
    "timeline",
    "panoramic",
]

EMOTION_TERMS = [
    "tension",
    "tense",
    "mood",
    "emotional",
    "confused",
    "cautious",
    "thoughtful",
    "pressure",
    "dramatic",
    "calm",
    "anxious",
    "skeptical",
    "breakthrough",
    "curiosity",
    "reflective",
    "uneasy",
    "stunned",
    "worried",
    "awkward",
    "surprise",
    "urgent",
    "focused",
]

LAZY_LABEL_PATTERNS = [
    r"\bbusy ancient marketplace\b",
    r"\bbusy marketplace\b",
    r"\bancient marketplace with strangers\b",
    r"\bgeneric marketplace\b",
    r"\bpeople using\b",
    r"\bperson thinking\b",
    r"\bancient scene\b",
    r"\bmodern scene\b",
    r"\bgroup of people\b",
    r"\bcrowd scene\b",
]

LEAN_ESCAPE_PATTERNS = [
    r"\blean editor-ready shot list\b",
    r"\blean shot list\b",
    r"\bexpand each\b.{0,80}\bmicro-shots\b",
    r"\bstrict validator-complete\b",
    r"\btoo bulky\b.{0,80}\bshot",
]

REPEATED_PROMPT_OPENINGS = [
    r"^medium shot of\b",
    r"^close-up composition focused on\b",
    r"^overhead diagram layout turning\b",
    r"^wide shot of\b",
    r"^tight close-up of\b",
    r"^centered composition of\b",
    r"^a literal\b",
    r"^an object-led\b",
    r"^a system-map\b",
    r"^top-down composition turning\b",
    r"^diagram layout for\b",
]

REPEATED_PROMPT_BODY_PATTERNS = [
    r"\bnarration cue\b",
    r"\breacting to\b",
    r"\bone .{0,40}figure reacting with\b",
    r"\bsits in the foreground beside small annotations\b",
    r"\bvisible arrows connecting\b",
    r"\bas a hand-drawn system map\b",
    r"\bthree small nodes for\b",
    r"\btiny map route and date tick\b",
    r"\bvisible social pressure\b",
    r"\bobject-specific historical details\b",
    r"\bstrong foreground-background clarity\b",
    r"\bclear foreground-background composition\b",
    r"\bno modern props or decorative clutter\b",
    r"\barranging .{0,90} as nodes connected by .{0,40} arrows\b",
    r"\bwhile arrows connect .{0,70} labels around the figure\b",
    r"\bexplicit emotional tension\b",
    r"\bunder visible pressure\b",
    r"\bin a tense narrative frame\b",
    r"\bonly the necessary arrows\b",
    r"\bone or two hand[- ]lettered labels specific to this beat\b",
    r"\bspecific to this beat\b",
    r"\bprecise historical props\b",
    r"\bmedium visual density\b",
    r"\bshaped as a\b",
    r"\bsimple role-based figures stand near the specific goods\b",
    r"\bmarks, or arrows that carry the exchange\b",
    r"\btrust-and-memory map\b",
    r"\bframe the timeline, witness marks, route line, or obligation loop\b",
    r"\bviewer feels .{0,40} before reading labels\b",
    r"\bbackground labels point to\b",
]

ROTATING_FRAGMENT_BANK_PATTERNS = [
    r"\bforeground sketch note references\b",
    r"\bbackground margin shows\b",
    r"\blower corner includes\b",
    r"\bcomposition reserves clean negative space\b",
    r"\bone witness mark or route tick\b",
    r"\bframe includes a small before[- ]after cue\b",
    r"\bedge annotation turns\b",
    r"\bforeground-to-background layout\b",
    r"\btiny date, debt, or status marker\b",
    r"\bone human gesture or object placement\b",
    r"\bpaper-margin insert shows\b",
    r"\bsimple map, tally, or memory mark\b",
]

ALLOWED_REPEATED_CLAUSE_PATTERNS = [
    r"\bhybrid sketch system map\b",
    r"\bancient/system-map identity\b",
    r"\bblack ink linework\b",
    r"\boff white\b",
    r"\bpaper texture\b",
    r"\bnotebook paper\b",
    r"\bmuted earth\b",
    r"\bno\b",
    r"\bavoid\b",
    r"\bwithout\b",
    r"\bexclude\b",
]

GENERIC_PADDING_TAIL_RE = re.compile(
    r",\s*(with (?:visible social pressure|clear foreground-background composition).+?)\.\s*$",
    flags=re.I,
)

SHOT_RE = re.compile(
    r"(?m)^\s*(?:shot\s*)?(\d+)[\).]\s*"
    r"(\d{1,2}:\d{2})\s*(?:-|\u2013)\s*(\d{1,2}:\d{2})"
)

PROMPT_LABEL_RE = re.compile(
    r"(?im)^\s*(?:prompt(?:\s+[abc])?|image prompt(?:\s+[abc])?|variation [abc]|[abc])\s*:\s*"
)

NARRATION_LINE_RE = re.compile(
    r"(?im)^\s*(?:narration|narration line|phrase|phrase covered|covers|covered narration)\s*:\s*(.+?)\s*$"
)

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "did",
    "for",
    "from",
    "had",
    "has",
    "have",
    "he",
    "her",
    "him",
    "his",
    "if",
    "in",
    "is",
    "it",
    "its",
    "not",
    "of",
    "on",
    "or",
    "people",
    "person",
    "that",
    "the",
    "their",
    "them",
    "then",
    "they",
    "this",
    "to",
    "was",
    "were",
    "what",
    "when",
    "who",
    "why",
    "with",
}


def timestamp_to_seconds(value: str) -> int:
    minutes, seconds = value.split(":")
    return int(minutes) * 60 + int(seconds)


def extract_selected_visual_system(text: str) -> str | None:
    section = find_section(text, ["selected visual system"])
    if not section:
        return None
    for line in section.splitlines():
        stripped = line.strip().strip("*_` ")
        if not stripped or stripped.lower().startswith("reason"):
            continue
        return stripped
    return None


def headings(text: str) -> set[str]:
    return {heading for heading, _start, _end in section_spans(text)}


def has_character_section(all_headings: set[str]) -> bool:
    return any(
        "primary character" in heading
        or "recurring character" in heading
        or "character set" in heading
        for heading in all_headings
    )


def split_shot_blocks(shot_section: str) -> list[dict[str, object]]:
    matches = list(SHOT_RE.finditer(shot_section))
    shots: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        start = timestamp_to_seconds(match.group(2))
        end = timestamp_to_seconds(match.group(3))
        block_start = match.end()
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(shot_section)
        shots.append(
            {
                "number": int(match.group(1)),
                "start": start,
                "end": end,
                "duration": end - start,
                "heading": match.group(0).strip(),
                "block": shot_section[block_start:block_end].strip(),
            }
        )
    return shots


def extract_prompts(block: str) -> list[str]:
    matches = list(PROMPT_LABEL_RE.finditer(block))
    prompts: list[str] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        prompt = block[start:end].strip()
        prompt = re.sub(r"\s+", " ", prompt)
        if prompt:
            prompts.append(prompt)
    return prompts


def has_narration_line(block: str) -> bool:
    return bool(NARRATION_LINE_RE.search(block))


def extract_narration_line(block: str) -> str | None:
    match = NARRATION_LINE_RE.search(block)
    if not match:
        return None
    return re.sub(r"\s+", " ", match.group(1).strip().strip('"'))


def is_simple_card(prompt: str) -> bool:
    return bool(
        re.search(
            r"\b(?:date card|text card|title card|quote card|statistic card|map hold|diagram hold)\b",
            prompt,
            flags=re.I,
        )
    )


def simple_card_label(prompt: str) -> str | None:
    match = re.search(
        r"\b(date card|text card|title card|quote card|statistic card|map hold|diagram hold)\b",
        prompt,
        flags=re.I,
    )
    if not match:
        return None
    return match.group(1).lower()


def contains_any(prompt: str, terms: list[str]) -> bool:
    lower = prompt.lower()
    return any(term in lower for term in terms)


def prompt_body_after_style(prompt: str, selected_visual_system: str | None) -> str:
    body = prompt.strip()
    if selected_visual_system and body.lower().startswith(selected_visual_system.lower()):
        body = body[len(selected_visual_system) :].lstrip(" ,:-")
    return body.strip().lower()


def normalize_prompt_clause(value: str) -> str:
    value = value.lower().replace(chr(8217), "'")
    value = re.sub(r"'[^']+'|\"[^\"]+\"", "", value)
    value = re.sub(r"[^a-z0-9/\- ]+", " ", value)
    value = value.replace("-", " ")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def repeated_prompt_clauses(
    prompts: list[tuple[str, str]], selected_visual_system: str | None
) -> list[tuple[str, int]]:
    clause_counts: dict[str, int] = {}
    for _heading, prompt in prompts:
        body = prompt_body_after_style(prompt, selected_visual_system)
        for raw_clause in re.split(r"[,:;.]", body):
            clause = normalize_prompt_clause(raw_clause)
            if len(clause) < 35 or len(words(clause)) < 6:
                continue
            if any(
                re.search(pattern, clause, flags=re.I)
                for pattern in ALLOWED_REPEATED_CLAUSE_PATTERNS
            ):
                continue
            clause_counts[clause] = clause_counts.get(clause, 0) + 1

    if not prompts:
        return []
    threshold = max(12, int(len(prompts) * 0.20))
    repeated = [
        (clause, count)
        for clause, count in clause_counts.items()
        if count > threshold
    ]
    return sorted(repeated, key=lambda item: item[1], reverse=True)


def content_tokens(value: str) -> list[str]:
    tokens = [token.lower() for token in words(value)]
    return [token for token in tokens if len(token) > 2 and token not in STOPWORDS]


def approximate_phrase_position(script_tokens: list[str], phrase: str) -> int | None:
    phrase_tokens = content_tokens(phrase)
    if len(phrase_tokens) < 2 or not script_tokens:
        return None

    unique_phrase_tokens = set(phrase_tokens)
    if not unique_phrase_tokens:
        return None

    window_size = max(12, min(35, len(phrase_tokens) * 5))
    best_score = 0.0
    best_position: int | None = None
    if len(script_tokens) <= window_size:
        overlap = len(unique_phrase_tokens & set(script_tokens))
        best_score = overlap / len(unique_phrase_tokens)
        best_position = 0 if overlap else None
    else:
        for start in range(0, len(script_tokens) - window_size + 1):
            window = set(script_tokens[start : start + window_size])
            overlap = len(unique_phrase_tokens & window)
            score = overlap / len(unique_phrase_tokens)
            if score > best_score:
                best_score = score
                best_position = start + window_size // 2

    if best_position is None or best_score < 0.6:
        return None
    return best_position


def median(values: list[int]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    midpoint = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[midpoint])
    return (ordered[midpoint - 1] + ordered[midpoint]) / 2


def check_channel_identity_lock(text: str) -> list[str]:
    section = find_section(text, ["channel visual identity lock"])
    if not section:
        return []
    lower = section.lower()
    missing = [item for item in CHANNEL_LOCK_REQUIRED if item not in lower]
    if missing:
        return [
            "Channel Visual Identity Lock is missing required decision data: "
            + ", ".join(missing)
        ]
    return []


def lint(
    text: str,
    min_shots: int,
    target_duration_sec: int,
    max_shot_duration_sec: int,
    max_hook_duration_sec: int,
    hook_window_sec: int,
    max_average_duration_sec: float,
    min_prompt_words: int,
    min_variants_per_shot: int,
) -> list[str]:
    issues: list[str] = []
    all_headings = headings(text)

    for section in FULL_PACK_SECTIONS:
        if normalize_heading(section) not in all_headings:
            issues.append(f"Missing full production pack section: {section}")

    issues.extend(check_channel_identity_lock(text))

    if not has_character_section(all_headings):
        issues.append(
            "Missing primary character prompt or recurring character set section; "
            "include one or explicitly state why none is needed"
        )

    lean_escapes = [
        pattern for pattern in LEAN_ESCAPE_PATTERNS if re.search(pattern, text, flags=re.I | re.S)
    ]
    if lean_escapes:
        issues.append(
            "Lean-production escape detected; do not tell the user to expand the shot list later. "
            "Deliver the complete timed pack or split it into parts."
        )

    selected_visual_system = extract_selected_visual_system(text)
    if not selected_visual_system:
        issues.append("Selected visual system is missing or unreadable")

    shot_section = find_section(text, ["shot by shot image prompts"])
    if not shot_section:
        issues.append("Missing shot-by-shot image prompts section")
        return issues

    shots = split_shot_blocks(shot_section)
    if len(shots) < min_shots:
        issues.append(
            f"Shot list is too thin for the target runtime: {len(shots)} shots < {min_shots}"
        )

    if shots:
        last_end = max(int(shot["end"]) for shot in shots)
        min_end = int(target_duration_sec * 0.95)
        if last_end < min_end:
            issues.append(
                f"Shot list stops too early: last shot ends at {last_end}s < {min_end}s"
            )

        durations = [int(shot["duration"]) for shot in shots]
        average_duration = sum(durations) / len(durations)
        if average_duration > max_average_duration_sec:
            issues.append(
                "Shot pacing is too slow: "
                f"average shot duration {average_duration:.1f}s > {max_average_duration_sec:.1f}s"
            )

        long_shots = [shot["heading"] for shot in shots if int(shot["duration"]) > max_shot_duration_sec]
        if long_shots:
            preview = "; ".join(long_shots[:8])
            extra = "" if len(long_shots) <= 8 else f"; +{len(long_shots) - 8} more"
            issues.append(
                f"Regular shots exceed {max_shot_duration_sec}s and need splitting: {preview}{extra}"
            )

        long_hook_shots = [
            shot["heading"]
            for shot in shots
            if int(shot["start"]) < hook_window_sec
            and int(shot["duration"]) > max_hook_duration_sec
        ]
        if long_hook_shots:
            issues.append(
                f"Hook shots exceed {max_hook_duration_sec}s in the first {hook_window_sec}s: "
                + "; ".join(long_hook_shots[:8])
            )

        continuity_errors: list[str] = []
        for previous, current in zip(shots, shots[1:]):
            previous_end = int(previous["end"])
            current_start = int(current["start"])
            if abs(current_start - previous_end) > 1:
                continuity_errors.append(f"{previous['heading']} -> {current['heading']}")
        if continuity_errors:
            issues.append(
                "Shot timestamps have gaps or overlaps: "
                + "; ".join(continuity_errors[:6])
            )

    missing_narration = [shot["heading"] for shot in shots if not has_narration_line(str(shot["block"]))]
    if missing_narration:
        issues.append(
            "Shots are missing narration line/phrase coverage: "
            + "; ".join(missing_narration[:8])
            + ("" if len(missing_narration) <= 8 else f"; +{len(missing_narration) - 8} more")
        )

    narration_lines = [
        extract_narration_line(str(shot["block"]))
        for shot in shots
        if extract_narration_line(str(shot["block"]))
    ]
    if len(narration_lines) >= 50:
        unique_ratio = len(set(narration_lines)) / len(narration_lines)
        if unique_ratio < 0.85:
            issues.append(
                "Shot narration coverage repeats too much: "
                f"{len(set(narration_lines))}/{len(narration_lines)} unique narration lines. "
                "Shot phrases should track the script, not recycle earlier beats."
            )

        script_body = find_script_body(text)
        script_tokens = content_tokens(script_body)
        positions = [
            position
            for line in narration_lines
            if (position := approximate_phrase_position(script_tokens, line)) is not None
        ]
        if len(script_tokens) >= 700 and len(positions) >= 20:
            max_ratio = max(positions) / len(script_tokens)
            if max_ratio < 0.80:
                issues.append(
                    "Shot narration coverage stops before the script ending: "
                    f"latest matched shot phrase reaches only {max_ratio:.0%} of the script. "
                    "Final shots must cover the final reversal/payoff, not stretch early-script beats to the end."
                )

            tail_count = max(10, len(narration_lines) // 10)
            tail_positions = [
                position
                for line in narration_lines[-tail_count:]
                if (position := approximate_phrase_position(script_tokens, line)) is not None
            ]
            if tail_positions and median(tail_positions) / len(script_tokens) < 0.70:
                issues.append(
                    "Last shot prompts appear semantically out of sync with the ending: "
                    f"tail median phrase position is {median(tail_positions) / len(script_tokens):.0%} of the script."
                )
            if tail_positions:
                early_tail_positions = [
                    position for position in tail_positions if position / len(script_tokens) < 0.60
                ]
                if len(early_tail_positions) / len(tail_positions) > 0.25:
                    issues.append(
                        "Final shot prompts recycle early-script narration after the ending: "
                        f"{len(early_tail_positions)}/{len(tail_positions)} tail shots match before 60% of the script."
                    )

    low_variant_shots: list[str] = []
    all_prompts: list[tuple[str, str]] = []
    for shot in shots:
        prompts = extract_prompts(str(shot["block"]))
        if len(prompts) < min_variants_per_shot:
            low_variant_shots.append(str(shot["heading"]))
        all_prompts.extend((str(shot["heading"]), prompt) for prompt in prompts)

    if low_variant_shots:
        issues.append(
            f"Shots need at least {min_variants_per_shot} prompt variation(s): "
            + "; ".join(low_variant_shots[:8])
            + ("" if len(low_variant_shots) <= 8 else f"; +{len(low_variant_shots) - 8} more")
        )

    if not all_prompts:
        issues.append("No parseable prompt text found inside shot blocks")
        return issues

    if selected_visual_system:
        missing_style = [
            heading
            for heading, prompt in all_prompts
            if not prompt.lower().startswith(selected_visual_system.lower())
        ]
        if missing_style:
            issues.append(
                "Prompts do not consistently start with the selected visual system: "
                + "; ".join(missing_style[:8])
                + ("" if len(missing_style) <= 8 else f"; +{len(missing_style) - 8} more")
            )

    short_prompts = [
        heading
        for heading, prompt in all_prompts
        if len(words(prompt)) < min_prompt_words and not is_simple_card(prompt)
    ]
    if short_prompts:
        issues.append(
            f"Prompts are too thin (<{min_prompt_words} words) for production depth: "
            + "; ".join(short_prompts[:8])
            + ("" if len(short_prompts) <= 8 else f"; +{len(short_prompts) - 8} more")
        )

    simple_card_labels: dict[str, int] = {}
    for _heading, prompt in all_prompts:
        label = simple_card_label(prompt)
        if label:
            simple_card_labels[label] = simple_card_labels.get(label, 0) + 1
    simple_card_count = sum(simple_card_labels.values())
    if simple_card_count / len(all_prompts) > 0.40:
        preview = "; ".join(
            f"{label} appears {count}x"
            for label, count in sorted(simple_card_labels.items(), key=lambda item: item[1], reverse=True)[:4]
        )
        issues.append(
            "Too many prompts are labeled as simple cards or holds; do not use card/hold labels "
            f"to bypass prompt-depth requirements: {preview}"
        )

    missing_camera = [
        heading
        for heading, prompt in all_prompts
        if not contains_any(prompt, CAMERA_TERMS) and not is_simple_card(prompt)
    ]
    if missing_camera:
        issues.append(
            "Prompts are missing camera/framing/composition language: "
            + "; ".join(missing_camera[:8])
            + ("" if len(missing_camera) <= 8 else f"; +{len(missing_camera) - 8} more")
        )

    missing_emotion = [
        heading
        for heading, prompt in all_prompts
        if not contains_any(prompt, EMOTION_TERMS) and not is_simple_card(prompt)
    ]
    if len(missing_emotion) / len(all_prompts) > 0.25:
        issues.append(
            "Too many prompts lack emotional/narrative tension language: "
            + "; ".join(missing_emotion[:8])
            + ("" if len(missing_emotion) <= 8 else f"; +{len(missing_emotion) - 8} more")
        )

    missing_negative = [
        heading
        for heading, prompt in all_prompts
        if not re.search(r"\b(?:no|avoid|without|exclude)\b", prompt, flags=re.I)
    ]
    if len(missing_negative) / len(all_prompts) > 0.25:
        issues.append(
            "Too many prompts lack mistake-prevention constraints: "
            + "; ".join(missing_negative[:8])
            + ("" if len(missing_negative) <= 8 else f"; +{len(missing_negative) - 8} more")
        )

    lazy_prompts: list[str] = []
    for heading, prompt in all_prompts:
        if len(words(prompt)) > 45:
            continue
        if any(re.search(pattern, prompt, flags=re.I) for pattern in LAZY_LABEL_PATTERNS):
            lazy_prompts.append(heading)
    if lazy_prompts:
        issues.append(
            "Prompt-label laziness detected; replace broad labels with directed visual specifics: "
            + "; ".join(lazy_prompts[:8])
            + ("" if len(lazy_prompts) <= 8 else f"; +{len(lazy_prompts) - 8} more")
        )

    if selected_visual_system and len(all_prompts) >= 30:
        opening_counts: dict[str, int] = {}
        for _heading, prompt in all_prompts:
            body = prompt_body_after_style(prompt, selected_visual_system)
            for pattern in REPEATED_PROMPT_OPENINGS:
                if re.search(pattern, body, flags=re.I):
                    opening_counts[pattern] = opening_counts.get(pattern, 0) + 1
                    break

        repeated = [
            (pattern, count)
            for pattern, count in opening_counts.items()
            if count / len(all_prompts) > 0.20
        ]
        if repeated:
            preview = "; ".join(
                f"{pattern} appears {count}x" for pattern, count in repeated[:4]
            )
            issues.append(
                "Prompt template repetition detected; vary production roles and sentence openings "
                f"instead of repeating one A/B/C skeleton: {preview}"
            )

        repeated_body_patterns = []
        for pattern in REPEATED_PROMPT_BODY_PATTERNS:
            count = sum(
                1
                for _heading, prompt in all_prompts
                if re.search(pattern, prompt_body_after_style(prompt, selected_visual_system), flags=re.I)
            )
            threshold = 0.75 if "narration cue" in pattern else 0.25
            if count / len(all_prompts) > threshold:
                repeated_body_patterns.append((pattern, count))
        if repeated_body_patterns:
            preview = "; ".join(
                f"{pattern} appears {count}x" for pattern, count in repeated_body_patterns[:4]
            )
            issues.append(
                "Prompt body template repetition detected; prompts look mechanically generated "
                f"instead of shot-directed: {preview}"
            )

        rotating_fragment_patterns = []
        fragment_threshold = max(12, int(len(all_prompts) * 0.06))
        for pattern in ROTATING_FRAGMENT_BANK_PATTERNS:
            count = sum(
                1
                for _heading, prompt in all_prompts
                if re.search(pattern, prompt_body_after_style(prompt, selected_visual_system), flags=re.I)
            )
            if count > fragment_threshold:
                rotating_fragment_patterns.append((pattern, count))
        if len(rotating_fragment_patterns) >= 4:
            preview = "; ".join(
                f"{pattern} appears {count}x" for pattern, count in rotating_fragment_patterns[:5]
            )
            issues.append(
                "Rotating prompt-fragment bank detected; do not repair prompt depth by cycling "
                f"generic margin/corner/annotation suffixes: {preview}"
            )

        repeated_clauses = repeated_prompt_clauses(all_prompts, selected_visual_system)
        if repeated_clauses:
            preview = "; ".join(
                f"'{clause[:70]}...' appears {count}x"
                for clause, count in repeated_clauses[:4]
            )
            issues.append(
                "Repeated long prompt clauses detected; keep shared visual identity, but rewrite "
                "camera, object, action, and tension language per shot instead of using polished "
                f"A/B/C templates: {preview}"
            )

        padding_tails: dict[str, int] = {}
        for _heading, prompt in all_prompts:
            match = GENERIC_PADDING_TAIL_RE.search(prompt)
            if match:
                tail = re.sub(r"\s+", " ", match.group(1).strip().lower())
                padding_tails[tail] = padding_tails.get(tail, 0) + 1
        repeated_padding = [
            (tail, count)
            for tail, count in padding_tails.items()
            if count / len(all_prompts) > 0.20
        ]
        if repeated_padding:
            preview = "; ".join(
                f"'{tail[:80]}...' appears {count}x"
                for tail, count in repeated_padding[:3]
            )
            issues.append(
                "Generic prompt-padding suffix detected; revise prompts with shot-specific details "
                f"instead of appending the same validator words: {preview}"
            )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Production pack text/markdown file, or '-' for stdin")
    parser.add_argument(
        "--preset",
        choices=["standard-8"],
        default=None,
        help="Apply the default 8-minute production pack gate.",
    )
    parser.add_argument("--min-shots", type=int, default=70)
    parser.add_argument("--target-duration-sec", type=int, default=480)
    parser.add_argument("--max-shot-duration-sec", type=int, default=6)
    parser.add_argument("--max-hook-duration-sec", type=int, default=4)
    parser.add_argument("--hook-window-sec", type=int, default=60)
    parser.add_argument("--max-average-duration-sec", type=float, default=5.3)
    parser.add_argument("--min-prompt-words", type=int, default=36)
    parser.add_argument("--min-variants-per-shot", type=int, default=1)
    args = parser.parse_args()

    if args.preset == "standard-8":
        args.min_shots = max(args.min_shots, 90)
        args.target_duration_sec = 480
        args.max_shot_duration_sec = 6
        args.max_hook_duration_sec = 4
        args.hook_window_sec = 60
        args.max_average_duration_sec = 5.3
        args.min_prompt_words = max(args.min_prompt_words, 36)
        args.min_variants_per_shot = max(args.min_variants_per_shot, 1)

    if args.path == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.path).read_text(encoding="utf-8")

    issues = lint(
        text=text,
        min_shots=args.min_shots,
        target_duration_sec=args.target_duration_sec,
        max_shot_duration_sec=args.max_shot_duration_sec,
        max_hook_duration_sec=args.max_hook_duration_sec,
        hook_window_sec=args.hook_window_sec,
        max_average_duration_sec=args.max_average_duration_sec,
        min_prompt_words=args.min_prompt_words,
        min_variants_per_shot=args.min_variants_per_shot,
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
