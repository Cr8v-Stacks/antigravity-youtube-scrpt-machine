import os
import re
import sys
import json
import difflib
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

WORK_DIR = os.path.abspath("shorts/build_vattenfall")
OUTPUT_DIR = os.path.abspath("shorts")
PREVIEW_DIR = os.path.join(OUTPUT_DIR, "previews", "short_vattenfall_wind_turbine_house")
os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)

AUDIO_FILE = os.path.abspath("temp_media_vattenfall/voiceover_57s.wav")
FINAL_MP4 = os.path.join(OUTPUT_DIR, "short_vattenfall_wind_turbine_house.mp4")

SCRIPT_TEXT = (
    "Critics always claim retired wind turbines are impossible to recycle. "
    "So this Swedish company decided to prove them wrong by turning them into luxury tiny houses and Alpine skis. "
    "Swedish energy giant Vattenfall took a 10-meter nacelle, the bus-sized capsule from the top of an Austrian turbine, "
    "and converted it into a 350-square-foot luxury home. "
    "Engineered to survive 25 years of hurricane gales, the shell is already aerodynamic, watertight, and fully insulated. "
    "Inside, it's fitted with a modern kitchen, bathroom, heat pump, and rooftop solar. "
    "And the blades? 57 decommissioned blades were mounted as the architectural facade of a multi-storey car park in Sweden. "
    "While in Norway, ski maker EVI uses thermal pyrolysis to cleanly extract carbon fibers from old blades, forging ultralight alpine skis. "
    "They're even testing new blades that dissolve in mild acid so the fibers can be reused forever. "
    "Over 90% of a turbine is steel that gets melted down. But turning the rest into homes and skis proves nothing has to go to waste."
)

SCENES = [
    {
        "name": "01_hook_criticism",
        "start": 0.0,
        "end": 4.2,
        "media": "temp_media_vattenfall/vframe_22s.jpg",
        "badge": "[!] CRITICISM // LANDFILL MYTH",
        "headline": "CAN'T RECYCLE WIND TURBINES?",
        "accent_hex": "#FF3B30", # Warning Red
        "zoom": "in"
    },
    {
        "name": "02_hook_payoff",
        "start": 4.2,
        "end": 9.5,
        "media": "temp_media_vattenfall/nacelle_exterior.jpg",
        "badge": "SWEDISH INNOVATION // VATTENFALL",
        "headline": "TINY HOMES & ALPINE SKIS",
        "accent_hex": "#00D6FF", # Nordic Cyan
        "zoom": "out"
    },
    {
        "name": "03_nacelle_exterior",
        "start": 9.5,
        "end": 19.0,
        "media": "temp_media_vattenfall/nacelle_exterior.jpg",
        "badge": "10M TURBINE NACELLE // RETIRED AUSTRIAN UNIT",
        "headline": "350 SQ FT LUXURY TINY HOUSE",
        "accent_hex": "#FFCC00", # Swedish Gold
        "zoom": "in"
    },
    {
        "name": "04_nacelle_interior",
        "start": 19.0,
        "end": 28.5,
        "media": "temp_media_vattenfall/nacelle_interior.jpg",
        "badge": "HURRICANE-PROOF // FULLY INSULATED",
        "headline": "KITCHEN, HEAT PUMP & SOLAR",
        "accent_hex": "#00D6FF",
        "zoom": "in"
    },
    {
        "name": "05_carpark_facade",
        "start": 28.5,
        "end": 38.5,
        "media": "temp_media_vattenfall/carpark_facade_or_house.jpg",
        "badge": "57 RETIRED BLADES // LUND, SWEDEN",
        "headline": "MULTI-STOREY CARPARK FACADE",
        "accent_hex": "#FF9500",
        "zoom": "out"
    },
    {
        "name": "06_skis_pyrolysis",
        "start": 38.5,
        "end": 47.5,
        "media": "temp_media_vattenfall/skis_or_materials.jpg",
        "badge": "THERMAL PYROLYSIS // EVI SKI NORWAY",
        "headline": "RECLAIMED CARBON FIBER SKIS",
        "accent_hex": "#00D6FF",
        "zoom": "in"
    },
    {
        "name": "07_closing_circular",
        "start": 47.5,
        "end": 57.65,
        "media": "temp_media_vattenfall/nacelle_exterior.jpg",
        "badge": "100% CIRCULAR FUTURE // ZERO WASTE",
        "headline": "REBORN, NOT BURIED.",
        "accent_hex": "#34C759", # Clean Green
        "zoom": "out"
    }
]

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def hex_to_ass(hex_str):
    hex_str = hex_str.lstrip('#')
    r, g, b = hex_str[0:2], hex_str[2:4], hex_str[4:6]
    return f"&H00{b}{g}{r}&"

def format_ass_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def create_header_overlay(badge_text, headline_text, accent_hex, output_png):
    img = Image.new("RGBA", (1080, 420), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    try:
        font_badge = ImageFont.truetype("arialbd.ttf", 24)
        font_head = ImageFont.truetype("arialbd.ttf", 38)
    except:
        font_badge = ImageFont.load_default()
        font_head = ImageFont.load_default()

    accent_rgb = hex_to_rgb(accent_hex)
    card_box = [50, 190, 1030, 395]
    draw.rounded_rectangle(card_box, radius=18, fill=(11, 15, 23, 235), outline=(40, 50, 65, 255), width=2)

    badge_w = draw.textlength(badge_text, font=font_badge) + 32
    badge_x1 = int(540 - badge_w / 2)
    badge_x2 = int(540 + badge_w / 2)
    draw.rounded_rectangle([badge_x1, 216, badge_x2, 258], radius=10, fill=(20, 26, 38, 255), outline=accent_rgb, width=2)
    draw.text((540, 237), badge_text, font=font_badge, fill=accent_rgb, anchor="mm")

    draw.text((540, 325), headline_text, font=font_head, fill=(255, 255, 255, 255), anchor="mm")
    draw.line([(0, 417), (1080, 417)], fill=(0, 0, 0, 220), width=4)
    draw.line([(0, 418), (1080, 418)], fill=accent_rgb, width=2)

    img.save(output_png)

def generate_subtitles():
    from faster_whisper import WhisperModel
    print("1. Transcribing audio with word-level timestamps...")
    model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(AUDIO_FILE, word_timestamps=True)

    whisper_words = []
    for s in segments:
        for w in s.words:
            clean_w = re.sub(r"[^\w\d€%°]", "", w.word.strip()).lower()
            if clean_w:
                whisper_words.append({
                    "raw": w.word.strip(),
                    "clean": clean_w,
                    "start": max(0.0, min(w.start, 57.65)),
                    "end": max(0.0, min(w.end, 57.65))
                })

    script_raw_words = SCRIPT_TEXT.split()
    script_words = []
    for w in script_raw_words:
        clean_w = re.sub(r"[^\w\d€%°]", "", w.strip()).lower()
        if clean_w:
            script_words.append({"raw": w.strip(), "clean": clean_w})

    matcher = difflib.SequenceMatcher(None, [w["clean"] for w in script_words], [w["clean"] for w in whisper_words])
    aligned_words = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for si, wj in zip(range(i1, i2), range(j1, j2)):
                aligned_words.append({
                    "word": script_words[si]["raw"],
                    "start": whisper_words[wj]["start"],
                    "end": whisper_words[wj]["end"]
                })
        elif tag in ("replace", "delete"):
            prev_end = whisper_words[j1-1]["end"] if j1 > 0 and j1-1 < len(whisper_words) else 0.0
            next_start = whisper_words[j2]["start"] if j2 < len(whisper_words) else 57.65
            span = max(0.2, (next_start - prev_end) / max(1, i2 - i1))
            for k, si in enumerate(range(i1, i2)):
                aligned_words.append({
                    "word": script_words[si]["raw"],
                    "start": prev_end + k * span,
                    "end": min(57.65, prev_end + (k + 1) * span)
                })

    if len(aligned_words) < len(script_words) * 0.7:
        aligned_words = [{"word": w["raw"], "start": w["start"], "end": w["end"]} for w in whisper_words]

    for i in range(len(aligned_words)):
        if i > 0 and aligned_words[i]["start"] < aligned_words[i-1]["end"]:
            aligned_words[i]["start"] = aligned_words[i-1]["end"]
        if aligned_words[i]["end"] <= aligned_words[i]["start"]:
            aligned_words[i]["end"] = min(57.65, aligned_words[i]["start"] + 0.25)

    ass_path = os.path.join(WORK_DIR, "subtitles.ass")
    highlight_color_ass = "&H00D6FF&" # Cyan highlight
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ActiveShorts,Arial,52,&H00FFFFFF,{highlight_color_ass},&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,4.5,2,2,80,120,480,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    chunk_size = 4
    chunks = [aligned_words[i:i + chunk_size] for i in range(0, len(aligned_words), chunk_size)]
    for chunk in chunks:
        if not chunk:
            continue
        for active_idx, target_word in enumerate(chunk):
            w_start = target_word["start"]
            w_end = target_word["end"]
            if w_end <= w_start:
                w_end = w_start + 0.25
            line_parts = []
            for idx, item in enumerate(chunk):
                raw_w = item["word"].upper()
                if idx == active_idx:
                    line_parts.append(f"{{\\c{highlight_color_ass}\\fscx108\\fscy108}}{raw_w}{{\\c&H00FFFFFF&\\fscx100\\fscy100}}")
                else:
                    line_parts.append(raw_w)
            events.append(f"Dialogue: 0,{format_ass_time(w_start)},{format_ass_time(w_end)},ActiveShorts,,0,0,0,,{' '.join(line_parts)}")

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events) + "\n")
    print(f"Subtitles generated: {ass_path} ({len(events)} events)")
    return ass_path

def build_scene_clip(scene, idx):
    dur = scene["end"] - scene["start"]
    out_mp4 = os.path.join(WORK_DIR, f"scene_{idx}_{scene['name']}.mp4")
    header_png = os.path.join(WORK_DIR, f"header_{idx}.png")
    create_header_overlay(scene["badge"], scene["headline"], scene["accent_hex"], header_png)

    # Ambient canvas background + 1080x1080 center foreground + header
    # Ken burns zoom
    fps = 30
    frames = int(dur * fps)
    if scene["zoom"] == "in":
        z_expr = f"min(zoom+0.0006,1.15)"
    else:
        z_expr = f"max(1.15-0.0006*on,1.0)"

    escaped_hdr = header_png.replace("\\", "/").replace(":", "\\:")

    filter_graph = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5,eq=brightness=-0.22[bg];"
        f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1080:1080:(iw-1080)/2:(ih-1080)/2,"
        f"zoompan=z='{z_expr}':d={frames}:s=1080x1080:fps={fps}[fg];"
        f"[bg][fg]overlay=0:420[comp1];"
        f"[comp1][1:v]overlay=0:0[v]"
    )

    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1", "-t", str(dur), "-i", scene["media"],
        "-loop", "1", "-t", str(dur), "-i", header_png,
        "-filter_complex", filter_graph,
        "-map", "[v]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-r", str(fps),
        "-t", str(dur),
        out_mp4
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print(f"Rendered scene {idx}: {out_mp4} ({dur:.2f}s)")
    return out_mp4

def draw_safe_zone_qc(src_jpg, dst_jpg):
    im = Image.open(src_jpg).convert("RGBA")
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # YouTube Right buttons danger zone (X > 960, Y: 700 to 1500)
    d.rectangle([960, 700, 1080, 1500], fill=(255, 0, 0, 40), outline=(255, 0, 0, 180), width=2)
    # YouTube Bottom metadata zone (Y > 1520)
    d.rectangle([0, 1520, 1080, 1920], fill=(255, 0, 0, 50), outline=(255, 0, 0, 180), width=2)
    # Top status zone (Y < 180)
    d.rectangle([0, 0, 1080, 180], fill=(255, 0, 0, 30), outline=(255, 0, 0, 120), width=2)
    # Safe Zone Box (X: 80 to 960, Y: 180 to 1520)
    d.rectangle([80, 180, 960, 1520], outline=(0, 255, 100, 220), width=3)

    combined = Image.alpha_composite(im, overlay)
    combined.convert("RGB").save(dst_jpg, quality=92)

def main():
    print("==========================================================")
    print("PRODUCING 60-SECOND VATTENFALL WIND TURBINE SHORT")
    print("==========================================================")
    ass_file = generate_subtitles()

    # Build individual scene video clips
    scene_clips = []
    concat_txt = os.path.join(WORK_DIR, "concat_scenes.txt")
    with open(concat_txt, "w") as f:
        for idx, sc in enumerate(SCENES):
            c_path = build_scene_clip(sc, idx)
            scene_clips.append(c_path)
            f.write(f"file '{c_path.replace(chr(92), '/')}'\n")

    # Concat all scenes together
    raw_video = os.path.join(WORK_DIR, "raw_concatenated.mp4")
    cmd_concat = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy", raw_video
    ]
    subprocess.run(cmd_concat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print("Scenes concatenated cleanly!")

    # Mux with voiceover audio and apply ASS subtitles
    print("Compositing master deliverable with audio & ASS subtitles...")
    escaped_ass = ass_file.replace("\\", "/").replace(":", "\\:")
    cmd_final = [
        FFMPEG_EXE, "-y",
        "-i", raw_video,
        "-i", AUDIO_FILE,
        "-vf", f"ass='{escaped_ass}'",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-shortest",
        FINAL_MP4
    ]
    res = subprocess.run(cmd_final, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("Final render failed! Stderr:\n", res.stderr[-800:])
        sys.exit(1)

    final_size_mb = os.path.getsize(FINAL_MP4) / 1024 / 1024
    print(f"\nSUCCESS! Master Short rendered to:\n{FINAL_MP4} ({final_size_mb:.2f} MB)")

    # Safe-zone QC previews at key moments
    print("Generating safe-zone QC preview frames...")
    qc_moments = [(2.0, "01_hook"), (14.0, "02_pod_exterior"), (24.0, "03_interior_apartment"), (34.0, "04_facade"), (44.0, "05_skis"), (54.0, "06_circular_verdict")]
    for sec, lbl in qc_moments:
        out_jpg = os.path.join(PREVIEW_DIR, f"preview_{lbl}.jpg")
        out_qc = os.path.join(PREVIEW_DIR, f"preview_{lbl}_safezone_qc.jpg")
        subprocess.run([FFMPEG_EXE, "-y", "-ss", str(sec), "-i", FINAL_MP4, "-vframes", "1", "-q:v", "2", out_jpg], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        draw_safe_zone_qc(out_jpg, out_qc)

    print(f"QC frames saved to: {PREVIEW_DIR}")

if __name__ == "__main__":
    main()
