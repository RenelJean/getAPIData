import sqlite3
from typing import Tuple


# For creating db
def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(
        filename
    )  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


# create table
def create_entries(cursor: sqlite3.Cursor):
    form_table = """CREATE TABLE IF NOT EXISTS WuFooData(
     entryID INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    org TEXT,
    email TEXT,
    website TEXT,
    course_project BOOLEAN,
    guest_speaker BOOLEAN,
    site_visit BOOLEAN,
    job_shadow BOOLEAN,
    internship BOOLEAN,
    career_panel BOOLEAN,
    networking_event BOOLEAN,
    subject_area TEXT NOT NULL,
    description TEXT,
    funding BOOLEAN,
    created_date TEXT,
    created_by TEXT);"""

    cursor.execute(form_table)





# insert data
def add_entries(cursor: sqlite3.Cursor, entries_data: list[dict]):
    insertStatement = """INSERT OR IGNORE INTO WuFooData (entryID, prefix, first_name, last_name, title, org, email, 
    website, course_project, guest_speaker, site_visit, job_shadow, internship, career_panel, networking_event, 
    subject_area, description, funding, created_date, created_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    i = 0

    for entry in entries_data:

        entry_values = list(
            entry.values()
        )  # get the list of values from the dictionary
        entry_values[0] = int(
            entry_values[0]
        )  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:-6]
#        while "" in entry_values:
#            entry_values.remove("")
        print(entry_values[0])

        cursor.execute(insertStatement, entry_values)
