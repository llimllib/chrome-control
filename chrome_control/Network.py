from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import Page
from . import Runtime
from . import Security

# Unique loader identifier.
LoaderId = str

# Unique request identifier.
RequestId = str

# Number of seconds since epoch.
Timestamp = float

class Headers: pass

ConnectionType = Enum("ConnectionType", "none cellular2g cellular3g cellular4g bluetooth ethernet wifi wimax other")
ConnectionType.__doc__ = """Loading priority of a resource request."""

CookieSameSite = Enum("CookieSameSite", "Strict Lax")
CookieSameSite.__doc__ = """Represents the cookie's 'SameSite' status: https://tools.ietf.org/html/draft-west-first-party-cookies"""

class ResourceTiming:
    """Timing information for the request."""
    def __init__(self, requestTime: float, proxyStart: float, proxyEnd: float, dnsStart: float, dnsEnd: float, connectStart: float, connectEnd: float, sslStart: float, sslEnd: float, workerStart: float, workerReady: float, sendStart: float, sendEnd: float, pushStart: float, pushEnd: float, receiveHeadersEnd: float):
        # Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime.
        self.requestTime = requestTime
        # Started resolving proxy.
        self.proxyStart = proxyStart
        # Finished resolving proxy.
        self.proxyEnd = proxyEnd
        # Started DNS address resolve.
        self.dnsStart = dnsStart
        # Finished DNS address resolve.
        self.dnsEnd = dnsEnd
        # Started connecting to the remote host.
        self.connectStart = connectStart
        # Connected to the remote host.
        self.connectEnd = connectEnd
        # Started SSL handshake.
        self.sslStart = sslStart
        # Finished SSL handshake.
        self.sslEnd = sslEnd
        # Started running ServiceWorker.
        self.workerStart = workerStart
        # Finished Starting ServiceWorker.
        self.workerReady = workerReady
        # Started sending request.
        self.sendStart = sendStart
        # Finished sending request.
        self.sendEnd = sendEnd
        # Time the server started pushing request.
        self.pushStart = pushStart
        # Time the server finished pushing request.
        self.pushEnd = pushEnd
        # Finished receiving response headers.
        self.receiveHeadersEnd = receiveHeadersEnd

ResourcePriority = Enum("ResourcePriority", "VeryLow Low Medium High VeryHigh")
ResourcePriority.__doc__ = """Loading priority of a resource request."""

class Request:
    """HTTP request data."""
    def __init__(self, url: str, method: str, headers: "Headers", initialPriority: "ResourcePriority", referrerPolicy: str, postData: str=None, mixedContentType: str=None):
        # Request URL.
        self.url = url
        # HTTP request method.
        self.method = method
        # HTTP request headers.
        self.headers = headers
        # Priority of the resource request at the time request is sent.
        self.initialPriority = initialPriority
        # The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/
        self.referrerPolicy = referrerPolicy
        # HTTP POST request data.
        self.postData = postData
        # The mixed content status of the request, as defined in http://www.w3.org/TR/mixed-content/
        self.mixedContentType = mixedContentType

class SignedCertificateTimestamp:
    """Details of a signed certificate timestamp (SCT)."""
    def __init__(self, status: str, origin: str, logDescription: str, logId: str, timestamp: "Timestamp", hashAlgorithm: str, signatureAlgorithm: str, signatureData: str):
        # Validation status.
        self.status = status
        # Origin.
        self.origin = origin
        # Log name / description.
        self.logDescription = logDescription
        # Log ID.
        self.logId = logId
        # Issuance date.
        self.timestamp = timestamp
        # Hash algorithm.
        self.hashAlgorithm = hashAlgorithm
        # Signature algorithm.
        self.signatureAlgorithm = signatureAlgorithm
        # Signature data.
        self.signatureData = signatureData

class SecurityDetails:
    """Security details about a request."""
    def __init__(self, protocol: str, keyExchange: str, cipher: str, certificateId: "Security.CertificateId", subjectName: str, sanList: List, issuer: str, validFrom: "Timestamp", validTo: "Timestamp", signedCertificateTimestampList: List, keyExchangeGroup: str=None, mac: str=None):
        # Protocol name (e.g. "TLS 1.2" or "QUIC").
        self.protocol = protocol
        # Key Exchange used by the connection, or the empty string if not applicable.
        self.keyExchange = keyExchange
        # Cipher name.
        self.cipher = cipher
        # Certificate ID value.
        self.certificateId = certificateId
        # Certificate subject name.
        self.subjectName = subjectName
        # Subject Alternative Name (SAN) DNS names and IP addresses.
        self.sanList = sanList
        # Name of the issuing CA.
        self.issuer = issuer
        # Certificate valid from date.
        self.validFrom = validFrom
        # Certificate valid to (expiration) date
        self.validTo = validTo
        # List of signed certificate timestamps (SCTs).
        self.signedCertificateTimestampList = signedCertificateTimestampList
        # (EC)DH group used by the connection, if applicable.
        self.keyExchangeGroup = keyExchangeGroup
        # TLS MAC. Note that AEAD ciphers do not have separate MACs.
        self.mac = mac

BlockedReason = Enum("BlockedReason", "csp mixed-content origin inspector subresource-filter other")
BlockedReason.__doc__ = """The reason why request was blocked."""

class Response:
    """HTTP response data."""
    def __init__(self, url: str, status: float, statusText: str, headers: "Headers", mimeType: str, connectionReused: bool, connectionId: float, encodedDataLength: float, securityState: "Security.SecurityState", headersText: str=None, requestHeaders: "Headers"=None, requestHeadersText: str=None, remoteIPAddress: str=None, remotePort: int=None, fromDiskCache: bool=None, fromServiceWorker: bool=None, timing: "ResourceTiming"=None, protocol: str=None, securityDetails: "SecurityDetails"=None):
        # Response URL. This URL can be different from CachedResource.url in case of redirect.
        self.url = url
        # HTTP response status code.
        self.status = status
        # HTTP response status text.
        self.statusText = statusText
        # HTTP response headers.
        self.headers = headers
        # Resource mimeType as determined by the browser.
        self.mimeType = mimeType
        # Specifies whether physical connection was actually reused for this request.
        self.connectionReused = connectionReused
        # Physical connection id that was actually used for this request.
        self.connectionId = connectionId
        # Total number of bytes received for this request so far.
        self.encodedDataLength = encodedDataLength
        # Security state of the request resource.
        self.securityState = securityState
        # HTTP response headers text.
        self.headersText = headersText
        # Refined HTTP request headers that were actually transmitted over the network.
        self.requestHeaders = requestHeaders
        # HTTP request headers text.
        self.requestHeadersText = requestHeadersText
        # Remote IP address.
        self.remoteIPAddress = remoteIPAddress
        # Remote port.
        self.remotePort = remotePort
        # Specifies that the request was served from the disk cache.
        self.fromDiskCache = fromDiskCache
        # Specifies that the request was served from the ServiceWorker.
        self.fromServiceWorker = fromServiceWorker
        # Timing information for the given request.
        self.timing = timing
        # Protocol used to fetch this request.
        self.protocol = protocol
        # Security details for the request.
        self.securityDetails = securityDetails

class WebSocketRequest:
    """WebSocket request data."""
    def __init__(self, headers: "Headers"):
        # HTTP request headers.
        self.headers = headers

class WebSocketResponse:
    """WebSocket response data."""
    def __init__(self, status: float, statusText: str, headers: "Headers", headersText: str=None, requestHeaders: "Headers"=None, requestHeadersText: str=None):
        # HTTP response status code.
        self.status = status
        # HTTP response status text.
        self.statusText = statusText
        # HTTP response headers.
        self.headers = headers
        # HTTP response headers text.
        self.headersText = headersText
        # HTTP request headers.
        self.requestHeaders = requestHeaders
        # HTTP request headers text.
        self.requestHeadersText = requestHeadersText

class WebSocketFrame:
    """WebSocket frame data."""
    def __init__(self, opcode: float, mask: bool, payloadData: str):
        # WebSocket frame opcode.
        self.opcode = opcode
        # WebSocke frame mask.
        self.mask = mask
        # WebSocke frame payload data.
        self.payloadData = payloadData

class CachedResource:
    """Information about the cached resource."""
    def __init__(self, url: str, type: "Page.ResourceType", bodySize: float, response: "Response"=None):
        # Resource URL. This is the url of the original network request.
        self.url = url
        # Type of this resource.
        self.type = type
        # Cached response body size.
        self.bodySize = bodySize
        # Cached response data.
        self.response = response

class Initiator:
    """Information about the request initiator."""
    def __init__(self, type: str, stack: "Runtime.StackTrace"=None, url: str=None, lineNumber: float=None):
        # Type of this initiator.
        self.type = type
        # Initiator JavaScript stack trace, set for Script only.
        self.stack = stack
        # Initiator URL, set for Parser type only.
        self.url = url
        # Initiator line number, set for Parser type only (0-based).
        self.lineNumber = lineNumber

class Cookie:
    """Cookie object"""
    def __init__(self, name: str, value: str, domain: str, path: str, expires: float, size: int, httpOnly: bool, secure: bool, session: bool, sameSite: "CookieSameSite"=None):
        # Cookie name.
        self.name = name
        # Cookie value.
        self.value = value
        # Cookie domain.
        self.domain = domain
        # Cookie path.
        self.path = path
        # Cookie expiration date as the number of seconds since the UNIX epoch.
        self.expires = expires
        # Cookie size.
        self.size = size
        # True if cookie is http-only.
        self.httpOnly = httpOnly
        # True if cookie is secure.
        self.secure = secure
        # True in case of session cookie.
        self.session = session
        # Cookie SameSite type.
        self.sameSite = sameSite

class enable(ChromeCommand):
    """Enables network tracking, network events will now be delivered to the client."""

    def __init__(self, maxTotalBufferSize: int=None, maxResourceBufferSize: int=None):
        # Buffer size in bytes to use when preserving network payloads (XHRs, etc).
        self.maxTotalBufferSize = maxTotalBufferSize
        # Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        self.maxResourceBufferSize = maxResourceBufferSize



class disable(ChromeCommand):
    """Disables network tracking, prevents network events from being sent to the client."""

    def __init__(self): pass

class setUserAgentOverride(ChromeCommand):
    """Allows overriding user agent with the given string."""

    def __init__(self, userAgent: str):
        # User agent to use.
        self.userAgent = userAgent



class setExtraHTTPHeaders(ChromeCommand):
    """Specifies whether to always send extra HTTP headers with the requests from this page."""

    def __init__(self, headers: "Headers"):
        # Map with extra HTTP headers.
        self.headers = headers



class getResponseBody(ChromeCommand):
    """Returns content served for the given request."""

    def __init__(self, requestId: "RequestId"):
        # Identifier of the network request to get content for.
        self.requestId = requestId



class addBlockedURL(ChromeCommand):
    """Blocks specific URL from loading."""

    def __init__(self, url: str):
        # URL to block.
        self.url = url



class removeBlockedURL(ChromeCommand):
    """Cancels blocking of a specific URL from loading."""

    def __init__(self, url: str):
        # URL to stop blocking.
        self.url = url



class replayXHR(ChromeCommand):
    """This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password."""

    def __init__(self, requestId: "RequestId"):
        # Identifier of XHR to replay.
        self.requestId = requestId



class setMonitoringXHREnabled(ChromeCommand):
    """Toggles monitoring of XMLHttpRequest. If <code>true</code>, console will receive messages upon each XHR issued."""

    def __init__(self, enabled: bool):
        # Monitoring enabled state.
        self.enabled = enabled



class canClearBrowserCache(ChromeCommand):
    """Tells whether clearing browser cache is supported."""

    def __init__(self): pass

class clearBrowserCache(ChromeCommand):
    """Clears browser cache."""

    def __init__(self): pass

class canClearBrowserCookies(ChromeCommand):
    """Tells whether clearing browser cookies is supported."""

    def __init__(self): pass

class clearBrowserCookies(ChromeCommand):
    """Clears browser cookies."""

    def __init__(self): pass

class getCookies(ChromeCommand):
    """Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field."""

    def __init__(self): pass

class getAllCookies(ChromeCommand):
    """Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field."""

    def __init__(self): pass

class deleteCookie(ChromeCommand):
    """Deletes browser cookie with given name, domain and path."""

    def __init__(self, cookieName: str, url: str):
        # Name of the cookie to remove.
        self.cookieName = cookieName
        # URL to match cooke domain and path.
        self.url = url



class setCookie(ChromeCommand):
    """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist."""

    def __init__(self, url: str, name: str, value: str, domain: str=None, path: str=None, secure: bool=None, httpOnly: bool=None, sameSite: "CookieSameSite"=None, expirationDate: "Timestamp"=None):
        # The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
        self.url = url
        # The name of the cookie.
        self.name = name
        # The value of the cookie.
        self.value = value
        # If omitted, the cookie becomes a host-only cookie.
        self.domain = domain
        # Defaults to the path portion of the url parameter.
        self.path = path
        # Defaults ot false.
        self.secure = secure
        # Defaults to false.
        self.httpOnly = httpOnly
        # Defaults to browser default behavior.
        self.sameSite = sameSite
        # If omitted, the cookie becomes a session cookie.
        self.expirationDate = expirationDate



class canEmulateNetworkConditions(ChromeCommand):
    """Tells whether emulation of network conditions is supported."""

    def __init__(self): pass

class emulateNetworkConditions(ChromeCommand):
    """Activates emulation of network conditions."""

    def __init__(self, offline: bool, latency: float, downloadThroughput: float, uploadThroughput: float, connectionType: "ConnectionType"=None):
        # True to emulate internet disconnection.
        self.offline = offline
        # Additional latency (ms).
        self.latency = latency
        # Maximal aggregated download throughput.
        self.downloadThroughput = downloadThroughput
        # Maximal aggregated upload throughput.
        self.uploadThroughput = uploadThroughput
        # Connection type if known.
        self.connectionType = connectionType



class setCacheDisabled(ChromeCommand):
    """Toggles ignoring cache for each request. If <code>true</code>, cache will not be used."""

    def __init__(self, cacheDisabled: bool):
        # Cache disabled state.
        self.cacheDisabled = cacheDisabled



class setBypassServiceWorker(ChromeCommand):
    """Toggles ignoring of service worker for each request."""

    def __init__(self, bypass: bool):
        # Bypass service worker and load from network.
        self.bypass = bypass



class setDataSizeLimitsForTest(ChromeCommand):
    """For testing."""

    def __init__(self, maxTotalSize: int, maxResourceSize: int):
        # Maximum total buffer size.
        self.maxTotalSize = maxTotalSize
        # Maximum per-resource size.
        self.maxResourceSize = maxResourceSize



class getCertificate(ChromeCommand):
    """Returns the DER-encoded certificate."""

    def __init__(self, origin: str):
        # Origin to get certificate for.
        self.origin = origin



class resourceChangedPriority(ChromeEvent):
    """Fired when resource loading priority is changed"""

    def __init__(self, requestId: "RequestId", newPriority: "ResourcePriority", timestamp: "Timestamp"):
        # Request identifier.
        self.requestId = requestId
        # New priority
        self.newPriority = newPriority
        # Timestamp.
        self.timestamp = timestamp



class requestWillBeSent(ChromeEvent):
    """Fired when page is about to send HTTP request."""

    def __init__(self, requestId: "RequestId", frameId: "Page.FrameId", loaderId: "LoaderId", documentURL: str, request: "Request", timestamp: "Timestamp", wallTime: "Timestamp", initiator: "Initiator", redirectResponse: "Response"=None, type: "Page.ResourceType"=None):
        # Request identifier.
        self.requestId = requestId
        # Frame identifier.
        self.frameId = frameId
        # Loader identifier.
        self.loaderId = loaderId
        # URL of the document this request is loaded for.
        self.documentURL = documentURL
        # Request data.
        self.request = request
        # Timestamp.
        self.timestamp = timestamp
        # UTC Timestamp.
        self.wallTime = wallTime
        # Request initiator.
        self.initiator = initiator
        # Redirect response data.
        self.redirectResponse = redirectResponse
        # Type of this resource.
        self.type = type



class requestServedFromCache(ChromeEvent):
    """Fired if request ended up loading from cache."""

    def __init__(self, requestId: "RequestId"):
        # Request identifier.
        self.requestId = requestId



class responseReceived(ChromeEvent):
    """Fired when HTTP response is available."""

    def __init__(self, requestId: "RequestId", frameId: "Page.FrameId", loaderId: "LoaderId", timestamp: "Timestamp", type: "Page.ResourceType", response: "Response"):
        # Request identifier.
        self.requestId = requestId
        # Frame identifier.
        self.frameId = frameId
        # Loader identifier.
        self.loaderId = loaderId
        # Timestamp.
        self.timestamp = timestamp
        # Resource type.
        self.type = type
        # Response data.
        self.response = response



class dataReceived(ChromeEvent):
    """Fired when data chunk was received over the network."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", dataLength: int, encodedDataLength: int):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # Data chunk length.
        self.dataLength = dataLength
        # Actual bytes received (might be less than dataLength for compressed encodings).
        self.encodedDataLength = encodedDataLength



class loadingFinished(ChromeEvent):
    """Fired when HTTP request has finished loading."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", encodedDataLength: float):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # Total number of bytes received for this request.
        self.encodedDataLength = encodedDataLength



class loadingFailed(ChromeEvent):
    """Fired when HTTP request has failed to load."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", type: "Page.ResourceType", errorText: str, canceled: bool=None, blockedReason: "BlockedReason"=None):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # Resource type.
        self.type = type
        # User friendly error message.
        self.errorText = errorText
        # True if loading was canceled.
        self.canceled = canceled
        # The reason why loading was blocked, if any.
        self.blockedReason = blockedReason



class webSocketWillSendHandshakeRequest(ChromeEvent):
    """Fired when WebSocket is about to initiate handshake."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", wallTime: "Timestamp", request: "WebSocketRequest"):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # UTC Timestamp.
        self.wallTime = wallTime
        # WebSocket request data.
        self.request = request



class webSocketHandshakeResponseReceived(ChromeEvent):
    """Fired when WebSocket handshake response becomes available."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", response: "WebSocketResponse"):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # WebSocket response data.
        self.response = response



class webSocketCreated(ChromeEvent):
    """Fired upon WebSocket creation."""

    def __init__(self, requestId: "RequestId", url: str, initiator: "Initiator"=None):
        # Request identifier.
        self.requestId = requestId
        # WebSocket request URL.
        self.url = url
        # Request initiator.
        self.initiator = initiator



class webSocketClosed(ChromeEvent):
    """Fired when WebSocket is closed."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp"):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp



class webSocketFrameReceived(ChromeEvent):
    """Fired when WebSocket frame is received."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", response: "WebSocketFrame"):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # WebSocket response data.
        self.response = response



class webSocketFrameError(ChromeEvent):
    """Fired when WebSocket frame error occurs."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", errorMessage: str):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # WebSocket frame error message.
        self.errorMessage = errorMessage



class webSocketFrameSent(ChromeEvent):
    """Fired when WebSocket frame is sent."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", response: "WebSocketFrame"):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # WebSocket response data.
        self.response = response



class eventSourceMessageReceived(ChromeEvent):
    """Fired when EventSource message is received."""

    def __init__(self, requestId: "RequestId", timestamp: "Timestamp", eventName: str, eventId: str, data: str):
        # Request identifier.
        self.requestId = requestId
        # Timestamp.
        self.timestamp = timestamp
        # Message type.
        self.eventName = eventName
        # Message identifier.
        self.eventId = eventId
        # Message content.
        self.data = data



