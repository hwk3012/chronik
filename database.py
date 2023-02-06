import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import sqlite3

CREATE_CHRONICLE_ITEM_TABLE = """CREATE TABLE IF NOT EXISTS chronicle_item (
    id SERIAL PRIMARY KEY,
    root_path TEXT,
    item_name TEXT,
    file_extension TEXT,
    file_size INTEGER,
    file_datetime_timestamp REAL,
    file_datetime TEXT,
    item_source INTEGER    
);"""

INSERT_CHRONICLE_ITEM = "INSERT INTO chronicle_item (root_path, item_name, file_extension, file_size, file_datetime, file_datetime_timestamp) VALUES %s;"         # %s => Tupel!

load_dotenv()

connection = psycopg2.connect(
    user=os.getenv("DATABASE_USERNAME"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_IP"),
    port=os.getenv("DATABASE_PORT"),
    database=os.getenv("DATABASE_NAME")
)

def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_CHRONICLE_ITEM_TABLE)

def create_chronicle_item(options):
    with connection:
        with connection.cursor() as cursor:
            chronical_values = [x for x in options]
            execute_values(cursor, INSERT_CHRONICLE_ITEM, chronical_values)
