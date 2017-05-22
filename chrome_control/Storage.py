from enum import Enum
from typing import Any, List

from .base import ChromeCommand


StorageType = Enum("StorageType", "appcache cookies file_systems indexeddb local_storage shader_cache websql service_workers cache_storage all")
StorageType.__doc__ = """Enum of possible storage types."""

class clearDataForOrigin(ChromeCommand):
    """Clears storage for origin."""

    def __init__(self, origin: str, storageTypes: str):
        # Security origin.
        self.origin = origin
        # Comma separated origin names.
        self.storageTypes = storageTypes



