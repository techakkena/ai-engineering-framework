from __future__ import annotations

"""JWT utilities."""

from app.config.security import (
    create_access_token,
    decode_access_token,
)

__all__ = [
    "create_access_token",
    "decode_access_token",
]