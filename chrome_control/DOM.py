from enum import Enum
from typing import Any, List

from .base import ChromeCommand

from . import Page

# Unique DOM node identifier.
NodeId = int

# Unique DOM node identifier used to reference a node that may not have been pushed to the front-end.
BackendNodeId = int

class BackendNode:
    """Backend node with a friendly name."""
    def __init__(self, nodeType: int, nodeName: str, backendNodeId: "BackendNodeId"):
        # <code>Node</code>'s nodeType.
        self.nodeType = nodeType
        # <code>Node</code>'s nodeName.
        self.nodeName = nodeName
        self.backendNodeId = backendNodeId

PseudoType = Enum("PseudoType", "first-line first-letter before after backdrop selection first-line-inherited scrollbar scrollbar-thumb scrollbar-button scrollbar-track scrollbar-track-piece scrollbar-corner resizer input-list-button")
PseudoType.__doc__ = """Pseudo element type."""

ShadowRootType = Enum("ShadowRootType", "user-agent open closed")
ShadowRootType.__doc__ = """Shadow root type."""

class Node:
    """DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes. DOMNode is a base node mirror type."""
    def __init__(self, nodeId: "NodeId", backendNodeId: "BackendNodeId", nodeType: int, nodeName: str, localName: str, nodeValue: str, childNodeCount: int=None, children: List=None, attributes: List=None, documentURL: str=None, baseURL: str=None, publicId: str=None, systemId: str=None, internalSubset: str=None, xmlVersion: str=None, name: str=None, value: str=None, pseudoType: "PseudoType"=None, shadowRootType: "ShadowRootType"=None, frameId: "Page.FrameId"=None, contentDocument: "Node"=None, shadowRoots: List=None, templateContent: "Node"=None, pseudoElements: List=None, importedDocument: "Node"=None, distributedNodes: List=None, isSVG: bool=None):
        # Node identifier that is passed into the rest of the DOM messages as the <code>nodeId</code>. Backend will only push node with given <code>id</code> once. It is aware of all requested nodes and will only fire DOM events for nodes known to the client.
        self.nodeId = nodeId
        # The BackendNodeId for this node.
        self.backendNodeId = backendNodeId
        # <code>Node</code>'s nodeType.
        self.nodeType = nodeType
        # <code>Node</code>'s nodeName.
        self.nodeName = nodeName
        # <code>Node</code>'s localName.
        self.localName = localName
        # <code>Node</code>'s nodeValue.
        self.nodeValue = nodeValue
        # Child count for <code>Container</code> nodes.
        self.childNodeCount = childNodeCount
        # Child nodes of this node when requested with children.
        self.children = children
        # Attributes of the <code>Element</code> node in the form of flat array <code>[name1, value1, name2, value2]</code>.
        self.attributes = attributes
        # Document URL that <code>Document</code> or <code>FrameOwner</code> node points to.
        self.documentURL = documentURL
        # Base URL that <code>Document</code> or <code>FrameOwner</code> node uses for URL completion.
        self.baseURL = baseURL
        # <code>DocumentType</code>'s publicId.
        self.publicId = publicId
        # <code>DocumentType</code>'s systemId.
        self.systemId = systemId
        # <code>DocumentType</code>'s internalSubset.
        self.internalSubset = internalSubset
        # <code>Document</code>'s XML version in case of XML documents.
        self.xmlVersion = xmlVersion
        # <code>Attr</code>'s name.
        self.name = name
        # <code>Attr</code>'s value.
        self.value = value
        # Pseudo element type for this node.
        self.pseudoType = pseudoType
        # Shadow root type.
        self.shadowRootType = shadowRootType
        # Frame ID for frame owner elements.
        self.frameId = frameId
        # Content document for frame owner elements.
        self.contentDocument = contentDocument
        # Shadow root list for given element host.
        self.shadowRoots = shadowRoots
        # Content document fragment for template elements.
        self.templateContent = templateContent
        # Pseudo elements associated with this node.
        self.pseudoElements = pseudoElements
        # Import document for the HTMLImport links.
        self.importedDocument = importedDocument
        # Distributed nodes for given insertion point.
        self.distributedNodes = distributedNodes
        # Whether the node is SVG.
        self.isSVG = isSVG

class RGBA:
    """A structure holding an RGBA color."""
    def __init__(self, r: int, g: int, b: int, a: float=None):
        # The red component, in the [0-255] range.
        self.r = r
        # The green component, in the [0-255] range.
        self.g = g
        # The blue component, in the [0-255] range.
        self.b = b
        # The alpha component, in the [0-1] range (default: 1).
        self.a = a

# An array of quad vertices, x immediately followed by y for each point, points clock-wise.
Quad = List[float]
class BoxModel:
    """Box model."""
    def __init__(self, content: "Quad", padding: "Quad", border: "Quad", margin: "Quad", width: int, height: int, shapeOutside: "ShapeOutsideInfo"=None):
        # Content box
        self.content = content
        # Padding box
        self.padding = padding
        # Border box
        self.border = border
        # Margin box
        self.margin = margin
        # Node width
        self.width = width
        # Node height
        self.height = height
        # Shape outside coordinates
        self.shapeOutside = shapeOutside

class ShapeOutsideInfo:
    """CSS Shape Outside details."""
    def __init__(self, bounds: "Quad", shape: List, marginShape: List):
        # Shape bounds
        self.bounds = bounds
        # Shape coordinate details
        self.shape = shape
        # Margin shape bounds
        self.marginShape = marginShape

class Rect:
    """Rectangle."""
    def __init__(self, x: float, y: float, width: float, height: float):
        # X coordinate
        self.x = x
        # Y coordinate
        self.y = y
        # Rectangle width
        self.width = width
        # Rectangle height
        self.height = height

class HighlightConfig:
    """Configuration data for the highlighting of page elements."""
    def __init__(self, showInfo: bool=None, showRulers: bool=None, showExtensionLines: bool=None, displayAsMaterial: bool=None, contentColor: "RGBA"=None, paddingColor: "RGBA"=None, borderColor: "RGBA"=None, marginColor: "RGBA"=None, eventTargetColor: "RGBA"=None, shapeColor: "RGBA"=None, shapeMarginColor: "RGBA"=None, selectorList: str=None):
        # Whether the node info tooltip should be shown (default: false).
        self.showInfo = showInfo
        # Whether the rulers should be shown (default: false).
        self.showRulers = showRulers
        # Whether the extension lines from node to the rulers should be shown (default: false).
        self.showExtensionLines = showExtensionLines
        self.displayAsMaterial = displayAsMaterial
        # The content box highlight fill color (default: transparent).
        self.contentColor = contentColor
        # The padding highlight fill color (default: transparent).
        self.paddingColor = paddingColor
        # The border highlight fill color (default: transparent).
        self.borderColor = borderColor
        # The margin highlight fill color (default: transparent).
        self.marginColor = marginColor
        # The event target element highlight fill color (default: transparent).
        self.eventTargetColor = eventTargetColor
        # The shape outside fill color (default: transparent).
        self.shapeColor = shapeColor
        # The shape margin fill color (default: transparent).
        self.shapeMarginColor = shapeMarginColor
        # Selectors to highlight relevant nodes.
        self.selectorList = selectorList

InspectMode = Enum("InspectMode", "searchForNode searchForUAShadowDOM none")
InspectMode.__doc__ = """"""

class enable(ChromeCommand):
    """Enables DOM agent for the given page."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables DOM agent for the given page."""

    def __init__(self): pass

class getDocument(ChromeCommand):
    """Returns the root DOM node (and optionally the subtree) to the caller."""

    def __init__(self, depth: int=None, pierce: bool=None):
        # The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        self.depth = depth
        # Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        self.pierce = pierce



class collectClassNamesFromSubtree(ChromeCommand):
    """Collects class names for the node with given id and all of it's child nodes."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to collect class names.
        self.nodeId = nodeId



class requestChildNodes(ChromeCommand):
    """Requests that children of the node with given id are returned to the caller in form of <code>setChildNodes</code> events where not only immediate children are retrieved, but all children down to the specified depth."""

    def __init__(self, nodeId: "NodeId", depth: int=None, pierce: bool=None):
        # Id of the node to get children for.
        self.nodeId = nodeId
        # The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        self.depth = depth
        # Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false).
        self.pierce = pierce



class querySelector(ChromeCommand):
    """Executes <code>querySelector</code> on a given node."""

    def __init__(self, nodeId: "NodeId", selector: str):
        # Id of the node to query upon.
        self.nodeId = nodeId
        # Selector string.
        self.selector = selector



class querySelectorAll(ChromeCommand):
    """Executes <code>querySelectorAll</code> on a given node."""

    def __init__(self, nodeId: "NodeId", selector: str):
        # Id of the node to query upon.
        self.nodeId = nodeId
        # Selector string.
        self.selector = selector



class setNodeName(ChromeCommand):
    """Sets node name for a node with given id."""

    def __init__(self, nodeId: "NodeId", name: str):
        # Id of the node to set name for.
        self.nodeId = nodeId
        # New node's name.
        self.name = name



class setNodeValue(ChromeCommand):
    """Sets node value for a node with given id."""

    def __init__(self, nodeId: "NodeId", value: str):
        # Id of the node to set value for.
        self.nodeId = nodeId
        # New node's value.
        self.value = value



class removeNode(ChromeCommand):
    """Removes node with given id."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to remove.
        self.nodeId = nodeId



class setAttributeValue(ChromeCommand):
    """Sets attribute for an element with given id."""

    def __init__(self, nodeId: "NodeId", name: str, value: str):
        # Id of the element to set attribute for.
        self.nodeId = nodeId
        # Attribute name.
        self.name = name
        # Attribute value.
        self.value = value



class setAttributesAsText(ChromeCommand):
    """Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs."""

    def __init__(self, nodeId: "NodeId", text: str, name: str=None):
        # Id of the element to set attributes for.
        self.nodeId = nodeId
        # Text with a number of attributes. Will parse this text using HTML parser.
        self.text = text
        # Attribute name to replace with new attributes derived from text in case text parsed successfully.
        self.name = name



class removeAttribute(ChromeCommand):
    """Removes attribute with given name from an element with given id."""

    def __init__(self, nodeId: "NodeId", name: str):
        # Id of the element to remove attribute from.
        self.nodeId = nodeId
        # Name of the attribute to remove.
        self.name = name



class getOuterHTML(ChromeCommand):
    """Returns node's HTML markup."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to get markup for.
        self.nodeId = nodeId



class setOuterHTML(ChromeCommand):
    """Sets node HTML markup, returns new node id."""

    def __init__(self, nodeId: "NodeId", outerHTML: str):
        # Id of the node to set markup for.
        self.nodeId = nodeId
        # Outer HTML markup to set.
        self.outerHTML = outerHTML



class performSearch(ChromeCommand):
    """Searches for a given string in the DOM tree. Use <code>getSearchResults</code> to access search results or <code>cancelSearch</code> to end this search session."""

    def __init__(self, query: str, includeUserAgentShadowDOM: bool=None):
        # Plain text or query selector or XPath search query.
        self.query = query
        # True to search in user agent shadow DOM.
        self.includeUserAgentShadowDOM = includeUserAgentShadowDOM



class getSearchResults(ChromeCommand):
    """Returns search results from given <code>fromIndex</code> to given <code>toIndex</code> from the sarch with the given identifier."""

    def __init__(self, searchId: str, fromIndex: int, toIndex: int):
        # Unique search session identifier.
        self.searchId = searchId
        # Start index of the search result to be returned.
        self.fromIndex = fromIndex
        # End index of the search result to be returned.
        self.toIndex = toIndex



class discardSearchResults(ChromeCommand):
    """Discards search results from the session with the given id. <code>getSearchResults</code> should no longer be called for that search."""

    def __init__(self, searchId: str):
        # Unique search session identifier.
        self.searchId = searchId



class requestNode(ChromeCommand):
    """Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of <code>setChildNodes</code> notifications."""

    def __init__(self, objectId: "Runtime.RemoteObjectId"):
        # JavaScript object id to convert into node.
        self.objectId = objectId



class setInspectMode(ChromeCommand):
    """Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection."""

    def __init__(self, mode: "InspectMode", highlightConfig: "HighlightConfig"=None):
        # Set an inspection mode.
        self.mode = mode
        # A descriptor for the highlight appearance of hovered-over nodes. May be omitted if <code>enabled == false</code>.
        self.highlightConfig = highlightConfig



class highlightRect(ChromeCommand):
    """Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport."""

    def __init__(self, x: int, y: int, width: int, height: int, color: "RGBA"=None, outlineColor: "RGBA"=None):
        # X coordinate
        self.x = x
        # Y coordinate
        self.y = y
        # Rectangle width
        self.width = width
        # Rectangle height
        self.height = height
        # The highlight fill color (default: transparent).
        self.color = color
        # The highlight outline color (default: transparent).
        self.outlineColor = outlineColor



class highlightQuad(ChromeCommand):
    """Highlights given quad. Coordinates are absolute with respect to the main frame viewport."""

    def __init__(self, quad: "Quad", color: "RGBA"=None, outlineColor: "RGBA"=None):
        # Quad to highlight
        self.quad = quad
        # The highlight fill color (default: transparent).
        self.color = color
        # The highlight outline color (default: transparent).
        self.outlineColor = outlineColor



class highlightNode(ChromeCommand):
    """Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified."""

    def __init__(self, highlightConfig: "HighlightConfig", nodeId: "NodeId"=None, backendNodeId: "BackendNodeId"=None, objectId: "Runtime.RemoteObjectId"=None):
        # A descriptor for the highlight appearance.
        self.highlightConfig = highlightConfig
        # Identifier of the node to highlight.
        self.nodeId = nodeId
        # Identifier of the backend node to highlight.
        self.backendNodeId = backendNodeId
        # JavaScript object id of the node to be highlighted.
        self.objectId = objectId



class hideHighlight(ChromeCommand):
    """Hides DOM node highlight."""

    def __init__(self): pass

class highlightFrame(ChromeCommand):
    """Highlights owner element of the frame with given id."""

    def __init__(self, frameId: "Page.FrameId", contentColor: "RGBA"=None, contentOutlineColor: "RGBA"=None):
        # Identifier of the frame to highlight.
        self.frameId = frameId
        # The content box highlight fill color (default: transparent).
        self.contentColor = contentColor
        # The content box highlight outline color (default: transparent).
        self.contentOutlineColor = contentOutlineColor



class pushNodeByPathToFrontend(ChromeCommand):
    """Requests that the node is sent to the caller given its path. // FIXME, use XPath"""

    def __init__(self, path: str):
        # Path to node in the proprietary format.
        self.path = path



class pushNodesByBackendIdsToFrontend(ChromeCommand):
    """Requests that a batch of nodes is sent to the caller given their backend node ids."""

    def __init__(self, backendNodeIds: List):
        # The array of backend node ids.
        self.backendNodeIds = backendNodeIds



class setInspectedNode(ChromeCommand):
    """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions)."""

    def __init__(self, nodeId: "NodeId"):
        # DOM node id to be accessible by means of $x command line API.
        self.nodeId = nodeId



class resolveNode(ChromeCommand):
    """Resolves JavaScript node object for given node id."""

    def __init__(self, nodeId: "NodeId", objectGroup: str=None):
        # Id of the node to resolve.
        self.nodeId = nodeId
        # Symbolic group name that can be used to release multiple objects.
        self.objectGroup = objectGroup



class getAttributes(ChromeCommand):
    """Returns attributes for the specified node."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to retrieve attibutes for.
        self.nodeId = nodeId



class copyTo(ChromeCommand):
    """Creates a deep copy of the specified node and places it into the target container before the given anchor."""

    def __init__(self, nodeId: "NodeId", targetNodeId: "NodeId", insertBeforeNodeId: "NodeId"=None):
        # Id of the node to copy.
        self.nodeId = nodeId
        # Id of the element to drop the copy into.
        self.targetNodeId = targetNodeId
        # Drop the copy before this node (if absent, the copy becomes the last child of <code>targetNodeId</code>).
        self.insertBeforeNodeId = insertBeforeNodeId



class moveTo(ChromeCommand):
    """Moves node into the new container, places it before the given anchor."""

    def __init__(self, nodeId: "NodeId", targetNodeId: "NodeId", insertBeforeNodeId: "NodeId"=None):
        # Id of the node to move.
        self.nodeId = nodeId
        # Id of the element to drop the moved node into.
        self.targetNodeId = targetNodeId
        # Drop node before this one (if absent, the moved node becomes the last child of <code>targetNodeId</code>).
        self.insertBeforeNodeId = insertBeforeNodeId



class undo(ChromeCommand):
    """Undoes the last performed action."""

    def __init__(self): pass

class redo(ChromeCommand):
    """Re-does the last undone action."""

    def __init__(self): pass

class markUndoableState(ChromeCommand):
    """Marks last undoable state."""

    def __init__(self): pass

class focus(ChromeCommand):
    """Focuses the given element."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to focus.
        self.nodeId = nodeId



class setFileInputFiles(ChromeCommand):
    """Sets files for the given file input element."""

    def __init__(self, nodeId: "NodeId", files: List):
        # Id of the file input node to set files for.
        self.nodeId = nodeId
        # Array of file paths to set.
        self.files = files



class getBoxModel(ChromeCommand):
    """Returns boxes for the currently selected nodes."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to get box model for.
        self.nodeId = nodeId



class getNodeForLocation(ChromeCommand):
    """Returns node id at given location."""

    def __init__(self, x: int, y: int):
        # X coordinate.
        self.x = x
        # Y coordinate.
        self.y = y



class getRelayoutBoundary(ChromeCommand):
    """Returns the id of the nearest ancestor that is a relayout boundary."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node.
        self.nodeId = nodeId



class getHighlightObjectForTest(ChromeCommand):
    """For testing."""

    def __init__(self, nodeId: "NodeId"):
        # Id of the node to get highlight object for.
        self.nodeId = nodeId



