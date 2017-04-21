import asyncio
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
    # This should only be considered successful if Page.enable() has
    # completed its round-trip to Chrome
    await tab.do(Page.enable())
    await tab.do(Page.navigate("http://adhocteam.us/our-team"))
    await (await tab.wait(Page.loadEventFired))
    script = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
    await tab.do(Runtime.evaluate(script, returnByValue=True))

tab = chrome.Tab()
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(tab.run(test))
    print("done")
finally:
    event_loop.close()
