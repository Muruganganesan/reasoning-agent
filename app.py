import streamlit as st
import json
from agent import solve

st.set_page_config(page_title="AI Reasoning Agent", page_icon="🤖")

st.title("🤖 Multi-Step Reasoning Agent")
st.write("Ask any question. The agent will plan → execute → verify → give the final answer.")

question = st.text_area("Enter your question")

if st.button("Solve"):
    if question.strip() == "":
        st.error("Please type a question!")
    else:
        with st.spinner("Thinking..."):
            result = solve(question)

        st.subheader("📌 Final Answer")
        st.success(result["answer"])

        st.subheader("🧠 Explanation (Short)")
        st.info(result["reasoning_visible_to_user"])

        with st.expander("🔍 Metadata (Debug Info)"):
            st.json(result["metadata"])
