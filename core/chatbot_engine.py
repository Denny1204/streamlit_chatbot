import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def get_gemini_response(prompt, history=None):
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    chat = model.start_chat(history=history or [])
    response = chat.send_message(prompt)
    return response.text
