import boto3


def get_resp_cl3(prompt):
    """
    Invokes Anthropic Claude 3 Sonnet to run an inference using the input
    provided in the request body.

    :param prompt: The prompt that you want Claude 3 to complete.
    :return: Inference response from the model.
    """

    acc=list(pd.read_csv(acccsv))[0]
    sec=list(pd.read_csv(seccsv))[0]

    # Initialize the Amazon Bedrock runtime client

    client = boto3.client(
        service_name="bedrock-runtime", region_name="us-west-2",aws_access_key_id=acc,aws_secret_access_key=sec
    )

    # Invoke Claude 3 with the text prompt
    # model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    model_id = 'anthropic.claude-3-haiku-20240307-v1:0'

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

    except ClientError as err:
        logger.error(
            "Couldn't invoke Claude 3 Sonnet. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise


