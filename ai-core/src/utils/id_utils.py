"""
AI Engineering Framework
ID Utilities

Author : TECHAKKENA
"""

from uuid import uuid4
import secrets


def generate_uuid() -> str:
    """
    Generate a UUID4 string.
    """
    return str(uuid4())


def generate_token(length: int = 32) -> str:
    """
    Generate a secure random token.
    """
    return secrets.token_hex(length)


def generate_short_id(length: int = 8) -> str:
    """
    Generate a short random identifier.
    """
    return secrets.token_hex(length // 2)