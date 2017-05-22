from enum import Enum
from typing import Any, List

from .base import ChromeCommand

from . import DOM

# Unique accessibility node identifier.
AXNodeId = str

AXValueType = Enum("AXValueType", "boolean tristate booleanOrUndefined idref idrefList integer node nodeList number string computedString token tokenList domRelation role internalRole valueUndefined")
AXValueType.__doc__ = """Enum of possible property types."""

AXValueSourceType = Enum("AXValueSourceType", "attribute implicit style contents placeholder relatedElement")
AXValueSourceType.__doc__ = """Enum of possible property sources."""

AXValueNativeSourceType = Enum("AXValueNativeSourceType", "figcaption label labelfor labelwrapped legend tablecaption title other")
AXValueNativeSourceType.__doc__ = """Enum of possible native property sources (as a subtype of a particular AXValueSourceType)."""

class AXValueSource:
    """A single source for a computed AX property."""
    def __init__(self, type: "AXValueSourceType", value: "AXValue"=None, attribute: str=None, attributeValue: "AXValue"=None, superseded: bool=None, nativeSource: "AXValueNativeSourceType"=None, nativeSourceValue: "AXValue"=None, invalid: bool=None, invalidReason: str=None):
        # What type of source this is.
        self.type = type
        # The value of this property source.
        self.value = value
        # The name of the relevant attribute, if any.
        self.attribute = attribute
        # The value of the relevant attribute, if any.
        self.attributeValue = attributeValue
        # Whether this source is superseded by a higher priority source.
        self.superseded = superseded
        # The native markup source for this value, e.g. a <label> element.
        self.nativeSource = nativeSource
        # The value, such as a node or node list, of the native source.
        self.nativeSourceValue = nativeSourceValue
        # Whether the value for this property is invalid.
        self.invalid = invalid
        # Reason for the value being invalid, if it is.
        self.invalidReason = invalidReason

class AXRelatedNode:
    def __init__(self, backendDOMNodeId: "DOM.BackendNodeId", idref: str=None, text: str=None):
        # The BackendNodeId of the related DOM node.
        self.backendDOMNodeId = backendDOMNodeId
        # The IDRef value provided, if any.
        self.idref = idref
        # The text alternative of this node in the current context.
        self.text = text

class AXProperty:
    def __init__(self, name: str, value: "AXValue"):
        # The name of this property.
        self.name = name
        # The value of this property.
        self.value = value

class AXValue:
    """A single computed AX property."""
    def __init__(self, type: "AXValueType", value: Any=None, relatedNodes: List=None, sources: List=None):
        # The type of this value.
        self.type = type
        # The computed value of this property.
        self.value = value
        # One or more related nodes, if applicable.
        self.relatedNodes = relatedNodes
        # The sources which contributed to the computation of this property.
        self.sources = sources

AXGlobalStates = Enum("AXGlobalStates", "disabled hidden hiddenRoot invalid")
AXGlobalStates.__doc__ = """States which apply to every AX node."""

AXLiveRegionAttributes = Enum("AXLiveRegionAttributes", "live atomic relevant busy root")
AXLiveRegionAttributes.__doc__ = """Attributes which apply to nodes in live regions."""

AXWidgetAttributes = Enum("AXWidgetAttributes", "autocomplete haspopup level multiselectable orientation multiline readonly required valuemin valuemax valuetext")
AXWidgetAttributes.__doc__ = """Attributes which apply to widgets."""

AXWidgetStates = Enum("AXWidgetStates", "checked expanded pressed selected")
AXWidgetStates.__doc__ = """States which apply to widgets."""

AXRelationshipAttributes = Enum("AXRelationshipAttributes", "activedescendant flowto controls describedby labelledby owns")
AXRelationshipAttributes.__doc__ = """Relationships between elements other than parent/child/sibling."""

class AXNode:
    """A node in the accessibility tree."""
    def __init__(self, nodeId: "AXNodeId", ignored: bool, ignoredReasons: List=None, role: "AXValue"=None, name: "AXValue"=None, description: "AXValue"=None, value: "AXValue"=None, properties: List=None, childIds: List=None, backendDOMNodeId: "DOM.BackendNodeId"=None):
        # Unique identifier for this node.
        self.nodeId = nodeId
        # Whether this node is ignored for accessibility
        self.ignored = ignored
        # Collection of reasons why this node is hidden.
        self.ignoredReasons = ignoredReasons
        # This <code>Node</code>'s role, whether explicit or implicit.
        self.role = role
        # The accessible name for this <code>Node</code>.
        self.name = name
        # The accessible description for this <code>Node</code>.
        self.description = description
        # The value for this <code>Node</code>.
        self.value = value
        # All other properties
        self.properties = properties
        # IDs for each of this node's child nodes.
        self.childIds = childIds
        # The backend ID for the associated DOM node, if any.
        self.backendDOMNodeId = backendDOMNodeId

class getPartialAXTree(ChromeCommand):
    """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists."""

    def __init__(self, nodeId: "DOM.NodeId", fetchRelatives: bool=None):
        # ID of node to get the partial accessibility tree for.
        self.nodeId = nodeId
        # Whether to fetch this nodes ancestors, siblings and children. Defaults to true.
        self.fetchRelatives = fetchRelatives



