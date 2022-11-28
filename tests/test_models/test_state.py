#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.state import State
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class StateTest(unittest.TestCase):
    """ Test cases for State class """

    my_state = State()

    def testState(self):
        """ Test attributes value of State insstance """

        self.my_state.name = "California"
        self.my_state.foo = {"bar": "foo"}

        my_state_dict = self.my_state.to_dict()

        self.assertEqual(self.my_state.name, my_state_dict['name'])
        self.assertEqual(self.my_state.foo, my_state_dict['foo'])

        self.my_state.foo = "bar"
        self.assertNotEqual(self.my_state.foo, my_state_dict['foo'])
        my_state_dict = self.my_state.to_dict()
        self.assertEqual(self.my_state.foo, my_state_dict['foo'])


if __name__ == '__main__':
    unittest.main()
