#!/usr/bin/env python3
"""Fast health check for the YouTube Content Machine skill.

This intentionally avoids third-party dependencies such as PyYAML. It checks
that the skill's required files exist, the frontmatter has the minimum fields,
the reference files contain the production rules that have regressed before,
and the lint scripts can be executed.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "references/output-formats.md",
    "references/visual-systems.md",
    "references/selection-matrices.md",
    "references/channel-profiles.md",
    "references/core-workflow.md",
    "scripts/script_quality_lint.py",
    "scripts/production_pack_lint.py",
]

SKILL_REQUIRED_PHRASES = [
    "misconception map",
    "Script Control Brief",
    "Opening Attack Ladder",
    "Channel Visual Identity Lock",
    "full retention stack",
    "8 minutes as the monetization-ready floor",
    "lean shot list",
    "Existing-file honesty rule",
    "Premium prompt quality",
    "Pre-final completeness ritual",
    "production-pack file first",
    "Technical file-writing rule",
    "Loop-generated prompt packs",
    "prompt-depth validator fails",
    "File-backed assemblers are allowed",
    "cycling a bank of margin",
    "fixed lanes repeated",
]

OUTPUT_REQUIRED_PHRASES = [
    "Runtime compression rule",
    "8 minutes is the normal floor",
    "research sheet",
    "Do not label a compressed visual outline",
    "first 3 minutes",
    "Do not frame an existing validated file as newly generated content",
    "Premium variation rule",
    "Pre-delivery completeness check",
    "A short chat response",
    "Shot narration coverage",
    "code loops over arrays",
    "generic depth suffix",
    "Passing the word-count gate",
    "real estimated runtime",
    "bypass prompt-depth checks",
    "# Script` section must begin with the first spoken narration line",
    "one reusable template function",
    "generic validator phrases",
    "cycling a small bank",
    "fixed lanes repeated",
]

VISUAL_REQUIRED_PHRASES = [
    "Canon episode-level visual systems",
    "Hybrid Sketch System Map",
    "Evidence Board / Polaroid System",
    "Prompt Depth Standard",
    "Prompt depth is not the same as prompt quality",
    "validator-complete prompts",
    "semantically aligned",
    "Loop-generated prompts",
    "inflate weak prompts",
    "nearly every prompt as a \"diagram hold\"",
]

MATRIX_REQUIRED_PHRASES = [
    "Channel / Niche Visual Identity Matrix",
    "Shot Visual Type Matrix",
    "Pacing Density Matrix",
    "Human origins / ancient everyday systems",
    "Premium variation pattern",
]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_frontmatter(text: str) -> list[str]:
    issues: list[str] = []
    match = re.match(r"^---\s*\n(?P<body>.*?)\n---\s*\n", text, flags=re.S)
    if not match:
        return ["SKILL.md is missing YAML-style frontmatter"]
    frontmatter = match.group("body")
    for key in ("name", "description"):
        if not re.search(rf"(?m)^{key}\s*:\s*\S+", frontmatter):
            issues.append(f"SKILL.md frontmatter missing {key}")
    return issues


def check_phrases(label: str, text: str, phrases: list[str]) -> list[str]:
    lower = text.lower()
    missing = [phrase for phrase in phrases if phrase.lower() not in lower]
    if not missing:
        return []
    return [f"{label} missing required phrase(s): {', '.join(missing)}"]


def make_fixture() -> str:
    prompts = []
    style = "Hybrid Sketch System Map, ancient/system-map identity"
    prompt_sets = [
        (
            "belief-attack split frame, tight composition showing a crossed-out fish-for-grain trade beside a clay tablet clue, foreground red correction mark, background witness icons, skeptical tension, no realism, no 3D, no modern dollar signs",
            "object-clue close-up, cropped foreground detail of barley sack, cowrie shell, and tally mark with shallow-focus sketch depth, tiny label reading proof, anxious documentary mood, no modern objects, no fantasy architecture",
            "clean myth-versus-reality board, split comparison layout connecting barter, memory, and record arrows, centered composition with legible labels, corrective tension, no clutter, no photorealism",
        ),
        (
            "social-pressure tableau, side-view character action around a roof repair favor, neighbors watching from the background, obligation arrow returning later, warm but tense mood, no modern objects, no fantasy architecture",
            "witness-detail insert, close-up on hands passing a grain basket while tally marks appear in the foreground, background faces simplified into ink silhouettes, uneasy reciprocity tension, no glossy coins",
            "reciprocity loop map, overhead village layout connecting help, memory, reputation, and return arrows around tiny household figures, calm social tension, no clutter, no photorealism",
        ),
        (
            "route-map vignette, map-like river boundary composition with two unfamiliar groups exchanging salt and hides outside the trust circle, cautious tension, no modern market, no fantasy crowd",
            "exchange-object insert, close-up of salt bundle and hide placed on a boundary line, hands paused before contact, shallow-focus sketch emphasis, cautious pressure, no modern props",
            "threshold diagram, overhead route map showing barter as edge behavior between non-overlapping memory circles, clear labels and controlled negative space, corrective tension, no clutter",
        ),
        (
            "administrative proof scene, close desk-level composition around a clay tablet, reed stylus, barley ration bowl, and waiting worker figure, focused authority tension, no modern paperwork",
            "archive-artifact sketch insert, tight close-up of wedge-like tablet marks and silver weight icon with finger-shadow ink shading, documentary credibility mood, no fake readable paragraphs",
            "ledger-system diagram, overhead storehouse flow where goods enter, marks record, and claims leave as ration arrows, institutional pressure, no modern spreadsheet, no photorealism",
        ),
    ]
    for index in range(104):
        if index < 20:
            start = index * 3
            end = start + 3
        else:
            start = 60 + (index - 20) * 5
            end = start + 5
        start_time = f"{start // 60}:{start % 60:02d}"
        end_time = f"{end // 60}:{end % 60:02d}"
        a, b, c = prompt_sets[index % len(prompt_sets)]
        depth_suffix = (
            "off-white notebook paper texture, black ink linework, muted earth tones, "
            "simple role-based human figures, clear foreground and background separation, "
            "short readable labels"
        )
        prompts.append(
            f"""{index + 1}. {start_time}-{end_time}
Narration line: "A visible retention beat {index + 1} about trust, memory, and value."
Prompt A: {style}, {a}, {depth_suffix}.
Prompt B: {style}, {b}, {depth_suffix}.
Prompt C: {style}, {c}, {depth_suffix}.
"""
        )
    return f"""# Fixture Production Pack

## Title
Primary title: Fixture

## Runtime
Target runtime: 8 minutes
Word budget: 1,080-1,350

## Script Control Brief
Viewer starting belief: Before money was only barter.
Opening targets: barter myth.
Retention engine: scenes and proof.
Scene ladder: scene, conflict, record.
Re-hook plan: update every 20 seconds.
Forbidden drift: no article voice.

## Opening Attack Ladder
0:00-0:05: barter belief breaks.
0:05-0:15: proof appears.
0:15-0:30: object clue.
0:30-0:45: scale problem.
0:45-1:00: memory limit.

## Retention Beat Map
0:00-0:30: question, scene, reveal.
0:30-1:00: question, scene, reveal.
1:00-1:30: question, scene, reveal.
1:30-2:00: question, scene, reveal.
2:00-2:30: question, scene, reveal.
2:30-3:00: question, scene, reveal.
3:00-3:30: question, scene, reveal.
3:30-4:00: question, scene, reveal.
4:00-4:30: question, scene, reveal.
4:30-5:00: question, scene, reveal.
5:00-5:30: question, scene, reveal.
5:30-6:00: question, scene, reveal.
6:00-6:30: question, scene, reveal.
6:30-7:00: question, scene, reveal.
7:00-7:30: question, scene, reveal.
7:30-8:00: question, scene, reveal.

## Narrative Texture Rules
Scene rule: every paragraph has objects.
Model-drip rule: do not reveal too early.

## Channel Visual Identity Lock
Channel/niche identity: ancient systems explainer.
Default episode visual system: Hybrid Sketch System Map.
Identity preset name: Ancient/system-map identity.
Approved alternates: archive artifact inserts.
Style DNA: paper texture and black ink.
Thumbnail art DNA: object-first myth correction.
Forbidden drift: fantasy realism.

## Selected Visual System
Hybrid Sketch System Map, ancient/system-map identity

## Thumbnail
Thumbnail text options: NOT BARTER, BEFORE MONEY, MEMORY FIRST, NO COINS.

## Recurring Character Set
Ancient community member: sketch role figure in the selected visual system.

## Script
The answer you were taught is too neat.

The problem is not that barter never happened. It is that the barter story is incomplete. A village can hold memory, witnesses, gifts, grain, cattle, debt, and reputation before it needs coins. People hold objects, repair roofs, share food, record claims, measure grain, and watch who refuses to repay.

Then the group grows. Around 10,000 BCE, farming and storage make the social map larger. Around 3,000 BCE, Mesopotamian accounting shows records doing part of money's job. Around 600 BCE, coins arrive later as one shortcut, not the beginning of value.

So money did not invent value. It made memory portable, obligation transferable, and trust easier to move between strangers.

## Shot-By-Shot Image Prompts
{''.join(prompts)}

## SEO Meta Description
Fixture description.

## Hashtags
#Fixture

## Tags
fixture, money, history

## Research Material
Misconception map: barter, shells, coins.
Opening targets chosen: barter myth.
Sources used: fixture.
"""


def run_fixture_lints(root: Path) -> list[str]:
    issues: list[str] = []
    script_lint = load_module(root / "scripts/script_quality_lint.py", "script_quality_lint")
    sys.modules["script_quality_lint"] = script_lint
    production_lint = load_module(
        root / "scripts/production_pack_lint.py", "production_pack_lint"
    )
    fixture = make_fixture()

    script_issues = script_lint.lint(
        fixture,
        target_min=None,
        target_max=1350,
        min_beats=16,
        target_duration_sec=480,
    )
    production_issues = production_lint.lint(
        text=fixture,
        min_shots=90,
        target_duration_sec=480,
        max_shot_duration_sec=6,
        max_hook_duration_sec=4,
        hook_window_sec=60,
        max_average_duration_sec=5.3,
        min_prompt_words=36,
        min_variants_per_shot=3,
    )
    if script_issues:
        issues.append("script_quality_lint fixture failed: " + "; ".join(script_issues))
    if production_issues:
        issues.append(
            "production_pack_lint fixture failed: " + "; ".join(production_issues)
        )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=str(ROOT),
        help="Skill root directory. Defaults to the parent of this script directory.",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    issues: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).exists():
            issues.append(f"Missing required file: {relative}")

    if issues:
        print("FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1

    skill_text = read(root / "SKILL.md")
    output_text = read(root / "references/output-formats.md")
    visual_text = read(root / "references/visual-systems.md")
    matrix_text = read(root / "references/selection-matrices.md")

    issues.extend(check_frontmatter(skill_text))
    issues.extend(check_phrases("SKILL.md", skill_text, SKILL_REQUIRED_PHRASES))
    issues.extend(
        check_phrases("references/output-formats.md", output_text, OUTPUT_REQUIRED_PHRASES)
    )
    issues.extend(
        check_phrases("references/visual-systems.md", visual_text, VISUAL_REQUIRED_PHRASES)
    )
    issues.extend(
        check_phrases(
            "references/selection-matrices.md", matrix_text, MATRIX_REQUIRED_PHRASES
        )
    )
    issues.extend(run_fixture_lints(root))

    if issues:
        print("FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
