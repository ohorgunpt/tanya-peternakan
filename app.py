import streamlit as st
from google import genai
import os

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def tanya_ternak(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=f"""
        Kamu adalah asisten ahli peternakan Indonesia yang ramah dan profesional.
        Jawab dengan jelas dan praktis.

        Pertanyaan: {prompt}
        """
    )
    return response.text

st.title("🐮 Tanya-Peternakan AI")

user_input = st.chat_input("Tanyakan sesuatu tentang ternak Bapak...")

if user_input:
    st.chat_message("user").write(user_input)
    try:
        jawaban = tanya_ternak(user_input)
        st.chat_message("assistant").write(jawaban)
    except Exception as e:
        st.error(f"Error: {e}")
