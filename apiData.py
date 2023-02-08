import requests
import sys
from secrets import api_key, subdomain, identifier, format
from requests.auth import HTTPBasicAuth

apiUrl = "https://" + subdomain + ".wufoo.com/api/v3/forms/" + identifier + "/entries." + format


def get_api_info() -> dict:
    response = requests.get(apiUrl, auth=HTTPBasicAuth(api_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response
        print(f"ERROR: Failed to connected api and retrieve data, \n"
              f"Response code:{response.status_code} \n"
              f"Error message: {response.reason} ")
        sys.exit(-1)
    json_response = response.json()
    return json_response


def parse_file(filename):
    key = ["entry_id", "sign_up", "prefix", "first_name", "last_name", "title", "email", 'organization_site', "number",
           "permission"]
    with open(filename) as formFile:
        i = 0
        entries = []
        val = []
        parsed_data = dict()
        # Splits data and stores into entries
        for line in formFile:
            lines = line.split(',')
            entry = line.split(':')
            entries.append(entry)

        for i in entries:
            value = entries.pop()
            val.append(value)

        print(val[3])
    # print(entries[1][1])
    # i = i + 1


def main():
    api_data = get_api_info()
    data = api_data['Entries']
    file_to_save = open("Output.txt", 'w')
    save_data(data, save_file=file_to_save)
    get_Form_Entries()
    parse_file("output.txt")


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # print the line break and save file
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


def get_Form_Entries():
    d = {}
    filename = "output.txt"
    infoToFind = "Field117:"
    data_file = open(filename)
    with data_file as form_file:
        lines = []
        for line in form_file:
            lines.append(line)
            if infoToFind in line:
                print(line)
                print('String exist in a file')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
