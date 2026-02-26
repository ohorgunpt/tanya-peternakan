import streamlit as st
import google.generativeai as genai
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Tanya-Peternakan AI", page_icon="🐮")
st.title("🐮 Tanya-Peternakan AI")

# Ambil API KEY dari Secrets Streamlit
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Input Chat
prompt = st.chat_input("Tanyakan sesuatu tentang ternak Bapak...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            full_prompt = f"Kamu adalah ahli peternakan Indonesia. Jawablah dengan ramah: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Ada kendala: {e}")
