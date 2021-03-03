########################################
# Another example using the JokeAPI
########################################
# import statements
import requests
import random

# Initialize lists to store API data
setups = []
punchlines = []

# Make the API call and store JSON object in response
resp = requests.get("https://official-joke-api.appspot.com/random_ten")
if resp.status_code != 200:
  # This means something went wrong.
  print("something went wrong")
else:
    # Iterate through the response items
    for joke in resp.json():
        # Capture and add data by key
        setups.append(joke['setup'])
        punchlines.append(joke['punchline'])

    # pick & display a random joke
    i = random.randrange(len(setups))
    print(setups[i])
    answer = input()
    if answer == punchlines[i]:
        print("Correct")
    else:
        print(punchlines[i])

