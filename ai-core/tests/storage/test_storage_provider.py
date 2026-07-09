"""
AI Engineering Framework
Storage Provider Tests

Author : TECHAKKENA
"""

import pytest

from storage.storage_provider import StorageProvider


def test_storage_provider_is_abstract():
    """
    StorageProvider is an abstract class and cannot be instantiated.
    """
    with pytest.raises(TypeError):
        StorageProvider()

