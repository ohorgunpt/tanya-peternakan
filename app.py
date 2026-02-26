import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Tanya-Peternakan AI", page_icon="🐮")
st.title("🐮 Tanya-Peternakan AI")

# Koneksi ke API Google
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # KUNCI PERBAIKAN: Memanggil model dengan jalur lengkap
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
except Exception as e:
    st.error(f"Gagal konfigurasi: {e}")

# Kotak Input Chat
prompt = st.chat_input("Tanyakan sesuatu tentang ternak Bapak...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Menggunakan generasi teks standar
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Waduh Pak, masih ada kendala: {str(e)}")
            st.info("Catatan: Jika error 404 berlanjut, kemungkinan API Key Bapak perlu dicek ulang di Google AI Studio.")
