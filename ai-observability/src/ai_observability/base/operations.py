from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from .constants import ObservationStatus


@dataclass(slots=True)
class Observation:
    """Represents an observation."""

    name: str

    status: ObservationStatus = ObservationStatus.CREATED

    attributes: dict[str, Any] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class ObservationContext:
    """Observation execution context."""

    correlation_id: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )


class BaseObserver(ABC):
    """Base observer."""

    @abstractmethod
    def start(
        self,
        observation: Observation,
    ) -> None:
        """Start an observation."""

    @abstractmethod
    def stop(
        self,
        observation: Observation,
    ) -> None:
        """Stop an observation."""
