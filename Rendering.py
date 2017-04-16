from enum import Enum
from typing import Any, List

from base import ChromeCommand


class setShowPaintRects(ChromeCommand):
    """Requests that backend shows paint rectangles"""

    def __init__(self, result: bool):
        # True for showing paint rectangles
        self.result = result



class setShowDebugBorders(ChromeCommand):
    """Requests that backend shows debug borders on layers"""

    def __init__(self, show: bool):
        # True for showing debug borders
        self.show = show



class setShowFPSCounter(ChromeCommand):
    """Requests that backend shows the FPS counter"""

    def __init__(self, show: bool):
        # True for showing the FPS counter
        self.show = show



class setShowScrollBottleneckRects(ChromeCommand):
    """Requests that backend shows scroll bottleneck rects"""

    def __init__(self, show: bool):
        # True for showing scroll bottleneck rects
        self.show = show



class setShowViewportSizeOnResize(ChromeCommand):
    """Paints viewport size upon main frame resize."""

    def __init__(self, show: bool):
        # Whether to paint size or not.
        self.show = show



