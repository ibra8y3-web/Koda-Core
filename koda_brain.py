import os
import ast
import json
import requests
import shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = "memory"
DATA_FILE = os.path.join(DATA_DIR, "dataset.json")

os.makedirs(DATA_DIR, exist_ok=True)

# تحميل البيانات

if os.path.exists(DATA_FILE):
dataset = json.load(open(DATA_FILE))
else:
dataset = []

# =========================

# AST فهم الكود الحقيقي

# =========================

def extract_ast_features(code):
try:
tree = ast.parse(code)
nodes = []

```
    for node in ast.walk(tree):
        nodes.append(type(node).__name__)

    return " ".join(nodes)
except:
    return ""
```

# =========================

# تنظيف + دمج

# =========================

def process_code(code):
ast_features = extract_ast_features(code)
return ast_features

# =========================

# جلب repos

# =========================

def fetch_repos():
topics = ["python", "algorithms"]
repos = []

```
for t in topics:
    url = f"https://api.github.com/search/repositories?q={t}&sort=stars&per_page=3"
    try:
        data = requests.get(url).json()
        repos.extend(data.get("items", []))
    except:
        pass

return repos
```

# =========================

# التعلم

# =========================

def learn():
global dataset

```
repos = fetch_repos()
os.makedirs("temp", exist_ok=True)

for repo in repos:
    path = f"temp/{repo['name']}"

    try:
        os.system(f"git clone --depth 1 {repo['clone_url']} {path}")

        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith(".py"):
                    try:
                        code = open(os.path.join(root, f), errors="ignore").read()
                        processed = process_code(code)

                        if len(processed) > 20:
                            dataset.append(processed)

                    except:
                        pass

        shutil.rmtree(path, ignore_errors=True)

    except:
        pass

json.dump(dataset, open(DATA_FILE, "w"))
```

# =========================

# بناء موديل

# =========================

def build_model():
if len(dataset) < 3:
return None, None

```
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(dataset)

return vectorizer, X
```

# =========================

# سؤال / رد

# =========================

def query(q):
vectorizer, X = build_model()

```
if vectorizer is None:
    return "لسه بيتعلم..."

q_vec = vectorizer.transform([q])
sim = cosine_similarity(q_vec, X)

idx = sim.argmax()
return dataset[idx][:300]
```

# =========================

if **name** == "**main**":
print("🔥 Learning...")
learn()
print("✅ Done.")

