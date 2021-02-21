#!/usr/bin/python3
""" Module Unittest for FileStorage """

import pep8
from unittest import TestCase
import models
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """ test class FileStorage """

    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        fchecker = pep8.Checker("models/engine/file_storage", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
