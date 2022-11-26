#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.base_model import BaseModel
from models.review import Review
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class ReviewTest(unittest.TestCase):
    """ Test cases for Review class """

    rev = Review()

    def testReview(self):
        """ Test attributes value of Review insstance """

        self.rev.place_id = str(self.rev.id)
        self.rev.foo = {"bar": "foo"}

        rev_dict = self.rev.to_dict()

        self.assertEqual(self.rev.place_id, rev_dict['place_id'])
        self.assertEqual(self.rev.id, rev_dict['place_id'])

        self.rev.foo = "bar"
        self.assertNotEqual(self.rev.foo, rev_dict['foo'])
        rev_dict = self.rev.to_dict()
        self.assertEqual(self.rev.foo, rev_dict['foo'])


if __name__ == '__main__':
    unittest.main()
