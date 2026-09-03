file_path = r"C:\Users\User\.gemini\antigravity\brain\690d8115-48e0-47e3-afbe-6cb2a924764c\.system_generated\steps\858\content.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
print("Total markdown links found:", len(matches))
for text, url in matches:
    if "index.py" in url or "models_compiled" in url or "index.py" in text or "models_compiled" in text:
        print(f"Match: Text={text}, URL={url}")
