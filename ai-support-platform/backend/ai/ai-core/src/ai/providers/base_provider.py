from __future__ import annotations

"""
AI Engineering Framework
Base Provider

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod

from ai.providers.types import (
    ProviderConfig,
    ProviderMessage,
    ProviderResponse,
)


class BaseProvider(ABC):
    """
    Base class for all AI providers.
    """

    def __init__(
        self,
        config: ProviderConfig,
    ):
        self.config = config

    @abstractmethod
    def connect(
        self,
    ) -> None:
        """
        Initialize provider.
        """

    @abstractmethod
    def chat(
        self,
        messages: list[ProviderMessage],
    ) -> ProviderResponse:
        """
        Generate chat completion.
        """

    @abstractmethod
    def embeddings(
        self,
        text: str,
    ):
        """
        Generate embeddings.
        """

    @abstractmethod
    def image(
        self,
        prompt: str,
    ):
        """
        Generate image.
        """

    @abstractmethod
    def speech(
        self,
        text: str,
    ):
        """
        Generate speech.
        """

    @abstractmethod
    def close(
        self,
    ) -> None:
        """
        Close provider resources.
        """
