import requests
from bs4 import BeautifulSoup

def get_html_text_requests(url):
  """
  Navigates to a provided URL and retrieves the text from within the HTML.

  Args:
    url: The URL to navigate to.

  Returns:
    A string containing the text extracted from the HTML.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving text from URL: {e}")
    return None