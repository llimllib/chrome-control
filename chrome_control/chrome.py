import asyncio
import json
import requests
import websockets
from .base import ChromeCommand, ChromeEvent

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (str, int, float, list, bool, dict)):
            return json.JSONEncoder.default(self, obj)
        attrs = [x for x in dir(obj) if not x.startswith('_')]
        return {key: getattr(obj, key) for key in attrs if getattr(obj, key) is not None}

class Tab:
    def __init__(self, debug=1):
        self.debug = debug
        self.ws = None
        self.client_queue = []
        self.server_queue = []
        self.cmdidx = 0
        self.commands = {}
        self.event_listeners = {}

        # is this documented anywhere? I had to find this from reading node code
        # https://github.com/cyrus-and/chrome-remote-interface/blob/2a85a87574053f4ef48d17ac1ac03b7513310336/lib/devtools.js#L65
        #
        # there appears to be an endpoint that's equivalent to /json/new, at:
        # https://chromedevtools.github.io/debugger-protocol-viewer/tot/Target/#method-createTarget
        #
        # update, no this is not documented anywhere:
        # https://github.com/GoogleChrome/devtools-docs/issues/67#issuecomment-37675331
        tab = requests.get("http://localhost:9222/json/new").json()

        self.wsurl = tab['webSocketDebuggerUrl']

    async def _client(self, ws):
        if len(self.client_queue):
            await self.client_queue.pop()(self)

    async def _server(self, ws):
        while 1:
            res = json.loads(await ws.recv())
            # We'll assume that if there's an id in res, that it's a command response.
            # if not, we'll assume it's an event
            if "id" in res:
                fut = self.commands.get(res["id"])
                if fut:
                    print(f'resolving {res["id"]}')
                    fut.set_result(res)
            else:
                if res["method"] in self.event_listeners:
                    self.event_listeners[res["method"]].set_result(res)
                    print("fired future", self.event_listeners[res["method"]])

    async def run(self, *tests):
        self.client_queue = list(tests)
        self.ws = await websockets.connect(self.wsurl)
        client_task = asyncio.ensure_future(self._client(self.ws))
        server_task = asyncio.ensure_future(self._server(self.ws))
        while 1:
            # XXX: eventually we will want this to finish, but for now
            #      just run it forever
            pending = [client_task, server_task]
            completed, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED)

    def wait(self, evt: type):
        if not isinstance(evt, type) or not ChromeEvent in evt.mro():
            raise TypeError("the object to wait on must be a ChromeEvent type, not an instance")

        evtname = f'{evt.__module__}.{evt.__name__}'
        # XXX: can multiple tasks be listening on the same future? I'm assuming yes
        #      but I have no idea
        if evtname in self.event_listeners:
            return self.event_listeners[evtname]
        else:
            fut = asyncio.Future()
            self.event_listeners[evtname] = fut
            print("returning future")
            return fut

    async def do(self, cmd: ChromeCommand):
        method = f'{cmd.__module__}.{cmd.__class__.__name__}'

        msg = json.dumps({
            "id": self.cmdidx,
            "method": method,
            "params": cmd
        }, cls=ObjectEncoder)

        fut = asyncio.Future()
        self.commands[self.cmdidx] = fut

        self.cmdidx += 1

        if self.debug:
            print("sending msg: ", msg)

        res = await self.ws.send(msg)

        return (res, fut)
