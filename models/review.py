#!/usr/bin/env python3
"""Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits BaseModel."""

    def __init__(self, *args, **kwargs):
        """Constructor for Review class."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""