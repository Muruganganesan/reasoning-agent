import google.generativeai as genai
import json
from prompts import PLANNER_PROMPT, EXECUTOR_PROMPT, VERIFIER_PROMPT

# ---------------- CONFIG ----------------
API_KEY = "AIzaSyBnLIORSh27u2AAbhbCIIg4koaAzbCcl6c"   # ← இதுல தான் உன் Gemini API Key paste பண்ணணும்

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# ----------------------------------------

def call_llm(prompt):
    """Generic LLM call function."""
    response = model.generate_content(prompt)
    return response.text


# ---------------- PLANNER ----------------
def planner(question):
    prompt = f"""{PLANNER_PROMPT}

Question:
{question}
"""
    return call_llm(prompt)


# ---------------- EXECUTOR ----------------
def executor(question, plan):
    prompt = f"""{EXECUTOR_PROMPT}

Question:
{question}

Plan:
{plan}
"""
    text = call_llm(prompt)

    # try reading as JSON
    try:
        return json.loads(text)
    except:
        return {"intermediate": text, "result": text}


# ---------------- VERIFIER ----------------
def verifier(question, solution):
    prompt = f"""{VERIFIER_PROMPT}

Question:
{question}

Proposed Solution:
{solution}
"""
    text = call_llm(prompt)

    try:
        data = json.loads(text)
        return data["passed"], data["reason"]
    except:
        return False, text


# ---------------- MAIN SOLVE FUNCTION ----------------
def solve(question):
    retries = 0

    plan = planner(question)
    exec_output = executor(question, plan)
    passed, reason = verifier(question, exec_output)

    status = "success" if passed else "failed"

    return {
        "answer": exec_output.get("result", "").strip(),
        "status": status,
        "reasoning_visible_to_user": "Solved using structured multi-step reasoning.",
        "metadata": {
            "plan": plan,
            "checks": [{
                "check_name": "Verifier",
                "passed": passed,
                "details": reason
            }],
            "retries": retries
        }
    }


# ---------------- CLI MODE ----------------
if __name__ == "__main__":
    print("\n🔥 Multi-Step Reasoning Agent (Google Gemini Powered)")
    print("Type 'exit' to quit.\n")

    while True:
        q = input("Ask question: ")
        if q.lower() == "exit":
            break

        result = solve(q)
        print(json.dumps(result, indent=2))
        print()
