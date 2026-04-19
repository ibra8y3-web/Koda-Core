import os
import requests
import json
import shutil
import re
from collections import Counter

TOPICS = [
"machine-learning","deep-learning","algorithms",
"python","javascript","cpp","cybersecurity"
]

MEMORY_DIR = "memory"
PROGRESS_FILE = "progress.json"
VOCAB_FILE = os.path.join(MEMORY_DIR, "vocab.json")

os.makedirs(MEMORY_DIR, exist_ok=True)

# تحميل التقدم

if os.path.exists(PROGRESS_FILE):
done = set(json.load(open(PROGRESS_FILE)))
else:
done = set()

# تحميل المعرفة

if os.path.exists(VOCAB_FILE):
vocab = Counter(json.load(open(VOCAB_FILE)))
else:
vocab = Counter()

def analyze_code(path):
global vocab
for root, _, files in os.walk(path):
for file in files:
if file.endswith((".py",".js",".cpp",".java",".rs",".ts")):
try:
full = os.path.join(root, file)
with open(full, "r", errors="ignore") as f:
text = f.read()

```
                tokens = re.findall(r"[a-zA-Z_]{2,}", text.lower())
                vocab.update(tokens)

            except:
                pass
```

def fetch_repos():
repos = []
for topic in TOPICS:
url = f"https://api.github.com/search/repositories?q={topic}&sort=stars&per_page=10"
try:
data = requests.get(url).json()
repos.extend(data.get("items", []))
except:
pass
return repos

repos = fetch_repos()

os.makedirs("temp", exist_ok=True)

for repo in repos:
name = repo["name"]
clone = repo["clone_url"]

```
if name in done:
    continue

path = f"temp/{name}"

try:
    print(f"Cloning {name}")
    os.system(f"git clone --depth 1 {clone} {path}")

    print(f"Learning from {name}")
    analyze_code(path)

    shutil.rmtree(path, ignore_errors=True)

    done.add(name)

    json.dump(list(done), open(PROGRESS_FILE, "w"))
    json.dump(dict(vocab.most_common(50000)), open(VOCAB_FILE, "w"))

except:
    pass
```

print("Done learning")

