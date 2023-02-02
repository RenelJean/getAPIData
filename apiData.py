import requests
import sys
from secrets import api_key,subdomain,identifier,format;
from requests.auth import HTTPBasicAuth


apiUrl ="https://"+subdomain+".wufoo.com/api/v3/forms/"+identifier+"/entries."+format;



def get_api_info() -> dict:
    response = requests.get(apiUrl, auth=HTTPBasicAuth(api_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"ERROR: Failed to connected api and retrieve data, \n"
              f"Response code:{response.status_code} \n"
              f"Error message: {response.reason} ")
        sys.exit(-1)
    json_response = response.json()
    return json_response


def main():
    api_data = get_api_info()
    data = api_data['Entries']
    file_to_save = open("output.txt", 'w')
    save_data(data, save_file=file_to_save)


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        #print the line break and save file
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
