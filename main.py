import apiData
import db
from db import open_db, close_db
import GUI

db_name = "cubesProject.sqlite"


def main():
    json_res = apiData.get_api_info()
    conn, cursor = open_db(db_name)
    entries_list = json_res["Entries"]
    db.create_entries(cursor)
    db.add_entries(cursor, entries_list)

    db.create_users()
    user_input = db.user_info()
    user_info = db.user_data(user_input)
    db.add_users(cursor, user_info, entries_list)
    db.add_users(cursor, user_info, entries_list)
    #GUI
    close_db(conn)
   # print(entries_list[5])


if __name__ == "__main__":
    main()
