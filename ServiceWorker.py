from enum import Enum
from typing import Any, List

from base import ChromeCommand

import Target

class ServiceWorkerRegistration:
    """ServiceWorker registration."""
    def __init__(self, registrationId: str, scopeURL: str, isDeleted: bool):
        self.registrationId = registrationId
        self.scopeURL = scopeURL
        self.isDeleted = isDeleted

ServiceWorkerVersionRunningStatus = Enum("ServiceWorkerVersionRunningStatus", "stopped starting running stopping")
ServiceWorkerVersionRunningStatus.__doc__ = ""

ServiceWorkerVersionStatus = Enum("ServiceWorkerVersionStatus", "new installing installed activating activated redundant")
ServiceWorkerVersionStatus.__doc__ = ""

class ServiceWorkerVersion:
    """ServiceWorker version."""
    def __init__(self, versionId: str, registrationId: str, scriptURL: str, runningStatus: "ServiceWorkerVersionRunningStatus", status: "ServiceWorkerVersionStatus", scriptLastModified: float=None, scriptResponseTime: float=None, controlledClients: List=None, targetId: "Target.TargetID"=None):
        self.versionId = versionId
        self.registrationId = registrationId
        self.scriptURL = scriptURL
        self.runningStatus = runningStatus
        self.status = status
        # The Last-Modified header value of the main script.
        self.scriptLastModified = scriptLastModified
        # The time at which the response headers of the main script were received from the server.  For cached script it is the last time the cache entry was validated.
        self.scriptResponseTime = scriptResponseTime
        self.controlledClients = controlledClients
        self.targetId = targetId

class ServiceWorkerErrorMessage:
    """ServiceWorker error message."""
    def __init__(self, errorMessage: str, registrationId: str, versionId: str, sourceURL: str, lineNumber: int, columnNumber: int):
        self.errorMessage = errorMessage
        self.registrationId = registrationId
        self.versionId = versionId
        self.sourceURL = sourceURL
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

class enable(ChromeCommand):
    def __init__(self): pass

class disable(ChromeCommand):
    def __init__(self): pass

class unregister(ChromeCommand):
    def __init__(self, scopeURL: str):
        self.scopeURL = scopeURL



class updateRegistration(ChromeCommand):
    def __init__(self, scopeURL: str):
        self.scopeURL = scopeURL



class startWorker(ChromeCommand):
    def __init__(self, scopeURL: str):
        self.scopeURL = scopeURL



class skipWaiting(ChromeCommand):
    def __init__(self, scopeURL: str):
        self.scopeURL = scopeURL



class stopWorker(ChromeCommand):
    def __init__(self, versionId: str):
        self.versionId = versionId



class inspectWorker(ChromeCommand):
    def __init__(self, versionId: str):
        self.versionId = versionId



class setForceUpdateOnPageLoad(ChromeCommand):
    def __init__(self, forceUpdateOnPageLoad: bool):
        self.forceUpdateOnPageLoad = forceUpdateOnPageLoad



class deliverPushMessage(ChromeCommand):
    def __init__(self, origin: str, registrationId: str, data: str):
        self.origin = origin
        self.registrationId = registrationId
        self.data = data



class dispatchSyncEvent(ChromeCommand):
    def __init__(self, origin: str, registrationId: str, tag: str, lastChance: bool):
        self.origin = origin
        self.registrationId = registrationId
        self.tag = tag
        self.lastChance = lastChance



