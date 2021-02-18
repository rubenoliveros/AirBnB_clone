#!/usr/bin/python3
"""
File containing the Filestorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Used for serializing/deserializing JSON files"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all key - value pairs on the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets obj with the class name ID"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dic = {}
        for key, value in self.__objects.items():
            new_dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dic, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    self.__objects[key] = eval("BaseModel(**value)")
        except:
            pass
