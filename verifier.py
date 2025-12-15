from google.generativeai import generativeai as genai

def verify_answer(model, question, answer):
    prompt = f"""
Question: {question}
Answer: {answer}

Is this correct? YES / NO
"""
    return model.generate_content(prompt).text.strip()
