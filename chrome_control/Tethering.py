from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


class bind(ChromeCommand):
    """Request browser port binding."""

    def __init__(self, port: int):
        # Port number to bind.
        self.port = port



class unbind(ChromeCommand):
    """Request browser port unbinding."""

    def __init__(self, port: int):
        # Port number to unbind.
        self.port = port



class accepted(ChromeEvent):
    """Informs that port was successfully bound and got a specified connection id."""

    def __init__(self, port: int, connectionId: str):
        # Port number that was successfully bound.
        self.port = port
        # Connection id to be used.
        self.connectionId = connectionId



