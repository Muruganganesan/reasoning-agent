import json
from llm import call_gemini
from prompts import VERIFIER_PROMPT

def verify(question: str, solution: str) -> dict:
    prompt = f"""
{VERIFIER_PROMPT}

Question:
{question}

Solution:
{solution}
"""
    response = call_gemini(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {"passed": False, "reason": "Invalid verifier response"}
