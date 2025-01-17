#!/usr/bin/python3


"""This module instantiates an object of class FileStorage"""


import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity

storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
