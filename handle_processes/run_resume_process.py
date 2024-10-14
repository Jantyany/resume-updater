import streamlit as st
from app_installer.installer import install_chrome
from file_readers_writers.docx_reader import extract_docx_text
from web_readers.html_readers import get_html_job
from load_screen.alt_intro_screen import load_alt_intro
from load_screen.download_screen import load_downloads
from models.get_model_responses import run_model

def process_resume_button(uploaded_document,input_url,selected_option):
    
    extracted_docx_text=extract_docx_text(uploaded_document)

    extracted_html_text=get_html_job(input_url)

    if selected_option == "ChatGPT 4o":
        run_model(input_url,extracted_docx_text,extracted_html_text,'ch4')
    elif selected_option == "Claude Instant v1":
        run_model((input_url,extracted_docx_text,extracted_html_text,'cl1')
    elif selected_option=="Claude v3 Haiku":
        run_model((input_url,extracted_docx_text,extracted_html_text,'cl3')

    # uploaded_document,input_url,selected_option,process_button,resume_download_button = load_downloads(resume_data, resume_name)    

    # if resume_download_button is not None:
    #     run()