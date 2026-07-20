from __future__ import annotations

"""
AI Engineering Framework
Base Component

Author : TECHAKKENA
"""

import logging
from abc import ABC
from datetime import datetime
from typing import Any

from config.settings import settings

from .component_status import ComponentStatus


class BaseComponent(ABC):
    """
    Base class for all framework components.

    Provides:

    - configuration
    - logging
    - lifecycle
    - metadata
    - health check
    """

    def __init__(
        self,
        name: str,
        version: str = settings.VERSION,
        description: str = "",
    ):

        self.name = name

        self.version = version

        self.description = description

        self.settings = settings

        self.status = ComponentStatus.RUNNING

        self.logger = logging.getLogger(name)

        self.status = ComponentStatus.CREATED

        self.created_at = datetime.now()

        self.metadata: dict[str, Any] = {}

    def initialize(self):
        """
        Initialize component.
        """

        self.status = ComponentStatus.INITIALIZED

        self.logger.info("%s initialized.", self.name)

    def shutdown(self):
        self.status = ComponentStatus.STOPPED
        self.logger.info("%s stopped.", self.name)

    def validate(self) -> bool:
        """
        Validation hook.
        """

        return True

    def health_check(self) -> dict:
        """
        Component health.
        """

        return {
            "component": self.name,
            "status": self.status,
            "healthy": self.status != ComponentStatus.FAILED,
        }

    def get_info(self) -> dict:

        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

    def to_dict(self) -> dict:

        return {
            "name": self.name,
            "version": self.version,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
        }
