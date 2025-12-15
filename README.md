# Multi-Step Reasoning Agent (Gemini + Streamlit)

## Overview
A reasoning agent that solves word problems using:
- Planning
- Execution
- Self-verification

Only the final answer and a short explanation are shown to the user.

## Tech Stack
- Python
- Gemini API
- Streamlit

## Run Locally
```bash
pip install -r requirements.txt
cp .env.example .env
# add Gemini API key
streamlit run app.py
