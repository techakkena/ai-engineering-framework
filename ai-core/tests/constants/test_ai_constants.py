from constants.ai_constants import (
    AIProvider,
    AITask,
    AudioModels,
    ChatModels,
    ChunkStrategy,
    DistanceMetric,
    EmbeddingModels,
    FinishReasons,
    ImageModels,
    PromptRole,
    ReasoningModels,
    ResponseFormat,
    RetrievalStrategy,
    TokenLimits,
    ToolTypes,
    VectorStores,
)


def test_ai_provider():
    assert AIProvider.OPENAI == "openai"
    assert AIProvider.ANTHROPIC == "anthropic"
    assert AIProvider.GOOGLE == "google"
    assert AIProvider.AZURE_OPENAI == "azure_openai"
    assert AIProvider.OLLAMA == "ollama"
    assert AIProvider.HUGGINGFACE == "huggingface"


def test_chat_models():
    assert ChatModels.GPT_5_5 == "gpt-5.5"
    assert ChatModels.GPT_5_MINI == "gpt-5-mini"
    assert ChatModels.CLAUDE_SONNET == "claude-sonnet"
    assert ChatModels.GEMINI_PRO == "gemini-pro"


def test_embedding_models():
    assert EmbeddingModels.TEXT_EMBEDDING_3_SMALL == "text-embedding-3-small"
    assert EmbeddingModels.TEXT_EMBEDDING_3_LARGE == "text-embedding-3-large"


def test_image_models():
    assert ImageModels.GPT_IMAGE_1 == "gpt-image-1"


def test_audio_models():
    assert AudioModels.GPT_4O_TRANSCRIBE == "gpt-4o-transcribe"
    assert AudioModels.GPT_4O_MINI_TRANSCRIBE == "gpt-4o-mini-transcribe"
    assert AudioModels.GPT_4O_MINI_TTS == "gpt-4o-mini-tts"


def test_reasoning_models():
    assert ReasoningModels.GPT_5 == "gpt-5"
    assert ReasoningModels.GPT_5_MINI == "gpt-5-mini"


def test_response_formats():
    assert ResponseFormat.TEXT == "text"
    assert ResponseFormat.JSON == "json"
    assert ResponseFormat.MARKDOWN == "markdown"
    assert ResponseFormat.HTML == "html"
    assert ResponseFormat.XML == "xml"


def test_prompt_roles():
    assert PromptRole.SYSTEM == "system"
    assert PromptRole.USER == "user"
    assert PromptRole.ASSISTANT == "assistant"


def test_token_limits():
    assert TokenLimits.DEFAULT_INPUT == 8192
    assert TokenLimits.DEFAULT_OUTPUT == 4096


def test_vector_stores():
    assert VectorStores.FAISS == "faiss"
    assert VectorStores.CHROMA == "chroma"
    assert VectorStores.PINECONE == "pinecone"
    assert VectorStores.WEAVIATE == "weaviate"
    assert VectorStores.MILVUS == "milvus"


def test_finish_reasons():
    assert FinishReasons.STOP == "stop"
    assert FinishReasons.LENGTH == "length"
    assert FinishReasons.TOOL_CALLS == "tool_calls"
    assert FinishReasons.CONTENT_FILTER == "content_filter"


def test_tool_types():
    assert ToolTypes.FUNCTION == "function"
    assert ToolTypes.RETRIEVAL == "retrieval"
    assert ToolTypes.WEB_SEARCH == "web_search"
    assert ToolTypes.CODE_INTERPRETER == "code_interpreter"


def test_retrieval_strategy():
    assert RetrievalStrategy.SIMILARITY == "similarity"
    assert RetrievalStrategy.MMR == "mmr"
    assert RetrievalStrategy.HYBRID == "hybrid"


def test_chunk_strategy():
    assert ChunkStrategy.FIXED == "fixed"
    assert ChunkStrategy.RECURSIVE == "recursive"
    assert ChunkStrategy.SEMANTIC == "semantic"


def test_distance_metric():
    assert DistanceMetric.COSINE == "cosine"
    assert DistanceMetric.EUCLIDEAN == "euclidean"
    assert DistanceMetric.DOT_PRODUCT == "dot_product"


def test_ai_task():
    assert AITask.CHAT == "chat"
    assert AITask.EMBEDDING == "embedding"
    assert AITask.IMAGE == "image"
    assert AITask.AUDIO == "audio"
    assert AITask.TRANSLATION == "translation"
    assert AITask.SUMMARIZATION == "summarization"
    assert AITask.CLASSIFICATION == "classification"
