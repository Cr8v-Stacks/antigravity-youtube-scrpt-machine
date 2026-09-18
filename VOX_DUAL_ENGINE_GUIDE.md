# 🎬 The Vox Dual-Engine Production Guide
## Architectural Specifications for Cinematic Paper-Dioramas & Swiss-Editorial Motion Graphics

---

### Overview: One Unified System, Two Sources, Two Intents

It is critical to understand: **Remotion ALSO contains the full GitHub Vox engine. This is NOT a dichotomy where AI video does dioramas and Remotion only does flat graphics. It is ONE UNIFIED SYSTEM with shared aesthetic DNA, deployed across different sources and different production intents:**

```
                                  ┌──────────────────────────────────────────────┐
                                  │           Script Narrative Scouting          │
                                  │      (Spoken Clause / Thesis / Paragraph)    │
                                  └──────────────────────┬───────────────────────┘
                                                         │
                                  ONE UNIFIED VOX VISUAL LANGUAGE
                     (Halftone Dots, Paper Dioramas, Calipers, Stamps, Foley)
                                                         │
                           ┌─────────────────────────────┴─────────────────────────────┐
                           │                                                           │
                           ▼                                                           ▼
             ┌───────────────────────────┐                               ┌───────────────────────────┐
             │         SOURCE A          │                               │         SOURCE B          │
             │   Generative AI Video     │                               │      Remotion Engine      │
             │   (Google Flow / Omni)    │                               │  (Deterministic 2.5D Code)│
             └─────────────┬─────────────┘                               └─────────────┬─────────────┘
                           │                                                           │
            • INTENT: Cinematic organic motion                          • INTENT: Exact frame accuracy,
              and photorealistic diffusion                                data meters, forensic tables
            • 3 Physical Depths (BG / MG / FG)                          • Halftone dot textures (`Halftone`)
            • Desaturated archival newsprint                            • Paper tear reveals (`TearReveal`)
            • Halftone cutouts, rough keylines                          • Distressed stamps (`VoxStamp`)
            • Brass calipers, ticking counters                          • Precision HUD calipers & meters
            • Diegetic physical Foley (NO VO/music)                     • Synchronous frame-accurate Foley
```

---

## 1. Engine 1: Cinematic Paper-Diorama Video Prompts (Google Flow / Omni Flash 1.1)

### Visual DNA & Materials:
- **Depth Architecture**: Every block strictly defines 3 physical layers separated in space: `[Background Depth]`, `[Midground Depth]`, `[Foreground Depth]`.
- **Materials**: Aged-newsprint documentary collage, desaturated archival palette with one hot red accent (`#D62E1F`) and mustard secondary (`#D9A441`), condensed bold headline caps, giant stat numbers treated as physical objects, halftone black-and-white cutout people with rough white keylines and offset red marker strokes, torn-paper edges, print grain, halftone dot texture.
- **Physical Dynamics**: Spring pop-ups with overshoot, mechanical brass calipers measuring openings, ticking mechanical counters, letterpress rubber stamps slamming down with micro-dust puffs.
- **Diegetic Sound Design (MANDATORY)**: Physical Foley only (`mechanical shutter click`, `heavy rubber stamp thud`, `ratchet tick`, `marker squeak`). **NO voiceover, NO dialogue, NO background music** in the generated video.
- **Prompt Token Guardrail**: **NEVER write code component tokens like `VoxTape` into video prompts.** Describe physical materials naturally (e.g. *"secured with semi-translucent yellow drafting tape"*, *"tactile brass calipers"*).

### Complete 4-Block Reference Suite (Bluetti Balco Intro):

#### Block 1 (0:00 – 0:06)
- **Vocal Cue**: *"In May 2026, Bluetti held a launch event on the first floor of the Eiffel Tower in Paris..."*
- **Reference Image**: Attach `C:\Users\user\Downloads\newsroom_style_master_sheet.png`
- **Prompt**:
```text
STYLE REFERENCE: Match the attached reference image EXACTLY. Replicate its look precisely: aged-newsprint documentary collage, desaturated archival palette with one hot red accent and mustard secondary, condensed bold headline caps with giant stat numbers, halftone black-and-white cutout people with rough white keylines and offset red strokes, torn-paper edges, print grain and halftone dot texture, layers at distinct depths like a paper diorama, spring pop-ups with overshoot and ticking counters, non-photorealistic, illustrated, not a photo, no live-action, no realism.
SCENE: [Background Depth] Architectural blueprint schematic of the Eiffel Tower's structural iron lattice and first-floor reception hall, tilted in perspective, soft focus. [Midground Depth] Halftone black-and-white cutout silhouettes of an audience and presentation stage with rough white keylines and an offset red marker stroke. [Foreground Depth] A tactile press credential badge reads "BLUETTI PARIS DEBUT" (label) secured with semi-translucent yellow drafting tape; a bold red rubber stamp slams down reading "MAY 2026" (giant number).
MOTION: Fast macro push-in descending at a 30-degree angle toward the paper drafting surface, gliding past the iron lattice layers. Settle on the credential badge and "MAY 2026" date stamp in razor focus.
AUDIO: Airy paper slide, mechanical dual-shutter camera click, heavy rubber stamp thud — NO voiceover, NO music.
NEGATIVE: color drift, photorealism, glossy 3D render, live-action footage, human faces talking, lip-sync, small illegible text, captions, subtitles, watermark.
```

#### Block 2 (0:06 – 0:12)
- **Vocal Cue**: *"...to unveil a piece of hardware designed to solve a problem that has frustrated apartment renters for a decade."*
- **Reference Image**: Attach `C:\Users\user\Downloads\newsroom_style_master_sheet.png`
- **Prompt**:
```text
STYLE REFERENCE: Match the attached reference image EXACTLY. Replicate its look precisely: aged-newsprint documentary collage, desaturated archival palette with one hot red accent and mustard secondary, condensed bold headline caps with giant stat numbers, halftone black-and-white cutout people with rough white keylines and offset red strokes, torn-paper edges, print grain and halftone dot texture, layers at distinct depths like a paper diorama, spring pop-ups with overshoot and ticking counters, non-photorealistic, illustrated, not a photo, no live-action, no realism.
SCENE: [Background Depth] Heavy cream drafting paper with a faint isometric millimeter grid and a subtle city skyline silhouette. [Midground Depth] An architectural cut-out cross-section of a multi-story European apartment building showing black metal balcony railings; animated glowing red schematic lines trace solar energy flowing from panels toward an outlet marked "WALL OUTLET LOCKOUT" (label). [Foreground Depth] Mechanical brass drafting calipers measuring the balcony railing opening; a giant stat counter ticks rapidly upward to "10 YEARS" (giant number).
MOTION: Smooth lateral tracking slide from right to left across the apartment cutouts following the red trace line, concluding with a sharp mechanical stop and slight spring overshoot. Settle on the measured balcony cross-section and "10 YEARS" counter in razor focus.
AUDIO: Mechanical caliper click, dry paper friction slide, metallic ratchet tick — NO voiceover, NO music.
NEGATIVE: color drift, photorealism, glossy 3D render, live-action video, human dialogue, small text blur, subtitles, captions, watermark.
```

#### Block 3 (0:12 – 0:18)
- **Vocal Cue**: *"Their promotional launch videos pitch the new Balco series as an effortless breakthrough for urban clean energy."*
- **Reference Image**: Attach `C:\Users\user\Downloads\newsroom_style_master_sheet.png`
- **Prompt**:
```text
STYLE REFERENCE: Match the attached reference image EXACTLY. Replicate its look precisely: aged-newsprint documentary collage, desaturated archival palette with one hot red accent and mustard secondary, condensed bold headline caps with giant stat numbers, halftone black-and-white cutout people with rough white keylines and offset red strokes, torn-paper edges, print grain and halftone dot texture, layers at distinct depths like a paper diorama, spring pop-ups with overshoot and ticking counters, non-photorealistic, illustrated, not a photo, no live-action, no realism.
SCENE: [Background Depth] Split-tone newsprint backdrop (ink black on left, archival cream on right) with subtle halftone dot texture. [Midground Depth] A physical paper cutout of a compact battery storage unit (matte white corrugated face with diagonal textured ridges and embossed BLUETTI logo) pops up on an elevated paper diorama pedestal with slight spring overshoot. [Foreground Depth] A bright yellow felt-tip highlighter sweeps horizontally behind a bold black stamped title reading "EFFORTLESS BREAKTHROUGH" (headline); an offset red marker arrow snaps in pointing directly at the unit.
MOTION: Low-angle dynamic push-in and rack focus, starting on the sliding highlighter streak and tilting up to frame the hardware pedestal. Settle on the battery cutout centered in crisp focus.
AUDIO: Felt-tip marker friction sweep, paper pop spring, soft pneumatic thud — NO voiceover, NO music.
NEGATIVE: color drift, photorealism, glossy 3D chrome, live-action footage, lip-sync, messy AI lettering, subtitles, watermark.
```

#### Block 4 (0:18 – 0:25)
- **Vocal Cue**: *"But what the new launch doesn't emphasize is that Bluetti has already gone through two earlier balcony generations. In late 2023, Bluetti debuted their first modular balcony kit—the A80 microinverter, D100S controller, and B210 battery—running up to €3,500. But early adopters hit documented hurdles: nightly app disconnects once the sun set, complex external wiring, and rigid battery pairing..."*
- **Reference Image**: Attach `C:\Users\user\Downloads\newsroom_style_master_sheet.png`
- **Prompt**:
```text
STYLE REFERENCE: Match the attached reference image EXACTLY. Replicate its look precisely: aged-newsprint documentary collage, desaturated archival palette with one hot red accent and mustard secondary, condensed bold headline caps with giant stat numbers, halftone black-and-white cutout people with rough white keylines and offset red strokes, torn-paper edges, print grain and halftone dot texture, layers at distinct depths like a paper diorama, spring pop-ups with overshoot and ticking counters, non-photorealistic, illustrated, not a photo, no live-action, no realism.
SCENE: [Background Depth] A forensic evidence ledger with dense printed technical German documentation, faded millimeter graph lines, and a bold diagonal red warning banner reading "CRITICAL OMISSION // THE UNDISCLOSED BACKSTORY" (label). [Midground Depth] Three paper diorama specimen cutouts drop onto the drafting table in rapid sequence: the Bluetti A80 microinverter with tangled dangling MC4 pigtail wires, the D100S intermediate controller box, and the heavy B210 expansion battery pack, each framed by a sharp white paper border and faint drop shadow. [Foreground Depth] A distressed crimson price tag reading "€3,500" (giant number); an offset red rubber stamp slams hard across the cards reading "GEN 1 & GEN 2" (stamp); a faint schematic warning indicator pulses at "NIGHTLY APP DISCONNECT".
MOTION: Rapid whip-pan landing hard on the forensic ledger surface, dynamic macro push-in gliding across the three predecessor hardware cards. Settle on the "GEN 1 & GEN 2" distressed stamp and the €3,500 price tag in razor focus.
AUDIO: Paper whip slide, metallic ratchet tick, three rapid tactile specimen drops, heavy rubber stamp thud — NO voiceover, NO music.
NEGATIVE: color drift, photorealism, glossy 3D chrome, live-action footage, human faces speaking, lip-sync, messy AI lettering, subtitles, watermark.
```

---

## 2. Source B: Remotion Deterministic Code Execution (Track B)

### Visual DNA & Full Component Library:
Remotion is NOT limited to flat graphics—it fully implements the GitHub Vox visual language:
- **Newsprint Halftone Textures**: `Halftone` component rendering pure CSS radial-gradient halftone dot patterns in multiply blend mode over warm drafting paper.
- **Physical Paper Tear Reveals**: `TearReveal` component using deterministic jittered clip-path polygons with SVG edge borders to rip away paper layers in physical space.
- **Alert Wash Overlays**: `AlertWash` component momentarily washing the entire canvas in hot red (`#D62E1F`) on dramatic turning points.
- **Rubber Letterpress Stamps**: `VoxStamp` / `Stamp` with spring-damped physical drop impact and distressed ink textures.
- **Dynamic Highlighters**: Translucent yellow felt-tip streak sweeping dynamically *behind* permanent high-contrast text.
- **Tactile Calipers & Metric Telemetry**: Precision mechanical measurement brackets and live ticking decibel/wattage meters.
- **Photographic Cutouts & Contact Shadows**: High-resolution authentic transparent PNGs floating with soft ambient contact shadows.
- **Synchronous Acoustic Foley**: Frame-accurate `.wav` Foley hits for every single physical event (`thud.wav`, `click.wav`, `swoosh.wav`, `draw.wav`, `stamp_slam.wav`, `pop.wav`).
- **Zero Unmotivated Tape**: No arbitrary masking tape strips across pristine hardware. Tape is only used when physically securing a card or badge.

---

## 3. General Production Directives

1. **Strict Spoken Chronology**: The audio dictates the timeline. Visuals arrive word-by-word with the vocal cadence. Never spoil future beats prematurely.
2. **Authentic Sourcing Law**: Never substitute real architectural landmarks or hardware units with synthetic vector line drawings. Extract clean photographic transparent cutouts from the web.
3. **Script-Proportional Asset Harvesting**: Match asset harvesting depth to narrative scope. Gather heroes, exploded views, rear I/O, accessories, lifestyle setups, and competitor context into `product_images/<brand>/`.
4. **Windows Execution Mandate**: Always run Remotion via `cmd /c npx remotion ...`.
