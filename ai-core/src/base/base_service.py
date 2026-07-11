"""
AI Engineering Framework
Base Service

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod

from .base_component import BaseComponent
from .component_status import ComponentStatus


class BaseService(BaseComponent, ABC):
    """
    Base class for all framework services.
    """

    def start(self):
        """
        Start the service.
        """

        self.status = ComponentStatus.RUNNING

        self.logger.info("%s started.", self.name)

    def stop(self):
        """
        Stop the service.
        """

        self.status = ComponentStatus.STOPPED

        self.logger.info("%s stopped.", self.name)

    def restart(self):
        """
        Restart the service.
        """

        self.stop()

        self.start()

    def is_running(self) -> bool:

        return self.status == ComponentStatus.RUNNING

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute service logic.
        """
        pass
