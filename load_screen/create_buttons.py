import streamlit as st
from file_readers_writers.docx_writer import save_string_to_docx,save_docx_to_binary
import zipfile
from io import BytesIO

def create_output_button(text_type,text,model,company_name):
  
  # jd_path=os.path.join(os.path.dirname(cvpath),'job_description_'+company_name+'_'+model+'.docx')
  text_docx = save_string_to_docx(text)
  text_docx_bin = save_docx_to_binary(text_docx)

  text_docx_button_description=text_type+'_'+company_name+'_'+model+'.docx'
  st.markdown(text_docx_button_description) 
  # Create a download button for the job description docx file
  st.download_button(
      label=text_type+" download",
      data=text_docx_bin,
      file_name=text_docx_button_description,
      mime="docx"
  )

def create_output_file(text_type,text,model,company_name):
  
  # jd_path=os.path.join(os.path.dirname(cvpath),'job_description_'+company_name+'_'+model+'.docx')
  text_docx = save_string_to_docx(text)
#   text_docx_bin = save_docx_to_binary(text_docx)
  text_docx_button_description=text_type+'_'+company_name+'_'+model+'.docx'
  st.markdown(text_docx_button_description) 
  return text_docx,text_docx_button_description

# Function to create a ZIP archive with multiple files
def create_zip(file_dict):
    # Create an in-memory BytesIO object to store the ZIP file
    zip_buffer = BytesIO()
    
    # Create a new ZIP file in the BytesIO buffer
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        # Add multiple files to the ZIP archive
        for key, value in file_dict.items():
            zip_file.writestr(value, key)
    
    # Move the buffer's pointer to the beginning
    zip_buffer.seek(0)
    
    return zip_buffer

def create_zip_output_button(file_dict):
    
    # Generate the ZIP file
    zip_data=create_zip(file_dict)

    # Create a download button for the ZIP file
    st.download_button(
        label="Download ZIP of job description, updated resume and cover letter",
        data=zip_data,  # The generated ZIP archive
        file_name="revised_output.zip",  # Name of the downloadable file
        mime="application/zip"  # MIME type for ZIP files
    )
#   # Create a download button for the job description docx file
#   st.download_button(
#       label=text_type+" download",
#       data=text_docx_bin,
#       file_name=text_docx_button_description,
#       mime="docx"
#   )