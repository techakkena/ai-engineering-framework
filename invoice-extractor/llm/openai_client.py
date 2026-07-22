import os

from fastapi import HTTPException
from openai import OpenAI

_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not configured.")
        _client = OpenAI(api_key=api_key)
    return _client


def get_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-5.5")
