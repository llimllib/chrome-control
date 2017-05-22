from enum import Enum
from typing import Any, List

from .base import ChromeCommand

from . import Page

class ApplicationCacheResource:
    """Detailed application cache resource information."""
    def __init__(self, url: str, size: int, type: str):
        # Resource url.
        self.url = url
        # Resource size.
        self.size = size
        # Resource type.
        self.type = type

class ApplicationCache:
    """Detailed application cache information."""
    def __init__(self, manifestURL: str, size: float, creationTime: float, updateTime: float, resources: List):
        # Manifest URL.
        self.manifestURL = manifestURL
        # Application cache size.
        self.size = size
        # Application cache creation time.
        self.creationTime = creationTime
        # Application cache update time.
        self.updateTime = updateTime
        # Application cache resources.
        self.resources = resources

class FrameWithManifest:
    """Frame identifier - manifest URL pair."""
    def __init__(self, frameId: "Page.FrameId", manifestURL: str, status: int):
        # Frame identifier.
        self.frameId = frameId
        # Manifest URL.
        self.manifestURL = manifestURL
        # Application cache status.
        self.status = status

class getFramesWithManifests(ChromeCommand):
    """Returns array of frame identifiers with manifest urls for each frame containing a document associated with some application cache."""

    def __init__(self): pass

class enable(ChromeCommand):
    """Enables application cache domain notifications."""

    def __init__(self): pass

class getManifestForFrame(ChromeCommand):
    """Returns manifest URL for document in the given frame."""

    def __init__(self, frameId: "Page.FrameId"):
        # Identifier of the frame containing document whose manifest is retrieved.
        self.frameId = frameId



class getApplicationCacheForFrame(ChromeCommand):
    """Returns relevant application cache data for the document in given frame."""

    def __init__(self, frameId: "Page.FrameId"):
        # Identifier of the frame containing document whose application cache is retrieved.
        self.frameId = frameId



