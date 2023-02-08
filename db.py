import mysql.connector

# For creating db
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="CUBE_Forms"
)
# prepare a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS CUBE_Forms")
# create table
insert_statement = ("CREATE TABLE IF NOT EXISTS CUBE_Forms (sign_up VARCHAR(70), prefix VARCHAR(5),first_name "
                    "VARCHAR(50),last_name VARCHAR(60),title VARCHAR(50),email VARCHAR(100),"
                    "organization_site VARCHAR(100), number VARCHAR(30), permission VARCHAR(10), entry_ID int PRIMARY "
                    "KEY AUTO_INCREMENT) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")


# insert data
cursor.execute(insert_statement)
#cursor.execute("insert into test (Sign up,Prefix,First Name,Last Name,Title,email,Organization Website,Number,"
#               "Permission,pwd) values('test@gmail.com','test')")

# Commit  changes in  database
db.commit()

# disconnect from server
db.close()
