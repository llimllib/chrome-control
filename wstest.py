import asyncio
import json
import requests
import websockets

# enable debugging
import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

async def enable(ws, idx):
    cmd = json.dumps({"id": idx, "method": "Page.enable", "params": {}})
    await ws.send(cmd)
    return await ws.recv()

async def go(ws, idx):
    cmd = json.dumps({
        "id": idx, "method": "Page.navigate",
        "params": {"url": "http://adhocteam.us/our-team"}})
    await ws.send(cmd)
    return await ws.recv()

async def exec_script(ws, idx):
    script = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
    cmd = json.dumps({
        "id": idx, "method": "Runtime.evaluate",
        "params": {"expression": script, "returnByValue": True}})
    return await ws.send(cmd)

async def produce():
    cmd = json.dumps({"id": idx, "method": "Page.enable", "params": {}})
    yield cmd
    cmd = json.dumps({
        "id": idx, "method": "Page.navigate",
        "params": {"url": "http://adhocteam.us/our-team"}})
    yield cmd
    script = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
    cmd = json.dumps({
        "id": idx, "method": "Runtime.evaluate",
        "params": {"expression": script, "returnByValue": True}})
    return cmd

async def handler():
    tab = requests.get("http://localhost:9222/json/new").json()
    tabs = requests.get("http://localhost:9222/json").json()

    # id is actually a command id; if we send a message with id 1, we can wait
    # until we receive a message with id 1 to return to a function.
    idx = 0

    wsurl = tab['webSocketDebuggerUrl']

    async with websockets.connect(wsurl) as ws:
        await enable(ws, idx)
        idx += 1
        await go(ws, idx)
        idx += 1
        while 1:
            res = json.loads(await ws.recv())
            if res.get("method") == "Page.loadEventFired":
                await exec_script(ws, idx)
                idx += 1

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(handler())
finally:
    event_loop.close()
