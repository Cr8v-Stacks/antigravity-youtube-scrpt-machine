import os
import re
import sys
import json
import difflib
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

# Paths
MASTER_VIDEO = r"C:\Users\user\OneDrive\Documents\Adobe\Premiere Pro\23.0\EcoFlow vs Zendure vs Anker SOLIX.mp4"
FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
OUTPUT_DIR = os.path.abspath("shorts")
PREVIEW_DIR = os.path.join(OUTPUT_DIR, "previews")
TEMP_DIR = os.path.abspath("temp_shorts_build")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Candidate definitions
SHORTS_DATA = [
    {
        "id": "short_01_melted_mc4_connector",
        "title": "Melted Connectors on Balcony Solar? (Zendure SolarFlow 2400 AC)",
        "start": 927.03, # 15:27.03
        "end": 968.60,   # 16:08.60
        "duration": 41.57,
        "badge": "[!] HARDWARE VULNERABILITY // SAFETY AUDIT",
        "headline": "MELTED MC4 SOLAR CONNECTORS",
        "accent_hex": "#FFB300", # Zendure Sun Gold
        "accent_ass": "&H00B3FF&",
        "script": (
            "Zendure faces a confirmed hardware vulnerability on the SolarFlow 2400 AC. "
            "Numerous owners on Zendure's official community forums documented melted MC4 solar connectors. "
            "Symptoms include burning plastic smells, fused electrical joints, and sudden power cutoffs under heavy midday current. "
            "Imagine pulling the plug of a heavy-duty electric space heater out of the wall and finding the plastic casing soft and scorching hot to the touch. "
            "Zendure moderators acknowledged the issue as affecting a small percentage of units and handled replacements under warranty, "
            "but no mandatory safety recall was announced. No similar issue has appeared on the Hyper 2000."
        ),
        "preview_offsets": [(1.0, "01_hook_1s"), (12.0, "02_body_12s"), (30.0, "03_payoff_30s")]
    },
    {
        "id": "short_02_cold_battery_freeze_drop",
        "title": "Why Balcony Batteries Die in Winter (55% Loss at 12°C)",
        "start": 472.21, # 07:52.21
        "end": 504.90,   # 08:24.90
        "duration": 32.69,
        "badge": "[LAB AUDIT] REAL-WORLD EFFICIENCY LOSS",
        "headline": "WHY BALCONY BATTERIES DIE IN WINTER",
        "accent_hex": "#007AFF", # EcoFlow Electric Blue
        "accent_ass": "&HFF7A00&",
        "script": (
            "Marketing brochures claim maximum efficiency numbers recorded under laboratory room temperatures. "
            "Real-world testing tells a different story. Cold weather is where lithium chemistry generally struggles, "
            "and an outdoor balcony battery has nowhere to hide from it. The Stream Ultra X includes an internal heating element "
            "that activates below 5 degrees Celsius specifically to protect the cells from freezing. "
            "A tacit admission from EcoFlow that round-trip efficiency does take a real hit in cold conditions, even with that mitigation in place."
        ),
        "preview_offsets": [(1.0, "01_hook_1s"), (14.0, "02_body_14s"), (28.0, "03_payoff_28s")]
    },
    {
        "id": "short_03_midnight_solar_bug_paywall",
        "title": "Your Solar App is Lying to You (340W at Midnight Bug)",
        "start": 349.64, # 05:49.64
        "end": 400.57,   # 06:40.57
        "duration": 50.93,
        "badge": "[!] CLOUD TELEMETRY BUG // 2:15 AM",
        "headline": "PRODUCING SOLAR AT MIDNIGHT?",
        "accent_hex": "#00D6FF", # Cyan / Amber Warning
        "accent_ass": "&HFFD600&",
        "script": (
            "EcoFlow provides one of the most comprehensive, polished interfaces on the market. "
            "However, early adopters on community threads have documented occasional data hiccups. "
            "The app misreporting solar generation overnight, or conflicting charge state numbers after dark. "
            "It's a known pattern across EcoFlow's product line. The firmware doesn't always cleanly hand off from solar charging logic once the sun goes down, "
            "and some Stream Ultra X owners report the same symptom. On top of that, EcoFlow's AI dynamic tariff feature is currently described by owners, "
            "as behaving more like a reliable scheduled timer than true predictive intelligence. "
            "And there's early word that some advanced tariff tools may move behind a paid subscription tier. "
            "Nothing official or price confirmed yet. But worth knowing before you buy and expecting every smart feature to stay free."
        ),
        "preview_offsets": [(1.0, "01_hook_1s"), (20.0, "02_body_20s"), (40.0, "03_payoff_40s")]
    }
]

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def create_header_overlay(badge_text, headline_text, accent_hex, output_png):
    """Generates a 1080x420 transparent PNG header card with badge and accent divider."""
    img = Image.new("RGBA", (1080, 420), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font_badge = ImageFont.truetype("arialbd.ttf", 24)
        font_head = ImageFont.truetype("arialbd.ttf", 40)
    except:
        font_badge = ImageFont.load_default()
        font_head = ImageFont.load_default()

    accent_rgb = hex_to_rgb(accent_hex)

    # Semi-transparent dark background card in safe zone (Y: 190 to 395)
    card_box = [60, 190, 1020, 395]
    draw.rounded_rectangle(card_box, radius=18, fill=(11, 15, 23, 230), outline=(40, 50, 65, 255), width=2)

    # Badge Pill (Y: 216 to 258)
    badge_w = draw.textlength(badge_text, font=font_badge) + 32
    badge_x1 = int(540 - badge_w / 2)
    badge_x2 = int(540 + badge_w / 2)
    draw.rounded_rectangle([badge_x1, 216, badge_x2, 258], radius=10, fill=(20, 26, 38, 255), outline=accent_rgb, width=2)
    draw.text((540, 237), badge_text, font=font_badge, fill=accent_rgb, anchor="mm")

    # Headline text (Y: 325)
    draw.text((540, 325), headline_text, font=font_head, fill=(255, 255, 255, 255), anchor="mm")

    # Crisp divider line at Y=418 with accent glow
    draw.line([(0, 417), (1080, 417)], fill=(0, 0, 0, 220), width=4)
    draw.line([(0, 418), (1080, 418)], fill=accent_rgb, width=2)

    img.save(output_png)
    print(f"Created header overlay: {output_png}")

def format_ass_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def transcribe_and_align(audio_path, script_text, short_duration):
    """Transcribes audio using faster-whisper and aligns with ground-truth script words."""
    from faster_whisper import WhisperModel
    print("Loading faster-whisper model (tiny.en)...")
    model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio_path, word_timestamps=True)
    
    whisper_words = []
    for seg in segments:
        for w in seg.words:
            clean_w = re.sub(r"[^\w\d€%°]", "", w.word.strip()).lower()
            if clean_w:
                whisper_words.append({
                    "raw": w.word.strip(),
                    "clean": clean_w,
                    "start": max(0.0, min(w.start, short_duration)),
                    "end": max(0.0, min(w.end, short_duration))
                })

    # Ground truth script words
    script_raw_words = script_text.split()
    script_words = []
    for w in script_raw_words:
        clean_w = re.sub(r"[^\w\d€%°]", "", w.strip()).lower()
        if clean_w:
            script_words.append({"raw": w.strip(), "clean": clean_w})

    # Alignment using SequenceMatcher
    matcher = difflib.SequenceMatcher(
        None,
        [w["clean"] for w in script_words],
        [w["clean"] for w in whisper_words]
    )

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
            next_start = whisper_words[j2]["start"] if j2 < len(whisper_words) else short_duration
            span = max(0.2, (next_start - prev_end) / max(1, i2 - i1))
            for k, si in enumerate(range(i1, i2)):
                aligned_words.append({
                    "word": script_words[si]["raw"],
                    "start": prev_end + k * span,
                    "end": min(short_duration, prev_end + (k + 1) * span)
                })

    if len(aligned_words) < len(script_words) * 0.7:
        aligned_words = [{"word": w["raw"], "start": w["start"], "end": w["end"]} for w in whisper_words]

    # Strictly enforce chronological monotonicity and clean non-overlapping boundaries
    for i in range(len(aligned_words)):
        if i > 0:
            if aligned_words[i]["start"] < aligned_words[i-1]["end"]:
                aligned_words[i]["start"] = aligned_words[i-1]["end"]
        if aligned_words[i]["end"] <= aligned_words[i]["start"]:
            aligned_words[i]["end"] = min(short_duration, aligned_words[i]["start"] + 0.25)
        aligned_words[i]["start"] = max(0.0, min(aligned_words[i]["start"], short_duration - 0.1))
        aligned_words[i]["end"] = max(aligned_words[i]["start"] + 0.1, min(aligned_words[i]["end"], short_duration))

    return aligned_words

def build_ass_subtitles(aligned_words, ass_path, short_duration, highlight_color_ass="&H00D6FF&"):
    """Creates a high-retention word-by-word active highlighted ASS subtitle file with strictly non-overlapping events."""
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
            text_line = " ".join(line_parts)
            events.append(f"Dialogue: 0,{format_ass_time(w_start)},{format_ass_time(w_end)},ActiveShorts,,0,0,0,,{text_line}")

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events) + "\n")
    print(f"Generated ASS subtitles: {ass_path} ({len(events)} events)")

def render_short(cfg):
    """Executes the full reframing, compositing, and rendering pipeline for one Short."""
    short_id = cfg["id"]
    print(f"\n=======================================================")
    print(f"PROCESSING: {short_id}")
    print(f"=======================================================")

    temp_audio = os.path.join(TEMP_DIR, f"{short_id}_audio.wav")
    header_png = os.path.join(TEMP_DIR, f"{short_id}_header.png")
    ass_path = os.path.join(TEMP_DIR, f"{short_id}.ass")
    output_mp4 = os.path.join(OUTPUT_DIR, f"{short_id}.mp4")

    # Step 1: Extract Audio Slice
    print(f"1. Extracting audio ({cfg['start']}s -> {cfg['end']}s)...")
    cmd_audio = [
        FFMPEG_EXE, "-ss", str(cfg["start"]), "-to", str(cfg["end"]),
        "-i", MASTER_VIDEO, "-vn", "-ac", "1", "-ar", "16000", "-y", temp_audio
    ]
    subprocess.run(cmd_audio, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    # Step 2: Transcribe and Build ASS Subtitles
    print("2. Transcribing with word timestamps...")
    words = transcribe_and_align(temp_audio, cfg["script"], cfg["duration"])
    build_ass_subtitles(words, ass_path, cfg["duration"], cfg["accent_ass"])

    # Step 3: Create Header Overlay Card
    print("3. Generating header overlay card...")
    create_header_overlay(cfg["badge"], cfg["headline"], cfg["accent_hex"], header_png)

    # Step 4: Full Reframing & Render
    print("4. Compositing and rendering 1080x1920 Short...")
    escaped_ass = ass_path.replace("\\", "/").replace(":", "\\:")
    escaped_header = header_png.replace("\\", "/").replace(":", "\\:")

    filter_complex = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5,eq=brightness=-0.22[bg];"
        f"[0:v]crop=1080:1080:420:0[fg];"
        f"[bg][fg]overlay=0:420[comp1];"
        f"[comp1][1:v]overlay=0:0[comp2];"
        f"[comp2]ass='{escaped_ass}'[v]"
    )

    cmd_render = [
        FFMPEG_EXE,
        "-ss", str(cfg["start"]), "-to", str(cfg["end"]), "-i", MASTER_VIDEO,
        "-loop", "1", "-i", header_png,
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "0:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", str(cfg["duration"]),
        "-y", output_mp4
    ]
    res = subprocess.run(cmd_render, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace")
    if res.returncode != 0:
        print("Rendering failed! Stderr:", res.stderr[-800:])
        raise RuntimeError(f"Rendering failed for {short_id}")

    print(f"SUCCESS: Rendered {output_mp4} ({os.path.getsize(output_mp4) / 1024 / 1024:.2f} MB)")

    # Step 5: Verification Preview Frames
    preview_subfolder = os.path.join(PREVIEW_DIR, short_id)
    os.makedirs(preview_subfolder, exist_ok=True)
    print("5. Generating validation preview frames...")
    preview_offsets = cfg.get("preview_offsets", [(1.0, "01_hook_1s"), (15.0, "02_body_15s"), (30.0, "03_payoff_30s")])
    for sec_offset, label in preview_offsets:
        out_frame = os.path.join(preview_subfolder, f"preview_{label}.jpg")
        cmd_prev = [
            FFMPEG_EXE, "-ss", str(sec_offset), "-i", output_mp4,
            "-vframes", "1", "-q:v", "2", "-y", out_frame
        ]
        subprocess.run(cmd_prev, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        overlay_qc = os.path.join(preview_subfolder, f"preview_{label}_safezone_qc.jpg")
        draw_safe_zone_qc(out_frame, overlay_qc)

    print(f"Validation frames saved to: {preview_subfolder}")

def draw_safe_zone_qc(src_jpg, dst_jpg):
    """Draws YouTube Shorts UI overlays to verify safe zones."""
    im = Image.open(src_jpg).convert("RGBA")
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # YouTube Right buttons danger zone (X > 960, Y: 700 to 1500)
    d.rectangle([960, 700, 1080, 1500], fill=(255, 0, 0, 40), outline=(255, 0, 0, 180), width=2)
    # YouTube Bottom channel metadata danger zone (Y > 1520)
    d.rectangle([0, 1520, 1080, 1920], fill=(255, 0, 0, 50), outline=(255, 0, 0, 180), width=2)
    # YouTube Top status bar zone (Y < 180)
    d.rectangle([0, 0, 1080, 180], fill=(255, 0, 0, 30), outline=(255, 0, 0, 120), width=2)

    # Safe Zone Green Box (X: 80 to 960, Y: 180 to 1520)
    d.rectangle([80, 180, 960, 1520], outline=(0, 255, 100, 220), width=3)

    combined = Image.alpha_composite(im, overlay)
    combined.convert("RGB").save(dst_jpg, quality=92)

def main():
    print("==========================================================")
    print("AUTONOMOUS YOUTUBE SHORTS GENERATION & REFRAMING ENGINE")
    print("==========================================================")
    for cfg in SHORTS_DATA:
        render_short(cfg)
    print("\nALL 3 YOUTUBE SHORTS SUCCESSFULLY PROCESSED AND VERIFIED!")

if __name__ == "__main__":
    main()
