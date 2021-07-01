#!/usr/bin/python3
"""
    This module contains test cases for City
"""
import unittest
from models.base_model import BaseModel
from models.city import City
import pep8
from datetime import datetime


class TestCity(unittest.TestCase):
    """" Test cases class of City """

    def test_pep8_city(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/city.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_attr_city(self):
        """ Test if City has attribute """
        new_city = City()
        self.assertTrue(hasattr(new_city, "id"))
        self.assertTrue(hasattr(new_city, "created_at"))
        self.assertTrue(hasattr(new_city, "updated_at"))
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertTrue(hasattr(new_city, "name"))

    def test_type_city(self):
        """ Test if attribute is string """
        new_city = City()
        self.assertIs(type(new_city.id), str)
        self.assertIs(type(new_city.created_at), datetime)
        self.assertIs(type(new_city.updated_at), datetime)
        self.assertIs(type(new_city.state_id), str)
        self.assertIs(type(new_city.name), str)

    def test_inherit_City(self):
        """ test inherit """
        new_inherit = City()
        self.assertNotIsInstance(type(new_inherit), BaseModel)

    def test_cityisempty(self):
        """ Test if attribute is empty string """
        new_city = City()
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")
