#!/usr/bin/python3
"""
This is 'city' module.
Functions and Classes:
    class City(BaseModel):
"""


from models.base_model import BaseModel


class City(BaseModel):
    """representing a city"""

    state_id = ""
    name = ""
