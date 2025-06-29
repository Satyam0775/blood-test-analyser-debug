# 🧪 Blood Test Report Analyzer (CrewAI Debug Challenge)

A FastAPI app using CrewAI agents to analyze blood test PDFs and provide medical, nutrition, and fitness advice.

---

## ✅ What Was Fixed

| 🔧 Bug | ✅ Fix |
|-------|-------|
| ❌ Used `Tool` class | ✅ Replaced with `@tool` decorator |
| ❌ Wrong import for `PDFLoader` | ✅ Used `langchain_community.document_loaders` |
| ❌ Class-based tool | ✅ Converted to function `read_blood_report(path)` |
| ❌ LLM missing | ✅ Added `ChatOpenAI(model="gpt-3.5-turbo")` |
| ❌ No error handling | ✅ Added try/except/finally in `main.py` |
| ❌ Output not saved | ✅ Saved results to `outputs/` folder |

---

## 🧰 Project Setup

### 1. Clone the Repo

```bash
git clone https://github.com/Satyam0775/blood-test-analyser-debug.git
cd blood-test-analyser-debug
