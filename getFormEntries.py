import requests
import json
from apiData import apiUrl, api_key
from requests.auth import HTTPBasicAuth
import sys


response = requests.get(apiUrl, auth=HTTPBasicAuth(api_key, 'pass'))

if response.status_code != 200:  # if we don't get an ok response
    print(f"ERROR: Failed to connected api and retrieve data, \n"
         f"Response code:{response.status_code} \n"
         f"Error message: {response.reason} ")

    sys.exit(-1)

json_response = response.json()
result = '{"Time":"NONE","Prefix":"X","Name":"XX","Title":"xxx","Organization":"null","Email":"@mail","Number":"xxxxxxx"},"Permission":"No","Opportunies":"internship"'


val = json_response['Entries']

for key in json_response:
    for keys in val:
        keys.values()
#print(json_response)
