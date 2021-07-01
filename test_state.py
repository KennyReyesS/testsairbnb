#!/usr/bin/python3
"""
    This module contains test cases for State
"""
import unittest
from models.state import State
from models.base_model import BaseModel
import pep8
from datetime import datetime


class TestState(unittest.TestCase):
    """" Test cases class of State """

    def test_pep8_state(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/state.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_stateattr(self):
        """ test if state has attribute """
        new_state = State()
        self.assertTrue(hasattr(new_state, "id"))
        self.assertTrue(hasattr(new_state, "created_at"))
        self.assertTrue(hasattr(new_state, "updated_at"))
        self.assertTrue(hasattr(new_state, "name"))

    def test_statetype(self):
        """ test type of attributes """
        new_state = State()
        self.assertIs(type(new_state.id), str)
        self.assertIs(type(new_state.created_at), datetime)
        self.assertIs(type(new_state.updated_at), datetime)
        self.assertIs(type(new_state.name), str)

    def test_inherit_State(self):
        """ test if inherit of BaseModel """
        new_inherit = State()
        self.assertIsInstance(new_inherit, BaseModel)

    def test_stateisempty(self):
        """ test if attribute is empty string """
        new_state = State()
        self.assertEqual(new_state.name, "")
