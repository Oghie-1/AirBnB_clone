#!/usr/bin/env python3
from models.base_model import BaseModel
"""Class City """


class City(BaseModel):
    """City class that inherits BaseModel."""

    def __init__(self, *args, **kwargs):
        """Constructor for City class."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""