"""Constants for the ai_cloud.providers module."""

from __future__ import annotations

from typing import Final

# Default provider configuration.
DEFAULT_PROVIDER_NAME: Final[str] = "provider"
DEFAULT_PROVIDER_TYPE: Final[str] = "aws"
DEFAULT_ENABLED: Final[bool] = True

# Supported cloud providers.
AWS_PROVIDER: Final[str] = "aws"
AZURE_PROVIDER: Final[str] = "azure"
GCP_PROVIDER: Final[str] = "gcp"
OCI_PROVIDER: Final[str] = "oci"

SUPPORTED_PROVIDER_TYPES: Final[frozenset[str]] = frozenset(
    {
        AWS_PROVIDER,
        AZURE_PROVIDER,
        GCP_PROVIDER,
        OCI_PROVIDER,
    }
)

# Validation.
MIN_PROVIDER_NAME_LENGTH: Final[int] = 1
MAX_PROVIDER_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
REGION_KEY: Final[str] = "region"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "AWS_PROVIDER",
    "AZURE_PROVIDER",
    "DEFAULT_ENABLED",
    "DEFAULT_PROVIDER_NAME",
    "DEFAULT_PROVIDER_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "GCP_PROVIDER",
    "MAX_PROVIDER_NAME_LENGTH",
    "MIN_PROVIDER_NAME_LENGTH",
    "NAME_KEY",
    "OCI_PROVIDER",
    "REGION_KEY",
    "SUPPORTED_PROVIDER_TYPES",
    "TYPE_KEY",
]