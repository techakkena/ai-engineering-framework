"""
AI Engineering Framework
AI Chat Constants

Author : TECHAKKENA
"""


class ChatConstants:
    """
    Chat framework constants.
    """

    # Default AI Model
    DEFAULT_MODEL = "gpt-5.5"

    # Default Generation Settings
    DEFAULT_TEMPERATURE = 0.2
    DEFAULT_MAX_TOKENS = 4096
    DEFAULT_STREAM = False

    # Session
    DEFAULT_SESSION_ID = None

    # Chat Roles
    SYSTEM_ROLE = "system"
    USER_ROLE = "user"
    ASSISTANT_ROLE = "assistant"
    TOOL_ROLE = "tool"

    # Conversation
    MAX_HISTORY = 100

    # Default Prompt
    DEFAULT_SYSTEM_PROMPT = "You are a helpful AI assistant."

    # Response
    DEFAULT_FINISH_REASON = "stop"

    # Health
    SERVICE_NAME = "ai-chat"
    SERVICE_VERSION = "0.1.0"
