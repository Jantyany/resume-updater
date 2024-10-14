from docx import Document

def save_string_to_docx(text, filepath):
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
    doc.save(filepath)
    print(f"File saved successfully to: {filepath}")
  except Exception as e:
    print(f"Error saving file: {e}")