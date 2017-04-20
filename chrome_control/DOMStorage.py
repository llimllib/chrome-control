from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


class StorageId:
    """DOM Storage identifier."""
    def __init__(self, securityOrigin: str, isLocalStorage: bool):
        # Security origin for the storage.
        self.securityOrigin = securityOrigin
        # Whether the storage is local storage (not session storage).
        self.isLocalStorage = isLocalStorage

# DOM Storage item.
Item = List[str]
class enable(ChromeCommand):
    """Enables storage tracking, storage events will now be delivered to the client."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables storage tracking, prevents storage events from being sent to the client."""

    def __init__(self): pass

class getDOMStorageItems(ChromeCommand):
    def __init__(self, storageId: "StorageId"):
        self.storageId = storageId



class setDOMStorageItem(ChromeCommand):
    def __init__(self, storageId: "StorageId", key: str, value: str):
        self.storageId = storageId
        self.key = key
        self.value = value



class removeDOMStorageItem(ChromeCommand):
    def __init__(self, storageId: "StorageId", key: str):
        self.storageId = storageId
        self.key = key



class domStorageItemsCleared(ChromeEvent):
    def __init__(self, storageId: "StorageId"):
        self.storageId = storageId



class domStorageItemRemoved(ChromeEvent):
    def __init__(self, storageId: "StorageId", key: str):
        self.storageId = storageId
        self.key = key



class domStorageItemAdded(ChromeEvent):
    def __init__(self, storageId: "StorageId", key: str, newValue: str):
        self.storageId = storageId
        self.key = key
        self.newValue = newValue



class domStorageItemUpdated(ChromeEvent):
    def __init__(self, storageId: "StorageId", key: str, oldValue: str, newValue: str):
        self.storageId = storageId
        self.key = key
        self.oldValue = oldValue
        self.newValue = newValue



