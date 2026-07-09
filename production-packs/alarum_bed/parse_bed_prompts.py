import re
import json
import os

md_path = 'alarum_bed_shorts_pack.md'
output_json = 'prompts_queue.json'

def sanitize_for_filename(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s_]', '', text)
    text = text.strip()
    text = re.sub(r'\s+', '_', text)
    return text

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the shot-by-shot section
sections = content.split('\n#')
shot_section = None
for sec in sections:
    lines = sec.strip().split('\n')
    if lines and lines[0].strip().lower().startswith('# shot-by-shot image prompts') or lines[0].strip().lower().startswith('shot-by-shot image prompts'):
        shot_section = sec
        break

if not shot_section:
    # Try alternate naming
    for sec in sections:
        lines = sec.strip().split('\n')
        if lines and lines[0].strip().lower().startswith('# shot by shot image prompts') or lines[0].strip().lower().startswith('shot by shot image prompts'):
            shot_section = sec
            break

if not shot_section:
    print("Error: Shot section not found!")
    exit(1)

shot_blocks = re.split(r'^\s*(\d+)[\).]\s*(\d{1,2}:\d{2})\s*(?:-|\u2013)\s*(\d{1,2}:\d{2})\s*$', shot_section, flags=re.M)

queue = []
for i in range(1, len(shot_blocks), 4):
    index = shot_blocks[i]
    start = shot_blocks[i+1]
    end = shot_blocks[i+2]
    block_content = shot_blocks[i+3]
    
    # Extract narration and prompt
    narration_match = re.search(r'narration:\s*"(.+?)"', block_content, re.I)
    prompt_match = re.search(r'prompt a:\s*(.+?)$', block_content, re.M | re.I)
    
    if narration_match and prompt_match:
        narration = narration_match.group(1).strip()
        prompt = prompt_match.group(1).strip()
        filename = sanitize_for_filename(narration)
        queue.append({
            "index": int(index),
            "start": start,
            "end": end,
            "narration": narration,
            "prompt": prompt,
            "filename": filename
        })

with open(output_json, 'w', encoding='utf-8') as out_f:
    json.dump(queue, out_f, indent=2)

print(f"Extracted {len(queue)} shots to {output_json}")
