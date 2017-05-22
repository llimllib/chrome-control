from enum import Enum
from typing import Any, List

from .base import ChromeCommand


class Domain:
    """Description of the protocol domain."""
    def __init__(self, name: str, version: str):
        # Domain name.
        self.name = name
        # Domain version.
        self.version = version

class getDomains(ChromeCommand):
    """Returns supported domains."""

    def __init__(self): pass

