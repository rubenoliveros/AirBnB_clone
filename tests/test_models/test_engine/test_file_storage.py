#!/usr/bin/python3
""" Unittest for FileStorage """
from models import storage
from models.base_model import BaseModel
import os
import unittest
import pep8
from datetime import datetime


class Test_FileStorage(unittest.TestCase):
    """ Test BaseModel class """

    @classmethod
    def setUpClass(cls):
        """ Setting instance of method """
        cls.inst = storage

    @classmethod
    def teardown(cls):
        """ Delete instances  """
        del cls.inst
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_all_method(self):
        """ Test all method """
        test_dict = self.inst.all()
        self.assertIsInstance(test_dict, dict)
        self.assertIs(test_dict, self.inst._FileStorage__objects)

    def test_pep8(self):
        """ Pep8 test """
        pep_8 = pep8.StyleGuide(quiet=True)
        answ = pep_8.check_files(['models/engine/file_storage.py'])
        self.assertEqual(answ.total_errors, 0, "Fix Style")

    def test_new(self):
        """ Test new Method """
        dictTest = self.inst.all()
        basM = BaseModel()
        strForm = "{}.{}".format(type(basM).__name__, basM.id)
        self.assertTrue(strForm in dictTest.keys())

    def test_save(self):
        """ Test save method """
        self.assertIsNotNone(storage.save)
        self.inst.save()
        with open("file.json", 'r') as read:
            lines = read.readlines()

        try:
            os.remove("file.json")
        except BaseException:
            pass

        self.inst.save()

        with open("file.json", 'r') as read2:
            lines2 = read2.readlines()

        self.assertEqual(lines, lines2)

    def test_reload(self):
        """ Test reload method """
        self.assertIsNotNone(storage.reload)
        try:
            os.remove("file.json")
        except BaseException:
            pass

        with open("file.json", 'w') as write:
            write.write("{}")
        with open("file.json", 'r') as reader:
            for line in reader:
                self.assertEqual(line, "{}")
        self.assertIs(self.inst.reload(), None)

    def test_all(self):
        """ Test all method """
        dictTest = self.inst.all()
        self.assertIsInstance(dictTest, dict)
        self.assertIs(dictTest, self.inst._FileStorage__objects)

    def test_att(self):
        """ Test Attributes """
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(type(self.inst._FileStorage__file_path) is str)

if __name__ == "__main__":
    unittest.main()
