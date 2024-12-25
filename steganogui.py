import streamlit as st
from stegano import lsb
import os
from io import BytesIO

# Fungsi untuk menyembunyikan pesan
def hide_message(img_path, message):
    try:
        secret = lsb.hide(img_path, message)
        # Menyimpan gambar ke dalam buffer BytesIO
        img_buffer = BytesIO()
        secret.save(img_buffer, format="PNG")
        img_buffer.seek(0)  # Reset pointer ke awal file
        return img_buffer
    except Exception as e:
        return f"Gagal menyembunyikan pesan: {e}"

# Fungsi untuk menampilkan pesan tersembunyi
def reveal_message(img_path):
    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            return f"Pesan tersembunyi: {clear_message}"
        else:
            return "Tidak ada pesan tersembunyi dalam gambar ini."
    except Exception as e:
        return f"Gagal menampilkan pesan: {e}"

# Konfigurasi Streamlit
st.set_page_config(page_title="Steganography Tool", page_icon="🛡️", layout="wide")

# CSS untuk Tema Cybersecurity
st.markdown(
    """
    <style>
        /* Background dan font */
        body {
            background-color: #121212;
            color: #00FF41;
            font-family: 'Courier New', Courier, monospace;
        }

        /* Judul utama */
        h1 {
            text-align: center;
            color: #00FF41;
            font-size: 3em;
            text-shadow: 0px 0px 10px #00FF41;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: #1E1E1E !important;
            border-right: 1px solid #00FF41 !important;
        }

        /* Tombol */
        button {
            background-color: #1E1E1E !important;
            color: #00FF41 !important;
            border: 1px solid #00FF41 !important;
            border-radius: 5px;
            font-weight: bold;
        }
        button:hover {
            background-color: #00FF41 !important;
            color: #121212 !important;
        }

        /* Area input */
        textarea, input {
            background-color: #1E1E1E !important;
            color: #00FF41 !important;
            border: 1px solid #00FF41 !important;
            font-family: 'Courier New', Courier, monospace;
        }

        /* Watermark */
        .watermark {
            position: fixed;
            bottom: 10px;
            right: 10px;
            color: #00FF41;
            font-size: 0.8em;
            text-shadow: 0px 0px 5px #00FF41;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul Aplikasi
st.markdown("<h1>Cybersecurity Steganography Tool</h1>", unsafe_allow_html=True)

# Menu Utama
menu = st.sidebar.selectbox("Menu", ["Sembunyikan Pesan", "Tampilkan Pesan"])

if menu == "Sembunyikan Pesan":
    st.subheader("🔐 Sembunyikan Pesan dalam Gambar")
    
    # Input file gambar
    uploaded_file = st.file_uploader("Upload gambar (format: .png, .jpg)", type=["png", "jpg"])
    
    if uploaded_file:
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        message = st.text_area("Masukkan pesan yang akan disembunyikan")
        
        if st.button("Sembunyikan Pesan"):
            if message:
                result = hide_message(temp_path, message)
                if isinstance(result, BytesIO):
                    st.success("✅ Pesan berhasil disembunyikan! Anda dapat mengunduh gambar di bawah ini.")
                    st.download_button(
                        label="⬇️ Unduh Gambar dengan Pesan Tersembunyi",
                        data=result,
                        file_name="hidden_image.png",
                        mime="image/png"
                    )
                else:
                    st.error(result)
                os.remove(temp_path)
            else:
                st.error("⚠️ Pesan tidak boleh kosong.")

elif menu == "Tampilkan Pesan":
    st.subheader("🔓 Tampilkan Pesan Tersembunyi dari Gambar")
    
    # Input file gambar
    uploaded_file = st.file_uploader("Upload gambar dengan pesan tersembunyi (format: .png, .jpg)", type=["png", "jpg"])
    
    if uploaded_file:
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Tampilkan Pesan"):
            result = reveal_message(temp_path)
            if "Pesan tersembunyi:" in result:
                st.success(result)
            else:
                st.error(result)
            os.remove(temp_path)

# Watermark
st.markdown(
    """
    <div class="watermark">Created by Fajar CyberSec Dev</div>
    """,
    unsafe_allow_html=True
)
