import os
import re
import requests
import csv
import json
import time

API_KEY = os.environ.get("OLLAMA_API_KEY")
BASE_URL = "https://ollama.com/api"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Step 1: Get all models
print("Fetching model list...")
resp = requests.get(f"{BASE_URL}/tags", headers=HEADERS)
resp.raise_for_status()
models = [m["model"] for m in resp.json()["models"]]
print(f"Found {len(models)} models.\n")

# Step 2 & 3: Chat each model and collect results
results = []

for i, model in enumerate(models, 1):
    print(f"[{i}/{len(models)}] Testing: {model} ...", end=" ", flush=True)

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "hello"}],
        "stream": False
    }

    try:
        r = requests.post(f"{BASE_URL}/chat", headers=HEADERS, json=payload)
        data = r.json()
        is_free = (
            r.status_code == 200
            and "message" in data
            and "content" in data.get("message", {})
            and bool(data["message"]["content"].strip())
        )
        print("✓ Free" if is_free else f"✗ Not free (HTTP {r.status_code}, content={data.get('message', {}).get('content', 'N/A')!r})")
    except Exception as e:
        is_free = False
        print(f"✗ Error: {e}")

    results.append({"model": model, "isFree": is_free})
    time.sleep(2)

# Step 4: Write CSV
with open("models.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "isFree"])
    writer.writeheader()
    for r in results:
        writer.writerow({"model": r["model"], "isFree": str(r["isFree"]).lower()})

# Step 5: Write JSON
with open("models.json", "w") as f:
    json.dump(results, f, indent=2)


# Step 6: Update README.md tables
def update_readme_tables(results):
    free_models = sorted([r["model"] for r in results if r["isFree"]])
    paid_models = sorted([r["model"] for r in results if not r["isFree"]])

    free_table = "| Model |\n|-------|\n" + "\n".join(f"| {m} |" for m in free_models)
    paid_table = "| Model |\n|-------|\n" + "\n".join(f"| {m} |" for m in paid_models)

    with open("README.md", "r") as f:
        content = f.read()

    content = re.sub(
        r"<!-- FREE_MODELS_TABLE -->\n.*?<!-- FREE_MODELS_TABLE_END -->",
        f"<!-- FREE_MODELS_TABLE -->\n{free_table}\n<!-- FREE_MODELS_TABLE_END -->",
        content,
        flags=re.DOTALL
    )

    content = re.sub(
        r"<!-- PAID_MODELS_TABLE -->\n.*?<!-- PAID_MODELS_TABLE_END -->",
        f"<!-- PAID_MODELS_TABLE -->\n{paid_table}\n<!-- PAID_MODELS_TABLE_END -->",
        content,
        flags=re.DOTALL
    )

    with open("README.md", "w") as f:
        f.write(content)


update_readme_tables(results)

print("\nDone! Results saved to models.csv and models.json")
