#Phil Brown Assignment 9.2 8/6/2026

#code modified from https://www.dataquest.io/blog/api-in-python/

import requests

#commented out Astronaut data to run pokemon data
"""
response = requests.get("http://api.open-notify.org/astros.json") 
print(response.status_code)


import json

# create a formatted string of the Python JSON object
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())
"""


#code modified from https://www.dataquest.io/blog/api-in-python/

import json
response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard") 
print(response.status_code)
#print(response.json())

def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())