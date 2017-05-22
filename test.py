import time

from chrome_control import Chrome, Page, Runtime

c = Chrome()
c.do(Page.navigate("http://adhocteam.us/our-team"))

# if we don't wait for the page to load, then we can run the script too
# early and get an empty array.
#
# TODO a great next step would be to figure out how to receive pageLoad
#      event from Page and only run the command at that time
time.sleep(2)

cmd = '[].map.call(document.querySelectorAll("h3.centered"), n => n.textContent)'
c.do(Runtime.evaluate(cmd, returnByValue=True))
