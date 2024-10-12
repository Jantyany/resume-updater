import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager


def get_html_text_selenium(url):
    """
    Uses Selenium with the Chrome WebDriver to connect to a webpage,
    scroll down, and download the content into a string.
    """

    # Set up the Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920x1080')
    # chrome_options.binary_location = '/usr/bin/google-chrome'

    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # # Initialize the WebDriver
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # # Test it by navigating to a simple page
    # driver.get("https://www.google.com")
    # st.success(f"Successfully lodaed page title: {driver.title}")
    
    # driver.quit()

    # Initialize the WebDriver
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Navigate to the webpage
        driver.get(url)

        # Scroll down to the bottom to load dynamic content
        scroll_pause_time = 2  # Adjust as needed
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for new content to load
            time.sleep(scroll_pause_time)

            # Calculate new scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # If height hasn't changed, exit loop
            last_height = new_height

        # Get page content
        page_content = driver.page_source

        return page_content

    finally:
        # Close the driver
        driver.quit()
