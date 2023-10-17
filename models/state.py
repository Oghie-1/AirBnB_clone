#!/usr/bin/env python3
"""Class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits BaseModel."""

    def __init__(self, *args, **kwargs):
        """Constructor for State class."""
        super().__init__(*args, **kwargs)
        self.name = ""