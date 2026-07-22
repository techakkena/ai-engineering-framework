"""
Enterprise monitoring utility operations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from ai_monitoring.utils.exceptions import (
    IdentifierValidationError,
)


@dataclass(slots=True, frozen=True)
class UtilityResult:
    """Represents the result of a utility operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def validate_identifier(identifier: str) -> None:
    """Validate an identifier."""
    if not identifier.strip():
        raise IdentifierValidationError(
            "Identifier cannot be empty."
        )


def generate_identifier() -> UtilityResult:
    """Generate a unique identifier."""
    return UtilityResult(
        task="generate_identifier",
        success=True,
        data={
            "identifier": str(uuid4()),
        },
    )


def build_metadata(identifier: str) -> UtilityResult:
    """Build metadata."""
    validate_identifier(identifier)

    return UtilityResult(
        task="build_metadata",
        success=True,
        data={
            "id": identifier,
        },
    )


def format_timestamp() -> UtilityResult:
    """Return the current UTC timestamp."""
    return UtilityResult(
        task="format_timestamp",
        success=True,
        data={
            "timestamp": datetime.now(UTC).isoformat(),
        },
    )


def format_duration(
    milliseconds: int,
) -> UtilityResult:
    """Format a duration."""
    return UtilityResult(
        task="format_duration",
        success=True,
        data={
            "duration": f"{milliseconds} ms",
        },
    )