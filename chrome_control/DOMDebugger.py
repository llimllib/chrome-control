from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import Runtime

DOMBreakpointType = Enum("DOMBreakpointType", "subtree-modified attribute-modified node-removed")
DOMBreakpointType.__doc__ = """DOM breakpoint type."""

class EventListener:
    """Object event listener."""
    def __init__(self, type: str, useCapture: bool, passive: bool, once: bool, scriptId: "Runtime.ScriptId", lineNumber: int, columnNumber: int, handler: "Runtime.RemoteObject"=None, originalHandler: "Runtime.RemoteObject"=None, removeFunction: "Runtime.RemoteObject"=None):
        # <code>EventListener</code>'s type.
        self.type = type
        # <code>EventListener</code>'s useCapture.
        self.useCapture = useCapture
        # <code>EventListener</code>'s passive flag.
        self.passive = passive
        # <code>EventListener</code>'s once flag.
        self.once = once
        # Script id of the handler code.
        self.scriptId = scriptId
        # Line number in the script (0-based).
        self.lineNumber = lineNumber
        # Column number in the script (0-based).
        self.columnNumber = columnNumber
        # Event handler function value.
        self.handler = handler
        # Event original handler function value.
        self.originalHandler = originalHandler
        # Event listener remove function.
        self.removeFunction = removeFunction

class setDOMBreakpoint(ChromeCommand):
    """Sets breakpoint on particular operation with DOM."""

    def __init__(self, nodeId: "DOM.NodeId", type: "DOMBreakpointType"):
        # Identifier of the node to set breakpoint on.
        self.nodeId = nodeId
        # Type of the operation to stop upon.
        self.type = type



class removeDOMBreakpoint(ChromeCommand):
    """Removes DOM breakpoint that was set using <code>setDOMBreakpoint</code>."""

    def __init__(self, nodeId: "DOM.NodeId", type: "DOMBreakpointType"):
        # Identifier of the node to remove breakpoint from.
        self.nodeId = nodeId
        # Type of the breakpoint to remove.
        self.type = type



class setEventListenerBreakpoint(ChromeCommand):
    """Sets breakpoint on particular DOM event."""

    def __init__(self, eventName: str, targetName: str=None):
        # DOM Event name to stop on (any DOM event will do).
        self.eventName = eventName
        # EventTarget interface name to stop on. If equal to <code>"*"</code> or not provided, will stop on any EventTarget.
        self.targetName = targetName



class removeEventListenerBreakpoint(ChromeCommand):
    """Removes breakpoint on particular DOM event."""

    def __init__(self, eventName: str, targetName: str=None):
        # Event name.
        self.eventName = eventName
        # EventTarget interface name.
        self.targetName = targetName



class setInstrumentationBreakpoint(ChromeCommand):
    """Sets breakpoint on particular native event."""

    def __init__(self, eventName: str):
        # Instrumentation name to stop on.
        self.eventName = eventName



class removeInstrumentationBreakpoint(ChromeCommand):
    """Removes breakpoint on particular native event."""

    def __init__(self, eventName: str):
        # Instrumentation name to stop on.
        self.eventName = eventName



class setXHRBreakpoint(ChromeCommand):
    """Sets breakpoint on XMLHttpRequest."""

    def __init__(self, url: str):
        # Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        self.url = url



class removeXHRBreakpoint(ChromeCommand):
    """Removes breakpoint from XMLHttpRequest."""

    def __init__(self, url: str):
        # Resource URL substring.
        self.url = url



class getEventListeners(ChromeCommand):
    """Returns event listeners of the given object."""

    def __init__(self, objectId: "Runtime.RemoteObjectId"):
        # Identifier of the object to return listeners for.
        self.objectId = objectId



