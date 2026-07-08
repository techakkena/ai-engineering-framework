"""
AI Engineering Framework
Base Agent

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod

from .base_component import BaseComponent
from constants.ai_constants import AIProvider, ChatModels
from config.settings import settings

class BaseAgent(BaseComponent, ABC):

    def __init__(
        self,
        name: str,
        provider: str,
        model: str,
        description: str = "",
    ):

        # Call BaseComponent ONLY with generic arguments
        super().__init__(
            name=name,
            version=settings.VERSION,
            description=description,
        )

        # Agent-specific attributes
        self.provider = provider
        self.model = model
        self.temperature = settings.TEMPERATURE
        self.max_tokens = settings.MAX_TOKENS

    @abstractmethod
    def chat(self, prompt: str):
        """
        Generate a chat response.
        """
        pass

    @abstractmethod
    def generate(self, *args, **kwargs):
        """
        Generate AI output.
        """
        pass

    def get_agent_info(self):

        return {
            "name": self.name,
            "provider": self.provider,
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }