import os
import re
import sys
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()

WORK_DIR = os.path.abspath("shorts/build_vattenfall_v3")
CUTS_DIR = os.path.join(WORK_DIR, "cuts")
OUTPUT_DIR = os.path.abspath("shorts")
PREVIEW_DIR = os.path.join(OUTPUT_DIR, "previews", "short_vattenfall_v3")

os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(CUTS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)

AUDIO_WAV = os.path.abspath("temp_media_vattenfall/voiceover_andrew_57s.wav")
WORDS_JSON = os.path.abspath("temp_media_vattenfall/andrew_words.json")
FINAL_MP4 = os.path.join(OUTPUT_DIR, "short_vattenfall_wind_turbine_house_v3.mp4")

# Total duration: exactly 58.20 seconds (Narration ends at 57.34s, audio file is 57.62s, clean 0.86s ringout)
CUTS = [
    # 1. Immediate Hero Hook: Blade-Made Tiny House Pod (User directive: introduce product immediately!)
    {"name": "01_hook_hero_pod", "start": 0.00, "end": 1.80, "src": "temp_user_vattenfall/user_asset_10_blade-made-tiny-hous.jpg", "zoom": "in"},
    # 2. Blade Graveyard / Storage Yard (Authentic, no Getty watermark!)
    {"name": "02_blade_storage_yard", "start": 1.80, "end": 3.80, "src": "temp_media_vattenfall/blade_storage_yard.jpg", "zoom": "out"},
    # 3. Swedish Innovation: Offshore Vattenfall Turbine
    {"name": "03_vattenfall_offshore_turbine", "start": 3.80, "end": 6.80, "src": "temp_user_vattenfall/user_asset_05_SaveClip.App_6566898.jpg", "zoom": "in"},
    # 4. Tiny House Pod Resident with Coffee
    {"name": "04_resident_coffee_door", "start": 6.80, "end": 10.00, "src": "temp_user_vattenfall/user_asset_06_SaveClip.App_6573055.jpg", "zoom": "in"},
    # 5. Heavy Crane Lifting 10m Vestas Nacelle
    {"name": "05_crane_lifting_nacelle", "start": 10.00, "end": 13.00, "src": "temp_user_vattenfall/user_asset_01_SaveClip.App_6517822.jpg", "zoom": "out"},
    # 6. Architect Standing in Hollow Cavernous Nacelle Shell
    {"name": "06_architect_empty_hull", "start": 13.00, "end": 16.00, "src": "temp_user_vattenfall/user_asset_02_SaveClip.App_6560184.jpg", "zoom": "in"},
    # 7. Completed House Lifted on Dutch Design Week Site
    {"name": "07_crane_truck_house_ddw", "start": 16.00, "end": 19.20, "src": "temp_user_vattenfall/user_asset_15_vattenfall-discarded.jpg", "zoom": "in"},
    # 8. Raw Rotor Hub Opening & Man
    {"name": "08_raw_rotor_opening", "start": 19.20, "end": 22.50, "src": "temp_user_vattenfall/user_asset_03_SaveClip.App_6562734.jpg", "zoom": "in"},
    # 9. Aerodynamic Curved Exterior Shell & EV Charger
    {"name": "09_aerodynamic_shell_ev", "start": 22.50, "end": 26.00, "src": "temp_user_vattenfall/user_asset_14_tiny-house-06.jpg", "zoom": "out"},
    # 10. Scandinavian Interior: Kitchen, Dining, Heat Pump AC Unit Overhead
    {"name": "10_interior_kitchen_heatpump", "start": 26.00, "end": 28.50, "src": "temp_user_vattenfall/user_asset_12_jlousberg_20241017_1.jpg", "zoom": "in"},
    # 11. Drone Shot: Rooftop Solar Panels
    {"name": "11_drone_solar_roof", "start": 28.50, "end": 31.00, "src": "temp_user_vattenfall/user_asset_04_SaveClip.App_6562794.jpg", "zoom": "in"},
    # 12. Lund Car Park Facade: 57 Wind Blades Mounted
    {"name": "12_lund_carpark_facade_wide", "start": 31.00, "end": 34.20, "src": "temp_media_vattenfall/carpark_facade_or_house.jpg", "zoom": "in"},
    # 13. Lund Blade Facade Architecture Detail
    {"name": "13_lund_blade_louvers_detail", "start": 34.20, "end": 37.50, "src": "temp_media_vattenfall/carpark_facade_or_house.jpg", "zoom": "out"},
    # 14. Norway EVI Ski Maker Workshop: Reclaiming Carbon Fiber with Sparks
    {"name": "14_ski_workshop_sparks", "start": 37.50, "end": 41.50, "src": "temp_media_vattenfall/skis_or_materials.jpg", "zoom": "in"},
    # 15. Ski Grinding & Handcrafted Alpine Skis
    {"name": "15_alpine_ski_crafting", "start": 41.50, "end": 45.80, "src": "temp_media_vattenfall/skis_or_materials.jpg", "zoom": "out"},
    # 16. Circular High-Angle Aerial View
    {"name": "16_circular_panoramic_aerial", "start": 45.80, "end": 50.50, "src": "temp_user_vattenfall/user_asset_11_blade-made-tiny-hous.jpg", "zoom": "in"},
    # 17. Blade Storage & Steel Recycling Overview
    {"name": "17_blade_steel_recycling", "start": 50.50, "end": 54.00, "src": "temp_media_vattenfall/blade_storage_yard.jpg", "zoom": "in"},
    # 18. Closing Hero Shot: Resident Smiling at Door of Finished Nacelle House
    {"name": "18_closing_hero_pod", "start": 54.00, "end": 58.20, "src": "temp_user_vattenfall/user_asset_09_Vattenfall-Tiny-Hous.jpg", "zoom": "in"}
]

def format_ass_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def generate_subtitles():
    with open(WORDS_JSON, "r", encoding="utf-8") as f:
        words = json.load(f)
        
    ass_path = os.path.join(WORK_DIR, "subtitles_v3.ass")
    
    # ASS Header with Center Alignment (Alignment=5 is Center-Middle)
    header = (
        "[Script Info]\n"
        "Title: Vattenfall Wind Turbine Short V3\n"
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
    out_mp4 = os.path.join(CUTS_DIR, f"cut_{idx:02d}_{cut['name']}.mp4")
    fps = 30
    frames = int(round(dur * fps))
    
    # Motion expressions for zoom
    if cut.get("zoom") == "in":
        z_expr = "min(zoom+0.0006,1.12)"
    else:
        z_expr = "max(1.12-0.0006*on,1.0)"
        
    # Hybrid 70% Layout:
    # 1. Background: Darkened blurred full 1080x1920 canvas
    # 2. Foreground: Scaled to height 1350, cropped to 1080x1350 with smooth Ken Burns motion
    # 3. Overlaid precisely at Y=285 ((1920-1350)/2)
    filter_graph = (
        f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.12[bg];"
        f"[0:v]scale=-1:1350:force_original_aspect_ratio=increase,crop=1080:1350:(iw-1080)/2:(ih-1350)/2,"
        f"zoompan=z='{z_expr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1350:fps={fps}[fg];"
        f"[bg][fg]overlay=0:285[v]"
    )
    
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1", "-t", str(dur),
        "-i", cut["src"],
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
    # Hybrid 70% Foreground Visual Bounds (Y: 285 to 1635)
    d.rectangle([0, 285, 1080, 1635], outline=(0, 255, 0, 120), width=2)
    combined = Image.alpha_composite(im, overlay)
    combined.convert("RGB").save(dst_jpg, quality=92)

def main():
    print("==========================================================")
    print("PRODUCING V3: 58.20S VATTENFALL SHORT (ANDREW VOICE, HYBRID 70% ZOOM, FULL AUDIO)")
    print("==========================================================")
    ass_file = generate_subtitles()

    # 1. Build individual video cut segments
    cut_clips = []
    concat_txt = os.path.join(WORK_DIR, "concat_cuts.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for idx, c in enumerate(CUTS):
            c_path = build_cut(c, idx)
            cut_clips.append(c_path)
            f.write(f"file '{c_path.replace(chr(92), '/')}'\n")

    # 2. Concat all cuts together
    raw_video = os.path.join(WORK_DIR, "raw_cuts_concat.mp4")
    cmd_concat = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy",
        raw_video
    ]
    subprocess.run(cmd_concat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print("Concatenated all 18 cuts:", raw_video)

    # 3. Burn subtitles and mux audio (audio padded to 58.20s, exactly matches video duration)
    escaped_ass = ass_file.replace("\\", "/").replace(":", "\\:")
    cmd_burn = [
        FFMPEG_EXE, "-y",
        "-i", raw_video,
        "-i", AUDIO_WAV,
        "-filter_complex", f"[0:v]subtitles='{escaped_ass}'[v];[1:a]apad=whole_dur=58.20[a]",
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-t", "58.20",
        FINAL_MP4
    ]
    subprocess.run(cmd_burn, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    print("MASTER SHORT V3 RENDERED:", FINAL_MP4)

    # 4. QC Previews at key moments
    checkpoints = [
        ("preview_01_hook_hero_pod", 1.0),
        ("preview_02_blade_storage_yard", 2.8),
        ("preview_03_vattenfall_offshore_turbine", 5.0),
        ("preview_04_resident_coffee_door", 8.0),
        ("preview_05_crane_lifting_nacelle", 11.5),
        ("preview_06_architect_empty_hull", 14.5),
        ("preview_07_crane_truck_house_ddw", 17.5),
        ("preview_08_aerodynamic_shell_ev", 24.0),
        ("preview_09_interior_kitchen_heatpump", 27.0),
        ("preview_10_drone_solar_roof", 29.8),
        ("preview_11_lund_carpark_facade", 32.5),
        ("preview_12_ski_workshop_sparks", 39.5),
        ("preview_13_circular_panoramic_aerial", 48.0),
        ("preview_14_closing_hero_pod", 56.0)
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

    print("==========================================================")
    print("V3 PRODUCTION COMPLETE! ALL ASSETS AND PREVIEWS READY.")
    print("==========================================================")

if __name__ == "__main__":
    main()
