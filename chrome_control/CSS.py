from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import Page
from . import DOM

StyleSheetId = str

StyleSheetOrigin = Enum("StyleSheetOrigin", "injected user-agent inspector regular")
StyleSheetOrigin.__doc__ = """Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for regular stylesheets."""

class PseudoElementMatches:
    """CSS rule collection for a single pseudo style."""
    def __init__(self, pseudoType: "DOM.PseudoType", matches: List):
        # Pseudo element type.
        self.pseudoType = pseudoType
        # Matches of CSS rules applicable to the pseudo style.
        self.matches = matches

class InheritedStyleEntry:
    """Inherited CSS rule collection from ancestor node."""
    def __init__(self, matchedCSSRules: List, inlineStyle: "CSSStyle"=None):
        # Matches of CSS rules matching the ancestor node in the style inheritance chain.
        self.matchedCSSRules = matchedCSSRules
        # The ancestor node's inline style, if any, in the style inheritance chain.
        self.inlineStyle = inlineStyle

class RuleMatch:
    """Match data for a CSS rule."""
    def __init__(self, rule: "CSSRule", matchingSelectors: List):
        # CSS rule in the match.
        self.rule = rule
        # Matching selector indices in the rule's selectorList selectors (0-based).
        self.matchingSelectors = matchingSelectors

class Value:
    """Data for a simple selector (these are delimited by commas in a selector list)."""
    def __init__(self, text: str, range: "SourceRange"=None):
        # Value text.
        self.text = text
        # Value range in the underlying resource (if available).
        self.range = range

class SelectorList:
    """Selector list data."""
    def __init__(self, selectors: List, text: str):
        # Selectors in the list.
        self.selectors = selectors
        # Rule selector text.
        self.text = text

class CSSStyleSheetHeader:
    """CSS stylesheet metainformation."""
    def __init__(self, styleSheetId: "StyleSheetId", frameId: "Page.FrameId", sourceURL: str, origin: "StyleSheetOrigin", title: str, disabled: bool, isInline: bool, startLine: float, startColumn: float, sourceMapURL: str=None, ownerNode: "DOM.BackendNodeId"=None, hasSourceURL: bool=None):
        # The stylesheet identifier.
        self.styleSheetId = styleSheetId
        # Owner frame identifier.
        self.frameId = frameId
        # Stylesheet resource URL.
        self.sourceURL = sourceURL
        # Stylesheet origin.
        self.origin = origin
        # Stylesheet title.
        self.title = title
        # Denotes whether the stylesheet is disabled.
        self.disabled = disabled
        # Whether this stylesheet is created for STYLE tag by parser. This flag is not set for document.written STYLE tags.
        self.isInline = isInline
        # Line offset of the stylesheet within the resource (zero based).
        self.startLine = startLine
        # Column offset of the stylesheet within the resource (zero based).
        self.startColumn = startColumn
        # URL of source map associated with the stylesheet (if any).
        self.sourceMapURL = sourceMapURL
        # The backend id for the owner node of the stylesheet.
        self.ownerNode = ownerNode
        # Whether the sourceURL field value comes from the sourceURL comment.
        self.hasSourceURL = hasSourceURL

class CSSRule:
    """CSS rule representation."""
    def __init__(self, selectorList: "SelectorList", origin: "StyleSheetOrigin", style: "CSSStyle", styleSheetId: "StyleSheetId"=None, media: List=None):
        # Rule selector data.
        self.selectorList = selectorList
        # Parent stylesheet's origin.
        self.origin = origin
        # Associated style declaration.
        self.style = style
        # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        self.styleSheetId = styleSheetId
        # Media list array (for rules involving media queries). The array enumerates media queries starting with the innermost one, going outwards.
        self.media = media

class RuleUsage:
    """CSS rule usage information."""
    def __init__(self, styleSheetId: "StyleSheetId", range: "SourceRange", used: bool):
        # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        self.styleSheetId = styleSheetId
        # Style declaration range in the enclosing stylesheet (if available).
        self.range = range
        # Indicates whether the rule was actually used by some element in the page.
        self.used = used

class SourceRange:
    """Text range within a resource. All numbers are zero-based."""
    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int):
        # Start line of range.
        self.startLine = startLine
        # Start column of range (inclusive).
        self.startColumn = startColumn
        # End line of range
        self.endLine = endLine
        # End column of range (exclusive).
        self.endColumn = endColumn

class ShorthandEntry:
    def __init__(self, name: str, value: str, important: bool=None):
        # Shorthand name.
        self.name = name
        # Shorthand value.
        self.value = value
        # Whether the property has "!important" annotation (implies <code>false</code> if absent).
        self.important = important

class CSSComputedStyleProperty:
    def __init__(self, name: str, value: str):
        # Computed style property name.
        self.name = name
        # Computed style property value.
        self.value = value

class CSSStyle:
    """CSS style representation."""
    def __init__(self, cssProperties: List, shorthandEntries: List, styleSheetId: "StyleSheetId"=None, cssText: str=None, range: "SourceRange"=None):
        # CSS properties in the style.
        self.cssProperties = cssProperties
        # Computed values for all shorthands found in the style.
        self.shorthandEntries = shorthandEntries
        # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        self.styleSheetId = styleSheetId
        # Style declaration text (if available).
        self.cssText = cssText
        # Style declaration range in the enclosing stylesheet (if available).
        self.range = range

class CSSProperty:
    """CSS property declaration data."""
    def __init__(self, name: str, value: str, important: bool=None, implicit: bool=None, text: str=None, parsedOk: bool=None, disabled: bool=None, range: "SourceRange"=None):
        # The property name.
        self.name = name
        # The property value.
        self.value = value
        # Whether the property has "!important" annotation (implies <code>false</code> if absent).
        self.important = important
        # Whether the property is implicit (implies <code>false</code> if absent).
        self.implicit = implicit
        # The full property text as specified in the style.
        self.text = text
        # Whether the property is understood by the browser (implies <code>true</code> if absent).
        self.parsedOk = parsedOk
        # Whether the property is disabled by the user (present for source-based properties only).
        self.disabled = disabled
        # The entire property range in the enclosing style declaration (if available).
        self.range = range

class CSSMedia:
    """CSS media rule descriptor."""
    def __init__(self, text: str, source: str, sourceURL: str=None, range: "SourceRange"=None, styleSheetId: "StyleSheetId"=None, mediaList: List=None):
        # Media query text.
        self.text = text
        # Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline stylesheet's STYLE tag.
        self.source = source
        # URL of the document containing the media query description.
        self.sourceURL = sourceURL
        # The associated rule (@media or @import) header range in the enclosing stylesheet (if available).
        self.range = range
        # Identifier of the stylesheet containing this object (if exists).
        self.styleSheetId = styleSheetId
        # Array of media queries.
        self.mediaList = mediaList

class MediaQuery:
    """Media query descriptor."""
    def __init__(self, expressions: List, active: bool):
        # Array of media query expressions.
        self.expressions = expressions
        # Whether the media query condition is satisfied.
        self.active = active

class MediaQueryExpression:
    """Media query expression descriptor."""
    def __init__(self, value: float, unit: str, feature: str, valueRange: "SourceRange"=None, computedLength: float=None):
        # Media query expression value.
        self.value = value
        # Media query expression units.
        self.unit = unit
        # Media query expression feature.
        self.feature = feature
        # The associated range of the value text in the enclosing stylesheet (if available).
        self.valueRange = valueRange
        # Computed length of media query expression (if applicable).
        self.computedLength = computedLength

class PlatformFontUsage:
    """Information about amount of glyphs that were rendered with given font."""
    def __init__(self, familyName: str, isCustomFont: bool, glyphCount: float):
        # Font's family name reported by platform.
        self.familyName = familyName
        # Indicates if the font was downloaded or resolved locally.
        self.isCustomFont = isCustomFont
        # Amount of glyphs that were rendered with this font.
        self.glyphCount = glyphCount

class CSSKeyframesRule:
    """CSS keyframes rule representation."""
    def __init__(self, animationName: "Value", keyframes: List):
        # Animation name.
        self.animationName = animationName
        # List of keyframes.
        self.keyframes = keyframes

class CSSKeyframeRule:
    """CSS keyframe rule representation."""
    def __init__(self, origin: "StyleSheetOrigin", keyText: "Value", style: "CSSStyle", styleSheetId: "StyleSheetId"=None):
        # Parent stylesheet's origin.
        self.origin = origin
        # Associated key text.
        self.keyText = keyText
        # Associated style declaration.
        self.style = style
        # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from.
        self.styleSheetId = styleSheetId

class StyleDeclarationEdit:
    """A descriptor of operation to mutate style declaration text."""
    def __init__(self, styleSheetId: "StyleSheetId", range: "SourceRange", text: str):
        # The css style sheet identifier.
        self.styleSheetId = styleSheetId
        # The range of the style text in the enclosing stylesheet.
        self.range = range
        # New style text.
        self.text = text

class InlineTextBox:
    """Details of post layout rendered text positions. The exact layout should not be regarded as stable and may change between versions."""
    def __init__(self, boundingBox: "DOM.Rect", startCharacterIndex: int, numCharacters: int):
        # The absolute position bounding box.
        self.boundingBox = boundingBox
        # The starting index in characters, for this post layout textbox substring.
        self.startCharacterIndex = startCharacterIndex
        # The number of characters in this post layout textbox substring.
        self.numCharacters = numCharacters

class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""
    def __init__(self, nodeId: "DOM.NodeId", boundingBox: "DOM.Rect", layoutText: str=None, inlineTextNodes: List=None, styleIndex: int=None):
        # The id of the related DOM node matching one from DOM.GetDocument.
        self.nodeId = nodeId
        # The absolute position bounding box.
        self.boundingBox = boundingBox
        # Contents of the LayoutText if any
        self.layoutText = layoutText
        # The post layout inline text nodes, if any.
        self.inlineTextNodes = inlineTextNodes
        # Index into the computedStyles array returned by getLayoutTreeAndStyles.
        self.styleIndex = styleIndex

class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request whitelist."""
    def __init__(self, properties: List):
        self.properties = properties

class enable(ChromeCommand):
    """Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables the CSS agent for the given page."""

    def __init__(self): pass

class getMatchedStylesForNode(ChromeCommand):
    """Returns requested styles for a DOM node identified by <code>nodeId</code>."""

    def __init__(self, nodeId: "DOM.NodeId"):
        self.nodeId = nodeId



class getInlineStylesForNode(ChromeCommand):
    """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by <code>nodeId</code>."""

    def __init__(self, nodeId: "DOM.NodeId"):
        self.nodeId = nodeId



class getComputedStyleForNode(ChromeCommand):
    """Returns the computed style for a DOM node identified by <code>nodeId</code>."""

    def __init__(self, nodeId: "DOM.NodeId"):
        self.nodeId = nodeId



class getPlatformFontsForNode(ChromeCommand):
    """Requests information about platform fonts which we used to render child TextNodes in the given node."""

    def __init__(self, nodeId: "DOM.NodeId"):
        self.nodeId = nodeId



class getStyleSheetText(ChromeCommand):
    """Returns the current textual content and the URL for a stylesheet."""

    def __init__(self, styleSheetId: "StyleSheetId"):
        self.styleSheetId = styleSheetId



class collectClassNames(ChromeCommand):
    """Returns all class names from specified stylesheet."""

    def __init__(self, styleSheetId: "StyleSheetId"):
        self.styleSheetId = styleSheetId



class setStyleSheetText(ChromeCommand):
    """Sets the new stylesheet text."""

    def __init__(self, styleSheetId: "StyleSheetId", text: str):
        self.styleSheetId = styleSheetId
        self.text = text



class setRuleSelector(ChromeCommand):
    """Modifies the rule selector."""

    def __init__(self, styleSheetId: "StyleSheetId", range: "SourceRange", selector: str):
        self.styleSheetId = styleSheetId
        self.range = range
        self.selector = selector



class setKeyframeKey(ChromeCommand):
    """Modifies the keyframe rule key text."""

    def __init__(self, styleSheetId: "StyleSheetId", range: "SourceRange", keyText: str):
        self.styleSheetId = styleSheetId
        self.range = range
        self.keyText = keyText



class setStyleTexts(ChromeCommand):
    """Applies specified style edits one after another in the given order."""

    def __init__(self, edits: List):
        self.edits = edits



class setMediaText(ChromeCommand):
    """Modifies the rule selector."""

    def __init__(self, styleSheetId: "StyleSheetId", range: "SourceRange", text: str):
        self.styleSheetId = styleSheetId
        self.range = range
        self.text = text



class createStyleSheet(ChromeCommand):
    """Creates a new special "via-inspector" stylesheet in the frame with given <code>frameId</code>."""

    def __init__(self, frameId: "Page.FrameId"):
        # Identifier of the frame where "via-inspector" stylesheet should be created.
        self.frameId = frameId



class addRule(ChromeCommand):
    """Inserts a new rule with the given <code>ruleText</code> in a stylesheet with given <code>styleSheetId</code>, at the position specified by <code>location</code>."""

    def __init__(self, styleSheetId: "StyleSheetId", ruleText: str, location: "SourceRange"):
        # The css style sheet identifier where a new rule should be inserted.
        self.styleSheetId = styleSheetId
        # The text of a new rule.
        self.ruleText = ruleText
        # Text position of a new rule in the target style sheet.
        self.location = location



class forcePseudoState(ChromeCommand):
    """Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser."""

    def __init__(self, nodeId: "DOM.NodeId", forcedPseudoClasses: List):
        # The element id for which to force the pseudo state.
        self.nodeId = nodeId
        # Element pseudo classes to force when computing the element's style.
        self.forcedPseudoClasses = forcedPseudoClasses



class getMediaQueries(ChromeCommand):
    """Returns all media queries parsed by the rendering engine."""

    def __init__(self): pass

class setEffectivePropertyValueForNode(ChromeCommand):
    """Find a rule with the given active property for the given node and set the new value for this property"""

    def __init__(self, nodeId: "DOM.NodeId", propertyName: str, value: str):
        # The element id for which to set property.
        self.nodeId = nodeId
        self.propertyName = propertyName
        self.value = value



class getBackgroundColors(ChromeCommand):
    def __init__(self, nodeId: "DOM.NodeId"):
        # Id of the node to get background colors for.
        self.nodeId = nodeId



class getLayoutTreeAndStyles(ChromeCommand):
    """For the main document and any content documents, return the LayoutTreeNodes and a whitelisted subset of the computed style. It only returns pushed nodes, on way to pull all nodes is to call DOM.getDocument with a depth of -1."""

    def __init__(self, computedStyleWhitelist: List):
        # Whitelist of computed styles to return.
        self.computedStyleWhitelist = computedStyleWhitelist



class startRuleUsageTracking(ChromeCommand):
    """Enables the selector recording."""

    def __init__(self): pass

class stopRuleUsageTracking(ChromeCommand):
    """The list of rules with an indication of whether these were used"""

    def __init__(self): pass

class mediaQueryResultChanged(ChromeEvent):
    """Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features."""

    def __init__(self): pass

class fontsUpdated(ChromeEvent):
    """Fires whenever a web font gets loaded."""

    def __init__(self): pass

class styleSheetChanged(ChromeEvent):
    """Fired whenever a stylesheet is changed as a result of the client operation."""

    def __init__(self, styleSheetId: "StyleSheetId"):
        self.styleSheetId = styleSheetId



class styleSheetAdded(ChromeEvent):
    """Fired whenever an active document stylesheet is added."""

    def __init__(self, header: "CSSStyleSheetHeader"):
        # Added stylesheet metainfo.
        self.header = header



class styleSheetRemoved(ChromeEvent):
    """Fired whenever an active document stylesheet is removed."""

    def __init__(self, styleSheetId: "StyleSheetId"):
        # Identifier of the removed stylesheet.
        self.styleSheetId = styleSheetId



