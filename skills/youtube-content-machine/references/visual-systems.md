# Visual Systems

Use this file for visual style definitions and prompt standards. Use `selection-matrices.md` before choosing an episode visual system or building a shot list.

Canon episode-level visual systems:

1. Editorial Diagram System.
2. Notebook Sketch System.
3. Social Comic System.
4. Hybrid Sketch System Map.
5. Cinematic Documentary System.
6. Evidence Board / Polaroid System.

Keep these as the main selectable systems. Use shot visual types for variety inside the selected system.

## Universal Thumbnail Rules

Use simple, high-contrast concepts. The viewer should understand the tension in under one second.

Prefer:

- One central visual idea.
- One emotional label or contradiction.
- Arrows, loops, symbols, or evidence objects.
- Minimal text, usually 2-6 words.

Avoid clutter, generic AI beauty shots, and thumbnails that only show the object without the story.

## Canon System Definitions

Use these visual systems deliberately. Always select one canon system for the episode before writing prompts, then choose a channel/niche identity preset from `selection-matrices.md`.

### Editorial Diagram System

Use for the main explanation.

Prompt base:

editorial minimalist diagram system, simple drawn human figures with expressive faces, conceptual explanation, arrows showing behavioral relationships, system flow visualization, clean academic infographic style, muted tones, high clarity, white or off-white background, subtle texture, explanatory diagram aesthetic

### Notebook Sketch System

Use for deep thinking, origin explanations, theory, and system breakdowns.

Prompt base:

hand-drawn notebook sketch style, rough pencil illustration of human behavior system, annotated diagrams, arrows and notes around figures, psychology explanation page, slightly messy academic notebook aesthetic, conceptual thinking visual, white paper texture, high contrast pencil lines

### Social Comic System

Use for emotion, social pressure, conformity, embarrassment, status interaction, and dialogue moments.

Prompt base:

minimalist expressive cartoon human characters, simple expressive faces, thin clean outlines, conversational scene, short speech bubbles, social interaction moment, emotional psychology illustration, flat clean design, white background, minimal color accents

### Hybrid Sketch System Map

Use for historical progression, system evolution, trust networks, behavior loops, and scripts that combine narrative history with abstract systems.

Prompt base:

hybrid sketch system map, hand-drawn historical timeline mixed with clean system diagrams, simple editorial human figures, arrows showing trust, memory, exchange, scale, and consequences, notebook paper texture, annotated labels, muted earth tones, black ink lines, documentary explanation style, clear visual hierarchy, no clutter, no realism, no 3D

## Cinematic Documentary System

Use for real people, inventions, companies, physical technology, energy projects, labs, factories, historical reenactments, business pressure, and stories where real-world authority matters.

Prompt base:

cinematic documentary image, historically or technically grounded scene, specific person or role performing a visible action, real-world location or period context, detailed physical props and evidence objects, intentional camera framing, naturalistic lighting, emotional tension, archival or investigative realism when appropriate, no generic stock imagery, no sci-fi holograms, no wrong-era objects

## Evidence Board / Polaroid System

Use for mysteries, forgotten history, hidden connections, investigative stories, and topics where the viewer should feel a case is being assembled from clues.

Prompt base:

evidence board / Polaroid investigation style, close-up of pinned archival photo or document, red string connections, handwritten labels, case-file notes, textured paper, dim investigative lighting, shallow depth of field, documentary mystery atmosphere, specific clue object visible, no modern clutter unless the story is modern, no unreadable wall of text

## Domain Presets

### Human Behavior / System-Explanation Domain Preset

For human-behavior/system-explanation videos:

- Hook: Social Comic System or a striking symbolic Editorial Diagram System shot.
- Explanation: Editorial Diagram System.
- Deep system: Notebook Sketch System.
- Conclusion: Editorial Diagram System or symbolic loop visual.
- Historical progression or system evolution: Hybrid Sketch System Map.

Use off-white or paper backgrounds by default. Use dark backgrounds only for tension, collapse, anxiety, conflict, or dramatic contrast.

### Renewable / Clean Energy / Energy-History Domain Preset

This is a domain implementation of Cinematic Documentary System, not a separate canon episode visual system. Use cinematic documentary prompts with historical or technical specificity.

Strong shot categories:

- Establishing shot.
- Close-up shot.
- Blueprint shot.
- Workshop shot.
- Failure shot.
- Newspaper shot.
- Detective board shot.
- Comparison shot.
- Scale shot.
- Map shot.
- Timeline shot.
- Patent shot.
- Crowd reaction shot.
- Investor or boardroom shot.
- Quote shot, used sparingly.
- Infographic shot.
- Future concept shot, only when the story genuinely requires it.

Every prompt should include:

- Camera framing.
- Physical storytelling element.
- Emotional tone.
- Period, location, technology, or object details where relevant.

However, not every shot needs to be elaborate. Use simple literal shots when they improve clarity, pacing, or retention:

- Text/date cards for major time jumps or numbers.
- Newspaper headline cards.
- Close-ups of a single object.
- Maps with one highlighted route or location.
- A character and one prop.
- Speech-bubble or quote-card moments.
- Simple comparison graphics.

If the narration says "150 million years ago," a valid prompt may simply be a dramatic text card reading "150,000,000 YEARS AGO" rather than an ancient landscape. If the narration says a dog interrupted a man's work, a valid prompt may be a simple man-at-desk scene with a dog and a short speech bubble.

Example prompt pattern:

overhead shot of a detective-style evidence board, multiple Polaroid photos pinned with red string connections, one Polaroid shows [specific location or machine], another shows [specific document or sketch], dim room lighting, cinematic tension, documentary investigation style, shallow depth of field, layered research wall, no modern objects

## Image Prompt Quality Checklist

Before finalizing prompts, check that each prompt has:

- A clear subject.
- A visible action or moment.
- Camera language.
- Emotional tension.
- Props or details that identify the story.
- Style consistency with the channel.
- Negative constraints when helpful, such as no modern objects, no realism, no 3D, no clutter, or no futuristic elements.
- Enough descriptive detail for an image model to produce a distinct frame, not a vague illustration.

### Director's Principle of Visual Simplicity & Clean Layouts

To prevent over-complicating prompts and introducing visual clutter, noise, or AI generation errors:
- **Simplify Conceptual and Negative Statements**: For purely abstract, negative, or conceptual narration beats, do not force a complex, realistic scene. Use clean, graphic design elements:
  - *Cancel/Red Cross Overlays*: For lines like "It is almost certainly wrong" or "You just unlocked liver failure," use a simple visual anchor (e.g. the word "WRONG" or a simple line art drawing of a human liver) overlayed with a bold, red cancel mark or red cross mark.
  - *Text Cards*: For numbers or time frames ("30 million years ago"), use a clean typographic text card or calendar sheet over a minimalist background.
  - *Emphasis on Locations/Countries*: For lines mentioning specific locations or countries (like Spain or Haifa), focus on a clean, simple map outline or location name/text rather than attempting a complex historical scene.
- **Strictly Add `, no text` to Textless Prompts**: AI image generators frequently add garbage letters or gibberish words to prompts. If a shot prompt does not require text, always explicitly append `, no text` or `, no texts` to the end of the prompt to enforce a clean image.
- **Ban Step/Point/Shot Numbers in Prompts**: Never leak workflow index numbers, cycle counts, or placeholders (like "point 20," "step 20," "shot 15," "cycle 7," "loop 7," "phase 7," "position 7") into the visual prompt descriptions. The prompt must only describe what should be seen in the final frame.

Do not output generic labels such as "[technology] image" or "person thinking." Turn each into a directed shot.

If the prompt would still make sense after replacing the topic noun with another topic noun, it is probably too generic. Add the specific object, tool, document, interface, location, clothing, material, date, social role, machine part, visible action, or mistake-prevention constraint that belongs to this topic.

## Prompt Depth Standard

Each shot prompt must read like a production-ready visual instruction, not a scene label. A weak prompt names a setting. A strong prompt defines the exact subject, action, period, setting, visible props, composition, lighting or texture, emotional tension, and mistake-prevention constraints.

Prompt depth is not the same as prompt quality. A long prompt can still be weak if every prompt uses the same sentence skeleton. For premium output, vary the shot's production role, not only the camera distance. Rotate between character action, object clue, map, timeline, document, social-pressure scene, split comparison, symbolic card, and system diagram as the narration demands.

Do not create validator-complete prompts by cycling one grammar through the whole list, such as "literal action," "object-led insert," and "system-map diagram" repeated for every beat. The shared identity should come from the visual system and preset; the prompt grammar should come from the narration's specific scene, object, or proof need.

Do not use code loops over noun, action, frame, label, or emotion arrays to author the final prompts. Loop-generated prompts usually pass length checks while failing production judgment. Write or revise prompts as shot clusters tied to actual script beats.

Do not inflate weak prompts by appending the same generic phrase to every shot, such as "visible social pressure," "object-specific historical details," or "foreground-background clarity." Those are validator words, not visual direction. Add the precise prop, gesture, setting, composition, and tension that only belongs to that shot.

Do not tag nearly every prompt as a "diagram hold" or other card/hold type to escape depth checks. A diagram hold is a deliberate pacing choice for a specific beat; it should not replace varied shot types such as character action, object clue, social pressure, map, timeline, archive artifact, and final synthesis.

Avoid mechanical A/B/C patterns such as:

- A: medium shot of...
- B: close-up composition focused on...
- C: overhead diagram layout turning...

This pattern is acceptable for a few isolated shots, but it becomes a failure when repeated through a whole pack. Instead, make each variation sound like a director chose it for that specific narration beat.

Do not write thin prompts such as "busy ancient marketplace with strangers exchanging coins." Expand the scene into a directed image prompt: exact time period, location context, object type, social tension, framing, background details, style system, and negative constraints.

For history and system-explanation episodes, include concrete visual anchors such as clay tablets, reed stylus, barley sacks, cowrie shells, livestock, tally marks, temple storehouse, boundary river, settlement fire circle, grain measure, electrum coin, map label, date card, reputation diagram, or trust-network arrows when relevant.

Use the selected visual system as the first phrase of every prompt unless the user requests otherwise. Keep the depth high even for simple shots. A date card can be simple, but it should still specify the exact text, background texture, visible supporting symbols, framing, and what mistakes to avoid.

Shot-list prompts are not allowed to become section summaries. Each prompt must be a frame the editor can generate and place on the timeline. For long-form videos, pair each timestamp with the narration phrase it covers so the visual plan proves it follows the script rather than floating beside it. The shot list must stay semantically aligned from start to finish; final prompts should visualize the final payoff, not recycled early-script phrases.

## Character Consistency

Create a primary character prompt before the shot list when a video has a named person, historical figure, recurring presenter, mascot, or recurring fictional character. Use it as the source description for all later prompts.

Create a recurring character set before the shot list when a video repeatedly shows generic people or social roles, even if no single person is the protagonist. Match the selected visual system exactly. A sketch shot list needs sketch character prompts. A stick-drawing shot list needs stick-drawing character prompts. A cinematic documentary shot list needs cinematic documentary character prompts.

For historical or renowned people:

- Research public descriptions or images before defining the character.
- Describe non-copyrightable visual facts: approximate age, hair, facial hair, clothing era, posture, tools, and role.
- Avoid reproducing a specific copyrighted image or named living artist style.
- If references are limited or conflicting, state that the character prompt is an approximate historically grounded depiction.

For first appearance prompts, fully define:

- Approximate age.
- Hair color, length, and style.
- Facial hair if relevant.
- Era-accurate clothing.
- Defining props such as spectacles, tools, notebooks, lab equipment, or documents.

For later prompts, reuse the exact same description or say "same character design as primary character prompt."
