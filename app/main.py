import streamlit as st

st.set_page_config(page_title="AI Interviewer", page_icon="🤖")

st.sidebar.title("Navigasi")
st.sidebar.page_link("app/interview_chatbot.py", label="Wawancara AI")
# nanti bisa tambah halaman lain: login, hasil analisis, dashboard, dll
