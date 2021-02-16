#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        id_ = obj.id
        key = obj.__class__.__name__
        self.__objects[key+"."+id_] = obj

    def save(self):
        new_dic = {}
        for key, value in self.__objects.items():
            new_dic[key] = value.to_dict()
            
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dic, file)

    def reload(self):
        try:    
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    self.__objects[key] = eval("BaseModel(**value)")
        except:
            pass 
