"""
AI Engineering Framework
Logging Configuration

Author: TECHAKKENA
Module: ai-core
"""

import logging
from pathlib import Path

from .settings import settings


class LoggingManager:
    """
    Configure and manage framework logging.
    """

    _configured = False

    @classmethod
    def configure(cls) -> None:
        """
        Configure the logging system once.
        """

        if cls._configured:
            return

        log_file = Path(settings.LOG_FILE)
        log_file.parent.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=getattr(logging, settings.LOG_LEVEL.upper()),
            format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler(log_file, encoding="utf-8"),
                logging.StreamHandler(),
            ],
            force=True,
        )

        cls._configured = True

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Return a configured logger.
        """

        return logging.getLogger(name)

    @staticmethod
    def shutdown() -> None:
        """
        Shutdown logging gracefully.
        """

        logging.shutdown()


# Configure logging when imported
