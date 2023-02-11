import sqlite3
from sqlite3 import Error
from apiData import row_data, parse_file

# For creating db
connection = sqlite3.connect('cube_forms.db')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# create table
form_table = "CREATE TABLE IF NOT EXISTS stores(entry_ID int PRIMARY KEY, sign_up TEXT, prefix TEXT,first_name TEXT, " \
        "last_name TEXT,title TEXT,email TEXT, organization_site TEXT, number TEXT, permission TEXT)"

data = parse_file(filename="output.txt")
col = data[1]
row = data[0]


# creates tables
cursor.execute(form_table)

# insert data
cursor.execute('INSERT INTO forms_table VALUES(?,?,?,?,?,?,?,?,?,?);', row_data)
# cursor.execute("insert into test (Sign up,Prefix,First Name,Last Name,Title,email,Organization Website,Number,"
#               "Permission,pwd) values('test@gmail.com','test')")
