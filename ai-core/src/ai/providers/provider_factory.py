"""
AI Engineering Framework
Provider Factory

Author : TECHAKKENA
"""

from ai.providers.openai_provider import OpenAIProvider
from ai.providers.types import ProviderConfig


class ProviderFactory:
    """
    Factory for creating AI providers.
    """

    @staticmethod
    def create(
        provider: str,
        config: ProviderConfig,
    ):
        """
        Create a provider instance.
        """

        provider = provider.lower()

        if provider == "openai":
            return OpenAIProvider(config)

        raise ValueError(f"Unsupported provider: {provider}")
