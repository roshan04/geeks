import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT, email TEXT, phone TEXT,intime TEXT,outtime TEXT)')
print ("Table created successfully")
conn.close()