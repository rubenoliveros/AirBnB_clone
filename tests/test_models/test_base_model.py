#!/usr/bin/python3
from models.base_model import BaseModel
import os
import unittest
import pep8
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel class """

    @classmethod
    def setUpClass(cls):
        """ Setting instance of method """
        cls.inst = BaseModel()

    @classmethod
    def teardown(cls):
        """ Delete instances  """
        del cls.inst
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        """ Pep8 test """
        pep_8 = pep8.StyleGuide(quiet=True)
        answ = pep_8.check_files(['models/base_model.py'])
        self.assertEqual(answ.total_errors, 0, "Fix Style")

    def test_instance(self):
        """ Verify instance """
        self.assertIsInstance(self.inst, BaseModel)

    def test_has_attribute(self):
        """ Test attributes """
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "__init__"))

    def test_docstring(self):
        """ Test docstring """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_dict_doc(self):
        """ test docstring of each method """
        for doc in dir(BaseModel):
            self.assertIsNotNone(doc.__doc__)

    def test_type_datetime(self):
        """ Datetime class verificationyo """
        self.assertEqual(datetime, type(self.inst.created_at))
        self.assertEqual(datetime, type(self.inst.updated_at))

    def test_save(self):
        """ Test difference between created_at and updated_at """
        self.inst.save()
        self.assertNotEqual(self.inst.created_at, self.inst.updated_at)
        self.old = self.inst.updated_at
        self.inst.save()
        self.new = self.inst.updated_at
        self.assertIsNot(self.old, self.new)

    def test_to_dict(self):
        """ Verify the dictionary convert """
        dict_test = self.inst.to_dict()
        self.assertEqual(dict, type(dict_test))
        self.assertTrue('to_dict' in dir(self.inst))
        self.assertIsInstance(dict_test["created_at"], str)
        self.assertIsInstance(dict_test["updated_at"], str)

    def test_create(self):
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def dict_test_att(self):
        """ Verify elements of dictionary """
        test_dict = self.inst.to_dict()
        self.assertEqual(test_dict.__class_.__name__, 'BaseModel')
        self.assertIsInstance(test_dict['updated_at'], str)
        self.assertIsInstance(test_dict['created_at'], str)
        self.assertIsInstance(test_dict['_id'], str)

    def test_type_id(self):
        """ Test the type of the id """
        self.assertEqual(str, type(self.inst.id))

    def test_attr(self):
        self.inst.name = "Nildiert"
        self.inst.number = 26
        self.inst.number2 = 2.3
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual(int, type(self.inst.number))
        self.assertEqual(float, type(self.inst.number2))

if __name__ == "__main__":
    unittest.main()
