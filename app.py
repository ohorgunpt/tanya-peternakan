import streamlit as st
import requests

# Ambil API Key dari Streamlit Secrets
API_KEY = st.secrets["OPENROUTER_API_KEY"]

def tanya_ternak(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {
                "role": "system",
                "content": "Kamu adalah asisten ahli peternakan Indonesia yang ramah dan profesional. Jawab dengan jelas dan praktis."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error API: {response.text}"

    result = response.json()
    return result["choices"][0]["message"]["content"]


# UI Streamlit
st.title("🐮 Tanya-Peternakan AI (Mistral)")

user_input = st.chat_input("Tanyakan sesuatu tentang ternak Bapak...")

if user_input:
    st.chat_message("user").write(user_input)
    try:
        jawaban = tanya_ternak(user_input)
        st.chat_message("assistant").write(jawaban)
    except Exception as e:
        st.error(f"Error: {e}")
