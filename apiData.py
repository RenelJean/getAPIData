import requests
import sys
from config import api_key, subdomain, identifier, formatted
from requests.auth import HTTPBasicAuth


apiUrl = "https://" + subdomain + ".wufoo.com/api/v3/forms/" + identifier + "/entries." + formatted
db_name = "cubesProject.sqlite"


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
    with open(filename) as formFile:
        i = 0
        entries = []
        row = []
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
    return row, entries


def prepare_result(data):
    if not isinstance(data, list):
        data = [data]
    result = []
    for location, entry in enumerate(data):
        result.append(
            {

                "entryID": entry[0],
                "prefix": entry[1],
                "first_name": entry[2],
                "last_name": entry[3],
                "title": entry[4],
                "org": entry[5],
                "email": entry[6],
                "website": entry[7],
                "course_project": True
                if len(entry[8]) > 0
                else False,  # inline if to assign true if the string was not ''
                "guest_speaker": True if len(entry[9]) > 0 else False,
                "site_visit": True if len(entry[10]) > 0 else False,
                "job_shadow": True if len(entry[11]) > 0 else False,
                "internship": True if len(entry[12]) > 0 else False,
                "career_panel": True if len(entry[13]) > 0 else False,
                "networking_event": True if len(entry[14]) > 0 else False,
                "subject_area": entry[15],
                "description": entry[16],
                "funding": entry[17],
                "created_date": entry[18],
            }

        )
    return result


# print(row_data)
# print(entries[1][1])
# i = i + 1


def main():
    api_data = get_api_info()
    data = api_data['Entries']
    file_to_save = open("Output.txt", 'w')
    save_data(data, save_file=file_to_save)


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # print the line break and save file
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file, )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
