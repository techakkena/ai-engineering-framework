"""
AI Engineering Framework
Storage Factory

Author : TECHAKKENA
"""

from constants.storage_constants import StorageTypes
from exceptions.configuration_exception import ConfigurationException

from .file_storage import FileStorage
from .storage_provider import StorageProvider


class StorageFactory:
    """
    Factory for creating storage providers.
    """

    @staticmethod
    def create(
        provider: str = StorageTypes.LOCAL,
    ) -> StorageProvider:
        """
        Create a storage provider.
        """

        if provider == StorageTypes.LOCAL:
            return FileStorage()

        raise ConfigurationException(
            message="Unsupported storage provider.",
            details={
                "provider": provider,
            },
        )
