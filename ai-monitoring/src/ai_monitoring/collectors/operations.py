"""
Enterprise collector operations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_monitoring.collectors.constants import CUSTOM
from ai_monitoring.collectors.exceptions import (
    CollectorValidationError,
)


@dataclass(slots=True, frozen=True)
class CollectorResult:
    """Represents the result of a collector operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_name(name: str) -> None:
    """Validate a collector name."""
    if not name.strip():
        raise CollectorValidationError(
            "Collector name cannot be empty."
        )


def register_collector(
    name: str,
    *,
    collector_type: str = CUSTOM,
) -> CollectorResult:
    """Register a collector."""
    _validate_name(name)

    return CollectorResult(
        task="register_collector",
        success=True,
        data={
            "name": name,
            "type": collector_type,
        },
    )


def collect_data(
    name: str,
) -> CollectorResult:
    """Collect monitoring data."""
    _validate_name(name)

    return CollectorResult(
        task="collect_data",
        success=True,
        data={
            "name": name,
        },
    )


def get_collector(
    name: str,
) -> CollectorResult:
    """Retrieve a collector."""
    _validate_name(name)

    return CollectorResult(
        task="get_collector",
        success=True,
        data={
            "name": name,
        },
    )


def list_collectors() -> CollectorResult:
    """List registered collectors."""
    return CollectorResult(
        task="list_collectors",
        success=True,
        data={
            "collectors": [],
        },
    )


def remove_collector(
    name: str,
) -> CollectorResult:
    """Remove a collector."""
    _validate_name(name)

    return CollectorResult(
        task="remove_collector",
        success=True,
        data={
            "name": name,
        },
    )