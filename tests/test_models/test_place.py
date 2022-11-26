#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.place import Place
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class PlaceTest(unittest.TestCase):
    """ Test cases for Place class """

    place = Place()

    def testPlace(self):
        """ Test attributes value of Place insstance """

        self.place.name = "98 street"
        self.place.number_of_rooms = 3

        place_dict = self.place.to_dict()

        self.assertEqual(self.place.name, place_dict['name'])
        self.assertEqual(self.place.number_of_rooms, place_dict['number_of_rooms'])

        self.place.number_of_rooms = 8
        self.assertNotEqual(self.place.number_of_rooms, place_dict['number_of_rooms'])
        place_dict = self.place.to_dict()
        self.assertEqual(self.place.number_of_rooms, place_dict['number_of_rooms'])


if __name__ == '__main__':
    unittest.main()
