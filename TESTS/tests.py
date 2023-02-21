import os
import apiData
import db


def test_file(file_name):
    os.path.exists(file_name)
    if os.stat(file_name).st_size == 0:
        print("Error File has no text, Empty text file")
    else:
        json_data = apiData.get_api_info()
        entries = json_data['Entries']
        assert len(entries) >= 10


def test_db():
    connection, cursor = db.open_db("test.db")
    db.open_db("output.txt")
    cursor.execute("SELECT Count() FROM SQLITE_MASTER WHERE name = ?", ["WuFooData"])
    record = cursor.fetchone()
    number_of_rows = record[0]  # the number is the first )and only) item in the tuple
    assert number_of_rows == 1
