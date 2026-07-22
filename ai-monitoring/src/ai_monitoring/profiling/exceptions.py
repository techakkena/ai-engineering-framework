"""
Exceptions for the ai_monitoring.profiling package.
"""

from __future__ import annotations


class ProfilingError(Exception):
    """Base exception for profiling errors."""


class ProfileValidationError(ProfilingError):
    """Raised when profile validation fails."""


class ProfileNotFoundError(ProfilingError):
    """Raised when a profile cannot be found."""


class ProfileCollectionError(ProfilingError):
    """Raised when profile collection fails."""


class ProfilingConfigurationError(ProfilingError):
    """Raised when profiling configuration is invalid."""


class ProfilingProviderError(ProfilingError):
    """Raised when an underlying profiling provider fails."""