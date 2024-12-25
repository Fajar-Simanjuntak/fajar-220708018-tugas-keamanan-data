import streamlit as st
from Crypto.Cipher import DES
import base64

# Fungsi Padding PKCS5
def pad(text):
    pad_len = 8 - (len(text) % 8)
    padding = chr(pad_len) * pad_len
    return text + padding

# Fungsi Unpadding
def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

# Fungsi Enkripsi
def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Fungsi Dekripsi
def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return unpad(decrypted_text)

# Konfigurasi Streamlit
st.set_page_config(page_title="DES Encryption App", page_icon="🔒", layout="centered")

# Fungsi Reset Input
def reset_inputs():
    # Mengosongkan semua session state terkait input dan output
    st.session_state["plain_text"] = ""
    st.session_state["key_input"] = ""
    st.session_state["encrypted_text"] = ""
    st.session_state["decrypted_text"] = ""

# Header Aplikasi
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>DES Encryption & Decryption</h1>", unsafe_allow_html=True)

# Inisialisasi Session State
for key in ["plain_text", "key_input", "encrypted_text", "decrypted_text"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Input Teks dan Key
plain_text = st.text_area("Plain Text", value=st.session_state["plain_text"], key="plain_text")
key_input = st.text_input("Key (8 characters)", value=st.session_state["key_input"], key="key_input", type="password")

# Validasi Key
if key_input and len(key_input) != 8:
    st.error("Key must be exactly 8 characters!")

# Proses Enkripsi dan Dekripsi
if key_input and len(key_input) == 8:
    key = key_input.encode('utf-8')

    # Enkripsi
    if plain_text:
        encrypted_text = encrypt(plain_text, key)
        st.session_state["encrypted_text"] = encrypted_text
        st.success(f"Encrypted Text: {encrypted_text}")

    # Dekripsi
    if st.session_state["encrypted_text"]:
        decrypted_text = decrypt(st.session_state["encrypted_text"], key)
        st.session_state["decrypted_text"] = decrypted_text
        st.success(f"Decrypted Text: {decrypted_text}")

# Tombol Reset
if st.button("Reset"):
    reset_inputs()  # Menghapus semua data dari session state
    st.experimental_rerun()  # Memuat ulang antarmuka untuk mencerminkan perubahan
