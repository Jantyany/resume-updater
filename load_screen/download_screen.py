import streamlit as st

def load_downloads(resume_file_data, resume_file_name):
    st.title("resume highlighter app")

    # File uploader widget
    uploaded_document = st.file_uploader("Enter your CV or resume in docx format", \
                                        type=["docx"])

    # Text input for URL
    input_url = st.text_input("Enter your target job url")

    # Dropdown menu with three options
    selected_option = st.selectbox(
        "Choose an LLM model:",  # Label for the dropdown
        ["ChatGPT 4o", "Claude Instant v1", "Claude v3 Haiku"]  # List of options
    )

    # st.markdown(':gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift: :gift:')
    st.markdown(' ')
    process_button=st.button("Process resume to fit target job")

    # Create a download button
    resume_download_button = st.download_button(
        label="Download updated resume",  # Text shown on the download button
        data=resume_file_data,  # File content to be downloaded
        file_name=resume_file_name,  # Name of the file that will be downloaded
        mime="docx"  # MIME type of the file
    )

    return uploaded_document,input_url,selected_option,process_button,resume_download_button
    # # Display the selected option
    # st.write(f"You selected: {selected_option}")