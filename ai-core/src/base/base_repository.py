"""
AI Engineering Framework
Base Repository

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod

from .base_component import BaseComponent


class BaseRepository(BaseComponent, ABC):
    """
    Base class for all repositories.
    """

    @abstractmethod
    def create(self, data):
        """Create a new record."""
        pass

    @abstractmethod
    def get_by_id(self, record_id):
        """Get a record by ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Return all records."""
        pass

    @abstractmethod
    def update(self, record_id, data):
        """Update an existing record."""
        pass

    @abstractmethod
    def delete(self, record_id):
        """Delete a record."""
        pass

    @abstractmethod
    def exists(self, record_id):
        """Check whether a record exists."""
        pass

    @abstractmethod
    def count(self):
        """Return the total number of records."""
        pass