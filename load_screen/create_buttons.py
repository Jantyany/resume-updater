import streamlit as st
from file_readers_writers.docx_writer import save_string_to_docx,save_docx_to_binary

def create_output_button(text_type,text,model,company_name):
  
  # jd_path=os.path.join(os.path.dirname(cvpath),'job_description_'+company_name+'_'+model+'.docx')
  text_docx = save_string_to_docx(text)
  text_docx_bin = save_docx_to_binary(text_docx)

  text_docx_button_description=text_type+'_'+company_name+'_'+model+'.docx'
  st.markdown(text_docx_button_description) 
  # Create a download button for the job description docx file
  st.download_button(
      label="job description download",
      data=text_docx_bin,
      file_name=text_docx_button_description,
      mime="application/octet-stream"
  )