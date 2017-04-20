from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import Runtime

# Heap snapshot object id.
HeapSnapshotObjectId = str

class SamplingHeapProfileNode:
    """Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes."""
    def __init__(self, callFrame: "Runtime.CallFrame", selfSize: float, children: List):
        # Function location.
        self.callFrame = callFrame
        # Allocations size in bytes for the node excluding children.
        self.selfSize = selfSize
        # Child nodes.
        self.children = children

class SamplingHeapProfile:
    """Profile."""
    def __init__(self, head: "SamplingHeapProfileNode"):
        self.head = head

class enable(ChromeCommand):
    def __init__(self): pass

class disable(ChromeCommand):
    def __init__(self): pass

class startTrackingHeapObjects(ChromeCommand):
    def __init__(self, trackAllocations: bool=None):
        self.trackAllocations = trackAllocations



class stopTrackingHeapObjects(ChromeCommand):
    def __init__(self, reportProgress: bool=None):
        # If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        self.reportProgress = reportProgress



class takeHeapSnapshot(ChromeCommand):
    def __init__(self, reportProgress: bool=None):
        # If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        self.reportProgress = reportProgress



class collectGarbage(ChromeCommand):
    def __init__(self): pass

class getObjectByHeapObjectId(ChromeCommand):
    def __init__(self, objectId: "HeapSnapshotObjectId", objectGroup: str=None):
        self.objectId = objectId
        # Symbolic group name that can be used to release multiple objects.
        self.objectGroup = objectGroup



class addInspectedHeapObject(ChromeCommand):
    """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""

    def __init__(self, heapObjectId: "HeapSnapshotObjectId"):
        # Heap snapshot object id to be accessible by means of $x command line API.
        self.heapObjectId = heapObjectId



class getHeapObjectId(ChromeCommand):
    def __init__(self, objectId: "Runtime.RemoteObjectId"):
        # Identifier of the object to get heap object id for.
        self.objectId = objectId



class startSampling(ChromeCommand):
    def __init__(self, samplingInterval: float=None):
        # Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        self.samplingInterval = samplingInterval



class stopSampling(ChromeCommand):
    def __init__(self): pass

class addHeapSnapshotChunk(ChromeEvent):
    def __init__(self, chunk: str):
        self.chunk = chunk



class resetProfiles(ChromeEvent):
    def __init__(self): pass

class reportHeapSnapshotProgress(ChromeEvent):
    def __init__(self, done: int, total: int, finished: bool=None):
        self.done = done
        self.total = total
        self.finished = finished



class lastSeenObjectId(ChromeEvent):
    """If heap objects tracking has been started then backend regulary sends a current value for last seen object id and corresponding timestamp. If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event."""

    def __init__(self, lastSeenObjectId: int, timestamp: float):
        self.lastSeenObjectId = lastSeenObjectId
        self.timestamp = timestamp



class heapStatsUpdate(ChromeEvent):
    """If heap objects tracking has been started then backend may send update for one or more fragments"""

    def __init__(self, statsUpdate: List):
        # An array of triplets. Each triplet describes a fragment. The first integer is the fragment index, the second integer is a total count of objects for the fragment, the third integer is a total size of the objects for the fragment.
        self.statsUpdate = statsUpdate



