#!/usr/bin/python3
"""
File containing the class BaseModel
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """a class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Function for initializing the base model"""
        if kwargs is None or len(kwargs) < 1:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

    def __str__(self,):
        """String representation of the BaseModel class"""
        x = "[{}] ({}) {}".format(self.__class__.__name__,
                                  self.id, self.__dict__)
        return x

    def save(self):
        """updates the class with the current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key-value pairs"""
        dic_n = self.__dict__.copy()
        dic_n['created_at'] = self.created_at.isoformat()
        dic_n['updated_at'] = self.updated_at.isoformat()
        dic_n['__class__'] = self.__class__.__name__
        return dic_n
