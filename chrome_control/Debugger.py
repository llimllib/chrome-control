from enum import Enum
from typing import Any, List

from .base import ChromeCommand, ChromeEvent

from . import Runtime

# Breakpoint identifier.
BreakpointId = str

# Call frame identifier.
CallFrameId = str

class Location:
    """Location in the source code."""
    def __init__(self, scriptId: "Runtime.ScriptId", lineNumber: int, columnNumber: int=None):
        # Script identifier as reported in the <code>Debugger.scriptParsed</code>.
        self.scriptId = scriptId
        # Line number in the script (0-based).
        self.lineNumber = lineNumber
        # Column number in the script (0-based).
        self.columnNumber = columnNumber

class ScriptPosition:
    """Location in the source code."""
    def __init__(self, lineNumber: int, columnNumber: int):
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

class CallFrame:
    """JavaScript call frame. Array of call frames form the call stack."""
    def __init__(self, callFrameId: "CallFrameId", functionName: str, location: "Location", scopeChain: List, this: "Runtime.RemoteObject", functionLocation: "Location"=None, returnValue: "Runtime.RemoteObject"=None):
        # Call frame identifier. This identifier is only valid while the virtual machine is paused.
        self.callFrameId = callFrameId
        # Name of the JavaScript function called on this call frame.
        self.functionName = functionName
        # Location in the source code.
        self.location = location
        # Scope chain for this call frame.
        self.scopeChain = scopeChain
        # <code>this</code> object for this call frame.
        self.this = this
        # Location in the source code.
        self.functionLocation = functionLocation
        # The value being returned, if the function is at return point.
        self.returnValue = returnValue

class Scope:
    """Scope description."""
    def __init__(self, type: str, object: "Runtime.RemoteObject", name: str=None, startLocation: "Location"=None, endLocation: "Location"=None):
        # Scope type.
        self.type = type
        # Object representing the scope. For <code>global</code> and <code>with</code> scopes it represents the actual object; for the rest of the scopes, it is artificial transient object enumerating scope variables as its properties.
        self.object = object
        self.name = name
        # Location in the source code where scope starts
        self.startLocation = startLocation
        # Location in the source code where scope ends
        self.endLocation = endLocation

class SearchMatch:
    """Search match for resource."""
    def __init__(self, lineNumber: float, lineContent: str):
        # Line number in resource content.
        self.lineNumber = lineNumber
        # Line with match content.
        self.lineContent = lineContent

class enable(ChromeCommand):
    """Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables debugger for given page."""

    def __init__(self): pass

class setBreakpointsActive(ChromeCommand):
    """Activates / deactivates all breakpoints on the page."""

    def __init__(self, active: bool):
        # New value for breakpoints active state.
        self.active = active



class setSkipAllPauses(ChromeCommand):
    """Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc)."""

    def __init__(self, skip: bool):
        # New value for skip pauses state.
        self.skip = skip



class setBreakpointByUrl(ChromeCommand):
    """Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in <code>locations</code> property. Further matching script parsing will result in subsequent <code>breakpointResolved</code> events issued. This logical breakpoint will survive page reloads."""

    def __init__(self, lineNumber: int, url: str=None, urlRegex: str=None, columnNumber: int=None, condition: str=None):
        # Line number to set breakpoint at.
        self.lineNumber = lineNumber
        # URL of the resources to set breakpoint on.
        self.url = url
        # Regex pattern for the URLs of the resources to set breakpoints on. Either <code>url</code> or <code>urlRegex</code> must be specified.
        self.urlRegex = urlRegex
        # Offset in the line to set breakpoint at.
        self.columnNumber = columnNumber
        # Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
        self.condition = condition



class setBreakpoint(ChromeCommand):
    """Sets JavaScript breakpoint at a given location."""

    def __init__(self, location: "Location", condition: str=None):
        # Location to set breakpoint in.
        self.location = location
        # Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
        self.condition = condition



class removeBreakpoint(ChromeCommand):
    """Removes JavaScript breakpoint."""

    def __init__(self, breakpointId: "BreakpointId"):
        self.breakpointId = breakpointId



class getPossibleBreakpoints(ChromeCommand):
    """Returns possible locations for breakpoint. scriptId in start and end range locations should be the same."""

    def __init__(self, start: "Location", end: "Location"=None):
        # Start of range to search possible breakpoint locations in.
        self.start = start
        # End of range to search possible breakpoint locations in (excluding). When not specifed, end of scripts is used as end of range.
        self.end = end



class continueToLocation(ChromeCommand):
    """Continues execution until specific location is reached."""

    def __init__(self, location: "Location"):
        # Location to continue to.
        self.location = location



class stepOver(ChromeCommand):
    """Steps over the statement."""

    def __init__(self): pass

class stepInto(ChromeCommand):
    """Steps into the function call."""

    def __init__(self): pass

class stepOut(ChromeCommand):
    """Steps out of the function call."""

    def __init__(self): pass

class pause(ChromeCommand):
    """Stops on the next JavaScript statement."""

    def __init__(self): pass

class resume(ChromeCommand):
    """Resumes JavaScript execution."""

    def __init__(self): pass

class searchInContent(ChromeCommand):
    """Searches for given string in script content."""

    def __init__(self, scriptId: "Runtime.ScriptId", query: str, caseSensitive: bool=None, isRegex: bool=None):
        # Id of the script to search in.
        self.scriptId = scriptId
        # String to search for.
        self.query = query
        # If true, search is case sensitive.
        self.caseSensitive = caseSensitive
        # If true, treats string parameter as regex.
        self.isRegex = isRegex



class setScriptSource(ChromeCommand):
    """Edits JavaScript source live."""

    def __init__(self, scriptId: "Runtime.ScriptId", scriptSource: str, dryRun: bool=None):
        # Id of the script to edit.
        self.scriptId = scriptId
        # New content of the script.
        self.scriptSource = scriptSource
        #  If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code.
        self.dryRun = dryRun



class restartFrame(ChromeCommand):
    """Restarts particular call frame from the beginning."""

    def __init__(self, callFrameId: "CallFrameId"):
        # Call frame identifier to evaluate on.
        self.callFrameId = callFrameId



class getScriptSource(ChromeCommand):
    """Returns source for the script with given id."""

    def __init__(self, scriptId: "Runtime.ScriptId"):
        # Id of the script to get source for.
        self.scriptId = scriptId



class setPauseOnExceptions(ChromeCommand):
    """Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or no exceptions. Initial pause on exceptions state is <code>none</code>."""

    def __init__(self, state: str):
        # Pause on exceptions mode.
        self.state = state



class evaluateOnCallFrame(ChromeCommand):
    """Evaluates expression on a given call frame."""

    def __init__(self, callFrameId: "CallFrameId", expression: str, objectGroup: str=None, includeCommandLineAPI: bool=None, silent: bool=None, returnByValue: bool=None, generatePreview: bool=None):
        # Call frame identifier to evaluate on.
        self.callFrameId = callFrameId
        # Expression to evaluate.
        self.expression = expression
        # String object group name to put result into (allows rapid releasing resulting object handles using <code>releaseObjectGroup</code>).
        self.objectGroup = objectGroup
        # Specifies whether command line API should be available to the evaluated expression, defaults to false.
        self.includeCommandLineAPI = includeCommandLineAPI
        # In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
        self.silent = silent
        # Whether the result is expected to be a JSON object that should be sent by value.
        self.returnByValue = returnByValue
        # Whether preview should be generated for the result.
        self.generatePreview = generatePreview



class setVariableValue(ChromeCommand):
    """Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually."""

    def __init__(self, scopeNumber: int, variableName: str, newValue: "Runtime.CallArgument", callFrameId: "CallFrameId"):
        # 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually.
        self.scopeNumber = scopeNumber
        # Variable name.
        self.variableName = variableName
        # New variable value.
        self.newValue = newValue
        # Id of callframe that holds variable.
        self.callFrameId = callFrameId



class setAsyncCallStackDepth(ChromeCommand):
    """Enables or disables async call stacks tracking."""

    def __init__(self, maxDepth: int):
        # Maximum depth of async call stacks. Setting to <code>0</code> will effectively disable collecting async call stacks (default).
        self.maxDepth = maxDepth



class setBlackboxPatterns(ChromeCommand):
    """Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""

    def __init__(self, patterns: List):
        # Array of regexps that will be used to check script url for blackbox state.
        self.patterns = patterns



class setBlackboxedRanges(ChromeCommand):
    """Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted."""

    def __init__(self, scriptId: "Runtime.ScriptId", positions: List):
        # Id of the script.
        self.scriptId = scriptId
        self.positions = positions



class scriptParsed(ChromeEvent):
    """Fired when virtual machine parses script. This event is also fired for all known and uncollected scripts upon enabling debugger."""

    def __init__(self, scriptId: "Runtime.ScriptId", url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: "Runtime.ExecutionContextId", hash: str, executionContextAuxData: dict=None, isLiveEdit: bool=None, sourceMapURL: str=None, hasSourceURL: bool=None):
        # Identifier of the script parsed.
        self.scriptId = scriptId
        # URL or name of the script parsed (if any).
        self.url = url
        # Line offset of the script within the resource with given URL (for script tags).
        self.startLine = startLine
        # Column offset of the script within the resource with given URL.
        self.startColumn = startColumn
        # Last line of the script.
        self.endLine = endLine
        # Length of the last line of the script.
        self.endColumn = endColumn
        # Specifies script creation context.
        self.executionContextId = executionContextId
        # Content hash of the script.
        self.hash = hash
        # Embedder-specific auxiliary data.
        self.executionContextAuxData = executionContextAuxData
        # True, if this script is generated as a result of the live edit operation.
        self.isLiveEdit = isLiveEdit
        # URL of source map associated with script (if any).
        self.sourceMapURL = sourceMapURL
        # True, if this script has sourceURL.
        self.hasSourceURL = hasSourceURL



class scriptFailedToParse(ChromeEvent):
    """Fired when virtual machine fails to parse the script."""

    def __init__(self, scriptId: "Runtime.ScriptId", url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: "Runtime.ExecutionContextId", hash: str, executionContextAuxData: dict=None, sourceMapURL: str=None, hasSourceURL: bool=None):
        # Identifier of the script parsed.
        self.scriptId = scriptId
        # URL or name of the script parsed (if any).
        self.url = url
        # Line offset of the script within the resource with given URL (for script tags).
        self.startLine = startLine
        # Column offset of the script within the resource with given URL.
        self.startColumn = startColumn
        # Last line of the script.
        self.endLine = endLine
        # Length of the last line of the script.
        self.endColumn = endColumn
        # Specifies script creation context.
        self.executionContextId = executionContextId
        # Content hash of the script.
        self.hash = hash
        # Embedder-specific auxiliary data.
        self.executionContextAuxData = executionContextAuxData
        # URL of source map associated with script (if any).
        self.sourceMapURL = sourceMapURL
        # True, if this script has sourceURL.
        self.hasSourceURL = hasSourceURL



class breakpointResolved(ChromeEvent):
    """Fired when breakpoint is resolved to an actual script and location."""

    def __init__(self, breakpointId: "BreakpointId", location: "Location"):
        # Breakpoint unique identifier.
        self.breakpointId = breakpointId
        # Actual breakpoint location.
        self.location = location



class paused(ChromeEvent):
    """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""

    def __init__(self, callFrames: List, reason: str, data: dict=None, hitBreakpoints: List=None, asyncStackTrace: "Runtime.StackTrace"=None):
        # Call stack the virtual machine stopped on.
        self.callFrames = callFrames
        # Pause reason.
        self.reason = reason
        # Object containing break-specific auxiliary properties.
        self.data = data
        # Hit breakpoints IDs
        self.hitBreakpoints = hitBreakpoints
        # Async stack trace, if any.
        self.asyncStackTrace = asyncStackTrace



class resumed(ChromeEvent):
    """Fired when the virtual machine resumed execution."""

    def __init__(self): pass

