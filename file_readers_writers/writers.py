from docx import Document
from io import BytesIO
import streamlit as st
import zipfile

def save_string_to_docx(text):
  """
  Saves a string to a docx file.

  Args:
    text: The string to be saved.
    filepath: The path to the docx file to be created.
  """
  try:
    doc = Document()
    #bold_text=convert_to_bold(text)
    doc.add_paragraph(text)
    return doc
    # doc.save(filepath)
    # print(f"File saved successfully to: {filepath}")
  except Exception as e:
    print(f"Error saving file: {e}")

def save_docx_to_binary(docx):
  """
  convert a docx file to binary.

  Args:
    docx: The file to be converted.
  """
  try:
    buffer = BytesIO()
    docx.save(buffer)
    docx_binary = buffer.getvalue()  # Extract the binary data
    # Check if data is binary
    if isinstance(docx_binary, (bytes, bytearray)):
        # st.write("The data is in binary format.")
        return docx_binary
    else:
        st.write("The data is NOT in binary format to provide for download.") 
  except Exception as e:
    print(f"Error converting file: {e}")


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
            value_binary = save_docx_to_binary(value)
            zip_file.writestr(key, value_binary)
    
    # Move the buffer's pointer to the beginning
    zip_buffer.seek(0)
    
    return zip_buffer