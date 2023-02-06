import pathlib
from datetime import datetime
import sys
import os

import database_sqlite


database_sqlite.create_tables()

root_dir = "C:\Daten"
chronicle_dir = "C:\Daten\Desktop_20190912"

chronikdir = pathlib.Path(root_dir)
chronik =  pathlib.Path(chronicle_dir)

print(type(chronikdir))
dirlist = []
dirset = set()

for item in chronikdir.iterdir():
    #print(item)
    #print(f"{item} - {'dir' if item.is_dir() else 'file'}")
    if item.is_dir():
        dirlist.append(item)
        dirset.add(item)

print(dirlist)
for val in dirlist:
    pass
    #print(val)

print(dirset)
for val in dirset:
    pass
    #print(val)

#sys.exit()

for item in chronik.iterdir():
    if item.is_file():
        #####
        print(f"item: {item}")
        # PurePath.stem: The final path component, without its suffix:
        filename1 = pathlib.Path(item).stem
        filename2 = pathlib.Path(item).name
        print(f"filename1: {filename1}")
        print(f"filename2: {filename2}")
        print(os.path.basename(filename1))
        basename = os.path.splitext(os.path.basename(filename1))[0]
        print(f"basename: {basename}")
        print(f"pathlib.Path(item): {pathlib.Path(item)}")
        print(f"os.path.basename(item).split('.')[0]: {os.path.basename(item).split('.')[0]}")
        print(f"pathlib.Path(item).suffix: {pathlib.Path(item).suffix[1:]}")
        print(f"item.stat(): {item.stat()}")
        print(f"timestamp: {item.stat().st_mtime}")
        print(f"item.stat().st_size): {item.stat().st_size}")




        #date_time = datetime.fromtimestamp(item.stat().st_ctime)
        #d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
        dt = datetime.fromtimestamp(item.stat().st_mtime )
        str_date_time = dt.strftime("%d.%m.%Y, %H:%M:%S")
        print(f"The date and time is: {str_date_time}")

        #my_ctime = datetime.datetime.strptime(item.stat().st_ctime , "%d.%m.%Y")
        print("############################################################# + \n")

        list1 = []
        list2 = ["wer", 123456, "10.12.2019"]
        lt1 = tuple(list2)
        list1.append(lt1)

        list2 = ["asd", 555555, "11.11.1888"]
        lt1 = tuple(list2)
        list1.append(lt1)

        # root_path
        # TEXT,
        # item_name
        # TEXT,
        # file_extension
        # TEXT,
        # file_size
        # INTEGER,
        # timestamp
        # INTEGER,
        # file - datetime
        # TEXT,
        # item_source
        # INTEGER

    print(list1)