#!/usr/bin/python3
"""
This is 'amenity' module.
Functions and Classes:
    class Amenity(BaseModel):
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """reprensing an amenity"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
