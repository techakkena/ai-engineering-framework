from __future__ import annotations

"""Vector module."""

from .constants import (
    DEFAULT_VECTOR_DIMENSIONS,
    DEFAULT_VECTOR_NAMESPACE,
    VectorMetric,
    VectorState,
    VectorType,
)
from .exceptions import (
    VectorError,
    VectorNotFoundError,
    VectorStateError,
    VectorValidationError,
)
from .operations import (
    is_valid_vector_metric,
    is_valid_vector_state,
    is_valid_vector_type,
    validate_vector_metric,
    validate_vector_state,
    validate_vector_type,
)

__all__ = [
    "VectorType",
    "VectorMetric",
    "VectorState",
    "DEFAULT_VECTOR_DIMENSIONS",
    "DEFAULT_VECTOR_NAMESPACE",
    "VectorError",
    "VectorNotFoundError",
    "VectorValidationError",
    "VectorStateError",
    "validate_vector_type",
    "validate_vector_metric",
    "validate_vector_state",
    "is_valid_vector_type",
    "is_valid_vector_metric",
    "is_valid_vector_state",
]
