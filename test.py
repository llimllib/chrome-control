import asyncio
import json
import time

from chrome_control import Chrome, Page, Runtime

# enable websockets debugging
import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# enable asyncio debugging
logger = logging.getLogger('asyncio')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

async def test(tab):
    await tab.do(Page.enable())
    await tab.do(Page.navigate("http://adhocteam.us/our-team"))
    await tab.wait(Page.loadEventFired)
    script = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
    _, fut = await tab.do(Runtime.evaluate(script, returnByValue=True))
    res = json.loads(await fut)
    print(res)

tab = chrome.Tab()
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(tab.run(test))
    print("done")
finally:
    event_loop.close()
