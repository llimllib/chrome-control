from enum import Enum
from typing import Any, List

from .base import ChromeCommand

from . import DOM

class Animation:
    """Animation instance."""
    def __init__(self, id: str, name: str, pausedState: bool, playState: str, playbackRate: float, startTime: float, currentTime: float, source: "AnimationEffect", type: str, cssId: str=None):
        # <code>Animation</code>'s id.
        self.id = id
        # <code>Animation</code>'s name.
        self.name = name
        # <code>Animation</code>'s internal paused state.
        self.pausedState = pausedState
        # <code>Animation</code>'s play state.
        self.playState = playState
        # <code>Animation</code>'s playback rate.
        self.playbackRate = playbackRate
        # <code>Animation</code>'s start time.
        self.startTime = startTime
        # <code>Animation</code>'s current time.
        self.currentTime = currentTime
        # <code>Animation</code>'s source animation node.
        self.source = source
        # Animation type of <code>Animation</code>.
        self.type = type
        # A unique ID for <code>Animation</code> representing the sources that triggered this CSS animation/transition.
        self.cssId = cssId

class AnimationEffect:
    """AnimationEffect instance"""
    def __init__(self, delay: float, endDelay: float, iterationStart: float, iterations: float, duration: float, direction: str, fill: str, backendNodeId: "DOM.BackendNodeId", easing: str, keyframesRule: "KeyframesRule"=None):
        # <code>AnimationEffect</code>'s delay.
        self.delay = delay
        # <code>AnimationEffect</code>'s end delay.
        self.endDelay = endDelay
        # <code>AnimationEffect</code>'s iteration start.
        self.iterationStart = iterationStart
        # <code>AnimationEffect</code>'s iterations.
        self.iterations = iterations
        # <code>AnimationEffect</code>'s iteration duration.
        self.duration = duration
        # <code>AnimationEffect</code>'s playback direction.
        self.direction = direction
        # <code>AnimationEffect</code>'s fill mode.
        self.fill = fill
        # <code>AnimationEffect</code>'s target node.
        self.backendNodeId = backendNodeId
        # <code>AnimationEffect</code>'s timing function.
        self.easing = easing
        # <code>AnimationEffect</code>'s keyframes.
        self.keyframesRule = keyframesRule

class KeyframesRule:
    """Keyframes Rule"""
    def __init__(self, keyframes: List, name: str=None):
        # List of animation keyframes.
        self.keyframes = keyframes
        # CSS keyframed animation's name.
        self.name = name

class KeyframeStyle:
    """Keyframe Style"""
    def __init__(self, offset: str, easing: str):
        # Keyframe's time offset.
        self.offset = offset
        # <code>AnimationEffect</code>'s timing function.
        self.easing = easing

class enable(ChromeCommand):
    """Enables animation domain notifications."""

    def __init__(self): pass

class disable(ChromeCommand):
    """Disables animation domain notifications."""

    def __init__(self): pass

class getPlaybackRate(ChromeCommand):
    """Gets the playback rate of the document timeline."""

    def __init__(self): pass

class setPlaybackRate(ChromeCommand):
    """Sets the playback rate of the document timeline."""

    def __init__(self, playbackRate: float):
        # Playback rate for animations on page
        self.playbackRate = playbackRate



class getCurrentTime(ChromeCommand):
    """Returns the current time of the an animation."""

    def __init__(self, id: str):
        # Id of animation.
        self.id = id



class setPaused(ChromeCommand):
    """Sets the paused state of a set of animations."""

    def __init__(self, animations: List, paused: bool):
        # Animations to set the pause state of.
        self.animations = animations
        # Paused state to set to.
        self.paused = paused



class setTiming(ChromeCommand):
    """Sets the timing of an animation node."""

    def __init__(self, animationId: str, duration: float, delay: float):
        # Animation id.
        self.animationId = animationId
        # Duration of the animation.
        self.duration = duration
        # Delay of the animation.
        self.delay = delay



class seekAnimations(ChromeCommand):
    """Seek a set of animations to a particular time within each animation."""

    def __init__(self, animations: List, currentTime: float):
        # List of animation ids to seek.
        self.animations = animations
        # Set the current time of each animation.
        self.currentTime = currentTime



class releaseAnimations(ChromeCommand):
    """Releases a set of animations to no longer be manipulated."""

    def __init__(self, animations: List):
        # List of animation ids to seek.
        self.animations = animations



class resolveAnimation(ChromeCommand):
    """Gets the remote object of the Animation."""

    def __init__(self, animationId: str):
        # Animation id.
        self.animationId = animationId



