import streamlit as st
from load_screen.intro_screen import load_intro
from load_screen.alt_intro_screen import load_alt_intro
# from handle_processes.run_resume_process import process_resume_button
from load_screen.download_screen import load_downloads

# Function to switch between screens
def switch_screen(screen_name):
    st.session_state.screen = screen_name
    st.experimental_rerun()  # Rerun the app to reflect the change

    # Home screen
    if st.session_state.screen == 'home':
        st.session_state.buttondict = load_intro()
        # Button to trigger processing
        if st.session_state.buttondict.process_button:
            # process_resume_button()
            switch_screen('alt_home')

    if st.session_state.screen == 'alt_home':
        st.session_state.buttondict = load_alt_intro()
        if st.session_state.buttondict.process_button:
            # process_resume_button()
            switch_screen('home')


