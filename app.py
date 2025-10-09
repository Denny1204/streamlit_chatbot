import streamlit as st
import google.generativeai as genai

# Ambil API key dari secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Pilih model
model = genai.GenerativeModel("gemini-2.5-flash-image")

# UI Streamlit
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chatbot Gemini AI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input user
user_input = st.chat_input("Ketik pesan kamu...")

if user_input:
    st.session_state.chat_history.append(("🧍 Kamu", user_input))
    response = model.generate_content(user_input)
    reply = response.text
    st.session_state.chat_history.append(("🤖 Gemini", reply))

# Tampilkan percakapan
for role, text in st.session_state.chat_history:
    st.markdown(f"**{role}:** {text}")
