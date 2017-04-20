from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import DOM

# Unique Layer identifier.
LayerId = str

# Unique snapshot identifier.
SnapshotId = str

class ScrollRect:
    """Rectangle where scrolling happens on the main thread."""
    def __init__(self, rect: "DOM.Rect", type: str):
        # Rectangle itself.
        self.rect = rect
        # Reason for rectangle to force scrolling on the main thread
        self.type = type

class PictureTile:
    """Serialized fragment of layer picture along with its offset within the layer."""
    def __init__(self, x: float, y: float, picture: str):
        # Offset from owning layer left boundary
        self.x = x
        # Offset from owning layer top boundary
        self.y = y
        # Base64-encoded snapshot data.
        self.picture = picture

class Layer:
    """Information about a compositing layer."""
    def __init__(self, layerId: "LayerId", offsetX: float, offsetY: float, width: float, height: float, paintCount: int, drawsContent: bool, parentLayerId: "LayerId"=None, backendNodeId: "DOM.BackendNodeId"=None, transform: List=None, anchorX: float=None, anchorY: float=None, anchorZ: float=None, invisible: bool=None, scrollRects: List=None):
        # The unique id for this layer.
        self.layerId = layerId
        # Offset from parent layer, X coordinate.
        self.offsetX = offsetX
        # Offset from parent layer, Y coordinate.
        self.offsetY = offsetY
        # Layer width.
        self.width = width
        # Layer height.
        self.height = height
        # Indicates how many time this layer has painted.
        self.paintCount = paintCount
        # Indicates whether this layer hosts any content, rather than being used for transform/scrolling purposes only.
        self.drawsContent = drawsContent
        # The id of parent (not present for root).
        self.parentLayerId = parentLayerId
        # The backend id for the node associated with this layer.
        self.backendNodeId = backendNodeId
        # Transformation matrix for layer, default is identity matrix
        self.transform = transform
        # Transform anchor point X, absent if no transform specified
        self.anchorX = anchorX
        # Transform anchor point Y, absent if no transform specified
        self.anchorY = anchorY
        # Transform anchor point Z, absent if no transform specified
        self.anchorZ = anchorZ
        # Set if layer is not visible.
        self.invisible = invisible
        # Rectangles scrolling on main thread only.
        self.scrollRects = scrollRects

# Array of timings, one per paint step.
# items: A time in seconds since the end of previous step (for the first step, time since painting started)PaintProfile = List[float]
class enable(ChromeCommand):
    """Enables compositing tree inspection."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables compositing tree inspection."""

    def __init__(self): pass

class compositingReasons(ChromeCommand):
    """Provides the reasons why the given layer was composited."""

    def __init__(self, layerId: "LayerId"):
        # The id of the layer for which we want to get the reasons it was composited.
        self.layerId = layerId



class makeSnapshot(ChromeCommand):
    """Returns the layer snapshot identifier."""

    def __init__(self, layerId: "LayerId"):
        # The id of the layer.
        self.layerId = layerId



class loadSnapshot(ChromeCommand):
    """Returns the snapshot identifier."""

    def __init__(self, tiles: List):
        # An array of tiles composing the snapshot.
        self.tiles = tiles



class releaseSnapshot(ChromeCommand):
    """Releases layer snapshot captured by the back-end."""

    def __init__(self, snapshotId: "SnapshotId"):
        # The id of the layer snapshot.
        self.snapshotId = snapshotId



class profileSnapshot(ChromeCommand):
    def __init__(self, snapshotId: "SnapshotId", minRepeatCount: int=None, minDuration: float=None, clipRect: "DOM.Rect"=None):
        # The id of the layer snapshot.
        self.snapshotId = snapshotId
        # The maximum number of times to replay the snapshot (1, if not specified).
        self.minRepeatCount = minRepeatCount
        # The minimum duration (in seconds) to replay the snapshot.
        self.minDuration = minDuration
        # The clip rectangle to apply when replaying the snapshot.
        self.clipRect = clipRect



class replaySnapshot(ChromeCommand):
    """Replays the layer snapshot and returns the resulting bitmap."""

    def __init__(self, snapshotId: "SnapshotId", fromStep: int=None, toStep: int=None, scale: float=None):
        # The id of the layer snapshot.
        self.snapshotId = snapshotId
        # The first step to replay from (replay from the very start if not specified).
        self.fromStep = fromStep
        # The last step to replay to (replay till the end if not specified).
        self.toStep = toStep
        # The scale to apply while replaying (defaults to 1).
        self.scale = scale



class snapshotCommandLog(ChromeCommand):
    """Replays the layer snapshot and returns canvas log."""

    def __init__(self, snapshotId: "SnapshotId"):
        # The id of the layer snapshot.
        self.snapshotId = snapshotId



class layerTreeDidChange(ChromeEvent):
    def __init__(self, layers: List=None):
        # Layer tree, absent if not in the comspositing mode.
        self.layers = layers



class layerPainted(ChromeEvent):
    def __init__(self, layerId: "LayerId", clip: "DOM.Rect"):
        # The id of the painted layer.
        self.layerId = layerId
        # Clip rectangle.
        self.clip = clip



