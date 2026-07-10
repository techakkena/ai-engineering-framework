"""
AI Engineering Framework
Environment Manager

Author: TECHAKKENA
Module: ai-core
"""

import sys
from pathlib import Path

from .logging_config import LoggingManager
from .settings import settings


class EnvironmentManager:
    """
    Handles AI Engineering Framework startup tasks.
    """

    def __init__(self):
        """
        Initialize environment manager.
        """
        self.base_dir = Path.cwd()

    def load_environment(self):
        """
        Verify that framework settings have been loaded.
        """

        print("Environment configuration loaded.")

    def check_python_version(self):
        """
        Verify supported Python version.
        """

        minimum_version = (3, 11)

        if sys.version_info < minimum_version:
            raise RuntimeError(
                f"Python {minimum_version[0]}.{minimum_version[1]} or higher is required."
            )

        print(f"Python Version : {sys.version.split()[0]}")

    def create_directories(self):
        """
        Create required framework directories.
        """

        directories = [
            settings.STORAGE_ROOT,
            settings.UPLOAD_FOLDER,
            settings.TEMP_FOLDER,
            settings.VECTOR_DB_PATH,
            settings.CACHE_FOLDER,
            settings.BACKUP_FOLDER,
            Path(settings.LOG_FILE).parent,
        ]

        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)

        print("Folders verified.")

    def validate(self):
        """
        Validate framework configuration.
        """

        required_settings = {
            "SECRET_KEY": settings.SECRET_KEY,
        }

        missing = []

        for key, value in required_settings.items():
            if value is None or value == "":
                missing.append(key)

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

        print("Configuration validated.")

    def show_framework_info(self):
        """
        Display framework startup information.
        """

        print()
        print("=" * 60)
        print(settings.FRAMEWORK_NAME)
        print("=" * 60)

        print(f"Application : {settings.APP_NAME}")
        print(f"Version     : {settings.VERSION}")
        print(f"Debug Mode  : {settings.DEBUG}")
        print(f"API Host    : {settings.API_HOST}")
        print(f"API Port    : {settings.API_PORT}")
        print(f"AI Model    : {settings.OPENAI_MODEL}")
        print(f"Database    : {settings.DATABASE_URL}")

        print("=" * 60)

    def startup(self):
        """
        Initialize AI Engineering Framework.
        """
        LoggingManager.configure()

        self.load_environment()

        self.check_python_version()

        self.create_directories()

        self.validate()

        self.show_framework_info()

        print()
        print("AI Core initialized successfully.")


environment = EnvironmentManager()
