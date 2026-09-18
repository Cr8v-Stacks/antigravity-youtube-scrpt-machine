import os
import re
import sys
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

WORK_DIR = os.path.abspath("shorts/build_vattenfall_v2")
OUTPUT_DIR = os.path.abspath("shorts")
PREVIEW_DIR = os.path.join(OUTPUT_DIR, "previews", "short_vattenfall_v2")
os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)

AUDIO_WAV = os.path.abspath("temp_media_vattenfall/voiceover_andrew_57s.wav")
WORDS_JSON = os.path.abspath("temp_media_vattenfall/andrew_words.json")
FINAL_MP4 = os.path.join(OUTPUT_DIR, "short_vattenfall_wind_turbine_house_v2.mp4")

CUTS = [
    # 1. Hook / Landfill Myth
    {"name": "01_casper_landfill", "start": 0.00, "end": 2.00, "type": "image", "src": "temp_media_vattenfall/casper_blade_landfill.jpg", "zoom": "in"},
    {"name": "02_blade_yard", "start": 2.00, "end": 3.80, "type": "image", "src": "temp_media_vattenfall/blade_storage_yard.jpg", "zoom": "out"},
    # 2. Swedish Innovation / Offshore Wind
    {"name": "03_offshore_turbine", "start": 3.80, "end": 6.40, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_00.mp4"},
    {"name": "04_turbine_sweep", "start": 6.40, "end": 9.10, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_01.mp4"},
    # 3. 10m Nacelle & Tiny House Pod
    {"name": "05_nacelle_crane", "start": 9.10, "end": 12.00, "type": "image", "src": "temp_media_vattenfall/nacelle_crane.jpg", "zoom": "in"},
    {"name": "06_nacelle_pod_reveal", "start": 12.00, "end": 15.00, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_02.mp4"},
    {"name": "07_nacelle_exterior_photo", "start": 15.00, "end": 18.20, "type": "image", "src": "temp_media_vattenfall/nacelle_exterior.jpg", "zoom": "out"},
    # 4. Scandinavian Interior & Eco Tech
    {"name": "08_interior_living", "start": 18.20, "end": 20.80, "type": "image", "src": "temp_media_vattenfall/nacelle_interior.jpg", "zoom": "in"},
    {"name": "09_interior_kitchen", "start": 20.80, "end": 23.50, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_03.mp4"},
    {"name": "10_heat_pump", "start": 23.50, "end": 25.50, "type": "image", "src": "temp_media_vattenfall/heat_pump.jpg", "zoom": "in"},
    {"name": "11_solar_panels", "start": 25.50, "end": 27.50, "type": "image", "src": "temp_media_vattenfall/solar_panels.jpg", "zoom": "out"},
    # 5. Lund Car Park Facade (57 blades)
    {"name": "12_lund_exterior_video", "start": 27.50, "end": 30.50, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_04.mp4"},
    {"name": "13_lund_facade_photo", "start": 30.50, "end": 34.00, "type": "image", "src": "temp_media_vattenfall/carpark_facade_or_house.jpg", "zoom": "in"},
    {"name": "14_lund_blade_detail", "start": 34.00, "end": 37.00, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_05.mp4"},
    # 6. Norway EVI Skis & Pyrolysis
    {"name": "15_ski_workshop_video", "start": 37.00, "end": 40.00, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_06.mp4"},
    {"name": "16_ski_grinding_sparks", "start": 40.00, "end": 43.00, "type": "image", "src": "temp_media_vattenfall/skis_or_materials.jpg", "zoom": "in"},
    {"name": "17_ski_craft_detail", "start": 43.00, "end": 46.00, "type": "image", "src": "temp_media_vattenfall/skis_or_materials.jpg", "zoom": "out"},
    # 7. Circular Future & Verdict
    {"name": "18_circular_turbine", "start": 46.00, "end": 49.50, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_01.mp4"},
    {"name": "19_steel_recovery", "start": 49.50, "end": 53.00, "type": "image", "src": "temp_media_vattenfall/blade_storage_yard.jpg", "zoom": "in"},
    {"name": "20_reborn_hero", "start": 53.00, "end": 57.62, "type": "video", "src": "temp_media_vattenfall/video_clips/clip_02.mp4"}
]

def format_ass_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def generate_subtitles():
    with open(WORDS_JSON, "r", encoding="utf-8") as f:
        words = json.load(f)
        
    ass_path = os.path.join(WORK_DIR, "subtitles_v2.ass")
    
    # ASS Header with Center Alignment (Alignment=5 is Center-Middle)
    header = (
        "[Script Info]\n"
        "Title: Vattenfall Wind Turbine Short V2\n"
        "ScriptType: v4.00+\n"
        "PlayResX: 1080\n"
        "PlayResY: 1920\n"
        "ScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Default,Arial Black,72,&H00FFFFFF,&H0000E5FF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,5,2,5,80,80,0,1\n\n"
        "[Events]\n"
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    
    # Group words into punchy bursts of 2-3 words max
    groups = []
    current_group = []
    for w in words:
        current_group.append(w)
        if len(current_group) >= 3 or w["word"].endswith((".", "?", "!", ",")):
            groups.append(current_group)
            current_group = []
    if current_group:
        groups.append(current_group)
        
    events = []
    for grp in groups:
        for idx, active_w in enumerate(grp):
            t_start = active_w["start"]
            t_end = active_w["end"]
            if t_end <= t_start:
                t_end = t_start + 0.20
            
            # Format line: all words white, active word electric yellow
            line_parts = []
            for j, w in enumerate(grp):
                cleaned = w["word"].upper()
                if j == idx:
                    line_parts.append(f"{{\\c&H0000E5FF&}}{cleaned}{{\\c&H00FFFFFF&}}")
                else:
                    line_parts.append(f"{{\\c&H00FFFFFF&}}{cleaned}")
            text = " ".join(line_parts)
            s_str = format_ass_time(t_start)
            e_str = format_ass_time(t_end)
            events.append(f"Dialogue: 0,{s_str},{e_str},Default,,0,0,0,,{text}")
            
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events) + "\n")
    print(f"Subtitles generated: {ass_path} ({len(events)} events)")
    return ass_path

def build_cut(cut, idx):
    dur = cut["end"] - cut["start"]
    out_mp4 = os.path.join(WORK_DIR, f"cut_{idx:02d}_{cut['name']}.mp4")
    fps = 30
    frames = int(dur * fps)
    
    if cut["type"] == "video":
        # Video clip: loop or trim to exact duration, scale & crop to full 1080x1920
        # No blurred borders! Full vertical screen fill!
        filter_graph = (
            f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920:(iw-1080)/2:(ih-1920)/2,fps={fps}[v]"
        )
        cmd = [
            FFMPEG_EXE, "-y",
            "-stream_loop", "3",
            "-ss", "0.5",
            "-t", str(dur),
            "-i", cut["src"],
            "-filter_complex", filter_graph,
            "-map", "[v]",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", str(fps),
            "-t", str(dur),
            out_mp4
        ]
    else:
        # High-res Image: Ken Burns zoom/pan to full 1080x1920
        if cut.get("zoom") == "in":
            z_expr = "min(zoom+0.0008,1.20)"
        else:
            z_expr = "max(1.20-0.0008*on,1.0)"
            
        filter_graph = (
            f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920:(iw-1080)/2:(ih-1920)/2,"
            f"zoompan=z='{z_expr}':d={frames}:s=1080x1920:fps={fps}[v]"
        )
        cmd = [
            FFMPEG_EXE, "-y",
            "-loop", "1", "-t", str(dur), "-i", cut["src"],
            "-filter_complex", filter_graph,
            "-map", "[v]",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-r", str(fps),
            "-t", str(dur),
            out_mp4
        ]
        
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print(f"Rendered cut {idx:02d}: {out_mp4} ({dur:.2f}s)")
    return out_mp4

def draw_safe_zone_qc(src_jpg, dst_jpg):
    im = Image.open(src_jpg).convert("RGBA")
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    # YouTube Right buttons (X > 960, Y: 700 to 1500)
    d.rectangle([960, 700, 1080, 1500], fill=(255, 0, 0, 40), outline=(255, 0, 0, 180), width=2)
    # Bottom metadata (Y > 1520)
    d.rectangle([0, 1520, 1080, 1920], fill=(255, 0, 0, 50), outline=(255, 0, 0, 180), width=2)
    # Top status bar (Y < 180)
    d.rectangle([0, 0, 1080, 180], fill=(255, 0, 0, 30), outline=(255, 0, 0, 120), width=2)
    # Center Subtitle Safe Zone Box (X: 100 to 980, Y: 850 to 1100)
    d.rectangle([100, 850, 980, 1100], outline=(0, 255, 255, 220), width=3)
    combined = Image.alpha_composite(im, overlay)
    combined.convert("RGB").save(dst_jpg, quality=92)

def main():
    print("==========================================================")
    print("PRODUCING V2: 60S VATTENFALL SHORT (ANDREW, FULL-SCREEN, CENTER SUBS)")
    print("==========================================================")
    ass_file = generate_subtitles()

    # Build individual video cut segments
    cut_clips = []
    concat_txt = os.path.join(WORK_DIR, "concat_cuts.txt")
    with open(concat_txt, "w") as f:
        for idx, c in enumerate(CUTS):
            c_path = build_cut(c, idx)
            cut_clips.append(c_path)
            f.write(f"file '{c_path.replace(chr(92), '/')}'\n")

    # Concat all cuts together
    raw_video = os.path.join(WORK_DIR, "raw_cuts_concat.mp4")
    cmd_concat = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy",
        raw_video
    ]
    subprocess.run(cmd_concat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print("Concatenated all 20 cuts:", raw_video)

    # Burn subtitles and mux audio
    escaped_ass = ass_file.replace("\\", "/").replace(":", "\\:")
    cmd_burn = [
        FFMPEG_EXE, "-y",
        "-i", raw_video,
        "-i", AUDIO_WAV,
        "-vf", f"subtitles='{escaped_ass}'",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        FINAL_MP4
    ]
    subprocess.run(cmd_burn, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print("MASTER SHORT V2 RENDERED:", FINAL_MP4)

    # QC Previews
    checkpoints = [
        ("preview_01_hook_landfill", 1.0),
        ("preview_02_offshore_turbine", 5.0),
        ("preview_03_nacelle_crane", 10.5),
        ("preview_04_pod_interior", 19.5),
        ("preview_05_lund_facade", 32.0),
        ("preview_06_ski_workshop", 41.5),
        ("preview_07_circular_verdict", 54.0)
    ]
    for name, ts in checkpoints:
        clean_jpg = os.path.join(PREVIEW_DIR, f"{name}.jpg")
        qc_jpg = os.path.join(PREVIEW_DIR, f"{name}_safezone_qc.jpg")
        cmd_thumb = [
            FFMPEG_EXE, "-y",
            "-ss", str(ts),
            "-i", FINAL_MP4,
            "-vframes", "1",
            "-q:v", "2",
            clean_jpg
        ]
        subprocess.run(cmd_thumb, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        draw_safe_zone_qc(clean_jpg, qc_jpg)
        print(f"Generated QC preview: {qc_jpg}")

if __name__ == "__main__":
    main()
