from enum import Enum
from typing import Any, List

from .base import ChromeCommand


# Unique identifier of Database object.
DatabaseId = str

class Database:
    """Database object."""
    def __init__(self, id: "DatabaseId", domain: str, name: str, version: str):
        # Database ID.
        self.id = id
        # Database domain.
        self.domain = domain
        # Database name.
        self.name = name
        # Database version.
        self.version = version

class Error:
    """Database error."""
    def __init__(self, message: str, code: int):
        # Error message.
        self.message = message
        # Error code.
        self.code = code

class enable(ChromeCommand):
    """Enables database tracking, database events will now be delivered to the client."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables database tracking, prevents database events from being sent to the client."""

    def __init__(self): pass

class getDatabaseTableNames(ChromeCommand):
    def __init__(self, databaseId: "DatabaseId"):
        self.databaseId = databaseId



class executeSQL(ChromeCommand):
    def __init__(self, databaseId: "DatabaseId", query: str):
        self.databaseId = databaseId
        self.query = query



