import sqlite3
from typing import Tuple


# For creating db
def open_db(filename) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)
    # prepare a cursor object using cursor() method
    cursor = connection.cursor()
    return connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


# create table
def create_entries(cursor: sqlite3.Cursor):
    form_table =  """CREATE TABLE IF NOT EXISTS WuFooData(
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
def add_entries(cursor: sqlite3.Cursor, entries: list[dict]):
    insertStatement = """INSERT OR IGNORE INTO WuFooData (entry_ID, prefix, first_name, last_name, title, 
    organization_site, email, website, course_project, guest_speaker, site_visit, job_shadow, internship, 
    career_panel, networking_event, subject_area, description, funding, created_date, created_by) VALUES(?,?,?,?,?,?,
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries:
        entry_val = list(entry.values())
        entry_val[0] = int(entry_val[0])  # turns id to int
        entry_val = entry_val[:-2]
        cursor.execute(insertStatement, entry_val)


# cursor.execute("insert into test (Sign up,Prefix,First Name,Last Name,Title,email,Organization Website,Number,"
#               "Permission,pwd) values('test@gmail.com','test')")

curs, conn = open_db("output.txt")

create_entries(curs)

