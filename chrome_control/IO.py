from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


StreamHandle = str

class read(ChromeCommand):
    """Read a chunk of the stream"""

    def __init__(self, handle: "StreamHandle", offset: int=None, size: int=None):
        # Handle of the stream to read.
        self.handle = handle
        # Seek to the specified offset before reading (if not specificed, proceed with offset following the last read).
        self.offset = offset
        # Maximum number of bytes to read (left upon the agent discretion if not specified).
        self.size = size



class close(ChromeCommand):
    """Close the stream, discard any temporary backing storage."""

    def __init__(self, handle: "StreamHandle"):
        # Handle of the stream to close.
        self.handle = handle



