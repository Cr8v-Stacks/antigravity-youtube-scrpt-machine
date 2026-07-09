import os
import json
import time
import shutil

queue_path = r"c:\Users\HP\Documents\Antigravity Youtube Scrpt Machine\production-packs\wedding_rings\new_prompts_queue.json"
images_dir = r"c:\Users\HP\Documents\Antigravity Youtube Scrpt Machine\production-packs\wedding_rings\images"
brain_dir = r"C:\Users\HP\.gemini\antigravity\brain\0946cc7b-c00c-4d20-89f4-21597ce4e236"

# Create images dir if not exists
os.makedirs(images_dir, exist_ok=True)

with open(queue_path, "r", encoding="utf-8") as f:
    queue = json.load(f)

print("Copier daemon started...", flush=True)

while True:
    try:
        # Get all png files in brain_dir
        brain_files = [f for f in os.listdir(brain_dir) if f.lower().endswith(".png")]
        
        # Check against queue
        for shot in queue:
            filename = shot["filename"]
            target_path = os.path.join(images_dir, filename + ".png")
            
            # If target already exists, skip
            if os.path.exists(target_path):
                continue
                
            # Look for matches in brain_dir
            # Format: filename_*.png
            for bf in brain_files:
                if bf.startswith(filename) and bf.lower().endswith(".png"):
                    source_path = os.path.join(brain_dir, bf)
                    print(f"Found match: {bf} -> copying to {filename}.png", flush=True)
                    shutil.copy2(source_path, target_path)
                    # Clean up source file
                    try:
                        os.remove(source_path)
                    except Exception as e:
                        print(f"Could not remove source file {bf}: {e}", flush=True)
                    break
    except Exception as e:
        print(f"Error in daemon loop: {e}", flush=True)
        
    time.sleep(1)
