from enum import Enum
from typing import Any, List

from .base import ChromeCommand

from . import Runtime
from . import Network

class LogEntry:
    """Log entry."""
    def __init__(self, source: str, level: str, text: str, timestamp: "Runtime.Timestamp", url: str=None, lineNumber: int=None, stackTrace: "Runtime.StackTrace"=None, networkRequestId: "Network.RequestId"=None, workerId: str=None):
        # Log entry source.
        self.source = source
        # Log entry severity.
        self.level = level
        # Logged text.
        self.text = text
        # Timestamp when this entry was added.
        self.timestamp = timestamp
        # URL of the resource if known.
        self.url = url
        # Line number in the resource.
        self.lineNumber = lineNumber
        # JavaScript stack trace.
        self.stackTrace = stackTrace
        # Identifier of the network request associated with this entry.
        self.networkRequestId = networkRequestId
        # Identifier of the worker associated with this entry.
        self.workerId = workerId

class ViolationSetting:
    """Violation configuration setting."""
    def __init__(self, name: str, threshold: float):
        # Violation type.
        self.name = name
        # Time threshold to trigger upon.
        self.threshold = threshold

class enable(ChromeCommand):
    """Enables log domain, sends the entries collected so far to the client by means of the <code>entryAdded</code> notification."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables log domain, prevents further log entries from being reported to the client."""

    def __init__(self): pass

class clear(ChromeCommand):
    """Clears the log."""

    def __init__(self): pass

class startViolationsReport(ChromeCommand):
    """start violation reporting."""

    def __init__(self, config: List):
        # Configuration for violations.
        self.config = config



class stopViolationsReport(ChromeCommand):
    """Stop violation reporting."""

    def __init__(self): pass

