"""
Exceptions for the ai_monitoring.analyzers package.
"""

from __future__ import annotations


class AnalyzerError(Exception):
    """Base exception for analyzer errors."""


class AnalyzerValidationError(AnalyzerError):
    """Raised when analyzer validation fails."""


class AnalysisNotFoundError(AnalyzerError):
    """Raised when an analysis cannot be found."""


class AnalysisExecutionError(AnalyzerError):
    """Raised when analysis execution fails."""


class AnalyzerConfigurationError(AnalyzerError):
    """Raised when analyzer configuration is invalid."""


class AnalyzerProviderError(AnalyzerError):
    """Raised when an analyzer provider fails."""