"""Exceptions for the ai_optimization.routing module."""

from __future__ import annotations


class RouteError(Exception):
    """Base exception for routing operations."""


class RouteValidationError(RouteError):
    """Raised when route validation fails."""


class RouteRegistrationError(RouteError):
    """Raised when route registration fails."""


class RouteNotFoundError(RouteRegistrationError):
    """Raised when a route definition cannot be found."""


class DuplicateRouteError(RouteRegistrationError):
    """Raised when attempting to register a duplicate route."""


class UnsupportedRoutingStrategyError(
    RouteValidationError,
):
    """Raised when an unsupported routing strategy is specified."""


__all__ = [
    "DuplicateRouteError",
    "RouteError",
    "RouteNotFoundError",
    "RouteRegistrationError",
    "RouteValidationError",
    "UnsupportedRoutingStrategyError",
]