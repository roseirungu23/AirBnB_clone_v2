#!/usr/bin/python3
"""
Add a conditional depending of the value of the 
environment variable HBNB_TYPE_STORAGE
"""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
