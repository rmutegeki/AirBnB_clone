#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.city import City
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class CityTest(unittest.TestCase):
    """ Test cases for City class """

    my_city = City()

    def testCity(self):
        """ Test attributes value of City insstance """

        self.my_city.state_id = str(self.my_city.id)
        self.my_city.name = "Marrakech"
        self.my_city.foo = "baar"

        city_dict = self.my_city.to_dict()

        self.assertEqual(self.my_city.state_id, city_dict['state_id'])
        self.assertEqual(self.my_city.state_id, city_dict['id'])
        self.assertEqual(self.my_city.name, city_dict['name'])
        self.assertEqual(self.my_city.foo, city_dict['foo'])

        self.my_city.name = "Betty"
        self.assertNotEqual(self.my_city.name, city_dict['name'])
        city_dict = self.my_city.to_dict()
        self.assertEqual(self.my_city.name, city_dict['name'])


if __name__ == '__main__':
    unittest.main()
