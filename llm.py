import streamlit as st
import google.generativeai as genai

# Configure Gemini using Streamlit Secrets
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

MODEL_NAME = "gemini-1.5-flash"

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text.strip()
