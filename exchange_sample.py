# Import request library
import requests

# build out the url request
base_url = "https://api.exchangeratesapi.io"
endpoint = "/latest"
query_params = "?base=USD"
url = base_url + endpoint + query_params

# Make the API call
resp = requests.get(url)

# test the status code
if resp.status_code != 200:
  print("Something went wrong.")
else:
  # Process the JSON object
  json_object = resp.json() 
  print("Python calls the json_object a " + \
    str(type(json_object)))

  # Get just the rates
  rates = json_object.items()

  # Convert the JSON object items into a list
  rates = list( rates )

  # Get the 2nd item from the 1st row 
  rates = rates[0][1]

  # Convert that dictionary's items into a list
  rates = rates.items()
  rates = list( rates )

  # rates is now a list of rates
  print(rates)

  # The REST is up to you