from enum import Enum
from typing import Any, List

from .base import ChromeCommand

from . import Runtime

class ProfileNode:
    """Profile node. Holds callsite information, execution statistics and child nodes."""
    def __init__(self, id: int, callFrame: "Runtime.CallFrame", hitCount: int=None, children: List=None, deoptReason: str=None, positionTicks: List=None):
        # Unique id of the node.
        self.id = id
        # Function location.
        self.callFrame = callFrame
        # Number of samples where this node was on top of the call stack.
        self.hitCount = hitCount
        # Child node ids.
        self.children = children
        # The reason of being not optimized. The function may be deoptimized or marked as don't optimize.
        self.deoptReason = deoptReason
        # An array of source position ticks.
        self.positionTicks = positionTicks

class Profile:
    """Profile."""
    def __init__(self, nodes: List, startTime: float, endTime: float, samples: List=None, timeDeltas: List=None):
        # The list of profile nodes. First item is the root node.
        self.nodes = nodes
        # Profiling start timestamp in microseconds.
        self.startTime = startTime
        # Profiling end timestamp in microseconds.
        self.endTime = endTime
        # Ids of samples top nodes.
        self.samples = samples
        # Time intervals between adjacent samples in microseconds. The first delta is relative to the profile startTime.
        self.timeDeltas = timeDeltas

class PositionTickInfo:
    """Specifies a number of samples attributed to a certain source position."""
    def __init__(self, line: int, ticks: int):
        # Source line number (1-based).
        self.line = line
        # Number of samples attributed to the source line.
        self.ticks = ticks

class enable(ChromeCommand):
    def __init__(self): pass

class disable(ChromeCommand):
    def __init__(self): pass

class setSamplingInterval(ChromeCommand):
    """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started."""

    def __init__(self, interval: int):
        # New sampling interval in microseconds.
        self.interval = interval



class start(ChromeCommand):
    def __init__(self): pass

class stop(ChromeCommand):
    def __init__(self): pass

