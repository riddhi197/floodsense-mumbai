import re

file_path = r"C:\Users\User\.gemini\antigravity\brain\690d8115-48e0-47e3-afbe-6cb2a924764c\.system_generated\steps\967\content.md"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Look for file link paths
matches = re.findall(r'href="/riddhi197/floodsense-mumbai/(tree|blob)/[^"]+"', html)
all_links = re.findall(r'href="/riddhi197/floodsense-mumbai/([a-zA-Z0-9_/.-]+)"', html)
unique_links = sorted(list(set(all_links)))

print("Links found on GitHub repository page:")
for link in unique_links:
    if "tree/main/" in link or "blob/main/" in link:
        print(" -", link.replace("tree/main/", "").replace("blob/main/", ""))
