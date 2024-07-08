import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://133e014f-3534-459e-8cfe-48273e919282.westeurope.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'GqMh4YuhZcTXStlLLGmRlmJTP8V8U367'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 30,
            "job": "unemployed",
            "marital": "married",
            "education": "primary",
            "default": "no",
            "balance": 1787,
            "housing": "yes",
            "loan": "yes",
            "contact": "cellular",
            "day": 19,
            "month": "may",
            "duration": 79,
            "campaign": 1,
            "pdays": 330,
            "previous": 1,
            "poutcome": "failure",
          }
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


