import streamlit as st
from handle_processes.screens import *
from load_screen.intro_screen import load_intro
from handle_processes.run_resume_process import process_resume_button

# st.session_state.buttondict = load_intro()
uploaded_document,input_url,selected_option,process_button = load_intro()

if process_button:
    st.markdown(f'button pushed')
    process_resume_button(uploaded_document,input_url,selected_option)
# if st.session_state.buttondict.process_button:
#     st.markdown(f'button pushed')

# # Initialize session state for screen if not already set
# if 'screen' not in st.session_state:
#     st.session_state.screen = 'home'  # Default screen
#     switch_screen(st.session_state.screen)