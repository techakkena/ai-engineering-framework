"""
Exceptions for the ai_datasets.splitters package.

This module defines the exception hierarchy for provider-independent
dataset splitting operations.
"""

from __future__ import annotations


class DatasetSplitterError(Exception):
    """Base exception for all dataset splitter errors."""


class SplitValidationError(DatasetSplitterError):
    """Raised when split input validation fails."""


class UnsupportedSplitStrategyError(SplitValidationError):
    """Raised when an unsupported split strategy is requested."""


class DatasetSplitError(DatasetSplitterError):
    """Base exception for dataset splitting failures."""


class TrainTestSplitError(DatasetSplitError):
    """Raised when a train/test split fails."""


class StratifiedSplitError(DatasetSplitError):
    """Raised when a stratified split fails."""


class KFoldSplitError(DatasetSplitError):
    """Raised when a k-fold split fails."""


class TimeSeriesSplitError(DatasetSplitError):
    """Raised when a time-series split fails."""


class SplitConfigurationError(DatasetSplitterError):
    """Raised when the split configuration is invalid."""


class SplitProviderError(DatasetSplitterError):
    """Raised when an underlying split provider returns an error."""