from enum import Enum
from typing import Any, List

from base import ChromeCommand


class ConsoleMessage:
    """Console message."""
    def __init__(self, source: str, level: str, text: str, url: str=None, line: int=None, column: int=None):
        # Message source.
        self.source = source
        # Message severity.
        self.level = level
        # Message text.
        self.text = text
        # URL of the message origin.
        self.url = url
        # Line number in the resource that generated this message (1-based).
        self.line = line
        # Column number in the resource that generated this message (1-based).
        self.column = column

class enable(ChromeCommand):
    """Enables console domain, sends the messages collected so far to the client by means of the <code>messageAdded</code> notification."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables console domain, prevents further console messages from being reported to the client."""

    def __init__(self): pass

class clearMessages(ChromeCommand):
    """Does nothing."""

    def __init__(self): pass

