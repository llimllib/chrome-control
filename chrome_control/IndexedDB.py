from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import Runtime

class DatabaseWithObjectStores:
    """Database with an array of object stores."""
    def __init__(self, name: str, version: int, objectStores: List):
        # Database name.
        self.name = name
        # Database version.
        self.version = version
        # Object stores in this database.
        self.objectStores = objectStores

class ObjectStore:
    """Object store."""
    def __init__(self, name: str, keyPath: "KeyPath", autoIncrement: bool, indexes: List):
        # Object store name.
        self.name = name
        # Object store key path.
        self.keyPath = keyPath
        # If true, object store has auto increment flag set.
        self.autoIncrement = autoIncrement
        # Indexes in this object store.
        self.indexes = indexes

class ObjectStoreIndex:
    """Object store index."""
    def __init__(self, name: str, keyPath: "KeyPath", unique: bool, multiEntry: bool):
        # Index name.
        self.name = name
        # Index key path.
        self.keyPath = keyPath
        # If true, index is unique.
        self.unique = unique
        # If true, index allows multiple entries for a key.
        self.multiEntry = multiEntry

class Key:
    """Key."""
    def __init__(self, type: str, number: float=None, string: str=None, date: float=None, array: List=None):
        # Key type.
        self.type = type
        # Number value.
        self.number = number
        # String value.
        self.string = string
        # Date value.
        self.date = date
        # Array value.
        self.array = array

class KeyRange:
    """Key range."""
    def __init__(self, lowerOpen: bool, upperOpen: bool, lower: "Key"=None, upper: "Key"=None):
        # If true lower bound is open.
        self.lowerOpen = lowerOpen
        # If true upper bound is open.
        self.upperOpen = upperOpen
        # Lower bound.
        self.lower = lower
        # Upper bound.
        self.upper = upper

class DataEntry:
    """Data entry."""
    def __init__(self, key: "Runtime.RemoteObject", primaryKey: "Runtime.RemoteObject", value: "Runtime.RemoteObject"):
        # Key object.
        self.key = key
        # Primary key object.
        self.primaryKey = primaryKey
        # Value object.
        self.value = value

class KeyPath:
    """Key path."""
    def __init__(self, type: str, string: str=None, array: List=None):
        # Key path type.
        self.type = type
        # String value.
        self.string = string
        # Array value.
        self.array = array

class enable(ChromeCommand):
    """Enables events from backend."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables events from backend."""

    def __init__(self): pass

class requestDatabaseNames(ChromeCommand):
    """Requests database names for given security origin."""

    def __init__(self, securityOrigin: str):
        # Security origin.
        self.securityOrigin = securityOrigin



class requestDatabase(ChromeCommand):
    """Requests database with given name in given frame."""

    def __init__(self, securityOrigin: str, databaseName: str):
        # Security origin.
        self.securityOrigin = securityOrigin
        # Database name.
        self.databaseName = databaseName



class requestData(ChromeCommand):
    """Requests data from object store or index."""

    def __init__(self, securityOrigin: str, databaseName: str, objectStoreName: str, indexName: str, skipCount: int, pageSize: int, keyRange: "KeyRange"=None):
        # Security origin.
        self.securityOrigin = securityOrigin
        # Database name.
        self.databaseName = databaseName
        # Object store name.
        self.objectStoreName = objectStoreName
        # Index name, empty string for object store data requests.
        self.indexName = indexName
        # Number of records to skip.
        self.skipCount = skipCount
        # Number of records to fetch.
        self.pageSize = pageSize
        # Key range.
        self.keyRange = keyRange



class clearObjectStore(ChromeCommand):
    """Clears all entries from an object store."""

    def __init__(self, securityOrigin: str, databaseName: str, objectStoreName: str):
        # Security origin.
        self.securityOrigin = securityOrigin
        # Database name.
        self.databaseName = databaseName
        # Object store name.
        self.objectStoreName = objectStoreName



