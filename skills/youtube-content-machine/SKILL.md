---
name: youtube-content-machine
description: Build, refine, and operate faceless YouTube content systems from raw ideas, channel concepts, niche notes, analytics lessons, or production requests. Use when Antigravity needs to help with YouTube channel creation, channel positioning, niche brainstorming, topic engines, video ideas, long-form or Shorts scripts, hooks, titles, thumbnails, SEO metadata, hashtags, tags, shot-by-shot script-to-image prompts, AI visual direction, production packs, or reusable content workflows. Especially use for human behavior/system-explanation channels, renewable or clean energy channels, historically centered technology channels, and any new niche where repeatable YouTube production is needed.
---

# YouTube Content Machine

## Operating Principle

Turn every YouTube request into a repeatable content machine, not a one-off answer. Preserve the user's current priority channels as strong examples, but do not hard-code the skill to those niches. Apply the same reasoning to any future channel by extracting its audience, promise, topic lanes, visual language, and production constraints.

When the user provides rough material, conversations, links, analytics lessons, or scattered notes, distill them into usable channel strategy, scripts, metadata, prompts, and next actions. Disagree with weak positioning, generic ideas, or low-retention packaging when needed.

## Start With The Request Type

Identify what the user is asking for:

- New channel brainstorm or validation.
- Existing channel strategy.
- Topic research or topic bank.
- Script only.
- Full production pack.
- Thumbnail/title/SEO metadata.
- Shot-by-shot image prompts.
- Primary character prompt for visual consistency.
- Visual style or prompt system.
- Performance diagnosis from analytics or competitor examples.

If the request is underspecified, ask only the questions needed to proceed. Prefer moving forward with reasonable assumptions and naming them.

## Question Policy

Ask intelligent questions when the answer would materially change the output:

- Which channel or niche is this for?
- Is this a Short, long-form video, or both?
- What target length should the script hit?
- Should the tone be documentary, intellectual, conversational, mysterious, urgent, or cinematic?
- Is the user asking for script only or the full production pack?
- Are current facts, statistics, companies, or timelines required?

Do not ask questions just to delay. If the user says "do the normal prep" or asks for a production pack, use the locked output format in `references/output-formats.md`.

## Core Workflow

1. Define or confirm the channel identity in one sentence.
2. **Topic Ideation & Suggestion Process**: When the user proposes a raw topic or asks for ideas, generate 3 distinct angles using the Content Engine templates (with clickable title, core hook attack, main tension/engine, and key visual scene each) and make a recommended selection. Do not proceed to full scripting until the topic's angle and core tension are locked.
3. Choose the content lane, angle template, or story type.
4. Build a misconception map before writing the hook: identify the viewer's likely wrong or incomplete answers, choose the strongest 2-3 to attack, then replace them with the stronger truth. For money/history/origin topics, attack the obvious folk answer before explaining.
4. After research and misconception mapping, write a Script Control Brief, Opening Attack Ladder, and Narrative Texture Rules that lock the angle, runtime, word budget, first-minute execution, re-hook plan, scene rules, model-drip, and forbidden drift before drafting.
5. Choose a Channel Visual Identity Lock, then package the video with title, alternatives, thumbnail text, and thumbnail prompt.
6. Add a primary character prompt or recurring character set before the shot list whenever named people, recurring hosts, mascots, historical figures, or repeated social roles appear.
6a. **Before writing any script, read `references/core-workflow.md` § Script Voice Standard, § Familiar Anchor Rule (Layer 4: Human Context), and § Altitude Shifting & Zooming Out.** Internalise the viewer-first hook rule, chronological escalation engine, conversational re-hook patterns, earned humor placement, stacked-timeline ending structure, the Familiar Anchor mapping system, altitude-shifting mini-documentary detour rules, and the forbidden moves list. Then write the script as a watching experience, not a reading experience. **For renewable/clean energy scripts specifically, also read `references/channel-profiles.md` § Renewable / Clean Energy / Storytelling Channels before writing** — it contains the full Writing Bible for that niche including the Layer 4 Familiar Anchor standard anchor mappings, the Human Voice Standard, the identified mistakes table, the Competitor Formula, the 30-Second Rule, and the North Star positioning.
6b. **Run the Script Voice Self-Audit Gate** immediately after the script is written and before any fact-checking or shot-by-shot work begins. Ask the seven gate questions (hook, chronological engine, scene test, re-hook test, forbidden moves, ending, article voice). Report the gate result. If any item fails, fix the script before proceeding. See `references/core-workflow.md` § Script Voice Self-Audit Gate.
6c. **Run the Fact-Check Gate** (see `references/fact-check.md`) after the script passes the voice audit and before shot-by-shot image prompt work begins. For factual, historical, science, archaeology, economics, or origin videos this gate is mandatory. Extract all specific claims, assign risk levels (✅ / ⚠️ / ❌), apply corrections, report results, and only proceed to shot-by-shot work after the gate passes.
7. Generate script-to-image prompts as tightly timed, standalone visual beats, not generic paragraph labels.
8. Add SEO description, hashtags, tags, and research material when the user wants upload-ready factual content.
9. Include edge cases, stronger alternatives, or warnings when the concept is weak.

Read these references as needed:

- `references/core-workflow.md` for universal channel and scripting rules, including the Script Voice Standard and Script Voice Self-Audit Gate.
- `references/channel-profiles.md` for priority channel profiles and niche-specific rules.
- `references/output-formats.md` for the exact production pack format.
- `references/visual-systems.md` for thumbnail and AI image prompt systems.
- `references/selection-matrices.md` for visual system, shot type, hook, narrative, research, thumbnail, pacing, and production-complexity selection.
- `references/fact-check.md` for the mandatory fact-check gate protocol, correction principles, and common failure patterns by content type.

For a full production pack, always read `references/output-formats.md`, `references/visual-systems.md`, and `references/selection-matrices.md` before writing. Do not rely only on this top-level file for shot-by-shot prompts.

Use validation scripts as pre-delivery tripwires when tools are available:

- `python skills/youtube-content-machine/scripts/script_quality_lint.py --preset standard-8 <file>` for substantial standard long-form scripts and script packs.
- `python skills/youtube-content-machine/scripts/production_pack_lint.py --preset standard-8 <file>` for standard long-form production packs with shot-by-shot prompts.
- `python skills/youtube-content-machine/scripts/quick_validate.py` for a fast local skill health check after updating the skill files.

For a full production pack in a tool-enabled Antigravity environment, create or update a markdown production-pack file first, then run the validators on that file before final delivery. Do not deliver a chat-only compressed pack unless the user explicitly asks for chat-only output. If chat-only output is required and the pack is too long, split it into numbered parts and continue instead of shrinking the shot list or omitting sections.

If generating directly in chat, save a temporary markdown copy and run the validators before delivery when possible. If tools are unavailable, manually apply the same gates. Passing a lint script does not prove the pack is good; failing it means revise before delivery.

Pre-final completeness ritual for every full production pack:

- Confirm the pack has every required section from `references/output-formats.md`.
- Confirm the script's actual word count and runtime estimate match the stated target band.
- Confirm the Retention Beat Map reaches the target runtime and audits the first 3 minutes, middle, and ending.
- **Confirm the Script Voice Self-Audit Gate was run and passed.** If not, run it now against the seven gate questions before proceeding. See `references/core-workflow.md` § Script Voice Self-Audit Gate.
- **Confirm the Familiar Anchor Gate was run and passed.** Scan the script: every major technical concept must have a Familiar Anchor (everyday experience, school lesson, older technology, or historical precedent). Any section lacking one must be revised before delivery. See `references/core-workflow.md` § Familiar Anchor Rule for the gate output format.
- **Confirm the Fact-Check Gate was run and passed.** If not, run it now before proceeding. See `references/fact-check.md` for the full protocol and output format.
- Confirm the shot list covers the whole runtime with the expected density. Shots ≤3 seconds get 1 prompt. Shots 5-8 seconds may be split into 2-3 individual prompts depending on the narration content.
- Confirm character prompts, thumbnail prompts, and shot prompts all use the same selected visual system and identity preset.
- Confirm prompt variations change production role, not only camera distance.
- Run `production_pack_lint.py` and `script_quality_lint.py`; revise before final if either fails.
- **Confirm the Familiar Anchor Gate was run.** Scan the script: every major technical concept must have a Familiar Anchor (everyday experience, school lesson, older technology, or historical precedent). Any section lacking one must be revised before delivery.
- In the final response, report the file path, whether it was fresh generation/revision/validation, validator results, voice audit gate result, fact-check gate result, and Familiar Anchor gate result. Do not call the work done if the pack is only a partial script, light metadata, or a prompt outline.

Technical file-writing rule:

- Prefer `apply_patch` or the normal workspace shell path for markdown production-pack files.
- Do not use the Node REPL to write directly into the workspace or `C:\tmp`; in restricted Antigravity sessions it may be read-only there. If Node is needed for generation or analysis, write only to `nodeRepl.tmpDir`, then bridge through the workspace shell, or regenerate through the shell path.
- Do not dump huge generated markdown through an inline `node -e` or here-string script unless there is no safer path. It hides quoting errors and encourages loop-generated creative content.
- File-backed assemblers are allowed for safe writing, counting, or stitching already-written material, but they must not generate creative A/B/C shot prompts from one template function over an array of beats. Remove temporary generator/assembler helpers before final delivery unless the user explicitly asked to keep the tool.

Existing-file honesty rule:

- If a matching production pack already exists, inspect it before overwriting, but be explicit about whether you are reusing, validating, revising, or creating fresh content.
- Do not claim "I generated" or "I prepared" a new pack if the work was mainly validating an existing compliant file.
- If the user is testing whether the skill can generate fresh output, create a new draft path or clearly state that the existing file would make the test a false positive.
- A fresh-generation test must not silently reuse an already-fixed production pack as the output. Use a new draft filename, a timestamped scratch file, or an explicit "reference only" statement.

Production pack hard gates:

- Standard long-form treats 8 minutes as the monetization-ready floor, not a rigid ceiling. The normal band is about 8:00-9:30, and 9-10+ minutes is acceptable when the research sheet, outline, and retention map genuinely justify the extra material.
- Runtime quality matters more than exact duration. Slight or moderate overshoot is acceptable when it comes from necessary proof, scenes, chronology, or payoff. Excessive overshoot caused by jargon, repeated explanation, filler, duplicated lists, or soft essay bridges must be cut.
- Do not pretend a 1,500+ word script is an 8-minute script. If a topic honestly needs that length, label the target as 10-12 minutes, strengthen the retention map, and expand the visual plan accordingly.
- The hook must attack the viewer's likely wrong belief or incomplete answer in the first 5-10 seconds.
- The first minute must follow an Opening Attack Ladder with 4-6 micro-beats, not a calm setup paragraph.
- The script must feel like a watching experience: scenes, objects, conflicts, people, dates, visible systems, and pressure points, not an article made of truth paragraphs.
- The script must follow Narrative Texture Rules so the voice avoids robotic essay phrasing, repeated abstract summaries, and generic bridges.
- Critiques must audit the full retention stack, not only the intro: opening attack, first 3 minutes, middle re-hooks, ending payoff, runtime math, visual density, prompt depth, timestamp coverage, and metadata/thumbnail consistency.
- Cutting down an overshot script is not automatic. First decide whether the extra runtime is justified by the research and outline. If it is bloat, remove repeated explanation, duplicated thesis lines, soft bridges, and redundant lists before cutting proof objects, conflict scenes, re-hook questions, timeline anchors, or payoff lines.
- The Channel Visual Identity Lock must define channel/niche identity, default visual system, identity preset name, approved inserts, style DNA, thumbnail DNA, and forbidden drift for the channel or niche.
- The shot list must cover the full runtime with directed visual beats. For an 8-minute production pack, use enough shots to support 2-4 second hook pacing and 3-6 second main pacing. Do not compress the video into 20-30 broad prompts.
- Select one canon episode visual system and one identity preset, then vary the video through shot visual types. Do not invent random visual systems when a preset, shot type, insert, or prompt variation solves the need.
- Premium prompt quality requires variety inside consistency: rotate shot types, camera language, visual function, object focus, and emotional staging. Do not repeat the same A/B/C prompt skeleton across the whole shot list.
- Prompt variations must change execution meaningfully: one may be a literal action scene, one an object/evidence insert, and one a system/timeline/map view, but the wording, composition, and visual role must feel bespoke to that narration beat.
- Do not author final shot prompts by looping over arrays of phrases, nouns, actions, and emotions. Scripts may help count, validate, or transform already-written material, but the creative shot list must be written and revised as script-aligned visual beats. Loop-generated prompt packs are not 9/10 output.
- Do not make A/B/C variants fixed lanes repeated across the whole pack, such as every B prompt becoming a top-down map and every C prompt becoming a diagram layout. Vary the visual role only when the narration beat calls for it.
- If a prompt-depth validator fails, do not mechanically append the same suffix to every prompt, such as "visible social pressure," "object-specific historical details," or "foreground-background clarity." Fix each weak shot by adding the specific object, action, setting, framing, evidence, or tension that belongs to that narration beat.
- Do not repair prompt-depth failures by cycling a bank of margin, corner, annotation, witness-mark, or map/tally fragments across prompts. That is still loop-generated filler even when each suffix mentions the narration phrase.
- Thumbnail prompts must follow the same visual identity lock unless the channel has a deliberately separate thumbnail brand.
- Every shot must include timestamp range, narration line or phrase covered, and image prompt variations unless the user explicitly asks for single-prompt output.
- Character prompts must match the selected visual system exactly. Sketch shots need sketch character prompts; cinematic documentary shots need cinematic documentary character prompts; stick-drawing shots need stick-drawing character prompts.
- If the complete shot list is too long for one response, split the production pack into parts instead of reducing prompt count, prompt depth, timestamps, or variations.
- A "lean shot list," "editor-ready outline," or note telling the user to expand prompts later is not a completed full production pack.
- A response containing only titles, a short script, thumbnail text, SEO metadata, and research anchors is not a full production pack, even if it says it used the workflow.

## Quality Bar

Favor:

- Clear channel promise.
- Repeatable angle systems over random topic lists.
- Tension, specificity, and curiosity.
- Real names, dates, locations, companies, numbers, and timelines when the niche requires factual authority.
- A researched or inferred misconception map for factual, historical, science, finance, system, and explainer topics.
- A clear target runtime, target word count, and maximum word count for long-form scripts.
- **Numbers and Figures Formatting Rule**: Always write numerical statistics, capacities, temperatures, and voltages as digits/figures (e.g., 66,000 volts, 23,500 times, 2.9-gigawatt) rather than words. Never spell them out. This keeps the figures visual, readable for subtitles, and easy to translate into video text overlays.
- A Script Control Brief before every substantial script so the output follows the chosen retention architecture.

- Visual prompts with action, framing, props, period/domain details, emotional tension, and mistake-prevention constraints.
- Literal/simple image prompts when the script only needs text, a plain object, or a simple interaction.
- Character consistency prompts for named people, recurring people, and repeated social-role archetypes.
- Familiar Anchors: every technical or complex concept bridged to something the viewer already knows (school lesson, everyday experience, older technology, historical precedent) before the formal explanation.
- Altitude shifts: regularly zoom in to specific objects/projects and zoom out to history, physics, economics, or geography to prevent a flat single-perspective feeling.
- Simple production that can be executed quickly.

Avoid:

- Generic educational lectures.
- Starting with definitions.
- Starting with an imagined scenario when the topic has a stronger misconception to destroy first.
- Leaning only on the user's notes for the hook instead of independently identifying audience misconceptions.
- Drafting the script before the Script Control Brief is clear.
- Writing a reading experience instead of a watching experience.
- Abstract truth paragraphs that summarize the model before the viewer has seen the scenes that prove it.
- Abstract titles that sound clever but are not clickable.
- AI essay voice.
- Overly complex production.
- Forcing every image prompt to be cinematic or elaborate.
- Paragraph-to-image prompting when shot-based pacing is needed.
- Hard-coding one niche as the only valid use case.

## Default Assumptions

If not specified:

- Standard long-form target length is normally at least 8 minutes, with a common 8:00-9:30 delivery band. Use 9-10+ or 10-12 minutes when the topic has enough real talking points and retention beats; use shorter only when the topic cannot honestly sustain 8 minutes or the user asks for a shorter format.
- Shorts target structure is hook, setup, tension, payoff, ending.
- Voice is calm, serious, documentary, and not hype-driven.
- Visuals should be AI-first, controlled, and consistent.
- The output should be practical enough for immediate production.
