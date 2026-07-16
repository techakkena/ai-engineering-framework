"""
Exceptions for the ai_datasets.validators package.
"""

from __future__ import annotations


class DatasetValidatorError(Exception):
    """Base exception for dataset validator errors."""


class DatasetValidationError(DatasetValidatorError):
    """Raised when dataset validation fails."""


class SchemaValidationError(DatasetValidationError):
    """Raised when schema validation fails."""


class IntegrityValidationError(DatasetValidationError):
    """Raised when integrity validation fails."""


class ConstraintValidationError(DatasetValidationError):
    """Raised when constraint validation fails."""


class MetadataValidationError(DatasetValidationError):
    """Raised when metadata validation fails."""


class ValidatorConfigurationError(DatasetValidatorError):
    """Raised when validator configuration is invalid."""


class UnsupportedValidationTypeError(DatasetValidatorError):
    """Raised when an unsupported validation type is requested."""


class ValidationProcessingError(DatasetValidatorError):
    """Raised when validation processing fails."""


class ValidatorProviderError(DatasetValidatorError):
    """Raised when a validator provider fails."""