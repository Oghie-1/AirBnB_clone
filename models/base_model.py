#!/usr/bin/env python3
"""This script contains the class BaseModel that defines common attributes/method for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The BaseModel  class from which all other classes  inherit."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of Basemodel
        Args: 
            *args: Unused
            **kwargs: Dictionary of artribute names and values / key-value pairs of attributes
        
        Attributes:
            id (str): A unique identifer generated as a string using uuid4.
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The timestamp of the last update.
        
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, tform))
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)



    def __str__(self):
        """Return a string representation of the BaseModel.
        
        Returns:
            str: A string in the format "[<class name>] (<self.id> <self.__dict__>)"        
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the public instance attribute 'update_at' attribute with the current datetime."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

#sample

class my_model(BaseModel):
    pass


def test_base(my_model):
    sample_model = my_model()
    sample_model.name = "my first model"
    sample_model.id = 98
    print("my first sample: ", sample_model)
    print("\n####\n")
    print(sample_model.id)
    print()
    print(type(sample_model.created_at))
    print("---")
    print()
    sample_model.save()
    print()
    print("saved model: ", sample_model)
    sample_model_json = sample_model.to_dict()
    print("Json sample: ", sample_model_json)
    print("##")
    for key in sample_model_json.keys():
        print("\t{}: ({}) - {}".format(key,
                                       type(sample_model_json[key]), sample_model_json[key]))


test_base(my_model)
