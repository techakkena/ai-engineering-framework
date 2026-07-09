from __future__ import annotations

from typing import Type

from .base_provider import BaseProvider


class ProviderFactory:
    """
    Factory for registering and creating AI providers.
    """

    _providers: dict[str, Type[BaseProvider]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        provider: Type[BaseProvider],
    ) -> None:
        """
        Register a provider implementation.
        """
        cls._providers[name.lower()] = provider

    @classmethod
    def create(
        cls,
        name: str,
    ) -> BaseProvider:
        """
        Create a provider instance.
        """
        provider = cls._providers.get(name.lower())

        if provider is None:
            raise ValueError(f"Unknown provider: {name}")

        return provider()