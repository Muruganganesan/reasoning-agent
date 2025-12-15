from planner import plan
from executor import execute
from verifier import verify

MAX_RETRIES = 2

def solve(question: str) -> dict:
    retries = 0

    while retries <= MAX_RETRIES:
        plan_text = plan(question)
        solution_text = execute(question, plan_text)
        check = verify(question, solution_text)

        if check["passed"]:
            return {
                "answer": extract_answer(solution_text),
                "status": "success",
                "reasoning_visible_to_user": short_reasoning(),
                "metadata": {
                    "plan": plan_text,
                    "checks": [
                        {
                            "check_name": "self_verification",
                            "passed": True,
                            "details": check["reason"]
                        }
                    ],
                    "retries": retries
                }
            }

        retries += 1

    return {
        "answer": "",
        "status": "failed",
        "reasoning_visible_to_user": "The agent could not verify a correct solution.",
        "metadata": {
            "plan": plan_text,
            "checks": [
                {
                    "check_name": "self_verification",
                    "passed": False,
                    "details": check["reason"]
                }
            ],
            "retries": retries
        }
    }

def extract_answer(solution: str) -> str:
    return solution.strip().split("\n")[-1]

def short_reasoning() -> str:
    return "The problem was solved step by step and verified for correctness."
