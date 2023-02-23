import pathlib
import sys
from datetime import datetime

import database_sqlite
import database

database.create_tables()
database_sqlite.create_tables()

chronicle_dir = "C:\Daten\Desktop_20190912"
# chronicle_dir = "C:\Daten\Chronik_20221202"
chronicle_dir = r"C:\Daten\Chronik\Chronik"
chronik = pathlib.Path(chronicle_dir)

list1 = []

for item in chronik.iterdir():
# for item in chronik.glob('**/*'):     # rekursiv in Unterverz.
    if item.is_file():
        filepath = str(item.parent)
        filename = pathlib.Path(item).stem
        fileextension = pathlib.Path(item).suffix[1:]
        filesize = item.stat().st_size
        dt = datetime.fromtimestamp(item.stat().st_mtime)
        str_date_time = dt.strftime("%d.%m.%Y, %H:%M:%S")
        timestamp = item.stat().st_mtime
        rt = database.search_chronicle_item(chronicle_dir, filename)
        if rt:
            if rt[5] < timestamp:
                database.delete_chronicle_item(rt[0])
                t1 = (filepath, filename, fileextension, filesize, str_date_time, timestamp)
                list1.append(t1)
        else:
            t1 = (filepath, filename, fileextension, filesize, str_date_time, timestamp)
            list1.append(t1)


database.create_chronicle_item(list1)
#database_sqlite.create_chronical_item(list1)

