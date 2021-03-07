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

# What happens if we print the response?
input("Press enter to see the response.")
print("The response is " + str(resp))

# test status (200 is what we want)
if resp.status_code != 200:
  # This means something went wrong.
  print("something went wrong")
else:
    # let's process the JSON object
    facts_json = resp.json()

    # What does the JSON object look like?
    input("Press enter to see what the JSON object looks like.")
    print(facts_json)

    # Note the data type
    input("Press enter to see what data type the JSON object is.")
    print( type(facts_json) )

    # TODO: Try to loop through facts_json

    # What does the first item look like?
    input("Press enter to see what the first item in the JSON object.")
    first_fact = facts_json[0]
    
    print( first_fact )

    # What is the first fact?
    input("Press enter to see what data type the first item is.")
    print( "The first fact is a " + str(type(first_fact)) )

    input("Press enter to see how to access elements of a dictionary.")
    print( "fact['type'] = " + first_fact['type'] )
    print( "fact['text'] = " + first_fact['text'] )

