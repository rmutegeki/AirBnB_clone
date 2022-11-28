#!/usr/bin/python3
"""
Module of Unittests 
"""
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class FileStorageTests(unittest.TestCase):
    """ Suite of Console Tests and the file storage"""

    mod = BaseModel()
    mod_id = mod.id
    mod_created_at = mod.created_at
    
    def testFileStorage(self):
        """ Test attributes value of a FileStorage instance """

        key = self.mod.__class__.__name__ + '.' + str(self.mod_id) 

        self.assertIn(self.mod, storage.all().values())
        self.assertIn(key, storage.all().keys())

        storage.save()
        storage.reload()

        self.assertNotIn(self.mod, storage.all().values())
        new_mod = storage.all()[key]
        self.assertIsNotNone(new_mod)
        self.assertEqual(new_mod.to_dict(), self.mod.to_dict())
        self.assertIn(key, storage.all().keys())
        self.assertEqual(self.mod_created_at, new_mod.created_at)
