import pathlib
from pathlib import Path
from datetime import datetime
import sys
import os

p = Path("C:\Daten\Chroniktest")
for child in p.glob("**/*"):
    if child.is_file():

        print(child.name)
        print(child.parent)