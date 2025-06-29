import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agent import Agent
from langchain_openai import ChatOpenAI
from tools import read_blood_report  # Import the @tool-decorated function

# Set up OpenAI LLM
llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

# Doctor Agent
doctor = Agent(
    role="Senior Experienced Doctor",
    goal="Analyze blood test reports and give medical advice",
    verbose=True,
    memory=True,
    backstory="You are a medical doctor who diagnoses health conditions using blood reports.",
    tools=[read_blood_report],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)

# Verifier Agent
verifier = Agent(
    role="Blood Report Verifier",
    goal="Verify whether the uploaded file is a blood report",
    verbose=True,
    memory=True,
    backstory="You verify and validate health documents.",
    tools=[read_blood_report],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)

# Nutritionist Agent
nutritionist = Agent(
    role="Certified Nutritionist",
    goal="Provide nutrition advice based on the blood test report",
    verbose=True,
    memory=True,
    backstory="You're an expert in diet, nutrition, and supplement guidance.",
    tools=[read_blood_report],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)

# Exercise Specialist Agent
exercise_specialist = Agent(
    role="Fitness Coach",
    goal="Recommend personalized workout plans based on blood reports",
    verbose=True,
    memory=True,
    backstory="You're a certified personal trainer and fitness expert.",
    tools=[read_blood_report],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)
