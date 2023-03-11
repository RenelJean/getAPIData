import sys

import PySide6

import apiData
import db
import gui_screen
from db import open_db, close_db

db_name = "cubesProject.sqlite"


def sprint2():  # comment for force workflow
    json_response = apiData.get_api_info()
    entries_list = json_response["Entries"]
    print(entries_list[10])
    conn, cursor = open_db(db_name)
    db.create_entries_table(cursor)
    db.add_entries_to_db(cursor, entries_list)
    close_db(conn)


def sprint3():
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = gui_screen.WuFooEntriesWindow()
    my_window.setWindowTitle("Instructor Demo Comp490 2023")
    sys.exit(qt_app.exec())


def show_options():
    print("=======================================")
    print("[1] Update the database with wufoo data")
    print("[2] Run the Graphical Program")
    print("=======================================")


def main():
    json_res = apiData.get_api_info()
    conn, cursor = open_db(db_name)
    entries_list = json_res["Entries"]
    db.create_entries(cursor)
    db.add_entries(cursor, entries_list)
    gui_screen
    close_db(conn)
   # print(entries_list[5])


if __name__ == "__main__":
    main()
