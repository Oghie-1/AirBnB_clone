#!/usr/bin/env python3
import json
#from models.base_model import BaseModel
"""This module defines a class FileStorage to manage serialization and deserialization of instances"""


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        Serializes and deserializes instances to/from JSON
    
    """
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """Returns the dictionary __objects """
        return self.__objects
    

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    
    def save(self):
        """Serializes __objects to the JSON file __file_path"""

        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)


    def reload(self):
        """Deserializes the Json file to __objects if it exits"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj.id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass