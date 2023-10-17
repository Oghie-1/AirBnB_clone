from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits BaseModel."""

    def __init__(self, *args, **kwargs):
        """Constructor for User class."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""