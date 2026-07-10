"""
AI Engineering Framework
Vector Storage

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List


class VectorStorage(ABC):
    """
    Abstract base class for vector databases.
    """

    @abstractmethod
    def add(
        self,
        vectors: List[List[float]],
        metadata: List[Dict[str, Any]],
    ):
        """
        Add vectors to storage.
        """
        pass

    @abstractmethod
    def search(
        self,
        vector: List[float],
        k: int = 5,
    ):
        """
        Search nearest vectors.
        """
        pass

    @abstractmethod
    def delete(
        self,
        ids: List[str],
    ):
        """
        Delete vectors.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Remove all vectors.
        """
        pass

    @abstractmethod
    def count(self) -> int:
        """
        Number of stored vectors.
        """
        pass

    @abstractmethod
    def save(self):
        """
        Persist vector index.
        """
        pass

    @abstractmethod
    def load(self):
        """
        Load vector index.
        """
        pass


@dataclass
class VectorRecord:
    id: str
    vector: list[float]
    metadata: dict[str, Any]
