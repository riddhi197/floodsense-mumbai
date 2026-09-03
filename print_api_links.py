file_path = r"C:\Users\User\.gemini\antigravity\brain\690d8115-48e0-47e3-afbe-6cb2a924764c\.system_generated\steps\858\content.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'href="([^"]+)"', content)
print("Total links found:", len(matches))
for m in matches:
    if "api" in m:
        print("Link with api:", m)
