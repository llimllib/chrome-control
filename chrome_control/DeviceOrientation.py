from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent


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

