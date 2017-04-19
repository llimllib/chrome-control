import asyncio
import json
import requests
import websockets
from chrome_control.base import ChromeCommand

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
            res = await ws.recv()

    async def run(self, *tests):
        self.client_queue = list(tests)
        self.ws = await websockets.connect(self.wsurl)
        client_task = asyncio.ensure_future(self._client(self.ws))
        server_task = asyncio.ensure_future(self._server(self.ws))
        while 1:
            pending = [client_task, server_task]
            completed, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED)

    async def close(self):
        self.ws.close()
        self.event_loop.close()

    async def do(self, cmd: ChromeCommand):
        method = f'{cmd.__module__}.{cmd.__class__.__name__}'

        msg = json.dumps({
            "id": self.cmdidx,
            "method": method,
            "params": cmd
        }, cls=ObjectEncoder)

        self.cmdidx += 1

        if self.debug:
            print("sending msg: ", msg)
        # TODO: return a future that lets the returner wait until this is received?
        res = await self.ws.send(msg)

        return res
