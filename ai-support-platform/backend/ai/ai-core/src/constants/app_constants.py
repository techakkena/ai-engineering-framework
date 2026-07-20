from __future__ import annotations

"""
AI Engineering Framework
Application Constants

Author : TECHAKKENA
"""

from enum import Enum


class Application:
    NAME = "AI Engineering Framework"

    VERSION = "0.1.0"

    DESCRIPTION = "Reusable AI Framework"


class Environment:
    DEVELOPMENT = "development"

    TESTING = "testing"

    PRODUCTION = "production"


class HTTPStatus:
    OK = 200

    CREATED = 201

    BAD_REQUEST = 400

    UNAUTHORIZED = 401

    FORBIDDEN = 403

    NOT_FOUND = 404

    INTERNAL_SERVER_ERROR = 500

    SERVICE_UNAVAILABLE = 503


class ContentType:
    JSON = "application/json"

    PDF = "application/pdf"

    CSV = "text/csv"

    TEXT = "text/plain"

    XML = "application/xml"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"

    INFO = "INFO"

    WARNING = "WARNING"

    ERROR = "ERROR"

    CRITICAL = "CRITICAL"
