import streamlit as st

def load_intro():
    st.title("resume highlighter app")

    bullet_points = """
    - Enter your CV or resume in docx format

    - Enter your target job url

    - select an LLM model

    - press the Process button
    """

    # st.title("Enter your CV/ resume,
    #          your target job url,\r 
    #          select an LLM model and \r 
    #          press the Process button")

    # st.write(
    #     "Upload your resume document below"
    # )

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

    return uploaded_document,input_url,selected_option,process_button
    # return {'uploaded_document':uploaded_document,\
    #         'input_url':input_url,\
    #         'selected_option':selected_option,\
    #         'process_button':process_button}
    # # Display the selected option
    # st.write(f"You selected: {selected_option}")