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
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dic = {}
        for key, value in self.__objects.items():
            new_dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dic, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
          """ Reload method """
        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp_dict = json.load(f)
            for item in tmp_dict.values():
                cls_name = item["__class__"]
                del item["__class__"]
                self.new(eval(cls_name)(**item))
        except:
            pass
