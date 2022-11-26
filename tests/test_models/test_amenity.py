#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class AmenityTest(unittest.TestCase):
    """ Test cases for Amenity class """

    am = Amenity()

    def testAmenity(self):
        """ Test attributes value of Amenity insstance """

        self.am.name = "unknown"
        self.am.foo = {"bar": "foo"}

        am_dict = self.am.to_dict()

        self.assertEqual(self.am.name, am_dict['name'])
        self.assertEqual(self.am.foo, am_dict['foo'])

        self.am.foo = "bar"
        self.assertNotEqual(self.am.foo, am_dict['foo'])
        am_dict = self.am.to_dict()
        self.assertEqual(self.am.foo, am_dict['foo'])


if __name__ == '__main__':
    unittest.main()
