#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.user import User
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class UserTest(unittest.TestCase):
    """ Test cases for User class """

    user_a = User()

    def testUser(self):
        """ Test attributes value of User insstance """

        self.user_a.first_name = "Bob"
        self.user_a.last_name = "Bark"
        self.user_a.email = "bob@mail.fr"
        self.user_a.password = "89@$$"
        self.user_a.new_attr = ["foo", "baar"]

        user_a_dict = self.user_a.to_dict()

        self.assertEqual(self.user_a.first_name, user_a_dict['first_name'])
        self.assertEqual(self.user_a.last_name, user_a_dict['last_name'])
        self.assertEqual(self.user_a.email, user_a_dict['email'])
        self.assertEqual(self.user_a.password, user_a_dict['password'])
        self.assertEqual(self.user_a.new_attr, user_a_dict['new_attr'])

        self.user_a.first_name = "Betty"
        self.assertNotEqual(self.user_a.first_name, user_a_dict['first_name'])
        user_a_dict = self.user_a.to_dict()
        self.assertEqual(self.user_a.first_name, user_a_dict['first_name'])


if __name__ == '__main__':
    unittest.main()
