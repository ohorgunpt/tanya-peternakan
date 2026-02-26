import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Tanya-Peternakan AI", page_icon="🐮")
st.title("🐮 Tanya-Peternakan AI")

# Koneksi ke API Google
try:
    # Mengambil kunci dari Secrets Streamlit yang sudah Bapak isi tadi
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Nama model ini HARUS persis seperti ini agar tidak 404
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Gagal menyambungkan kunci API. Pastikan 'Advanced settings' sudah benar.")

# Kotak Input Chat
prompt = st.chat_input("Tanyakan sesuatu tentang ternak Bapak...")

if prompt:
    # Tampilkan chat User
    with st.chat_message("user"):
        st.markdown(prompt)

    # Proses jawaban AI
    with st.chat_message("assistant"):
        try:
            # Mengirim pertanyaan ke AI
            response = model.generate_content(f"Kamu adalah ahli peternakan Indonesia. Jawablah: {prompt}")
            st.markdown(response.text)
        except Exception as e:
            # Jika masih error, tampilkan pesan bantuan
            st.error(f"Maaf Pak, ada gangguan teknis: {str(e)}")
            st.info("Saran: Coba refresh halaman ini atau cek sisa kuota API Gemini Bapak.")
