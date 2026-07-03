# Remotion Video Automation Pipeline

This directory contains the automated program for transforming our generated YouTube Shorts production packs and image assets into vertical `1080x1920` video files with custom subtitles and slide transitions.

---

## 🚀 Quick Start Workflow

### 1. Parse a Production Pack & Assets
To load the timeline timestamps, narration texts, and copy matched image assets into the video compiler, run:
```bash
# General Command
npm run prepare-video <pack_name_prefix>

# Example: For Cadaver Synod
npm run prepare-video cadaver_synod
```
*This parses `production-packs/cadaver_synod_shorts_pack.md`, copies the matched generated PNGs from `production-packs/cadaver_synod_images/` into Remotion's public folder, and compiles `src/video-data.json`.*

### 2. Live Preview the Video
To review the slides, transitions, and styled subtitle captions live in a local browser editor, run:
```bash
npm run dev
```
*This opens the Remotion Studio at `http://localhost:3000` where you can play the video frame-by-frame and preview the visual styling.*

### 3. Render the Video to MP4
To export the final high-retention video file (`out.mp4`), run:
```bash
npm run render-video
```
*This runs the headless chromium compiler to render the timeline into a finished video file.*

---

## 🛠️ Folder Structure

*   `scripts/prepare-video.js`: Node.js compiler that bridges the markdown files, image folders, and Remotion.
*   `src/video-data.json`: The compiled timeline data structure containing frame timings, captions, and source routes.
*   `src/Root.tsx`: Mounts the video canvas and sets dynamic framerates/duration.
*   `src/Composition.tsx`: React component rendering the images and styled subtitles overlays.
