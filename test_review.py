#!/usr/bin/python3
"""
Test module for models/review.py
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
import pep8
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Test for Review class """

    def test_pep8_review(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_attr_rev(self):
        """ checks review attribute """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_type_rev(self):
        """ test type of attribute """
        review = Review()
        self.assertTrue(type(review.id), str)
        self.assertTrue(type(review.created_at), datetime)
        self.assertTrue(type(review.updated_at), datetime)
        self.assertTrue(type(review.place_id), int)
        self.assertTrue(type(review.user_id), int)
        self.assertTrue(type(review.text), int)

    def test_inherit_Review(self):
        """ Test inherit """
        new_inherit = Review()
        self.assertIsInstance(new_inherit, BaseModel)

    def test_isempty_rev(self):
        """ test if attribute is empty """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
