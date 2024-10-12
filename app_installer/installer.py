import subprocess
import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager

def install_chromium():
    st.write("Setting up headless Chromium...")
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    
    driver = webdriver.Chrome(options=options)
    
    st.success("Headless Chromium set up successfully!")


def install_chrome():
    try:
        # Set Chrome options
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Initialize the WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # Test it by navigating to a simple page
        driver.get("https://www.google.com")
        st.success(f"Successfully lodaed page title: {driver.title}")
        
        driver.quit()

    except Exception as e:
        st.error(f"An error occurred: {e}")

# # Define a function to run shell commands
# def install_chrome():
#     """
#     Install Google Chrome by downloading the .deb file, installing it, and cleaning up.
#     """
#     try:
#         # Download Google Chrome
#         st.write("Downloading Google Chrome...")
#         subprocess.run(['wget', '-q', 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'], check=True)

#         # Install using dpkg, this may also need sudo privileges, so check your environment
#         st.write("Installing Google Chrome using dpkg...")
#         subprocess.run(['sudo', 'dpkg', '-i', 'google-chrome-stable_current_amd64.deb'], check=True)

#         # Fix missing dependencies
#         st.write("Fixing missing dependencies...")
#         subprocess.run(['sudo', 'apt-get', '-f', 'install', '-y'], check=True)

#         # Clean up
#         subprocess.run(['rm', 'google-chrome-stable_current_amd64.deb'], check=True)
        
#         st.success("Google Chrome installed successfully!")

#     except subprocess.CalledProcessError as e:
#         st.error(f"An error occurred during installation: {e}")