# Output Formats

## Full Production Pack

Use this when the user asks for the normal prep, upload-ready material, full package, production pack, or anything similar.

In a tool-enabled Antigravity environment, make the production pack file-backed by default. Create or update a markdown file, run the validators, then summarize the result to the user with the file path. A short chat response with a script and light metadata is not a completed production pack.

Return:

1. Title and alternative titles.
2. Runtime target, word budget, and estimated runtime.
3. Script Control Brief.
4. Opening Attack Ladder.
5. Retention Beat Map.
6. Narrative Texture Rules.
7. Channel Visual Identity Lock.
8. Draft script diagnosis, when the user provides an existing script.
9. Selected visual system for this episode, with a short reason.
10. Thumbnail text and thumbnail image prompts.
11. Primary character image prompt or recurring character set, when a person, recurring figure, repeated archetype, mascot, or historical individual appears.
12. Script only, with no image prompts inside the script.
13. Shot-by-shot script-to-image prompts.
14. SEO meta description.
15. Hashtags.
16. Tags.
17. Research material with source links and key facts used, when the topic is factual or historical.

Do not make the pack look complete by compressing production data. A full pack with script-to-image prompts must preserve runtime math, shot density, prompt depth, and timestamp coverage. If the answer becomes too long, split it into parts and continue the shot list in the next part.

If a file with the same topic/title already exists, state whether the output is an existing pack validation, a revision, or a fresh generation. Do not frame an existing validated file as newly generated content. For fresh-generation tests, write to a new draft file or explicitly say the existing file is being used as a reference.

Pre-delivery completeness check:

- All required sections are present as clear markdown headings.
- Runtime target, word budget, actual or estimated word count, and estimated runtime agree with each other.
- Script Control Brief, Opening Attack Ladder, Retention Beat Map, and Narrative Texture Rules appear before the script.
- Retention Beat Map reaches the stated runtime and includes first-minute pressure, first-3-minute escalation, middle re-hooks, and ending payoff.
- If the script estimate or shot timeline runs longer than the nominal target, extend the Retention Beat Map to the real estimated runtime instead of stopping at 8:00 by habit.
- Channel Visual Identity Lock includes default visual system, identity preset, approved inserts, style DNA, thumbnail DNA, and forbidden drift.
- Selected Visual System includes a canon system plus identity preset, not only a broad system name.
- Recurring character set or primary character prompt is included when repeated people or roles appear.
- Shot-by-shot prompts cover the entire runtime with timestamps and narration phrase coverage. Standard shots (≤3 seconds) get exactly one prompt. Longer narration lines (5-8 seconds) are split into 2-3 individual timed prompts based on what is being spoken about (e.g. 2s+2s+2s or 4s+3s or 4s+4s). Splits are used for emphasis, deep emotion, or scenes with visual progression.
- Shot narration coverage follows the actual script sequence: hook shots cover the hook, middle shots cover the middle, and final shots cover the final reversal or payoff.
- A/B/C prompt variations for any shots where multiple options are provided change production role, object focus, scene function, or visual metaphor, not only camera distance.
- SEO description is minimum 250-400 words (not a short paragraph summary). Must include the hook/setup, core reversal, modern connection, topic timestamps, and resources section.
- `script_quality_lint.py` and `production_pack_lint.py` pass when tools are available.

Never finish with phrases like "this can be expanded into shots later" for a requested full pack. Split the pack, continue in a file, or say the output is incomplete.

## Title Section

Include one primary title and 3-8 alternatives.

Prioritize curiosity, specificity, and tension. Avoid clever abstractions that reduce clickability.

When a topic contains a concrete weird detail, lead with that detail. Prefer a title built around the weird number, time gap, cost, scale, or impossible-sounding result over a broad category title. The title should make the viewer ask why or how before the video starts.

## Thumbnail Section

Include:

- Thumbnail text: at least 4 variations per thumbnail image variation.
- Thumbnail image prompts: provide multiple image variations when useful for A/B testing.
- Recommendation: name the best thumbnail text + image pairing and explain why.

The thumbnail should communicate the story before the viewer reads the title.

Prefer the strongest curiosity element over a broad theme. Numbers, contradictions, rejection, impossible scale, and private-use surprises often beat general labels.

Thumbnail text should be short, usually 2-6 words, but never provide only one option. If there are 3 image prompt variations, provide at least 4 text options for each variation.

Recommendation logic:

- Prefer the clearest curiosity object.
- Prefer concrete numbers, contradictions, and emotional labels.
- Avoid clever wording that hides the story.
- Explain the recommendation in one sentence.

Thumbnail prompts must follow the Channel Visual Identity Lock. If the channel uses Hybrid Sketch System Map, the thumbnail should not suddenly become cinematic realism unless the channel has explicitly approved separate thumbnail branding. Thumbnail art may be more contrast-heavy than the video, but it must share the same visual world, recurring anchors, and forbidden-drift rules.

## Draft Script Diagnosis

When the user provides a script or draft, do not simply repackage it. First critique it against the channel's standards.

Include:

- What works.
- What does not fit the channel style.
- Which likely viewer misconceptions the current intro attacks or fails to attack.
- Whether the intro fits the preferred hook pattern.
- Whether the script feels like a watching experience or a reading experience.
- Estimated word count and runtime versus the target runtime.
- Where the script lacks 20-30 second re-hook loops, pressure points, scenes, proof teases, or mid-body belief updates.
- Whether the story has enough tension, contrast, and payoff.
- Whether the first 3 minutes, middle section, and ending each keep retention pressure or only the intro works.
- Whether the visual pack supports retention with dense shot timing, deep prompts, and full narration coverage.
- Whether runtime cuts would damage quality or only remove repeated explanation.
- What must be corrected before production.

Then rewrite or package the script using those corrections.

## Script Control Brief

Include this before writing the script for substantial long-form videos. It should guide the script, not become narration.

Return:

- Topic promise.
- Target runtime and word budget.
- Content type.
- Viewer starting belief.
- Opening targets.
- Core replacement idea.
- Retention engine.
- Scene ladder.
- Re-hook plan.
- Forbidden drift.
- Ending target.

## Opening Attack Ladder

Include this after the Script Control Brief for every substantial script. This is the first-minute execution plan, not a generic hook note.

Return 4-6 timestamped micro-beats:

- `0:00-0:05`: the exact belief, assumption, object, number, date, contradiction, or visible situation that starts the video.
- `0:05-0:15`: the first attack or complication.
- `0:15-0:30`: the proof tease, object, scene, or reason the viewer's answer is incomplete.
- `0:30-0:45`: the second misconception or deeper question.
- `0:45-1:00`: the promise of the real engine without fully explaining it.

The ladder must use the topic's native world. Do not use generic salary, office, contract, wage, task, or modern admin examples unless the topic itself is about those things.

Do not default to the exact phrase "Most people think..." Use it only when it is truly the fastest cleanest attack. Prefer object contradiction, date inversion, visible scene contradiction, strange evidence, or a direct correction when possible.

## Retention Beat Map

Include this before the script for substantial long-form videos. It proves the script has enough pressure points to sustain the target runtime.

For each beat, include:

- Timestamp range.
- Viewer question or pressure point.
- Scene, object, person, date, place, conflict, or proof shown.
- Mini-reveal or belief update.

For an 8-minute script, provide about 16-24 beats and make the final beat reach the target runtime. If the beat map feels repetitive, under-built, or stops early, revise it before writing the script.

## Narrative Texture Rules

Include this before the script as a short, episode-specific writing control. It must prevent the script from reading like an article.

Return:

- Voice texture: how the narration should sound.
- Sentence rhythm: how to mix short pressure lines with fuller scene paragraphs.
- Scene rule: what must be visible in most paragraphs.
- Re-hook rule: what kind of viewer update appears every 20-30 seconds.
- Forbidden phrases or moves: topic-specific versions of article voice, generic bridges, weak summaries, and early full-model reveals.
- Model-drip rule: what truth must be delayed until scenes earn it.

## Channel Visual Identity Lock

Include this before selecting thumbnails or shot prompts. Use `selection-matrices.md` to choose it.

Return:

- Channel/niche identity.
- Default episode visual system.
- Identity preset name.
- Approved alternates or inserts.
- Style DNA: texture, line style or lighting, palette, character treatment, object treatment, label treatment.
- Thumbnail art DNA: composition, text behavior, recurring symbols, contrast style.
- Forbidden drift.

The Selected Visual System must follow this lock. A shot prompt or thumbnail prompt that violates the lock should be rewritten before delivery.
Do not deliver a broad system name without an identity preset. For example, write "Hybrid Sketch System Map, modern institution map identity" or "Cinematic Documentary System, modern lab/product identity," not only "Hybrid Sketch System Map" or "Cinematic Documentary System."

## Selected Visual System

Before image prompts, choose the best visual system and identity preset for the episode and say why. Use `selection-matrices.md` to make the choice, then keep that system stable across the character prompt, thumbnail prompts, and shot list.

Do not default to generic prompts. Select the visual system based on the script's subject:

- Editorial Diagram System: best for clean conceptual explanations.
- Notebook Sketch System: best for deep theory, origin questions, and reflective sections.
- Social Comic System: best for human interaction, emotion, social pressure, and dialogue.
- Hybrid Sketch System Map: best for historical progression, system evolution, trust networks, behavior loops, and concepts that need both narrative and diagrams.
- Cinematic Documentary System: best for historical people, inventions, projects, companies, and physical technology.
- Evidence Board / Polaroid System: best for mystery, investigation, forgotten history, hidden connections, and research-driven stories.

If the user suggests a visual system and it fits, use it. If a different system is stronger, say so and explain.

Do not invent a new episode-level visual system unless the topic truly cannot fit one of the six canon systems. When variety is needed, choose different shot visual types inside the selected system.

## Script Section

Write the script cleanly without image prompts. If timestamps are useful, include them. If the user asked for a Short, write tightly for the requested length.

State runtime data in the Runtime section or immediately before the Script heading, not inside the `# Script` section. The `# Script` section must begin with the first spoken narration line.

Runtime data to state before the script section:

- Target runtime.
- Target word count range.
- Actual or estimated word count.
- Estimated runtime using 195 words per minute (3.25 words per second) as the default calibrated pace.

If the script exceeds the chosen target by more than 10%, audit before cutting. Cut only when the excess is caused by bloat, filler, repeated explanation, weak bridges, or duplicated points. If the extra runtime is justified by the research sheet, outline, proof scenes, chronology, or payoff, update the target runtime honestly and strengthen the retention and visual plan instead of forcing the script down.

For a standard long-form script, 8 minutes is the normal floor, not a hard ceiling. A delivery around 8:30 or close to 9 minutes is usually fine. Some topics should run 9-10+ or 10-12 minutes when the research and outline genuinely support that length. Do not call a 1,500+ word script an 8-minute pack; declare the longer target and make sure the retention beat map and shot list scale with it.

Runtime compression rule:

- Cutting a script should make it sharper, not thinner.
- Do not cut just because the runtime passes 8 minutes. First ask whether the extra time comes from necessary talking points or from bloat.
- Cut repeated thesis statements, duplicated lists, generic bridges, and already-proven explanations first.
- Preserve hook attacks, proof scenes, conflict moments, re-hook questions, timeline anchors, object clues, and ending payoff.
- If a cut removes a retention pressure point, replace it with a shorter pressure point rather than leaving a smooth article paragraph.

The script should preserve:

- Hook.
- Setup.
- Tension.
- Payoff.
- Present-day or system connection.

## Primary Character Image Prompt Or Recurring Character Set

Include this section before the shot-by-shot prompts whenever the video has a main historical figure, recognizable person, recurring presenter, mascot, recurring fictional character, or repeated social-role archetype.

- **Strict Markdown Formatting & Spacing Rules**:
  - **Never** bunch distinct descriptions, character profiles, or lists into a single continuous paragraph.
  - Every character profile in a recurring character set must be written as a separate block element. Use clear bullet points (`- **[Character Name]**: [Description]`) or sub-headings (`### [Character Name]`) with empty lines before and after.
  - Apply this clean spacing throughout the entire production pack: ensure headings, paragraphs, list items, and shots are separated by double line breaks (`\n\n`) so the document is highly readable.

Purpose: give the user a stable reference image prompt they can generate once and reuse for consistency across the video.

For system-history, human-behavior, faceless documentary, or explainer videos that repeatedly show the same type of person across shots, create a recurring character set even when there is no single named protagonist. Define only the archetypes needed for continuity, such as "ancient community member," "outsider trader," "temple scribe," or "modern viewer."

The character prompt must use the same visual system selected for the episode and the same style layer as the shot-by-shot prompts. If the shot list uses stick drawing, character prompts must be stick drawing. If the shot list uses cinematic documentary realism, character prompts must use cinematic documentary realism. If the shot list uses Evidence Board / Polaroid, character prompts must be written for that visual world. Do not mix a realistic character prompt with sketch, diagram, comic, or stick-drawing shot prompts.

For historical or renowned individuals:

- Research what the person looked like using public, factual references.
- Describe age range, hair, facial hair, face shape, clothing era, and defining non-copyrightable traits.
- Avoid copying a specific copyrighted photograph, portrait composition, illustration style, or living artist's style.
- Phrase the prompt as a historically grounded character design, not a replica of a specific image.
- Mention uncertainty when visual references conflict or are limited.

For fictional or generic recurring characters:

- Define stable age, build, hair, clothing, expression range, and color palette.
- Keep the description reusable across shots.

Every later shot featuring the same character should reuse the same character description or refer to it explicitly.

## Shot-By-Shot Image Prompts

Do not map prompts mechanically paragraph by paragraph. Use timed shots like a documentary director.

- **Calibrate Timestamps to Word Count**: Never assign arbitrary shot durations that ignore actual narration length. Compute shot duration dynamically using the default pace of 195 WPM (3.25 words per second):
  `Shot Duration (seconds) = Word Count of Narration / 3.25`.
  Ensure timestamps accurately match the duration needed to speak the covered narration phrase.
- **Visual Simplicity & Director's Mindset**: Keep prompts simple and straight to the point. Avoid visual noise, bloat, or over-crowding in scenes. For conceptual or negative statements (e.g., "wrong", "failure", "30 million years ago"), use clean visual layouts (text cards, simple diagrams, map outlines, cancel cross overlays) rather than complex characters and backgrounds.
- **Mandatory `, no text` Suffix**: For all prompts that are not explicit text cards or labelled diagrams, append `, no text` (or `, no texts`) at the end of the prompt to prevent the image generator from adding gibberish text.
- **Ban Workflow Placeholders**: Never include index step markers, shot counts, or loop counters (e.g., "point 20," "step 20," "shot 15", "cycle 7", "loop 7") inside the prompt text. The prompt must describe only visible elements.
- **Split Pacing and Spacing Rules**:
  - A standard narration line of approximately 3 seconds gets **exactly one image prompt**. Do not generate A/B/C variants for standard lines unless explicitly requested.
  - Longer narration lines of 5-8 seconds must be split into 2-3 separate timed prompt segments (e.g., 2s x3 or 4s + 3s) based on the visual progression of the text.
  - Every shot block must use double line breaks (`\n\n`) to separate the timestamps, narration line, and individual prompts (e.g., separating Prompt A, Prompt B, and Prompt C with empty lines) to ensure the document is highly readable and easy to scan.

Each shot should include:

- Timestamp range.
- Narration line or phrase covered by the shot.
- Image prompt.

Multiple shots may cover one sentence when pacing requires it.

After generating the shot list, audit semantic alignment against the script. The final 10-15 shots must cover the script's ending, not recycled phrases from the first half.

For long-form videos, when prompt variations are requested, provide 3 image prompt variations per shot for A/B testing, keeping them separated by blank lines. Vary framing, style layer, or visual metaphor while preserving the same narration beat and channel identity.

Premium variation rule:

- A/B/C variations should not be the same prompt sentence with only "medium shot," "close-up," and "overhead" swapped in.
- Give each variation a different production role, such as literal character action, object/evidence insert, system diagram, map/timeline view, split comparison, archive artifact, emotional reaction, or final synthesis.
- Do not turn A/B/C into fixed lanes repeated across the whole pack, such as every A being a literal scene, every B being a top-down map, and every C being a diagram layout. Choose the three variants from the needs of that narration beat.
- Rotate the wording and composition across the shot list so the prompts feel directed by the narration, not generated from one repeated template.
- If the same opening phrase appears across many prompts, rewrite the set with more varied shot types before delivery.
- Do not generate prompts by cycling a small grammar such as "literal scene," "object-led insert," and "system-map diagram" across every shot. That creates validator-complete but editor-weak prompts.
- Do not use code loops over arrays of narration phrases, nouns, actions, frames, labels, or emotions to create the final shot list. That produces surface variety while keeping the same prompt skeleton. Use scripts only for counting, validation, or cleanup after the shot prompts are genuinely written.
- A file-backed assembler may stitch or count already-written prompt material, but it must not create A/B/C prompts from one reusable template function over a beat array. Delete temporary assembler/generator helpers before final delivery unless the user explicitly asked to keep them.
- Do not repair thin prompts by appending the same generic depth suffix to every line. Phrases like "visible social pressure," "object-specific historical details," and "foreground-background clarity" are not substitutes for naming the actual object, action, framing, evidence clue, setting, and tension of that shot.
- Do not satisfy camera/emotion/depth gates by rotating generic validator phrases such as "explicit emotional tension," "under visible pressure," "precise historical props," "medium visual density," or "specific to this beat." Replace them with shot-specific emotion, composition, props, and stakes.
- Do not repair prompt-depth failures by cycling a small bank of margin/corner/annotation fragments across prompts, even if each suffix repeats the narration phrase. Add new shot-specific evidence, action, framing, or stakes instead.
- Do not label most prompts as "diagram hold," "map hold," "text card," or "title card" to bypass prompt-depth checks. Hold/card labels are for deliberate pacing beats, not the default state of a full shot list.

Long-form script-to-image ratio:

- Do not use one prompt per large script section.
- Treat each visual beat as a shot.
- Hook sections should usually change visuals every 2-4 seconds.
- Main explanation sections should usually change visuals every 3-4 seconds.
- A 5-6 second shot is only acceptable when it is a deliberate emphasis moment, emotional pause, statistic card, date card, map hold, diagram hold, or visual idea that needs time to sink in.
- If a regular narration beat is longer than 5-6 seconds, split it into two or more image prompts. For example, 6 seconds can become 3+3, 7 seconds can become 4+3, and 8 seconds can become 4+4.
- No single prompt should cover more than about 6 seconds unless there is a clear retention reason. If a longer timestamp is unavoidable, create multiple numbered prompts inside that timestamp instead of one generic prompt.
- An 8-minute standard video should normally produce roughly 90-120 visual beats when delivered as a true shot-by-shot pack. Longer videos may need more.
- If the full shot list would be too long for one response, split it into parts instead of compressing it into a thin shot list.
- Never turn an 8-minute video into 20-30 broad visual prompts. That is a chapter outline, not a shot list.
- Do not label a compressed visual outline as a full pack by saying the user can expand it later. That is a failed production pack. Split the delivery into parts instead.

Every image prompt must answer:

1. What is visually happening?
2. How is it framed?
3. What emotional tension is present?
4. What props, setting, or details make the concept clear?

Prompts must be production-ready visual instructions, not labels. Include visual system, exact subject, visible action, period or domain context, composition, framing, setting, props, style texture, emotional tone, important labels/text, and negative constraints where needed.

The AI image generator does not know the script. Each image prompt must stand alone. Do not assume the generator knows the topic, timeline, place, product, object, character, emotional context, visual system, or surrounding narration.

Every prompt must use domain-specific specificity. Do not use a broad category word when the scene needs a precise object, environment, interface, machine, material, person type, document, currency, tool, product, or visual state.

For example:

- Do not write "money" when the scene needs a specific currency, value object, ledger, banknote, coin, shell, grain store, card payment, or digital balance.
- Do not write "technology" when the scene needs a battery cell, wind turbine nacelle, transformer, GPU rack, satellite, robotic arm, or lab prototype.
- Do not write "company" when the scene needs a boardroom, factory floor, warehouse, retail shelf, investor deck, earnings chart, or product launch stage.
- Do not write "people" when the scene needs a tired founder, skeptical engineer, anxious customer, village elder, factory worker, student, doctor, trader, or executive.
- Do not write "place" when the scene needs a desert solar farm, cramped apartment, ancient village, modern server room, city street, courtroom, classroom, clinic, or port.

For any prompt involving period, location, technology level, culture, industry, interface, clothing, architecture, tools, documents, data, or physical objects, define the exact context needed for the shot. The prompt should prevent the generator from filling gaps with generic stock imagery, wrong-era details, vague AI-history visuals, random futuristic objects, or incorrect modern elements.

Every generated prompt should include:

1. Visual system or style layer.
2. Exact subject and action.
3. Time period, location, industry, social setting, or domain context when relevant.
4. Composition and camera/framing.
5. Props, clothing, interface details, tools, setting, labels, maps, materials, or physical details.
6. Emotional tension or narrative meaning.
7. Negative constraints for mistakes to avoid.

Prompt depth gate:

- A normal production prompt should usually be 36+ words unless it is a deliberate date card, text card, statistic card, map hold, or very simple object shot.
- Each prompt should include framing or composition language, visible action, exact subject, domain or period context when relevant, props/details, emotional or narrative tension, and mistake-prevention constraints.
- A prompt that only names a scene, setting, or category is a failure even if it uses the selected visual style.
- If the selected system is sketch, diagram, comic, stick drawing, cinematic documentary, or evidence-board style, every character prompt and shot prompt must stay in that same visual world.
- Passing the word-count gate by adding repeated meta-instructions is still a failure. The prompt must become more specific, not merely longer.

Bad prompt: "People using technology."

Better prompt: "Cinematic Documentary System, modern battery research lab, close-up of a gloved engineer placing a rectangular solid-state battery cell prototype into a testing rig, transparent safety shield in foreground, voltage monitor and thermal camera screen visible in background, cool white lab lighting, tense experimental mood, shallow depth of field, no generic robots, no sci-fi holograms, no unrelated circuit-board background."

Use judgment on complexity. Some shots should be literal and simple when the narration itself is the visual idea:

- "150 million years ago" can be a bold text/date card reading "150,000,000 YEARS AGO" over a simple background.
- "He had a dog that interrupted his work" can be a simple scene of a man at a desk with a dog interrupting him and a short speech bubble.
- A number, date, quote, map label, newspaper headline, or simple object can be the whole prompt if it serves pacing.

Do not turn every line into an elaborate historical scene. Alternate elaborate documentary shots with simple text cards, props, diagrams, character beats, and visual punctuation.

## SEO Meta Description

Write a rich, detailed, upload-ready description (minimum 250–400 words for long-form), not a short summary. Match the depth of a serious YouTube description that optimizes search visibility and engages potential viewers.

Strict structure:

1. **Paragraph 1 (Hook & Setup)**: Start with a strong, curiosity-inducing sentence that immediately outlines the main mystery or tension of the video. Naturally integrate the primary keyword within the first 1-2 sentences, mentioning key entities, dates, locations, or concepts.
2. **Paragraph 2 (Incentive & Core Reversal)**: Deepen the context. Detail the core conflict, historical contradiction, or systemic incentive loop that is explored in the video. Outline why the common assumption (the misconception attacked in the script) is incorrect.
3. **Paragraph 3 (Modern Connection & Payoff)**: Explain the modern relevance or philosophical payoff of the story. Connect the prehistorical or historical mechanism directly to the viewer's current behaviors, systems, or modern technologies.
4. **"Timestamps / Topics Covered" Section**: Provide 6-10 descriptive bullet points with corresponding conceptual timestamps or topics mapped out.
5. **Call to Action & Resources**: Add a section pointing to references, reading material, or secondary links, and instruct the viewer to check the pinned comment or description resources.
6. **Hashtags**: Place 3-5 clean, highly relevant hashtags separated by spaces at the very bottom.

Keep the tone natural, authoritative, and engaging. Do not write short 2-3 sentence summaries. Ensure names, dates, tools, locations, and concepts are richly described.

## Hashtags

Return 3-8 hashtags. Mix broad and specific tags.

## Tags

Return a comma-separated list of search tags. Include:

- Core topic.
- Alternate wording.
- Niche terms.
- Related entities.
- Viewer search phrases.

## Research Material

For factual, historical, science, technology, energy, finance, legal, medical, or current-event content, include a final research section. Keep it concise but useful.

Return:

- Sources used, with links.
- Key facts pulled from each source.
- Misconception map: likely viewer wrong answers, partial answers, or folk explanations considered for the opening.
- Opening targets chosen: the 2-3 misconceptions or assumptions the script should attack first, with a short reason.
- Any uncertainty or conflicting detail that should be checked before publishing.

This section is for the user to cross-check the content and should not be written like video narration.

## Script Only Format

When the user asks only for a script, do not include metadata unless useful. Provide:

- Primary title.
- Runtime target and estimated word count.
- Script Control Brief, when the script is substantial or factual.
- Retention Beat Map, when the script is long-form.
- Script.
- Notes on hook, retention beats, re-hook loops, and visual opportunities when useful.

## Brainstorm Format

When brainstorming a new channel, return:

- Channel promise.
- Audience.
- Content lanes.
- Angle templates.
- Visual identity.
- Logo/profile image prompt.
- Banner image prompt.
- Optional watermark, default thumbnail, or recurring character prompt.
- First 10 video ideas.
- Risks and weak points.
- Best next action.

Challenge weak niches or overly broad positioning.
