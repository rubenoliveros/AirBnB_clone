#!/usr/bin/python3
""" Module Unittest for State """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models import state

State = state.State


class TestBase(TestCase):
    """ test class State """

    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py',
                                        'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(State.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(State.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)
