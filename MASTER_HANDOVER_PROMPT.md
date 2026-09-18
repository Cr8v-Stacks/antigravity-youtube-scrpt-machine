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

## 3. The Two Vox Production Directions (Dual-Engine Architecture)

We maintain two distinct, specialized Vox creative directions (codified in `VOX_DUAL_ENGINE_GUIDE.md`):

### Direction 1: Cinematic Paper-Diorama Video Prompts (Generative AI Video)
- **Target Engine**: Google Flow (Omni Flash 1.1 / Gemini Omni), Runway, Seedance.
- **Visual DNA**: 3 physical depths separated in space (`[Background Depth]`, `[Midground Depth]`, `[Foreground Depth]`), aged-newsprint documentary collage, desaturated archival palette with hot red (`#D62E1F`) and mustard secondary (`#D9A441`), condensed bold headline caps, giant stat numbers, halftone black-and-white cutouts with rough white keylines and offset red marker strokes, torn-paper edges, brass drafting calipers, spring pop-ups with overshoot, ticking mechanical counters, rubber letterpress stamps slamming down with micro-dust puffs.
- **Prompt Structure**: Strict 5-line format (`STYLE REFERENCE`, `SCENE`, `MOTION`, `AUDIO`, `NEGATIVE`).
- **Sound Design**: Physical diegetic Foley ONLY (`AUDIO: mechanical shutter click, rubber stamp thud, caliper click, ratchet tick — NO voiceover, NO music`).
- **Style Reference File**: Instruct user to attach `C:\Users\user\Downloads\newsroom_style_master_sheet.png`.
- **NO CODE TOKENS**: Never write code component names (like `VoxTape`) in prompts. Describe real tactile materials directly (e.g., *"secured with semi-translucent yellow drafting tape"*).

### Direction 2: Editorial Swiss Graphic Motion Engine (Remotion 2.5D Parallax)
- **Target Engine**: Remotion deterministic rendering directly to `motion_clips/`.
- **Visual DNA**: Warm editorial paper desk (`VoxPaperDesk`, `#F4EFEA`), authentic high-resolution photographic PNG cutouts floating with soft contact shadows, permanent high-contrast typography (Space Grotesk + IBM Plex Mono), vibrant yellow felt-tip highlighter sweeps (`#F5E050`) behind permanent text, precision HUD calipers, forensic comparison tables, distressed ink stamps (`VoxStamp`).
- **Sound Design**: Frame-accurate synchronous `.wav` Foley hits for every visual arrival and transition (`swoosh.wav`, `click.wav`, `thud.wav`, `draw.wav`, `stamp_slam.wav`).
- **Zero Unmotivated Tape**: No arbitrary masking tape strips slapped across pristine hardware photos or slides.

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
