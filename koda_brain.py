import os
import json

DATA_FILE = "memory.json"

os.makedirs("memory", exist_ok=True)

if os.path.exists(DATA_FILE):
    dataset = json.load(open(DATA_FILE))
else:
    dataset = []

dataset.append({"status": "running", "count": len(dataset)})

with open(DATA_FILE, "w") as f:
    json.dump(dataset, f)

print("OK")
