import streamlit as st

def load_intro():
    st.title("resume highlighter app")

    bullet_points = """
    - Enter your CV or resume

    - Enter your target job url

    - select an LLM model

    - press the Process button
    """
    st.markdown(bullet_points)

    # st.title("Enter your CV/ resume,
    #          your target job url,\r 
    #          select an LLM model and \r 
    #          press the Process button")

    # st.write(
    #     "Upload your resume document below"
    # )

    # File uploader widget
    uploaded_document = st.file_uploader("Upload a resume document in docx format", \
                                        type=["docx"])

    # Text input for URL
    input_url = st.text_input("Enter a  URL")

    # Dropdown menu with three options
    selected_option = st.selectbox(
        "Choose an LLM model:",  # Label for the dropdown
        ["ChatGPT 4o", "Claude Instant v1", "Claude v3 Haiku"]  # List of options
    )

    return uploaded_document,input_url,selected_option
    # # Display the selected option
    # st.write(f"You selected: {selected_option}")