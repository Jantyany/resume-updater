from web_readers.html_requests import get_html_text_requests
from web_readers.html_chrome import get_html_text_selenium

def get_html_job(job_description_path):
  target_job=get_html_text_requests(job_description_path)
  try:
     if target_job.replace(' ','').replace('\n','')!='':
       return target_job
  except Exception as e:
    print(f"Error retrieving text from URL: {e}")
    try:
      return get_html_text_selenium(job_description_path)
    except Exception as e:
      print(f"Error retrieving text from URL: {e}")