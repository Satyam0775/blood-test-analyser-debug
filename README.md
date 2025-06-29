# 🧪 Blood Test Report Analyser (CrewAI Debug Challenge)

A FastAPI-based multi-agent system using [CrewAI](https://docs.crewai.com) to analyze blood test reports using AI agents: doctor, verifier, nutritionist, and exercise specialist.

---

## 🚀 Project Overview

This system accepts a blood test PDF and generates a medical analysis, nutrition advice, and fitness plan using LLMs. The task was to debug a broken CrewAI implementation and deliver a working API.

---

## ✅ Fixes Made (Bug Report & Solutions)

| 🔧 Bug | ✅ Fix |
|-------|--------|
| ❌ Used `Tool` class instead of `@tool` decorator | ✅ Replaced with `@tool` from `crewai_tools` |
| ❌ Old `langchain.document_loaders` import | ✅ Updated to `langchain_community.document_loaders` |
| ❌ Used `.read_data_tool` method from a class | ✅ Converted to `read_blood_report()` function |
| ❌ LLM config unclear | ✅ Used `ChatOpenAI(model="gpt-3.5-turbo")` |
| ❌ Incorrect `tools=[BloodTestReportTool.read_data_tool]` | ✅ Fixed to `tools=[read_blood_report]` |
| ❌ No error handling or cleanup | ✅ Added `try/except/finally` in `main.py` |
| ❌ No result saving | ✅ Results saved in `outputs/analysis_*.txt` |

---

## 📁 Project Structure

blood-test-analyser-debug/
│
├── data/ # Uploaded PDF reports
├── outputs/ # Generated analysis outputs
├── agents.py # Defines all AI agents
├── main.py # FastAPI app
├── tools.py # @tool function for PDF loading
├── task.py # CrewAI task definitions
├── requirements.txt # Python dependencies
├── .env # Contains OPENAI_API_KEY
├── test_upload.py # CLI test to POST PDF
└── README.md # (You're reading this)

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. **Clone the repo** (or copy directory)
2. Setup Python 3.11 environment:

```bash
python -m venv venv
venv\Scripts\activate   # on Windows
pip install -r requirements.txt
Add your OpenAI key in .env file:

ini
Copy
Edit
OPENAI_API_KEY=sk-...
▶️ Run the API
bash
Copy
Edit
uvicorn main:app --reload
Go to http://127.0.0.1:8000/docs to test the /analyze endpoint.

🧪 Test Upload (CLI)
bash
Copy
Edit
python test_upload.py
It will:

Upload a sample PDF from /data

Save analysis JSON in /outputs
