import os
import google.generativeai as genai
from app.prompts import REASONING_PROMPT

# setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def solve(question: str) -> str:
    prompt = REASONING_PROMPT.format(question=question)
    response = model.generate_content(prompt)
    return response.text.strip()
