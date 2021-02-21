#!/usr/bin/python3
""" Module Unittest for BaseModel """

import pep8
from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """ test class BaseModel """

    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        fchecker = pep8.Checker("models/base_model", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
