import streamlit as st
from app_installer.installer import install_chrome
from file_readers_writers.docx_reader import extract_docx_text
from web_readers.html_readers import get_html_job
from load_screen.intro_screen import load_intro
from models.get_model_responses import run_model

uploaded_document,input_url,selected_option = load_intro()
 
# # Display the selected option
# st.write(f"You selected: {selected_option}")

# Button to trigger processing
if st.button("Process"):
    #Check file is Docx

    # Call the Python function that handles the uploaded document and URL
    process_inputs(uploaded_document, input_url)
   
    if selected_option == "ChatGPT 4o":
        run_model(job_description_path,current_cv,target_job,'ch4')
    elif selected_option == "Claude Instant v1":
        run_model(job_description_path,current_cv,target_job,'cl1')
    elif selected_option=="Claude v3 Haiku":
        run_model(job_description_path,current_cv,target_job,'cl3')

# print('target job:',target_job)
# for m in models:
#   if m=='cl1':
#     run_model(job_description_path,current_cv,target_job,m)
#   elif m=='cl3':
#     run_model(job_description_path,current_cv,target_job,m)
#   elif m=='ch4':
#     run_model(job_description_path,current_cv,target_job,m)