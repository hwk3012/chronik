import pathlib
from datetime import datetime
import sys
import os

import database_sqlite
import database

database.create_tables()

chronicle_dir = "C:\Daten\Desktop_20190912"
chronicle_dir = "C:\Daten\Chronik_20221202"
chronik = pathlib.Path(chronicle_dir)

database_sqlite.create_tables()

list1 = []
for item in chronik.iterdir():
    if item.is_file():
        filename = pathlib.Path(item).stem
        fileextension = pathlib.Path(item).suffix[1:]
        filesize = item.stat().st_size
        dt = datetime.fromtimestamp(item.stat().st_mtime)
        str_date_time = dt.strftime("%d.%m.%Y, %H:%M:%S")
        timestamp = item.stat().st_mtime
        t1 = (chronicle_dir, filename, fileextension, filesize, str_date_time, timestamp)
        list1.append(t1)

database.create_chronicle_item(list1)
database_sqlite.create_chronical_item(list1)