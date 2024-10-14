import streamlit as st
from handle_processes.screens import *

# Initialize session state for screen if not already set
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'  # Default screen
    switch_screen(st.session_state.screen)