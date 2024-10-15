from models.chatgpt_models import call_openai_with_retry
import streamlit as st
import logging
from models.chatgpt_models import get_resp_chgpt
from models.aws_models import get_resp_cl1,get_resp_cl3
from file_readers_writers.writers import create_output_file
from load_screen.create_buttons import create_zip_output_button

def get_resp_chgpt(prompt):
  """
  Invokes Chatgpt to run an inference using the input
  provided in the request body.

  :param prompt: The prompt that you want Claude 3 to complete.
  :return: Inference response from the model.
  """
  # Initialize logger
  logger = logging.getLogger(__name__)

  try:
    return call_openai_with_retry(prompt)

  except Exception as err:
    # Handle any other unexpected errors
    logger.error(
        f"Unexpected Error: {err}"
    )
    raise
  
def company_name_jobrole_name_extraction(model,target_job):
  if model == 'cl1':
    return get_resp_cl1(f"extract the company name and the job/ role title from the following job description as a single string with an underscore delimiter with no comment or description: {target_job}")
  elif model == 'cl3':
    return get_resp_cl3(f"extract the company name and the job/ role title from the following job description as a single string with an underscore delimiter with no comment or description: {target_job}")
  elif model == 'ch4':
    return get_resp_chgpt(f"extract the company name and the job/ role title from the following job description as a single string with an underscore delimiter with no comment or description: {target_job}")
  
def jd_extractor(target_job,model):
  """
  Invokes model to run an inference using the input
  provided in the request body.

  :param prompt: The prompt that you want model to complete.
  :return: Inference response from the model.
  """
  jd_prompt_1 = f"You are an html parsing bot and are able to extract text from a web page document structure.\
  Please extract the details of the job description provided in the following job description webpage, particularly the below information:\
  1. Job Title and Department \
  Job Title: The official title of the role, which indicates the level (junior, mid-level, senior) and specialization (e.g., Data Scientist, ESG Analyst). \
  Department: The team or division within the company where this role sits (e.g., Finance, Engineering, ESG, etc.), which can provide insight into the type of work and stakeholders. \
  2. Key Responsibilities and Duties \
  Core Tasks: Understand the day-to-day responsibilities of the role. This section outlines what the job entails and the specific tasks you'll be expected to perform (e.g., building models, conducting research, preparing reports). \
  Scope of Work: Clarifies if the role is technical, managerial, research-focused, client-facing, etc. For example, do they expect you to manage teams, work independently, or collaborate cross-functionally? \
  3. Required Skills and Qualifications \
  Technical Skills: These include programming languages, software tools, frameworks, and domain-specific knowledge (e.g., Python, SQL, machine learning, ESG standards). \
  Soft Skills: Qualities like communication, leadership, teamwork, problem-solving, and adaptability. \
  Certifications or Degrees: If specific certifications (e.g., CFA, FRM, ESG certifications) or degrees (e.g., MSc, MBA) are required or preferred, these should be noted. \
  4. Experience Level \
  Years of Experience: Whether the role requires a certain number of years in a related field (e.g., 5+ years of experience in data analysis or ESG research). \
  Industry or Domain Experience: Some roles might specify experience in particular industries (e.g., finance, tech, energy) or functions (e.g., investment management, quantitative research). \
  5. Preferred Qualifications (Nice-to-Have) \
  These qualifications are not mandatory but are desirable (e.g., knowledge of a niche software tool, experience with a particular methodology). This helps you understand what might set you apart from other applicants. \
  6. Key Performance Indicators (KPIs) or Success Metrics \
  Some job descriptions outline the goals or metrics by which success in the role will be measured (e.g., meeting sales targets, increasing operational efficiency, developing high-performing models). \
  This gives you an understanding of what the company values and the impact they expect you to deliver. \
  7. Company Overview and Culture \
  Mission and Values: Insight into the company's purpose and cultural priorities (e.g., sustainability focus, innovation-driven). \
  Work Environment: Information on the work culture, remote/hybrid working options, and team dynamics (e.g., collaborative vs. independent work). \
  8. Compensation and Benefits \
  Salary: If listed, this gives an idea of compensation. Some descriptions might include salary ranges or competitive pay. \
  Benefits: Mention of benefits like healthcare, pension plans, stock options, bonuses, or educational stipends can give insights into the overall package. \
  9. Location and Travel Requirements \
  Work Location: Whether the position is based in a specific city or offers remote, hybrid, or flexible working options. \
  Travel: Any indication of travel expectations (e.g., up to 25% travel), which might affect your interest in the role. \
  10. Application Process \
  Deadline: If there's a specific application closing date, this helps you prioritize your applications. \
  Submission Requirements: Details on what needs to be submitted (e.g., resume, cover letter, portfolio, references). \
  Screening Process: Some descriptions may provide insight into the interview stages (e.g., technical test, behavioral interviews, case studies). \
  11. Growth Opportunities and Career Path \
  Promotions or Progression: Indications of career growth, leadership opportunities, or development pathways within the company. \
  Learning and Development: Whether the role offers training programs or continued learning opportunities (e.g., professional development, conference attendance). \
  12. Technological Stack and Tools (for Technical Roles) \
  Software and Tools: The job description may specify the technology stack or tools the company uses \
  job description webpage: {target_job}.\
  provide only the output which should feature on a job description.\
  Please provide only a 200 words output"

  if model == 'cl1':
    return get_resp_cl1(jd_prompt_1)
  elif model == 'cl3':
    return get_resp_cl3(jd_prompt_1)
  elif model == 'ch4':
    return get_resp_chgpt(jd_prompt_1)
  
def resume_rewriter(current_cv,target_job,model):
  """
  Invokes model to run an inference using the input
  provided in the request body.

  :param prompt: The prompt that you want model to complete.
  :return: Inference response from the model.
  """
  res_prompt_1 = f"You are a resume writing expert that targets key skills and experience listed in a target job description and highlights this is a provided resume.\
  You know how to extract the key words from a job description to place in a candidate resume experience and skills sections. \
  Please rewrite the experience and skills sections of the following candidate resume to highlight the skills ans experience requirements of the target job description. \
  Rewrite the current experience paragraphs, including keywords and requirements from the target job description.\
  candidate resume: {current_cv}\
  target job description: {target_job}.\
  provide only the complete resume or CV document. Do not include any introductory/ presenatation/ descriptive text before or after the document content."

  if model == 'cl1':
    return get_resp_cl1(res_prompt_1)
  elif model == 'cl3':
    return get_resp_cl3(res_prompt_1)
  elif model == 'ch4':
    return get_resp_chgpt(res_prompt_1)
  
def cover_letter_writer(new_cv,target_job,model):
  """
  Invokes model to run an inference using the input
  provided in the request body.

  :param prompt: The prompt that you want model to complete.
  :return: Inference response from the model.
  """
  cl_prompt_1 = f"You are a recruitment expert that targets key skills and synergies between a provided job description and candidate resume.\
  You are tasked with producing a job application cover letter which descries the skill and experience of the candidate resume and matches it to the requirements of a job description.\
  Please write a two paragraph or four hundred word length job application cover letter highlighting the most recent work experience and skills from the following candidate resume which matches job description.\
  Do not add any extra experience paragraphs only rewrite the current experience paragraphs as required.\
  candidate resume: {new_cv}\
  job description: {target_job}\
  provide only the output which should feature on in the cover letter document"

  if model == 'cl1':
    return get_resp_cl1(cl_prompt_1)
  elif model == 'cl3':
    return get_resp_cl3(cl_prompt_1)
  elif model == 'ch4':
    return get_resp_chgpt(cl_prompt_1)
  
def run_model(job_description_path:str,current_cv:str,current_cv_filename:str,target_job:str,model:str):

  company_name=company_name_jobrole_name_extraction(model,job_description_path)
  
  filedict = {}

  # jd=jd_extractor(target_job,model)
  # jd_docx,jd_docx_name=create_output_file('job_description',jd,model,company_name)
  # # create_output_button('job_description',jd,model,company_name)
  # filedict[jd_docx_name]=jd_docx

  new_resume=resume_rewriter(current_cv,jd,model)
  new_resume_filename = current_cv_filename.replace('.docx','')
  # new_resume_docx,new_resume_docx_name=create_output_file(new_resume_filename,new_resume,model,company_name)
  create_output_button(new_resume_filename,new_resume,model,company_name)
  
  # filedict[new_resume_docx_name]=new_resume_docx

  # cover_letter = cover_letter_writer(new_resume,target_job,model)
  # cover_letter_docx,cover_letter_name=create_output_file('cover_letter_',cover_letter,model,company_name)
  # # create_output_button('cover_letter_',cover_letter,model,company_name)
  # filedict[cover_letter_name]=cover_letter_docx

  # create_zip_output_button(filedict)
