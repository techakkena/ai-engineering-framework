"""Constants for prompt variables."""

VARIABLE_PATTERN = r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}"

MAX_VARIABLE_NAME_LENGTH = 64

RESERVED_VARIABLES = {
    "system",
    "assistant",
    "user",
}

__all__ = [
    "VARIABLE_PATTERN",
    "MAX_VARIABLE_NAME_LENGTH",
    "RESERVED_VARIABLES",
]
