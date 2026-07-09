from enum import Enum


class ChatModels(str, Enum):
    """
    Supported OpenAI chat models.

    Using str + Enum allows enum members to behave like strings
    while still providing type safety and autocomplete.
    """

    GPT5 = "gpt-5"
    GPT5_MINI = "gpt-5-mini"
    GPT5_NANO = "gpt-5-nano"

class EmbeddingModels(str, Enum):
    """
    Supported OpenAI embedding models.
    """

    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"