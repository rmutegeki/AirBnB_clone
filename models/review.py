#!/usr/bin/python3
"""
This is 'review' module.
Functions and Classes:
    class User(BaseModel):
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """representing a review"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    place_id = ""
    user_id = ""
    text = ""
