from enum import Enum
from typing import Any, List

from .base import ChromeCommand


# Unique script identifier.
ScriptId = str

# Unique object identifier.
RemoteObjectId = str

UnserializableValue = Enum("UnserializableValue", "Infinity NaN -Infinity -0")
UnserializableValue.__doc__ = """Primitive value which cannot be JSON-stringified."""

class RemoteObject:
    """Mirror object referencing original JavaScript object."""
    def __init__(self, type: str, subtype: str=None, className: str=None, value: Any=None, unserializableValue: "UnserializableValue"=None, description: str=None, objectId: "RemoteObjectId"=None, preview: "ObjectPreview"=None, customPreview: "CustomPreview"=None):
        # Object type.
        self.type = type
        # Object subtype hint. Specified for <code>object</code> type values only.
        self.subtype = subtype
        # Object class (constructor) name. Specified for <code>object</code> type values only.
        self.className = className
        # Remote object value in case of primitive values or JSON values (if it was requested).
        self.value = value
        # Primitive value which can not be JSON-stringified does not have <code>value</code>, but gets this property.
        self.unserializableValue = unserializableValue
        # String representation of the object.
        self.description = description
        # Unique object identifier (for non-primitive values).
        self.objectId = objectId
        # Preview containing abbreviated property values. Specified for <code>object</code> type values only.
        self.preview = preview
        self.customPreview = customPreview

class CustomPreview:
    def __init__(self, header: str, hasBody: bool, formatterObjectId: "RemoteObjectId", bindRemoteObjectFunctionId: "RemoteObjectId", configObjectId: "RemoteObjectId"=None):
        self.header = header
        self.hasBody = hasBody
        self.formatterObjectId = formatterObjectId
        self.bindRemoteObjectFunctionId = bindRemoteObjectFunctionId
        self.configObjectId = configObjectId

class ObjectPreview:
    """Object containing abbreviated remote object value."""
    def __init__(self, type: str, overflow: bool, properties: List, subtype: str=None, description: str=None, entries: List=None):
        # Object type.
        self.type = type
        # True iff some of the properties or entries of the original object did not fit.
        self.overflow = overflow
        # List of the properties.
        self.properties = properties
        # Object subtype hint. Specified for <code>object</code> type values only.
        self.subtype = subtype
        # String representation of the object.
        self.description = description
        # List of the entries. Specified for <code>map</code> and <code>set</code> subtype values only.
        self.entries = entries

class PropertyPreview:
    def __init__(self, name: str, type: str, value: str=None, valuePreview: "ObjectPreview"=None, subtype: str=None):
        # Property name.
        self.name = name
        # Object type. Accessor means that the property itself is an accessor property.
        self.type = type
        # User-friendly property value string.
        self.value = value
        # Nested value preview.
        self.valuePreview = valuePreview
        # Object subtype hint. Specified for <code>object</code> type values only.
        self.subtype = subtype

class EntryPreview:
    def __init__(self, value: "ObjectPreview", key: "ObjectPreview"=None):
        # Preview of the value.
        self.value = value
        # Preview of the key. Specified for map-like collection entries.
        self.key = key

class PropertyDescriptor:
    """Object property descriptor."""
    def __init__(self, name: str, configurable: bool, enumerable: bool, value: "RemoteObject"=None, writable: bool=None, get: "RemoteObject"=None, set: "RemoteObject"=None, wasThrown: bool=None, isOwn: bool=None, symbol: "RemoteObject"=None):
        # Property name or symbol description.
        self.name = name
        # True if the type of this property descriptor may be changed and if the property may be deleted from the corresponding object.
        self.configurable = configurable
        # True if this property shows up during enumeration of the properties on the corresponding object.
        self.enumerable = enumerable
        # The value associated with the property.
        self.value = value
        # True if the value associated with the property may be changed (data descriptors only).
        self.writable = writable
        # A function which serves as a getter for the property, or <code>undefined</code> if there is no getter (accessor descriptors only).
        self.get = get
        # A function which serves as a setter for the property, or <code>undefined</code> if there is no setter (accessor descriptors only).
        self.set = set
        # True if the result was thrown during the evaluation.
        self.wasThrown = wasThrown
        # True if the property is owned for the object.
        self.isOwn = isOwn
        # Property symbol object, if the property is of the <code>symbol</code> type.
        self.symbol = symbol

class InternalPropertyDescriptor:
    """Object internal property descriptor. This property isn't normally visible in JavaScript code."""
    def __init__(self, name: str, value: "RemoteObject"=None):
        # Conventional property name.
        self.name = name
        # The value associated with the property.
        self.value = value

class CallArgument:
    """Represents function call argument. Either remote object id <code>objectId</code>, primitive <code>value</code>, unserializable primitive value or neither of (for undefined) them should be specified."""
    def __init__(self, value: Any=None, unserializableValue: "UnserializableValue"=None, objectId: "RemoteObjectId"=None):
        # Primitive value.
        self.value = value
        # Primitive value which can not be JSON-stringified.
        self.unserializableValue = unserializableValue
        # Remote object handle.
        self.objectId = objectId

# Id of an execution context.
ExecutionContextId = int

class ExecutionContextDescription:
    """Description of an isolated world."""
    def __init__(self, id: "ExecutionContextId", origin: str, name: str, auxData: dict=None):
        # Unique id of the execution context. It can be used to specify in which execution context script evaluation should be performed.
        self.id = id
        # Execution context origin.
        self.origin = origin
        # Human readable name describing given context.
        self.name = name
        # Embedder-specific auxiliary data.
        self.auxData = auxData

class ExceptionDetails:
    """Detailed information about exception (or error) that was thrown during script compilation or execution."""
    def __init__(self, exceptionId: int, text: str, lineNumber: int, columnNumber: int, scriptId: "ScriptId"=None, url: str=None, stackTrace: "StackTrace"=None, exception: "RemoteObject"=None, executionContextId: "ExecutionContextId"=None):
        # Exception id.
        self.exceptionId = exceptionId
        # Exception text, which should be used together with exception object when available.
        self.text = text
        # Line number of the exception location (0-based).
        self.lineNumber = lineNumber
        # Column number of the exception location (0-based).
        self.columnNumber = columnNumber
        # Script ID of the exception location.
        self.scriptId = scriptId
        # URL of the exception location, to be used when the script was not reported.
        self.url = url
        # JavaScript stack trace if available.
        self.stackTrace = stackTrace
        # Exception object if available.
        self.exception = exception
        # Identifier of the context where exception happened.
        self.executionContextId = executionContextId

# Number of milliseconds since epoch.
Timestamp = float

class CallFrame:
    """Stack entry for runtime errors and assertions."""
    def __init__(self, functionName: str, scriptId: "ScriptId", url: str, lineNumber: int, columnNumber: int):
        # JavaScript function name.
        self.functionName = functionName
        # JavaScript script id.
        self.scriptId = scriptId
        # JavaScript script name or url.
        self.url = url
        # JavaScript script line number (0-based).
        self.lineNumber = lineNumber
        # JavaScript script column number (0-based).
        self.columnNumber = columnNumber

class StackTrace:
    """Call frames for assertions or error messages."""
    def __init__(self, callFrames: List, description: str=None, parent: "StackTrace"=None):
        # JavaScript function name.
        self.callFrames = callFrames
        # String label of this stack trace. For async traces this may be a name of the function that initiated the async call.
        self.description = description
        # Asynchronous JavaScript stack trace that preceded this stack, if available.
        self.parent = parent

class evaluate(ChromeCommand):
    """Evaluates expression on global object."""

    def __init__(self, expression: str, objectGroup: str=None, includeCommandLineAPI: bool=None, silent: bool=None, contextId: "ExecutionContextId"=None, returnByValue: bool=None, generatePreview: bool=None, userGesture: bool=None, awaitPromise: bool=None):
        # Expression to evaluate.
        self.expression = expression
        # Symbolic group name that can be used to release multiple objects.
        self.objectGroup = objectGroup
        # Determines whether Command Line API should be available during the evaluation.
        self.includeCommandLineAPI = includeCommandLineAPI
        # In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
        self.silent = silent
        # Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        self.contextId = contextId
        # Whether the result is expected to be a JSON object that should be sent by value.
        self.returnByValue = returnByValue
        # Whether preview should be generated for the result.
        self.generatePreview = generatePreview
        # Whether execution should be treated as initiated by user in the UI.
        self.userGesture = userGesture
        # Whether execution should wait for promise to be resolved. If the result of evaluation is not a Promise, it's considered to be an error.
        self.awaitPromise = awaitPromise



class awaitPromise(ChromeCommand):
    """Add handler to promise with given promise object id."""

    def __init__(self, promiseObjectId: "RemoteObjectId", returnByValue: bool=None, generatePreview: bool=None):
        # Identifier of the promise.
        self.promiseObjectId = promiseObjectId
        # Whether the result is expected to be a JSON object that should be sent by value.
        self.returnByValue = returnByValue
        # Whether preview should be generated for the result.
        self.generatePreview = generatePreview



class callFunctionOn(ChromeCommand):
    """Calls function with given declaration on the given object. Object group of the result is inherited from the target object."""

    def __init__(self, objectId: "RemoteObjectId", functionDeclaration: str, arguments: List=None, silent: bool=None, returnByValue: bool=None, generatePreview: bool=None, userGesture: bool=None, awaitPromise: bool=None):
        # Identifier of the object to call function on.
        self.objectId = objectId
        # Declaration of the function to call.
        self.functionDeclaration = functionDeclaration
        # Call arguments. All call arguments must belong to the same JavaScript world as the target object.
        self.arguments = arguments
        # In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
        self.silent = silent
        # Whether the result is expected to be a JSON object which should be sent by value.
        self.returnByValue = returnByValue
        # Whether preview should be generated for the result.
        self.generatePreview = generatePreview
        # Whether execution should be treated as initiated by user in the UI.
        self.userGesture = userGesture
        # Whether execution should wait for promise to be resolved. If the result of evaluation is not a Promise, it's considered to be an error.
        self.awaitPromise = awaitPromise



class getProperties(ChromeCommand):
    """Returns properties of a given object. Object group of the result is inherited from the target object."""

    def __init__(self, objectId: "RemoteObjectId", ownProperties: bool=None, accessorPropertiesOnly: bool=None, generatePreview: bool=None):
        # Identifier of the object to return properties for.
        self.objectId = objectId
        # If true, returns properties belonging only to the element itself, not to its prototype chain.
        self.ownProperties = ownProperties
        # If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
        self.accessorPropertiesOnly = accessorPropertiesOnly
        # Whether preview should be generated for the results.
        self.generatePreview = generatePreview



class releaseObject(ChromeCommand):
    """Releases remote object with given id."""

    def __init__(self, objectId: "RemoteObjectId"):
        # Identifier of the object to release.
        self.objectId = objectId



class releaseObjectGroup(ChromeCommand):
    """Releases all remote objects that belong to a given group."""

    def __init__(self, objectGroup: str):
        # Symbolic object group name.
        self.objectGroup = objectGroup



class runIfWaitingForDebugger(ChromeCommand):
    """Tells inspected instance to run if it was waiting for debugger to attach."""

    def __init__(self): pass

class enable(ChromeCommand):
    """Enables reporting of execution contexts creation by means of <code>executionContextCreated</code> event. When the reporting gets enabled the event will be sent immediately for each existing execution context."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables reporting of execution contexts creation."""

    def __init__(self): pass

class discardConsoleEntries(ChromeCommand):
    """Discards collected exceptions and console API calls."""

    def __init__(self): pass

class setCustomObjectFormatterEnabled(ChromeCommand):
    def __init__(self, enabled: bool):
        self.enabled = enabled



class compileScript(ChromeCommand):
    """Compiles expression."""

    def __init__(self, expression: str, sourceURL: str, persistScript: bool, executionContextId: "ExecutionContextId"=None):
        # Expression to compile.
        self.expression = expression
        # Source url to be set for the script.
        self.sourceURL = sourceURL
        # Specifies whether the compiled script should be persisted.
        self.persistScript = persistScript
        # Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        self.executionContextId = executionContextId



class runScript(ChromeCommand):
    """Runs script with given id in a given context."""

    def __init__(self, scriptId: "ScriptId", executionContextId: "ExecutionContextId"=None, objectGroup: str=None, silent: bool=None, includeCommandLineAPI: bool=None, returnByValue: bool=None, generatePreview: bool=None, awaitPromise: bool=None):
        # Id of the script to run.
        self.scriptId = scriptId
        # Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        self.executionContextId = executionContextId
        # Symbolic group name that can be used to release multiple objects.
        self.objectGroup = objectGroup
        # In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
        self.silent = silent
        # Determines whether Command Line API should be available during the evaluation.
        self.includeCommandLineAPI = includeCommandLineAPI
        # Whether the result is expected to be a JSON object which should be sent by value.
        self.returnByValue = returnByValue
        # Whether preview should be generated for the result.
        self.generatePreview = generatePreview
        # Whether execution should wait for promise to be resolved. If the result of evaluation is not a Promise, it's considered to be an error.
        self.awaitPromise = awaitPromise



