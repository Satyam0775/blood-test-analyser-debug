import os
import uuid
import certifi
from fastapi import FastAPI, File, UploadFile, Form, HTTPException

from crewai import Crew, Process
from agents import doctor, verifier, nutritionist, exercise_specialist
from task import help_patients, verification, nutrition_analysis, exercise_planning

# Set environment certs
os.environ['SSL_CERT_FILE'] = certifi.where()

app = FastAPI(title="Blood Test Report Analyser")

def run_crew(query: str, file_path: str = "data/sample.pdf"):
    crew = Crew(
        agents=[verifier, doctor, nutritionist, exercise_specialist],
        tasks=[verification, help_patients, nutrition_analysis, exercise_planning],
        process=Process.sequential,
        verbose=True
    )
    return crew.kickoff(inputs={"query": query, "path": file_path})

@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)
        os.makedirs("outputs", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        result = run_crew(query=query, file_path=file_path)

        output_file = f"outputs/analysis_{file_id}.txt"
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(str(result))

        return {
            "status": "success",
            "query": query,
            "analysis": str(result),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

    finally:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass
