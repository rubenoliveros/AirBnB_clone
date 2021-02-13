#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.create_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

        
    def __str__(self,):
        x = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return x

    def save(self):
        self.update_at = datetime.datetime.now()


    def to_dict(self):
        dic_n = self.__dict__.copy()
        if 'create_at' in dic_n:
            dic_n['create_at'] = (dic_n['create_at']).isoformat()
        if 'update_at' in dic_n:
            dic_n['update_at'] = (dic_n['update_at']).isoformat()
        dic_n['__class__'] = self.__class__.__name__
        return dic_n
