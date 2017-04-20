from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


TargetID = str

BrowserContextID = str

class TargetInfo:
    def __init__(self, targetId: "TargetID", type: str, title: str, url: str):
        self.targetId = targetId
        self.type = type
        self.title = title
        self.url = url

class RemoteLocation:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

class setDiscoverTargets(ChromeCommand):
    """Controls whether to discover available targets and notify via <code>targetCreated/targetDestroyed</code> events."""

    def __init__(self, discover: bool):
        # Whether to discover available targets.
        self.discover = discover



class setAutoAttach(ChromeCommand):
    """Controls whether to automatically attach to new targets which are considered to be related to this one. When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets."""

    def __init__(self, autoAttach: bool, waitForDebuggerOnStart: bool):
        # Whether to auto-attach to related targets.
        self.autoAttach = autoAttach
        # Whether to pause new targets when attaching to them. Use <code>Runtime.runIfWaitingForDebugger</code> to run paused targets.
        self.waitForDebuggerOnStart = waitForDebuggerOnStart



class setAttachToFrames(ChromeCommand):
    def __init__(self, value: bool):
        # Whether to attach to frames.
        self.value = value



class setRemoteLocations(ChromeCommand):
    """Enables target discovery for the specified locations, when <code>setDiscoverTargets</code> was set to <code>true</code>."""

    def __init__(self, locations: List):
        # List of remote locations.
        self.locations = locations



class sendMessageToTarget(ChromeCommand):
    """Sends protocol message to the target with given id."""

    def __init__(self, targetId: str, message: str):
        self.targetId = targetId
        self.message = message



class getTargetInfo(ChromeCommand):
    """Returns information about a target."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class activateTarget(ChromeCommand):
    """Activates (focuses) the target."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class closeTarget(ChromeCommand):
    """Closes the target. If the target is a page that gets closed too."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class attachToTarget(ChromeCommand):
    """Attaches to the target with given id."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class detachFromTarget(ChromeCommand):
    """Detaches from the target with given id."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class createBrowserContext(ChromeCommand):
    """Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one."""

    def __init__(self): pass

class disposeBrowserContext(ChromeCommand):
    """Deletes a BrowserContext, will fail of any open page uses it."""

    def __init__(self, browserContextId: "BrowserContextID"):
        self.browserContextId = browserContextId



class createTarget(ChromeCommand):
    """Creates a new page."""

    def __init__(self, url: str, width: int=None, height: int=None, browserContextId: "BrowserContextID"=None):
        # The initial URL the page will be navigated to.
        self.url = url
        # Frame width in DIP (headless chrome only).
        self.width = width
        # Frame height in DIP (headless chrome only).
        self.height = height
        # The browser context to create the page in (headless chrome only).
        self.browserContextId = browserContextId



class getTargets(ChromeCommand):
    """Retrieves a list of available targets."""

    def __init__(self): pass

class targetCreated(ChromeEvent):
    """Issued when a possible inspection target is created."""

    def __init__(self, targetInfo: "TargetInfo"):
        self.targetInfo = targetInfo



class targetDestroyed(ChromeEvent):
    """Issued when a target is destroyed."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class attachedToTarget(ChromeEvent):
    """Issued when attached to target because of auto-attach or <code>attachToTarget</code> command."""

    def __init__(self, targetInfo: "TargetInfo", waitingForDebugger: bool):
        self.targetInfo = targetInfo
        self.waitingForDebugger = waitingForDebugger



class detachedFromTarget(ChromeEvent):
    """Issued when detached from target for any reason (including <code>detachFromTarget</code> command)."""

    def __init__(self, targetId: "TargetID"):
        self.targetId = targetId



class receivedMessageFromTarget(ChromeEvent):
    """Notifies about new protocol message from attached target."""

    def __init__(self, targetId: "TargetID", message: str):
        self.targetId = targetId
        self.message = message



