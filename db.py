import mysql.connector

# prepare a cursor object using cursor() method
cursor = db.cursor()

# For creating create db
# Below line  is hide your warning
cursor.execute("SET sql_notes = 0; ")
# create db here....
cursor.execute("create database IF NOT EXISTS CUBE_Forms")



# create table
cursor.execute("SET sql_notes = 0; ")
cursor.execute("create table IF NOT EXISTS test (Sign Up varchar(70),Prefix varchar(10),First Name varchar(50),Last Name varchar(60),Title varchar(100),email varchar(70),Organization Website varchar(100),Number varchar(20),Permission varchar(10),pwd varchar(20));")
cursor.execute("SET sql_notes = 1; ")

#insert data
#cursor.execute("insert into test (Sign up,Prefix,First Name,Last Name,Title,email,Organization Website,Number,Permission,pwd) values('test@gmail.com','test')")

# Commit  changes in  database
db.commit()

# disconnect from server
db.close()
