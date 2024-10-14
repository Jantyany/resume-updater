import streamlit as st
from handle_processes.screens import *
from load_screen.intro_screen import load_intro
from handle_processes.run_resume_process import process_resume_button
from models.chatgpt_models import get_chgpt_api_key
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# st.session_state.buttondict = load_intro()
uploaded_document,input_url,selected_option,process_button = load_intro()

if process_button:
    if uploaded_document is None:
        st.markdown(f'please upload a docx resume document')
    elif input_url is None:
        st.markdown(f'please a target job url')
    else:
        process_resume_button(uploaded_document,input_url,selected_option)
  
