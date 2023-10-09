#!/usr/bin/env python3
"""This script contains the class BaseModel that defines common attributes/method for other classes"""
import uuid
from datetime import datetime



class BaseModel:
    """Base class for all models."""

    def __init__(self):
        """Initialize a new instance of Basemodel
        
        Attributes:
            id (str): A unique identifer generated as a string using uuid4.
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The timestamp of the last update.
        
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """Return a string representation of the BaseModel.
        
        Returns:
            str: A string in the format "[<class name>] (<self.id> <self.__dict__>)"        
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the 'update_at' attribute with the current datetime."""

        self.updated_at = datetime.now()

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

models =  my_model()

models.name = "sample"
models.id = 22


print(models)