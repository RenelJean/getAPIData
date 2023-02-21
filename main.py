import db
from db import open_db, close_db
import apiData


def main():
    json_res = apiData.get_api_info()
    connection, cursor = open_db("cubesForms.sqlite")
    entries_list = json_res["Entries"]
    db.create_entries(cursor)
    db.add_entries(cursor, entries_list)
    close_db(connection)


if __name__ == "__main__":
    main()
