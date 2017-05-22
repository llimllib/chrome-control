from enum import Enum
from typing import Any, List

from .base import ChromeCommand


class ScreenOrientation:
    """Screen orientation."""
    def __init__(self, type: str, angle: int):
        # Orientation type.
        self.type = type
        # Orientation angle.
        self.angle = angle

VirtualTimePolicy = Enum("VirtualTimePolicy", "advance pause pauseIfNetworkFetchesPending")
VirtualTimePolicy.__doc__ = """advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches."""

class setDeviceMetricsOverride(ChromeCommand):
    """Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results)."""

    def __init__(self, width: int, height: int, deviceScaleFactor: float, mobile: bool, fitWindow: bool, scale: float=None, offsetX: float=None, offsetY: float=None, screenWidth: int=None, screenHeight: int=None, positionX: int=None, positionY: int=None, screenOrientation: "ScreenOrientation"=None):
        # Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        self.width = width
        # Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        self.height = height
        # Overriding device scale factor value. 0 disables the override.
        self.deviceScaleFactor = deviceScaleFactor
        # Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
        self.mobile = mobile
        # Whether a view that exceeds the available browser window area should be scaled down to fit.
        self.fitWindow = fitWindow
        # Scale to apply to resulting view image. Ignored in |fitWindow| mode.
        self.scale = scale
        # Not used.
        self.offsetX = offsetX
        # Not used.
        self.offsetY = offsetY
        # Overriding screen width value in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        self.screenWidth = screenWidth
        # Overriding screen height value in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        self.screenHeight = screenHeight
        # Overriding view X position on screen in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        self.positionX = positionX
        # Overriding view Y position on screen in pixels (minimum 0, maximum 10000000). Only used for |mobile==true|.
        self.positionY = positionY
        # Screen orientation override.
        self.screenOrientation = screenOrientation



class clearDeviceMetricsOverride(ChromeCommand):
    """Clears the overriden device metrics."""

    def __init__(self): pass

class forceViewport(ChromeCommand):
    """Overrides the visible area of the page. The change is hidden from the page, i.e. the observable scroll position and page scale does not change. In effect, the command moves the specified area of the page into the top-left corner of the frame."""

    def __init__(self, x: float, y: float, scale: float):
        # X coordinate of top-left corner of the area (CSS pixels).
        self.x = x
        # Y coordinate of top-left corner of the area (CSS pixels).
        self.y = y
        # Scale to apply to the area (relative to a page scale of 1.0).
        self.scale = scale



class resetViewport(ChromeCommand):
    """Resets the visible area of the page to the original viewport, undoing any effects of the <code>forceViewport</code> command."""

    def __init__(self): pass

class resetPageScaleFactor(ChromeCommand):
    """Requests that page scale factor is reset to initial values."""

    def __init__(self): pass

class setPageScaleFactor(ChromeCommand):
    """Sets a specified page scale factor."""

    def __init__(self, pageScaleFactor: float):
        # Page scale factor.
        self.pageScaleFactor = pageScaleFactor



class setVisibleSize(ChromeCommand):
    """Resizes the frame/viewport of the page. Note that this does not affect the frame's container (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported on Android."""

    def __init__(self, width: int, height: int):
        # Frame width (DIP).
        self.width = width
        # Frame height (DIP).
        self.height = height



class setScriptExecutionDisabled(ChromeCommand):
    """Switches script execution in the page."""

    def __init__(self, value: bool):
        # Whether script execution should be disabled in the page.
        self.value = value



class setGeolocationOverride(ChromeCommand):
    """Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable."""

    def __init__(self, latitude: float=None, longitude: float=None, accuracy: float=None):
        # Mock latitude
        self.latitude = latitude
        # Mock longitude
        self.longitude = longitude
        # Mock accuracy
        self.accuracy = accuracy



class clearGeolocationOverride(ChromeCommand):
    """Clears the overriden Geolocation Position and Error."""

    def __init__(self): pass

class setTouchEmulationEnabled(ChromeCommand):
    """Toggles mouse event-based touch event emulation."""

    def __init__(self, enabled: bool, configuration: str=None):
        # Whether the touch event emulation should be enabled.
        self.enabled = enabled
        # Touch/gesture events configuration. Default: current platform.
        self.configuration = configuration



class setEmulatedMedia(ChromeCommand):
    """Emulates the given media for CSS media queries."""

    def __init__(self, media: str):
        # Media type to emulate. Empty string disables the override.
        self.media = media



class setCPUThrottlingRate(ChromeCommand):
    """Enables CPU throttling to emulate slow CPUs."""

    def __init__(self, rate: float):
        # Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        self.rate = rate



class canEmulate(ChromeCommand):
    """Tells whether emulation is supported."""

    def __init__(self): pass

class setVirtualTimePolicy(ChromeCommand):
    """Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget."""

    def __init__(self, policy: "VirtualTimePolicy", budget: int=None):
        self.policy = policy
        # If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
        self.budget = budget



