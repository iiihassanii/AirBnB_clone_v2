#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

# Check the value of the environment variable HBNB_TYPE_STORAGE
storage_type = os.getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    # Import the DBStorage class and create an instance
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # Default to FileStorage if the environment variable is not set to "db"
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Execute storage reload() after instantiating storage
storage.reload()
