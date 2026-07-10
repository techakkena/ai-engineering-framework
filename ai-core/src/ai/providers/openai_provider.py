"""
AI Engineering Framework
OpenAI Provider

Author : TECHAKKENA
"""

from openai import OpenAI

from ai.providers.base_provider import BaseProvider
from ai.providers.types import (
    ProviderConfig,
    ProviderMessage,
    ProviderResponse,
)


class OpenAIProvider(BaseProvider):
    """
    OpenAI provider implementation.
    """

    def __init__(
        self,
        config: ProviderConfig,
    ):
        super().__init__(config)

        self.client: OpenAI | None = None

    def connect(
        self,
    ) -> None:
        """
        Initialize OpenAI client.
        """

        self.client = OpenAI(
            api_key=self.config.api_key,
        )

    def chat(
        self,
        messages: list[ProviderMessage],
    ) -> ProviderResponse:
        """
        Generate chat completion.
        """

        raise NotImplementedError("Chat not implemented yet.")

    def embeddings(
        self,
        text: str,
    ):
        """
        Generate embeddings.
        """

        raise NotImplementedError("Embeddings not implemented yet.")

    def image(
        self,
        prompt: str,
    ):
        """
        Generate image.
        """

        raise NotImplementedError("Image generation not implemented yet.")

    def speech(
        self,
        text: str,
    ):
        """
        Generate speech.
        """

        raise NotImplementedError("Speech generation not implemented yet.")

    def close(
        self,
    ) -> None:
        """
        Release provider resources.
        """

        self.client = None
