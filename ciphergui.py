import streamlit as st
from streamlit_lottie import st_lottie

# Function for Caesar Cipher
def caesar_cipher(text, shift, alphabet):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx + shift) % len(alphabet)
            encrypted_text += alphabet[new_idx]
        else:
            encrypted_text += char
    return encrypted_text

st.set_page_config(page_title="Caesar Cipher by Fajar", page_icon=":closed_lock_with_key:")

# Set custom background and text color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #E0F7FA;
        color: #004D40;
    }
    .stButton>button {
        background-color: #004D40;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: #eb0505;'>Welcome to Fajar Caesar Cipher App!</h1>", unsafe_allow_html=True)

# Alphabet type selection
st.subheader("Choose Alphabet Type")
alphabet_type = st.selectbox("Alphabet type", ["English alphabet (A-Z)", "English alphabet and digits (A-Z, 0-9)"])

# Define alphabet based on choice
if alphabet_type == "English alphabet (A-Z)":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
else:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Encoder Section
st.subheader("Caesar Cipher Encoder")
plain_text = st.text_input("Enter text to encrypt")
shift_encrypt = st.number_input("Shift value for encryption", min_value=0, step=1)
if st.button("Encrypt"):
    encrypted_text = caesar_cipher(plain_text, shift_encrypt, alphabet)
    st.success(f"Encrypted message: {encrypted_text}")

# Decoder Section
st.subheader("Caesar Cipher Decoder")
cipher_text = st.text_input("Enter text to decrypt")
shift_decrypt = st.number_input("Shift value for decryption", min_value=0, step=1)
if st.button("Decrypt"):
    decrypted_text = caesar_cipher(cipher_text, -shift_decrypt, alphabet)
    st.success(f"Decrypted message: {decrypted_text}")

# Watermark
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; right: 10px; color: #004D40;'>Created by Fina Dwi Aulia</div>
    """,
    unsafe_allow_html=True
)