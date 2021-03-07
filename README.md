# Python API Examples
## by HundredVisionsGuy 

**Purpose:**  demonstrate how to use Python 3 and requests to capture and process JSON data 

## Strategies:
1. Find an open API from [Public APIs](https://github.com/public-apis/public-apis)
2. Build a custom URL by combining the 
    * base_url
    * endpoint
    * query parameters
    * Example: 
    ```
    base_url = "https://cat-fact.herokuapp.com"
    endpoint = "/facts/random?animal_type=cat&amount=3"
    url = base_url + endpoint
    ```
3. Make a json call using requests library
    ```
    resp = requests.get(url)
    ```
4. Test against the response 
    * 200 is good
    * anything else = bad
    ```
    if resp.status_code != 200:
        # something went wrong
    else:
        # Success!
        # Now is the time to have some fun.
    ```
5. use the `.json()` method to get the JSON response
    ```
    json_object = resp.json()
    ```
6. Loop through the JSON object and use the key to capture the specific data you want 
    ```
    for item in json_object:
        datum = item['json_key']
    ```
7. The other thing you can do is extract the currencies with their rates like so...
    ```
    # get all items & convert them to a list
    items = json_object.items()
    items = list( items )
    
    # Grab the rates (1st row, 2nd column)
    rates = items[0][1]
    
    # Get the currency and rates & convert them to a list
    rates = rates.items()
    rates = list(rates)
    ```
8. The REST is up to you (little API humor - just look up REST to see what I mean).

## Credits:  
 * [API Integration in Python](https://realpython.com/api-integration-in-python)
 * [Official Joke API](https://github.com/15Dkatz/official_joke_api)
 * [Public APIs](https://github.com/public-apis/public-apis)

