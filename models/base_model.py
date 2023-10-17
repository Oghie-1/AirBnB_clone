#!/usr/bin/python3
""" Base Model Class """
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """ Base Model class """

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs:
                    self.id = str(uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs:
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String representation """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Save function """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary """
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict
