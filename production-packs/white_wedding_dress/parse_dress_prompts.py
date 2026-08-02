import os
import re
import json

md_path = 'white_wedding_dress_production_pack.md'
output_path = 'prompts_queue.json'

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Shot By Shot section
sections = content.split('\n# ')
shot_section = None
for sec in sections:
    if sec.strip().lower().startswith('shot by shot image prompts') or sec.strip().lower().startswith('shot-by-shot image prompts'):
        shot_section = sec
        break

if not shot_section:
    print("Error: Shot section not found!")
    exit(1)

lines = shot_section.split('\n')
shots = []
current_shot = None

for line in lines:
    line = line.strip()
    # Match time marker: 1. 0:00 - 0:03
    time_match = re.match(r'^(\d+)[\).]\s*(\d{1,2}:\d{2})\s*(?:-|\u2013)\s*(\d{1,2}:\d{2})$', line)
    if time_match:
        if current_shot:
            shots.append(current_shot)
        current_shot = {
            "index": int(time_match.group(1)),
            "start": time_match.group(2),
            "end": time_match.group(3),
            "narration": "",
            "prompt": ""
        }
    elif current_shot:
        if line.lower().startswith('narration:'):
            current_shot["narration"] = line.replace('Narration:', '', 1).replace('narration:', '', 1).strip().strip('"')
        elif line.lower().startswith('prompt a:'):
            current_shot["prompt"] = line.replace('Prompt A:', '', 1).replace('prompt a:', '', 1).strip()

if current_shot:
    shots.append(current_shot)

# Format filename slug from narration
def slugify(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9\s_]', '', s)
    s = s.strip()
    s = re.sub(r'\s+', '_', s)
    return s[:100]

for shot in shots:
    shot["filename"] = slugify(shot["narration"])

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(shots, f, indent=2)

print(f"Extracted {len(shots)} shots to {output_path}")
