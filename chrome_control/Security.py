from enum import Enum
from typing import Any, List

from .base import ChromeCommand


# An internal certificate ID value.
CertificateId = int

SecurityState = Enum("SecurityState", "unknown neutral insecure warning secure info")
SecurityState.__doc__ = """The security level of a page or resource."""

class SecurityStateExplanation:
    """An explanation of an factor contributing to the security state."""
    def __init__(self, securityState: "SecurityState", summary: str, description: str, hasCertificate: bool):
        # Security state representing the severity of the factor being explained.
        self.securityState = securityState
        # Short phrase describing the type of factor.
        self.summary = summary
        # Full text explanation of the factor.
        self.description = description
        # True if the page has a certificate.
        self.hasCertificate = hasCertificate

class InsecureContentStatus:
    """Information about insecure content on the page."""
    def __init__(self, ranMixedContent: bool, displayedMixedContent: bool, ranContentWithCertErrors: bool, displayedContentWithCertErrors: bool, ranInsecureContentStyle: "SecurityState", displayedInsecureContentStyle: "SecurityState"):
        # True if the page was loaded over HTTPS and ran mixed (HTTP) content such as scripts.
        self.ranMixedContent = ranMixedContent
        # True if the page was loaded over HTTPS and displayed mixed (HTTP) content such as images.
        self.displayedMixedContent = displayedMixedContent
        # True if the page was loaded over HTTPS without certificate errors, and ran content such as scripts that were loaded with certificate errors.
        self.ranContentWithCertErrors = ranContentWithCertErrors
        # True if the page was loaded over HTTPS without certificate errors, and displayed content such as images that were loaded with certificate errors.
        self.displayedContentWithCertErrors = displayedContentWithCertErrors
        # Security state representing a page that ran insecure content.
        self.ranInsecureContentStyle = ranInsecureContentStyle
        # Security state representing a page that displayed insecure content.
        self.displayedInsecureContentStyle = displayedInsecureContentStyle

class enable(ChromeCommand):
    """Enables tracking security state changes."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables tracking security state changes."""

    def __init__(self): pass

class showCertificateViewer(ChromeCommand):
    """Displays native dialog with the certificate details."""

    def __init__(self): pass

