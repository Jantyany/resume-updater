import streamlit as st
import json
import logging

def get_hf_api_key():
    return st.secrets.hf_credentials.hf_key,st.secrets.hf_credentials.hf_secret
    # return list(pd.read_csv(acccsv))[0],list(pd.read_csv(seccsv))[0]

def get_resp_cl3(prompt):
    return get_resp_template(prompt, 'anthropic.claude-3-haiku-20240307-v1:0')

def get_resp_template(prompt, model_id):
    """
    Invokes AWS foundation models to run an inference using the input
    provided in the request body.

    :param prompt: The prompt that you want Claude 3 to complete.
    :return: Inference response from the model.
    """
    # Initialize logger
    logger = logging.getLogger(__name__)

    acc,sec=get_aws_api_key()

    # Initialize the Amazon Bedrock runtime client

    client = boto3.client(
        service_name="bedrock-runtime", region_name="us-west-2",aws_access_key_id=acc,aws_secret_access_key=sec
    )

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(
                {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 1024,
                    "messages": [
                        {
                            "role": "user",
                            "content": [{"type": "text", "text": prompt}],
                        }
                    ],
                }
            ),
        )

        # Process and print the response
        result = json.loads(response.get("body").read())
        input_tokens = result["usage"]["input_tokens"]
        output_tokens = result["usage"]["output_tokens"]
        output_list = result.get("content", [])
        return result['content'][0]['text']

    # except ClientError as err:
    # except client.exceptions.NoSuchEntityException as err:
    #     logger.error(
    #         "Couldn't invoke Claude 3 Sonnet. Here's why: %s: %s",
    #         err.response["Error"]["Code"],
    #         err.response["Error"]["Message"],
    #     )
    #     raise  # Reraise the exception if it's not a rate limit issue
    except Exception as e:
        # Handle any other unexpected errors
        logger.error(
            f"Unexpected Error: {e}"
        )
