"""Constants for the ai_testing.assertions module."""

from __future__ import annotations

from typing import Final

DEFAULT_ASSERTION_NAME: Final[str] = "assertion"

STATUS_PASSED: Final[str] = "passed"
STATUS_FAILED: Final[str] = "failed"

SUPPORTED_ASSERTION_STATUSES: Final[frozenset[str]] = frozenset(
    {
        STATUS_PASSED,
        STATUS_FAILED,
    }
)

DEFAULT_STRICT: Final[bool] = True

MIN_ASSERTION_NAME_LENGTH: Final[int] = 1
MAX_ASSERTION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
STATUS_KEY: Final[str] = "status"
MESSAGE_KEY: Final[str] = "message"
EXPECTED_KEY: Final[str] = "expected"
ACTUAL_KEY: Final[str] = "actual"

__all__ = [
    "ACTUAL_KEY",
    "DEFAULT_ASSERTION_NAME",
    "DEFAULT_STRICT",
    "EXPECTED_KEY",
    "MAX_ASSERTION_NAME_LENGTH",
    "MESSAGE_KEY",
    "MIN_ASSERTION_NAME_LENGTH",
    "NAME_KEY",
    "STATUS_FAILED",
    "STATUS_KEY",
    "STATUS_PASSED",
    "SUPPORTED_ASSERTION_STATUSES",
]