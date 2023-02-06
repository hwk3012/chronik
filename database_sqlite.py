
import sqlite3

CREATE_CHRONICLE_ITEM_TABLE = """CREATE TABLE IF NOT EXISTS chronicle_item (
    id INTEGER PRIMARY KEY,
    root_path TEXT,
    item_name TEXT,
    file_extension TEXT,
    file_size INTEGER,
    file_datetime_timestamp REAL,
    file_datetime TEXT,
    item_source INTEGER    
);"""

INSERT_CHRONICLE_ITEM = "INSERT INTO chronicle_item (root_path, item_name, file_extension, file_size, file_datetime, file_datetime_timestamp) VALUES (?, ?, ?, ?, ?, ?);"

connection = sqlite3.connect("chronicle.db")

def create_tables():
    with connection:
        connection.execute(CREATE_CHRONICLE_ITEM_TABLE)

def create_chronical_item(options):
    with connection:
        cursor = connection.cursor()
        for option_value in options:
            cursor.execute(INSERT_CHRONICLE_ITEM, option_value)

