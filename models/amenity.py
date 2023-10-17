#!/usr/bin/env python3
"""Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits BaseModel."""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity class."""
        super().__init__(*args, **kwargs)
        self.name = ""