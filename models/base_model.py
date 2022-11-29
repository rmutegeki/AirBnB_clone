#!/usr/bin/python3
"""
This is the  'base_model' module.
Functions and Classes:
    class BaseModel
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base model that defines all common
    attributes/methods for other classes
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """initializes all the attributes of this class
        """
        if kwargs:
            d = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(kwargs[k], d)
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """returns a string of info about the model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """returns a string representation
        """
        return self.__str__()

    def save(self):
        """save to file"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a new dictionary representation of an instance
        with datetimes converted to strings
        """
        my_dict = {}

        for k, values in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                my_dict[k] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    my_dict[k] = values
        my_dict['__class__'] = self.__class__.__name__

        return my_dict