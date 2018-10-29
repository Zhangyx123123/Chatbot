import json
import requests

def lambda_handler(event, context):
    url = "https://api.dialogflow.com/v1/query?v=20150910"
    message = event["messages"][0]['unstructured']['text']
    body={
        "contexts": "shop",
        "lang": "en",
        "query": message,
        "sessionId": "12345",
        "timezone": "America/New_York"
    }
    headers = {"Authorization": "Bearer 79e01fd3a9744922806bef4eef045a14","Content-Type":"application/json"}
    content = requests.post(url, headers=headers,json=body).json()
    response = content["result"]["fulfillment"]['speech']

    return {
        "statesCode": 200,
        "body": {
            "messages": [
                {
                  "type": 0,
                  "unstructured": {
                    "id": content["id"],
                    "text": content["result"]["fulfillment"]['speech'],
                    "timestamp": content["timestamp"]
                  }
                }
            ]
        }
    }