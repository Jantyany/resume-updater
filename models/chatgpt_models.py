import openai
import logging
import pandas as pd
import streamlit as st
# from openai.error import RateLimitError, OpenAIError
import time

def get_chgpt_api_key():
    return st.secrets.chgpt_api_key
    # return list(pd.read_csv(chgptcsv))[0]

def call_openai_with_retry(prompt, max_retries=3, retry_delay=5):
    retries = 0

    # Initialize logger
    logger = logging.getLogger(__name__)

    openai.api_key = get_chgpt_api_key()
    while retries < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response['choices'][0]['message']['content']

        # except RateLimitError as e:
        #     logger.warning(
        #         "Rate limit reached: %s. Retrying in %s seconds...",
        #         e, retry_delay
        #     )
        #     time.sleep(retry_delay)  # Wait before retrying
        #     retries += 1
        #     retry_delay *= 2  # Exponential backoff for subsequent retries

        except ClientError as err:
            logger.error(
                "Couldn't invoke ChatGPT. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise  # Reraise the exception if it's not a rate limit issue

    # If we run out of retries, raise an exception
    logger.error("Max retries reached. Could not complete the request.")
    raise Exception("Rate limit error after multiple retries")

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
      logger.error(
          "Couldn't invoke Chatgpt 4. Here's why: %s: %s",
          err.response["Error"]["Code"],
          err.response["Error"]["Message"],
      )
      raise