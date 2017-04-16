import json
import requests
import websocket
from base import ChromeCommand

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (str, int, float, list, bool, dict)):
            return json.JSONEncoder.default(self, obj)
        attrs = [x for x in dir(obj) if not x.startswith('_')]
        return {key: getattr(obj, key) for key in attrs if getattr(obj, key) is not None}

class Chrome:
    def __init__(self):
        # is this documented anywhere? I had to find this from reading node code
        # https://github.com/cyrus-and/chrome-remote-interface/blob/2a85a87574053f4ef48d17ac1ac03b7513310336/lib/devtools.js#L65
        self.tab = requests.get("http://localhost:9222/json/new").json()
        tabs = requests.get("http://localhost:9222/json").json()

        # we need to find the index of our new tab in the tablist, which the API
        # calls the "id", but also doesn't come back in the /new obj. Search the tablist
        # for our tab.
        for i, t in enumerate(tabs):
            if t["id"] == self.tab["id"]:
                self.idx = i
                break
        else: 1/0

        #  * Maybe a tab is the proper unit for the client to deal with? Something like:
        #  with Tab(url) as tab:
        #    tab.do(Page.navigate("http://bananas.com"))
        #    tab.do(Runtime.evaluate("console.log(window.location);", returnByValue=true))
        self.ws = websocket.create_connection(self.tab['webSocketDebuggerUrl'])

    def do(self, cmd: ChromeCommand):
        method = f'{cmd.__module__}.{cmd.__class__.__name__}'
        print("sent: ", json.dumps({
            "id": self.idx,
            "method": method,
            "params": cmd
        }, cls=ObjectEncoder))
        self.ws.send(json.dumps({
            "id": self.idx,
            "method": method,
            "params": cmd,
        }, cls=ObjectEncoder))
        o = json.loads(self.ws.recv())
        print("rcvd: ", o)
        return o
