"""
AI Engineering Framework
Base Manager

Author : TECHAKKENA
"""

from abc import ABC

from .base_component import BaseComponent


class BaseManager(BaseComponent, ABC):
    """
    Base class for all managers.

    Responsible for managing framework
    components and services.
    """

    def __init__(
        self,
        name: str,
        version: str = "0.1.0",
        description: str = "",
    ):

        super().__init__(name, version, description)

        self._components = {}

    def register(self, component: BaseComponent):
        """
        Register a component.
        """

        self._components[component.name] = component

        self.logger.info("%s registered.", component.name)

    def unregister(self, name: str):
        """
        Remove a component.
        """

        self._components.pop(name, None)

    def get(self, name: str):

        return self._components.get(name)

    def get_all(self):

        return list(self._components.values())

    def count(self):

        return len(self._components)

    def start_all(self):

        for component in self._components.values():

            component.initialize()

    def stop_all(self):

        for component in self._components.values():

            component.shutdown()