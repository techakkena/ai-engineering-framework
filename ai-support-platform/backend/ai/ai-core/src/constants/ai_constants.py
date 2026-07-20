from __future__ import annotations

"""
AI Engineering Framework
AI Constants

Author : TECHAKKENA
"""


class AIProvider:
    """
    Supported AI providers.
    """

    OPENAI = "openai"

    ANTHROPIC = "anthropic"

    GOOGLE = "google"

    AZURE_OPENAI = "azure_openai"

    OLLAMA = "ollama"

    HUGGINGFACE = "huggingface"


class ChatModels:
    """
    Chat models.
    """

    GPT_5_5 = "gpt-5.5"

    GPT_5_MINI = "gpt-5-mini"

    CLAUDE_SONNET = "claude-sonnet"

    GEMINI_PRO = "gemini-pro"


class AIModels:
    GPT_5_5 = "gpt-5.5"
    GPT_5_MINI = "gpt-5-mini"
    GPT_4_1 = "gpt-4.1"

    CLAUDE_SONNET = "claude-sonnet-4"
    CLAUDE_OPUS = "claude-opus-4"

    GEMINI_2_5_PRO = "gemini-2.5-pro"

    OLLAMA_LLAMA3 = "llama3"


class EmbeddingModels:
    """
    Embedding models.
    """

    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"

    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"


class ImageModels:
    """
    Image generation models.
    """

    GPT_IMAGE_1 = "gpt-image-1"


class AudioModels:
    """
    Audio AI models.
    """

    GPT_4O_TRANSCRIBE = "gpt-4o-transcribe"
    GPT_4O_MINI_TRANSCRIBE = "gpt-4o-mini-transcribe"
    GPT_4O_MINI_TTS = "gpt-4o-mini-tts"


class ReasoningModels:
    """
    Reasoning AI models.
    """

    GPT_5 = "gpt-5"
    GPT_5_MINI = "gpt-5-mini"


class ResponseFormat:
    """
    AI response formats.
    """

    TEXT = "text"

    JSON = "json"

    MARKDOWN = "markdown"

    HTML = "html"

    XML = "xml"


class PromptRole:
    """
    Prompt roles.
    """

    SYSTEM = "system"

    USER = "user"

    ASSISTANT = "assistant"


class TokenLimits:
    """
    Default token limits.
    """

    DEFAULT_INPUT = 8192

    DEFAULT_OUTPUT = 4096


class VectorStores:
    """
    Vector store types.
    """

    FAISS = "faiss"
    CHROMA = "chroma"
    PINECONE = "pinecone"
    WEAVIATE = "weaviate"
    MILVUS = "milvus"


class FinishReasons:
    """
    Reason for finishing a conversation.
    """

    STOP = "stop"

    LENGTH = "length"

    TOOL_CALLS = "tool_calls"

    CONTENT_FILTER = "content_filter"


class ToolTypes:
    """
    Types of tools available.
    """

    FUNCTION = "function"

    RETRIEVAL = "retrieval"

    WEB_SEARCH = "web_search"

    CODE_INTERPRETER = "code_interpreter"


class RetrievalStrategy:
    """
    Retrieval strategies.
    """

    SIMILARITY = "similarity"
    MMR = "mmr"
    HYBRID = "hybrid"


class ChunkStrategy:
    """
    Text chunking strategies.
    """

    FIXED = "fixed"
    RECURSIVE = "recursive"
    SEMANTIC = "semantic"


class DistanceMetric:
    """
    Vector distance metrics.
    """

    COSINE = "cosine"
    EUCLIDEAN = "euclidean"
    DOT_PRODUCT = "dot_product"


class AITask:
    """
    AI task categories.
    """

    CHAT = "chat"
    EMBEDDING = "embedding"
    IMAGE = "image"
    AUDIO = "audio"
    TRANSLATION = "translation"
    SUMMARIZATION = "summarization"
    CLASSIFICATION = "classification"
