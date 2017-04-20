from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


class MemoryDumpConfig: pass

class TraceConfig:
    def __init__(self, recordMode: str=None, enableSampling: bool=None, enableSystrace: bool=None, enableArgumentFilter: bool=None, includedCategories: List=None, excludedCategories: List=None, syntheticDelays: List=None, memoryDumpConfig: "MemoryDumpConfig"=None):
        # Controls how the trace buffer stores data.
        self.recordMode = recordMode
        # Turns on JavaScript stack sampling.
        self.enableSampling = enableSampling
        # Turns on system tracing.
        self.enableSystrace = enableSystrace
        # Turns on argument filter.
        self.enableArgumentFilter = enableArgumentFilter
        # Included category filters.
        self.includedCategories = includedCategories
        # Excluded category filters.
        self.excludedCategories = excludedCategories
        # Configuration to synthesize the delays in tracing.
        self.syntheticDelays = syntheticDelays
        # Configuration for memory dump triggers. Used only when "memory-infra" category is enabled.
        self.memoryDumpConfig = memoryDumpConfig

class start(ChromeCommand):
    """Start trace events collection."""

    def __init__(self, categories: str=None, options: str=None, bufferUsageReportingInterval: float=None, transferMode: str=None, traceConfig: "TraceConfig"=None):
        # Category/tag filter
        self.categories = categories
        # Tracing options
        self.options = options
        # If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        self.bufferUsageReportingInterval = bufferUsageReportingInterval
        # Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to <code>ReportEvents</code>).
        self.transferMode = transferMode
        # 
        self.traceConfig = traceConfig



class end(ChromeCommand):
    """Stop trace events collection."""

    def __init__(self): pass

class getCategories(ChromeCommand):
    """Gets supported tracing categories."""

    def __init__(self): pass

class requestMemoryDump(ChromeCommand):
    """Request a global memory dump."""

    def __init__(self): pass

class recordClockSyncMarker(ChromeCommand):
    """Record a clock sync marker in the trace."""

    def __init__(self, syncId: str):
        # The ID of this clock sync marker
        self.syncId = syncId



class dataCollected(ChromeEvent):
    """Contains an bucket of collected trace events. When tracing is stopped collected events will be send as a sequence of dataCollected events followed by tracingComplete event."""

    def __init__(self, value: List):
        self.value = value



class tracingComplete(ChromeEvent):
    """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""

    def __init__(self, stream: "IO.StreamHandle"=None):
        # A handle of the stream that holds resulting trace data.
        self.stream = stream



class bufferUsage(ChromeEvent):
    def __init__(self, percentFull: float=None, eventCount: float=None, value: float=None):
        # A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        self.percentFull = percentFull
        # An approximate number of events in the trace log.
        self.eventCount = eventCount
        # A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        self.value = value



