from __future__ import annotations

"""
AI Engineering Framework
Logging Constants

Author : TECHAKKENA
"""


class LogLevel:
    """
    Supported logging levels.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LoggerName:
    """
    Standard framework logger names.
    """

    FRAMEWORK = "AI-Framework"
    CORE = "AI-Core"
    AUTH = "AI-Auth"
    CHAT = "AI-Chat"
    AGENT = "AI-Agent"
    RAG = "AI-RAG"
    STORAGE = "AI-Storage"
    DOCUMENT = "AI-Documents"
    EMAIL = "AI-Email"
    DASHBOARD = "AI-Dashboard"


class LogFormat:
    """
    Standard logging formats.
    """

    SIMPLE = "%(levelname)s | %(message)s"

    STANDARD = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    DETAILED = (
        "%(asctime)s | %(levelname)-8s | %(name)s | "
        "%(filename)s:%(lineno)d | %(message)s"
    )


class Rotation:
    """
    Log rotation defaults.
    """

    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    BACKUP_COUNT = 5


class OutputType:
    """
    Logging output destinations.
    """

    CONSOLE = "console"

    FILE = "file"

    BOTH = "both"
