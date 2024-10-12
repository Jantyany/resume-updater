
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


def log_file_paths(cvpath:str, job_description_path:str, model_name:str,new_cvpath:str,cl_path:str):
  """
  Logs the input and output file paths to a CSV file.

  Args:
    cvpath: Path to the input CV file.
    job_description_path: URL of the job description.
    acccsv: Path to the CSV file containing access keys.
    seccsv: Path to the CSV file containing secret keys.
  """
  try:
    # Read existing log file if it exists
    log_path=os.path.join(os.path.dirname(cvpath),'LLM_resume_fixer_log_v1.csv')
    try:
      df = pd.read_csv(log_path)
    except FileNotFoundError:
      df = pd.DataFrame(columns=['Timestamp', 'CV_Path', 'Job_Description_Path','model_name','new_cvpath', 'cl_path'])

    # Create a new row with current data
    new_row = pd.DataFrame({
        'Timestamp': [datetime.datetime.now()],
        'CV_Path': [cvpath],
        'Job_Description_Path': [job_description_path],
        'model_name':model_name,
        'new_cvpath': [new_cvpath],
        'cl_path': [cl_path],
    })

    # Append the new row to the DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the updated DataFrame to the CSV file
    df.to_csv(log_path, index=False)

  except Exception as e:
    print(f"An error occurred: {e}")

