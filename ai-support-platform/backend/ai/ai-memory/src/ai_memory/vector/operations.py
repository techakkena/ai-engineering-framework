from __future__ import annotations

"""Operations for the ai_memory.vector module."""

from __future__ import annotations

from .constants import VectorMetric
from .constants import VectorState
from .constants import VectorType
from .exceptions import VectorValidationError


def validate_vector_type(vector_type: VectorType | str) -> VectorType:
    """Validate a vector type."""
    try:
        return VectorType(vector_type)
    except ValueError as exc:
        raise VectorValidationError(
            f"Invalid vector type: {vector_type!r}."
        ) from exc


def validate_vector_metric(metric: VectorMetric | str) -> VectorMetric:
    """Validate a vector metric."""
    try:
        return VectorMetric(metric)
    except ValueError as exc:
        raise VectorValidationError(
            f"Invalid vector metric: {metric!r}."
        ) from exc


def validate_vector_state(state: VectorState | str) -> VectorState:
    """Validate a vector state."""
    try:
        return VectorState(state)
    except ValueError as exc:
        raise VectorValidationError(
            f"Invalid vector state: {state!r}."
        ) from exc


def is_valid_vector_type(vector_type: str) -> bool:
    """Return True if the vector type is valid."""
    try:
        VectorType(vector_type)
        return True
    except ValueError:
        return False


def is_valid_vector_metric(metric: str) -> bool:
    """Return True if the vector metric is valid."""
    try:
        VectorMetric(metric)
        return True
    except ValueError:
        return False


def is_valid_vector_state(state: str) -> bool:
    """Return True if the vector state is valid."""
    try:
        VectorState(state)
        return True
    except ValueError:
        return False
