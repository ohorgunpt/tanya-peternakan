import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Tanya-Peternakan AI", page_icon="🐮")
st.title("🐮 Tanya-Peternakan AI")

# Ambil API KEY dari Secrets Streamlit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Gunakan pemanggilan model yang lebih stabil
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Masalah kunci API: {e}")

# Input Chat
prompt = st.chat_input("Tanyakan sesuatu tentang ternak Bapak...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Tambahkan instruksi agar jawaban lebih mantap
            response = model.generate_content(f"Kamu adalah ahli peternakan Indonesia. Jawablah: {prompt}")
            st.markdown(response.text)
        except Exception as e:
            if "404" in str(e):
                st.error("Gagal menyambung ke otak AI. Coba hapus '-latest' di nama model atau gunakan 'gemini-1.5-flash'.")
            else:
                st.error(f"Ada kendala: {e}")
