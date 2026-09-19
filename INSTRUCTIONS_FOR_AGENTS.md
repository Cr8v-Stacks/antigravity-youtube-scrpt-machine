# 🎬 MASTER DIRECTIVE: Broadcast Motion Design & B-Roll Production Framework
## The Definitive Operating Guide for Remotion Engineering & Motion Design Agents

---

### Table of Contents
1. **The Creative Mandate: Freedom, Artistry & Thinking Like the Viewer**
2. **Operating Environment & Execution Rules (Zero Exceptions)**
3. **The 3-Concept Ideation Step (Never Dive Straight into Code)**
4. **The Cardinal Sin: The "Full Canvas" Trap & Unresolved Tension**
5. **Media Agility: When NOT to Force Pure Motion (Stock Videos, OEM B-Roll, Subtitle Cropping)**
6. **Breaking the "One-Track Mind" (Dynamism Lessons from VoxIntro)**
7. **The Modular Spec Library (Specs 1–7): How to Use, Adapt, and Upgrade**
8. **Evidence Vault & Documented Receipts**
9. **Anti-AI Slop & Anti-Bloat Mandate (Zero-Bloat Rules with Code Diffs)**
10. **Audio-Visual Timing Math & The 9-Step Production Pipeline**
11. **Design Tokens, Typography & Synchronous Acoustic Foley**

---

## 1. The Creative Mandate: Freedom, Artistry & Thinking Like the Viewer

> **"Don't take this as a Bible or as the law. It's not a Bible and it is not the law. You have freedom. The only thing that is truly law is the background palette, dead center vertical alignment, and sound design. The creative aspects are on you. Think like a motion designer, think like a creative director, think like a producer, think like an artist. Think like the viewer: if I am watching this, what would I want to see that would excite me to keep watching?"**

### The Viewer's Psychology:
- A viewer does not watch motion graphics in an isolated vacuum; they are listening to spoken narration in real time.
- If what they see on screen does not match what they hear in the audio, it looks like an **editing mistake** or a **misrepresented edit**.
- If what they see on screen is a static, pre-assembled card filled with text boxes and decorative HUD bars, they instantly recognize it as **AI slop** and tune out.
- Every cut, transition, and reveal must feel like an intentional visual argument that propels the story forward.

---

## 2. Operating Environment & Execution Rules (Zero Exceptions)

| Parameter | Specification | Strict Rule / Consequence |
| :--- | :--- | :--- |
| **Operating System** | Windows 11 (PowerShell) | **NEVER run raw `npx` or `npm`**. PowerShell execution policy blocks raw scripts on Windows. **Always execute: `cmd /c npx remotion ...`** |
| **Remotion Codebase** | `C:\Users\user\OneDrive\Documents\antigravity-solar-remotion` | All production components live in `src/production/`. All reusable archetype specs live in `src/specs/`. |
| **Timeline Delivery Target** | `C:\Users\user\OneDrive\Documents\antigravity-youtube-scrpt-machine-main\motion_clips` | Every rendered `.mp4` MUST be copied/mirrored here with canonical naming (e.g. `motion_12_anker_inverter_overhead_thermal.mp4`). |
| **Canvas & Frame Rate** | `1920x1080` @ `30fps` | Standard broadcast timing: **30 frames = exactly 1.0 second**. |
| **Dead-Center Vertical Alignment** | `justifyContent: 'center'` | Content must always be vertically and horizontally centered in the 1920x1080 frame. No awkward top-heavy floating. |
| **Composition Registration** | `src/Root.tsx` | Every clip must be registered with `<Composition id="..." component={...} durationInFrames={...} width={1920} height={1080} fps={30} />`. |
| **Stale Files Policy** | Zero Stale Preview Files | All `.png` preview stills generated in `preview_frames/` or `out/` **MUST be purged** via PowerShell before delivering the canonical `.mp4`. |

---

## 3. The 3-Concept Ideation Step (Never Dive Straight into Code)

> **"Don't just dive deep into what you are seeing. You think, you reason, you ideate... You come up with like two to three different concepts. Then you make a decision on the best concept to use going forward."**

Before writing a single line of code, any agent handling a script paragraph MUST pause and ideate **2 to 3 distinct creative concepts**:
- **Concept 1 (e.g. Pure Physical Hardware Journey)**: Centered around authentic studio cutouts of the machine, showing physical inputs/outputs, thermal heat glows on heatsinks, and direct energy flow.
- **Concept 2 (e.g. Minimalist Editorial / Vox Data Flow)**: Centered around high-contrast typography, battery capacity bars physically slicing away loss, and kinetic data readouts.
- **Concept 3 (e.g. Mixed Media / Authentic Document Reality)**: Bringing in real editorial installation photography or lab evidence cards from the vault, scaling them dynamically.

Compare the concepts, consider what excites the viewer, and pick the strongest direction (or discuss with the user) before opening the editor.

---

## 4. The Cardinal Sin: The "Full Canvas" Trap & Unresolved Tension

The single biggest mistake AI agents make is opening a scene with a **completed layout**.

- **The Crime**: When a scene begins at frame 0 with a card, an energy pipe, an inverter box, and a wall socket all already sitting on the canvas, **the punchline is spoiled immediately**. The viewer reads the entire slide in 0.5s. There is zero suspense, zero tension, and zero reason to watch the next 15 seconds.
- **The Law of Progressive Disclosure**:
  1. The scene begins **clean, minimal, or completely empty**.
  2. Elements arrive **word-by-word** as the narrator introduces them.
  3. **Causal Spatial Displacement**: Elements must physically interact. When Element B is introduced in the audio, Element A doesn't just sit there—it physically translates, scales down, or reacts to *make room* for Element B.
  4. **Unresolved Visual Tension**: If energy is flowing from a battery, **do not show the socket yet**. Let the viewer wonder where the energy is going until the narrator speaks the words *"at the socket"*.

---

## 5. Media Agility: When NOT to Force Pure Motion (Images & Videos)

A massive blind spot of AI agents is assuming that *every single concept* must be constructed out of CSS boxes, SVG vectors, and coordinate geometry.

### The "Forced Motion" Trap:
In real filmmaking and documentary editing (Vox, Bloomberg, Johnny Harris), **nobody uses 100% vector motion graphics for 10 minutes straight**. Forcing abstract geometric shapes onto emotional, scenic, installation, or physical topics looks artificial, sterile, and exhausting for the viewer. If you try to hand-code an electrical connector melting or a solar panel on a balcony with CSS polygons, **it will look like slop**.

---

### 5.1 Master OEM Video & B-Roll Library: `Plug-in Renewables`
The user has provided an extensive master repository of pristine 1080p and 4K official manufacturer footage, real balcony installation documentaries, and teardown b-roll located at:
📁 **`C:\Users\user\Downloads\Plug-in Renewables\`**

#### Available Media Folders:
1. **`Plug-in Battery\Anker\`**:
   - `How to Install Anker SOLIX Solarbank 2 E1600 Pro` (Mounting, brackets, cabling, wall socket)
   - `NEU Anker SOLIX Solarbank 4 E5000 Pro_2160p.mp4` (4K 2026 flagship footage & chassis reveals)
2. **`Plug-in Battery\Ecoflow\`**:
   - `EcoFlow STREAM AC Pro Plug-In Battery Quick Intro...` (Official Stream AC hardware b-roll)
   - `EcoFlow PowerOcean Three-phase...` & `EcoFlow OCEAN 2_1080p.mp4`
   - Short b-roll clips: `5.mp4`, `12.mp4`, high-res product stills (`6_2.jpg`, `6_3.jpg`, `pic15-pc.jpg`)
3. **`Plug-in Battery\Zendure\`**:
   - `Unleashing SolarFlow 2400 Pro Maximize Balcony S...` (Official 2400 series b-roll)
   - `Zendure Solarflow 2400 AC + AB3000X Effortless App...` (Hardware stacks, modular cables)
4. **`Plug-in Battery\Bluetti\`**, **`Jackery\`**, **`Pila\`**:
   - High-res hardware introductions and modular battery teardowns.
5. **`Plug-in Battery\Virtual Power Plant\`**:
   - `Virtual Power Plant Tesla Energy_216...` & `Powering a Smarter Grid How Enel X's...` (Grid export, dynamic tariffs, peak shaving b-roll)
6. **`Plug-in Solar\`**:
   - Authentic German Balkonkraftwerk installation footage, flat-roof mounting brackets, flexible solar panels, inverter cabling, micro-inverter hookups.

#### How Parallel Agents Must Ingest This Media:
Because Remotion serves media exclusively from the project's `public/` directory, agents MUST follow this simple 2-step ingestion pattern:
1. **Copy the desired clip into `public/footage/`** with a canonical descriptive name:
   ```powershell
   Copy-Item "C:\Users\user\Downloads\Plug-in Renewables\Plug-in Battery\Anker\NEU  Anker SOLIX Solarbank 4 E5000 Pro_2160p.mp4" -Destination "public\footage\anker_solarbank_4_e5000_oem.mp4"
   ```
2. **Reference it inside the Remotion composition**:
   ```tsx
   <OffthreadVideo src={staticFile('footage/anker_solarbank_4_e5000_oem.mp4')} ... />
   ```
3. Always enforce **Rule 1 (Zero Overlay on Baked Text)** and **Rule 2 (The Premiere Pro Crop)** on all ingested b-roll!

---

### 5.2 Stock Video & Additional Media Sourcing (Preserving AI Quotas & Quality)
Constantly calling image-generation tools burns hourly API rate limits, causes timeouts, and yields generic, uncanny AI images. Instead, use real footage and photography:
- **Free Stock Video Repositories**: Mixkit (`https://assets.mixkit.co/videos/...`), Pexels, Pixabay, Wikimedia Commons. Free 720p/1080p MP4 clips can be downloaded directly via curl/node into `public/footage/`.
- **Existing Asset Vault**: Always check project directories before generating:
  - Product Cutouts: `public/product_images/{ecoflow, zendure, anker}/`
  - Raw OEM & Real Footage: `public/footage/`
  - Editorial & Real Lifestyle: `public/editorial/`
  - Lab Benchmarks & Forum Evidence: `public/evidence/` and `public/evidence_vault/`
  - Textures: `public/textures/studio_slate_texture.jpg`

---

### 5.3 Product Videos & OEM B-Roll: The 3 Golden Rules

When using official product videos, b-roll cuts, or manufacturer promotional clips, agents MUST enforce three non-negotiable rules:

#### Rule 1: Zero Overlay on Baked-in Text / UI (Collision Avoidance)
- OEM product videos frequently have on-screen text, technical specs, dimension callouts, or brand logos baked into specific regions (e.g. bottom-right specs or center titles).
- **CRITICAL**: Never place titles, telemetry readouts, badges, or animated cards directly on top of baked-in text or busy UI elements. That creates unreadable, chaotic clutter.
- **Creative Solution**:
  - Analyze where the source video is busy vs clean.
  - Position overlay graphics strictly in **clean negative space** (e.g., top-left, dark blurred corners).
  - Or wrap text in an editorial semi-transparent frosted card (`background: 'rgba(5, 7, 11, 0.82)', backdropFilter: 'blur(16px)'`) with clear padding, or use a split-screen layout.

#### Rule 2: The "Premiere Pro Crop" (Eliminating Subtitles & Lower Thirds)
- Many product videos and foreign reviews come with baked-in subtitles, captions, or watermarks across the lower third.
- In manual editing (Premiere Pro / After Effects), an editor scales up the frame (`115% - 125%`) and repositions the anchor to push the subtitle bar off the screen.
- **Remotion Implementation**:
  ```tsx
  // Wrap <OffthreadVideo> inside an overflow: hidden container
  <div style={{
    position: 'absolute',
    inset: 0,
    overflow: 'hidden',
    width: 1920,
    height: 1080,
  }}>
    <OffthreadVideo
      src={staticFile('footage/zendure_segmented_broll.mp4')}
      style={{
        width: 1920,
        height: 1080,
        objectFit: 'cover',
        // Scale up to 115-125% and push the frame up to crop out bottom subtitles:
        transform: 'scale(1.22) translateY(-35px)',
        transformOrigin: 'center center',
      }}
    />
  </div>
  ```
  Adjust `scale` (e.g. `1.15` to `1.28`) and `translateY` so that lower-third subtitles are completely cropped out while keeping the product centered.

#### Rule 3: Rapid Punch-In to Full-Bleed (Pacing & Immersion)
- **Do not trap media in an undersized card**: If the narrative is presenting the physical product or b-roll as the main subject, do not leave it floating as a modest 600px box in the center of the frame for 10 seconds.
- **Fast Expansion**: Punch in rapidly from a focal card to **full 1920x1080 canvas** within **8 to 15 frames** using a snappy spring:
  ```tsx
  const punchProgress = spring({ frame: frame - 12, fps, config: { damping: 16, mass: 0.6 } });
  const width = interpolate(punchProgress, [0, 1], [720, 1920]);
  const height = interpolate(punchProgress, [0, 1], [460, 1080]);
  const borderRadius = interpolate(punchProgress, [0, 1], [24, 0]);
  ```
  This creates a high-energy documentary transition (like Vox or Bloomberg) where the subject bursts open into the full world.

---

### 5.4 The Cinematic Hold (3 to 6 Seconds)
It is completely valid—and often vastly superior—to animate in a high-res photo or video clip and **hold it for 3 to 6 seconds** with a slow, subtle Ken Burns push (`scale: 1.0 -> 1.05`) while the narrator speaks. Not every second needs a new SVG animation. Let the authentic footage do the heavy lifting!

---

### 5.5 The Web-First Photographic Sourcing Rule (No Synthetic Vector SVGs)
When depicting real-world architectural landmarks (e.g., Eiffel Tower, Brandenburg Gate, exhibition centers), physical venues, or real hardware units:
- **STRICT PROHIBITION**: Never replace real physical subjects with synthetic SVG line drawings or CSS polygon sketches.
- **MANDATORY PROTOCOL**: Go online, search for high-resolution photography or official press portals, extract clean transparent cutouts, and composite the authentic photographic texture into the scene. Real metal reflections, authentic shadows, and genuine architectural details are mandatory for documentary authority.
- **NO CODE TOKENS IN MEDIA PROMPTS & ZERO ARBITRARY TAPE**: Never write code component tokens like `VoxTape` into generative video prompts. In video prompts, describe physical materials naturally (e.g., "secured with yellow drafting tape"). In motion graphics, avoid slapping arbitrary decorative tape across clean hardware photos.
- **SCRIPT-PROPORTIONAL ASSET RESERVOIR**: Long-form reviews and teardowns require comprehensive visual coverage matching the script's narrative scope (heroes, exploded circuitry, rear ports, accessories, lifestyle setups, predecessor hardware, and press event photos) in `product_images/<brand>/`. Avoid stopping at superficial 3–4 images.

---

## 6. Breaking the "One-Track Mind" (Dynamism Lessons from VoxIntro)

AI agents easily fall into a repetitive conveyor-belt habit:
`Box enters center -> Spring scale -> Title on top -> Stats inside -> Stamp slam -> Next scene`.
This is boring, formulaic, and slop.

### Study `src/vox_intro/VoxIntroV1.tsx` and `VoxIntro2.tsx`:
Look at what made those sequences electrifying:
1. **Dramatic Scale Contrasts**:
   In `VoxIntro`, a `£1,000` text doesn't politely fade in inside a small box. It enters **massive**, commanding the entire canvas, and then snaps down into perspective, revealing the landscape behind it.
2. **Rhythmic Visual Shifts (Unpredictability)**:
   - Beat 1: An oversized kinetic typography hit.
   - Beat 2: A torn Reddit quote receipt with masking tape (`camera_click.wav`).
   - Beat 3: A forensic 4-quadrant split-screen warning grid.
   - Beat 4: An authentic documentary photo collage.
   The viewer stays engaged because their brain **cannot predict what visual form the next thought will take**.
3. **Asymmetry & Depth**:
   Do not put every single card dead-center. Use off-axis angles (-3 deg, +4 deg), diagonal directional arrows, perspective shifts, and layered shadows (`filter: 'drop-shadow(0 20px 40px rgba(0,0,0,0.18))'`).

---

## 7. The Modular Spec Library: Living Blueprints, Not Rigid Molds

The repository contains 7 pre-built archetype specs under `src/specs/`:
- `Spec1_ProductSpec.tsx`: Hardware breakdown & internal tech specs
- `Spec2_RatingScore.tsx`: Community sentiment & rating scores
- `Spec3_Comparison.tsx`: Direct head-to-head showdown
- `Spec4_MetricTelemetry.tsx`: Live wattage, efficiency, and thermal meters
- `Spec5_QuoteReceipt.tsx`: Forum complaints, Reddit receipts, lab quotes
- `Spec6_StatementSpec.tsx`: Hard truths, warnings, bold facts
- `Spec7_SequentialEmphasis.tsx`: Multi-beat kinetic narrative emphasis

### The Duration Adaptation Law:
Specs were designed with default placeholder durations. In real production, **audio dictates the timeline**. You must adapt flexibly:

1. **When Audio is Shorter than the Spec (e.g. 10s spec needed for 4s audio)**:
   - ❌ **DO NOT** compress a 10-second multi-step animation into 4 seconds. It becomes an unreadable, frantic blur.
   - ✅ **DO SUBTRACT**: Extract *only the hero punchline* of that spec (e.g. just the highlighted quote card from `Spec5`, or just the delta bar from `Spec3`) and let it breathe cleanly for the 4 seconds.
2. **When Audio is Longer than the Spec (e.g. 3s spec needed for 7s audio)**:
   - ❌ **DO NOT** let the spec card sit completely frozen and static for the remaining 4 seconds.
   - ✅ **DO LAYER**: Let the card land at second 1; at second 3, an animated highlighter sweeps across the key phrase (`draw.wav`); at second 5, the camera slowly pushes in 3%; at second 6, a decisive stamp slams onto the corner (`stamp_slam.wav`). The visual continues to evolve with the narrator's thought.

### Upgrading Older Specs:
Note: Specs created early in the project may contain older font declarations (`Inter`) or generic backgrounds. When pulling components from `src/specs/`, **always upgrade them** to use:
- Fonts: `spaceGroteskFamily` and `ibmPlexMonoFamily` from `../design_system/fonts`
- Canonical Backgrounds: `#F8FAFC`, `#0A1224`, or `#05070B`.

---

## 8. Evidence Vault & Documented Receipts

When a script paragraph mentions:
- User complaints, criticisms, or forum discussions (e.g. *"Stream Ultra X owners report the same symptom"*),
- Lab test measurements (e.g. *"Notebookcheck measured losing roughly 12%"*),
- Early pricing rumors or subscription leaks...

**DO NOT invent generic text cards.** Check the project repository:
- `public/evidence/`
- `public/evidence_vault/`

We frequently have the **actual Reddit screenshot, lab graph, or forum post** documented as an image (e.g. `05_lab_notebookcheck_anker_charging_loss.png`). Bring in the real evidence graphic with an angled stamp slam (`stamp_slam.wav`) or use `Spec5_QuoteReceipt.tsx` to give the claim journalistic credibility.

---

## 9. Anti-AI Slop & Anti-Bloat Mandate (Zero-Bloat Rules with Code Diffs)

### ❌ BANNED: Decorative Top HUD Bars
Agents often add arbitrary tech headers at the top of the canvas to fill space. **This screams AI template.**
```tsx
// ❌ STRICTLY BANNED (AI SLOP):
<div style={{ position: 'absolute', top: 40, left: 72, right: 72, display: 'flex', justifyContent: 'space-between' }}>
  <div style={{ display: 'flex', gap: 14 }}>
    <div style={{ width: 12, height: 12, borderRadius: '50%', backgroundColor: '#38BDF8' }} />
    <span>ELECTRICAL EFFICIENCY & THERMAL AUDIT</span>
  </div>
  <div>ANKER SOLIX • LAB DISCHARGE AUDIT</div>
</div>
```
```tsx
// ✅ ACCEPTED BROADCAST STANDARD:
// Keep the top of the frame completely clean.
// ABSOLUTELY ZERO EYEBROWS, ZERO PILL BADGES, AND ZERO CATEGORY LABELS.
// Primary titles land on their own with authoritative typography and pure negative space.
```

### ❌ BANNED: Inventing Filler Text & Over-Explaining
```tsx
// ❌ STRICTLY BANNED:
<div style={{ display: 'flex', gap: 20 }}>
  <span>⏱️ Sustained Output @ High Ambient</span>
  <span>🛡️ Protects LiFePO4 Cell Chemistry</span>
  <span>🔇 100% Silent Operation</span>
</div>
```
**Golden Rule**: If the narrator did not speak it in the voiceover script, **DO NOT put it on the screen**. Users cannot read small multi-point bullet lists while listening to audio.

### ❌ BANNED: Nested Cards Inside Cards Inside Cards
Avoid wrapping boxes inside boxes inside boxes. Use direct physical objects, authentic hardware cutouts, high-contrast typography, or clean single-layer cards.

---

## 10. Audio-Visual Timing Math & The 9-Step Production Pipeline

### Broadcast Narration Math:
- Spoken broadcast pace = **135 to 140 words per minute** = **~2.25 words per second**.
- At 30fps: **1 spoken word ≈ 13.3 frames** | **1.0 second = 30 frames**.

### The 9-Step Execution Pipeline:
1. **Analyze Transcript**: Identify the key claims, criticisms, and metrics.
2. **Check Evidence Vault**: Search `public/evidence/` and `public/evidence_vault/` for real receipts or lab audits.
3. **Ideate 2–3 Concepts**: Brainstorm distinct visual metaphors (hardware focus, data focus, mixed media).
4. **Build Timing Map**: Break paragraph into 3–5 micro-scenes mapped to exact frame windows.
5. **Code with Progressive Disclosure**: Build in `src/production/` ensuring elements enter sequentially without pre-assembled layouts.
6. **Integrate Synchronous Foley**: Align audio cues (`swoosh.wav`, `click.wav`, `draw.wav`, `thud.wav`, `stamp_slam.wav`).
7. **Typecheck**: Run `cmd /c npx tsc --noEmit` in `C:\Users\user\OneDrive\Documents\antigravity-solar-remotion`. Must exit 0.
8. **Render & Purge Stills**: Render stills at key progressive beats, view with `view_file`, then purge all `.png` stills.
9. **Render Master & Mirror**: Render `.mp4` and copy to `..\antigravity-youtube-scrpt-machine-main\motion_clips\<Name>.mp4`.

---

## 11. Design Tokens, Typography & Synchronous Acoustic Foley

- **Canonical 3-Background Palette**:
  - `White Keynote Editorial`: `#F8FAFC` (dark charcoal text `#0F172A`)
  - `Checkered Blue Slate`: `#0A1224` (48px cyan grid `rgba(56, 189, 248, 0.08)` + slate texture overlay at 20% opacity)
  - `Deep Minimal Black`: `#05070B` (subtle warm amber radial glow, vivid telemetry metrics)
- **Typography**:
  - Primary Display / Headings: `spaceGroteskFamily`
  - Technical Data / Labels / Numbers: `ibmPlexMonoFamily`
- **Synchronous Foley SFX (`public/sfx/`)**:
  - `sfx/swoosh.wav`: Smooth spatial transitions, card glides, camera dollies.
  - `sfx/click.wav`: Electrical node latching, UI toggle, laser activation.
  - `sfx/pop.wav`: Small badge reveals, pill pop-ins, socket connection.
  - `sfx/thud.wav`: Solid hardware lock, heavy data arrival.
  - `sfx/stamp_slam.wav`: Decisive audit stamps, truth seals, warning banners.
  - `sfx/alert_beep.wav`: Energy drain, thermal warnings, parasitic loss alerts.
  - `sfx/draw.wav`: Highlighter sweeps, laser scans, oscilloscope curve drawings.
