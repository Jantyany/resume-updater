import streamlit as st
from app_installer.installer import install_chrome
from file_readers.docx_reader import extract_docx_text
from web_readers.html_requests import get_html_text_requests
from web_readers.html_chrome import get_html_text_selenium

# install_chrome()

chrometext = get_html_text_selenium("https://www.google.com")
st.success(f"Successfully lodaed page title: {chrometext[:100]}")

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
