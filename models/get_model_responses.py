from chatgpt_models import call_openai_with_retry

def get_resp_chgpt(prompt):
  """
  Invokes Chatgpt to run an inference using the input
  provided in the request body.

  :param prompt: The prompt that you want Claude 3 to complete.
  :return: Inference response from the model.
  """

  try:
    return call_openai_with_retry(prompt)

  except Exception as err:
      logger.error(
          "Couldn't invoke Chatgpt 4. Here's why: %s: %s",
          err.response["Error"]["Code"],
          err.response["Error"]["Message"],
      )
      raise