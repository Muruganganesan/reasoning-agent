import streamlit as st
from agent import solve

st.set_page_config(page_title="Reasoning Agent", layout="centered")

st.title("🧠 Multi-Step Reasoning Agent")
st.write("Powered by **Gemini API** with self-checking")

question = st.text_area(
    "Enter a word problem:",
    placeholder="Example: If a train leaves at 14:30 and arrives at 18:05, how long is the journey?"
)

if st.button("Solve"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            result = solve(question)

        st.subheader("✅ Answer")
        st.success(result["answer"])

        st.subheader("🧩 Explanation")
        st.write(result["reasoning_visible_to_user"])

        with st.expander("🔍 Debug Info (Metadata)"):
            st.json(result["metadata"])
