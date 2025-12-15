from llm import call_gemini
from prompts import PLANNER_PROMPT

def plan(question: str) -> str:
    prompt = f"{PLANNER_PROMPT}\n\nQuestion:\n{question}"
    return call_gemini(prompt)
