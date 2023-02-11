import requests
import sys
from secrets import api_key, subdomain, identifier, format
from requests.auth import HTTPBasicAuth
import os

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


# test to see if file exist and if empty
def test_file(file_name):
    os.path.exists(file_name)
    if os.stat(file_name).st_size == 0:
        print("Error File has no text, Empty text file")


def parse_file(filename):
    with open(filename) as formFile:
        i = 0
        row = []
        columns = ["entry_ID", "sign_up", "prefix", "first_name", "last_name", "email", "organization_site", "number",
                   "permission", "reasons"]
        entries = []
        # Splits data and stores into entries
        for line in formFile:
            entry = line.split(':')
            entries.append(entry)

        for i in range(len(entries)):
            # print(entries[i][1])

            if i == 26:
                break
            line = entries[i][1].strip("\n")
            # print(entries[25][1])
            # if line not blank store row data
            if line != " ":
                row.append(line)

        print(row)

    return row, columns
    # print(entries[1][1])
    # i = i + 1


def main():
    # api_data = get_api_info()
    # data = api_data['Entries']
    # file_to_save = open("Output.txt", 'w')
    # save_data(data, save_file=file_to_save)
    parse_file("output.txt")


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # print the line break and save file
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
