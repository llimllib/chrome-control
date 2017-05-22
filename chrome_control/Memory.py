from enum import Enum
from typing import Any, List

from .base import ChromeCommand


PressureLevel = Enum("PressureLevel", "moderate critical")
PressureLevel.__doc__ = """Memory pressure level."""

class getDOMCounters(ChromeCommand):
    def __init__(self): pass

class setPressureNotificationsSuppressed(ChromeCommand):
    """Enable/disable suppressing memory pressure notifications in all processes."""

    def __init__(self, suppressed: bool):
        # If true, memory pressure notifications will be suppressed.
        self.suppressed = suppressed



class simulatePressureNotification(ChromeCommand):
    """Simulate a memory pressure notification in all processes."""

    def __init__(self, level: "PressureLevel"):
        # Memory pressure level of the notification.
        self.level = level



