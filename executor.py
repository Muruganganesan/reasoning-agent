from llm import call_gemini
from prompts import EXECUTOR_PROMPT

def execute(question: str, plan: str) -> str:
    prompt = f"""
{EXECUTOR_PROMPT}

Question:
{question}

Plan:
{plan}
"""
    return call_gemini(prompt)
