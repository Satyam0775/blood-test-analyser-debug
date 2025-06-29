import os
import json
import requests

file_path = r"data/sample.pdf"
url = "http://127.0.0.1:8000/analyze"
output_file = "outputs/analysis_result.json"

os.makedirs("outputs", exist_ok=True)

try:
    with open(file_path, "rb") as f:
        files = {"file": ("sample.pdf", f, "application/pdf")}
        data = {"query": "Summarise my Blood Test Report"}

        print(f"📤 Uploading: {file_path}")
        response = requests.post(url, files=files, data=data)

except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
    exit(1)

if response.status_code == 200:
    result = response.json()
    print("✅ Success!\n", json.dumps(result, indent=2))
    with open(output_file, "w") as out_file:
        json.dump(result, out_file, indent=2)
        print(f"💾 Saved output to {output_file}")
else:
    print(f"❌ Server error {response.status_code}")
    print(response.text)
