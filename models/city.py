#!/usr/bin/python3
"""
This is 'city' module.
Functions and Classes:
    class City(BaseModel):
"""


from models.base_model import BaseModel


class City(BaseModel):
    """representing a city"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""
