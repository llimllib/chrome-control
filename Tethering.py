from enum import Enum
from typing import Any, List

from base import ChromeCommand


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



