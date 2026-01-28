import requests
import os
import uuid


# The complete API endpoint URL for this flow
url = "https://aws-us-east-2.langflow.datastax.com/lf/febe9155-ba52-4c9a-ac79-34c01ff3ee80/api/v1/run/ea29de89-372f-4df0-94cf-9e7092c6b2a9"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "What is Agentic AI"
}
payload["session_id"] = str(uuid.uuid4())

headers = {
    "X-DataStax-Current-Org": "b0459cde-2158-4aea-b2f2-074a051e9b1c", 
    "Authorization": "Bearer AstraCS:FyjOAZmEDMvvqJmlnMEFgPJD:be49d5621002c2734d123961dfe6937047182d5aabc11a66657eb5a6828a2b7e",
    "Content-Type": "application/json", 
    "Accept": "application/json",
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
