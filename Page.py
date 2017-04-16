from enum import Enum
from typing import Any, List

from base import ChromeCommand

import Network

ResourceType = Enum("ResourceType", "Document Stylesheet Image Media Font Script TextTrack XHR Fetch EventSource WebSocket Manifest Other")
ResourceType.__doc__ = "Resource type as it was perceived by the rendering engine."

# Unique frame identifier.
FrameId = str

class Frame:
    """Information about the Frame on the page."""
    def __init__(self, id: str, loaderId: "Network.LoaderId", url: str, securityOrigin: str, mimeType: str, parentId: str=None, name: str=None):
        # Frame unique identifier.
        self.id = id
        # Identifier of the loader associated with this frame.
        self.loaderId = loaderId
        # Frame document's URL.
        self.url = url
        # Frame document's security origin.
        self.securityOrigin = securityOrigin
        # Frame document's mimeType as determined by the browser.
        self.mimeType = mimeType
        # Parent frame identifier.
        self.parentId = parentId
        # Frame's name as specified in the tag.
        self.name = name

class FrameResource:
    """Information about the Resource on the page."""
    def __init__(self, url: str, type: "ResourceType", mimeType: str, lastModified: "Network.Timestamp"=None, contentSize: float=None, failed: bool=None, canceled: bool=None):
        # Resource URL.
        self.url = url
        # Type of this resource.
        self.type = type
        # Resource mimeType as determined by the browser.
        self.mimeType = mimeType
        # last-modified timestamp as reported by server.
        self.lastModified = lastModified
        # Resource content size.
        self.contentSize = contentSize
        # True if the resource failed to load.
        self.failed = failed
        # True if the resource was canceled during loading.
        self.canceled = canceled

class FrameResourceTree:
    """Information about the Frame hierarchy along with their cached resources."""
    def __init__(self, frame: "Frame", resources: List, childFrames: List=None):
        # Frame information for this tree item.
        self.frame = frame
        # Information about frame resources.
        self.resources = resources
        # Child frames.
        self.childFrames = childFrames

# Unique script identifier.
ScriptIdentifier = str

class NavigationEntry:
    """Navigation history entry."""
    def __init__(self, id: int, url: str, title: str):
        # Unique id of the navigation history entry.
        self.id = id
        # URL of the navigation history entry.
        self.url = url
        # Title of the navigation history entry.
        self.title = title

class ScreencastFrameMetadata:
    """Screencast frame metadata."""
    def __init__(self, offsetTop: float, pageScaleFactor: float, deviceWidth: float, deviceHeight: float, scrollOffsetX: float, scrollOffsetY: float, timestamp: float=None):
        # Top offset in DIP.
        self.offsetTop = offsetTop
        # Page scale factor.
        self.pageScaleFactor = pageScaleFactor
        # Device screen width in DIP.
        self.deviceWidth = deviceWidth
        # Device screen height in DIP.
        self.deviceHeight = deviceHeight
        # Position of horizontal scroll in CSS pixels.
        self.scrollOffsetX = scrollOffsetX
        # Position of vertical scroll in CSS pixels.
        self.scrollOffsetY = scrollOffsetY
        # Frame swap timestamp.
        self.timestamp = timestamp

DialogType = Enum("DialogType", "alert confirm prompt beforeunload")
DialogType.__doc__ = "Javascript dialog type."

class AppManifestError:
    """Error while paring app manifest."""
    def __init__(self, message: str, critical: int, line: int, column: int):
        # Error message.
        self.message = message
        # If criticial, this is a non-recoverable parse error.
        self.critical = critical
        # Error line.
        self.line = line
        # Error column.
        self.column = column

NavigationResponse = Enum("NavigationResponse", "Proceed Cancel CancelAndIgnore")
NavigationResponse.__doc__ = "Proceed: allow the navigation; Cancel: cancel the navigation; CancelAndIgnore: cancels the navigation and makes the requester of the navigation acts like the request was never made."

class LayoutViewport:
    """Layout viewport position and dimensions."""
    def __init__(self, pageX: int, pageY: int, clientWidth: int, clientHeight: int):
        # Horizontal offset relative to the document (CSS pixels).
        self.pageX = pageX
        # Vertical offset relative to the document (CSS pixels).
        self.pageY = pageY
        # Width (CSS pixels), excludes scrollbar if present.
        self.clientWidth = clientWidth
        # Height (CSS pixels), excludes scrollbar if present.
        self.clientHeight = clientHeight

class VisualViewport:
    """Visual viewport position, dimensions, and scale."""
    def __init__(self, offsetX: float, offsetY: float, pageX: float, pageY: float, clientWidth: float, clientHeight: float, scale: float):
        # Horizontal offset relative to the layout viewport (CSS pixels).
        self.offsetX = offsetX
        # Vertical offset relative to the layout viewport (CSS pixels).
        self.offsetY = offsetY
        # Horizontal offset relative to the document (CSS pixels).
        self.pageX = pageX
        # Vertical offset relative to the document (CSS pixels).
        self.pageY = pageY
        # Width (CSS pixels), excludes scrollbar if present.
        self.clientWidth = clientWidth
        # Height (CSS pixels), excludes scrollbar if present.
        self.clientHeight = clientHeight
        # Scale relative to the ideal viewport (size at width=device-width).
        self.scale = scale

class enable(ChromeCommand):
    """Enables page domain notifications."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables page domain notifications."""

    def __init__(self): pass

class addScriptToEvaluateOnLoad(ChromeCommand):
    def __init__(self, scriptSource: str):
        self.scriptSource = scriptSource



class removeScriptToEvaluateOnLoad(ChromeCommand):
    def __init__(self, identifier: "ScriptIdentifier"):
        self.identifier = identifier



class setAutoAttachToCreatedPages(ChromeCommand):
    """Controls whether browser will open a new inspector window for connected pages."""

    def __init__(self, autoAttach: bool):
        # If true, browser will open a new inspector window for every page created from this one.
        self.autoAttach = autoAttach



class reload(ChromeCommand):
    """Reloads given page optionally ignoring the cache."""

    def __init__(self, ignoreCache: bool=None, scriptToEvaluateOnLoad: str=None):
        # If true, browser cache is ignored (as if the user pressed Shift+refresh).
        self.ignoreCache = ignoreCache
        # If set, the script will be injected into all frames of the inspected page after reload.
        self.scriptToEvaluateOnLoad = scriptToEvaluateOnLoad



class navigate(ChromeCommand):
    """Navigates current page to the given URL."""

    def __init__(self, url: str):
        # URL to navigate the page to.
        self.url = url



class stopLoading(ChromeCommand):
    """Force the page stop all navigations and pending resource fetches."""

    def __init__(self): pass

class getNavigationHistory(ChromeCommand):
    """Returns navigation history for the current page."""

    def __init__(self): pass

class navigateToHistoryEntry(ChromeCommand):
    """Navigates current page to the given history entry."""

    def __init__(self, entryId: int):
        # Unique id of the entry to navigate to.
        self.entryId = entryId



class getCookies(ChromeCommand):
    """Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field."""

    def __init__(self): pass

class deleteCookie(ChromeCommand):
    """Deletes browser cookie with given name, domain and path."""

    def __init__(self, cookieName: str, url: str):
        # Name of the cookie to remove.
        self.cookieName = cookieName
        # URL to match cooke domain and path.
        self.url = url



class getResourceTree(ChromeCommand):
    """Returns present frame / resource tree structure."""

    def __init__(self): pass

class getResourceContent(ChromeCommand):
    """Returns content of the given resource."""

    def __init__(self, frameId: "FrameId", url: str):
        # Frame id to get resource for.
        self.frameId = frameId
        # URL of the resource to get content for.
        self.url = url



class searchInResource(ChromeCommand):
    """Searches for given string in resource content."""

    def __init__(self, frameId: "FrameId", url: str, query: str, caseSensitive: bool=None, isRegex: bool=None):
        # Frame id for resource to search in.
        self.frameId = frameId
        # URL of the resource to search in.
        self.url = url
        # String to search for.
        self.query = query
        # If true, search is case sensitive.
        self.caseSensitive = caseSensitive
        # If true, treats string parameter as regex.
        self.isRegex = isRegex



class setDocumentContent(ChromeCommand):
    """Sets given markup as the document's HTML."""

    def __init__(self, frameId: "FrameId", html: str):
        # Frame id to set HTML for.
        self.frameId = frameId
        # HTML content to set.
        self.html = html



class setDeviceMetricsOverride(ChromeCommand):
    """Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results)."""

    def __init__(self, width: int, height: int, deviceScaleFactor: float, mobile: bool, fitWindow: bool, scale: float=None, offsetX: float=None, offsetY: float=None, screenWidth: int=None, screenHeight: int=None, positionX: int=None, positionY: int=None, screenOrientation: "Emulation.ScreenOrientation"=None):
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
        # X offset to shift resulting view image by. Ignored in |fitWindow| mode.
        self.offsetX = offsetX
        # Y offset to shift resulting view image by. Ignored in |fitWindow| mode.
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

class setDeviceOrientationOverride(ChromeCommand):
    """Overrides the Device Orientation."""

    def __init__(self, alpha: float, beta: float, gamma: float):
        # Mock alpha
        self.alpha = alpha
        # Mock beta
        self.beta = beta
        # Mock gamma
        self.gamma = gamma



class clearDeviceOrientationOverride(ChromeCommand):
    """Clears the overridden Device Orientation."""

    def __init__(self): pass

class setTouchEmulationEnabled(ChromeCommand):
    """Toggles mouse event-based touch event emulation."""

    def __init__(self, enabled: bool, configuration: str=None):
        # Whether the touch event emulation should be enabled.
        self.enabled = enabled
        # Touch/gesture events configuration. Default: current platform.
        self.configuration = configuration



class captureScreenshot(ChromeCommand):
    """Capture page screenshot."""

    def __init__(self): pass

class startScreencast(ChromeCommand):
    """Starts sending each frame using the <code>screencastFrame</code> event."""

    def __init__(self, format: str=None, quality: int=None, maxWidth: int=None, maxHeight: int=None, everyNthFrame: int=None):
        # Image compression format.
        self.format = format
        # Compression quality from range [0..100].
        self.quality = quality
        # Maximum screenshot width.
        self.maxWidth = maxWidth
        # Maximum screenshot height.
        self.maxHeight = maxHeight
        # Send every n-th frame.
        self.everyNthFrame = everyNthFrame



class stopScreencast(ChromeCommand):
    """Stops sending each frame in the <code>screencastFrame</code>."""

    def __init__(self): pass

class screencastFrameAck(ChromeCommand):
    """Acknowledges that a screencast frame has been received by the frontend."""

    def __init__(self, sessionId: int):
        # Frame number.
        self.sessionId = sessionId



class handleJavaScriptDialog(ChromeCommand):
    """Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload)."""

    def __init__(self, accept: bool, promptText: str=None):
        # Whether to accept or dismiss the dialog.
        self.accept = accept
        # The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
        self.promptText = promptText



class setColorPickerEnabled(ChromeCommand):
    """Shows / hides color picker"""

    def __init__(self, enabled: bool):
        # Shows / hides color picker
        self.enabled = enabled



class configureOverlay(ChromeCommand):
    """Configures overlay."""

    def __init__(self, suspended: bool=None, message: str=None):
        # Whether overlay should be suspended and not consume any resources.
        self.suspended = suspended
        # Overlay message to display.
        self.message = message



class getAppManifest(ChromeCommand):
    def __init__(self): pass

class requestAppBanner(ChromeCommand):
    def __init__(self): pass

class setControlNavigations(ChromeCommand):
    """Toggles navigation throttling which allows programatic control over navigation and redirect response."""

    def __init__(self, enabled: bool):
        self.enabled = enabled



class processNavigation(ChromeCommand):
    """Should be sent in response to a navigationRequested or a redirectRequested event, telling the browser how to handle the navigation."""

    def __init__(self, response: "NavigationResponse", navigationId: int):
        self.response = response
        self.navigationId = navigationId



class getLayoutMetrics(ChromeCommand):
    """Returns metrics relating to the layouting of the page, such as viewport bounds/scale."""

    def __init__(self): pass

