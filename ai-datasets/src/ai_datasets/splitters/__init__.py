"""
ai_datasets.splitters

Enterprise dataset splitting module for the AI Engineering Framework.

This package provides provider-independent dataset splitting strategies
for machine learning workflows including train/validation/test splits,
k-fold cross validation, stratified splitting, and time-series splitting.

Modules
-------
constants
    Splitter-specific constants.

exceptions
    Splitter-specific exception hierarchy.

operations
    High-level dataset splitting operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.splitters.operations import (
    k_fold_split,
    split_dataset,
    stratified_split,
    train_test_split,
    time_series_split,
)

__all__ = [
    "split_dataset",
    "train_test_split",
    "stratified_split",
    "k_fold_split",
    "time_series_split",
]