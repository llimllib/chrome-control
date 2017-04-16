from enum import Enum
from typing import Any, List

from base import ChromeCommand


# Unique identifier of the Cache object.
CacheId = str

class DataEntry:
    """Data entry."""
    def __init__(self, request: str, response: str):
        # Request url spec.
        self.request = request
        # Response stataus text.
        self.response = response

class Cache:
    """Cache identifier."""
    def __init__(self, cacheId: "CacheId", securityOrigin: str, cacheName: str):
        # An opaque unique id of the cache.
        self.cacheId = cacheId
        # Security origin of the cache.
        self.securityOrigin = securityOrigin
        # The name of the cache.
        self.cacheName = cacheName

class requestCacheNames(ChromeCommand):
    """Requests cache names."""

    def __init__(self, securityOrigin: str):
        # Security origin.
        self.securityOrigin = securityOrigin



class requestEntries(ChromeCommand):
    """Requests data from cache."""

    def __init__(self, cacheId: "CacheId", skipCount: int, pageSize: int):
        # ID of cache to get entries from.
        self.cacheId = cacheId
        # Number of records to skip.
        self.skipCount = skipCount
        # Number of records to fetch.
        self.pageSize = pageSize



class deleteCache(ChromeCommand):
    """Deletes a cache."""

    def __init__(self, cacheId: "CacheId"):
        # Id of cache for deletion.
        self.cacheId = cacheId



class deleteEntry(ChromeCommand):
    """Deletes a cache entry."""

    def __init__(self, cacheId: "CacheId", request: str):
        # Id of cache where the entry will be deleted.
        self.cacheId = cacheId
        # URL spec of the request.
        self.request = request



