import asyncio
import json
import requests
import websockets

# enable websockets debugging
import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# enable asyncio debugging
logging.getLogger('asyncio').setLevel(logging.DEBUG)

async def server(ws):
    while 1:
        res = await ws.recv()

async def client(ws):
    idx = 0
    cmd = json.dumps({"id": idx, "method": "Page.enable", "params": {}})
    res = await ws.send(cmd)

    idx += 1
    cmd = json.dumps({
        "id": idx, "method": "Page.navigate",
        "params": {"url": "http://adhocteam.us/our-team"}})
    res = await ws.send(cmd)

    idx += 1
    script = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
    cmd = json.dumps({
        "id": idx, "method": "Runtime.evaluate",
        "params": {"expression": script, "returnByValue": True}})
    res = await ws.send(cmd)

async def handler():
    tab = requests.get("http://localhost:9222/json/new").json()
    tabs = requests.get("http://localhost:9222/json").json()

    # id is actually a command id; if we send a message with id 1, we can wait
    # until we receive a message with id 1 to return to a function.
    idx = 0

    wsurl = tab['webSocketDebuggerUrl']

    async with websockets.connect(wsurl) as ws:
        client_task = asyncio.ensure_future(client(ws))
        server_task = asyncio.ensure_future(server(ws))
        while 1:
            pending = [client_task, server_task]
            completed, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED)

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(handler())
finally:
    print("closing event loop")
    event_loop.close()
