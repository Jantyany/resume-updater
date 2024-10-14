import streamlit as st
from app_installer.installer import install_chrome
from file_readers_writers.docx_reader import extract_docx_text
from web_readers.html_readers import get_html_job

# install_chrome()

chrometext = get_html_job("https://www.google.com")
st.success(f"Successfully lodaed page title: {chrometext[:100]}")

# st.title("🎈 My new Streamlit app")
st.title("Resume Document and job URL Processor")

st.write(
    "Upload your resume document below"
)

# File uploader widget
uploaded_document = st.file_uploader("Upload a resume document in docx format", \
                                     type=["docx"])

# Text input for URL
input_url = st.text_input("Enter a URL")

# current_cv = extract_docx_text(cvpath)

# target_job=get_html_job(job_description_path)

# print('target job:',target_job)
# for m in models:
#   if m=='cl1':
#     run_model(job_description_path,current_cv,target_job,m)
#   elif m=='cl3':
#     run_model(job_description_path,current_cv,target_job,m)
#   elif m=='ch4':
#     run_model(job_description_path,current_cv,target_job,m)