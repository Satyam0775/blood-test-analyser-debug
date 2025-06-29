from crewai import Task
from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import read_blood_report

help_patients = Task(
    description="Analyze the blood report and respond to: {query}",
    expected_output="Provide a medical summary with any concerns or conditions.",
    agent=doctor,
    tools=[read_blood_report],
    async_execution=False
)

nutrition_analysis = Task(
    description="Give nutritional advice based on {query} and blood test data.",
    expected_output="Provide dietary changes, supplement suggestions, and food list.",
    agent=nutritionist,
    tools=[read_blood_report],
    async_execution=False
)

exercise_planning = Task(
    description="Design a personalized exercise plan based on the blood report and {query}.",
    expected_output="Suggest workout routines, intensity, and goals.",
    agent=exercise_specialist,
    tools=[read_blood_report],
    async_execution=False
)

verification = Task(
    description="Confirm that the uploaded file is a valid blood test report.",
    expected_output="Return confirmation with supporting data from the report.",
    agent=verifier,
    tools=[read_blood_report],
    async_execution=False
)
