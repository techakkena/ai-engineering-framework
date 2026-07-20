from __future__ import annotations

class ErrorMessage:
    UNKNOWN = "An unexpected error occurred."
    INVALID_REQUEST = "Invalid request."
    ACCESS_DENIED = "Access denied."
    RESOURCE_NOT_FOUND = "Requested resource not found."
    INVALID_CONFIGURATION = "Invalid configuration."


class ErrorCategory:
    VALIDATION = "validation"
    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"
    DATABASE = "database"
    NETWORK = "network"
    AI = "ai"
