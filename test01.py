import sqlite3
import csv
from datetime import datetime
from uuid import uuid4

connection = sqlite3.connect("data.db")

# CREATE_TABLE_POSTS = """CREATE TABLE IF NOT EXISTS posts (
#     id INTEGER PRIMARY KEY, 
#     post_name TEXT,
#     file_size INTEGER,
#     file_timestamp REAL,
#     FOREIGN KEY (id) REFERENCES sources(id)
#     );"""
CREATE_TABLE_POSTS = """CREATE TABLE IF NOT EXISTS posts (
    id TEXT PRIMARY KEY, 
    post_name TEXT,
    file_size INTEGER,
    file_timestamp REAL,
    file_source INTEGER,
    FOREIGN KEY (file_source) REFERENCES sources(id)
    );"""
CREATE_TABLE_SOURCE = """CREATE TABLE IF NOT EXISTS sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    source_name TEXT
    );"""

SELECT_POSTS = """SELECT post_name, sources.source_name FROM posts
JOIN sources ON sources.id = posts.file_source
"""

connection.execute(CREATE_TABLE_POSTS)
with connection:
    connection.execute(CREATE_TABLE_SOURCE)
    
my_list = []
with open('/home/hwk/test1.csv', 'r', encoding='utf-8-sig') as csv_datei:
    reader = csv.reader(csv_datei, delimiter=';')
    for zeile in reader:
        my_list.append(zeile)
        

c = connection.cursor()

# with connection:
#     c.execute("INSERT INTO sources(id, source_name) VALUES(?, ?)", (1, "Quelle 1"))

# with connection:
#     for item in my_list:
#         _id = str(uuid4())
#         file_size = int(item[2].replace(".", ""))
#         file_date_object = datetime.strptime(item[3], "%d.%m.%Y")
#         file_date_timestamp = datetime.timestamp(file_date_object)
        
#         c.execute("INSERT INTO posts(id, post_name, file_size, file_timestamp, file_source) VALUES(?, ?, ?, ?, ?)", (_id, item[1], file_size, file_date_timestamp, 1))

with connection:
    c.execute(SELECT_POSTS)    
    x = c.fetchall
    for item in c:
        print(item)

#connection.commit()  
 
connection.close()

a = 123_456_789
print(type(a))
b = 734_529.678
print(type(b))

