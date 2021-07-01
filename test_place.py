#!/usr/bin/python3
"""Defines unittests for place.py"""
from models.base_model import BaseModel
from models.place import Place
import unittest
import pep8
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests for Place Class"""

    def test_pep8_place(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/place.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_is_subclass_place(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_type_place(self):
        """Test type of id, created_at and updated_at"""
        place = Place()
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)

    def test_city_id(self):
        """Test if Place has attr city_id and it's empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """Test if Place has attr user_id and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(place.user_id, "")

    def test_name(self):
        """Test if Place has attr name and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(type(place.name), str)
        self.assertEqual(place.name, "")

    def test_description(self):
        """Test if Place has attr description and it's an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(type(place.description), str)
        self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """Test if Place has attr number_rooms and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test if Place has attr number_bathrooms and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest(self):
        """Test if Place has attr max_guest and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        """Test if Place has attr price_by_night and it's an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        """Test if Place has attr latitude and it's an float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        """Test if Place has attr longitude and it's an float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        """Test if Place has attr amenity_ids and it's an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(place.amenity_ids, [])
