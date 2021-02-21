#!/usr/bin/python3
""" Module Unittest for Amenity """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models import amenity

Amenity = amenity.Amenity


class TestAmenity(TestCase):
    """ test class Amenity """

    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py',
                                        'tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)
