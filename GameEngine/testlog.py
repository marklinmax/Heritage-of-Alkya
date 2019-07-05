from lib import logger
import time


log = logger.Logger("../Log")

log.log("Some text")
log.log("More text in red", "error")
log.log("Even more text in cyan", "info")
log.log("Text in yellow", "warning")

time.sleep(10)
log.stop()
