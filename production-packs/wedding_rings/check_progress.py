import os
import json

queue_path = r"c:\Users\HP\Documents\Antigravity Youtube Scrpt Machine\production-packs\wedding_rings\new_prompts_queue.json"
images_dir = r"c:\Users\HP\Documents\Antigravity Youtube Scrpt Machine\production-packs\wedding_rings\images"

with open(queue_path, "r", encoding="utf-8") as f:
    queue = json.load(f)

existing_images = os.listdir(images_dir)
pending = [shot for shot in queue if (shot["filename"] + ".png") not in existing_images]

print(f"Total: {len(queue)}, Done: {len(queue) - len(pending)}, Pending: {len(pending)}")
for p in pending[:3]:
    print(f"--- Index {p['index']} ---")
    print(f"Filename: {p['filename']}")
    print(f"Prompt: {p['prompt']}")
