#!/usr/bin/python3
""" Check FileStorage class """
import unittest
import os
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Check the FileStorage class """

    def setUp(self):
        """ Set up """
        try:
            os.remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        """ Check empty class """
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """ Check all method """
        file_storage = FileStorage()
        obj = file_storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, file_storage._FileStorage__objects)

    def test_save_create(self):
        """ Test save method """
        obj = BaseModel()
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        obj1 = User()
        obj1_key = f'{obj1.__class__.__name__}.{obj1.id}'
        obj2 = City()
        obj2_key = f'{obj2.__class__.__name__}.{obj2.id}'
        obj3 = Amenity()
        obj3_key = f'{obj3.__class__.__name__}.{obj3.id}'
        obj4 = Place()
        obj4_key = f'{obj4.__class__.__name__}.{obj4.id}'
        obj5 = Review()
        obj5_key = f'{obj5.__class__.__name__}.{obj5.id}'
        obj6 = State()
        obj6_key = f'{obj6.__class__.__name__}.{obj6.id}'

        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_new_empty(self):
        """ Check new method with no arguments """
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_classes(self):
        """ Check new method with valid arguments """
        obj = BaseModel(id='123')
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        obj1 = User(id='01')
        obj1_key = f'{obj1.__class__.__name__}.{obj1.id}'
        obj2 = City(id='02')
        obj2_key = f'{obj2.__class__.__name__}.{obj2.id}'
        obj3 = Amenity(id='03')
        obj3_key = f'{obj3.__class__.__name__}.{obj3.id}'
        obj4 = Place(id='04')
        obj4_key = f'{obj4.__class__.__name__}.{obj4.id}'
        obj5 = Review(id='05')
        obj5_key = f'{obj5.__class__.__name__}.{obj5.id}'
        obj6 = State(id='06')
        obj6_key = f'{obj6.__class__.__name__}.{obj6.id}'

        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_reload(self):
        """ Check reload method """
        obj = BaseModel()
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        obj1 = User()
        obj1_key = f'{obj1.__class__.__name__}.{obj1.id}'
        obj2 = City()
        obj2_key = f'{obj2.__class__.__name__}.{obj2.id}'
        obj3 = Amenity()
        obj3_key = f'{obj3.__class__.__name__}.{obj3.id}'
        obj4 = Place()
        obj4_key = f'{obj4.__class__.__name__}.{obj4.id}'
        obj5 = Review()
        obj5_key = f'{obj5.__class__.__name__}.{obj5.id}'
        obj6 = State()
        obj6_key = f'{obj6.__class__.__name__}.{obj6.id}'
        storage.save()

        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)
        self.assertTrue(obj1_key in storage.all().keys())
        self.assertEqual(obj1.id, storage.all()[obj1_key].id)
        self.assertTrue(obj2_key in storage.all().keys())
        self.assertEqual(obj2.id, storage.all()[obj2_key].id)
        self.assertTrue(obj3_key in storage.all().keys())
        self.assertEqual(obj3.id, storage.all()[obj3_key].id)
        self.assertTrue(obj4_key in storage.all().keys())
        self.assertEqual(obj4.id, storage.all()[obj4_key].id)
        self.assertTrue(obj5_key in storage.all().keys())
        self.assertEqual(obj5.id, storage.all()[obj5_key].id)
        self.assertTrue(obj6_key in storage.all().keys())
        self.assertEqual(obj6.id, storage.all()[obj6_key].id)
