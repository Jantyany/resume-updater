from docx import Document
from io import BytesIO


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
    return docx_binary
  except Exception as e:
    print(f"Error converting file: {e}")
