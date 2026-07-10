"""
AI Engineering Framework
Base Controller

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod

from .base_component import BaseComponent


class BaseController(BaseComponent, ABC):
    """
    Base class for all controllers.
    """

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute controller request.
        """
        pass

    def success(
        self,
        data=None,
        message="Success",
    ):
        """
        Standard success response.
        """

        return {
            "success": True,
            "message": message,
            "data": data,
        }

    def error(
        self,
        message="Error",
        details=None,
    ):
        """
        Standard error response.
        """

        return {
            "success": False,
            "message": message,
            "details": details,
        }

    def validate(self):

        return True
