import streamlit as st
from core.chatbot_engine import get_gemini_response

st.title("🧠 AI Interviewer")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

prompt = st.chat_input("Pertanyaan atau jawaban kamu...")

if prompt:
    st.session_state.chat_history.append(("user", prompt))
    reply = get_gemini_response(prompt, history=st.session_state.chat_history)
    st.session_state.chat_history.append(("assistant", reply))

for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(text)
