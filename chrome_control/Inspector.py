from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


class enable(ChromeCommand):
    """Enables inspector domain notifications."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables inspector domain notifications."""

    def __init__(self): pass

class detached(ChromeEvent):
    """Fired when remote debugging connection is about to be terminated. Contains detach reason."""

    def __init__(self, reason: str):
        # The reason why connection has been terminated.
        self.reason = reason



class targetCrashed(ChromeEvent):
    """Fired when debugging target has crashed"""

    def __init__(self): pass

