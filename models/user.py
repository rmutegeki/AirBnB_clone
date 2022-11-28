#!/usr/bin/python3
"""
This is 'user' module.
Functions and Classes:
    class User(BaseModel):
"""


from models.base_model import BaseModel


class User(BaseModel):
    """representing a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
