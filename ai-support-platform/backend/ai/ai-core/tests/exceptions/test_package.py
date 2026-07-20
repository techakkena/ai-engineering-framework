from __future__ import annotations

from exceptions import (
    AIException,
    DatabaseException,
    ErrorCode,
    ValidationException,
)

print("Exceptions package imported successfully.")

print(ErrorCode.VALIDATION_ERROR)
print(ValidationException)
print(DatabaseException)
print(AIException)
