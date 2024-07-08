import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://3f1c250e-0584-4078-a38c-42db42d8bbef.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '20b9fGG2IZz2d8C8Y33L9bvb4AcT75i4'

# Two sets of data to score, so we get two results back
data = {
  "Inputs": {
    "data": [
      {
        "age": 0,
        "job": "example_value",
        "marital": "example_value",
        "education": "example_value",
        "default": "example_value",
        "housing": "example_value",
        "loan": "example_value",
        "contact": "example_value",
        "month": "example_value",
        "day_of_week": "example_value",
        "duration": 0,
        "campaign": 0,
        "pdays": 0,
        "previous": 0,
        "poutcome": "example_value",
        "emp.var.rate": 0,
        "cons.price.idx": 0,
        "cons.conf.idx": 0,
        "euribor3m": 0,
        "nr.employed": 0
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
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


