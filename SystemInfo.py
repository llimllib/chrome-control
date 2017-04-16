from enum import Enum
from typing import Any, List

from base import ChromeCommand


class GPUDevice:
    """Describes a single graphics processor (GPU)."""
    def __init__(self, vendorId: float, deviceId: float, vendorString: str, deviceString: str):
        # PCI ID of the GPU vendor, if available; 0 otherwise.
        self.vendorId = vendorId
        # PCI ID of the GPU device, if available; 0 otherwise.
        self.deviceId = deviceId
        # String description of the GPU vendor, if the PCI ID is not available.
        self.vendorString = vendorString
        # String description of the GPU device, if the PCI ID is not available.
        self.deviceString = deviceString

class GPUInfo:
    """Provides information about the GPU(s) on the system."""
    def __init__(self, devices: List, driverBugWorkarounds: List, auxAttributes: dict=None, featureStatus: dict=None):
        # The graphics devices on the system. Element 0 is the primary GPU.
        self.devices = devices
        # An optional array of GPU driver bug workarounds.
        self.driverBugWorkarounds = driverBugWorkarounds
        # An optional dictionary of additional GPU related attributes.
        self.auxAttributes = auxAttributes
        # An optional dictionary of graphics features and their status.
        self.featureStatus = featureStatus

class getInfo(ChromeCommand):
    """Returns information about the system."""

    def __init__(self): pass

