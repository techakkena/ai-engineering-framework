from __future__ import annotations

from constants.error_constants import ErrorCategory, ErrorMessage


def test_error_messages():
    assert ErrorMessage.UNKNOWN == "An unexpected error occurred."
    assert ErrorMessage.INVALID_REQUEST == "Invalid request."
    assert ErrorMessage.ACCESS_DENIED == "Access denied."
    assert ErrorMessage.RESOURCE_NOT_FOUND == "Requested resource not found."
    assert ErrorMessage.INVALID_CONFIGURATION == "Invalid configuration."


def test_error_categories():
    assert ErrorCategory.VALIDATION == "validation"
    assert ErrorCategory.AUTHENTICATION == "authentication"
    assert ErrorCategory.AUTHORIZATION == "authorization"
    assert ErrorCategory.DATABASE == "database"
    assert ErrorCategory.NETWORK == "network"
    assert ErrorCategory.AI == "ai"
