"""Constants for the ai_cloud.networking module."""

from __future__ import annotations

from typing import Final

DEFAULT_NETWORK_NAME: Final[str] = "network"
DEFAULT_NETWORK_TYPE: Final[str] = "private"
DEFAULT_ENABLED: Final[bool] = True

PRIVATE_NETWORK: Final[str] = "private"
PUBLIC_NETWORK: Final[str] = "public"
HYBRID_NETWORK: Final[str] = "hybrid"
VPC_NETWORK: Final[str] = "vpc"

SUPPORTED_NETWORK_TYPES: Final[frozenset[str]] = frozenset(
    {
        PRIVATE_NETWORK,
        PUBLIC_NETWORK,
        HYBRID_NETWORK,
        VPC_NETWORK,
    }
)

MIN_NETWORK_NAME_LENGTH: Final[int] = 1
MAX_NETWORK_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
CIDR_KEY: Final[str] = "cidr"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CIDR_KEY",
    "DEFAULT_ENABLED",
    "DEFAULT_NETWORK_NAME",
    "DEFAULT_NETWORK_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "HYBRID_NETWORK",
    "MAX_NETWORK_NAME_LENGTH",
    "MIN_NETWORK_NAME_LENGTH",
    "NAME_KEY",
    "PRIVATE_NETWORK",
    "PUBLIC_NETWORK",
    "SUPPORTED_NETWORK_TYPES",
    "TYPE_KEY",
    "VPC_NETWORK",
]