# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```
2. adapt the environment to include and git to manage chrome
   ```
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   git lfs install
   git lfs track "google-chrome.deb"
   ```
to add chrome.deb to git repo using Large File System (LFS)
   ```
   git add google-chrome.deb
   git add .gitattributes
   git commit -m "Add google-chrome.deb using Git LFS"
   ```

3. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
4. considering authentication
   
blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/

https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso#option-2-individual-password-for-each-user

https://docs.streamlit.io/develop/tutorials/databases

6. 
