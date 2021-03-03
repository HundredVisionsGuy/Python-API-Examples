##########################################################
# cat_facts.py
# by Chris Winikka 
#
# Purpose:  demonstrate how to use Python 3 and requests
#           to capture and process JSON data 
##########################################################


# import statements
import requests

# Build out a new API call url
base_url = "https://cat-fact.herokuapp.com"
endpoint = "/facts/random"
query_params = "?animal_type=cat&amount=3"
# You could have the user select amount or type

url = base_url + endpoint + query_params

# new API call
resp = requests.get(url)

# test status (200 is what we want)
if resp.status_code != 200:
  # This means something went wrong.
  print("something went wrong")
else:
    # let's process the JSON object
    facts_json = resp.json()
    cat_facts = []

    for fact in facts_json:
        cat_facts.append(fact['text'])

    # show each dog fact on its own line
    for i in cat_facts:
        print(i)

