import streamlit as st
from app_installer.installer import install_chrome
from file_readers_writers.docx_reader import extract_docx_text
from web_readers.html_readers import get_html_job
from load_screen.alt_intro_screen import load_alt_intro
from load_screen.download_screen import load_downloads
from models.get_model_responses import run_model

def process_resume_button():
    
    #Check file is Docx

    # Call the Python function that handles the uploaded document and URL
    # process_inputs(uploaded_document, input_url)

    # if selected_option == "ChatGPT 4o":
    #     resume_data, resume_name = run_model(job_description_path,current_cv,target_job,'ch4')
    # elif selected_option == "Claude Instant v1":
    #     resume_data, resume_name = run_model(job_description_path,current_cv,target_job,'cl1')
    # elif selected_option=="Claude v3 Haiku":
    #     resume_data, resume_name = run_model(job_description_path,current_cv,target_job,'cl3')

    # uploaded_document,input_url,selected_option,process_button,resume_download_button = load_downloads(resume_data, resume_name)    

    # if resume_download_button is not None:
    #     run()