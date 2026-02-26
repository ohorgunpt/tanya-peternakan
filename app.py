import streamlit as st
import requests

# ==============================
# KONFIGURASI
# ==============================

API_KEY = st.secrets["OPENROUTER_API_KEY"]
MODEL = "meta-llama/llama-3.1-8b-instruct"

# ==============================
# FUNGSI AI
# ==============================

def tanya_ternak(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://streamlit.io",
        "X-Title": "Tanya-Peternakan-AI"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "Kamu adalah asisten ahli peternakan Indonesia yang ramah, profesional, dan praktis. Jawab dengan jelas dan mudah dipahami peternak."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error API: {response.text}"

    result = response.json()
    return result["choices"][0]["message"]["content"]


# ==============================
# UI STREAMLIT
# ==============================

st.set_page_config(page_title="🐮 Tanya Peternakan AI-by TPN", page_icon="🐮")

st.title("🐮 Tanya-Peternakan AI-by TPN")
st.write("Konsultasi masalah sapi, kambing, domba, ayam, dan ternak lainnya.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Tanyakan sesuatu tentang ternak...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        jawaban = tanya_ternak(user_input)
        st.chat_message("assistant").write(jawaban)
        st.session_state.messages.append({"role": "assistant", "content": jawaban})

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
