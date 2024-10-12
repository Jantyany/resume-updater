from docx import Document

def extract_docx_text(file_path):
  """
  Extracts text from a docx file including formatting.

  Args:
    file_path: Path to the docx file.

  Returns:
    A string containing the extracted text with formatting.
  """
  try:
    doc = Document(file_path)
    fullText = []
    for para in doc.paragraphs:
      fullText.append(para.text)
    return '\n'.join(fullText)
  except Exception as e:
    print(f"Error extracting text from docx file: {e}")
    return None
