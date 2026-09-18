# 🚀 Master Handover Prompt (For New Chat Session)

Copy and paste the entire block below directly into your new Antigravity chat session to resume production seamlessly with zero loss of context:

```markdown
# MISSION BRIEFING: Bluetti Balco Review Video Production & Motion Design

We are producing the broadcast video assets and motion design B-rolls for the YouTube documentary script located at:
`c:\Users\user\OneDrive\Documents\antigravity-youtube-scrpt-machine-main\bluetti_balco_review_script.md`

Read this briefing carefully. All technical rules, creative guardrails, and architectural guidelines are codified below.

---

## 1. Operating Environment & Workspaces

1. **Workspace Root**: `c:\Users\user\OneDrive\Documents\antigravity-youtube-scrpt-machine-main`
   - Master Script: `bluetti_balco_review_script.md`
   - Master Directives: `INSTRUCTIONS_FOR_AGENTS.md` and `VOX_DUAL_ENGINE_GUIDE.md`
   - Final Delivery Directory: `motion_clips/` (Formula: `motion_<index>_<spoken_cue_slug>.mp4`)
   - Curated Assets: `product_images/bluetti/`
2. **Remotion Project Directory**: `C:\Users\user\OneDrive\Documents\antigravity-solar-remotion`
   - Production Compositions: `src/production/` and `src/vox_editorial/`
   - Reusable Specs (1–8): `src/specs/`
   - Frame Rate & Resolution: 1920x1080 @ 30fps (30 frames = 1.0 second)
   - Foley Sound Library: `public/sfx/` (`thud.wav`, `click.wav`, `swoosh.wav`, `draw.wav`, `stamp_slam.wav`, `pop.wav`)
3. **Execution Rule (Windows 11 PowerShell)**:
   - NEVER run raw `npx` or `npm`. Always execute Remotion commands via `cmd /c`:
     `cmd /c npx remotion render <CompositionID> motion_clips/<filename>.mp4`
   - Always purge temporary preview PNG stills from `preview_frames/` after inspection.

---

## 2. Current Project Status

- **Intro Section (Lines 143–148)**: Fully completed across both production tracks:
  - **Track A (Generative AI Video Prompts)**: Complete 4-block cinematic paper-diorama prompt suite tailored for Google Flow (Omni Flash 1.1 / Gemini Omni) referencing `C:\Users\user\Downloads\newsroom_style_master_sheet.png`.
  - **Track B (Remotion 2.5D Parallax Fallback)**: 750 frames (25.0s @ 30fps) rendered and verified at:
    `motion_clips/motion_01_bluetti_eiffel_intro_trackB.mp4`
- **Next Up**: Scouting, prompt engineering, or coding the next section of `bluetti_balco_review_script.md` starting at **[TEST 1: THE BALCONY SHADING TRAP]** (Lines 159–175) or specific paragraphs requested by the user.

---

## 3. The Two Vox Production Pathways & 6 Locked House Styles

We maintain two execution pathways for Vox (codified in `VOX_DUAL_ENGINE_GUIDE.md` and `SYSTEM_ARCHITECTURE_AND_ENGINE_HIERARCHY.md`):

### The 6 Locked House Styles & Documentary Directions:
1. **Newsroom Collage (Default)**: Aged newsprint (`#F4EFEA`), halftone B&W cutouts with rough white borders and offset red strokes, giant stat numerals treated as characters.
2. **Mixed-Media Paper**: Bold solid color blocks, archival photographic cutouts, black marker circles, and high-contrast geometric paper shapes.
3. **3D Paper Diorama**: Deep sepia craft paper and heavy textured cardboard, layers separated in physical space, censor bars, letterpress props.
4. **Detective Casefile (Murder Board)**: Dark corkboard (`#2E1F16`), taut red yarn linking pushpins between suspect products and lab benchmarks, manila evidence folders with `[CLASSIFIED]` stamps, typewriter text, fingerprint smudges.
5. **Polaroid Forensic Snapshot**: Authentic white chemical Polaroid 600 frames with wide chins, handwritten black Sharpie notes, chemical developing emulsion bloom (dark to full exposure), scotch tape, paperclips pinning field receipts. Ideal for field reportage and high-impact scene openers.
6. **Tactical Cartography (Johnny Harris Map)**: Tilted 3D topographic contour blueprints, animated red route trajectories, glowing amber GPS pins, coordinate crosshairs (`48°51'24"N 2°17'48"E`), and torn paper revealing satellite terrain.

### Execution Pathways:
- **Pathway 1: Cinematic Generative AI Video Prompts (Google Flow / Omni Flash 1.1)**:
  - 3 physical depths separated in space (`[Background Depth]`, `[Midground Depth]`, `[Foreground Depth]`).
  - Strict 5-line format (`STYLE REFERENCE`, `SCENE`, `MOTION`, `AUDIO`, `NEGATIVE`).
  - Physical diegetic Foley ONLY (`AUDIO: mechanical shutter click, rubber stamp thud, caliper click, ratchet tick — NO voiceover, NO music`).
  - Style Reference File: Instruct user to attach `C:\Users\user\Downloads\newsroom_style_master_sheet.png`.
  - NO CODE TOKENS: Never write code component names (like `VoxTape`) in prompts. Describe real tactile materials directly.
- **Pathway 2: Editorial Swiss Graphic Motion Engine (Remotion Deterministic Code)**:
  - Built deterministically in Remotion directly to `motion_clips/`.
  - Warm editorial paper desk (`VoxPaperDesk`), authentic high-resolution photographic PNG cutouts floating with soft contact shadows, permanent high-contrast typography, yellow felt-tip highlighter sweeps, precision HUD calipers, forensic comparison tables, distressed ink stamps (`VoxStamp`).
  - Frame-accurate synchronous `.wav` Foley hits (`swoosh.wav`, `click.wav`, `thud.wav`, `draw.wav`, `stamp_slam.wav`).
  - Zero Unmotivated Tape: No arbitrary tape strips slapped across pristine hardware photos or slides.

---

## 4. Universal Production Guardrails

1. **Strict Vocal Chronology**: The audio dictates what appears on screen at every exact second. Visuals arrive word-by-word with the vocal cadence. Never spoil a future concept prematurely, and never lag behind the spoken clause.
2. **Authentic Sourcing Law (No Synthetic SVGs for Real Subjects)**: Never replace real-world architectural landmarks, venues, or hardware products with synthetic SVG line drawings. Always search the web and extract authentic, high-resolution photographic transparent PNG cutouts. Real physical texture, metal reflection, and architectural realism are mandatory for documentary authority.
3. **Script-Proportional Visual Reservoir**: Sourcing depth must match the script's narrative scope. For teardowns, benchmarks, and reviews, assemble a comprehensive visual library (heroes, exploded internals, rear ports, accessories, lifestyle setups, predecessor units, and press event photos) into `product_images/<brand>/`. Never settle for a superficial 3–4 images.
4. **The "Full Canvas" Trap**: Never open a scene at frame 0 with pre-assembled layouts. Every product, metric, or clause gets its own isolated entrance and Foley punch.
5. **Sound Design is Mandatory**: Sound design is a first-class citizen across both engines—diegetic acoustic physical Foley in generative prompts, and frame-accurate `.wav` hits in Remotion code.

---

## 5. Ready for Next Steps

Acknowledge this briefing, confirm understanding of the two distinct Vox engines and guardrails, and let me know how you'd like to tackle the next script section in `bluetti_balco_review_script.md`!
```
