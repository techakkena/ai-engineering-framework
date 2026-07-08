"""
AI Engineering Framework
Base Model

Author : TECHAKKENA
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Base class for framework models.
    """

    def __init__(self):

        self.id = str(uuid4())

        self.created_at = datetime.now()

        self.updated_at = datetime.now()

        self.is_active = True

        self.metadata = {}

    def update(self, **kwargs):
        """
        Update model fields.
        """

        for key, value in kwargs.items():

            if hasattr(self, key):

                setattr(self, key, value)

        self.updated_at = datetime.now()

    def deactivate(self):
        """
        Deactivate model.
        """

        self.is_active = False

        self.updated_at = datetime.now()

    def activate(self):
        """
        Activate model.
        """

        self.is_active = True

        self.updated_at = datetime.now()

    def to_dict(self):

        result = {}

        for key, value in self.__dict__.items():

            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value

        return result