#
# Python 3.10
#
# Project: SQL .txt Practice
#
# Author: Lily Kiousis
#
# Requirments: 
#               1. Use Python 3 and sqlite3 module
#               2. The database will require 2 fields: an auto-increment primary
#                  integer field and a field with the data type “string.”
#               3. Your script will need to read from the supplied list of file names
#                  and determine only the files from the list which end with a .”txt”
#                  file extension. The Python code provided needs to be inserted exsctly
#                  as given. There is no need to create a folder on the computer that
#                  contains these files
#               4. The script should add those file names from the list ending with “.txt”
#                  file extension within your database.
#               5. The script should legibly print the qualifying text files to the console.
#               6. Comment the code.

#import sql module
import sqlite3

#connect and hold connection to database 
conn = sqlite3.connect('STP.db')

#with loop to create commands and tables in the database.
with conn:
    #creates command ability
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fName TEXT) \
                ")
    #commit table to DB
    conn.commit()

#adding files to database
conn = sqlite3.connect('STP.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object in the tuple to find the files that end with .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fName) VALUES (?)",(x,))
            print(x)

conn.close()
