#!/usr/bin/python3
"""
test_user.py module
"""
import unittest
from models.base_model import BaseModel
from models.user import User
import pep8
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Tests for User Class """
    def test_pep8_user(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_hasattr_user(self):
        """ test if user has attribute """
        new_user = User()
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

    def test_type_user(self):
        """ test type of attribute """
        new_user = User()
        self.assertIs(type(new_user.id), str)
        self.assertIs(type(new_user.created_at), datetime)
        self.assertIs(type(new_user.updated_at), datetime)
        self.assertIs(type(new_user.email), str)
        self.assertIs(type(new_user.password), str)
        self.assertIs(type(new_user.first_name), str)
        self.assertIs(type(new_user.last_name), str)

    def test_inherit_User(self):
        """ test inherit of BaseModel """
        new_inherit = User()
        self.assertIsInstance(new_inherit, BaseModel)
