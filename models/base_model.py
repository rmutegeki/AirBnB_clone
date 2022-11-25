#!/usr/bin/python3
"""
This is 'base_model' module.
Functions and Classes:
    class BaseModel
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base model that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if (k == 'created_at') or (k == 'updated_at'):
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """save to file"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary representation of an instance"""

        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        return my_dict

    def __str__(self):
        """string representation of an instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
